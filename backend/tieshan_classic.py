"""Version-isolated tables from 康节说易全书·铁板神数, 学林出版社 2003.

This modern punctuated compilation is not the Qing 虚白庐藏本. The code
stores independent tables and does not claim to reconstruct a complete method.
Source PDF: https://vr-d.com/pdf-file/周易/康节说易全书铁板神数(宋)邵雍).pdf
Verified PDF lines/pages in searchable extraction: 717-808 (乾集).
"""

EDITION = "康节说易全书·铁板神数，学林出版社，2003，陈明点校"
SOURCE_STATUS = "searchable_pdf_text_verified_for_listed_sections"

EIGHT_TRIGRAM_ADDITION_EXPLANATION = {
    "edition": EDITION,
    "source": "乾集《八卦加则例》解说，PDF文本行684-715",
    "status": "source_explained_not_executable",
    "verse": [
        "交从三十起，乾卦六为头。兑为后少女，只中一网收。",
        "变知六百止，应世两同传。遇十须不用，玄玄妙法周。",
        "当看多寡数，及止悉因由。",
    ],
    "clauses": [
        {"key":"yao_from_thirty","title":"爻从三十起","source_lines":"699-700","source_meaning":"原书解为爻代表运与日主；元会运世数序中三十运为一会，年月日时数序中三十日为一月；每时又含三十分钟、三十卦值一时，以六亲之数演算三十卦。","algorithm_status":"conceptual_only"},
        {"key":"qian_six_lines","title":"乾卦六爻为头","source_lines":"701","source_meaning":"乾为元、为年；年卦以世卦六爻变得。","algorithm_status":"conceptual_only"},
        {"key":"dui_month","title":"兑为后少女","source_lines":"702","source_meaning":"兑为会、为月；月在日之后；以乾上交变阴成兑说明少女之象。","algorithm_status":"conceptual_only"},
        {"key":"one_net","title":"只中一网收","source_lines":"704-708","source_meaning":"原书将此句接续解释为年、月之义，称一年总数从会、月中出。","algorithm_status":"conceptual_only"},
        {"key":"six_hundred","title":"变知六百止","source_lines":"710","source_meaning":"原书以六十律数与六亲、十天干相乘，说明十乘六十为六百。","algorithm_status":"conceptual_only"},
        {"key":"shi_ying","title":"应世两同倚","source_lines":"711","source_meaning":"原书解释会为世、月为应，并以十二月、六十律数和十说明六百与十二会数的关系。","algorithm_status":"conceptual_only"},
        {"key":"discard_ten","title":"遇十须不用","source_lines":"712","source_meaning":"原书以先天八卦六十四卦、三百八十四爻说明十除不足，因此不用十。具体运算中如何执行，仍需完整例题验证。","algorithm_status":"conceptual_only"},
        {"key":"hexagram_change","title":"玄玄妙法周","source_lines":"713","source_meaning":"原书称先天八卦图中各卦都可变为六十四卦，变化无止境。","algorithm_status":"conceptual_only"},
        {"key":"count_range","title":"当看多寡数、及止悉因由","source_lines":"714-715","source_meaning":"原书要求查明数值的位数规模，并明确计算终止位置及其依据。","algorithm_status":"conceptual_only"},
    ],
    "not_yet_implemented": [
        "世卦、应卦及年卦/月卦的具体取卦输入和变爻次序。",
        "六亲如何映射十天干、六十律数，以及三十卦逐项运算的完整公式。",
        "“遇十须不用”在每个中间步骤的精确舍取位置与例题校验。",
        "从上述中间数如何形成可与坤集密码条文匹配的最终数序。",
    ],
    "warning": "本说明是对2003年点校本解说文字的结构化登记，不等于完整算法。没有逐项复算例题前，不执行数值运算。",
}

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
        "eight_trigram_addition": EIGHT_TRIGRAM_ADDITION_EXPLANATION,
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

    lunar_month is the numbered lunar month (1..12). The cited edition explicitly
    says a leap month is counted as one additional month, so it advances the
    palace by one additional step.
    """
    if isinstance(lunar_month, bool) or not isinstance(lunar_month, int) or not 1 <= lunar_month <= 12:
        raise ValueError("农历出生月份必须是1至12的整数。")
    if hour_branch not in BRANCHES_IN_ORDER:
        raise ValueError("出生时支必须是子至亥中的一个。")
    effective_lunar_month = lunar_month + (1 if leap_month else 0)
    month_palace_index = (BRANCHES_IN_ORDER.index("寅") + effective_lunar_month - 1) % 12
    hour_index = BRANCHES_IN_ORDER.index(hour_branch)
    life_index = (month_palace_index - hour_index) % 12
    body_index = (month_palace_index + hour_index) % 12
    return {
        "lunar_month": lunar_month,
        "leap_month": bool(leap_month),
        "effective_lunar_month_count": effective_lunar_month,
        "month_palace": BRANCHES_IN_ORDER[month_palace_index],
        "hour_branch": hour_branch,
        "life_palace": BRANCHES_IN_ORDER[life_index],
        "body_palace": BRANCHES_IN_ORDER[body_index],
        "rule": "寅宫起正月，顺数至生月；由生月起子时，逆数安命、顺数安身。",
        "source": "康节说易全书·铁板神数，乾集安身命例，PDF文本行810-817",
        "limitations": [
            "本函数要求明确提供农历月份；不能用节气月柱月份替代。",
            "本函数按2003年点校本“若有闰月，作多一月算”执行；其他版本是否同例，仍需异本交叉核验。",
            "安身命宫只是基础宫位定位，不等于铁板神数密码数或最终断语。",
        ],
    }
