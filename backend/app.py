import os
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from flask import Flask, jsonify, request
from flask_cors import CORS
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import swisseph as swe

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
    geolocator = Nominatim(user_agent="astro-studio/0.1 (birth chart calculation)")
    try:
        result = geolocator.geocode(place, exactly_one=True, timeout=12)
    except Exception as exc:
        app.logger.exception("Birthplace geocoding failed")
        raise ValueError(
            "出生地点解析服务暂时不可用（" + type(exc).__name__ +
            "）。请稍后重试，或改用经纬度计算。"
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


def generate_life_analysis(positions, angles, houses, aspects):
    """Generate transparent, rule-based astrology themes from calculated chart factors."""
    by_name = {p["name"]: p for p in positions}
    cusp_by_house = {h["house"]: h for h in houses}

    def planet(name):
        return by_name.get(name, {})

    def house_of(name):
        return planet(name).get("house")

    def ruler_of(house_no):
        cusp = cusp_by_house.get(house_no, {})
        sign = cusp.get("sign")
        ruler = SIGN_RULERS.get(sign)
        return sign, ruler, planet(ruler) if ruler else {}

    def aspects_for(name):
        return [a for a in aspects if a["planet_a"] == name or a["planet_b"] == name]

    def aspect_text(names, limit=4):
        selected = [a for a in aspects if a["planet_a"] in names and a["planet_b"] in names]
        selected = sorted(selected, key=lambda a: a["orb"])[:limit]
        if not selected:
            return "相关主要相位不突出，解读更侧重星体落座与宫位。"
        return "；".join(
            f'{a["planet_a"]}与{a["planet_b"]}{a["aspect"]}（容许度{a["orb"]}°，{a["phase"]}）'
            for a in selected
        ) + "。"

    venus, mars, moon = planet("金星"), planet("火星"), planet("月亮")
    fifth_sign, fifth_ruler, fifth_ruler_pos = ruler_of(5)
    seventh_sign, seventh_ruler, seventh_ruler_pos = ruler_of(7)
    eighth_sign, eighth_ruler, eighth_ruler_pos = ruler_of(8)
    second_sign, second_ruler, second_ruler_pos = ruler_of(2)
    tenth_sign, tenth_ruler, tenth_ruler_pos = ruler_of(10)
    jupiter, saturn = planet("木星"), planet("土星")

    relationship = [
        {
            "title": "情感需求与恋爱表达",
            "content": (
                f'金星落在{venus.get("sign", "未知")}，位于第{venus.get("house", "未知")}宫，'
                f'对应的情感表达风格是：{SIGN_STYLE.get(venus.get("sign"), "需要结合完整星盘判断")}。'
                f'月亮落在{moon.get("sign", "未知")}、第{moon.get("house", "未知")}宫，'
                f'反映内在安全感更容易从{SIGN_STYLE.get(moon.get("sign"), "情绪理解与稳定回应")}中获得。'
                f'金星所在宫位涉及{PLANET_HOUSE_MEANING.get(venus.get("house"), "个人生活主题")}；'
                f'这说明关系体验容易与该生活领域相互牵动。'
            )
        },
        {
            "title": "吸引力、主动方式与恋爱节奏",
            "content": (
                f'火星落在{mars.get("sign", "未知")}、第{mars.get("house", "未知")}宫，'
                f'行动方式偏向{SIGN_STYLE.get(mars.get("sign"), "需要结合全盘判断")}。'
                f'第五宫宫头为{fifth_sign or "未知"}，传统宫主星为{fifth_ruler or "未知"}，'
                f'该宫主星落在{fifth_ruler_pos.get("sign", "未知")}、第{fifth_ruler_pos.get("house", "未知")}宫。'
                f'恋爱机会、兴趣活动与表达好感的方式，适合结合这颗宫主星所在宫位观察。'
            )
        },
        {
            "title": "长期伴侣与婚姻关系",
            "content": (
                f'第七宫宫头为{seventh_sign or "未知"}，传统宫主星为{seventh_ruler or "未知"}，'
                f'宫主星落在{seventh_ruler_pos.get("sign", "未知")}、第{seventh_ruler_pos.get("house", "未知")}宫。'
                f'第七宫主题是承诺、平等协商、长期伴侣与一对一合作；'
                f'宫主星所在的{PLANET_HOUSE_MEANING.get(seventh_ruler_pos.get("house"), "相关生活领域")}，'
                f'是理解长期关系如何融入人生的重要线索。'
            )
        },
        {
            "title": "亲密关系中的优势与挑战",
            "content": (
                f'金星、火星、月亮相关相位：{aspect_text(["金星", "火星", "月亮"], 6)}'
                f'相位描述的是不同心理需求之间较顺畅或较需要磨合的部分，不等于关系必然幸福或失败。'
                f'第八宫宫头为{eighth_sign or "未知"}，其传统宫主星{eighth_ruler or "未知"}'
                f'落在第{eighth_ruler_pos.get("house", "未知")}宫，也可用于观察信任、亲密边界和共享资源议题。'
            )
        },
        {
            "title": "关系经营建议",
            "content": (
                "把情绪需求说清楚，不用猜测代替沟通；在承诺、金钱、家庭责任和个人空间上提前协商。"
                "观察现实中的尊重、稳定、诚实与冲突修复能力，比单一星座或相位更能判断关系质量。"
            )
        }
    ]

    finance = [
        {
            "title": "个人赚钱方式与收入结构",
            "content": (
                f'第二宫宫头为{second_sign or "未知"}，传统宫主星为{second_ruler or "未知"}，'
                f'宫主星落在{second_ruler_pos.get("sign", "未知")}、第{second_ruler_pos.get("house", "未知")}宫。'
                f'第二宫重点对应个人劳动收入、可支配资源、技能定价与储蓄习惯；'
                f'宫主星所在的{PLANET_HOUSE_MEANING.get(second_ruler_pos.get("house"), "相关生活领域")}，'
                f'可作为探索收入渠道与变现能力的占星线索。'
            )
        },
        {
            "title": "扩张机会与长期积累",
            "content": (
                f'木星落在{jupiter.get("sign", "未知")}、第{jupiter.get("house", "未知")}宫，'
                f'其所在宫位涉及{PLANET_HOUSE_MEANING.get(jupiter.get("house"), "个人成长领域")}；'
                f'土星落在{saturn.get("sign", "未知")}、第{saturn.get("house", "未知")}宫，'
                f'提示需要通过该领域的纪律、经验和长期投入建立稳定性。'
                f'木星与土星相位：{aspect_text(["木星", "土星"], 3)}'
            )
        },
        {
            "title": "事业与财富的连接",
            "content": (
                f'第十宫宫头为{tenth_sign or "未知"}，传统宫主星为{tenth_ruler or "未知"}，'
                f'宫主星落在{tenth_ruler_pos.get("sign", "未知")}、第{tenth_ruler_pos.get("house", "未知")}宫。'
                f'天顶位于{angles.get("天顶", {}).get("sign", "未知")}。'
                f'第十宫与天顶用于观察职业方向、公众角色和长期发展；'
                f'将其与第二宫个人收入主题对照，能看出事业投入如何可能转化为收入。'
            )
        },
        {
            "title": "合作资金、债务与风险边界",
            "content": (
                f'第八宫宫头为{eighth_sign or "未知"}，宫主星{eighth_ruler or "未知"}'
                f'落在{eighth_ruler_pos.get("sign", "未知")}、第{eighth_ruler_pos.get("house", "未知")}宫。'
                f'第八宫涉及借贷、税务、保险、投资共担、伴侣或合作方资金。'
                f'相关星体相位：{aspect_text(["木星", "土星", "冥王星"], 5)}'
                f'现实中应特别重视合同、现金流、负债成本、风险分散与应急储备。'
            )
        },
        {
            "title": "财富管理与行动建议",
            "content": (
                "把收入能力、现金流和资产积累分开管理；先建立稳定可重复的收入来源，再考虑扩大规模。"
                "避免因乐观预期而过度借贷、重仓或替他人承担不清晰的财务责任。"
                "星盘不能预测具体收入金额、发财年份或投资涨跌，重大财务决策应依据真实数据和专业意见。"
            )
        }
    ]

    return {
        "relationship": {
            "title": "婚姻与感情深度分析",
            "intro": "本报告综合金星、火星、月亮、第五宫、第七宫、第八宫及相关相位。它描述关系倾向，不代表婚姻结果或必然事件。",
            "sections": relationship
        },
        "finance": {
            "title": "财运与财富结构深度分析",
            "intro": "本报告综合第二宫、第八宫、第十宫、木星、土星及相关相位。它用于整理赚钱与风险管理主题，不是收益承诺或投资建议。",
            "sections": finance
        },
        "method": "宫主星采用传统守护星体系；文字由本命盘实际落座、宫位与主要相位规则生成。"
    }

def calculate_chart(payload):
    required = ["birth_date", "birth_time", "timezone"]
    missing = [key for key in required if not payload.get(key)]
    if missing:
        raise ValueError("缺少必填字段：" + ", ".join(missing))

    tz_name = str(payload["timezone"])
    try:
        tz = ZoneInfo(tz_name)
    except Exception:
        raise ValueError("无效的时区名称，请使用 IANA 时区，例如 Asia/Shanghai。")

    local_naive = datetime.strptime(
        payload["birth_date"] + " " + payload["birth_time"], "%Y-%m-%d %H:%M"
    )
    local_dt = local_naive.replace(tzinfo=tz)
    utc_dt = local_dt.astimezone(timezone.utc)

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
    timezone_warning = []
    if detected_tz and detected_tz != tz_name:
        timezone_warning.append(f"所选时区 {tz_name} 与坐标推算时区 {detected_tz} 不一致，请核对出生地当地时间。")

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
                    aspects.append({
                        "planet_a": a_name, "planet_b": b_name,
                        "aspect": aspect_name, "angle": exact,
                        "orb": round(deviation, 3),
                        "phase": "趋近" if applying else "分离"
                    })
    aspects.sort(key=lambda x: x["orb"])

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
        "analysis": generate_life_analysis(positions, angles, houses, aspects),
        "warnings": timezone_warning + [
            "当前使用 Moshier 星历算法，不是 Swiss Ephemeris 星历数据文件；结果应标注数据来源。",
            "使用地名查询时，出生地点文本会发送给 OpenStreetMap Nominatim 地理编码服务；如不希望发送地名，可改为直接提交经纬度。",
            "出生地点若由地名自动解析，坐标可能是城镇中心或地名匹配点，不一定是实际出生地点。",
            "占星解释属于文化与自我探索内容，不构成科学预测。"
        ]
    }


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
