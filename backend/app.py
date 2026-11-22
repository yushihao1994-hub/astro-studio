import os
import re
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request
from deepseek_client import analyze_with_deepseek, generate_full_report, analyze_tieshan_profile, DeepSeekNotConfigured, DeepSeekError
from flask_cors import CORS
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import swisseph as swe
from tieshan import calculate_tieshan_pillars
from bazi_details import derive_bazi_details
from tieshan_time import derive_eight_ke
from tieshan_classic import derive_classic_reference, derive_body_life_palaces
from tieshan_engine import build_tieshan_foundation
from tieshan_kunji_index import get_kunji_glossary
from tieshan_collection_catalog import get_collection_sample, get_group_index, get_collection_progress, get_collection_branch_group_index
from chinese_calendar import lunar_month_options, lunar_to_solar, solar_to_lunar

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

SIGNS = ["白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
         "天秤座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座"]
PLANETS = [
    ("太阳", swe.SUN), ("月亮", swe.MOON), ("水星", swe.MERCURY),
    ("金星", swe.VENUS), ("火星", swe.MARS), ("木星", swe.JUPITER),
    ("土星", swe.SATURN), ("天王星", swe.URANUS),
    ("海王星", swe.NEPTUNE), ("冥王星", swe.PLUTO),
    ("北交点", swe.TRUE_NODE)
]
ASPECTS = [(0, "合相"), (60, "六分相"), (90, "四分相"),
           (120, "三分相"), (180, "冲相")]


