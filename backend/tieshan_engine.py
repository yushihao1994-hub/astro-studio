"""Iron Plate Shen Shu workflow foundation with explicit evidence and stop-gates.
This module orchestrates only source-traceable steps already implemented.
It deliberately does not invent a final number, six-relative numbers, or clauses.
"""
SYSTEM_NAME = "铁板神数推演基础引擎"
ENGINE_VERSION = "0.4.0-qing-source-audit"
PRIMARY_REFERENCE = "《神機妙算鐵板數》清刻影印本（用户提供扫描件；核心规则待逐页核验）"
QING_REFERENCE_STATUS = "清刻足本原始PDF共665页；全部665页已完成图像版式初检（100%），但原书印刷页至约1363页的起数、考刻、六亲数、秘钞密码及条文索引仍待逐条转录和验证"
from tieshan_kunji import get_kunji_reference
from tieshan_qing_source import get_qing_source_reference
KUNJI_REFERENCE = get_kunji_reference()
QING_SOURCE_REFERENCE = get_qing_source_reference()
WORKFLOW = [
    {"key":"birth_record","name":"出生资料与历法归档","status":"verified","description":"保存原始历法输入、换算公历日期、农历日期、地点与时区。"},
    {"key":"four_pillars","name":"四柱基础定位","status":"verified","description":"四柱仅作为铁板起数的输入资料，不将普通八字解释当作铁板结论。"},
    {"key":"eight_ke","name":"八刻十五分分段","status":"partial","description":"当前仅按钟表时间切分时辰内八段，尚不等于传统考刻定盘。"},
    {"key":"body_life","name":"安身命宫","status":"partial","description":"清刻本原页已定位，规则正在逐字转录；当前现代点校本函数只作异本参照。"},
    {"key":"classic_tables","name":"乾集基础数理表","status":"partial","description":"目前仅接入异本对照资料；必须与清刻本原页逐项校勘后才能升级，不代表清刻本规则已验证。"},
    {"key":"start_number","name":"起数与卦值日月推数","status":"blocked","description":"缺少完整可复核的连贯例题及全部中间步骤，禁止生成最终铁板数。"},
    {"key":"traditional_examination","name":"考刻定盘","status":"blocked","description":"清刻本已取得；仍需复原六亲校验、刻分推进、历史时刻修正及可复算例题。"},
    {"key":"six_relatives","name":"六亲数推演","status":"blocked","description":"尚未取得可复核的六亲数完整取数公式与例题。"},
    {"key":"cipher_lookup","name":"秘钞密码数与条文定位","status":"blocked","description":"清刻扫描件已取得；附录密码表尚未定位、转录和核验，不生成、不猜测条文编号。"},
    {"key":"life_interpretation","name":"一生命运条文汇编","status":"blocked","description":"必须以已验证的数序命中原文条文后才可解释，不以AI故事替代古籍条文。"},
]
RULE_REGISTRY = [
    {"id":"QIAN-STEM-TRIGRAM","name":"天干配卦例（异本对照）","source":"2003年《康节说易全书·铁板神数》乾集文本行717-731；非清刻本直接证据","source_kind":"modern_edition_comparator","status":"modern_comparator_only_not_qing_verified"},
    {"id":"QIAN-LUOSHU-TRIGRAM","name":"地支配卦例（异本对照）","source":"2003年《康节说易全书·铁板神数》乾集文本行732-737；非清刻本直接证据","source_kind":"modern_edition_comparator","status":"modern_comparator_only_not_qing_verified"},
    {"id":"QIAN-DAYMASTER-TRIGRAM","name":"日主配卦例（异本对照）","source":"2003年《康节说易全书·铁板神数》乾集文本行738-761；非清刻本直接证据","source_kind":"modern_edition_comparator","status":"modern_comparator_only_not_qing_verified"},
    {"id":"QIAN-HELUO-NUMBER","name":"河洛配数例（异本对照）","source":"2003年《康节说易全书·铁板神数》乾集文本行762-787；己字异文待核，非清刻本直接证据","source_kind":"modern_edition_comparator","status":"modern_comparator_only_not_qing_verified"},
    {"id":"QIAN-BRANCH-NUMBER","name":"地支取数例（异本对照）","source":"2003年《康节说易全书·铁板神数》乾集文本行788-808；非清刻本直接证据","source_kind":"modern_edition_comparator","status":"modern_comparator_only_not_qing_verified"},
    {"id":"QIAN-BODY-LIFE","name":"安身命例（异本对照）","source":"2003年《康节说易全书·铁板神数》乾集文本行810-817；闰月口径待核，非清刻本直接证据","source_kind":"modern_edition_comparator","status":"modern_comparator_only_not_qing_verified"},
    {"id":"QIAN-EIGHT-KE","name":"每时八刻、每刻十五分（异本对照）","source":"2003年点校本乾集开篇说明；清刻本另有PDF图像第1页独立候选证据","source_kind":"modern_edition_comparator","status":"modern_comparator_only_qing_candidate_separate"},
    {"id":"QIAN-EIGHT-TRIGRAM-ADD","name":"八卦加则例（异本对照）","source":"2003年点校本乾集文本行684-715；清刻本PDF图像第2页另有口诀候选，须逐字校勘","source_kind":"modern_edition_comparator","status":"modern_comparator_only_qing_variant_pending"},
    {"id":"KUNJI-CIPHER-EDITORIAL","name":"坤集密码代号（2003点校本编者说明）","source":"坤集浅释，PDF文本行250-277；含十天干数字代号与少量示例","status":"partial_editorial_metadata_not_full_cipher"},
    {"id":"QING-FRONT-EIGHT-KE","name":"清刻本八刻十五分说明","source":"用户提供清刻扫描件，PDF图像第1页封面内页","status":"high_resolution_image_transcribed_candidate_pending_second_review"},
    {"id":"QING-TRUE-KE-EXAMINATION","name":"清刻本真刻与考刻原则","source":"用户提供清刻扫描件，PDF图像第1页封面内页","status":"high_resolution_image_transcribed_candidate_pending_second_review"},
    {"id":"QING-EIGHT-TRIGRAM-ADD","name":"清刻本八卦加则例口诀（PDF第2页右页/印刷页5）","source":"用户提供清刻扫描件，PDF图像第2页（印刷页4-5）","status":"image_observed_variant_transcription_pending"},
    {"id":"QING-HELUO-CLAUSES","name":"清刻本河洛配数例（PDF第2页左页/印刷页4）","source":"用户提供清刻扫描件，PDF图像第2页（印刷页4-5）","status":"image_transcribed_candidate_pending_second_review"},
    {"id":"QING-BRANCH-NUMBER","name":"清刻本地支取数例","source":"用户提供清刻扫描件，PDF图像第2页（印刷页4-5）","status":"image_transcribed_candidate_pending_second_review"},
    {"id":"QING-LUOSHU-TRIGRAM","name":"清刻本洛书数卦定局","source":"用户提供清刻扫描件，PDF图像第2页（印刷页4-5）","status":"image_transcribed_candidate_pending_second_review"},
    {"id":"QING-STEM-TRIGRAM","name":"清刻本天干配卦例","source":"用户提供清刻扫描件，PDF图像第2页（印刷页4-5）","status":"image_located_transcription_pending"},
    {"id":"QING-DAYMASTER-TRIGRAM","name":"清刻本日主配卦例","source":"用户提供清刻扫描件，PDF图像第2页（印刷页4-5）","status":"image_located_transcription_pending"},
    {"id":"QING-BODY-LIFE","name":"清刻本安身命例","source":"用户提供清刻扫描件，PDF图像第3页（印刷页6-7）","status":"image_located_transcription_pending"},
    {"id":"QING-P3-HETU-LUOSHU-ORDER","name":"清刻本河图洛书方位次序说明","source":"用户提供清刻扫描件，PDF图像第3页右页（印刷页7）；仅有局部转录候选","status":"partial_image_transcription_candidate"},
]


