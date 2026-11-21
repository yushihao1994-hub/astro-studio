"""Version-isolated Kunji cipher metadata from the editorial explanation in the
2003 punctuated edition of 康节说易全书·铁板神数.

This is NOT a recovered Qing manuscript cipher table. It records only the
digit legend and examples explicitly printed in the edition's introductory
explanation. It deliberately does not implement a universal cipher decoder.
"""

EDITION = "康节说易全书·铁板神数，学林出版社，2003，陈明点校"
SOURCE = "坤集浅释，PDF文本行250-277"
SOURCE_KIND = "modern_editorial_explanation"
STATUS = "partial_metadata_not_full_cipher"

# The editor's explanation explicitly prints these mappings.
STEM_TO_CIPHER_DIGIT = {
    "甲": "1", "丙": "2", "戊": "3", "庚": "4", "壬": "5",
    "乙": "6", "丁": "7", "己": "8", "辛": "9", "癸": "0",
}
PLACEHOLDER_TO_CIPHER_DIGIT = {"月": "0", "支": "0"}

# Preserve exact worked examples as evidence; do not infer unprinted rules.
PUBLISHED_CIPHER_EXAMPLES = [
    {"code": "辛月月戊", "number": "9003", "meaning": "乾宫甲流度示例"},
    {"code": "辛月壬戊", "number": "9053", "meaning": "乾宫甲流度示例"},
    {"code": "庚丁庚乙", "number": "4746", "meaning": "纳乾坤屯卦示例"},
    {"code": "丙月辛辛", "number": "2099", "meaning": "纳乾坤屯卦示例"},
    {"code": "戊己月辛", "number": "3809", "meaning": "日月并明卦示例"},
    {"code": "辛丁乙丁", "number": "9767", "meaning": "木宫甲流度示例"},
    {"code": "丙庚月戌", "number": "2403", "meaning": "纳民虚实交示例"},
]

# The explanation says the initial code is a first刻; if it does not fit,
# the operator advances by刻/分 increments. It does not define a complete,
# independently reproducible selection procedure.
ADVANCEMENT_NOTE = {
    "source_lines": "274-277",
    "editorial_statement": "初刻不准确时可向前推进加分；条目不合可再推进，示例提到10分或30分。",
    "status": "editorial_guidance_only",
    "not_implemented": True,
}

LIMITATIONS = [
    "此表仅为2003年点校本导读中的编者说明，不等于清刻本秘钞密码表。",
    "“月”“支”均记作0的说明，与个别示例中地支戌对应末位3的表现存在无法由当前说明独立解释之处；保留示例，不推导支的通用编码。",
    "没有取得完整坤集密码页、全部条文及对应索引，不生成任何新条号或断语。",
    "刻分推进规则只记录编者说明，不作为自动考刻算法。",
    "任何条文解释都必须绑定版本、原文与出处，不能将不同传本混合。",
]


def get_kunji_reference():
    """Return source-labelled editorial metadata; never calculate a fortune number."""
    return {
        "edition": EDITION,
        "source": SOURCE,
        "source_kind": SOURCE_KIND,
        "status": STATUS,
        "stem_to_cipher_digit": dict(STEM_TO_CIPHER_DIGIT),
        "placeholder_to_cipher_digit": dict(PLACEHOLDER_TO_CIPHER_DIGIT),
        "published_examples": [dict(row) for row in PUBLISHED_CIPHER_EXAMPLES],
        "advancement_note": dict(ADVANCEMENT_NOTE),
        "limitations": list(LIMITATIONS),
    }


def audit_published_example(example):
    """Audit only explicitly documented symbols; never guess unknown characters."""
    code = example.get("code", "")
    published = str(example.get("number", ""))
    mapping = {**STEM_TO_CIPHER_DIGIT, **PLACEHOLDER_TO_CIPHER_DIGIT}
    known_digits = "".join(mapping[ch] for ch in code if ch in mapping)
    unresolved = [ch for ch in code if ch not in mapping]
    return {
        "code": code,
        "published_number": published,
        "known_symbol_digits": known_digits,
        "unresolved_symbols": unresolved,
        "full_match": not unresolved and known_digits == published,
        "status": "fully_reproduced" if not unresolved and known_digits == published else "partial_match_requires_source_rule",
    }