def sign_position(longitude):
    value = longitude % 360
    sign_index = int(value // 30)
    within = value % 30
    degree = int(within)
    minute_float = (within - degree) * 60
    minute = int(minute_float)
    second = round((minute_float - minute) * 60)
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        degree += 1
    return {
        "sign": SIGNS[sign_index],
        "degree": degree,
        "minute": minute,
        "second": second,
        "longitude": round(value, 6)
    }


def angular_distance(a, b):
    return abs((a - b + 180) % 360 - 180)


def geocode_place(place):
    # Known town-level fallback avoids repeated Nominatim requests for this
    # previously resolved birthplace when the public geocoder rate-limits us.
    normalized = str(place).replace(" ", "")
    if "白马镇" in normalized and ("郸城" in normalized or "周口" in normalized):
        return (
            33.578217, 115.514567,
            "白马镇, 郸城县, 周口市, 河南省, 中国（缓存参考坐标；镇级匹配点，非具体村庄定位）"
        )

    geolocator = Nominatim(user_agent="astro-studio/0.1 (birth chart calculation)")
    try:
        result = geolocator.geocode(place, exactly_one=True, timeout=12)
    except Exception as exc:
        app.logger.warning("Birthplace geocoding failed: %s", type(exc).__name__)
        raise ValueError(
            "出生地点解析服务暂时限流或不可用（" + type(exc).__name__ +
            "）。请稍后重试，或提供经纬度。"
        ) from exc
    if not result:
        raise ValueError("无法识别出生地点。请补充到市/县/乡镇，或直接提供经纬度。")
    return float(result.latitude), float(result.longitude), result.address



SIGN_RULERS = {
    "白羊座": "火星", "金牛座": "金星", "双子座": "水星",
    "巨蟹座": "月亮", "狮子座": "太阳", "处女座": "水星",
    "天秤座": "金星", "天蝎座": "火星", "射手座": "木星",
    "摩羯座": "土星", "水瓶座": "土星", "双鱼座": "木星"
}

SIGN_STYLE = {
    "白羊座": "直接、主动，重视行动与明确回应",
    "金牛座": "稳定、务实，重视安全感与持续投入",
    "双子座": "善于交流、好奇灵活，需要思想互动",
    "巨蟹座": "重视情感照顾、归属感与家庭氛围",
    "狮子座": "热情慷慨，需要被欣赏，也愿意表达心意",
    "处女座": "细致谨慎，常通过实际行动表达关心",
    "天秤座": "重视平等、协调、审美与伴侣关系",
    "天蝎座": "情感深刻，重视信任、忠诚与真实连接",
    "射手座": "坦率乐观，需要空间、成长与共同探索",
    "摩羯座": "慢热认真，重视责任、长期规划与可靠性",
    "水瓶座": "看重精神交流、独立性与平等相处",
    "双鱼座": "敏感浪漫、富有共情，需要温柔与情绪理解"
}

PLANET_HOUSE_MEANING = {
    1: "个人表达、主动性与自我形象",
    2: "个人收入、资源、价值观与积累",
    3: "沟通、学习、信息与日常往来",
    4: "家庭、内在安全感、居所与根基",
    5: "恋爱表达、创造力、兴趣与子女议题",
    6: "工作习惯、服务、技能与日常管理",
    7: "婚姻、长期伴侣、一对一合作与契约",
    8: "共同财务、债务、投资风险、亲密与资源共享",
    9: "高等学习、远行、信念与视野",
    10: "事业方向、社会角色、声誉与长期目标",
    11: "朋友、人脉、社群、团队与长期愿景",
    12: "隐性压力、休息、独处与幕后事务"
}



def detect_chart_patterns(positions, aspects):
    """Identify common major natal-chart patterns and return their evidence."""
    core = [p for p in positions if p.get("name") not in ("北交点", "南交点")]
    by_name = {p["name"]: p for p in core}
    names = list(by_name)
    amap = {}
    for a in aspects:
        if a["planet_a"] in by_name and a["planet_b"] in by_name:
            amap[(frozenset((a["planet_a"], a["planet_b"])), a["aspect"])] = a

    def get(a, b, kind):
        return amap.get((frozenset((a, b)), kind))

    results, seen, trines = [], set(), []
    def add(kind, members, evidence, meaning, strengths, challenges, advice, roles=None):
        key = (kind, tuple(sorted(members)))
        if key in seen:
            return
        seen.add(key)
        orb_values = []
        for item in evidence:
            match = re.search(r"（([0-9.]+)°）", item)
            if match:
                orb_values.append(float(match.group(1)))
        max_orb = max(orb_values) if orb_values else None
        if max_orb is None:
            quality, quality_note = "未评定", "缺少完整容许度数据。"
        elif max_orb <= 3:
            quality, quality_note = "紧密", "结构中最宽的相位容许度不超过3°。"
        elif max_orb <= 5:
            quality, quality_note = "中等", "结构中最宽的相位容许度在3°至5°之间。"
        else:
            quality, quality_note = "宽容许度", "至少一条相位超过5°，解读时应降低整体权重。"
        results.append({
            "name": kind,
            "planets": members,
            "placements": [{"name": n, "sign": by_name[n]["sign"],
                            "house": by_name[n].get("house")} for n in members],
            "roles": roles or {n: "参与星体" for n in members},
            "orb_quality": quality,
            "max_orb": round(max_orb, 3) if max_orb is not None else None,
            "orb_note": quality_note,
            "evidence": evidence, "meaning": meaning, "strengths": strengths,
            "challenges": challenges, "advice": advice
        })

    # Grand trines
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            for k in range(j + 1, len(names)):
                trio = [names[i], names[j], names[k]]
                pairs = [(trio[0],trio[1]),(trio[0],trio[2]),(trio[1],trio[2])]
                if all(get(a,b,"三分相") for a,b in pairs):
                    ev = [f"{a}—{b} 三分相（{get(a,b,'三分相')['orb']}°）" for a,b in pairs]
                    add("大三角", trio, ev,
                        "三个星体形成连续的三分相，相关心理动力较容易彼此配合。",
                        "容易形成自然优势、熟练能力和资源整合感。",
                        "过于顺手的领域可能缺少主动突破。",
                        "把天赋落实为训练、作品或长期成果，不要只停留在感觉容易。")
                    trines.append(trio)

    # T-squares
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a,b = names[i],names[j]
            if not get(a,b,"冲相"): continue
            for c in names:
                if c in (a,b): continue
                if get(a,c,"四分相") and get(b,c,"四分相"):
                    ev = [f"{x}—{y} {kind}（{get(x,y,kind)['orb']}°）"
                          for x,y,kind in [(a,b,"冲相"),(a,c,"四分相"),(b,c,"四分相")]]
                    add("T三角",[a,b,c],ev,
                        "一组对立需求与第三个星体形成的压力出口相连，张力容易集中到某个生活主题。",
                        "可能带来较强的行动、解决问题和持续成长动力。",
                        "压力可能集中爆发，容易在两个极端之间摇摆。",
                        "先识别冲突两端的真实需求，再为顶点主题建立稳定、可执行的出口。")

    # Grand crosses
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            for k in range(j+1,len(names)):
                for m in range(k+1,len(names)):
                    q=[names[i],names[j],names[k],names[m]]
                    pairs=[(q[x],q[y]) for x in range(4) for y in range(x+1,4)]
                    opp=[(a,b) for a,b in pairs if get(a,b,"冲相")]
                    sq=[(a,b) for a,b in pairs if get(a,b,"四分相")]
                    # A valid grand cross has two disjoint opposition axes and
                    # four square edges; every point belongs to one opposition
                    # and exactly two square edges.
                    opp_degree = {n: sum(n in pair for pair in opp) for n in q}
                    sq_degree = {n: sum(n in pair for pair in sq) for n in q}
                    if (len(opp)==2 and len(sq)==4
                            and all(v == 1 for v in opp_degree.values())
                            and all(v == 2 for v in sq_degree.values())):
                        ev=[f"{a}—{b} 冲相（{get(a,b,'冲相')['orb']}°）" for a,b in opp]
                        ev += [f"{a}—{b} 四分相（{get(a,b,'四分相')['orb']}°）" for a,b in sq]
                        add("大十字",q,ev,
                            "四个星体形成多方向的对立与摩擦结构，多个生活主题可能同时要求回应。",
                            "复杂环境中的适应、承担和推动改变能力可能被持续锻炼。",
                            "容易感到多头拉扯、长期紧绷或难以取舍。",
                            "把问题拆成优先级逐项处理，避免试图一次满足所有冲突需求。")

    # Yods use exact longitude geometry, independent of major-aspect display.
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            a,b=names[i],names[j]
            if not get(a,b,"六分相"): continue
            for c in names:
                if c in (a,b): continue
                d1=angular_distance(by_name[a]["longitude"],by_name[c]["longitude"])
                d2=angular_distance(by_name[b]["longitude"],by_name[c]["longitude"])
                sextile = get(a,b,"六分相")
                if (abs(d1-150)<=3 and abs(d2-150)<=3
                        and sextile and sextile.get("orb", 99) <= 3):
                    ev=[f"{a}—{b} 六分相（{sextile['orb']}°）",
                        f"{a}—{c} 梅花相（{round(abs(d1-150),3)}°）",
                        f"{b}—{c} 梅花相（{round(abs(d2-150),3)}°）"]
                    add("上帝手指（Yod）",[a,b,c],ev,
                        "两个星体的协作关系指向一个需要持续调整的焦点。",
                        "可能善于在变化中寻找新方法，对调整信号较敏感。",
                        "容易反复修正方向，或觉得某个领域总需要协调。",
                        "把调整转化为阶段目标，避免把所有困难都解释成命定课题。",
                        {a: "底边端点", b: "底边端点", c: "顶点／焦点"})

    # Kites: grand trine plus an opposition apex sextile to the other two vertices.
    for tri in trines:
        for apex in names:
            if apex in tri: continue
            for vertex in tri:
                others=[n for n in tri if n!=vertex]
                if get(apex,vertex,"冲相") and all(get(apex,n,"六分相") for n in others):
                    ev=[f"{a}—{b} 三分相（{get(a,b,'三分相')['orb']}°）"
                        for a,b in [(tri[0],tri[1]),(tri[0],tri[2]),(tri[1],tri[2])]]
                    ev += [f"{apex}—{vertex} 冲相（{get(apex,vertex,'冲相')['orb']}°）"]
                    ev += [f"{apex}—{n} 六分相（{get(apex,n,'六分相')['orb']}°）" for n in others]
                    add("风筝格局",tri+[apex],ev,
                        "大三角的顺畅循环被一个对冲点牵引，并通过六分相形成行动出口。",
                        "可能把既有优势转化为目标感和实际推动力。",
                        "可能过度依赖单一目标，或把压力集中到对冲轴线上。",
                        "让目标服务长期价值，同时保留调整空间。")
    return results


def build_pattern_report_section(patterns, relevant_planets, title):
    """Translate detected configurations into a cautious, domain-specific report section."""
    relevant = []
    for pattern in patterns or []:
        overlap = [name for name in pattern.get("planets", []) if name in relevant_planets]
        if overlap:
            relevant.append(pattern)
    if not relevant:
        return None

    lines, plain_lines, evidence = [], [], []
    for pattern in relevant:
        quality = pattern.get("orb_quality", "未评定")
        max_orb = pattern.get("max_orb")
        orb_text = f'，最大容许度{max_orb}°' if max_orb is not None else ""
        weight_note = {
            "紧密": "结构较紧密，可作为本专题的重要补充线索，但仍需结合具体相位与现实经验。",
            "中等": "结构力度居中，适合作为辅助线索，不宜单独决定结论。",
            "宽容许度": "结构中存在较宽相位，整体权重应降低，只作背景参考。",
            "未评定": "结构容许度尚未完整评定，暂不提高其解释权重。"
        }.get(quality, "应结合相位容许度谨慎解读。")
        roles = pattern.get("roles", {})
        role_text = "、".join(
            f'{name}（{roles.get(name, "参与星体")}）'
            for name in pattern.get("planets", [])
        )
        lines.append(
            f'{pattern.get("name", "星盘格局")}：涉及{role_text}。'
            f'结构质量为{quality}{orb_text}。{weight_note}'
            f'结构含义：{pattern.get("meaning", "")}'
            f'优势线索：{pattern.get("strengths", "")}'
            f'需要留意：{pattern.get("challenges", "")}'
            f'实践方向：{pattern.get("advice", "")}'
        )
        placements = pattern.get("placements", [])
        placement_text = "、".join(
            f'{item.get("name")}位于{item.get("sign", "未知")}'
            + (f'第{item.get("house")}宫' if item.get("house") else "")
            for item in placements
        )
        plain_lines.append(
            f"你的出生盘中，{placement_text}之间形成了一组相互关联的结构。"
            f"这组联系的整体紧密程度为“{quality}”，{weight_note}"
            f"{pattern.get('meaning', '')}"
            f"它可能带来的优势是：{pattern.get('strengths', '')}"
            f"需要留意的是：{pattern.get('challenges', '')}"
            f"可以尝试这样运用：{pattern.get('advice', '')}"
        )
        evidence.extend(pattern.get("evidence", []))
    return {
        "title": title,
        "content": "\n\n".join(lines),
        "plain_content": "\n\n".join(plain_lines),
        "evidence": evidence
    }


def generate_natal_profile(positions, angles, houses, aspects, patterns=None):
    """Create a chart-evidence-led natal overview; avoid single-placement determinism."""
    by_name = {p["name"]: p for p in positions}
    cusp_by_house = {h["house"]: h for h in houses}

    def p(name):
        return by_name.get(name, {})

    def place(name):
        item = p(name)
        if not item:
            return f"{name}位置资料缺失"
        retro = "，逆行" if item.get("retrograde") else ""
        house = item.get("house")
        house_text = f"第{house}宫" if house else "宫位未知"
        return f'{name}：{item.get("sign", "星座未知")}{item.get("degree", 0)}°{item.get("minute", 0)}′，{house_text}{retro}'

    def house_ruler(no):
        cusp = cusp_by_house.get(no, {})
        sign = cusp.get("sign", "未知")
        ruler = SIGN_RULERS.get(sign)
        rp = p(ruler) if ruler else {}
        return sign, ruler, rp

    def related_aspects(names, limit=5):
        chosen = [a for a in aspects if a.get("planet_a") in names and a.get("planet_b") in names]
        return sorted(chosen, key=lambda a: a.get("orb", 99))[:limit]

    def aspect_evidence(names, limit=5):
        chosen = related_aspects(names, limit)
        return [
            f'{a.get("planet_a")}—{a.get("planet_b")} {a.get("aspect")}，容许度 {a.get("orb")}°，{a.get("phase")}'
            for a in chosen
        ]

    sun, moon = p("太阳"), p("月亮")
    asc = angles.get("上升点", {})
    mercury, venus, mars = p("水星"), p("金星"), p("火星")
    jupiter, saturn = p("木星"), p("土星")
    second_sign, second_ruler, second_pos = house_ruler(2)
    sixth_sign, sixth_ruler, sixth_pos = house_ruler(6)
    tenth_sign, tenth_ruler, tenth_pos = house_ruler(10)
    mc = angles.get("天顶", {})

    identity_evidence = [place("太阳"), place("月亮")]
    if asc:
        identity_evidence.append(f'上升点：{asc.get("sign", "未知")}{asc.get("degree", 0)}°{asc.get("minute", 0)}′')
    identity_evidence += aspect_evidence(["太阳", "月亮"], 4)

    sections = [
        {
            "title": "一、核心人格结构：意志、情绪与外在表达",
            "content": (
                f'太阳落在{sun.get("sign", "未知")}第{sun.get("house", "未知")}宫，'
                f'可作为自我认同、主动意志与长期发展方向的观察线索；'
                f'月亮落在{moon.get("sign", "未知")}第{moon.get("house", "未知")}宫，'
                f'更接近情绪反应、习惯和安全感需求。'
                f'上升点位于{asc.get("sign", "未知")}，描述初始应对方式与面对新环境时的表达风格。'
                f'三者需要合并理解：太阳不等于全部性格，月亮不等于全部情绪，上升也不是固定面具。'
                f'当三者表现出不同需求时，可能体验为内在目标、情绪习惯和外在行动之间需要协调。'
                f'建议结合真实生活场景观察：你主动追求什么、压力下如何反应，以及别人初识你时感受到什么。'
            ),
            "evidence": identity_evidence
        },
        {
            "title": "二、思维与沟通：理解、表达和决策习惯",
            "content": (
                f'水星落在{mercury.get("sign", "未知")}第{mercury.get("house", "未知")}宫，'
                f'提示信息处理和表达可能更关注{SIGN_STYLE.get(mercury.get("sign"), "该星座所代表的思维风格")}；'
                f'其宫位将学习、沟通和判断的注意力带入{PLANET_HOUSE_MEANING.get(mercury.get("house"), "对应生活领域")}。'
                f'这不是智力高低的评判，而是理解自己如何收集信息、组织观点和做决定。'
                f'重要决定可以采用“先列事实、再列假设、最后验证”的方式，避免在信息不足时把直觉当成事实。'
            ),
            "evidence": [place("水星")] + aspect_evidence(["水星", "太阳", "月亮", "土星"], 5)
        },
        {
            "title": "三、关系表达与行动驱力：喜欢、追求和冲突处理",
            "content": (
                f'金星位于{venus.get("sign", "未知")}第{venus.get("house", "未知")}宫，'
                f'可观察你重视的关系价值、审美和愉悦来源；火星位于{mars.get("sign", "未知")}第{mars.get("house", "未知")}宫，'
                f'更侧重行动、欲望表达和面对阻力时的反应。'
                f'两者并非简单代表“喜欢什么类型”或“会不会主动”，还需要结合月亮需求、第五宫恋爱体验和第七宫长期关系结构。'
                f'在现实关系中，清晰表达意愿、尊重边界、观察对方持续行为，比用单一配置给关系贴标签更可靠。'
            ),
            "evidence": [place("金星"), place("火星")] + aspect_evidence(["金星", "火星", "月亮"], 6)
        },
        {
            "title": "四、事业与资源：能力如何落到现实生活",
            "content": (
                f'第二宫宫头为{second_sign}，传统宫主星{second_ruler or "未知"}落在'
                f'{second_pos.get("sign", "未知")}第{second_pos.get("house", "未知")}宫；'
                f'第六宫宫头为{sixth_sign}，宫主星{sixth_ruler or "未知"}落在'
                f'{sixth_pos.get("sign", "未知")}第{sixth_pos.get("house", "未知")}宫；'
                f'第十宫宫头为{tenth_sign}，宫主星{tenth_ruler or "未知"}落在'
                f'{tenth_pos.get("sign", "未知")}第{tenth_pos.get("house", "未知")}宫，'
                f'天顶位于{mc.get("sign", "未知")}。'
                f'把收入、日常工作和职业方向放在一起看，可以形成更完整的现实问题：'
                f'你能提供什么价值、如何稳定交付、市场是否愿意付费，以及长期职业定位能否形成持续现金流。'
                f'星盘不能替代行业调研和财务核算，职业选择仍应通过小规模实践验证。'
            ),
            "evidence": [
                f'第二宫：{second_sign}宫头；宫主星{second_ruler}落{second_pos.get("sign", "未知")}第{second_pos.get("house", "未知")}宫',
                f'第六宫：{sixth_sign}宫头；宫主星{sixth_ruler}落{sixth_pos.get("sign", "未知")}第{sixth_pos.get("house", "未知")}宫',
                f'第十宫：{tenth_sign}宫头；宫主星{tenth_ruler}落{tenth_pos.get("sign", "未知")}第{tenth_pos.get("house", "未知")}宫',
                f'天顶：{mc.get("sign", "未知")}{mc.get("degree", 0)}°{mc.get("minute", 0)}′'
            ] + aspect_evidence(["木星", "土星", "太阳", "火星"], 5)
        },
        {
            "title": "五、成长与长期课题：扩张、边界和持续建设",
            "content": (
                f'木星落在{jupiter.get("sign", "未知")}第{jupiter.get("house", "未知")}宫，'
                f'可作为学习、扩张和寻找机会的主题；土星落在{saturn.get("sign", "未知")}第{saturn.get("house", "未知")}宫，'
                f'可作为责任、限制、耐心和长期建设的主题。'
                f'二者需要结合相位、宫主星和现实环境判断，不能简单说木星一定带来好运、土星一定带来困难。'
                f'更稳健的用法是：识别自己容易乐观扩张的领域，同时建立预算、节奏、检查点和可持续的执行规则。'
            ),
            "evidence": [place("木星"), place("土星")] + aspect_evidence(["木星", "土星"], 4)
        }
    ]
    pattern_section = build_pattern_report_section(
        patterns,
        {"太阳", "月亮", "水星", "金星", "火星", "木星", "土星", "天王星", "海王星", "冥王星"},
        "六、重要格局整合：潜在优势、张力与调整方式"
    )
    if pattern_section:
        sections.append(pattern_section)

    # Plain-language layer shown to customers; all calculation terminology remains hidden.
    def everyday(item, label):
        if not item:
            return f"{label}方面的资料不足，先不作具体判断。"
        style = SIGN_STYLE.get(item.get("sign"), "需要结合现实经历观察")
        area = PLANET_HOUSE_MEANING.get(item.get("house"), "日常生活")
        return f"{label}方面，你更容易表现出{style}；这种特点容易在{area}中体现。"

    customer_sections = [
        f"你身上有两种需要同时照顾的部分：一方面希望主动表达自己、被别人看见；另一方面也需要空间、变化和真实交流。{everyday(sun, '你的核心动力')} {everyday(moon, '你的情绪与安全感')} 别人初识你时感受到的样子，不一定完全等于你私下真实的感受。给自己留出表达真实需求的空间，会比一味迎合别人更轻松。",
        f"你处理信息和沟通时，容易采用自己熟悉的思考节奏。{everyday(mercury, '你的思考与表达')} 遇到重要决定时，建议把已确认的事实、自己的猜测和还需要核实的部分分开写下来，避免因为一时判断太快而遗漏关键细节。",
        f"在关系里，你既需要吸引力，也需要实际行动带来的安全感。{everyday(venus, '你表达喜欢和欣赏的方式')} {everyday(mars, '你主动行动和处理分歧的方式')} 不必用猜测代替沟通，也不要只凭一时热情判断一个人是否适合长期相处。",
        f"事业发展更适合从真实能力和实际需求出发。{everyday(second_pos, '你的收入与资源管理')} {everyday(tenth_pos, '你的事业方向')} 选择方向时，先确认自己能解决什么问题、谁愿意付费、交付成本是多少，再决定是否投入更多时间和资金。",
        f"长期成长的重点，是让机会和风险管理保持平衡。{everyday(jupiter, '你寻找机会和拓展的方式')} {everyday(saturn, '你面对责任和长期任务的方式')} 有想法可以尝试，但最好先设定预算、期限和检查标准，用实际结果决定下一步。"
    ]
    for idx, section in enumerate(sections):
        if idx < len(customer_sections):
            section["plain_content"] = customer_sections[idx]
        else:
            section["plain_content"] = "这一部分属于补充分析。你可以把它当作自我观察的提示，不需要根据某个标签给自己下定论；更重要的是结合真实经历，判断哪些描述确实符合你。"

    return {
        "title": "你的性格与人生方向",
        "intro": "这里直接讲你的性格特点、思考方式、关系习惯和发展方向。无需了解任何专业知识。",
        "sections": sections
    }


def generate_life_analysis(positions, angles, houses, aspects, patterns=None):
    """Generate detailed, chart-grounded relationship and finance interpretations."""
    by_name = {p["name"]: p for p in positions}
    cusp_by_house = {h["house"]: h for h in houses}

    def planet(name):
        return by_name.get(name, {})

    def ruler_of(house_no):
        cusp = cusp_by_house.get(house_no, {})
        sign = cusp.get("sign")
        ruler = SIGN_RULERS.get(sign)
        return sign, ruler, planet(ruler) if ruler else {}

    def aspect_list(names, limit=8):
        selected = [
            a for a in aspects
            if a["planet_a"] in names and a["planet_b"] in names
        ]
        return sorted(selected, key=lambda a: a["orb"])[:limit]

    def aspect_text(names, limit=8):
        selected = aspect_list(names, limit)
        if not selected:
            return "这些关键星体之间没有落入本报告采用范围的主要相位，因此本段主要依据星座、宫位和宫主星判断。"
        meanings = {
            "合相": "两种心理动力容易集中在同一议题上，表现可能更强烈，也需要有意识地分辨各自需求",
            "六分相": "两种动力之间存在可主动运用的配合空间，通常需要通过选择、练习或沟通来发挥",
            "四分相": "两种动力容易产生摩擦，可能带来压力，也可能推动当事人调整旧习惯",
            "三分相": "两种动力较容易自然配合，但过于熟悉的模式也可能让人缺少主动调整",
            "冲相": "两种动力容易在不同方向之间拉扯，需要在两端需求之间建立平衡"
        }
        return "；".join(
            f'{a["planet_a"]}与{a["planet_b"]}{a["aspect"]}（容许度{a["orb"]}°，{a["phase"]}）：'
            f'{meanings.get(a["aspect"], "提示两项主题之间存在互动")} '
            for a in selected
        ) + "。"

    def placement(name):
        p = planet(name)
        if not p:
            return f"{name}位置资料缺失"
        state = "逆行" if p.get("retrograde") else "顺行"
        return f'{name}位于{p.get("sign", "未知")}第{p.get("house", "未知")}宫，{state}'

    def house_focus(house_no):
        h = cusp_by_house.get(house_no, {})
        sign = h.get("sign", "未知")
        ruler = SIGN_RULERS.get(sign, "未知")
        rp = planet(ruler)
        return (
            f"第{house_no}宫宫头落在{sign}，传统宫主星为{ruler}；"
            f"宫主星落在{rp.get('sign', '未知')}第{rp.get('house', '未知')}宫。"
            f"这意味着第{house_no}宫的议题，往往会通过"
            f"“{PLANET_HOUSE_MEANING.get(rp.get('house'), '宫主星所在生活领域')}”"
            f"这一生活场景被体验或推动。"
        )

    venus, mars, moon = planet("金星"), planet("火星"), planet("月亮")
    fifth_sign, fifth_ruler, fifth_pos = ruler_of(5)
    seventh_sign, seventh_ruler, seventh_pos = ruler_of(7)
    eighth_sign, eighth_ruler, eighth_pos = ruler_of(8)
    second_sign, second_ruler, second_pos = ruler_of(2)
    tenth_sign, tenth_ruler, tenth_pos = ruler_of(10)
    jupiter, saturn = planet("木星"), planet("土星")
    mc = angles.get("天顶", {})

    relationship = [
        {
            "title": "一、你的情感需求：喜欢怎样的人，怎样才有安全感",
            "content": (
                f"{placement('金星')}。金星描述被吸引的类型、表达好感的方式，以及你在关系中重视的价值。"
                f"落在{venus.get('sign', '未知')}时，情感表达倾向于{SIGN_STYLE.get(venus.get('sign'), '需要结合其他配置判断')}。"
                f"它所在的第{venus.get('house', '未知')}宫对应{PLANET_HOUSE_MEANING.get(venus.get('house'), '相关生活领域')}，"
                f"所以你容易在这一领域寻找欣赏、愉悦或关系连接。"
                f"\n\n{placement('月亮')}。月亮更接近本能反应、私下情绪和安全感需求。"
                f"月亮落在{moon.get('sign', '未知')}，情绪上更需要{SIGN_STYLE.get(moon.get('sign'), '稳定而清晰的回应')}；"
                f"第{moon.get('house', '未知')}宫说明这种需求也会受到"
                f"{PLANET_HOUSE_MEANING.get(moon.get('house'), '相关生活领域')}的影响。"
                f"\n\n综合来看，金星代表“你容易被什么打动”，月亮代表“什么相处方式能让你安心”。"
                f"两者不一定完全相同：短期吸引力不能代替长期情绪适配。观察对方是否言行一致、能否回应真实需求，比只看外在条件更重要。"
            )
        },
        {
            "title": "二、恋爱启动与相处节奏：主动方式、吸引力和磨合点",
            "content": (
                f"{placement('火星')}。火星描述行动、欲望表达、冲突反应和推进关系的节奏。"
                f"火星落在{mars.get('sign', '未知')}，行动风格偏向{SIGN_STYLE.get(mars.get('sign'), '需要结合全盘判断')}；"
                f"第{mars.get('house', '未知')}宫强调"
                f"{PLANET_HOUSE_MEANING.get(mars.get('house'), '相关生活领域')}，说明你可能更容易在该类情境中投入行动或表现主动。"
                f"\n\n第五宫宫头为{fifth_sign or '未知'}，宫主星{fifth_ruler or '未知'}落在"
                f"{fifth_pos.get('sign', '未知')}第{fifth_pos.get('house', '未知')}宫。"
                f"第五宫关注恋爱初期、约会、兴趣和表达热情；宫主星所在宫位提示恋爱体验可能与"
                f"{PLANET_HOUSE_MEANING.get(fifth_pos.get('house'), '该宫生活主题')}发生联系。"
                f"\n\n实际建议：不要只靠猜测对方态度来推进关系。用稳定、适度的表达确认彼此意愿；"
                f"当主动节奏不同，先讨论联系频率、见面安排和个人空间，而不是把节奏差异直接理解成不在乎。"
            )
        },
        {
            "title": "三、长期伴侣与婚姻：承诺模式及关系中的核心课题",
            "content": (
                f"{house_focus(7)}第七宫是长期伴侣、婚姻、平等协商和一对一承诺的重要观察点。"
                f"宫头星座{seventh_sign or '未知'}提供关系互动的基本风格线索，"
                f"宫主星{seventh_ruler or '未知'}落在{seventh_pos.get('sign', '未知')}第{seventh_pos.get('house', '未知')}宫，"
                f"说明长期关系容易与{PLANET_HOUSE_MEANING.get(seventh_pos.get('house'), '该宫生活主题')}相互牵动。"
                f"\n\n这不是对配偶外貌、职业或结婚时间的确定判断，而是提示你在选择长期伴侣时，"
                f"需要认真评估关系能否融入现实生活：双方的生活目标是否兼容，遇到分歧能否协商，"
                f"是否愿意共同承担家庭、时间和经济责任。"
                f"\n\n判断关系是否适合长期发展，优先看尊重、诚信、责任感、冲突后的修复能力，以及双方是否都愿意持续投入。"
            )
        },
        {
            "title": "四、亲密关系的优势与挑战：情绪、爱意和行动如何互动",
            "content": (
                f"金星、火星、月亮之间的主要相位：{aspect_text(['金星', '火星', '月亮'], 8)}"
                f"\n\n这些相位描述的是情感表达、情绪需求和行动方式之间的互动，不是对感情结果的判决。"
                f"较顺畅的配置可以成为沟通与亲密的资源；较紧张的配置则提醒你，"
                f"在情绪上头时先区分“我感到什么”“我需要什么”和“我希望对方做什么”，避免把感受直接变成指责。"
                f"\n\n{house_focus(8)}第八宫还涉及信任、隐私、亲密边界、共同财务和风险共担。"
                f"进入稳定关系后，金钱往来、债务、家庭责任和个人隐私应提前讲清楚，避免用牺牲边界换取安全感。"
            )
        },
        {
            "title": "五、容易重复的关系模式与需要留意的盲点",
            "content": (
                f"观察重点是金星的关系价值、月亮的安全感需求、火星的冲突反应，以及第七宫宫主星的落点。"
                f"当你很在意一段关系时，可能更容易放大对方的某个优点，或把一时的热情当成长期承诺。"
                f"如果关系中出现反复失联、冷处理、承诺落空、单方面付出或金钱边界模糊，"
                f"应以实际行为作为判断依据，不要用星盘解释或合理化持续伤害。"
                f"\n\n较成熟的做法是：给关系观察时间，确认对方是否持续兑现承诺；"
                f"遇到矛盾时看双方是否愿意修复，而不只看争吵当下谁对谁错。"
            )
        },
        {
            "title": "六、感情行动建议与综合结论",
            "content": (
                f"你的关系分析应同时看金星（月亮的情感需要）、火星（行动节奏）、第五宫（恋爱体验）、"
                f"第七宫（长期承诺）和第八宫（信任与共享资源），不能只凭一个星座下结论。"
                f"\n\n建议把择偶标准分成三层：第一层是底线，包括诚实、尊重、不暴力、不操控；"
                f"第二层是适配，包括生活节奏、沟通方式、家庭观念和经济观念；"
                f"第三层才是吸引力、兴趣与浪漫体验。"
                f"\n\n星盘无法保证复合、结婚、分手或某个人一定出现，也不能替代你对现实关系的观察。"
                f"本报告最有用的部分，是帮助你识别需求、看见容易忽略的模式，并把选择权落实到现实行动中。"
            )
        }
    ]

    finance = [
        {
            "title": "一、个人财富结构：收入、安全感与金钱观",
            "content": (
                f"{house_focus(2)}第二宫主要观察个人劳动收入、可支配资源、技能定价、消费倾向和储蓄习惯。"
                f"宫头星座为{second_sign or '未知'}，其传统宫主星{second_ruler or '未知'}落在"
                f"{second_pos.get('sign', '未知')}第{second_pos.get('house', '未知')}宫。"
                f"\n\n宫主星所在宫位为收入模式提供了一个探索方向："
                f"第{second_pos.get('house', '未知')}宫对应{PLANET_HOUSE_MEANING.get(second_pos.get('house'), '相关生活领域')}，"
                f"可以思考你是否能把该领域的知识、经验、人脉或服务转化为稳定价值。"
                f"\n\n这不是说财富会自动从该领域到来。真正能否变现，还取决于市场需求、产品质量、执行能力、成本结构和持续获客能力。"
            )
        },
        {
            "title": "二、适合发展的赚钱路径：能力如何转化为现金流",
            "content": (
                f"第二宫宫主星是{second_ruler or '未知'}，落在{second_pos.get('sign', '未知')}第{second_pos.get('house', '未知')}宫；"
                f"第十宫宫主星是{tenth_ruler or '未知'}，落在{tenth_pos.get('sign', '未知')}第{tenth_pos.get('house', '未知')}宫。"
                f"\n\n把个人收入宫与事业宫放在一起看，重点不是简单判断“适合做什么职业”，"
                f"而是寻找可重复的价值链：你能解决什么问题、谁愿意为此付费、交付成本是多少、客户是否会复购或转介绍。"
                f"如果收入依赖单次机会或高波动项目，应逐步增加可复用技能、稳定客户来源和标准化交付。"
                f"\n\n建议用小规模试单验证需求，再扩大投入；每个项目都记录获客成本、毛利、回款周期和售后成本。"
            )
        },
        {
            "title": "三、事业发展与社会定位：长期方向和收入转化",
            "content": (
                f"第十宫宫头为{tenth_sign or '未知'}，传统宫主星{tenth_ruler or '未知'}落在"
                f"{tenth_pos.get('sign', '未知')}第{tenth_pos.get('house', '未知')}宫；"
                f"天顶（MC）位于{mc.get('sign', '未知')}。第十宫与天顶侧重职业方向、社会角色、声誉和长期目标。"
                f"\n\n宫主星所在的{PLANET_HOUSE_MEANING.get(tenth_pos.get('house'), '相关生活领域')}，"
                f"可以作为你建立专业标签或职业影响力的切入点。"
                f"要让事业真正转化为财富，需要把专业能力变成可报价、可交付、可复购的产品或服务，"
                f"并建立稳定的获客和回款流程。"
                f"\n\n职位、名声或忙碌程度本身不等于财富；要持续检查净利润、现金流和时间投入是否匹配。"
            )
        },
        {
            "title": "四、扩张能力与长期积累：机会、纪律和时间",
            "content": (
                f"{placement('木星')}。木星象征扩张、信念、学习和机会感，其所在宫位涉及"
                f"{PLANET_HOUSE_MEANING.get(jupiter.get('house'), '个人成长领域')}。"
                f"它可以提示你在哪些领域更愿意尝试、扩大视野或寻找增长机会，但也要留意过度乐观和高估回报。"
                f"\n\n{placement('土星')}。土星强调责任、边界、延迟满足和长期建设；"
                f"其所在宫位对应{PLANET_HOUSE_MEANING.get(saturn.get('house'), '需要长期经营的领域')}，"
                f"提醒你通过规则、流程、经验和持续投入建立可靠性。"
                f"\n\n木星与土星的主要相位：{aspect_text(['木星', '土星'], 4)}"
                f"。更稳妥的策略是先验证小规模模型，再逐步扩大；让预算、能力和风险承受度跟得上增长速度。"
            )
        },
        {
            "title": "五、债务、合作资金与风险边界",
            "content": (
                f"{house_focus(8)}第八宫对应借贷、税务、保险、投资共担、伴侣或合作方资金，以及财务责任边界。"
                f"第八宫宫主星{eighth_ruler or '未知'}落在{eighth_pos.get('sign', '未知')}第{eighth_pos.get('house', '未知')}宫。"
                f"\n\n木星、土星、冥王星相关相位：{aspect_text(['木星', '土星', '冥王星'], 6)}"
                f"\n\n现实层面的重点是：任何借款先算总成本、利息、还款来源和最坏情形；"
                f"合作前写清出资比例、收益分配、退出机制和责任承担；不要替他人签署不理解的担保或借款文件。"
                f"在现金流尚不稳定时，优先控制固定支出和高息负债，不以借新还旧或高杠杆押注未来收入。"
            )
        },
        {
            "title": "六、财富积累的主要短板与纠偏方法",
            "content": (
                f"本命盘中的第二宫提示个人收入与资源管理，第八宫提示外部资金和共同风险，"
                f"第十宫提示职业路径；木星与土星则分别提供扩张和约束的观察角度。"
                f"\n\n最值得检查的不是所谓“有没有财运”，而是收入是否稳定、利润是否真实、回款是否及时、"
                f"负债是否可控，以及是否有应急资金。若营业额增加但毛利下降、库存积压或账期拉长，"
                f"规模扩大反而可能加重现金压力。"
                f"\n\n建议每周记录收入、必要支出、债务余额、到期日和可用现金；先建立基本安全垫，再考虑高风险投资或扩张。"
            )
        },
        {
            "title": "七、财运综合结论与执行顺序",
            "content": (
                "占星中的财富主题不能直接换算成具体收入金额、发财年份、中奖概率或投资涨跌。"
                "本报告提供的是自我观察框架，不是财务预测。"
                "\n\n可执行的优先顺序是：第一，盘点现金、债务、利率和还款日期；第二，确定一项能低成本验证的收入来源；"
                "第三，连续记录真实毛利、获客成本、回款周期和复购率；第四，确认模型稳定后再增加投入；"
                "第五，建立应急储备并避免替他人承担不清晰的财务责任。"
                "\n\n衡量财富进展时，优先看净资产和自由现金流，而不只看营业额、订单数或账面估值。"
            )
        }
    ]

    relationship_pattern_section = build_pattern_report_section(
        patterns, {"金星", "火星", "月亮", "水星", "土星", "天王星", "冥王星"},
        "七、格局对关系模式的补充观察"
    )
    if relationship_pattern_section:
        relationship.append(relationship_pattern_section)

    finance_pattern_section = build_pattern_report_section(
        patterns, {"水星", "木星", "土星", "天王星", "海王星", "冥王星", "火星"},
        "八、格局对事业与财富管理的补充观察"
    )
    if finance_pattern_section:
        finance.append(finance_pattern_section)

    # Detailed plain-language layer: synthesize the actual chart factors instead of
    # repeating generic advice. The technical evidence remains available below.
    sign_detail = {
        "白羊座": "更倾向先行动、直接表达，喜欢明确的态度；需要留意急于推进或把即时反应当成最终决定",
        "金牛座": "重视稳定、可触摸的安全感和持续兑现；需要留意因害怕变化而拖延必要调整",
        "双子座": "需要交流、信息流动和思想上的新鲜感；需要留意兴趣变化快或沟通很多却迟迟不落地",
        "巨蟹座": "重视照顾、归属感和情绪上的被接纳；需要留意把对方的情绪变化过度理解为关系冷热",
        "狮子座": "希望被认真看见、尊重和肯定，也愿意热情投入；需要留意自尊受挫时不愿先表达脆弱",
        "处女座": "重视细节、可靠性和实际行动；需要留意过度分析、挑错，或把关心变成不断纠正",
        "天秤座": "重视公平、互动质量和双方的体面；需要留意为了避免冲突而迟迟不说真实立场",
        "天蝎座": "重视深度、忠诚和真实信任，不容易满足于表面关系；需要留意猜测、试探或控制感",
        "射手座": "需要坦诚、成长空间和共同探索；需要留意把自由理解成不必交代，或在压力下回避细节",
        "摩羯座": "看重责任、长期规划和可依靠的行动；需要留意过度克制情绪，或把关系变成任务",
        "水瓶座": "重视平等、精神交流和个人空间；需要留意显得过于理性，让对方难以确认你的情感投入",
        "双鱼座": "重视共情、温柔和情绪连结；需要留意理想化对方、界限模糊或替别人承担过多"
    }
    def sign_detail_of(item):
        return sign_detail.get(item.get("sign"), "需要结合具体宫位与相位判断")
    def placement_detail(name, focus):
        item = planet(name)
        if not item:
            return f"{name}资料缺失，暂不作具体判断。"
        sign = item.get("sign", "未知")
        house = item.get("house", "未知")
        return (f"{name}在{sign}第{house}宫：{sign_detail_of(item)}。"
                f"它把{focus}带到“{PLANET_HOUSE_MEANING.get(house, '对应生活领域')}”这一现实场景。")
    def ruler_detail(label, sign, ruler, pos):
        if not pos:
            return f"{label}资料不完整，暂时无法追踪宫主星。"
        return (f"{label}宫头为{sign}，由{ruler}主导；{ruler}落在{pos.get('sign', '未知')}第{pos.get('house', '未知')}宫。"
                f"因此，{label}的事情不只看宫头星座，还会与“{PLANET_HOUSE_MEANING.get(pos.get('house'), '对应生活领域')}”发生联系。"
                f"{sign_detail_of(pos)}")
    def focused_aspects(names):
        selected = aspect_list(names, 10)
        if not selected:
            return "这些重点星体之间没有筛选到主要相位；这不代表没有相关体验，而是本段更应依据各自落座、宫位和宫主星来理解。"
        lines = []
        pair_meanings = {
            frozenset(("金星", "月亮")): "喜欢的表达方式与情绪安全感之间的配合或落差",
            frozenset(("金星", "火星")): "吸引力、表达好感和主动推进关系之间的互动",
            frozenset(("月亮", "火星")): "情绪需求与冲突反应之间的互动",
            frozenset(("金星", "土星")): "亲密需求与谨慎、责任、承诺门槛之间的互动",
            frozenset(("月亮", "土星")): "情绪表达与自我保护、责任压力之间的互动",
            frozenset(("金星", "木星")): "情感表达、慷慨程度与期待值之间的互动",
            frozenset(("木星", "土星")): "扩张机会与现实约束之间的互动",
            frozenset(("水星", "土星")): "思考沟通与审慎、规则之间的互动",
            frozenset(("水星", "木星")): "信息判断与大方向、机会感之间的互动",
            frozenset(("火星", "土星")): "行动冲劲与风险控制、延迟之间的互动"
        }
        for a in selected:
            pair = frozenset((a["planet_a"], a["planet_b"]))
            focus = pair_meanings.get(pair, f'{a["planet_a"]}与{a["planet_b"]}所代表的两类需求')
            nature = {
                "合相": "两股力量集中在一起，相关议题容易变得突出",
                "六分相": "两股力量有协作空间，但通常需要主动运用",
                "四分相": "两股力量容易摩擦，压力也可能推动调整",
                "三分相": "两股力量较容易配合，但熟悉的做法也可能被惯性固定",
                "冲相": "两股力量容易拉扯，需要兼顾双方需求"
            }.get(a["aspect"], "两股力量形成互动")
            phase = "正在趋近精确" if a.get("phase") == "趋近" else ("已经越过精确点" if a.get("phase") == "分离" else "处于精确位置")
            lines.append(f'{a["planet_a"]}与{a["planet_b"]}{a["aspect"]}，容许度{a["orb"]}°（{phase}）：这主要反映{focus}；{nature}。')
        return " ".join(lines)
    # Customer-facing copy uses everyday language only; technical calculations stay server-side.
    life_area = {
        1: "个人表达和自我定位", 2: "收入、储蓄和个人价值", 3: "沟通、学习和信息往来",
        4: "家庭、居住和内心安全感", 5: "恋爱、兴趣和创造表达",
        6: "日常工作、技能和习惯", 7: "长期伴侣、婚姻和合作",
        8: "共同财务、信任和责任边界", 9: "学习进修、远行和视野",
        10: "事业发展、社会角色和长期目标",
        11: "朋友、人脉、团队和长期愿景", 12: "休息、独处和幕后事务"
    }
    def human_style(item):
        return sign_detail_of(item).replace("；需要留意", "；同时要留意")
    def human_area(item):
        return life_area.get(item.get("house"), "现实生活中的相关领域")
    def human_profile(name, topic):
        item = planet(name)
        if not item:
            return f"{topic}方面的具体资料不足，建议结合现实经历判断。"
        return f"你在{topic}方面，比较明显的特点是：{human_style(item)}。这类特点容易在{human_area(item)}中表现出来。"

    venus_house = venus.get("house", "未知")
    moon_house = moon.get("house", "未知")
    mars_house = mars.get("house", "未知")
    relationship_plain = [
        (
            f"【你容易被什么样的人吸引】{human_profile('金星', '表达好感和选择伴侣')} "
            f"你通常会留意对方是否温柔、有回应，能不能在日常互动中让你感到被放在心上。比起只有外在条件或短暂热情，你更容易被持续的关心、熟悉感，以及能从朋友般相处逐渐建立的亲近感打动。"
            f"但“喜欢一个人”和“适合一起生活”是两回事：吸引力可以开启关系，不能单独证明两个人合适。"
        ),
        (
            f"【你在恋爱中需要怎样的相处节奏】{human_profile('月亮', '情绪满足和恋爱体验')} "
            f"你需要关系里有轻松感、共同兴趣和新鲜体验，同时也需要对方愿意回应你的情绪。长期只有日常琐事、缺少交流和共同活动，容易让亲密感变淡；但如果只追求一时开心、不谈现实安排，也很难形成稳定关系。"
            f"适合你的节奏，是既能一起体验新事物，也能在普通日子里保持联系和关心。"
        ),
        (
            f"【你表达好感、推进关系和处理争执的方式】{human_profile('火星', '主动行动和冲突反应')} "
            f"你在决定投入之前可能更看重实际感受和相处是否可靠；一旦认定，往往希望关系有持续性。需要留意的是，不要把忍耐当成解决问题，也不要在不满积累很久后才一次性爆发。"
            f"出现分歧时，尽量在问题刚出现时说清具体事情、自己的感受和希望怎样调整，而不是用冷战或反复试探来确认对方在不在乎。"
        ),
        (
            f"【长期伴侣与婚姻：什么样的关系更能走得久】{human_profile(seventh_ruler or '土星', '长期承诺和婚姻责任')} "
            f"你需要的婚姻不是时时黏在一起，而是双方既有各自空间，也愿意对共同生活负责。真正需要提前磨合的，是未来定居方式、家庭责任分配、工作与陪伴时间，以及遇到困难时是否站在同一边。"
            f"不要只凭恋爱时的感觉判断婚姻适配度；观察对方能否兑现承诺、承担责任，并愿意把重要决定拿出来共同商量。"
        ),
        (
            f"【亲密、信任与金钱边界】{human_profile(eighth_ruler or '木星', '深层信任和共同责任')} "
            f"关系进入更深阶段后，真正考验的不只是感情浓度，还包括能否坦诚面对脆弱、家庭影响和现实压力。尤其涉及共同开支、借款、债务、财产安排或双方家庭时，不能因为信任就省略沟通。"
            f"建议重要约定说清楚并留下记录；亲密不等于失去个人边界，互相支持也不等于由一方长期承担全部责任。"
        ),
        (
            f"【你需要警惕的感情盲点】{human_profile('金星', '关系期待')} {human_profile('月亮', '情绪反应')} "
            f"当你既渴望被在意、又希望关系保持轻松时，容易出现一种矛盾：一方面期待对方主动给出确定感，另一方面又可能不愿直接说出自己的不安。这样容易让双方靠猜测相处。"
            f"如果对方长期失联、反复失约、回避关键问题或只在需要时出现，不要只记住对方偶尔的好；把一段时间里的实际行为放在一起看。"
        ),
        (
            f"【择偶时怎样判断是否适合结婚】综合你的情感需求、恋爱节奏和长期承诺特点，建议用三个现实问题筛选：第一，和对方相处时能否自然表达，不必长期猜测或讨好；第二，双方对家庭、金钱、孩子、居住和未来安排是否有基本共识；第三，发生冲突后，双方是否都愿意承担责任并修复关系。"
            f"先确认人品、稳定性和生活目标，再考虑浪漫程度与外在条件。星盘不能判断某个人必然出现，也不能保证结婚或复合；是否适合，最终要看双方长期、具体的行动。"
        )
    ]
    # The second-house and tenth-house rulers reveal whether income and career
    # are routed through the same life area or through different channels.
    income_house = second_pos.get("house")
    career_house = tenth_pos.get("house")
    if income_house == career_house:
        income_career_link = (
            f"一个值得重点关注的结构是：第二宫收入宫主星{second_ruler}与第十宫事业宫主星{tenth_ruler}，"
            f"都落在第{income_house}宫。收入能力和职业发展因此指向同一类生活场景——"
            f"“{PLANET_HOUSE_MEANING.get(income_house, '相关生活领域')}”。"
            f"这意味着职业定位与赚钱方式可能需要协同经营；在这个领域积累的技能、信誉和关系网络，"
            f"更容易同时影响客户来源与收入稳定性。"
        )
    else:
        income_career_link = (
            f"收入宫主星{second_ruler}落在第{income_house}宫，事业宫主星{tenth_ruler}落在第{career_house}宫，"
            f"两者连接了不同生活场景。要把职业成果转成个人收入，需要主动搭桥："
            f"把事业领域的成果转成可报价的服务或产品，再通过收入宫所指向的渠道完成成交、交付和回款。"
        )
    finance_plain = [
        (
            f"【你怎样建立个人收入】{ruler_detail('第二宫', second_sign, second_ruler, second_pos)} "
            f"第二宫关注个人劳动收入、技能定价、可支配资源和储蓄。宫主星所在宫位提供的是收入切入口，"
            f"不是自动进账的保证。你可以据此追问三个现实问题：别人愿意为你解决什么问题付费？"
            f"你提供的价值能否重复交付？扣除获客、材料、物流、时间和售后成本后，是否还剩下真实利润？"
        ),
        (
            f"【职业方向怎样转化为收入】{ruler_detail('第十宫', tenth_sign, tenth_ruler, tenth_pos)} "
            f"天顶位于{mc.get('sign', '未知')}，补充职业角色、公众定位和长期声誉的观察角度。"
            f"{income_career_link} 不要只看行业名称是否“适合”，而要验证具体产品或服务有没有真实需求、"
            f"客户是否愿意付费、交付是否稳定，以及回款周期是否能支撑日常经营。"
        ),
        (
            f"【你的机会更可能从哪里被打开】{placement_detail('木星', '扩张机会、学习成长、信念和资源放大')} "
            f"木星所在第{jupiter.get('house', '未知')}宫，把增长、学习和拓展的注意力带到"
            f"“{PLANET_HOUSE_MEANING.get(jupiter.get('house'), '相关生活领域')}”。"
            f"它可以提示你愿意在哪些领域扩大投入，但机会感不等于项目已经验证。"
            f"每次准备扩张前，都应先用小样本确认成交率、毛利、复购、获客成本和现金回款。"
        ),
        (
            f"【财富积累需要什么纪律】{placement_detail('土星', '责任、限制、长期建设和风险意识')} "
            f"土星所在第{saturn.get('house', '未知')}宫，提示长期建设需要在哪类生活议题上建立规则。"
            f"木星与土星之间的具体关系是：{focused_aspects(['木星', '土星'])} "
            f"这部分不应被理解为“有财”或“破财”的判词，而应转化为预算、合同、账期、库存和扩张节奏的管理制度。"
        ),
        (
            f"【借贷、合作与共同资金风险】{ruler_detail('第八宫', eighth_sign, eighth_ruler, eighth_pos)} "
            f"第八宫涉及借款、共同投资、税务保险、合作资金和责任边界。"
            f"它的宫主星位置提示外部资金议题容易牵动哪个生活领域；现实中，任何借款或合伙都应书面确认"
            f"本金、利息、期限、担保、收益分配、退出条件和最坏情形。不能只因关系好或预期乐观就承担不清楚的责任。"
        ),
        (
            f"【最容易被忽略的财务盲点】{focused_aspects(['水星', '木星', '土星', '火星', '天王星', '海王星', '冥王星'])} "
            f"这组相位更适合用来检查决策习惯：信息是否核实、乐观估算是否留了余量、压力下是否冲动投入、"
            f"是否因为害怕错过机会而忽略合同和现金流。每个项目都应单独核算收入、直接成本、获客成本、售后成本、"
            f"库存占用和回款时间，不能把营业额当成利润。"
        ),
        (
            f"【财富行动顺序】结合第二宫个人收入、第十宫事业路径、第八宫外部资金责任，以及木星和土星的扩张/约束主题，"
            f"更稳妥的步骤是：先盘清可用现金和全部到期责任；选一项启动成本可控的收入方向；"
            f"先做小规模真实成交；连续验证净利润、回款和复购后再扩大；最后建立应急储备。"
            f"星盘不能给出发财年份、具体收入金额或投资涨跌，财富进展应以净资产、自由现金流和实际经营数据衡量。"
        )
    ]
    # Build customer-facing relationship sections explicitly so titles and copy
    # cannot drift when optional technical pattern sections are added.
    relationship_titles = [
        "容易被什么样的人吸引",
        "恋爱中需要怎样的相处节奏",
        "表达好感、推进关系和处理争执",
        "长期伴侣与婚姻：什么样的关系更能走得久",
        "亲密、信任与金钱边界",
        "需要警惕的感情盲点",
        "择偶时怎样判断是否适合结婚"
    ]
    relationship = [
        {"title": title, "content": copy, "plain_content": copy}
        for title, copy in zip(relationship_titles, relationship_plain)
    ]
    if relationship_pattern_section:
        relationship.append(relationship_pattern_section)
    for index, item in enumerate(finance):
        if index < len(finance_plain):
            item["plain_content"] = finance_plain[index]

    return {
        "relationship": {
            "title": "婚姻与感情深度分析",
            "intro": "这份报告用日常语言讨论你在亲密关系中的需要、相处习惯、择偶判断和可以采取的行动。内容是自我观察参考，不代表感情事件必然发生。",
            "sections": relationship
        },
        "finance": {
            "title": "财运与财富结构深度分析",
            "intro": "这份报告重点讨论你可以怎样把能力转化为收入、怎样验证赚钱方向、如何管理现金流与风险。它不是收入预测，也不保证发财或投资回报。",
            "sections": finance
        },
        "method": "解释由本命盘实际星座、宫位、宫主星和主要相位按规则生成；传统宫主星采用传统守护体系。占星属于文化与自我探索工具，不是经科学验证的事件预测。"
    }

def generate_monthly_transit_analysis(natal_positions, houses, birth_timezone):
    """Create plain-language past/future 30-day summaries from daily transit contacts."""
    from datetime import timedelta
    tz = ZoneInfo(birth_timezone)
    now_local = datetime.now(tz)
    today = now_local.date()
    past_start, future_end = today - timedelta(days=30), today + timedelta(days=30)
    natal = {p["name"]: p["longitude"] for p in natal_positions}
    cusp = {h["house"]: h["longitude"] for h in houses}
    relationship_targets = {"本命金星": natal.get("金星"), "本命火星": natal.get("火星"),
        "本命月亮": natal.get("月亮"), "第五宫宫头": cusp.get(5),
        "第七宫宫头": cusp.get(7), "第八宫宫头": cusp.get(8)}
    finance_targets = {"本命木星": natal.get("木星"), "本命土星": natal.get("土星"),
        "第二宫宫头": cusp.get(2), "第八宫宫头": cusp.get(8), "第十宫宫头": cusp.get(10)}
    bodies = [("水星", swe.MERCURY), ("金星", swe.VENUS), ("火星", swe.MARS),
        ("木星", swe.JUPITER), ("土星", swe.SATURN), ("天王星", swe.URANUS),
        ("海王星", swe.NEPTUNE), ("冥王星", swe.PLUTO)]
    aspect_defs = [(0, "合相"), (60, "六分相"), (90, "四分相"), (120, "三分相"), (180, "冲相")]
    buckets = {"relationship": [], "finance": []}
    day = past_start
    while day <= future_end:
        local_noon = datetime(day.year, day.month, day.day, 12, 0, tzinfo=tz)
        utc = local_noon.astimezone(timezone.utc)
        jd = swe.julday(utc.year, utc.month, utc.day, utc.hour + utc.minute / 60, swe.GREG_CAL)
        for planet, body in bodies:
            values, _ = swe.calc_ut(jd, body, swe.FLG_MOSEPH | swe.FLG_SPEED)
            lon = values[0] % 360
            for category, targets in (("relationship", relationship_targets), ("finance", finance_targets)):
                for target, target_lon in targets.items():
                    if target_lon is None: continue
                    separation = angular_distance(lon, target_lon)
                    for exact, aspect in aspect_defs:
                        orb = abs(separation - exact)
                        limit = 1.5 if planet in ("木星", "土星", "天王星", "海王星", "冥王星") else 1.0
                        if orb <= limit:
                            buckets[category].append({"date": day.isoformat(), "transit": planet,
                                "target": target, "aspect": aspect, "orb": round(orb, 2)})
        day += timedelta(days=1)

    target_plain = {
        "本命金星": "你表达喜欢、建立亲近感和判断关系价值的方式",
        "本命火星": "你主动沟通、推进关系和处理分歧的方式",
        "本命月亮": "你的情绪、安全感和日常相处需求",
        "第五宫宫头": "恋爱、约会、兴趣和表达好感",
        "第七宫宫头": "长期伴侣、承诺、合作与相互协商",
        "第八宫宫头": "亲密信任、共同开支和金钱边界",
        "本命木星": "你对机会、增长和扩大收入的判断",
        "本命土星": "工作责任、长期规划和现实限制",
        "第二宫宫头": "个人收入、日常现金流和储蓄",
        "第十宫宫头": "事业方向、工作责任和长期目标"}
    transit_plain = {
        "水星": "沟通、消息、合同和计划安排", "金星": "人际互动、关系感受、消费与价值判断",
        "火星": "行动力、竞争、推进速度和容易起冲突的地方", "木星": "学习、拓展、机会判断和增长预期",
        "土星": "责任、规则、压力以及需要耐心处理的事", "天王星": "临时变化、调整计划和争取自主空间",
        "海王星": "理想与期待，也提醒核实信息、避免想当然", "冥王星": "深层调整、控制边界和重要资源的重新安排"}
    aspect_plain = {
        "合相": "相关主题容易变得突出，注意别因一时感受而过度反应",
        "六分相": "存在可主动把握的协调空间，通常需要自己行动才能转化",
        "四分相": "可能感到不顺或有压力，适合检查计划、预算和边界",
        "三分相": "推进起来可能相对顺手，但仍要留意细节",
        "冲相": "可能出现两种需求拉扯，重点是协调，不要走极端"}
    def date_cn(d):
        return f"{d.month}月{d.day}日"
    def summarize(items, begin, finish, domain, future):
        selected = [e for e in items if begin.isoformat() <= e["date"] <= finish.isoformat()]
        grouped = {}
        for e in selected: grouped.setdefault((e["transit"], e["target"], e["aspect"]), []).append(e)
        ranked = sorted(grouped.items(), key=lambda pair: min(x["orb"] for x in pair[1]))[:5]
        if not ranked:
            return ("这30天没有筛选到特别突出的阶段性提醒。这不代表一定没有好事或坏事，"
                "只是目前没有需要特别标出的时间段。请照常安排生活，重要决定以现实信息为准。")
        paragraphs = ["以下日期是值得留意或回顾的时间段，不代表事情一定发生。"]
        for (planet, target, aspect), hits in ranked:
            hits.sort(key=lambda x: x["date"])
            dates = sorted({datetime.strptime(x["date"], "%Y-%m-%d").date() for x in hits})
            windows, first, previous = [], dates[0], dates[0]
            for current in dates[1:]:
                if current == previous + timedelta(days=1): previous = current
                else:
                    windows.append((first, previous)); first = previous = current
            windows.append((first, previous))
            window = "、".join(date_cn(a) if a == z else f"{date_cn(a)}至{date_cn(z)}" for a,z in windows[:2])
            if domain == "感情":
                action = ("建议把话说清楚，观察对方是否言行一致；涉及承诺时先沟通彼此期待，不要急着下结论。"
                    if future else "可以回想这段时间是否出现沟通增多、情绪起伏或关系边界需要协商的情况；没有对应经历也不必硬套。")
            else:
                action = ("建议检查报价、成本、回款和合同细节，不要只凭乐观预期借钱、囤货或扩大投入。"
                    if future else "可以回顾订单、支出、回款和工作安排，看看是否有计划调整或风险核查的需要。")
            paragraphs.append(
                f"【{window}｜这段时间的重点】\n"
                f"这段时间较值得留意的是：{target_plain.get(target, '相关生活事项')}。"
                f"{aspect_plain.get(aspect, '建议留意相关变化')}。"
                f"{action}")
        return "\n\n".join(paragraphs) + "\n\n说明：这些日期是阶段性提醒，不代表某件事一定发生。请结合自己的真实经历和现实情况判断。"
    def make_period(title, begin, finish, items, domain, future):
        return {"title": title, "plain_content": summarize(items, begin, finish, domain, future),
            "content": f"计算区间：{begin.isoformat()} 至 {finish.isoformat()}（出生地时区：{birth_timezone}）。按当地每日中午的行运行星位置，筛选与本命感情或财务关键点形成较紧密主要相位的日期。日期为近似活跃窗口，不是精确过境时刻。",
            "period_start": begin.isoformat(), "period_end": finish.isoformat(),
            "period_type": "future" if future else "past"}
    return {
        "relationship": [
            make_period("过去30天｜感情回顾", past_start, today, buckets["relationship"], "感情", False),
            make_period("未来30天｜感情提醒", today + timedelta(days=1), future_end, buckets["relationship"], "感情", True)],
        "finance": [
            make_period("过去30天｜财务回顾", past_start, today, buckets["finance"], "财运", False),
            make_period("未来30天｜财务提醒", today + timedelta(days=1), future_end, buckets["finance"], "财运", True)],
        "as_of": now_local.isoformat(timespec="minutes"),
        "method": "使用 Moshier 行运行星位置，按出生地当地日期逐日扫描；只筛选与本命关键点容许度较紧的主要相位。占星内容属于自我观察参考，不是科学验证的事件预测。"
    }


def calculate_chart(payload):
    required = ["birth_date", "birth_time"]
    missing = [key for key in required if not payload.get(key)]
    if missing:
        raise ValueError("缺少必填字段：" + ", ".join(missing))

    # Resolve the birthplace first, then derive its IANA time zone. A fixed
    # front-end default would silently miscalculate charts for users abroad.
    if payload.get("latitude") is not None and payload.get("longitude") is not None:
        lat = float(payload["latitude"])
        lon = float(payload["longitude"])
        place_label = payload.get("place", "用户提供坐标")
    elif payload.get("place"):
        lat, lon, place_label = geocode_place(str(payload["place"]))
    else:
        raise ValueError("请提供出生地点，或同时提供 latitude 和 longitude。")

    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("经纬度超出有效范围。")
    detected_tz = TimezoneFinder().timezone_at(lat=lat, lng=lon)
    requested_tz = str(payload.get("timezone") or "").strip()
    if requested_tz:
        tz_name = requested_tz
    elif detected_tz:
        tz_name = detected_tz
    else:
        raise ValueError("无法根据出生地点确定时区，请补充有效的 IANA 时区名称。")

    try:
        tz = ZoneInfo(tz_name)
    except Exception:
        raise ValueError("无效的时区名称，请使用 IANA 时区，例如 Asia/Shanghai。")

    local_naive = datetime.strptime(
        payload["birth_date"] + " " + payload["birth_time"], "%Y-%m-%d %H:%M"
    )
    # Detect daylight-saving gaps and repeated local clock times. Historical
    # IANA rules are applied for the actual birth date, not today's UTC offset.
    valid_folds = []
    for fold in (0, 1):
        candidate = local_naive.replace(tzinfo=tz, fold=fold)
        roundtrip = candidate.astimezone(timezone.utc).astimezone(tz).replace(tzinfo=None)
        if roundtrip == local_naive:
            valid_folds.append(candidate)
    if not valid_folds:
        raise ValueError("该出生地日期的当地时间处于夏令时跳时区间，钟表时间不存在，请核对出生记录。")
    timezone_warning = []
    if requested_tz and detected_tz and requested_tz != detected_tz:
        timezone_warning.append(
            f"手动指定时区 {requested_tz} 与出生坐标识别时区 {detected_tz} 不一致，请核对出生地和当地时间。"
        )
    distinct_offsets = {candidate.utcoffset() for candidate in valid_folds}
    if len(distinct_offsets) > 1:
        requested_fold = payload.get("fold")
        if requested_fold in (0, 1, "0", "1"):
            local_dt = local_naive.replace(tzinfo=tz, fold=int(requested_fold))
        else:
            local_dt = local_naive.replace(tzinfo=tz, fold=0)
            timezone_warning.append("出生时间处于夏令时重复时段，系统暂按第一次出现的当地时间计算；请核对当时钟表记录。")
    else:
        local_dt = valid_folds[0]
    utc_dt = local_dt.astimezone(timezone.utc)

    # Convert UTC to Julian day. Moshier is explicitly selected so the API
    # never claims to be using Swiss Ephemeris data files when none are installed.
    hour = utc_dt.hour + utc_dt.minute / 60 + utc_dt.second / 3600
    jd_ut = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, hour, swe.GREG_CAL)
    flags = swe.FLG_MOSEPH | swe.FLG_SPEED

    positions = []
    longitudes = {}
    speeds = {}
    for name, body in PLANETS:
        values, returned_flags = swe.calc_ut(jd_ut, body, flags)
        longitude = values[0] % 360
        speed = values[3]
        longitudes[name] = longitude
        speeds[name] = speed
        item = sign_position(longitude)
        item.update({
            "name": name,
            "retrograde": speed < 0,
            "longitude_speed_per_day": round(speed, 6)
        })
        positions.append(item)

    # South Node is exactly opposite the calculated True North Node.
    south = sign_position((longitudes["北交点"] + 180) % 360)
    south.update({"name": "南交点", "retrograde": speeds["北交点"] < 0, "longitude_speed_per_day": round(speeds["北交点"], 6)})
    positions.append(south)
    longitudes["南交点"] = south["longitude"]
    speeds["南交点"] = speeds["北交点"]

    try:
        cusps, ascmc = swe.houses_ex(jd_ut, lat, lon, b'P')
    except Exception as exc:
        raise ValueError("此纬度下 Placidus 宫位计算失败；请核对地点，或后续选择其他宫位系统。") from exc

    asc = sign_position(ascmc[0])
    mc = sign_position(ascmc[1])
    angles = {
        "上升点": asc,
        "天顶": mc,
        "下降点": sign_position((ascmc[0] + 180) % 360),
        "天底": sign_position((ascmc[1] + 180) % 360)
    }

    houses = []
    for index, cusp in enumerate(cusps, start=1):
        point = sign_position(cusp)
        point["house"] = index
        houses.append(point)

    def house_for(longitude):
        for i in range(12):
            start = float(cusps[i]) % 360
            end = float(cusps[(i + 1) % 12]) % 360
            span = (end - start) % 360
            offset = (longitude - start) % 360
            if offset < span or (i == 11 and abs(offset - span) < 1e-7):
                return i + 1
        return None

    for item in positions:
        item["house"] = house_for(item["longitude"])

    aspects = []
    names = list(longitudes.keys())
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a_name, b_name = names[i], names[j]
            a_lon, b_lon = longitudes[a_name], longitudes[b_name]
            separation = angular_distance(a_lon, b_lon)
            relative_speed = speeds[a_name] - speeds[b_name]
            for exact, aspect_name in ASPECTS:
                deviation = abs(separation - exact)
                orb_limit = 8 if exact in (0, 180) else 6
                if deviation <= orb_limit:
                    # The absolute aspect deviation is shrinking when applying.
                    signed = (a_lon - b_lon + 180) % 360 - 180
                    derivative = relative_speed * (1 if signed >= 0 else -1)
                    applying = (separation - exact) * derivative < 0
                    phase = "精确" if deviation < 0.001 else ("趋近" if applying else "分离")
                    aspects.append({
                        "planet_a": a_name, "planet_b": b_name,
                        "aspect": aspect_name, "angle": exact,
                        "orb": round(deviation, 3),
                        "phase": phase
                    })
    aspects.sort(key=lambda x: x["orb"])

    patterns = detect_chart_patterns(positions, aspects)

    return {
        "calculation": {
            "engine": "pyswisseph / Moshier ephemeris",
            "ephemeris_source": "Moshier analytical ephemeris (not Swiss Ephemeris data files)",
            "zodiac": "Tropical",
            "house_system": "Placidus",
            "julian_day_ut": round(jd_ut, 8)
        },
        "birth": {
            "local_datetime": local_dt.isoformat(),
            "utc_datetime": utc_dt.isoformat(),
            "timezone": tz_name,
            "place_resolved": place_label,
            "latitude": round(lat, 6),
            "longitude": round(lon, 6)
        },
        "planets": positions,
        "angles": angles,
        "houses": houses,
        "aspects": aspects,
        "patterns": patterns,
        "analysis": generate_life_analysis(positions, angles, houses, aspects, patterns),
        "natal_profile": generate_natal_profile(positions, angles, houses, aspects, patterns),
        "monthly_transits": generate_monthly_transit_analysis(positions, houses, tz_name),
        "warnings": timezone_warning + [
            "当前使用 Moshier 星历算法，不是 Swiss Ephemeris 星历数据文件；结果应标注数据来源。",
            "使用地名查询时，出生地点文本会发送给 OpenStreetMap Nominatim 地理编码服务；如不希望发送地名，可改为直接提交经纬度。",
            "出生地点若由地名自动解析，坐标可能是城镇中心或地名匹配点，不一定是实际出生地点。",
            "占星解释属于文化与自我探索内容，不构成科学预测。"
        ]
    }


