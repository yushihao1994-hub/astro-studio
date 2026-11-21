"""Iron Plate Shen Shu workflow foundation with explicit evidence and stop-gates.
This module orchestrates only source-traceable steps already implemented.
It deliberately does not invent a final number, six-relative numbers, or clauses.
"""
SYSTEM_NAME = "铁板神数推演基础引擎"
ENGINE_VERSION = "0.3.0-kunji-reference"
PRIMARY_REFERENCE = "康节说易全书·铁板神数，学林出版社2003年陈明点校本（现代异本）"
QING_REFERENCE_STATUS = "清刻虚白庐藏本及秘钞密码表全文尚未取得，不能标记为已验证"
from backend.tieshan_kunji import get_kunji_reference
KUNJI_REFERENCE = get_kunji_reference()
WORKFLOW = [
    {"key":"birth_record","name":"出生资料与历法归档","status":"verified","description":"保存原始历法输入、换算公历日期、农历日期、地点与时区。"},
    {"key":"four_pillars","name":"四柱基础定位","status":"verified","description":"四柱仅作为铁板起数的输入资料，不将普通八字解释当作铁板结论。"},
    {"key":"eight_ke","name":"八刻十五分分段","status":"partial","description":"当前仅按钟表时间切分时辰内八段，尚不等于传统考刻定盘。"},
    {"key":"body_life","name":"安身命宫","status":"partial","description":"按已核对现代点校本安身命例定位；闰月进位仍待异本核验。"},
    {"key":"classic_tables","name":"乾集基础数理表","status":"partial","description":"分开保存天干配卦、洛书数卦、日主配卦、河洛配数及地支取数类。"},
    {"key":"start_number","name":"起数与卦值日月推数","status":"blocked","description":"缺少完整可复核的连贯例题及全部中间步骤，禁止生成最终铁板数。"},
    {"key":"traditional_examination","name":"考刻定盘","status":"blocked","description":"需要版本明确的考刻规则、六亲校验资料与历史时间修正。"},
    {"key":"six_relatives","name":"六亲数推演","status":"blocked","description":"尚未取得可复核的六亲数完整取数公式与例题。"},
    {"key":"cipher_lookup","name":"秘钞密码数与条文定位","status":"blocked","description":"清刻足本附录密码表全文未取得，不生成、不猜测条文编号。"},
    {"key":"life_interpretation","name":"一生命运条文汇编","status":"blocked","description":"必须以已验证的数序命中原文条文后才可解释，不以AI故事替代古籍条文。"},
]
RULE_REGISTRY = [
    {"id":"QIAN-STEM-TRIGRAM","name":"天干配卦例","source":"乾集，PDF文本行717-731","status":"verified_table"},
    {"id":"QIAN-LUOSHU-TRIGRAM","name":"地支配卦例（洛书数卦定局）","source":"乾集，PDF文本行732-737","status":"verified_table"},
    {"id":"QIAN-DAYMASTER-TRIGRAM","name":"日主配卦例","source":"乾集，PDF文本行738-761","status":"verified_table"},
    {"id":"QIAN-HELUO-NUMBER","name":"河洛配数例","source":"乾集，PDF文本行762-787；己字存在原文重叠","status":"verified_with_ambiguity"},
    {"id":"QIAN-BRANCH-NUMBER","name":"地支取数例","source":"乾集，PDF文本行788-808","status":"verified_table"},
    {"id":"QIAN-BODY-LIFE","name":"安身命例","source":"乾集，PDF文本行810-817；闰月口径待核","status":"partial"},
    {"id":"QIAN-EIGHT-KE","name":"每时八刻、每刻十五分","source":"乾集开篇说明；当前只实现钟表分段","status":"partial"},
    {"id":"QIAN-EIGHT-TRIGRAM-ADD","name":"八卦加则例","source":"乾集，PDF文本行684-715；逐句解说行699-715","status":"documented_conceptual_only"},
    {"id":"KUNJI-CIPHER-EDITORIAL","name":"坤集密码代号（点校本编者说明）","source":"坤集浅释，PDF文本行250-277；含十天干数字代号与少量示例","status":"partial_editorial_metadata_not_full_cipher"},
]

def build_tieshan_foundation(birth, pillars, eight_ke=None, body_life_palaces=None, classic_reference=None):
    """Assemble auditable Iron Plate stages without pretending the method is complete."""
    if not isinstance(pillars, dict) or any(k not in pillars for k in ("year","month","day","hour")):
        raise ValueError("铁板神数基础引擎需要完整四柱输入。")
    birth = birth if isinstance(birth, dict) else {}
    classic_reference = classic_reference if isinstance(classic_reference, dict) else {}
    steps = []
    for item in WORKFLOW:
        entry = dict(item)
        if item["key"] == "eight_ke":
            entry["status"] = "partial" if eight_ke else "blocked"
            entry["available"] = bool(eight_ke)
        elif item["key"] == "body_life":
            entry["status"] = "partial" if body_life_palaces else "blocked"
            entry["available"] = bool(body_life_palaces)
        elif item["key"] == "classic_tables":
            entry["status"] = "partial" if classic_reference.get("pillars") else "blocked"
            entry["available"] = bool(classic_reference.get("pillars"))
        else:
            entry["available"] = item["status"] == "verified"
        steps.append(entry)
    return {
        "system": SYSTEM_NAME, "engine_version": ENGINE_VERSION,
        "primary_reference": PRIMARY_REFERENCE, "qing_reference_status": QING_REFERENCE_STATUS,
        "overall_status": "foundation_only", "can_generate_final_iron_plate_number": False,
        "birth_basis": {key: birth.get(key) for key in ("input_calendar","input_date","converted_solar_date","converted_lunar_date","place_resolved","timezone")},
        "four_pillars": {key: {field: (pillars.get(key) or {}).get(field) for field in ("name","stem","branch")} for key in ("year","month","day","hour")},
        "available_foundations": {"eight_ke":eight_ke,"body_life_palaces":body_life_palaces,"classic_reference":classic_reference, "eight_trigram_addition":classic_reference.get("eight_trigram_addition"), "kunji_reference":KUNJI_REFERENCE},
        "workflow": steps, "rule_registry": [dict(item) for item in RULE_REGISTRY],
        "stop_reasons": [
            "目前可访问的资料为2003年现代点校本部分可检索文本，不是清刻虚白庐藏本完整影印件。",
            "完整起数、考刻、六亲数、秘钞密码表和条文编号匹配尚未形成可逐步复算的证据链。",
            "在上述关键环节补齐并通过原文例题回归测试之前，不输出所谓最终铁板定数或人生断语。",
        ],
    }