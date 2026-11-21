"""Version-isolated tables from 康节说易全书·铁板神数, 学林出版社 2003.

This modern punctuated compilation is not the Qing 虚白庐藏本. The code
stores independent tables and does not claim to reconstruct a complete method.
Source PDF: https://vr-d.com/pdf-file/周易/康节说易全书铁板神数(宋)邵雍).pdf
Verified PDF lines/pages in searchable extraction: 717-808 (乾集).
"""

EDITION = "康节说易全书·铁板神数，学林出版社，2003，陈明点校"
SOURCE_STATUS = "searchable_pdf_text_verified_for_listed_sections"

# 乾集「天干配卦例」: PDF lines 717-731.
STEM_TO_TRIGRAM = {
    "甲": "乾", "壬": "乾",
    "乙": "坤", "癸": "坤",
    "丙": "艮",
    "辛": "巽",
    "庚": "震",
    "己": "离",
    "戊": "坎",
    "丁": "兑",
}

# 乾集「地支配卦例」is 洛书取卦定局, not a direct branch-to-trigram table.
# PDF lines 732-737.
LUOSHU_NUMBER_TO_TRIGRAM = {
    1: "坎", 2: "坤", 3: "震", 4: "巽", 5: "中宫",
    6: "乾", 7: "兑", 8: "艮", 9: "离",
}

# 乾集「日主配卦例」: keep this branch mapping separate from 洛书定局.
# PDF lines 738-761. The mnemonic gives branch-to-trigram correspondence.
DAY_MASTER_BRANCH_TO_TRIGRAM = {
    "子": "坎", "亥": "坎",
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

# 乾集「河洛配数例」is a set of grouped clauses, not a simple one-to-one
# character map. The text has an apparent overlap for 己:
# "甲己子午九" and "己亥单四数". Preserve the source clauses without
# silently choosing which value applies to 己 in every context.
HELUO_NUMBER_CLAUSES = [
    {"members": ["甲", "己", "子", "午"], "number": 9, "source_clause": "甲己子午九"},
    {"members": ["乙", "庚", "丑", "未"], "number": 8, "source_clause": "乙庚丑未八"},
    {"members": ["丙", "辛", "寅", "申"], "number": 7, "source_clause": "丙辛寅申七"},
    {"members": ["丁", "壬", "卯", "酉"], "number": 6, "source_clause": "丁壬卯酉六"},
    {"members": ["戊", "癸", "辰", "戌"], "number": 5, "source_clause": "戊癸辰戌五"},
    {"members": ["己", "亥"], "number": 4, "source_clause": "己亥单四数"},
]

# 乾集「地支取数例」: PDF lines 788-808. Each branch is assigned two
# numbers except the central group, which is assigned five.
BRANCH_NUMBER_CLASSES = {
    "亥": (1, 6), "子": (1, 6),
    "寅": (3, 8), "卯": (3, 8),
    "巳": (2, 7), "午": (2, 7),
    "申": (4, 9), "酉": (4, 9),
    "辰": (5,), "戌": (5,), "丑": (5,), "未": (5,),
}


def _clause_matches(character):
    return [
        {"number": row["number"], "source_clause": row["source_clause"]}
        for row in HELUO_NUMBER_CLAUSES
        if character in row["members"]
    ]


def derive_classic_reference(pillars):
    """Return source-labelled lookup data; no final Iron Plate number is inferred."""
    result = {}
    for key in ("year", "month", "day", "hour"):
        pillar = pillars.get(key) or {}
        stem = pillar.get("stem")
        branch = pillar.get("branch")
        day_master_branch_trigram = DAY_MASTER_BRANCH_TO_TRIGRAM.get(branch)
        result[key] = {
            "stem_trigram": STEM_TO_TRIGRAM.get(stem),
            "day_master_branch_trigram": day_master_branch_trigram,
            "stem_heluo_clauses": _clause_matches(stem),
            "branch_heluo_clauses": _clause_matches(branch),
            "branch_number_class": list(BRANCH_NUMBER_CLASSES.get(branch, ())),
            "trigram_element": TRIGRAM_TO_ELEMENT.get(day_master_branch_trigram),
        }
    return {
        "edition": EDITION,
        "lineage_status": "secondary_compilation_reference_only",
        "source_status": SOURCE_STATUS,
        "luoshu_number_to_trigram": LUOSHU_NUMBER_TO_TRIGRAM,
        "pillars": result,
        "limitations": [
            "地支配卦例是洛书数到卦的定局表；日主配卦例是另一张地支到卦的表，不能混为一张表。",
            "河洛配数例原文中己同时出现在九数句与四数句，程序保留两条原文，不擅自裁定。",
            "地支取数只返回数类；尚未实现如何将这些数投入完整起数公式。",
            "八卦加则例涉及年、月、运、日主、六亲及六百律数等环节；当前未实现完整算法。",
            "尚未实现考刻、八刻十五分校时、六亲数完整演算、卦值日月推数及密码条文定位。",
            "本版为现代点校本，不是清刻虚白庐藏本及其秘钞密码表。",
        ],
    }


BRANCHES_IN_ORDER = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


def derive_body_life_palaces(lunar_month, hour_branch, leap_month=False):
    """安身命例：寅宫起正月，顺数至生月；由生月起子时，逆数安命、顺数安身.

    lunar_month must be the user's explicitly verified lunar month (1..12).
    leap_month is recorded, but automatic leap-month handling is intentionally
    not guessed until the edition's exact convention is independently verified.
    """
    if isinstance(lunar_month, bool) or not isinstance(lunar_month, int) or not 1 <= lunar_month <= 12:
        raise ValueError("农历出生月份必须是1至12的整数。")
    if hour_branch not in BRANCHES_IN_ORDER:
        raise ValueError("出生时支必须是子至亥中的一个。")
    month_palace_index = (BRANCHES_IN_ORDER.index("寅") + lunar_month - 1) % 12
    hour_index = BRANCHES_IN_ORDER.index(hour_branch)
    life_index = (month_palace_index - hour_index) % 12
    body_index = (month_palace_index + hour_index) % 12
    return {
        "lunar_month": lunar_month,
        "leap_month": bool(leap_month),
        "month_palace": BRANCHES_IN_ORDER[month_palace_index],
        "hour_branch": hour_branch,
        "life_palace": BRANCHES_IN_ORDER[life_index],
        "body_palace": BRANCHES_IN_ORDER[body_index],
        "rule": "寅宫起正月，顺数至生月；由生月起子时，逆数安命、顺数安身。",
        "source": "康节说易全书·铁板神数，乾集安身命例，PDF文本行810-817",
        "limitations": [
            "本函数要求明确提供农历月份；不能用节气月柱月份替代。",
            "闰月是否按多一月计及其具体落宫处理，尚未完成版本交叉核验；当前仅记录闰月标记，不自动加月。",
            "安身命宫只是基础宫位定位，不等于铁板神数密码数或最终断语。",
        ],
    }