AI_TOPICS = {"personality", "relationship", "finance", "career", "trends"}


def build_ai_evidence(chart, topic):
    """Create a minimized, auditable evidence packet; never send birth identity data."""
    if not isinstance(chart, dict):
        raise ValueError("缺少有效的星盘数据。")
    planets = chart.get("planets") or []
    angles = chart.get("angles") or {}
    houses = chart.get("houses") or []
    aspects = chart.get("aspects") or []
    patterns = chart.get("patterns") or []
    if not planets or not houses:
        raise ValueError("星盘数据不完整，请先完成本命盘计算。")

    selected_planets = {
        "personality": {"太阳", "月亮", "水星", "金星", "火星", "土星"},
        "relationship": {"月亮", "金星", "火星", "土星", "木星"},
        "finance": {"木星", "土星", "金星", "水星", "火星"},
        "career": {"太阳", "水星", "火星", "木星", "土星"},
        "trends": {"太阳", "月亮", "金星", "火星", "木星", "土星"}
    }[topic]
    relevant_houses = {
        "personality": {1, 3, 5, 10},
        "relationship": {5, 7, 8},
        "finance": {2, 8, 10, 11},
        "career": {2, 6, 10, 11},
        "trends": {1, 2, 5, 7, 8, 10, 11}
    }[topic]

    # Traditional sign rulers are included so the model can connect a house
    # topic to the planet managing that house, rather than reading cusp signs alone.
    sign_rulers = {
        "白羊座": "火星", "金牛座": "金星", "双子座": "水星",
        "巨蟹座": "月亮", "狮子座": "太阳", "处女座": "水星",
        "天秤座": "金星", "天蝎座": "火星", "射手座": "木星",
        "摩羯座": "土星", "水瓶座": "土星", "双鱼座": "木星"
    }
    planet_by_name = {p.get("name"): p for p in planets}
    ruler_targets = set()
    if topic == "personality":
        asc_sign = (angles.get("上升点") or {}).get("sign")
        if asc_sign in sign_rulers:
            ruler_targets.add(("上升点", sign_rulers[asc_sign]))
    if topic == "career":
        mc_sign = (angles.get("天顶") or {}).get("sign")
        if mc_sign in sign_rulers:
            ruler_targets.add(("天顶", sign_rulers[mc_sign]))
    for house in houses:
        if house.get("house") in relevant_houses and house.get("sign") in sign_rulers:
            ruler_targets.add(("第" + str(house.get("house")) + "宫", sign_rulers[house["sign"]]))

    evidence = []
    for p in planets:
        if p.get("name") in selected_planets:
            evidence.append({
                "id": "planet_" + str(p.get("name")),
                "type": "natal_planet",
                "name": p.get("name"),
                "sign": p.get("sign"),
                "degree": p.get("degree"),
                "minute": p.get("minute"),
                "house": p.get("house"),
                "retrograde": bool(p.get("retrograde"))
            })
    for name, value in angles.items():
        if name in {"上升点", "天顶", "下降点", "天底"}:
            evidence.append({
                "id": "angle_" + name, "type": "chart_angle",
                "name": name, "sign": value.get("sign"),
                "degree": value.get("degree"), "minute": value.get("minute")
            })
    for h in houses:
        if h.get("house") in relevant_houses:
            evidence.append({
                "id": "house_" + str(h.get("house")), "type": "house_cusp",
                "house": h.get("house"), "sign": h.get("sign"),
                "degree": h.get("degree"), "minute": h.get("minute")
            })
    for source_name, ruler_name in sorted(ruler_targets):
        ruler = planet_by_name.get(ruler_name)
        if ruler:
            evidence.append({
                "id": "ruler_" + source_name + "_" + ruler_name,
                "type": "traditional_house_ruler",
                "topic_point": source_name,
                "ruler": ruler_name,
                "ruler_sign": ruler.get("sign"),
                "ruler_house": ruler.get("house"),
                "retrograde": bool(ruler.get("retrograde")),
                "interpretation_note": "传统守护星；需结合其落座、落宫和相位综合解释"
            })
    for i, aspect in enumerate(aspects):
        names = {aspect.get("planet_a"), aspect.get("planet_b")}
        if names & selected_planets:
            evidence.append({
                "id": "aspect_" + str(i), "type": "natal_aspect",
                "planet_a": aspect.get("planet_a"),
                "planet_b": aspect.get("planet_b"),
                "aspect": aspect.get("aspect"),
                "orb": aspect.get("orb"),
                "phase": aspect.get("phase")
            })
    for i, pattern in enumerate(patterns):
        evidence.append({
            "id": "pattern_" + str(i), "type": "chart_pattern",
            "name": pattern.get("name"),
            "planets": pattern.get("planets"),
            "description": pattern.get("description")
        })
    if topic == "trends":
        # Only include calculated transit text; no birth date, time, place, or name.
        transits = chart.get("monthly_transits")
        if transits:
            evidence.append({"id": "monthly_transits", "type": "calculated_transit_summary", "data": transits})
    if not evidence:
        raise ValueError("没有找到可供分析的有效星盘证据。")
    return evidence


