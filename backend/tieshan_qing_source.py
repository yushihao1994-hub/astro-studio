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
    {"pdf_pages": [1, 100], "review_status": "image_reviewed"},
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
        "id": "QING-TRUE-KE-EXAMINATION",
        "topic": "真刻与考刻原则",
        "pdf_page": 1,
        "location": "封面内页说明",
        "visible_text_fragments": ["八字相同而贫富名异，皆因未识真刻", "每刻每一刻又推十五分"],
        "status": "image_observed_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "原页明确把八字相同而命运表现不同与未识真刻联系起来，并提及每刻十五分；尚未说明如何用六亲应事完成真刻选择。",
    },
    {
        "id": "QING-EIGHT-TRIGRAM-ADD",
        "topic": "八卦加则例",
        "pdf_page": 2,
        "printed_pages": [4, 5],
        "location": "右页上半部",
        "visible_text_fragments": ["爻从三十起", "乾卦六为头", "兑为后少女", "变知六百止", "遇十须不用", "玄玄妙法周", "当看多寡数", "及止悉因由"],
        "variant_notes": ["清刻原页可见“世应两同倚”字样，须与2003点校本“世应两同传”逐字校勘。", "“只中一网收”附近存在疑似异文，需按原图放大确认。"],
        "status": "image_observed_variant_transcription_pending",
        "algorithm_status": "conceptual_only",
        "note": "可确认清刻本确有八卦加则例口诀；只登记清刻原页可辨字句，不把现代点校本的逐句解释移植为清刻本算法。",
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
        "id": "QING-NAYIN-NAJIA-TABLES",
        "topic": "納音卦、納甲卦及相關配卦表",
        "pdf_pages": [11, 15],
        "printed_pages": [22, 31],
        "location": "圖表與例表連續頁",
        "status": "image_reviewed_structure_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "已確認後續頁面出現納音卦、納甲卦及大量干支組合表；目前僅登記表類與頁段，不將縮略圖辨字直接寫成映射。",
    },
    {
        "id": "QING-LIFE-EVENT-TABLES",
        "topic": "六親、壽夭、兄弟、婚姻等條目表",
        "pdf_pages": [16, 20],
        "printed_pages": [32, 41],
        "location": "分類條目密集頁",
        "status": "image_reviewed_structure_transcription_pending",
        "algorithm_status": "not_implemented",
        "note": "頁面可見比劫、姻緣、兄弟等分類標題及干支條目；具體條文和索引須放大逐條轉錄，暫不作為財運婚姻可執行資料庫。",
    },
    {
        "id": "QING-LIFE-CLAUSE-EXPANSION",
        "topic": "分類命例及財祿、外財、婚姻相關條目",
        "pdf_pages": [21, 30],
        "printed_pages": [42, 61],
        "location": "分類命例頁",
        "status": "image_reviewed_headings_and_layout",
        "algorithm_status": "not_implemented",
        "note": "已看到分類命例密集排布，部分頁面可辨認外財、妻妾、婚姻類標題；條文正文和編號尚未逐條放大轉錄，不能據此輸出專項斷語。",
    },
    {
        "id": "QING-CLASSIFIED-TABULAR-SEQUENCES",
        "topic": "干支组合分类表与分栏索引页",
        "pdf_pages": [31, 40],
        "printed_pages": [62, 81],
        "location": "连续双页表格区",
        "status": "image_reviewed_layout_only",
        "algorithm_status": "not_implemented",
        "note": "页面以密集干支组合、分栏标题和分类表格为主，版式与前段命例散文不同；本轮只确认其为分类索引/组合表连续区，未逐字转录栏标题与单元格，不据此建立映射。",
    },
    {
        "id": "QING-HEXAGRAM-HEADING-GROUPS",
        "topic": "易卦卦名分組及干支條目表",
        "pdf_pages": [41, 50],
        "printed_pages": [82, 101],
        "location": "卦名標題連續分類表",
        "status": "image_reviewed_headings_only",
        "algorithm_status": "not_implemented",
        "note": "可辨識多處以卦名作分組標題，並列干支組合條目；需逐個卦名、條目和原書位置核對，尚未確認其取數規則或映射方向。",
    },
    {
        "id": "QING-HEXAGRAM-HEADING-GROUPS-CONTINUED",
        "topic": "易卦卦名分組表續段",
        "pdf_pages": [51, 60],
        "printed_pages": [102, 121],
        "location": "卦名標題連續分類表續段",
        "status": "image_reviewed_headings_only",
        "algorithm_status": "not_implemented",
        "note": "延續前段卦名分組及干支條目格式；本段可見多個卦名標題與分組條目，未完成逐字校錄及條目對應驗證。",
    },
    {
        "id": "QING-NUMBERED-CLAUSE-SECTION",
        "topic": "按數字序列編排的斷語條文區",
        "pdf_pages": [66, 100],
        "printed_pages": [132, 201],
        "location": "數字欄頭與直排斷語連續頁",
        "status": "image_reviewed_sample_headings_and_clauses",
        "algorithm_status": "not_implemented",
        "sample_text": ["婚姻早配天喜並頭", "移花接木艱難培植", "大生兩口孝服之憂", "子孫釣於富春江游然自得", "四子送老皆庶所出", "身入宮門可以謀衣食", "五湖水順江水順好行舟", "兄弟十人數有五貴", "兄弟三人數有貴", "妻生一子妾生二兒", "鬼怪出世破財多失"],
        "note": "PDF第66頁起版式由干支/卦名分組表轉為數字欄頭及直排斷語條文。上述僅為可辨識的短句樣本，目前可見條文涉及婚姻、子女、家宅、財祿、仕途/職業、疾病/災厄、兄弟親屬等不同主題；第81—100頁仍沿用數字欄頭與直排條文版式，條目持续覆盖六亲、婚姻、子女、财禄、仕途及寿夭等主题。尚未逐條校字、確認數字欄位意義及建立命盤到條文的檢索映射。",
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

# Conservative transcription candidates copied from the legible scan text.
# These are source strings, not executable mappings; every item remains pending
# independent character-by-character review against the page image.
TRANSCRIPTION_CANDIDATES = [
    {
        "id": "QING-HELUO-CLAUSES",
        "topic": "河洛配数例",
        "pdf_page": 2,
        "raw_text": "甲己子午九；乙庚丑未八；丙辛寅申七；丁壬卯酉六；戊癸辰戌五；己亥单四数。",
        "status": "image_transcribed_candidate_pending_second_review",
        "ambiguities": ["己同时出现在九数句与四数句，暂不裁定其适用条件。"],
    },
    {
        "id": "QING-BRANCH-NUMBER",
        "topic": "地支取数例",
        "pdf_page": 2,
        "raw_text": "亥子一六水；寅卯三八木；巳午二七火；申酉四九金；辰戌丑未五同归。",
        "status": "image_transcribed_candidate_pending_second_review",
        "ambiguities": [],
    },
    {
        "id": "QING-LUOSHU-TRIGRAM",
        "topic": "洛书数卦定局",
        "pdf_page": 2,
        "raw_text": "一数坎兮二数坤；三震四巽；数中分五寄。",
        "status": "image_transcribed_candidate_pending_second_review",
        "ambiguities": ["六至九的完整对应表需结合左页图表逐字复核。"],
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
        "page_count_basis": "Files 文件解析服务对当前可访问 PDF 报告 150 页；原书扫描页脚印刷页码显示至 1363",
        "printed_page_count_shown": PRINTED_PAGE_COUNT_SHOWN,
        "source_class": SOURCE_CLASS,
        "status": STATUS,
        "reviewed_pdf_pages": 100,
        "image_reviewed_ranges": [dict(row) for row in IMAGE_REVIEWED_RANGES],
        "observations": [dict(row) for row in OBSERVATIONS],
        "transcription_candidates": [dict(row) for row in TRANSCRIPTION_CANDIDATES],
        "blockers": list(BLOCKERS),
        "can_generate_final_iron_plate_number": False,
    }
