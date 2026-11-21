"""Reference mappings transcribed from the 2003 Xuelin edition of 康节说易全书·铁板神数.

This is a secondary printed compilation, NOT the Qing 虚白庐藏本 and NOT proof
of a complete/authoritative Iron Plate lineage. The module only exposes explicit
mapping tables described in that edition; it does not guess missing rules,
select a final number, or generate fate statements.
Source: https://vr-d.com/pdf-file/周易/康节说易全书铁板神数(宋)邵雍).pdf
Relevant source sections: 乾集, "天干配卦例", "地支配卦例",
"日主配卦例", "河洛配数例", "地支取数例".
"""

STEM_TO_TRIGRAM = {
    "甲": "乾", "壬": "乾",
    "乙": "坤", "癸": "坤",
    "丙": "艮", "辛": "巽",
    "庚": "震", "己": "离",
    "戊": "坎", "丁": "兑",
}

BRANCH_TO_TRIGRAM = {
    "亥": "坎", "子": "坎",
    "寅": "震",
    "巳": "离", "午": "离",
    "未": "坤",
    "申": "兑", "酉": "兑",
    "戌": "乾",
    "丑": "艮",
    "辰": "巽",
}

TRIGRAM_TO_ELEMENT = {
    "乾": "金", "兑": "金", "离": "火",
    "震": "木", "巽": "木", "坎": "水",
    "艮": "土", "坤": "土",
}

# The edition's "河洛配数例" gives paired stem/branch classes.
HETU_PAIR_NUMBERS = {
    "甲己子午": 9,
    "乙庚丑未": 8,
    "丙辛寅申": 7,
    "丁壬卯酉": 6,
    "戊癸辰戌": 5,
    "己亥": 4,
}

# The edition's separate "地支取数例" gives the branch-number classes.
BRANCH_NUMBER_CLASSES = {
    "亥": (1, 6), "子": (1, 6),
    "寅": (3, 8), "卯": (3, 8),
    "巳": (2, 7), "午": (2, 7),
    "申": (4, 9), "酉": (4, 9),
    "辰": (5,), "戌": (5,), "丑": (5,), "未": (5,),
}


def derive_classic_reference(pillars):
    """Return only transparent lookup results for supplied four pillars."""
    result = {}
    for key in ("year", "month", "day", "hour"):
        pillar = pillars.get(key) or {}
        stem = pillar.get("stem")
        branch = pillar.get("branch")
        result[key] = {
            "stem_trigram": STEM_TO_TRIGRAM.get(stem),
            "branch_trigram": BRANCH_TO_TRIGRAM.get(branch),
            "branch_number_class": list(BRANCH_NUMBER_CLASSES.get(branch, ())),
            "trigram_element": TRIGRAM_TO_ELEMENT.get(BRANCH_TO_TRIGRAM.get(branch)),
        }
    return {
        "edition": "康节说易全书·铁板神数，学林出版社，2003，陈明点校",
        "lineage_status": "secondary_compilation_reference_only",
        "pillars": result,
        "limitations": [
            "这些是该版本明确列出的纳甲/配卦/配数对照，不是完整铁板神数起数算法。",
            "未实现考刻、八刻十五分校时、六亲数演算、卦值日月推数及密码条文定位。",
            "不同传本不得混用；本表不能替代清刻足本及其秘钞密码表。",
            "同一地支可能对应一组数而非唯一数，不能擅自选取其中一个数。",
        ],
    }