@app.post("/api/ai/analyze")
def ai_analyze():
    payload = request.get_json(silent=True) or {}
    topic = str(payload.get("topic") or "").strip().lower()
    if topic not in AI_TOPICS:
        return jsonify({"ok": False, "error": "分析主题无效。"}), 400
    try:
        evidence = build_ai_evidence(payload.get("chart"), topic)
        result = analyze_with_deepseek(topic, evidence)
        sections = result.get("sections", [])
        if not isinstance(sections, list) or not 3 <= len(sections) <= 5:
            raise DeepSeekError("AI 报告专题数量不符合要求，已拒绝不完整报告。")
        allowed_ids = {item["id"] for item in evidence}
        for section in sections:
            if not isinstance(section, dict) or any(
                not isinstance(section.get(field), str) or not section.get(field).strip()
                for field in ("title", "conclusion", "reasoning", "advice")
            ):
                raise DeepSeekError("AI 报告缺少必要的分析内容，已拒绝不完整报告。")
            ids = section.get("evidence_ids", [])
            if not isinstance(ids, list) or not ids or any(
                not isinstance(item, str) or item not in allowed_ids for item in ids
            ):
                raise DeepSeekError("AI 返回了无法核验的证据编号，已拒绝该报告。")
        return jsonify({"ok": True, "topic": topic, "analysis": result})
    except DeepSeekNotConfigured as exc:
        return jsonify({"ok": False, "error": str(exc)}), 503
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except DeepSeekError as exc:
        app.logger.warning("DeepSeek analysis unavailable: %s", str(exc))
        return jsonify({"ok": False, "error": "AI 深度分析暂时不可用，原有星盘计算报告不受影响。"}), 502
    except Exception as exc:
        app.logger.exception("AI analysis failed")
        return jsonify({"ok": False, "error": "AI 分析发生内部错误（" + type(exc).__name__ + "）。"}), 500


