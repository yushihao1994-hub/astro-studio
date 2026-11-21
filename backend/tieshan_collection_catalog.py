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

GROUP_GAPS = [{
    "expected_group_marker": "一二一〇",
    "status": "not_located_between_1200_and_1220_in_available_pdf_text_layer",
    "evidence": "PDF text layer jumps from 一二〇〇 (10944-10956) to 一二二〇 (10958)",
    "action": "retain as an unverified gap; do not fabricate ten entries",
}]


def get_group_index():
    return {
        "edition": EDITION,
        "collection": "子集",
        "status": "text_layer_indexed_image_verification_pending",
        "group_count": len(GROUP_INDEX),
        "group_gaps": [dict(x) for x in GROUP_GAPS],
        "unassigned_blocks": [dict(x, entries=[dict(e) for e in x["entries"]]) for x in UNASSIGNED_BLOCKS],
        "group_anomalies": [dict(x) for x in GROUP_ANOMALIES],
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
             "layout_note": group.get("layout_note") }
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
        "entries": [dict(row) for row in ENTRIES],
        "field_guide": dict(FIELD_GUIDE),
        "limitations": list(LIMITATIONS),
    }
