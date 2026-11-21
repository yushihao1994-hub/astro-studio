"""Structured sample transcription for the 子集, 2003 punctuated edition.

Only a short, source-located sample is included. This is not a complete clause
corpus, not a cipher table, and not suitable for automatic fortune matching.
"""

EDITION = "康节说易全书·铁板神数，学林出版社，2003年12月，陈明点校"
COLLECTION = "子集"
SOURCE_PDF = "https://vr-d.com/pdf-file/周易/康节说易全书铁板神数(宋)邵雍).pdf"
STATUS = "sample_transcription_ocr_not_image_verified"
CATALOG_SCHEMA_VERSION = "0.2.0"

# The source displays the group marker 一〇八〇 followed by entries 一至十.
# Keep the marker as a printed group label, not a Gregorian year or a clause ID.
ENTRIES = [
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":1,"raw_number_text":"卅四","content":"婚姻早临，天喜当头。","pdf_text_lines":"10670-10670","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":2,"raw_number_text":"卅三","content":"先培根本，枝叶畅茂乃成。","pdf_text_lines":"10671-10671","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":3,"raw_number_text":None,"content":"其人品自宏，深衿怀安乐。","pdf_text_lines":"10672-10672","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":4,"raw_number_text":None,"content":"风监通神人共仰，伏遇提携与起家。","pdf_text_lines":"10673-10673","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":5,"raw_number_text":None,"content":"清问薄利与微名，做个都城卖卜人。","pdf_text_lines":"10674-10674","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":6,"raw_number_text":"四十四","content":"万恨千愁，一朝尽释。","pdf_text_lines":"10675-10675","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":7,"raw_number_text":"卅三","content":"一日吉利，再日亨通。","pdf_text_lines":"10676-10676","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":8,"raw_number_text":"卅五","content":"告君记四字，待兔守株。","pdf_text_lines":"10677-10677","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":9,"raw_number_text":"四十六","content":"草色逢春，始发萌芽。","pdf_text_lines":"10678-10678","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
    {"collection":"子","group_marker":"一〇八〇","entry_sequence":10,"raw_number_text":"四十九","content":"流年顺利，何事不可为。","pdf_text_lines":"10679-10679","printed_page":None,"ocr_status":"text_layer_only","age_markers":[],"age_marker_text":None},
]

FIELD_GUIDE = {
    "group_marker":"原书分组标记；不可当作公历年份或坤集密码条号",
    "entry_sequence":"组内序号，一至十",
    "raw_number_text":"原书对应数的原始写法；保留卅等异体数字",
    "content":"原文转录文本；尚未逐页图像校对",
    "pdf_text_lines":"PDF文本层行号，供复核定位",
    "printed_page":"印刷页码；本批样本暂不推断",
    "ocr_status":"文本层转录，尚未与扫描图像逐字核对",
}


# Layout observations are separated from transcribed clause content.
CLAUSE_LAYOUT_PATTERNS = [
    {"pattern_id":"repeated_collection_headers","description":"子集正文中重复出现分集页眉，不能把每次页眉都当成新分集。","pdf_text_lines":["10668","10766","11028","11202","11279"],"status":"text_layer_observed_image_check_pending"},
    {"pattern_id":"group_marker_then_local_sequence","description":"分组标记后出现组内序号；组标记与组内序号是两个字段。","pdf_text_lines":["10668-10679"],"status":"text_layer_observed_image_check_pending"},
    {"pattern_id":"optional_corresponding_number","description":"部分组内条目显示对应数，部分条目没有显示；缺失值必须保留为空。","pdf_text_lines":["10670-10679"],"status":"text_layer_observed_image_check_pending"},
    {"pattern_id":"age_markers_are_independent","description":"正文条目可带一个或多个岁数/年龄标记；它们不等同组内序号或对应数。","pdf_text_lines":["10766","11028","11202","11279"],"status":"structure_requires_page_image_verification"},
]

LIMITATIONS = [
    "本接口仅展示子集一〇八〇组的十条样本，不代表完整子集。",
    "一〇八〇是原书分组标记，不是公历年份，也不是条文密码号。",
    "对应数缺失时保留null，不根据上下文补数。",
    "对应数以原始中文数字保存，不自动转成条文编号。",
    "PDF文本层可能存在OCR错误，必须对照页面图像复核后才能标记verified。",
    "样本内容不得用于自动考刻、定数或生成个人命运结论。",
]