@app.post("/api/ai/full-report")
def ai_full_report():
    """Create a full report from the real natal/transit evidence already calculated."""
    payload = request.get_json(silent=True) or {}
    try:
        chart_data = payload.get("chart")
        if not isinstance(chart_data, dict):
            raise ValueError("缺少有效的星盘数据，请先生成本命盘。")
        # Merge evidence from all five existing domains, keeping the original IDs.
        evidence_by_id = {}
        for topic in ("personality", "relationship", "finance", "career", "trends"):
            for item in build_ai_evidence(chart_data, topic):
                evidence_by_id[item["id"]] = item
        evidence = list(evidence_by_id.values())
        result = generate_full_report(evidence)
        sections = result.get("sections")
        expected_ids = ["identity", "strengths", "mindset", "relationship", "career", "finance", "timing"]
        if not isinstance(sections, list) or len(sections) != 7:
            raise DeepSeekError("完整报告专题数量不符合要求，已拒绝不完整报告。")
        allowed_ids = set(evidence_by_id)
        for expected, section in zip(expected_ids, sections):
            if not isinstance(section, dict) or section.get("id") != expected:
                raise DeepSeekError("完整报告专题结构不完整，已拒绝返回。")
            if any(not isinstance(section.get(field), str) or not section[field].strip()
                   for field in ("title", "conclusion", "reasoning", "advice")):
                raise DeepSeekError("完整报告缺少必要分析内容，已拒绝返回。")
            ids = section.get("evidence_ids")
            if not isinstance(ids, list) or not ids or any(
                not isinstance(value, str) or value not in allowed_ids for value in ids
            ):
                raise DeepSeekError("完整报告包含无法核验的星盘依据，已拒绝返回。")
        plan = result.get("action_plan")
        if not isinstance(plan, list) or not 3 <= len(plan) <= 5 or any(
            not isinstance(item, str) or not item.strip() for item in plan
        ):
            raise DeepSeekError("完整报告缺少可执行行动方案，已拒绝返回。")
        return jsonify({"ok": True, "report_type": "full", "report": result})
    except DeepSeekNotConfigured as exc:
        return jsonify({"ok": False, "error": str(exc)}), 503
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except DeepSeekError as exc:
        app.logger.warning("Full report unavailable: %s", str(exc))
        return jsonify({"ok": False, "error": "完整报告暂时生成失败，原有星盘报告不受影响。请稍后重试。"}), 502
    except Exception as exc:
        app.logger.exception("Full report failed")
        return jsonify({"ok": False, "error": "完整报告发生内部错误（" + type(exc).__name__ + "）。"}), 500


