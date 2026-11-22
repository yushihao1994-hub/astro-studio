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

# Further groups located in the PDF text layer. Multi-age strings are recorded
# only as unassigned candidates until the original page layout is checked.
# Corresponding-number fields remain unknown (None), not assumed absent.
def _pending_layout_group(marker, line_range, age_hints):
    entries = []
    for sequence in range(1, 11):
        hint = age_hints.get(sequence)
        entries.append({
            "entry_sequence": sequence,
            "raw_number_text": None,
            "number_field_present": None,
            "content_present": None,
            "pdf_text_lines": None,
            "age_markers": [],
            "age_marker_text": hint,
            "age_marker_association_status": (
                "needs_layout_verification" if hint else "not_assessed"
            ),
        })
    return {
        "group_marker": marker,
        "pdf_text_lines": line_range,
        "entry_count": 10,
        "layout_status": "text_layer_located_layout_unverified",
        "age_marker_candidates": [
            {"entry_sequence_hint": sequence, "raw_text": value,
             "status": "unassigned_pending_page_image"}
            for sequence, value in age_hints.items()
        ],
        "entries": entries,
    }


GROUP_INDEX.extend([
    _pending_layout_group("一一一〇", "10707-10719", {
        4: "五十三／五十四", 5: "五十七／五十八", 7: "三十三／三十四"
    }),
    _pending_layout_group("一一二〇", "10721-10741", {
        3: "四十九／五十七／五十五／五十八",
        5: "三十三／三十四／三十七／三十八",
        8: "四十五／四十六／四十九／五十"
    }),
    _pending_layout_group("一一三〇", "10743-10762", {
        1: "十五／十六／四十三／四十四",
        5: "十三／十四／三十七／三十八",
        6: "六十三／六十四",
        8: "六十九／七十",
        10: "三十三／三十四"
    }),
    {
        "group_marker": "一一四〇",
        "pdf_text_lines": "10764-10809",
        "entry_count": 10,
        "layout_status": "sequential_number_age_lines_then_clause",
        "layout_note": "本组版式为组内序号、其后一个或多个岁数行、再接正文；岁数不属于独立对应数栏。",
        "entries": [
            {"entry_sequence": 1, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10768-10771", "age_markers": ["四十九", "五十"], "age_marker_text": "四十九／五十", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 2, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10773-10776", "age_markers": ["五十", "五十一"], "age_marker_text": "五十／五十一", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 3, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10779-10780", "age_markers": ["五十二"], "age_marker_text": "五十二", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 4, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10783-10784", "age_markers": ["五十三"], "age_marker_text": "五十三", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 5, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10787-10788", "age_markers": ["五十四"], "age_marker_text": "五十四", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 6, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10791-10792", "age_markers": ["五十五"], "age_marker_text": "五十五", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 7, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10795-10796", "age_markers": ["五十六"], "age_marker_text": "五十六", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 8, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10799-10800", "age_markers": ["十七"], "age_marker_text": "十七", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 9, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10803-10804", "age_markers": ["十八"], "age_marker_text": "十八", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 10, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10806-10809", "age_markers": ["五十七", "五十八", "五十九"], "age_marker_text": "五十七／五十八／五十九", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
        ],
    },
    {
        "group_marker": "一一五〇",
        "pdf_text_lines": "10811-10858",
        "entry_count": 10,
        "layout_status": "sequential_number_age_lines_then_clause",
        "layout_note": "与一一四〇组相同，组内序号后列岁数（可缺省或多值），再接正文；岁数不是独立对应数栏。",
        "entries": [
            {"entry_sequence": 1, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10813-10814", "age_markers": [], "age_marker_text": None, "age_marker_association_status": "age_not_listed_in_text_layer"},
            {"entry_sequence": 2, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10816-10819", "age_markers": ["三十五", "三十六"], "age_marker_text": "三十五／三十六", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 3, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10821-10825", "age_markers": ["五十七", "五十八", "五十九"], "age_marker_text": "五十七／五十八／五十九", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 4, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10827-10830", "age_markers": ["四十一", "四十二"], "age_marker_text": "四十一／四十二", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 5, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10832-10833", "age_markers": [], "age_marker_text": None, "age_marker_association_status": "age_not_listed_in_text_layer"},
            {"entry_sequence": 6, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10835-10836", "age_markers": [], "age_marker_text": None, "age_marker_association_status": "age_not_listed_in_text_layer"},
            {"entry_sequence": 7, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10838-10841", "age_markers": ["三十五", "三十六"], "age_marker_text": "三十五／三十六", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 8, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10843-10846", "age_markers": ["三十二", "三十三"], "age_marker_text": "三十二／三十三", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 9, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10848-10851", "age_markers": ["三十三", "三十四"], "age_marker_text": "三十三／三十四", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 10, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10853-10858", "age_markers": ["三十三", "三十四", "三十五", "三十六"], "age_marker_text": "三十三／三十四／三十五／三十六", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
        ],
    },

    {
        "group_marker": "一一六〇",
        "pdf_text_lines": "10860-10902",
        "entry_count": 10,
        "layout_status": "sequential_number_age_lines_then_clause",
        "layout_note": "沿用序号、岁数行、正文分行结构；部分条目文本层未列岁数。",
        "entries": [
            {"entry_sequence": 1, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10862-10863", "age_markers": [], "age_marker_text": None, "age_marker_association_status": "age_not_listed_in_text_layer"},
            {"entry_sequence": 2, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10865-10868", "age_markers": ["三十七", "三十八"], "age_marker_text": "三十七／三十八", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 3, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10871-10872", "age_markers": ["三十九"], "age_marker_text": "三十九", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 4, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10874-10877", "age_markers": ["五十五", "五十六"], "age_marker_text": "五十五／五十六", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 5, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10879-10880", "age_markers": [], "age_marker_text": None, "age_marker_association_status": "age_not_listed_in_text_layer"},
            {"entry_sequence": 6, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10882-10883", "age_markers": [], "age_marker_text": None, "age_marker_association_status": "age_not_listed_in_text_layer"},
            {"entry_sequence": 7, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10885-10888", "age_markers": ["三十五", "三十六"], "age_marker_text": "三十五／三十六", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 8, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10890-10892", "age_markers": ["四十二", "四十三"], "age_marker_text": "四十二／四十三", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 9, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10894-10898", "age_markers": ["四十四", "四十五", "四十六"], "age_marker_text": "四十四／四十五／四十六", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
            {"entry_sequence": 10, "raw_number_text": None, "number_field_present": False, "content_present": True, "pdf_text_lines": "10900-10902", "age_markers": ["五十八"], "age_marker_text": "五十八", "age_marker_association_status": "text_layer_sequence_associated_image_check_pending"},
        ],
    },
])


# Later 子集 groups: preserve raw OCR labels and keep normalization candidates
# separate from the printed transcription until page-image verification.
def _source_group(raw_marker, normalized_marker, line_range, age_hints,
                  normalization_status="verified_text_layer_group_marker"):
    entries = []
    for sequence in range(1, 11):
        hint = age_hints.get(sequence)
        entries.append({
            "entry_sequence": sequence,
            "raw_number_text": None,
            "number_field_present": False if hint is not None else None,
            "content_present": True if hint is not None else None,
            "pdf_text_lines": None,
            "age_markers": hint or [],
            "age_marker_text": "／".join(hint) if hint else None,
            "age_marker_association_status": (
                "text_layer_sequence_associated_image_check_pending"
                if hint else "not_assessed"
            ),
        })
    return {
        "group_marker": normalized_marker or raw_marker,
        "raw_group_marker": raw_marker,
        "normalized_group_marker_candidate": normalized_marker,
        "normalization_status": normalization_status,
        "pdf_text_lines": line_range,
        "entry_count": 10,
        "layout_status": "sequential_number_age_lines_then_clause",
        "entries": entries,
    }


GROUP_INDEX.extend([
    _source_group("一一七〇", "一一七〇", "10904-10917", {
        1:["五十二"], 2:["五十七"], 3:["五十八"], 4:["三十九"],
        5:["二十六"], 6:["三十一"], 7:["五十三"], 8:["五十二"],
        10:["五十三"]
    }),
    _source_group("一九〇", "一一八〇", "10919-10929", {
        1:["三十八"], 2:["五十九"], 3:["六十"], 4:["五十七"],
        5:["三十三"], 6:["四十二"], 7:["四十三"], 8:["六十三"],
        9:["十七"], 10:["五十六"]
    }, "probable_ocr_correction_pending_image_check"),
    _source_group("一九一", "一一九〇", "10931-10942", {
        1:["三十九"], 2:["十二"], 3:["六十九"], 4:["七十"],
        5:["九十"], 6:["三十一"], 7:["二十二"], 8:["二十五"],
        9:["十四"]
    }, "probable_ocr_correction_pending_image_check"),
    _source_group("一二〇〇", "一二〇〇", "10944-10956", {
        1:["七十九","八十"], 2:["三十一"], 3:["四十八"],
        5:["二十五"], 6:["七十七","七十八"], 10:["二十三","三十四"]
    }),
    _source_group("一二二〇", "一二二〇", "10958-10968", {
        1:["二十九","三十"], 4:["六十七","六十八","六十九"],
        5:["二十八","三十八","四十八","五十八"],
        7:["五十"], 10:["二十"]
    }),
    _source_group("一二三〇", "一二三〇", "10970-10980", {
        2:["二十一"], 3:["二十九","五十","六十"],
        5:["二十七","三十","三十","九十"],
        6:["二十二","三十"], 7:["二十九"],
        10:["五十五","五十六"]
    }),
])

# Table-form 子集 blocks use the printed column heading "序号". Keep that
# source column verbatim and do not reinterpret it as age or cipher number.
def _table_layout_group(marker, line_range, raw_index_values, row_lines, layout_note="PDF文本层采用表格列标题“年份／序号／诗句”；序号栏原文独立保存，不擅自解释为岁数、对应数或密码条号。"):
    entries = []
    for sequence, (raw_value, line_ref) in enumerate(zip(raw_index_values, row_lines), 1):
        entries.append({
            "entry_sequence": sequence,
            "source_index_text": raw_value,
            "raw_number_text": None,
            "number_field_present": None,
            "content_present": True,
            "pdf_text_lines": line_ref,
            "age_markers": [],
            "age_marker_text": None,
            "age_marker_association_status": "source_column_semantics_unverified",
        })
    return {
        "group_marker": marker,
        "raw_group_marker": marker,
        "normalized_group_marker_candidate": marker,
        "normalization_status": "verified_text_layer_group_marker",
        "pdf_text_lines": line_range,
        "entry_count": len(entries),
        "layout_status": "table_rows_year_sequence_clause",
        "layout_note": layout_note,
        "entries": entries,
    }


GROUP_INDEX.extend([
    _table_layout_group("一二四〇", "10986-10998",
        ["四十七／四十八", "三十五／三十六", None, None, None, "五十一", None,
         "三十五／三十七／四十五／四十七／四十八", None],
        ["10989", "10990", "10991", "10992", "10993", "10994", "10995", "10996", "10997"]),
    _table_layout_group("一二五〇", "10999-11012",
        ["三十三／三十四", None, "三十三／三十四", None, "八十五／八十六", None,
         "三十四／十三／五十三／十三", None, "二十一", None],
        ["11002", "11003", "11004", "11005", "11006", "11007", "11008", "11009", "11010", "11011"]),
    _table_layout_group("一二六〇", "11013-11026",
        ["三十七", None, None, None, "四十七／四十八／五十二／五十五", None,
         "六十九／六十／三十三／三十三／五十三／五十四", None, None, None],
        ["11016", "11017", "11018", "11019", "11020", "11021", "11022", "11023", "11024", "11025"]),
])


# Preserve two OCR-specific anomalies without silently normalizing their raw forms.
GROUP_INDEX[9]["source_header_ocr"] = {
    "raw_text": "康节报具全书",
    "normalized_candidate": "康节说易全书",
    "status": "probable_ocr_error_pending_image_check",
    "pdf_text_lines": "10906",
}
GROUP_INDEX[14]["age_marker_ambiguities"] = [{
    "entry_sequence": 5,
    "raw_token": "三十作",
    "status": "unresolved_ocr_token_pending_image_check",
}]
GROUP_INDEX[14]["entries"][4]["age_marker_text"] = "二十七／三十／三十作／九十"
GROUP_INDEX[14]["entries"][4]["age_markers"] = ["二十七", "三十", "九十"]
GROUP_INDEX[14]["entries"][4]["age_marker_association_status"] = "contains_ocr_ambiguous_age_token_pending_image_check"


# Explicitly indexed groups whose marker and sequential layout are clear.
GROUP_INDEX.extend([
    _source_group("一二七〇", "一二七〇", "11069-11109", {
        1:["三十六", "三十七", "三十九"],
        2:["三十"],
        4:["五十七", "三十八"],
        7:["三十二"],
        8:["六十五"],
        10:["五十三", "五十四"],
    }),
    _source_group("一二八〇", "一二八〇", "11111-11151", {
        2:["四十"],
        4:["五十六"],
        6:["五十五", "五十六", "三十二", "三十三", "三十三", "三十三", "三十四"],
        9:["四十五", "四十六"],
    }),
])

# These two groups use sequence-age-clause layout; age is not a number column.


for _group, _spans in [
    (GROUP_INDEX[18], ["11071-11075","11077-11079","11081-11082","11084-11087",
                       "11089-11090","11092-11093","11095-11097","11099-11101",
                       "11103-11105","11107-11109"]),
    (GROUP_INDEX[19], ["11113-11114","11117-11118","11121-11121","11124-11125",
                       "11127-11129","11130-11137","11139-11140","11142-11143",
                       "11145-11148","11150-11151"]),
]:
    for _entry, _span in zip(_group["entries"], _spans):
        _entry["pdf_text_lines"] = _span
        _entry["number_field_present"] = False
        _entry["content_present"] = True
        _entry["age_marker_association_status"] = (
            "text_layer_sequence_associated_image_check_pending"
            if _entry["age_markers"] else "age_not_listed_in_text_layer"
        )
GROUP_INDEX.extend([
    _table_layout_group("一三二〇", "11186-11198",
        [None, None, None, None, None, None, None, None, "四十四／四十五", "三十七／三十八"],
        ["11189","11190","11191","11192","11193","11194","11195","11196","11197","11198"],
        "PDF表头为“序号／干支/岁数／内容”；第二列原文值保留为来源字段，不解释成密码数。"),
    _source_group("一三三〇", "一三三〇", "11214-11225", {
        2:["三十五"], 3:["三十二"], 8:["三十七"], 10:["四十七"],
    }),
])

for _entry, _span in zip(GROUP_INDEX[20]["entries"],
    ["11189","11190","11191","11192","11193","11194","11195","11196","11197","11198"]):
    _entry["pdf_text_lines"] = _span
    _entry["number_field_present"] = None
    _entry["content_present"] = True
    _entry["age_marker_association_status"] = "source_column_semantics_unverified"
for _entry, _span in zip(GROUP_INDEX[21]["entries"],
    ["11216-11216","11217-11217","11218-11218","11219-11219","11220-11220",
     "11221-11221","11222-11222","11223-11223","11224-11224","11225-11225"]):
    _entry["pdf_text_lines"] = _span
    _entry["number_field_present"] = False
    _entry["content_present"] = True
    _entry["age_marker_association_status"] = (
        "text_layer_sequence_associated_image_check_pending" if _entry["age_markers"]
        else "age_not_listed_in_text_layer")
UNASSIGNED_BLOCKS = [{
    "block_id": "child_collection_unheaded_block_before_1270",
    "pdf_text_lines": "11028-11067",
    "entry_count": 10,
    "status": "group_marker_missing_do_not_assign",
    "note": "该块位于一二六〇表格之后、一二七〇组标题之前；当前文本层未显示独立组号。",
    "entries": [{"entry_sequence": n, "pdf_text_lines": line}
                for n, line in enumerate(
                    ["11030-11033", "11035-11037", "11039-11041", "11043-11046",
                     "11048-11049", "11051-11052", "11054-11056", "11058-11061",
                     "11063-11064", "11066-11067"], 1)]
}]

GROUP_INDEX.extend([
    _source_group("一三四〇", "一三四〇", "11227-11238", {
        1:["十", "三十七"], 2:["六十三"], 3:["六十四"], 4:["六十二"],
        5:["九", "十七"], 6:["八十七"], 7:["五十五"], 9:["三十九"],
    }),
    _source_group("一三五〇", "一三五〇", "11240-11252", {}),
])
for _group, _spans in [
    (GROUP_INDEX[22], ["11229","11230","11231","11232","11233","11234","11235","11236","11237","11238"]),
    (GROUP_INDEX[23], ["11242-11242","11243","11244","11245","11246","11247","11248","11249","11250","11251-11252"]),
]:
    for _entry, _span in zip(_group["entries"], _spans):
        _entry["pdf_text_lines"] = _span
        _entry["number_field_present"] = False
        _entry["content_present"] = True
        _entry["age_marker_association_status"] = (
            "text_layer_sequence_associated_image_check_pending" if _entry["age_markers"]
            else "age_not_listed_in_text_layer")
GROUP_INDEX.extend([
    _source_group("二三六〇", "一三六〇", "11254-11265", {},
                  "probable_ocr_correction_pending_image_check"),
    _source_group("二三八〇", "一三八〇", "11267-11277", {},
                  "probable_ocr_correction_pending_image_check"),
    _source_group("一四〇〇", "一四〇〇", "11317-11354", {
        4:["六十三","六十四","四十三","四十四"],
        5:["四十五","四十六"],
        6:["三十三","三十四","五十三","五十四"],
        7:["三十四","三十五"],
        9:["三十二","三十三"],
        10:["三十五","三十六"],
    }),
    _source_group("一四〇", "一四一〇", "11356-11389", {
        5:["三十三"], 6:["三十四","五十三","五十四"],
        7:["三十四"], 8:["四十七","四十八"],
        9:["三十二","三十三"], 10:["三十五","三十六"],
    }, "probable_ocr_correction_pending_image_check"),
])
for _group, _spans in [
    (GROUP_INDEX[24], ["11256","11257","11258","11259","11260","11261","11262","11263","11264","11265"]),
    (GROUP_INDEX[25], ["11268","11269","11270","11271","11272","11273","11274","11275","11276","11277"]),
    (GROUP_INDEX[26], ["11318-11318","11320-11321","11323-11324","11325-11329","11331-11333",
                       "11335-11339","11341-11343","11345-11346","11348-11350","11352-11354"]),
    (GROUP_INDEX[27], ["11357-11357","11359-11360","11362-11363","11365-11366","11368-11369",
                       "11371-11374","11376-11377","11379-11381","11383-11385","11387-11389"]),
]:
    for _entry, _span in zip(_group["entries"], _spans):
        _entry["pdf_text_lines"] = _span
        _entry["content_present"] = True
        _entry["number_field_present"] = False
        if _entry["age_markers"]:
            _entry["age_marker_association_status"] = "text_layer_sequence_associated_image_check_pending"
        else:
            _entry["age_marker_association_status"] = "age_not_listed_in_text_layer"

GROUP_INDEX.extend([
    _table_layout_group("一四二〇", "11393-11414",
        ["三十九","四十五","五十六","四十七","四十八","六十五","六十六","六十三","六十四","四十二"],
        ["11394;11405","11395;11406","11396;11407","11397;11408","11398;11409",
         "11399;11410","11400;11411","11401;11412","11402;11413","11403;11414"],
        "文本层先列十项岁数，再列十项正文；当前按序号顺序暂配，逐项对应仍待页面图像核验。"),
    _source_group("一四三〇", "一四三〇", "11416-11443", {
        1:["二十八"], 4:["十","四十七","七十八","七十七"],
        5:["六十三","六十四"], 6:["三十七","十八"],
        7:["三十五","五十四"], 8:["二十八"], 10:["五十二"],
    }),
    _source_group("一四四〇", "一四四〇", "11445-11474", {
        1:["八十九","九十"], 3:["二十九","四十"],
        4:["七十","四十九"], 5:["七十九","四十二"], 6:["十二"],
        8:["五十七","五十八"], 9:["五十四","五十五"], 10:["三十五","三十六"],
    }),
    _source_group("一四五〇", "一四五〇", "11489-11500", {}),
    _source_group("一四六〇", "一四六〇", "11501-11511", {}),
])
for _group, _spans in [
    (GROUP_INDEX[29], ["11418","11419-11420","11421-11424","11425-11426","11427-11428",
                       "11429-11430","11431","11432","11433","11434-11443"]),
    (GROUP_INDEX[30], ["11447-11448","11449","11450-11451","11452-11453","11454-11455",
                       "11456","11457","11458-11459","11460-11461","11462-11463"]),
    (GROUP_INDEX[31], ["11491","11492","11493","11494","11495","11496","11497","11498","11499","11500"]),
    (GROUP_INDEX[32], ["11502","11503","11504","11505","11506","11507","11508","11509","11510","11511"]),
]:
    for _entry, _span in zip(_group["entries"], _spans):
        _entry["pdf_text_lines"] = _span
        _entry["number_field_present"] = False
        _entry["content_present"] = True
        _entry["age_marker_association_status"] = (
            "text_layer_sequence_associated_image_check_pending" if _entry["age_markers"]
            else "age_not_listed_in_text_layer")
UNASSIGNED_BLOCKS.append({
    "block_id": "child_collection_unheaded_block_after_1380_candidate",
    "pdf_text_lines": "11279-11315",
    "entry_count": 10,
    "status": "group_marker_missing_do_not_assign",
    "note": "子集页眉后出现十项分行记录，至一四〇〇标题前未见独立组号。",
    "entries": [{"entry_sequence": n, "pdf_text_lines": line}
                for n, line in enumerate(
                    ["11281-11283","11285-11286","11288-11289","11291-11292","11294-11298",
                     "11300-11301","11303-11304","11306-11307","11309-11312","11314-11315"], 1)]
})

UNASSIGNED_BLOCKS.append({
    "block_id": "child_collection_unheaded_block_after_1320",
    "pdf_text_lines": "11202-11213",
    "entry_count": 10,
    "status": "group_marker_missing_do_not_assign",
    "note": "该块位于一三二〇表格之后、一三三〇组标题之前，文本层只有子集页眉，没有独立组号。",
    "entries": [{"entry_sequence": n, "pdf_text_lines": line}
                for n, line in enumerate(
                    ["11204","11205","11206","11207","11208","11209","11210","11211","11212","11213"], 1)]
})

CANDIDATE_GROUPS = [{
    "raw_group_marker": "一二〇〇",
    "normalized_group_marker_candidate": "一三〇〇",
    "pdf_text_lines": "11157-11170",
    "status": "probable_ocr_correction_pending_image_check",
    "entries": [
        {"entry_sequence": 1, "raw_age_column_text": "六十一", "pdf_text_lines": "11161"},
        {"entry_sequence": 2, "raw_age_column_text": "三十七", "pdf_text_lines": "11162"},
        {"entry_sequence": 3, "raw_age_column_text": "四十五", "pdf_text_lines": "11163"},
        {"entry_sequence": 4, "raw_age_column_text": "三十三", "pdf_text_lines": "11164"},
        {"entry_sequence": 5, "raw_age_column_text": "六十九", "pdf_text_lines": "11165"},
        {"entry_sequence": 6, "raw_age_column_text": "四十九", "pdf_text_lines": "11166"},
        {"entry_sequence": 7, "raw_age_column_text": "五十", "pdf_text_lines": "11167"},
        {"entry_sequence": 8, "raw_age_column_text": None, "pdf_text_lines": "11168"},
        {"entry_sequence": 9, "raw_age_column_text": "六十七", "pdf_text_lines": "11169"},
        {"entry_sequence": 10, "raw_age_column_text": None, "pdf_text_lines": "11170"},
    ],
}]
GROUP_ANOMALIES = [
    {
        "raw_group_marker": "一二九〇",
        "pdf_text_lines": "11153-11153",
        "status": "group_marker_seen_content_not_located_before_next_header",
        "normalized_group_marker_candidate": "一二九〇",
    },
    {
        "raw_header_text": "康节说身全书",
        "pdf_text_lines": "11155",
        "normalized_header_candidate": "康节说易全书",
        "status": "probable_ocr_error_pending_image_check",
    },
    {
        "raw_group_marker": "一二〇〇",
        "pdf_text_lines": "11157-11170",
        "normalized_group_marker_candidate": "一三〇〇",
        "status": "probable_ocr_correction_pending_image_check",
        "note": "位于一二九〇之后、一三二〇之前；按序列推测为一三〇〇，必须保留原始识别。",
    },
    {
        "expected_group_marker": "一三一〇",
        "status": "not_located_between_probable_1300_and_1320",
        "pdf_text_lines": "11157-11186",
    },
]

GROUP_INDEX.extend([
    _table_layout_group("一四八〇", "11518-11530",
        ["十七","十八","十九","四十二","四十三","五十","五十一","五十二","五十三","五十四"],
        ["11520","11521","11522","11523","11524","11525","11526","11527","11528","11529"]),
    _table_layout_group("一四九〇", "11532-11544",
        ["十七","十八","十九","四十一","五十五","五十六","五十九","六十","十九","四十九"],
        ["11534","11535","11536","11537","11538","11539","11540","11541","11542","11543"]),
    _table_layout_group("一五〇〇", "11546-11558",
        ["二十一","二十二","二十五","四十二","四十三","四十六","四十八","四十五","四十六","四十八"],
        ["11548","11549","11550","11551","11552","11553","11554","11555","11556","11557"]),
    _source_group("一五一〇", "一五一〇", "11564-11575", {
        1:["四十七"], 2:["四十八"], 3:["四十五"], 4:["四十六"],
        6:["四十七"], 7:["四十五"], 8:["三十七"],
        9:["三七十三","七十四"], 10:["六十六"],
    }),
    _source_group("一五三〇", "一五三〇", "11590-11601", {
        2:["四十七"], 4:["五十三"], 6:["五十五"],
        8:["五十一"], 9:["三十二","三十二","三十二"], 10:["九百"],
    }),
    _table_layout_group("一五四〇", "11626-11647",
        ["三十三","七十八","三十九","五十","四十四","四十四","三十六","十一","四十三","二十"],
        ["11627","11628","11629","11630","11631","11632","11633","11634","11635","11636"],
        "文本层先列十项独立数值，再列十项正文，按序号暂配；页面图像核验前不认定其字段语义。"),
    _source_group("一五五〇", "一五五〇", "11649-11670", {
        1:["三十三"], 3:["七十九"], 4:["三十四"], 5:["三十五"],
        7:["三十六"], 10:["二十"],
    }),
])
for _group, _spans in [
    (GROUP_INDEX[36], ["11565","11566","11567","11568","11569","11570","11571","11572","11573-11574","11575"]),
    (GROUP_INDEX[37], ["11591","11592","11593","11594","11595","11596","11597","11598","11599-11600","11601"]),
    (GROUP_INDEX[39], ["11650","11651","11652","11653","11654","11655","11656","11657","11658","11659"]),
]:
    for _entry, _span in zip(_group["entries"], _spans):
        _entry["pdf_text_lines"] = _span
        _entry["content_present"] = True
        _entry["number_field_present"] = False
        _entry["age_marker_association_status"] = (
            "text_layer_sequence_associated_image_check_pending" if _entry["age_markers"]
            else "age_not_listed_in_text_layer")

UNASSIGNED_BLOCKS.append({
    "block_id": "child_collection_unheaded_block_after_1530",
    "pdf_text_lines": "11605-11625",
    "entry_count": 10,
    "status": "group_marker_missing_do_not_assign",
    "note": "一五三〇组之后出现十项独立数值及十项正文，至一五四〇标题前未见独立组号；按序号对应关系仍待版面核验。",
    "entries": [{"entry_sequence": n, "pdf_text_lines": line}
                for n, line in enumerate(
                    ["11605","11606","11607","11608","11609","11610","11611","11612","11613","11614"], 1)]
})

CANDIDATE_GROUPS.append({
    "raw_group_marker": "二五二〇",
    "normalized_group_marker_candidate": "一五二〇",
    "pdf_text_lines": "11577-11588",
    "status": "probable_ocr_correction_pending_image_check",
    "entries": [
        {"entry_sequence": 1, "raw_age_column_text": "三十一", "pdf_text_lines": "11579"},
        {"entry_sequence": 2, "raw_age_column_text": "三十三", "pdf_text_lines": "11580"},
        {"entry_sequence": 3, "raw_age_column_text": "六十四", "pdf_text_lines": "11581"},
        {"entry_sequence": 4, "raw_age_column_text": "三十二", "pdf_text_lines": "11582"},
        {"entry_sequence": 5, "raw_age_column_text": None, "pdf_text_lines": "11583"},
        {"entry_sequence": 6, "raw_age_column_text": "六十三", "pdf_text_lines": "11584"},
        {"entry_sequence": 7, "raw_age_column_text": None, "pdf_text_lines": "11585"},
        {"entry_sequence": 8, "raw_age_column_text": None, "pdf_text_lines": "11586"},
        {"entry_sequence": 9, "raw_age_column_text": None, "pdf_text_lines": "11587"},
        {"entry_sequence": 10, "raw_age_column_text": "二十四", "pdf_text_lines": "11588"},
    ],
})

GROUP_ANOMALIES.extend([
    {"raw_group_marker":"一四七〇","pdf_text_lines":"11512-11516",
     "status":"group_marker_seen_content_not_located_before_next_header",
     "note":"标题后出现153页码，随后为一四八〇；未定位到一四七〇组十条正文。"},
    {"raw_group_marker":"二五二〇","normalized_group_marker_candidate":"一五二〇",
     "pdf_text_lines":"11577-11588","status":"probable_ocr_correction_pending_image_check"},
])
UNASSIGNED_BLOCKS.append({
    "block_id": "child_collection_unheaded_block_after_1440",
    "pdf_text_lines": "11476-11488",
    "entry_count": 10,
    "status": "group_marker_missing_do_not_assign",
    "note": "子集页眉后出现十项分行记录，至一四五〇标题前没有独立组号。",
    "entries": [{"entry_sequence": n, "pdf_text_lines": line}
                for n, line in enumerate(
                    ["11477","11478-11479","11480-11481","11482","11483","11484","11485","11486","11487","11488"], 1)]
})
GROUP_ANOMALIES.extend([
    {"raw_group_marker":"二三六〇","normalized_group_marker_candidate":"一三六〇",
     "pdf_text_lines":"11254","status":"probable_ocr_correction_pending_image_check"},
    {"raw_group_marker":"二三八〇","normalized_group_marker_candidate":"一三八〇",
     "pdf_text_lines":"11267","status":"probable_ocr_correction_pending_image_check"},
    {"expected_group_marker":"一三七〇","status":"not_located_between_1360_and_1380_candidates",
     "pdf_text_lines":"11254-11277"},
    {"expected_group_marker":"一三九〇","status":"not_located_between_1380_and_1400_candidates",
     "pdf_text_lines":"11267-11317"},
    {"raw_group_marker":"一四〇","normalized_group_marker_candidate":"一四一〇",
     "pdf_text_lines":"11356","status":"probable_truncated_group_marker_pending_image_check"},
])

GROUP_GAPS = [{
    "expected_group_marker": "一二一〇",
    "status": "not_located_between_1200_and_1220_in_available_pdf_text_layer",
    "evidence": "PDF text layer jumps from 一二〇〇 (10944-10956) to 一二二〇 (10958)",
    "action": "retain as an unverified gap; do not fabricate ten entries",
}]


# 一五六〇组：十条正文与十六项数值序列在文本层分离，暂不配对。
GROUP_INDEX.append({
    "group_marker": "一五六〇",
    "pdf_text_lines": "11672-11714",
    "entry_count": 10,
    "layout_status": "layout_alignment_unresolved",
    "layout_note": "文本层先列十个序号、随后连续列出十六个数值、再列十条正文；数值与正文的列/行配对无法仅凭文本层确定，故独立保存，不分配到具体条目。",
    "unassigned_number_sequence": {
        "raw_values": ["四十七","四十八","四十五","四十六","三十二","三十三","三十四","六十二","六十五","六十六","六十七","六十八","四十七","四十八","四十九","五十"],
        "pdf_text_lines": "11687-11702",
        "status": "sequence_located_entry_alignment_unresolved"
    },
    "entries": [
        {"entry_sequence": n, "raw_number_text": None, "number_field_present": None,
         "content_present": True, "pdf_text_lines": line,
         "age_markers": [], "age_marker_association_status": "unassigned_pending_page_image"}
        for n, line in enumerate(
            ["11704","11705","11706","11707","11708","11709","11710","11711","11712","11713"], 1)
    ],
})

UNASSIGNED_BLOCKS.extend([
    {
        "block_id": "child_collection_unheaded_block_after_1560",
        "pdf_text_lines": "11715-11750",
        "entry_count": 10,
        "status": "group_marker_missing_do_not_assign",
        "note": "十个序号、十五项数值及十条正文分段出现；无独立组号，数值与正文配对未明。",
        "entries": [{"entry_sequence": n, "pdf_text_lines": line}
                    for n, line in enumerate(
                        ["11715-11716","11717-11718","11719-11720","11721-11722","11723-11724",
                         "11725-11726","11727-11728","11729-11730","11731-11732","11733-11740"],1)]
    },
    {
        "block_id": "child_collection_unheaded_block_after_first_1560_orphan",
        "pdf_text_lines": "11752-11785",
        "entry_count": 10,
        "status": "group_marker_missing_do_not_assign",
        "note": "十个序号、十二项数值及十条正文分段出现；无独立组号，数值与正文配对未明。",
        "entries": [{"entry_sequence": n, "pdf_text_lines": line}
                    for n, line in enumerate(
                        ["11752-11753","11754-11755","11756-11757","11758-11759","11760-11761",
                         "11762-11763","11764-11765","11766-11767","11768-11769","11770-11775"],1)]
    }
])

CANDIDATE_GROUPS.extend([
    {"raw_group_marker":"五七〇","normalized_group_marker_candidate":"一五七〇",
     "pdf_text_lines":"11787","status":"probable_leading_digit_ocr_loss_pending_image_check","entries":[]},
    {"raw_group_marker":"五八〇","normalized_group_marker_candidate":"一五八〇",
     "pdf_text_lines":"11788","status":"probable_leading_digit_ocr_loss_pending_image_check","entries":[]},
    {"raw_group_marker":"五九〇","normalized_group_marker_candidate":"一五九〇",
     "pdf_text_lines":"11789","status":"probable_leading_digit_ocr_loss_pending_image_check","entries":[]}
])
GROUP_ANOMALIES.extend([
    {"raw_group_marker":"五七〇","normalized_group_marker_candidate":"一五七〇","pdf_text_lines":"11787",
     "status":"probable_leading_digit_ocr_loss_pending_image_check"},
    {"raw_group_marker":"五八〇","normalized_group_marker_candidate":"一五八〇","pdf_text_lines":"11788",
     "status":"probable_leading_digit_ocr_loss_pending_image_check"},
    {"raw_group_marker":"五九〇","normalized_group_marker_candidate":"一五九〇","pdf_text_lines":"11789",
     "status":"probable_leading_digit_ocr_loss_pending_image_check"}
])




# 一六〇〇至一六六〇：仅建立结构索引，岁数/对应数候选按原文行号保留。
def _indexed_entries(lines, start=1, raw_numbers=None):
    raw_numbers = raw_numbers or {}
    return [
        {"entry_sequence": n, "raw_number_text": raw_numbers.get(n),
         "number_field_present": (n in raw_numbers) if raw_numbers else None,
         "content_present": True, "pdf_text_lines": line,
         "age_markers": [], "age_marker_association_status": "needs_layout_verification"}
        for n, line in enumerate(lines, start)
    ]

GROUP_INDEX.extend([
    {
        "group_marker": "一六〇〇", "pdf_text_lines": "11814-11837",
        "layout_status": "text_layer_located_layout_unverified",
        "age_marker_candidates": [
            {"entry_sequence_hint": 1, "raw_text": "十／七十八", "pdf_text_lines": "11816"},
            {"entry_sequence_hint": 2, "raw_text": "五十五", "pdf_text_lines": "11818"},
            {"entry_sequence_hint": 3, "raw_text": "五十九", "pdf_text_lines": "11820"},
            {"entry_sequence_hint": 4, "raw_text": "二十", "pdf_text_lines": "11822"},
            {"entry_sequence_hint": 6, "raw_text": "六十七／六十八", "pdf_text_lines": "11826-11827"},
            {"entry_sequence_hint": 7, "raw_text": "三十八", "pdf_text_lines": "11829"},
            {"entry_sequence_hint": 10, "raw_text": "九十八／九十四／四十五", "pdf_text_lines": "11835-11837"}
        ],
        "entries": _indexed_entries(
            ["11816","11818","11820","11822","11824","11826-11827","11829","11831","11833","11835-11837"],
            raw_numbers={1:"十／七十八",2:"五十五",3:"五十九",4:"二十",6:"六十七／六十八",7:"三十八",10:"九十八／九十四／四十五"})
    },
    {
        "group_marker": "一六二〇", "pdf_text_lines": "11839-11860",
        "layout_status": "text_layer_located_layout_unverified",
        "age_marker_candidates": [
            {"entry_sequence_hint":1,"raw_text":"六十九","pdf_text_lines":"11841"},
            {"entry_sequence_hint":3,"raw_text":"四十九／五十","pdf_text_lines":"11845-11846"},
            {"entry_sequence_hint":4,"raw_text":"十","pdf_text_lines":"11848"},
            {"entry_sequence_hint":8,"raw_text":"三十三","pdf_text_lines":"11855"},
            {"entry_sequence_hint":10,"raw_text":"四十九／四十五","pdf_text_lines":"11859-11860"}
        ],
        "entries": _indexed_entries(
            ["11841","11843","11845-11846","11848","11850","11852","11854","11855","11857","11859-11860"],
            raw_numbers={1:"六十九",3:"四十九／五十",4:"十",8:"三十三",10:"四十九／四十五"})
    },
    {
        "group_marker": "一六三〇", "pdf_text_lines": "11868-11878",
        "layout_status": "text_layer_located_layout_unverified",
        "age_marker_candidates": [
            {"entry_sequence_hint":1,"raw_text":"二十七","pdf_text_lines":"11869"},
            {"entry_sequence_hint":2,"raw_text":"三十六","pdf_text_lines":"11870"},
            {"entry_sequence_hint":3,"raw_text":"三十三","pdf_text_lines":"11871"},
            {"entry_sequence_hint":5,"raw_text":"三十四","pdf_text_lines":"11873"},
            {"entry_sequence_hint":8,"raw_text":"五十五","pdf_text_lines":"11876"},
            {"entry_sequence_hint":9,"raw_text":"三十三","pdf_text_lines":"11877"},
            {"entry_sequence_hint":10,"raw_text":"五十三","pdf_text_lines":"11878"}
        ],
        "entries": _indexed_entries(
            ["11869","11870","11871","11872","11873","11874","11875","11876","11877","11878"],
            raw_numbers={1:"二十七",2:"三十六",3:"三十三",5:"三十四",8:"五十五",9:"三十三",10:"五十三"})
    },
    {
        "group_marker": "一六四〇", "pdf_text_lines": "11880-11890",
        "layout_status": "text_layer_located_layout_unverified",
        "age_marker_candidates": [
            {"entry_sequence_hint":2,"raw_text":"六十","pdf_text_lines":"11882"},
            {"entry_sequence_hint":4,"raw_text":"七十三","pdf_text_lines":"11884"},
            {"entry_sequence_hint":7,"raw_text":"三十九","pdf_text_lines":"11887"},
            {"entry_sequence_hint":8,"raw_text":"四十五","pdf_text_lines":"11888"},
            {"entry_sequence_hint":9,"raw_text":"四十七","pdf_text_lines":"11889"},
            {"entry_sequence_hint":10,"raw_text":"三十三／三十三","pdf_text_lines":"11890"}
        ],
        "entries": _indexed_entries(
            ["11881","11882","11883","11884","11885","11886","11887","11888","11889","11890"],
            raw_numbers={2:"六十",4:"七十三",7:"三十九",8:"四十五",9:"四十七",10:"三十三／三十三"})
    },
    {
        "group_marker": "一六五〇", "pdf_text_lines": "11891-11901",
        "layout_status": "text_layer_located_layout_unverified",
        "age_marker_candidates": [
            {"entry_sequence_hint":1,"raw_text":"四十三","pdf_text_lines":"11892"},
            {"entry_sequence_hint":2,"raw_text":"四十四","pdf_text_lines":"11893"},
            {"entry_sequence_hint":3,"raw_text":"四十一","pdf_text_lines":"11894"},
            {"entry_sequence_hint":5,"raw_text":"七十九","pdf_text_lines":"11896"},
            {"entry_sequence_hint":6,"raw_text":"四十五","pdf_text_lines":"11897"},
            {"entry_sequence_hint":7,"raw_text":"五十七","pdf_text_lines":"11898"},
            {"entry_sequence_hint":8,"raw_text":"五十二","pdf_text_lines":"11899"},
            {"entry_sequence_hint":9,"raw_text":"五十五","pdf_text_lines":"11900"},
            {"entry_sequence_hint":10,"raw_text":"五十六","pdf_text_lines":"11901"}
        ],
        "entries": _indexed_entries(
            ["11892","11893","11894","11895","11896","11897","11898","11899","11900","11901"],
            raw_numbers={1:"四十三",2:"四十四",3:"四十一",5:"七十九",6:"四十五",7:"五十七",8:"五十二",9:"五十五",10:"五十六"})
    },
    {
        "group_marker": "一六六〇", "pdf_text_lines": "11917-11927",
        "layout_status": "text_layer_located_content_without_independent_number_column",
        "layout_note": "文本层可见十条序号与正文，未见独立岁数/对应数栏；不从正文句内数字抽取对应数。",
        "entries": _indexed_entries(["11918","11919","11920","11921","11922","11923","11924","11925","11926","11927"])
    }
])

GROUP_GAPS.extend([
    {"expected_group_marker":"一六一〇","status":"not_located_between_1600_and_1620_in_available_pdf_text_layer",
     "evidence":"一六〇〇正文后直接出现一六二〇标题；当前文本层未见一六一〇组标题或十条正文。",
     "action":"retain as unverified gap; do not fabricate entries"},
    {"expected_group_marker":"一六一〇/一六二〇_boundary","status":"possible_missing_or_misread_group_marker",
     "evidence":"11839出现一六二〇；随后11862再次出现一六二〇，11864出现截断的一六三，11868出现完整一六三〇。",
     "action":"keep duplicate/truncated markers as anomalies pending page-image review"}
])
GROUP_ANOMALIES.extend([
    {"raw_group_marker":"一六二〇","pdf_text_lines":"11862","status":"duplicate_marker_after_1620_block_pending_image_check",
     "note":"一六二〇在11839和11862均出现；第二处之后有截断标题一六三。不得自动认定为新组。"},
    {"raw_group_marker":"一六三","normalized_group_marker_candidate":"一六三〇",
     "pdf_text_lines":"11864","status":"truncated_marker_candidate_pending_image_check"}
])
UNASSIGNED_BLOCKS.append({
    "block_id":"child_collection_unheaded_block_after_1650",
    "pdf_text_lines":"11907-11916","entry_count":10,
    "status":"group_marker_missing_do_not_assign",
    "note":"一六五〇十条后、一六六〇标题前出现十条连续内容，未见明确组号；单独保留，不并入相邻组。",
    "entries":[{"entry_sequence":n,"pdf_text_lines":line} for n,line in enumerate(
        ["11907","11908","11909","11910","11911","11912","11913","11914","11915","11916"],1)]
})

 
# 一六七〇至一七七〇：结构索引与异常隔离
GROUP_INDEX.extend([
{"group_marker":"一六七〇","pdf_text_lines":"11928-11939","layout_status":"text_layer_located_content_without_independent_number_column","layout_note":"十条序号与正文可定位；文本层未见独立对应数栏。","entries":_indexed_entries(["11930","11931","11932","11933","11934","11935","11936","11937","11938","11939"])},
{"group_marker":"一七〇〇","pdf_text_lines":"11960-11972","layout_status":"table_rows_year_sequence_clause","layout_note":"表格十项；原始数字字段保留，不解释为密码数。","entries":[
{"entry_sequence":1,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"11963"},
{"entry_sequence":2,"raw_number_text":"六十四／六十六","number_field_present":True,"content_present":True,"pdf_text_lines":"11964"},
{"entry_sequence":3,"raw_number_text":"三十五／三十六","number_field_present":True,"content_present":True,"pdf_text_lines":"11965"},
{"entry_sequence":4,"raw_number_text":"三十三／三十四","number_field_present":True,"content_present":True,"pdf_text_lines":"11966"},
{"entry_sequence":5,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"11967"},
{"entry_sequence":6,"raw_number_text":"三十三／三十四","number_field_present":True,"content_present":True,"pdf_text_lines":"11968"},
{"entry_sequence":7,"raw_number_text":"十九／二十","number_field_present":True,"content_present":True,"pdf_text_lines":"11969"},
{"entry_sequence":8,"raw_number_text":"五十二／五十三","number_field_present":True,"content_present":True,"pdf_text_lines":"11970"},
{"entry_sequence":9,"raw_number_text":"六十二／六十三","number_field_present":True,"content_present":True,"pdf_text_lines":"11971"},
{"entry_sequence":10,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"11972"}]},
{"group_marker":"一七二〇","pdf_text_lines":"12001-12011","layout_status":"text_layer_located_partial_sequence","layout_note":"仅定位序号二至十及续文；第1项未定位，保留9项。","entries":[
{"entry_sequence":2,"raw_number_text":"四十三","number_field_present":True,"content_present":True,"pdf_text_lines":"12002"},
{"entry_sequence":3,"raw_number_text":"五十九","number_field_present":True,"content_present":True,"pdf_text_lines":"12003"},
{"entry_sequence":4,"raw_number_text":"三十一","number_field_present":True,"content_present":True,"pdf_text_lines":"12004"},
{"entry_sequence":5,"raw_number_text":"五十八","number_field_present":True,"content_present":True,"pdf_text_lines":"12005"},
{"entry_sequence":6,"raw_number_text":"五十七","number_field_present":True,"content_present":True,"pdf_text_lines":"12006"},
{"entry_sequence":7,"raw_number_text":"六十一","number_field_present":True,"content_present":True,"pdf_text_lines":"12007"},
{"entry_sequence":8,"raw_number_text":"四十三／三十七","number_field_present":True,"content_present":True,"pdf_text_lines":"12008"},
{"entry_sequence":9,"raw_number_text":"三十八","number_field_present":True,"content_present":True,"pdf_text_lines":"12009"},
{"entry_sequence":10,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"12010-12011"}]},
{"group_marker":"一七三〇","pdf_text_lines":"12013-12024","layout_status":"text_layer_located_partial_sequence","layout_note":"仅定位序号二至十及续文；第1项未定位，保留9项。","entries":[
{"entry_sequence":2,"raw_number_text":"七十二","number_field_present":True,"content_present":True,"pdf_text_lines":"12015"},
{"entry_sequence":3,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"12016"},
{"entry_sequence":4,"raw_number_text":"六十三","number_field_present":True,"content_present":True,"pdf_text_lines":"12017"},
{"entry_sequence":5,"raw_number_text":"六十四","number_field_present":True,"content_present":True,"pdf_text_lines":"12018"},
{"entry_sequence":6,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"12019"},
{"entry_sequence":7,"raw_number_text":"四十一／四十二","number_field_present":True,"content_present":True,"pdf_text_lines":"12020"},
{"entry_sequence":8,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"12021"},
{"entry_sequence":9,"raw_number_text":"五十二／五十二","number_field_present":True,"content_present":True,"pdf_text_lines":"12022"},
{"entry_sequence":10,"raw_number_text":None,"number_field_present":False,"content_present":True,"pdf_text_lines":"12023-12024"}]},
{"group_marker":"一七五〇","pdf_text_lines":"12033-12043","layout_status":"text_layer_located_layout_unverified","entries":_indexed_entries(["12034","12035","12036","12037","12038","12039","12040","12041","12042","12043"],raw_numbers={1:"三十七",3:"三十九",5:"五十八",6:"二十七／三十八",7:"十四",8:"五十八",9:"二十四",10:"二十五／六十六"})},
{"group_marker":"一七六〇","pdf_text_lines":"12045-12056","layout_status":"text_layer_located_layout_unverified","entries":_indexed_entries(["12047","12048","12049","12050","12051","12052","12053","12054","12055","12056"],raw_numbers={1:"三十二",3:"五十七",4:"五十八",5:"四十九／三十三",6:"三十六",7:"四十五",8:"三十五／三十六",10:"六十一／六十三"})},
{"group_marker":"一七七〇","pdf_text_lines":"12058-12068","layout_status":"text_layer_located_layout_unverified","entries":_indexed_entries(["12059","12060","12061","12062","12063","12064","12065","12066","12067","12068"],raw_numbers={2:"七十五",3:"六十二",4:"四十五",5:"四十六／三十五",6:"三十六／二十一",8:"十九",10:"四十九／四十五／五十"})}
])
CANDIDATE_GROUPS.extend([
{"raw_group_marker":"一九〇","normalized_group_marker_candidate":"一六九〇","pdf_text_lines":"11946-11958","status":"probable_ocr_truncation_candidate_pending_image_check","entries":[
{"entry_sequence":1,"raw_age_column_text":"三十七","pdf_text_lines":"11949"},{"entry_sequence":2,"raw_age_column_text":"三十八","pdf_text_lines":"11950"},{"entry_sequence":3,"raw_age_column_text":None,"pdf_text_lines":"11951"},{"entry_sequence":4,"raw_age_column_text":"五十三／五十四／五十九","pdf_text_lines":"11952"},{"entry_sequence":5,"raw_age_column_text":"六十／五十七","pdf_text_lines":"11953"},{"entry_sequence":6,"raw_age_column_text":"五十八","pdf_text_lines":"11954"},{"entry_sequence":7,"raw_age_column_text":None,"pdf_text_lines":"11955"},{"entry_sequence":8,"raw_age_column_text":"六十七／六十八","pdf_text_lines":"11956"},{"entry_sequence":9,"raw_age_column_text":"三十三／三十四","pdf_text_lines":"11957"},{"entry_sequence":10,"raw_age_column_text":None,"pdf_text_lines":"11958"}]},
{"raw_group_marker":"一七〇〇","normalized_group_marker_candidate":"一七一〇","pdf_text_lines":"11974-11986","status":"duplicate_marker_possible_next_group_pending_image_check","entries":[{"entry_sequence":n,"raw_age_column_text":None,"pdf_text_lines":line} for n,line in enumerate(["11977","11978","11979","11980","11981","11982","11983","11984","11985","11986"],1)]}
])
GROUP_GAPS.extend([
{"expected_group_marker":"一六八〇","status":"marker_seen_content_not_located_in_text_layer","evidence":"11940出现一六八〇，未定位到其十条正文。","action":"retain marker-only anomaly; do not fabricate entries"},
{"expected_group_marker":"一七一〇","status":"possible_duplicate_1700_and_unheaded_block","evidence":"11974重复一七〇〇，11990-11999另有十项无组号内容。","action":"keep candidate and unheaded block separate"},
{"expected_group_marker":"一七四〇","status":"marker_seen_content_not_extractable_from_text_layer","evidence":"12026出现一七四〇，文本层未取得可逐项解析的正文。","action":"retain marker-only gap; do not infer entries"}
])
GROUP_ANOMALIES.extend([
{"raw_group_marker":"一六八〇","pdf_text_lines":"11940","status":"marker_seen_body_not_located"},
{"raw_group_marker":"一九〇","normalized_group_marker_candidate":"一六九〇","pdf_text_lines":"11946","status":"probable_ocr_truncation_candidate_pending_image_check"},
{"raw_group_marker":"一七〇〇","normalized_group_marker_candidate":"一七一〇","pdf_text_lines":"11974","status":"duplicate_marker_possible_next_group_pending_image_check"},
{"raw_group_marker":"一七四〇","pdf_text_lines":"12026","status":"marker_seen_body_not_extractable_from_text_layer"}
])
UNASSIGNED_BLOCKS.append({"block_id":"child_collection_unheaded_block_after_duplicate_1700","pdf_text_lines":"11990-11999","entry_count":10,"status":"group_marker_missing_do_not_assign","note":"疑似重复一七〇〇标题之后出现十条连续内容；可能与一七一〇有关，但无明确组号，不作归组。","entries":[{"entry_sequence":n,"pdf_text_lines":line} for n,line in enumerate(["11990","11991","11992","11993","11994","11995","11996","11997","11998","11999"],1)]})



# 子集后段：一七八〇至二〇一〇。仅记录可定位结构，不复制正文。
GROUP_INDEX.extend([
{"group_marker":"一七八〇","pdf_text_lines":"12079-12113","layout_status":"separate_number_and_clause_blocks","layout_note":"序号、数字序列与正文分块出现，数字序列暂不逐条配对。","unassigned_number_sequence":{"raw_values":["四十八","三十三","三十三","三十三","三十三","四十四","三十三","三十四","五十四","五十四","四十四","三十九"],"pdf_text_lines":"12091-12102","association_status":"unassigned_due_to_separate_layout"},"entries":_indexed_entries(["12104","12105","12106","12107","12108","12109","12110","12111","12112","12113"])},
{"group_marker":"一七九〇","pdf_text_lines":"12142-12171","layout_status":"separate_number_and_clause_blocks","layout_note":"十条正文与数字序列分块，数字序列不强行配对。","unassigned_number_sequence":{"raw_values":["八十","五十三","五十四","五十七","五十八","四十五","四十六"],"pdf_text_lines":"12154-12160","association_status":"unassigned_due_to_separate_layout"},"entries":_indexed_entries(["12162","12163","12164","12165","12166","12167","12168","12169","12170","12171"])},
{"group_marker":"一八〇〇","pdf_text_lines":"12173-12214","layout_status":"mixed_interleaved_number_and_clause_blocks","unassigned_number_sequence":{"raw_values":["七十九","八十","四十三","四十四","十七","五十五","三十五","三十九","四十"],"pdf_text_lines":"12181-12210","association_status":"partial_layout_not_fully_associated"},"entries":_indexed_entries(["12178","12185","12188","12191","12195","12198","12201","12205","12211","12214"])},
{"group_marker":"一八一〇","pdf_text_lines":"12216-12264","layout_status":"text_layer_located_layout_unverified","entries":_indexed_entries(["12222","12227","12231","12236","12241","12246","12249","12254","12259","12264"],raw_numbers={1:"三十七／三十八／四十七",2:"十二／十六",3:"三十二／三十三",4:"四十二／四十三",5:"四十五／四十六",6:"五十五／五十六",8:"七十二／七十三",9:"六十三／六十四",10:"七十五／七十六"})},
{"group_marker":"一八二〇","pdf_text_lines":"12266-12307","layout_status":"text_layer_located_layout_unverified","entries":_indexed_entries(["12271","12276","12281","12285","12288","12293","12296","12299","12304","12307"],raw_numbers={1:"十／十三",2:"十五／十六",3:"十五／十六",4:"五十五",6:"四十二／四十三",9:"五十七／五十八"})},
{"group_marker":"一八四〇","pdf_text_lines":"12314-12324","layout_status":"text_layer_located_inline_rows","entries":_indexed_entries(["12315","12316","12317","12318","12319","12320","12321","12322","12323","12324"],raw_numbers={1:"四十九",2:"五十",3:"五十三",4:"五十二",5:"五十一",6:"六十七",7:"六十六",8:"六十三",9:"六十四",10:"三十二"})},
{"group_marker":"一八五〇","pdf_text_lines":"12326-12337","layout_status":"text_layer_located_inline_rows","entries":_indexed_entries(["12328","12329","12330","12331","12332","12333","12334","12335","12336","12337"],raw_numbers={1:"七十一",2:"七十",3:"五十三",4:"五十四",5:"四十八",6:"二十",8:"三十五",9:"三十三",10:"三十二"})},
{"group_marker":"一八六〇","pdf_text_lines":"12339-12349","layout_status":"text_layer_located_inline_rows","entries":_indexed_entries(["12340","12341","12342","12343","12344","12345","12346","12347","12348","12349"],raw_numbers={1:"三十一",2:"三十九",4:"三十九",5:"三十六",6:"三十五",7:"三十三",9:"三十五",10:"四十二"})},
{"group_marker":"一八七〇","pdf_text_lines":"12353-12364","layout_status":"text_layer_located_inline_rows","entries":_indexed_entries(["12355","12356","12357","12358","12359","12360","12361","12362","12363","12364"],raw_numbers={1:"五十七",2:"五十八",3:"五十二",4:"三十七／三十八",6:"六十一／六十三／六十七",7:"六十八",8:"四十"})},
{"group_marker":"一八八〇","pdf_text_lines":"12366-12376","layout_status":"text_layer_located_inline_rows","entries":_indexed_entries(["12367","12368","12369","12370","12371","12372","12373","12374","12375","12376"],raw_numbers={2:"五十七",3:"五十七／七十七／七十八",4:"三十一／三十二",5:"三十二",6:"二十九",7:"七十九／八十",8:"三十二",9:"三十五／三十六",10:"三十七／三十八"})},
{"group_marker":"一八九〇","pdf_text_lines":"12378-12389","layout_status":"text_layer_located_inline_rows_with_age_marker","age_marker_candidates":[{"entry_sequence_hint":1,"raw_text":"九十岁","pdf_text_lines":"12380"}],"entries":_indexed_entries(["12380","12381","12382","12383","12384","12385","12386","12387","12388","12389"],raw_numbers={1:"三十三",2:"三十三",3:"三十四／三十五／三十六",5:"六十七",6:"二十四",7:"五十九",8:"五十五",10:"三十二"})},
{"group_marker":"一九〇〇","pdf_text_lines":"12403-12414","layout_status":"text_layer_located_inline_rows_with_ocr_uncertainty","entries":_indexed_entries(["12405","12406","12407","12408","12409","12410","12411","12412","12413","12414"],raw_numbers={1:"十九",2:"五十三／五十四",3:"五十二",4:"四十九",5:"三十",6:"六十三",7:"三十五／三十六",8:"三四岁",9:"——",10:"六十五"})},
{"group_marker":"一九一〇","pdf_text_lines":"12416-12426","layout_status":"text_layer_located_inline_rows_with_age_markers","entries":_indexed_entries(["12417","12418","12419","12420","12421","12422","12423","12424","12425","12426"],raw_numbers={3:"六十三／六十四",6:"二十七",8:"十九岁",9:"五十八",10:"——"})},
{"group_marker":"一九三〇","pdf_text_lines":"12430-12445","layout_status":"split_number_lines_pending_association","unassigned_number_sequence":{"raw_values":["五十九／六十","四十七／四十八","六十六","九十五／九十六","三十五／三十六","五十七／五十八"],"pdf_text_lines":"12432-12445","association_status":"sequence_lines_associated_to_entries_but_layout_pending"},"entries":_indexed_entries(["12431","12433","12435","12436","12437","12439","12440","12442","12443","12445"])},
{"group_marker":"一九四〇","pdf_text_lines":"12446-12459","layout_status":"split_number_lines_pending_association","unassigned_number_sequence":{"raw_values":["七十六","七十","五十二／五十三","十七／十八","三十四／三十五","五六岁"],"pdf_text_lines":"12447-12459","association_status":"sequence_lines_associated_to_entries_but_layout_pending"},"entries":_indexed_entries(["12447","12448","12449","12451","12453","12455","12456","12457","12458","12459"])},
{"group_marker":"一九五〇","pdf_text_lines":"12461-12478","layout_status":"split_number_lines_pending_association","unassigned_number_sequence":{"raw_values":["五十一／五十二","六十四／五十九／六十","十二／九十","六十一／六十三／六十四","三十七／三十八"],"pdf_text_lines":"12462-12478","association_status":"sequence_lines_associated_to_entries_but_layout_pending"},"entries":_indexed_entries(["12463","12464","12465","12468","12469","12470","12472","12473","12476","12478"])},
{"group_marker":"一九六〇","pdf_text_lines":"12483-12493","layout_status":"text_layer_located_inline_rows","entries":_indexed_entries(["12484","12485","12486","12487","12488","12489","12490","12491","12492","12493"],raw_numbers={1:"二十三",6:"五十三／五十四",7:"一岁",10:"五十二／五十二"})},
{"group_marker":"一九七〇","pdf_text_lines":"12495-12505","layout_status":"text_layer_located_inline_rows_with_age_candidates","age_marker_candidates":[{"entry_sequence_hint":1,"raw_text":"七十","pdf_text_lines":"12496"},{"entry_sequence_hint":8,"raw_text":"七旬加五","pdf_text_lines":"12503"}],"entries":_indexed_entries(["12496","12497","12498","12499","12500","12501","12502","12503","12504","12505"],raw_numbers={1:"七十",2:"三十三",3:"三十三",4:"四十九",10:"七八四十四／四十四"})},
{"group_marker":"一九八〇","pdf_text_lines":"12506-12516","layout_status":"text_layer_located_inline_rows_with_age_candidates","age_marker_candidates":[{"entry_sequence_hint":3,"raw_text":"三岁","pdf_text_lines":"12509"},{"entry_sequence_hint":4,"raw_text":"六旬加五","pdf_text_lines":"12510"}],"entries":_indexed_entries(["12507","12508","12509","12510","12511","12512","12513","12514","12515","12516"],raw_numbers={1:"四十九"})},
{"group_marker":"一九九〇","pdf_text_lines":"12533-12543","layout_status":"text_layer_located_inline_rows","entries":_indexed_entries(["12534","12535","12536","12537","12538","12539","12540","12541","12542","12543"],raw_numbers={1:"五十二／五十三",4:"十二／九十九",5:"三十三／十九／三十",7:"三十三／十三",8:"三十三／十三",9:"四十九",10:"七十三"})},
{"group_marker":"二〇一〇","pdf_text_lines":"12558-12568","layout_status":"text_layer_located_content_without_independent_number_column","entries":_indexed_entries(["12559","12560","12561","12562","12563","12564","12565","12566","12567","12568"])}
])
GROUP_GAPS.extend([
{"expected_group_marker":"一八三〇","status":"marker_seen_body_not_extractable","evidence":"12309-12311仅有一八三〇页面视觉元素说明，未定位十条正文文本。","action":"retain marker-only gap"},
{"expected_group_marker":"一九二〇","status":"marker_not_located_between_1910_and_1930","evidence":"12426后一组标题为一九三〇，文本层未见一九二〇。","action":"do not fabricate group"},
{"expected_group_marker":"二〇〇〇","status":"marker_not_located_between_1990_and_2010","evidence":"12543后一组为扭秧无标题块，再出现二〇一〇。","action":"keep unheaded block separate"},
{"expected_group_marker":"二〇二〇","status":"marker_seen_no_body_before_chou_collection","evidence":"12570出现二〇二〇，12572即转入丑集页眉，未定位十条正文。","action":"retain marker-only gap"}
])
GROUP_ANOMALIES.extend([
{"raw_group_marker":"一八三〇","pdf_text_lines":"12309-12311","status":"marker_visible_body_only_visual_summary"},
{"raw_group_marker":"一九二〇","pdf_text_lines":"12426-12430","status":"missing_marker_between_1910_and_1930"},
{"raw_group_marker":"二〇〇〇","pdf_text_lines":"12543-12558","status":"missing_marker_unheaded_block_between_1990_and_2010"},
{"raw_group_marker":"二〇二〇","pdf_text_lines":"12570-12572","status":"marker_seen_no_body_before_next_collection"}
])
UNASSIGNED_BLOCKS.append({"block_id":"child_collection_unheaded_block_niu_yang_after_1990","pdf_text_lines":"12545-12556","entry_count":10,"status":"named_unheaded_section_not_assigned_to_group","note":"标题为“扭秧”的十条独立内容，不能推定为二〇〇〇组。","entries":[{"entry_sequence":n,"pdf_text_lines":line} for n,line in enumerate(["12547","12548","12549","12550","12551","12552","12553","12554","12555","12556"],1)]})


def get_group_index():
    return {
        "edition": EDITION,
        "collection": "子集",
        "status": "text_layer_indexed_image_verification_pending",
        "group_count": len(GROUP_INDEX),
        "group_gaps": [dict(x) for x in GROUP_GAPS],
        "unassigned_blocks": [dict(x, entries=[dict(e) for e in x["entries"]]) for x in UNASSIGNED_BLOCKS],
        "group_anomalies": [dict(x) for x in GROUP_ANOMALIES],
        "candidate_groups": [dict(x, entries=[dict(e) for e in x["entries"]]) for x in CANDIDATE_GROUPS],
        "status": "mixed_text_layer_index_and_layout_pending",
        "entry_count": sum(len(group["entries"]) for group in GROUP_INDEX),
        "groups": [
            {"group_marker": group["group_marker"],
             "pdf_text_lines": group["pdf_text_lines"],
             "entry_count": len(group["entries"]),
             "layout_status": group.get("layout_status", "text_layer_indexed_image_verification_pending"),
             "raw_group_marker": group.get("raw_group_marker", group["group_marker"]),
             "normalized_group_marker_candidate": group.get("normalized_group_marker_candidate", group["group_marker"]),
             "normalization_status": group.get("normalization_status", "verified_text_layer_group_marker"),
             "source_header_ocr": dict(group["source_header_ocr"]) if group.get("source_header_ocr") else None,
             "age_marker_ambiguities": [dict(x) for x in group.get("age_marker_ambiguities", [])],
             "age_marker_candidates": [dict(x) for x in group.get("age_marker_candidates", [])],
             "entries": [dict(entry) for entry in group["entries"]],
             "layout_note": group.get("layout_note"),
             "unassigned_number_sequence": dict(group["unassigned_number_sequence"]) if group.get("unassigned_number_sequence") else None }
            for group in GROUP_INDEX
        ],
        "limitations": [
            "仅为PDF文本层字段索引，未逐字对照扫描图像。",
            "不复制完整条文正文；请按PDF行号核对。",
            "raw_number_text只记录独立数字栏，条文句内数字不转入该字段。",
            "空值表示原文该条没有独立数字栏，不允许按相邻条目补齐。",
            "一一一〇至一一三〇组的岁数只作为待核候选，不代表已确认归属。",
            "对应数栏未知时保留null，不得解释为原书没有对应数。",
            "一一四〇至一一六〇组采用序号—岁数—正文分行版式，岁数字段不等于对应数栏。",
            "本索引不构成铁板密码条号，不用于自动考刻或断命。"
        ]
    }


# 2003点校本目录页所列的分集起始印刷页。仅记录起始页，不推断结束页。
COLLECTION_METADATA = {
    "子": {"printed_page_start": 138, "pdf_text_line_start": 10664, "pdf_text_line_end": 12570, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "丑": {"printed_page_start": 172, "pdf_text_line_start": 12572, "pdf_text_line_end": 14290, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "寅": {"printed_page_start": 206, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "卯": {"printed_page_start": 240, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "辰": {"printed_page_start": 274, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "巳": {"printed_page_start": 308, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "午": {"printed_page_start": 342, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "未": {"printed_page_start": 376, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "申": {"printed_page_start": 410, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "酉": {"printed_page_start": 444, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "戌": {"printed_page_start": 478, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
    "亥": {"printed_page_start": 512, "toc_status": "located_in_contents", "index_status": "not_transcribed", "indexed_groups": 0, "indexed_entries": 0},
}


# 丑集首批结构索引：仅记录分组标题、序号和PDF文本行，不复制条文正文。
# 组号保留PDF文本层的原始圆圈字符“○”，不擅自统一为“〇”。
def _chou_group(raw_marker, header_line, entry_lines, layout_status="text_layer_rows_located_image_check_pending", occurrence=1):
    return {
        "collection": "丑",
        "raw_group_marker": raw_marker,
        "occurrence": occurrence,
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": header_line,
        "pdf_text_lines": f"{header_line}-{entry_lines[-1]}",
        "layout_status": layout_status,
        "entry_count": len(entry_lines),
        "entries": [
            {"entry_sequence": sequence, "pdf_text_line": line}
            for sequence, line in enumerate(entry_lines, 1)
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending",
    }


CHOU_GROUP_INDEX = [
    _chou_group("二○三○", 12576, list(range(12577, 12587))),
    _chou_group("二○四○", 12588, list(range(12589, 12599))),
    _chou_group("二○五○", 12599, list(range(12600, 12610))),
    _chou_group("二○六○", 12613, list(range(12615, 12625))),
    _chou_group("二○七○", 12626, list(range(12627, 12637))),
    _chou_group("二○八○", 12638, list(range(12640, 12650))),
    _chou_group("二○九○", 12664, list(range(12667, 12677)), "table_rows_text_layer_located"),
    _chou_group("二一○○", 12689, list(range(12693, 12703)), "table_rows_text_layer_located"),
    _chou_group("二一一○", 12714, list(range(12718, 12728)), "table_rows_text_layer_located"),
    _chou_group("二一二○", 12732, list(range(12733, 12743))),
    _chou_group("二二三○", 12744, list(range(12746, 12756))),
    _chou_group("二二四○", 12757, list(range(12758, 12768))),
    # The source text layer shows the abbreviated marker 二六○ exactly;
    # do not normalize it to 二二六○ without page-image confirmation.
    {
        "collection": "丑",
        "raw_group_marker": "二六○",
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": 12798,
        "pdf_text_lines": "12798-12809",
        "layout_status": "text_layer_span_located_entry_alignment_unresolved",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": sequence, "pdf_text_line": None,
             "source_span": "12799-12809",
             "alignment_status": "ten_entries_reported_span_has_eleven_text_lines_pending_image_check"}
            for sequence in range(1, 11)
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending",
    },
    _chou_group("二一八○", 12824, list(range(12825, 12835))),
    _chou_group("二一九○", 12836, list(range(12838, 12848))),
    _chou_group("二二一○", 12851, list(range(12851, 12861)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二二二○", 12863, list(range(12863, 12873)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二二三○", 12875, list(range(12875, 12885)), "table_rows_text_layer_located_title_row_is_entry_1", occurrence=2),
    _chou_group("二二四○", 12894, list(range(12895, 12905)), occurrence=2),
    _chou_group("二二五○", 12906, list(range(12908, 12918))),
    _chou_group("二二六○", 12919, list(range(12920, 12930))),
    _chou_group("二三○○", 12969, list(range(12969, 12979)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二三一○", 12981, list(range(12981, 12991)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二三二○", 12993, list(range(12993, 13003)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二三三○", 13019, list(range(13021, 13031))),
    _chou_group("二三四○", 13032, list(range(13033, 13043))),
    {
        "collection": "丑", "raw_group_marker": "二三五○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13044,
        "pdf_text_lines": "13044-13076", "layout_status": "multi_line_entry_layout_structured_by_sequence_markers",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 13052, "record_span": "13052-13053"},
            {"entry_sequence": 2, "pdf_text_line": 13054, "record_span": "13054-13055"},
            {"entry_sequence": 3, "pdf_text_line": 13056, "record_span": "13056-13057"},
            {"entry_sequence": 4, "pdf_text_line": 13058, "record_span": "13058-13059"},
            {"entry_sequence": 5, "pdf_text_line": 13060, "record_span": "13060-13061"},
            {"entry_sequence": 6, "pdf_text_line": 13062, "record_span": "13062-13064"},
            {"entry_sequence": 7, "pdf_text_line": 13065, "record_span": "13065-13067"},
            {"entry_sequence": 8, "pdf_text_line": 13068, "record_span": "13068-13070"},
            {"entry_sequence": 9, "pdf_text_line": 13071, "record_span": "13071-13073"},
            {"entry_sequence": 10, "pdf_text_line": 13074, "record_span": "13074-13076"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二三六○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13077,
        "pdf_text_lines": "13077-13099", "layout_status": "multi_line_age_clause_layout_text_layer_only",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 13079, "record_span": "13079-13080"},
            {"entry_sequence": 2, "pdf_text_line": 13081, "record_span": "13081-13082"},
            {"entry_sequence": 3, "pdf_text_line": 13083, "record_span": "13083-13084"},
            {"entry_sequence": 4, "pdf_text_line": 13085, "record_span": "13085-13086"},
            {"entry_sequence": 5, "pdf_text_line": 13087, "record_span": "13087-13089"},
            {"entry_sequence": 6, "pdf_text_line": 13090, "record_span": "13090-13091"},
            {"entry_sequence": 7, "pdf_text_line": 13092, "record_span": "13092-13093"},
            {"entry_sequence": 8, "pdf_text_line": 13094, "record_span": "13094-13095"},
            {"entry_sequence": 9, "pdf_text_line": 13096, "record_span": "13096-13097"},
            {"entry_sequence": 10, "pdf_text_line": 13098, "record_span": "13098-13099"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二三七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13101,
        "pdf_text_lines": "13101-13123", "layout_status": "multi_line_age_clause_layout_text_layer_only",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 13103, "record_span": "13103-13104"},
            {"entry_sequence": 2, "pdf_text_line": 13105, "record_span": "13105-13106"},
            {"entry_sequence": 3, "pdf_text_line": 13107, "record_span": "13107-13108"},
            {"entry_sequence": 4, "pdf_text_line": 13109, "record_span": "13109-13110"},
            {"entry_sequence": 5, "pdf_text_line": 13111, "record_span": "13111-13112"},
            {"entry_sequence": 6, "pdf_text_line": 13113, "record_span": "13113-13114"},
            {"entry_sequence": 7, "pdf_text_line": 13115, "record_span": "13115-13116"},
            {"entry_sequence": 8, "pdf_text_line": 13117, "record_span": "13117-13118"},
            {"entry_sequence": 9, "pdf_text_line": 13119, "record_span": "13119-13120"},
            {"entry_sequence": 10, "pdf_text_line": 13122, "record_span": "13122-13123"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二三八○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13125,
        "pdf_text_lines": "13125-13159", "layout_status": "multi_line_age_clause_layout_boundary_ambiguous",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 13129, "record_span": "13129-13131"},
            {"entry_sequence": 2, "pdf_text_line": 13133, "record_span": "13133-13134"},
            {"entry_sequence": 3, "pdf_text_line": 13136, "record_span": "13136-13137"},
            {"entry_sequence": 4, "pdf_text_line": 13139, "record_span": "13139-13140"},
            {"entry_sequence": 5, "pdf_text_line": 13142, "record_span": "13142-13144"},
            {"entry_sequence": 6, "pdf_text_line": 13146, "record_span": "13146-13147"},
            {"entry_sequence": 7, "pdf_text_line": 13149, "record_span": "13149-13150"},
            {"entry_sequence": 8, "pdf_text_line": 13152, "record_span": "13152-13153"},
            {"entry_sequence": 9, "pdf_text_line": 13155, "record_span": "13155-13156"},
            {"entry_sequence": 10, "pdf_text_line": 13158, "record_span": "13158-13159",
             "boundary_note": "末行含二三九○字样，是否同时承担下一组标识待版面复核"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
]72,
     "normalized_group_marker_candidate": None,
     "status": "raw_marker_preserved_numbering_interpretation_unresolved",
     "note": "文本层原样为二五○，后文另有明确二二五○（12906行）；不得仅凭顺序自动改写。"},
    {"raw_group_marker": "二六○", "pdf_text_line": 12798,
     "normalized_group_marker_candidate": None,
     "status": "raw_marker_preserved_numbering_interpretation_unresolved",
     "note": "文本层原样为二六○，后文另有明确二二六○（12919行）；该处十条行位尚待扫描页复核。"},
    {"raw_group_marker": "二二三○", "pdf_text_line": 12875,
     "occurrence": 2, "status": "repeated_group_marker_second_occurrence",
     "note": "前段12744行已出现同名组号，按不同出现位置独立保存。"},
    {"raw_group_marker": "二二四○", "pdf_text_line": 12894,
     "occurrence": 2, "status": "repeated_group_marker_second_occurrence",
     "note": "前段12757行已出现同名组号，按不同出现位置独立保存。"}
]

CHOU_UNASSIGNED_BLOCKS = [
    {"block_id": "chou_unheaded_entries_after_raw_marker_二五○",
     "pdf_text_lines": "12785-12797", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chou_unheaded_entries_after_raw_marker_二六○",
     "pdf_text_lines": "12813-12823", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign",
     "note": "位于原始组号二六○之后、二一八○标题之前，序列异常；不自动补成二二六○。"},
    {"block_id": "chou_unheaded_entries_before_2330",
     "pdf_text_lines": "13008-13017", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign",
     "note": "位于二三二○表格之后、二三三○标题之前，保留为独立无组号块。"}
]


def get_collection_branch_group_index(branch):
    if branch == "子":
        return get_group_index()
    if branch == "丑":
        return {
            "edition": EDITION,
            "collection": "丑集",
            "status": "partial_text_layer_index_image_verification_pending",
            "group_count": len(CHOU_GROUP_INDEX),
            "entry_count": sum(len(group["entries"]) for group in CHOU_GROUP_INDEX),
            "groups": [dict(group, entries=[dict(entry) for entry in group["entries"]])
                       for group in CHOU_GROUP_INDEX],
            "group_anomalies": [dict(item) for item in CHOU_GROUP_ANOMALIES],
            "unassigned_blocks": [dict(item) for item in CHOU_UNASSIGNED_BLOCKS],
            "limitations": [
                "本批仅索引丑集已定位组号的结构记录，不能代表丑集全部内容。",
                "仅保存组号、序号和PDF文本行，不复制条文正文。",
                "PDF文本层中的组号保留原始字符，未擅自规范化。",
                "所有行号和分组结构仍需扫描页面图像复核。",
                "未索引的中间组号、缺组和版式异常不自动补造。",
                "丑集原始二五○、二六○与后文二二五○、二二六○分开登记；二二三○、二二四○重复出现时按位置分别记录。无组号内容仍独立保存。",
                "该结构索引不是坤集密码表，不可用于自动考刻、定数或断命。"
            ]
        }
    return {
        "edition": EDITION,
        "collection": branch,
        "status": "not_transcribed",
        "group_count": 0,
        "entry_count": 0,
        "groups": [],
        "limitations": ["该分集尚未开始结构索引。"]
    }


def get_collection_progress():
    return {
        "edition": EDITION,
        "source_note": "分集起始印刷页来自2003点校本目录；仅登记起始页，不推断结束页或正文条数。",
        "collections": [
            {"collection": branch, **dict(values), **(
                ({"indexed_groups": len(GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in GROUP_INDEX)} if branch == "子" else
                 {"indexed_groups": len(CHOU_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in CHOU_GROUP_INDEX)} if branch == "丑" else {})
            )}
            for branch, values in COLLECTION_METADATA.items()
        ],
        "limitations": [
            "目录页码定位不代表正文已经转录。",
            "子集索引是PDF文本层结构记录，仍待扫描图像核验。",
            "丑集正式组号索引与异常组号、无组号块分开保存；扫描图像核验待完成。",
            "PDF文本层行号不是印刷页码；所有组号与条目结构仍需逐项核对。",
            "未核实的组号、对应数和条文不生成、不补齐。"
        ]
    }


def get_collection_sample(branch="子"):
    if branch == "丑":
        index = get_collection_branch_group_index(branch)
        return {
            "edition": EDITION,
            "collection": "丑集",
            "status": index["status"],
            "printed_page_start": COLLECTION_METADATA[branch].get("printed_page_start"),
            "entry_count": index["entry_count"],
            "entries": [],
            "group_index": index,
            "field_guide": dict(FIELD_GUIDE),
            "limitations": list(index["limitations"]),
        }
    if branch != "子":
        details = dict(COLLECTION_METADATA.get(branch, {}))
        return {
            "edition": EDITION,
            "collection": branch,
            "status": "not_transcribed",
            "printed_page_start": details.get("printed_page_start"),
            "toc_status": details.get("toc_status", "not_located"),
            "entry_count": 0,
            "entries": [],
            "field_guide": dict(FIELD_GUIDE),
            "limitations": ["该分集尚未完成逐条转录。", "目录起始页不代表正文已核对。"],
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
        "entries": [dict(row) for row in ENTRIES],
        "field_guide": dict(FIELD_GUIDE),
        "limitations": list(LIMITATIONS),
    }
