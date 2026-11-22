"""Evidence registry for the user-provided Qing woodblock scan.

This module records only what has been visually inspected in the scan.
It deliberately does not convert OCR guesses or partial readings into
executable Iron Plate calculations.
"""

EDITION = "《神機妙算鐵板數》；题署邵康節先生著；封面内页见“貞元書屋藏板”"
FILE_NAME = "鐵板神數(清刻足本).pdf"
FILE_SIZE_BYTES = 83686820
SCAN_PAGE_COUNT = 150
PRINTED_PAGE_COUNT_SHOWN = 1363
STATUS = "scan_acquired_initial_pages_image_reviewed_core_rules_pending"
SOURCE_CLASS = "user_provided_primary_scan"

# Page numbers below are 1-based PDF image pages, not printed book page numbers.
# Each scan image may contain a two-page spread.
IMAGE_REVIEWED_RANGES = [
    {"pdf_pages": [1, 5], "review_status": "image_reviewed"},
    {"pdf_pages": [6, 15], "review_status": "image_reviewed"},
]

OBSERVATIONS = [
    {
        "id": "QING-FRONT-EIGHT-KE",
        "topic": "八刻十五分",
        "pdf_page": 1,
        "location": "封面内页说明",
        "visible_text_fragment": "八刻每一刻又推十五分",
        "status": "image_observed_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "只确认书中出现八刻与每刻十五分的说明；传统考刻如何结合六亲校验、定数与刻分推进，尚未据完整例题复原。",
    },
    {
        "id": "QING-STEM-TRIGRAM",
        "topic": "天干配卦例",
        "pdf_page": 2,
        "printed_pages": [4, 5],
        "location": "左/右页卦例区域",
        "status": "image_located_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "已定位到标题与对应表格；须逐字转录、双人复核后再与2003点校本对照。",
    },
    {
        "id": "QING-DAYMASTER-TRIGRAM",
        "topic": "日主配卦例",
        "pdf_page": 2,
        "printed_pages": [4, 5],
        "location": "左页下半部",
        "status": "image_located_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "已定位到标题与对应表格；暂不直接复用现代点校本映射。",
    },
    {
        "id": "QING-BODY-LIFE",
        "topic": "安身命例",
        "pdf_page": 3,
        "printed_pages": [6, 7],
        "location": "左页",
        "status": "image_located_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "已定位原版图像；具体顺逆、起宫及闰月规则须按原页重新转录，不沿用现代本函数。",
    },
    {
        "id": "QING-NINE-PALACE-CHARTS",
        "topic": "九宫/局数图表",
        "pdf_pages": [6, 7, 8, 9],
        "printed_pages": [12, 13, 14, 15, 16, 17, 18, 19],
        "status": "image_reviewed_structure_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "已看到金四局、水二局、木三局、土五局、火六局等图表版式；表内数值须逐格抄录并校验，不能仅凭缩略图推算法。",
    },
]

BLOCKERS = [
    "清刻本起数/卦值日月推数的完整步骤尚未逐页转录并复算。",
    "传统考刻的六亲验证、刻分推进与最终定盘条件尚未形成可重复算法。",
    "六亲数与六十律数之间的完整映射及例题尚未完成核验。",
    "附录秘钞密码表及密码数到条文的映射尚未逐页定位和转录。",
    "财运、婚姻等主题条文尚未建立经复核的索引。",
]


def get_qing_source_reference():
    """Return transparent provenance and review state; never calculate a fate number."""
    return {
        "edition": EDITION,
        "file_name": FILE_NAME,
        "file_size_bytes": FILE_SIZE_BYTES,
        "scan_page_count": SCAN_PAGE_COUNT,
        "printed_page_count_shown": PRINTED_PAGE_COUNT_SHOWN,
        "source_class": SOURCE_CLASS,
        "status": STATUS,
        "image_reviewed_ranges": [dict(row) for row in IMAGE_REVIEWED_RANGES],
        "observations": [dict(row) for row in OBSERVATIONS],
        "blockers": list(BLOCKERS),
        "can_generate_final_iron_plate_number": False,
    }