@app.get("/api/tieshan/collections/progress")
def tieshan_collections_progress():
    """Return evidence-based transcription progress for all twelve collections."""
    return jsonify({"ok": True, "progress": get_collection_progress()})


@app.get("/api/tieshan/collections/<branch>/groups")
def tieshan_collection_groups(branch):
    """Return metadata-only group index for a collection."""
    if branch not in ("子", "丑"):
        progress = next((x for x in get_collection_progress()["collections"] if x["collection"] == branch), None)
        return jsonify({"ok": True, "index": {
            "collection": branch, "status": "not_indexed",
            "printed_page_start": progress["printed_page_start"] if progress else None,
            "toc_status": progress["toc_status"] if progress else "not_located",
            "group_count": 0, "entry_count": 0, "groups": []
        }})
    return jsonify({"ok": True, "index": get_collection_branch_group_index(branch)})


@app.get("/api/tieshan/collections/<branch>/entries")
def tieshan_collection_entries(branch):
    """Return source-located clause samples; never imply corpus completeness."""
    if branch not in list("子丑寅卯辰巳午未申酉戌亥"):
        return jsonify({"ok": False, "error": "unsupported_collection"}), 404
    return jsonify({"ok": True, "catalog": get_collection_sample(branch)})


@app.get("/api/tieshan/kunji/glossary")
def tieshan_kunji_glossary():
    """Return source-indexed Kunji category labels, not a cipher decoder."""
    return jsonify({"ok": True, "glossary": get_kunji_glossary()})