def is_kaoke_attestation_trusted(kaoke_result):
    """Fail closed: client-supplied 'verified' flags are not proof of examination.

    This remains False until a server-side Qing-source calculation and
    reproducible case verifier are implemented and issue a trusted attestation.
    """
    return False


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
        "available_foundations": {"eight_ke":eight_ke,"body_life_palaces":body_life_palaces,"classic_reference":classic_reference, "eight_trigram_addition":classic_reference.get("eight_trigram_addition"), "kunji_reference":KUNJI_REFERENCE, "qing_source_reference":QING_SOURCE_REFERENCE},
        "workflow": steps, "rule_registry": [dict(item) for item in RULE_REGISTRY],
        "stop_reasons": [
            "清刻足本原始PDF共665页，全部扫描页已完成图像版式初检；核心规则和附录密码表尚未完整转录、复算和验证。",
            "2003年点校本乾集规则仅作异本对照；代码中的QIAN条目不得冒充清刻本已验证规则。该版本与清刻本的逐条异文校勘尚未完成。",
            "完整起数、考刻、六亲数、秘钞密码表和条文编号匹配尚未形成可逐步复算的证据链。",
            "在上述关键环节补齐并通过原文例题回归测试之前，不输出所谓最终铁板定数或人生断语。",
        ],
    }