# Source-checked group index. Clause prose is not duplicated here; each row
# points to the PDF text layer for review. The numeric column is kept distinct
# from numbers that happen to occur inside the clause prose.
GROUP_INDEX = [
    {"group_marker":"一〇八〇","pdf_text_lines":"10664-10679","entries":[
        {"entry_sequence":1,"raw_number_text":"卅四","number_field_present":True,"content_present":True,"pdf_text_lines":"10670"},
        {"entry_sequence":2,"raw_number_text":"卅三","number_field_present":True,"content_present":True,"pdf_text_lines":"10671"},
        {"entry_sequence":3,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10672"},
        {"entry_sequence":4,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10673"},
        {"entry_sequence":5,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10674"},
        {"entry_sequence":6,"raw_number_text":"四十四","number_field_present":True,"content_present":True,"pdf_text_lines":"10675"},
        {"entry_sequence":7,"raw_number_text":"卅三","number_field_present":True,"content_present":True,"pdf_text_lines":"10676"},
        {"entry_sequence":8,"raw_number_text":"卅五","number_field_present":True,"content_present":True,"pdf_text_lines":"10677"},
        {"entry_sequence":9,"raw_number_text":"四十六","number_field_present":True,"content_present":True,"pdf_text_lines":"10678"},
        {"entry_sequence":10,"raw_number_text":"四十九","number_field_present":True,"content_present":True,"pdf_text_lines":"10679"},
    ]},
    {"group_marker":"一〇九〇","pdf_text_lines":"10681-10691","entries":[
        {"entry_sequence":1,"raw_number_text":"四十三","number_field_present":True,"content_present":True,"pdf_text_lines":"10682"},
        {"entry_sequence":2,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10683"},
        {"entry_sequence":3,"raw_number_text":"七十五","number_field_present":True,"content_present":True,"pdf_text_lines":"10684"},
        {"entry_sequence":4,"raw_number_text":"六十四","number_field_present":True,"content_present":True,"pdf_text_lines":"10685"},
        {"entry_sequence":5,"raw_number_text":"五十九","number_field_present":True,"content_present":True,"pdf_text_lines":"10686"},
        {"entry_sequence":6,"raw_number_text":"六十一","number_field_present":True,"content_present":True,"pdf_text_lines":"10687"},
        {"entry_sequence":7,"raw_number_text":"七十三","number_field_present":True,"content_present":True,"pdf_text_lines":"10688"},
        {"entry_sequence":8,"raw_number_text":"七十七","number_field_present":True,"content_present":True,"pdf_text_lines":"10689"},
        {"entry_sequence":9,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10690"},
        {"entry_sequence":10,"raw_number_text":"五十九","number_field_present":True,"content_present":True,"pdf_text_lines":"10691"},
    ]},
    {"group_marker":"一一〇〇","pdf_text_lines":"10693-10704","entries":[
        {"entry_sequence":1,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10695"},
        {"entry_sequence":2,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10696"},
        {"entry_sequence":3,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10697"},
        {"entry_sequence":4,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10698"},
        {"entry_sequence":5,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10699"},
        {"entry_sequence":6,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10700"},
        {"entry_sequence":7,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10701"},
        {"entry_sequence":8,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10702"},
        {"entry_sequence":9,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10703","note":"条文句子内部含数字写法；不等同独立对应数栏"},
        {"entry_sequence":10,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"10704"},
    ]},
]

def get_group_index():
    return {
        "edition": EDITION,
        "collection": "子集",
        "status": "text_layer_indexed_image_verification_pending",
        "group_count": len(GROUP_INDEX),
        "entry_count": sum(len(group["entries"]) for group in GROUP_INDEX),
        "groups": [
            {"group_marker": group["group_marker"],
             "pdf_text_lines": group["pdf_text_lines"],
             "entry_count": len(group["entries"]),
             "entries": [dict(entry) for entry in group["entries"]]}
            for group in GROUP_INDEX
        ],
        "limitations": [
            "仅为PDF文本层字段索引，未逐字对照扫描图像。",
            "不复制完整条文正文；请按PDF行号核对。",
            "raw_number_text只记录独立数字栏，条文句内数字不转入该字段。",
            "空值表示原文该条没有独立数字栏，不允许按相邻条目补齐。",
            "本索引不构成铁板密码条号，不用于自动考刻或断命。"
        ]
    }


def get_collection_sample(branch="子"):
    if branch != "子":
        return {
            "edition": EDITION,
            "collection": branch,
            "status": "not_transcribed",
            "entry_count": 0,
            "entries": [],
            "field_guide": dict(FIELD_GUIDE),
            "limitations": ["该分集尚未完成逐条转录。"],
        }
    return {
        "edition": EDITION,
        "collection": COLLECTION,
        "source_pdf": SOURCE_PDF,
        "status": STATUS,
        "group_marker": "一〇八〇",
        "schema_version": CATALOG_SCHEMA_VERSION,
        "layout_patterns": [dict(row) for row in CLAUSE_LAYOUT_PATTERNS],
        "entry_count": len(ENTRIES),
        "schema_version": CATALOG_SCHEMA_VERSION,
        "layout_patterns": [dict(row) for row in CLAUSE_LAYOUT_PATTERNS],
        "entries": [dict(row) for row in ENTRIES],
        "field_guide": dict(FIELD_GUIDE),
        "limitations": list(LIMITATIONS),
    }