@app.get("/api/tieshan/calendar/months")
def tieshan_calendar_months():
    try:
        year = int(request.args.get("year", ""))
        return jsonify({"ok": True, "year": year, "months": lunar_month_options(year)})
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400


@app.post("/api/tieshan/pillars")
def tieshan_pillars():
    """Calculate transparent Four Pillars data for the standalone Iron Plate app."""
    payload = request.get_json(silent=True) or {}
    try:
        if payload.get("latitude") is not None and payload.get("longitude") is not None:
            lat, lon = float(payload["latitude"]), float(payload["longitude"])
            place_label = str(payload.get("place") or "用户提供坐标")
        elif payload.get("place"):
            lat, lon, place_label = geocode_place(str(payload["place"]))
        else:
            raise ValueError("请填写出生地点，或提供经纬度。")
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            raise ValueError("出生地点经纬度超出有效范围。")
        detected_tz = TimezoneFinder().timezone_at(lat=lat, lng=lon)
        timezone_name = str(payload.get("timezone") or detected_tz or "").strip()
        if not timezone_name:
            raise ValueError("无法根据出生地点确定历史时区，请补充 IANA 时区名称。")
        # Convert the selected calendar date to a Gregorian civil date before
        # astronomical Four Pillars calculation. Keep the original calendar data.
        calculation_payload = dict(payload)
        calendar_kind = str(payload.get("calendar") or "solar").lower()
        try:
            birth_year = int(payload.get("birth_year"))
            birth_month = int(payload.get("birth_month"))
            birth_day = int(payload.get("birth_day"))
        except (TypeError, ValueError) as exc:
            raise ValueError("请完整选择出生年、月、日。") from exc
        if calendar_kind == "lunar":
            lunar_year = birth_year
            lunar_month_value = birth_month
            lunar_day = birth_day
            solar_date = lunar_to_solar(lunar_year, lunar_month_value, lunar_day)
            birth_date_text = solar_date.isoformat()
            lunar_info = {
                "year": lunar_year, "month": abs(lunar_month_value),
                "month_value": lunar_month_value, "day": lunar_day,
                "is_leap": lunar_month_value < 0,
            }
        elif calendar_kind == "solar":
            birth_date_text = date(birth_year, birth_month, birth_day).isoformat()
            lunar_info = solar_to_lunar(birth_date_text)
        else:
            raise ValueError("出生日期类型只能选择公历或农历。")
        calculation_payload["birth_date"] = birth_date_text
        calculation_payload["calendar"] = "solar"
        result = calculate_tieshan_pillars(calculation_payload, lat, lon, place_label, timezone_name)
        result["eight_ke"] = derive_eight_ke(
            str(payload.get("birth_time") or ""),
            (result.get("pillars", {}).get("hour") or {}).get("branch"),
        )
        result["birth"]["input_calendar"] = calendar_kind
        result["birth"]["input_date"] = {
            "year": birth_year,
            "month": birth_month,
            "day": birth_day,
            "is_leap": bool(lunar_info.get("is_leap")) if calendar_kind == "lunar" else False,
        }
        result["birth"]["converted_solar_date"] = birth_date_text
        result["birth"]["converted_lunar_date"] = {
            "year": int(lunar_info["year"]), "month": int(lunar_info["month"]),
            "day": int(lunar_info["day"]), "is_leap": bool(lunar_info["is_leap"]),
        }
        # Expose only explicitly documented lookup mappings from the accessible
        # 2003 compilation; this is not a complete Iron Plate number calculation.
        result["bazi_details"] = derive_bazi_details(result.get("pillars") or {})
        result["classic_reference"] = derive_classic_reference(result.get("pillars") or {})
        # Optional classical palace lookup requires an explicitly supplied lunar month;
        # the solar-term month pillar is not a substitute for a lunar month.
        lunar_month = int(lunar_info["month"])
        hour_branch = (result.get("pillars", {}).get("hour") or {}).get("branch")
        result["body_life_palaces"] = derive_body_life_palaces(
            lunar_month, hour_branch, bool(lunar_info["is_leap"])
        )
        result["iron_plate_engine"] = build_tieshan_foundation(
            result.get("birth") or {},
            result.get("pillars") or {},
            result.get("eight_ke"),
            result.get("body_life_palaces"),
            result.get("classic_reference"),
        )
        return jsonify(result)
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except Exception as exc:
        app.logger.exception("Iron Plate pillar calculation failed")
        # Temporary bounded diagnostic for production recovery; never include
        # request payloads, environment variables, or secret values.
        detail = str(exc).replace("\n", " ")[:240]
        return jsonify({
            "ok": False,
            "error": "四柱计算发生内部错误（" + type(exc).__name__ + "）。",
            "diagnostic": detail,
        }), 500


