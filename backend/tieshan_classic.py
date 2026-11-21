"""Version-isolated reference tables transcribed from 康节说易全书·铁板神数.

Edition: 学林出版社，2003，陈明点校（现代点校本）。
This is NOT the Qing 虚白庐藏本 and NOT a complete Iron Plate algorithm.
The tables below are lookup references only. They do not determine a final
number, select a secret code, or generate fate statements.

Publicly readable transcription references:
- https://www.shenjige.cn/details/juY2GFfnpr.html
  (天干配卦、地支配卦节录)
- https://r1689.com/a/2019/845.shtml
  (edition metadata and table-of-contents headings)
- https://www.shukui.net/book/2479457.html
  (contents corroboration; OCR/download listing is not treated as authority)

Important: the source directory separately lists 天干配卦例、地支配卦例、
日主配卦例、河洛配数例、地支取数例. They must remain separate tables.
Where only partial transcription is publicly visible, the app labels it as such.
"""

EDITION = "康节说易全书·铁板神数，学林出版社，2003，陈明点校"

STEM_TO_TRIGRAM = {
    "甲": "乾", "壬": "乾",
    "乙": "坤", "癸": "坤",
    "丙": "艮", "辛": "巽",
    "庚": "震", "己": "离",
    "戊": "坎", "丁": "兑",
}

# Corrected from the publicly visible verse:
# 亥子坎宫寅震木，巳午离门丑在坤；
# 卯酉乾金辰是兑，未申艮宫戌巽真。
BRANCH_TO_TRIGRAM = {
    "亥": "坎", "子": "坎",
    "寅": "震",
    "巳": "离", "午": "离",
    "丑": "坤",
    "卯": "乾", "酉": "乾",
    "辰": "兑",
    "未": "艮", "申": "艮",
    "戌": "巽",
}

TRIGRAM_TO_ELEMENT = {
    "乾": "金", "兑": "金", "离": "火",
    "震": "木", "巽": "木", "坎": "水",
    "艮": "土", "坤": "土",
}

# 河洛配数例: the same number class is assigned to the listed stems/branches.
# Kept as an explicit per-character lookup to avoid ambiguous compound keys.
HELUO_NUMBER_BY_CHARACTER = {
    "甲": 9, "己": 9, "子": 9, "午": 9,
    "乙": 8, "庚": 8, "丑": 8, "未": 8,
    "丙": 7, "辛": 7, "寅": 7, "申": 7,
    "丁": 6, "壬": 6, "卯": 6, "酉": 6,
    "戊": 5, "癸": 5, "辰": 5, "戌": 5,
    "巳": 4, "亥": 4,
}

# 地支取数例. The source transcription gives number pairs for four
# directional groups and 5 for the central group; this is a class, not
# a unique selected value. Keep it separate from 河洛配数例.
BRANCH_NUMBER_CLASSES = {
    "亥": (1, 6), "子": (1, 6),
    "寅": (3, 8), "卯": (3, 8),
    "巳": (2, 7), "午": (2, 7),
    "申": (4, 9), "酉": (4, 9),
    "辰": (5,), "戌": (5,), "丑": (5,), "未": (5,),
}


def derive_classic_reference(pillars):
    """Return transparent, version-labelled lookup results for four pillars."""
    result = {}
    for key in ("year", "month", "day", "hour"):
        pillar = pillars.get(key) or {}
        stem = pillar.get("stem")
        branch = pillar.get("branch")
        branch_trigram = BRANCH_TO_TRIGRAM.get(branch)
        result[key] = {
            "stem_trigram": STEM_TO_TRIGRAM.get(stem),
            "branch_trigram": branch_trigram,
            "stem_heluо_number": HELUO_NUMBER_BY_CHARACTER.get(stem),
            "branch_heluо_number": HELUO_NUMBER_BY_CHARACTER.get(branch),
            "branch_number_class": list(BRANCH_NUMBER_CLASSES.get(branch, ())),
            "trigram_element": TRIGRAM_TO_ELEMENT.get(branch_trigram),
        }
    return {
        "edition": EDITION,
        "lineage_status": "secondary_compilation_reference_only",
        "source_status": "public_excerpt_transcription_not_full_page_verified",
        "pillars": result,
        "limitations": [
            "本表属于2003年现代点校本的版本对照，不是清刻虚白庐藏本。",
            "天干配卦、地支配卦、河洛配数、地支取数是不同表，不得互相替代。",
            "地支取数返回数类，不代表已确定其中某一个数。",
            "尚未实现考刻、八刻十五分校时、六亲数完整演算、卦值日月推数及密码条文定位。",
            "公开节录未覆盖全书所有规则；未核对原页的内容不得标为已验证。",
        ],
    }