@app.post("/api/tieshan/analyze")
def tieshan_analyze():
    """AI interpretation of already-calculated pillars; not a claimed Iron Plate numbering method."""
    payload = request.get_json(silent=True) or {}
    try:
        result = analyze_tieshan_profile(
            payload.get("pillars"),
            payload.get("birth") or {},
            str(payload.get("gender") or ""),
            payload.get("derived") or {}
        )
        return jsonify({"ok": True, "analysis_type": "四柱基础文化解读", "analysis": result})
    except DeepSeekNotConfigured as exc:
        return jsonify({"ok": False, "error": str(exc)}), 503
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except DeepSeekError as exc:
        app.logger.warning("Iron Plate AI analysis unavailable: %s", str(exc))
        return jsonify({"ok": False, "error": "AI 深度分析暂时不可用，请稍后重试。"}), 502
    except Exception as exc:
        app.logger.exception("Iron Plate AI analysis failed")
        return jsonify({"ok": False, "error": "AI 分析发生内部错误（" + type(exc).__name__ + "）。"}), 500


@app.get("/api/health")
def health():
    return jsonify({"ok": True, "service": "astro-studio-api", "engine": "pyswisseph-moshier"})


@app.post("/api/chart")
def chart():
    payload = request.get_json(silent=True) or {}
    try:
        return jsonify({"ok": True, "chart": calculate_chart(payload)})
    except ValueError as exc:
        return jsonify({"ok": False, "error": str(exc)}), 400
    except Exception as exc:
        app.logger.exception("Chart calculation failed")
        # Return a concise diagnostic class so deployment/runtime faults can be
        # identified without exposing a traceback or server internals.
        return jsonify({
            "ok": False,
            "error": "服务器内部计算异常（" + type(exc).__name__ +
                     "）。请把这条提示发给开发人员。"
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
