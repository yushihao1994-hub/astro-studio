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
    "丑": {"printed_page_start": 172, "pdf_text_line_start": 12572, "pdf_text_line_end": 14174, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "寅": {"printed_page_start": 206, "pdf_text_line_start": 14175, "pdf_text_line_end": 15796, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "卯": {"printed_page_start": 240, "pdf_text_line_start": 15797, "pdf_text_line_end": 17108, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "辰": {"printed_page_start": 274, "pdf_text_line_start": 17109, "pdf_text_line_end": 18702, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "巳": {"printed_page_start": 308, "pdf_text_line_start": 18706, "pdf_text_line_end": 20328, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "午": {"printed_page_start": 342, "pdf_text_line_start": 20332, "pdf_text_line_end": 21988, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
    "未": {"printed_page_start": 376, "pdf_text_line_start": 21990, "toc_status": "located_in_contents", "index_status": "partial_text_layer_index", "indexed_groups": None, "indexed_entries": None},
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
    _chou_group("二四二○", 13233, list(range(13233, 13243)), "table_ten_rows_without_explicit_sequence_column"),
    _chou_group("二四三○", 13247, list(range(13247, 13257)), "table_ten_rows_without_explicit_sequence_column"),
    _chou_group("二四四○", 13261, list(range(13261, 13271)), "table_ten_rows_without_explicit_sequence_column"),
    _chou_group("二四五○", 13279, list(range(13279, 13289)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二四六○", 13291, list(range(13291, 13301)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二四七○", 13303, list(range(13303, 13313)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chou_group("二四八○", 13331, list(range(13333, 13343))),
    _chou_group("二四九○", 13344, list(range(13345, 13355))),
    _chou_group("二五一○", 13360, list(range(13362, 13372))),
    _chou_group("二五二○", 13373, list(range(13374, 13384))),
    _chou_group("二五三○", 13385, list(range(13387, 13397))),
    _chou_group("二五四○", 13410, list(range(13412, 13422))),
    _chou_group("二五五○", 13423, list(range(13424, 13434))),
    _chou_group("二五七○", 13443, list(range(13446, 13456)), "table_rows_text_layer_located"),
    _chou_group("二五八○", 13457, list(range(13460, 13470)), "table_rows_text_layer_located"),
    _chou_group("二五九○", 13471, list(range(13474, 13484)), "table_rows_text_layer_located"),
    _chou_group("二六一", 13487, list(range(13487, 13497)), "raw_short_marker_table_rows_title_row_is_entry_1"),
    _chou_group("二六○", 13499, list(range(13499, 13509)), "raw_short_marker_table_rows_title_row_is_entry_1", occurrence=2),
    _chou_group("二六二", 13511, list(range(13511, 13521)), "raw_short_marker_table_rows_title_row_is_entry_1"),
    _chou_group("二六三○", 13546, list(range(13547, 13557)), "ten_clause_lines_without_visible_sequence_column"),
    {
        "collection": "丑", "raw_group_marker": "二六五○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13617,
        "pdf_text_lines": "13617-13640", "layout_status": "multi_line_ordinal_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 13621, "record_span": "13621-13622"},
            {"entry_sequence": 2, "pdf_text_line": 13623, "record_span": "13623-13624"},
            {"entry_sequence": 3, "pdf_text_line": 13625, "record_span": "13625-13626"},
            {"entry_sequence": 4, "pdf_text_line": 13627, "record_span": "13627-13628"},
            {"entry_sequence": 5, "pdf_text_line": 13629, "record_span": "13629-13630"},
            {"entry_sequence": 6, "pdf_text_line": 13631, "record_span": "13631-13632"},
            {"entry_sequence": 7, "pdf_text_line": 13633, "record_span": "13633-13634"},
            {"entry_sequence": 8, "pdf_text_line": 13635, "record_span": "13635-13636"},
            {"entry_sequence": 9, "pdf_text_line": 13637, "record_span": "13637-13638"},
            {"entry_sequence": 10, "pdf_text_line": 13639, "record_span": "13639-13640"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二六六○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13642,
        "pdf_text_lines": "13642-13662", "layout_status": "multi_line_ordinal_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": n, "pdf_text_line": line, "record_span": f"{line}-{line+1}"}
            for n, line in enumerate([13643,13645,13647,13649,13651,13653,13655,13657,13659,13661], 1)
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二六七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13664,
        "pdf_text_lines": "13664-13685", "layout_status": "multi_line_ordinal_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": n, "pdf_text_line": line, "record_span": f"{line}-{line+1}"}
            for n, line in enumerate([13666,13668,13670,13672,13674,13676,13678,13680,13682,13684], 1)
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _chou_group("二六九○", 13699, list(range(13701, 13711))),
    _chou_group("二七○○", 13712, list(range(13713, 13723))),
    {
        "collection": "丑", "raw_group_marker": "二七二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13749,
        "pdf_text_lines": "13749-13771", "layout_status": "ten_sequences_present_multiline_alignment_unresolved",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": None, "source_span": "13750-13771"} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二七三○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13773,
        "pdf_text_lines": "13773-13793", "layout_status": "ten_sequences_present_multiline_alignment_unresolved",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": None, "source_span": "13775-13793"} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二七五○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13802,
        "pdf_text_lines": "13802-13811", "layout_status": "first_sequence_missing_in_text_layer",
        "entry_count": 9,
        "entries": [{"entry_sequence": n, "pdf_text_line": line} for n,line in zip(range(2,11),range(13803,13812))],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _chou_group("二七六○", 13813, list(range(13815, 13825))),
    _chou_group("二七七○", 13826, list(range(13827, 13837))),
    _chou_group("二七八○", 13840, list(range(13842, 13852))),
    _chou_group("二七九○", 13853, list(range(13854, 13864))),
    _chou_group("二八○○", 13865, list(range(13867, 13877))),
    _chou_group("二八一○", 13880, list(range(13883, 13893)), "table_rows_text_layer_located"),
    _chou_group("二八二○", 13906, list(range(13909, 13919)), "table_rows_text_layer_located"),
    _chou_group("二八三○", 13920, list(range(13923, 13933))),
    _chou_group("二八四○", 13933, list(range(13935, 13945))),
    _chou_group("二八五○", 13945, list(range(13946, 13956))),
    {
        "collection": "丑", "raw_group_marker": "二八六○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13956,
        "pdf_text_lines": "13956-13980", "layout_status": "sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line, "clause_text_line": clause}
                    for n,line,clause in zip(range(1,11),range(13960,13970),range(13971,13981))],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二八七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 13982,
        "pdf_text_lines": "13982-14003", "layout_status": "sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": None, "source_span": "13983-14003"} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "丑", "raw_group_marker": "二八八○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 14005,
        "pdf_text_lines": "14005-14027", "layout_status": "sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": None, "source_span": "14007-14027"} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _chou_group("二九○", 14044, list(range(14045, 14055)), "raw_short_marker_preserved"),
    _chou_group("二九二", 14055, list(range(14056, 14066)), "raw_short_marker_preserved"),
    _chou_group("二九三○", 14082, list(range(14083, 14093))),
    _chou_group("二九四○", 14094, list(range(14096, 14106))),
    _chou_group("二九六○", 14111, list(range(14112, 14122))),
    _chou_group("二九七○", 14123, list(range(14125, 14135))),
    _chou_group("二九八○", 14136, list(range(14137, 14147))),
    _chou_group("二九九○", 14161, list(range(14162, 14172))),
]

CHOU_GROUP_ANOMALIES = [
    {"raw_group_marker": "二五○", "pdf_text_line": 12772,
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
     "note": "前段12757行已出现同名组号，按不同出现位置独立保存。"},
    {"raw_group_marker": "二三九○", "pdf_text_line": 13159,
     "status": "marker_embedded_in_prior_group_last_entry_boundary_unresolved",
     "candidate_entry_span": "13161-13190",
     "note": "该字样出现在二三八○第十条的文本行中，随后出现十条序号块；是否为二三九○组界待扫描版面确认。"},
    {"raw_group_marker": "二四○○", "pdf_text_line": 13190,
     "status": "marker_embedded_at_prior_block_end_boundary_unresolved",
     "candidate_entry_span": "13192-13223",
     "note": "该字样出现在前一十条序号块末行，随后又出现十条序号块；暂不提升为正式组。"},
    {"raw_group_marker": "二五○○", "pdf_text_line": 13356,
     "status": "marker_seen_body_not_located_before_2510"},
    {"raw_group_marker": "二五六○", "pdf_text_line": 13435,
     "status": "marker_seen_body_not_located_before_2570"},
    {"raw_group_marker": "二六一", "pdf_text_line": 13487,
     "status": "raw_short_marker_preserved_possible_2610_pending_image_check"},
    {"raw_group_marker": "二六○", "pdf_text_line": 13499,
     "occurrence": 2, "status": "raw_short_marker_preserved_possible_2620_pending_image_check"},
    {"raw_group_marker": "二六二", "pdf_text_line": 13511,
     "status": "raw_short_marker_preserved_possible_2620_pending_image_check"},
    {"raw_group_marker": "二七○", "pdf_text_line": 13724,
     "status": "raw_short_marker_preserved_possible_2710_pending_image_check"},
    {"raw_group_marker": "二六四○", "pdf_text_line": 13584,
     "status": "marker_seen_body_layout_unresolved"},
    {"raw_group_marker": "二七四○", "pdf_text_line": 13795,
     "status": "marker_seen_body_not_located_before_2750"},
    {"raw_group_marker": "二八九○", "pdf_text_line": 14029,
     "status": "marker_seen_body_boundary_ambiguous_before_raw_二○○"},
    {"raw_group_marker": "二○○", "pdf_text_line": 14032,
     "status": "raw_marker_preserved_possible_2900_body_marker_pending_image_check"},
    {"raw_group_marker": "二九五○", "pdf_text_line": 14107,
     "status": "marker_seen_body_not_located_before_2960"}
]

def _yin_group(raw_marker, header_line, entry_lines, layout_status="text_layer_rows_located_image_check_pending", occurrence=1):
    return {
        "collection": "寅",
        "raw_group_marker": raw_marker,
        "occurrence": occurrence,
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": header_line,
        "pdf_text_lines": f"{header_line}-{entry_lines[-1]}",
        "layout_status": layout_status,
        "entry_count": len(entry_lines),
        "entries": [{"entry_sequence": sequence, "pdf_text_line": line}
                    for sequence, line in enumerate(entry_lines, 1)],
        "verification_status": "pdf_text_layer_only_image_check_pending",
    }


YIN_GROUP_INDEX = [
    _yin_group("三○一○", 14177, list(range(14178, 14188)),
               "table_has_extra_leading_sequence_10_row_pending_image_check"),
    _yin_group("三○二○", 14190, list(range(14190, 14200)),
               "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三○三○", 14218, list(range(14219, 14229))),
    _yin_group("三○四○", 14230, list(range(14232, 14242))),
    {
        "collection": "寅", "raw_group_marker": "三○六○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 14257,
        "pdf_text_lines": "14257-14272", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 14259, "record_span": "14259-14259"},
            {"entry_sequence": 2, "pdf_text_line": 14260, "record_span": "14260-14260"},
            {"entry_sequence": 3, "pdf_text_line": 14261, "record_span": "14261-14261"},
            {"entry_sequence": 4, "pdf_text_line": 14262, "record_span": "14262-14262"},
            {"entry_sequence": 5, "pdf_text_line": 14263, "record_span": "14263-14263"},
            {"entry_sequence": 6, "pdf_text_line": 14264, "record_span": "14264-14264"},
            {"entry_sequence": 7, "pdf_text_line": 14265, "record_span": "14265-14267"},
            {"entry_sequence": 8, "pdf_text_line": 14268, "record_span": "14268-14268"},
            {"entry_sequence": 9, "pdf_text_line": 14269, "record_span": "14269-14270"},
            {"entry_sequence": 10, "pdf_text_line": 14271, "record_span": "14271-14272"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _yin_group("三○七○", 14274, [14275,14277,14278,14279,14280,14281,14283,14285,14286,14287], "multi_line_age_clause_spans"),
    _yin_group("三○九○", 14293, list(range(14295, 14305))),
    _yin_group("三一○○", 14306, list(range(14307, 14317))),
    _yin_group("三一一○", 14318, list(range(14320, 14330))),
    _yin_group("三一二○", 14343, list(range(14345, 14355))),
    _yin_group("三一三○", 14356, list(range(14357, 14367))),
    _yin_group("三一五○", 14372, list(range(14372, 14382)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三一六○", 14384, list(range(14384, 14394)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三一七○", 14396, list(range(14396, 14406)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三一八○", 14413, list(range(14415, 14425))),
    _yin_group("三一九○", 14426, list(range(14427, 14437))),
    _yin_group("三二○○", 14438, list(range(14440, 14450))),
    _yin_group("三二一○", 14453, list(range(14453, 14463)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三二二○", 14465, list(range(14465, 14475)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三二三○", 14477, list(range(14477, 14487)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("二三四○", 14501, list(range(14503, 14513)), "raw_marker_preserved_in_yin_collection"),
    _yin_group("二三五○", 14514, list(range(14516, 14526)), "raw_marker_preserved_in_yin_collection"),
    _yin_group("三二七○", 14543, list(range(14545, 14555))),
    _yin_group("三二八○", 14556, list(range(14558, 14568))),
    _yin_group("三二九○", 14569, list(range(14572, 14582))),
    _yin_group("三三三○", 14621, list(range(14622, 14632))),
    _yin_group("三三四○", 14633, list(range(14635, 14645))),
    _yin_group("三三六○", 14655, list(range(14657, 14667))),
    _yin_group("三三七○", 14668, list(range(14669, 14679))),
    _yin_group("三三八○", 14680, list(range(14682, 14692))),
    {
        "collection": "寅", "raw_group_marker": "三三九○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 14757,
        "pdf_text_lines": "14757-14808", "layout_status": "age_sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_span": "14759-14797", "clause_text_line": line}
                    for n,line in enumerate(range(14799,14809),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "寅", "raw_group_marker": "三四○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 14810,
        "pdf_text_lines": "14810-14837", "layout_status": "age_sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_span": "14812-14827", "clause_text_line": line}
                    for n,line in enumerate(range(14828,14838),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _yin_group("三四二○", 14847, list(range(14848, 14858))),
    _yin_group("三四三○", 14859, list(range(14861, 14871))),
    _yin_group("三四四○", 14872, list(range(14873, 14883))),
    _yin_group("三四五○", 14899, list(range(14900, 14910))),
    _yin_group("三四六○", 14911, list(range(14913, 14923))),
    _yin_group("三四六○", 14924, list(range(14929, 14939)), "repeated_marker_second_occurrence", occurrence=2),
    _yin_group("三四八○", 14940, list(range(14943, 14953))),
    _yin_group("三四九○", 14954, list(range(14956, 14966))),
    {
        "collection": "寅", "raw_group_marker": "三五○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 14966,
        "pdf_text_lines": "14966-14994", "layout_status": "sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line, "clause_text_line": clause}
                    for n,line,clause in zip(range(1,11),range(14975,14985),range(14985,14995))],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "寅", "raw_group_marker": "三五一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 14996,
        "pdf_text_lines": "14996-15019", "layout_status": "age_sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_span": "14998-15007", "clause_text_line": line}
                    for n,line in enumerate(range(15009,15019),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "寅", "raw_group_marker": "三五二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 15020,
        "pdf_text_lines": "15020-15041", "layout_status": "sequence_age_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "sequence_age_line": seq, "clause_text_line": clause}
                    for n,(seq,clause) in enumerate(zip(range(15022,15032),range(15032,15042)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _yin_group("三五三○", 15043, list(range(15047, 15057))),
    _yin_group("三五四○", 15058, list(range(15059, 15069))),
    _yin_group("三五五○", 15070, list(range(15072, 15082))),
    _yin_group("三五七○", 15087, list(range(15088, 15098))),
    _yin_group("三五八○", 15099, list(range(15101, 15111))),
    _yin_group("三五八○", 15112, list(range(15113, 15123)), "repeated_marker_second_occurrence", occurrence=2),
    _yin_group("三六○○", 15127, list(range(15127, 15137)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三六一○", 15140, list(range(15140, 15150)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三六二○", 15153, [15153,15154,15155,15156,15157,15158,15159,15160,15161],
               "table_missing_sequence_3_nine_rows_only"),
    _yin_group("三六三○", 15180, list(range(15182, 15192))),
    _yin_group("三六四○", 15193, list(range(15194, 15204))),
    _yin_group("三六六○", 15212, list(range(15215, 15225)), "table_rows_text_layer_located"),
    _yin_group("三六七○", 15226, list(range(15229, 15239)), "table_rows_text_layer_located"),
    _yin_group("三六八○", 15240, list(range(15243, 15253)), "table_rows_text_layer_located"),
    _yin_group("三六九○", 15267, list(range(15268, 15278))),
    _yin_group("三七○○", 15279, list(range(15281, 15291))),
    _yin_group("三七二○", 15296, list(range(15296, 15306)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三七三○", 15308, list(range(15308, 15318)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三七四○", 15320, list(range(15320, 15330)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _yin_group("三七五○", 15348, list(range(15349, 15359))),
    _yin_group("三七六○", 15360, list(range(15362, 15372))),
    {
        "collection": "寅", "raw_group_marker": "三七八○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 15380,
        "pdf_text_lines": "15380-15380", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": 15380, "cell_position": n}
                    for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "寅", "raw_group_marker": "三七九○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 15381,
        "pdf_text_lines": "15381-15381", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": 15381, "cell_position": n}
                    for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "寅", "raw_group_marker": "三八○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 15382,
        "pdf_text_lines": "15382-15382", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": 15382, "cell_position": n}
                    for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "寅", "raw_group_marker": "三八一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 15397,
        "pdf_text_lines": "15397-15419", "layout_status": "age_sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_span": "15399-15409", "clause_text_line": line}
                    for n,line in enumerate(range(15410,15420),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _yin_group("三八二○", 15421, list(range(15422, 15432))),
    _yin_group("三八四○", 15437, [15438,15440,15441,15442,15443,15445,15446,15447,15448,15449], "multi_line_age_clause_spans"),
    _yin_group("三八五○", 15451, [15452,15454,15455,15456,15458,15459,15461,15462,15464,15466], "multi_line_age_clause_spans"),
    _yin_group("三八六○", 15469, [15470,15471,15472,15474,15476,15478,15480,15482,15484,15485], "multi_line_age_clause_spans"),
]

YIN_GROUP_ANOMALIES = [
    {"raw_group_marker": "三○一○", "pdf_text_line": 14177,
     "status": "leading_sequence_10_row_before_sequence_1_to_10_table",
     "note": "组标题所在首行序号为十，后续又出现一至十；首行暂不并入十条正式序号。"},
    {"raw_group_marker": "三○五○", "pdf_text_line": 14243,
     "status": "group_marker_not_seen_possible_unheaded_group_before_3060"},
    {"raw_group_marker": "三○八○", "pdf_text_line": 14289,
     "status": "marker_seen_body_not_located_before_3090"},
    {"raw_group_marker": "三一四○", "pdf_text_line": 14368,
     "status": "marker_seen_body_not_located_before_3150"},
    {"raw_group_marker": "三二六○", "pdf_text_line": 14527,
     "status": "marker_seen_body_boundary_ambiguous_before_special_section_shiji"},
    {"raw_group_marker": "三三五○", "pdf_text_line": 14646,
     "status": "marker_seen_body_not_located_before_3360"},
    {"raw_group_marker": "三四一○", "pdf_text_line": 14839,
     "status": "marker_seen_body_not_located_before_3420"},
    {"raw_group_marker": "三四七○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_3460_and_3480"},
    {"raw_group_marker": "三五六○", "pdf_text_line": None,
     "status": "expected_group_marker_not_seen_before_bin_collection_subsection"},
    {"raw_group_marker": "三五九○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_3580_and_3600"},
    {"raw_group_marker": "三六五○", "pdf_text_line": 15205,
     "status": "marker_seen_body_not_located_before_3660"},
    {"raw_group_marker": "三七一○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_3700_and_3720"},
    {"raw_group_marker": "三七七○", "pdf_text_line": 15373,
     "status": "marker_seen_body_not_located_before_3780"},
    {"raw_group_marker": "三八三○", "pdf_text_line": 15433,
     "status": "marker_seen_body_not_located_before_3840"}
]

YIN_UNASSIGNED_BLOCKS = [
    {"block_id": "yin_special_section_shiji_before_3030",
     "pdf_text_lines": "14205-14216", "entry_count_candidate": 10,
     "status": "separate_section_heading_shiji_not_assigned_to_numbered_group"},
    {"block_id": "yin_possible_3050_group_body",
     "pdf_text_lines": "14245-14255", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "yin_unheaded_entries_before_3120",
     "pdf_text_lines": "14331-14341", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "yin_unheaded_entries_before_2340",
     "pdf_text_lines": "14490-14499", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "yin_special_section_shiji_after_3260",
     "pdf_text_lines": "14530-14541", "entry_count_candidate": 10,
     "status": "separate_section_heading_shiji_not_assigned_to_numbered_group"},
    {"block_id": "yin_unheaded_entries_before_3330_a",
     "pdf_text_lines": "14583-14592", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "yin_unheaded_entries_before_3330_b",
     "pdf_text_lines": "14593-14602", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "yin_unheaded_entries_before_3330_c",
     "pdf_text_lines": "14610-14619", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "yin_special_section_shiji_before_3390",
     "pdf_text_lines": "14696-14755", "entry_count_candidate": 10,
     "status": "separate_section_heading_shiji_with_age_table_not_assigned_to_numbered_group"},
    {"block_id": "yin_special_section_shenji",
     "pdf_text_lines": "15167-15179", "entry_count_candidate": 10,
     "status": "separate_section_heading_shenji_not_assigned_to_numbered_group"},
    {"block_id": "yin_special_section_shiji_after_3680",
     "pdf_text_lines": "15254-15265", "entry_count_candidate": 10,
     "status": "separate_section_heading_shiji_not_assigned_to_numbered_group"},
    {"block_id": "yin_special_section_shiji_after_3740",
     "pdf_text_lines": "15335-15346", "entry_count_candidate": 10,
     "status": "separate_section_heading_shiji_not_assigned_to_numbered_group"},
    {"block_id": "yin_special_section_shiji_after_3860",
     "pdf_text_lines": "15487-15500", "entry_count_candidate": 20,
     "status": "separate_section_heading_shiji_with_groups_3870_3880_not_assigned_to_yin_index"}
]


def _mao_group(raw_marker, header_line, entry_lines, layout_status="text_layer_rows_located_image_check_pending", occurrence=1):
    return {
        "collection": "卯",
        "raw_group_marker": raw_marker,
        "occurrence": occurrence,
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": header_line,
        "pdf_text_lines": f"{header_line}-{entry_lines[-1]}",
        "layout_status": layout_status,
        "entry_count": len(entry_lines),
        "entries": [{"entry_sequence": sequence, "pdf_text_line": line}
                    for sequence, line in enumerate(entry_lines, 1)],
        "verification_status": "pdf_text_layer_only_image_check_pending",
    }


MAO_GROUP_INDEX = [
    _mao_group("四○八○", 15791, list(range(15798, 15808)), "first_sequence_label_missing_after_branch_title"),
    _mao_group("四○九○", 15809, list(range(15811, 15821))),
    _mao_group("四一○○", 15822, list(range(15823, 15833))),
    _mao_group("四一二○", 15836, list(range(15837, 15847))),
    _mao_group("四一三○", 15858, list(range(15859, 15869))),
    _mao_group("四一五○", 15884, list(range(15886, 15896))),
    _mao_group("四一六○", 15897, list(range(15898, 15908))),
    _mao_group("四一八○", 15924, list(range(15925, 15935))),
    _mao_group("四一九○", 15936, list(range(15938, 15948))),
    _mao_group("四二○○", 15949, list(range(15952, 15962))),
    _mao_group("四二一○", 15963, list(range(15965, 15975))),
    _mao_group("四二二○", 15976, list(range(15977, 15987))),
    _mao_group("四二四○", 15992, list(range(15992, 16002)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _mao_group("四二五○", 16004, list(range(16004, 16014)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _mao_group("四二六○", 16016, list(range(16016, 16026)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _mao_group("四二七○", 16046, [16048,16049,16050,16051,16052,16054,16055,16056,16057,16058], "multi_line_age_clause_spans"),
    _mao_group("四二八○", 16060, [16061,16065,16066,16067,16068,16069,16070,16071,16073], "sequence_10_missing_text_layer_nine_rows_only"),
    _mao_group("四二九○", 16075, list(range(16079, 16089))),
    _mao_group("四三○○", 16090, list(range(16091, 16101))),
    _mao_group("四三一○", 16102, list(range(16104, 16114))),
    _mao_group("四三三○", 16120, list(range(16121, 16131))),
    _mao_group("四三四○", 16132, list(range(16133, 16143))),
    _mao_group("四三五○", 16143, list(range(16144, 16154))),
    _mao_group("四三六○", 16157, list(range(16157, 16167)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _mao_group("四三七○", 16167, list(range(16167, 16177)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _mao_group("四三二○", 16177, list(range(16177, 16187)), "repeated_marker_late_occurrence_table_title_row_is_entry_1", occurrence=2),
    _mao_group("四三九○", 16194, list(range(16198, 16208)), "table_rows_text_layer_located"),
    _mao_group("四四○○", 16209, list(range(16212, 16222)), "table_rows_text_layer_located"),
    _mao_group("四四一○", 16223, list(range(16226, 16236)), "table_rows_text_layer_located"),
    _mao_group("四四二○", 16252, list(range(16253, 16263))),
    _mao_group("四四三○", 16264, list(range(16266, 16276))),
    _mao_group("四四四○", 16277, list(range(16281, 16291)), "extra_leading_sequence_row_16280_not_counted"),
    _mao_group("四四六○", 16292, list(range(16293, 16303))),
    _mao_group("四四七○", 16303, list(range(16304, 16314)), "table_rows_text_layer_located"),
    _mao_group("四四八○", 16317, list(range(16319, 16329)), "raw_marker_preserved_possible_short_form"),
    _mao_group("四四九○", 16330, list(range(16331, 16341))),
    _mao_group("四四九○", 16342, list(range(16344, 16354)), "repeated_marker_second_occurrence", occurrence=2),
    _mao_group("四五一○", 16359, list(range(16362, 16372)), "table_rows_text_layer_located"),
    _mao_group("四五二○", 16385, list(range(16388, 16398)), "table_rows_text_layer_located"),
    _mao_group("四五四○", 16407, list(range(16409, 16419)), "table_rows_text_layer_located"),
    _mao_group("四五七○", 16451, list(range(16453, 16463))),
    _mao_group("四五八○", 16464, list(range(16465, 16475))),
    _mao_group("四五九○", 16476, list(range(16478, 16488))),
    _mao_group("四六○", 16496, list(range(16498, 16508)), "raw_short_marker_preserved"),
    _mao_group("四六一", 16509, list(range(16510, 16520)), "raw_short_marker_preserved"),
    _mao_group("四六二", 16521, list(range(16523, 16533)), "raw_short_marker_preserved"),
    _mao_group("四六三○", 16539, list(range(16539, 16549)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _mao_group("四六四○", 16551, list(range(16551, 16561)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _mao_group("四六四○", 16563, list(range(16563, 16573)), "repeated_marker_second_occurrence_table_title_row_is_entry_1", occurrence=2),
    _mao_group("四六六", 16580, list(range(16580, 16590)), "raw_short_marker_preserved_table_title_row_is_entry_1"),
    _mao_group("四六七", 16592, list(range(16592, 16602)), "raw_short_marker_preserved_table_title_row_is_entry_1"),
    _mao_group("四六八", 16604, list(range(16604, 16614)), "raw_short_marker_preserved_table_title_row_is_entry_1"),
    _mao_group("四六九○", 16632, list(range(16634, 16644)), "multi_line_age_clause_spans"),
    _mao_group("四七○○", 16646, list(range(16647, 16657))),
    _mao_group("四七二○", 16664, list(range(16666, 16676)), "table_rows_text_layer_located"),
    _mao_group("四七三○", 16677, list(range(16679, 16689)), "table_rows_text_layer_located"),
    _mao_group("四七三○", 16690, list(range(16692, 16702)), "repeated_marker_second_occurrence_table_rows", occurrence=2),
    _mao_group("四七五○", 16720, list(range(16722, 16732))),
    _mao_group("四七六○", 16733, list(range(16734, 16744))),
    _mao_group("四七八○", 16760, list(range(16761, 16771))),
    _mao_group("四七九○", 16772, list(range(16774, 16784))),
    _mao_group("四八一○", 16799, list(range(16801, 16811))),
    _mao_group("四八二○", 16812, list(range(16813, 16823))),
    _mao_group("四八三○", 16824, list(range(16828, 16838))),
    _mao_group("四八四○", 16839, list(range(16840, 16850))),
    _mao_group("四八五○", 16851, list(range(16853, 16863))),
    _mao_group("四八六○", 16864, list(range(16871, 16881))),
    _mao_group("四八七○", 16882, list(range(16884, 16894))),
    _mao_group("四八八○", 16895, list(range(16897, 16907))),
    {
        "collection": "卯", "raw_group_marker": "四九○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 16926,
        "pdf_text_lines": "16926-16947", "layout_status": "age_sequence_and_clause_columns_separated",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(16928,16938),range(16938,16948)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "卯", "raw_group_marker": "四九一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 16949,
        "pdf_text_lines": "16949-16982", "layout_status": "multi_row_age_table_and_clause_column",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "clause_text_line": line, "age_data_span": "16951-16972"}
                    for n,line in enumerate(range(16973,16983),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _mao_group("四九三○", 16995, list(range(16998, 17008)), "table_rows_text_layer_located"),
    _mao_group("四九四○", 17021, list(range(17024, 17034)), "table_rows_text_layer_located"),
    _mao_group("四九五○", 17035, list(range(17042, 17052)), "multi_line_body_after_section_header"),
    _mao_group("四九六○", 17053, list(range(17054, 17064))),
    _mao_group("四九七○", 17065, list(range(17067, 17077))),
    _mao_group("四九八○", 17078, list(range(17081, 17091))),
    _mao_group("四九九○", 17092, list(range(17094, 17104))),
]

MAO_GROUP_ANOMALIES = [
    {"raw_group_marker": "四一一○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_before_unheaded_ten_entry_block"},
    {"raw_group_marker": "四一四○", "pdf_text_line": 15872,
     "status": "branch_header_seen_body_without_group_marker"},
    {"raw_group_marker": "四一七○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_before_4180"},
    {"raw_group_marker": "四二三○", "pdf_text_line": 15988,
     "status": "marker_seen_body_not_located_before_4240"},
    {"raw_group_marker": "四三二○", "pdf_text_line": 16115,
     "status": "marker_seen_body_not_located_before_4330"},
    {"raw_group_marker": "四三八○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_4370_and_4390"},
    {"raw_group_marker": "四四五○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_4440_and_4460"},
    {"raw_group_marker": "四四八○", "pdf_text_line": 16317,
     "status": "raw_marker_possible_4480_text_layer_short_form"},
    {"raw_group_marker": "四五○○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_4490_and_4510"},
    {"raw_group_marker": "四五三○", "pdf_text_line": 16399,
     "status": "marker_seen_body_not_located_before_4540"},
    {"raw_group_marker": "四五五○", "pdf_text_line": 16420,
     "status": "raw_short_marker_with_two_following_table_blocks_boundary_unresolved"},
    {"raw_group_marker": "四五六○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_4550_and_4570"},
    {"raw_group_marker": "四六五○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_4640_and_4660"},
    {"raw_group_marker": "四七一○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_4700_and_4720"},
    {"raw_group_marker": "四七四○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_before_4750"},
    {"raw_group_marker": "四八○○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_after_internal_guaji_subsection"},
    {"raw_group_marker": "四九二○", "pdf_text_line": 16984,
     "status": "marker_seen_body_not_located_before_4930"},
    {"raw_group_marker": "五○○○", "pdf_text_line": 17105,
     "status": "marker_seen_body_not_located_before_chen_collection_boundary"}
]

MAO_UNASSIGNED_BLOCKS = [
    {"block_id": "mao_possible_4110_group_body",
     "pdf_text_lines": "15847-15856", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_possible_4140_group_body",
     "pdf_text_lines": "15873-15882", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_possible_4170_group_body",
     "pdf_text_lines": "15913-15922", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_bp_collection_subsection",
     "pdf_text_lines": "16192-16193", "entry_count_candidate": 0,
     "status": "internal_section_heading_not_branch_boundary"},
    {"block_id": "mao_unheaded_table_after_4510",
     "pdf_text_lines": "16374-16383", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_possible_4550_table_a",
     "pdf_text_lines": "16422-16432", "entry_count_candidate": 10,
     "status": "group_boundary_ambiguous_do_not_promote"},
    {"block_id": "mao_possible_4560_table_b",
     "pdf_text_lines": "16434-16444", "entry_count_candidate": 10,
     "status": "group_boundary_ambiguous_do_not_promote"},
    {"block_id": "mao_unheaded_entries_before_4690",
     "pdf_text_lines": "16621-16630", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_unheaded_entries_before_4750",
     "pdf_text_lines": "16709-16718", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_unheaded_entries_before_4780",
     "pdf_text_lines": "16749-16758", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_unheaded_entries_after_guaji",
     "pdf_text_lines": "16788-16797", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "mao_possible_4890_group_body",
     "pdf_text_lines": "16915-16924", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"}
]


def _chen_group(raw_marker, header_line, entry_lines, layout_status="text_layer_rows_located_image_check_pending", sequence_start=1, occurrence=1):
    return {
        "collection": "辰",
        "raw_group_marker": raw_marker,
        "occurrence": 1,
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": header_line,
        "pdf_text_lines": f"{header_line}-{entry_lines[-1]}",
        "layout_status": layout_status,
        "entry_count": len(entry_lines),
        "entries": [{"entry_sequence": sequence, "pdf_text_line": line}
                    for sequence, line in enumerate(entry_lines, sequence_start)],
        "verification_status": "pdf_text_layer_only_image_check_pending",
    }


CHEN_GROUP_INDEX = [
    _chen_group("五○一○", 17112, [17112,17118,17124,17130,17136,17142,17148,17154,17160], "sequence_1_missing_nine_rows_only", sequence_start=2),
    _chen_group("五○二○", 17168, [17168,17174,17180,17186,17192,17198,17204,17210,17216,17222], "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五○三○", 17244, list(range(17246,17256))),
    _chen_group("五○四○", 17257, list(range(17258,17268))),
    _chen_group("五○六○", 17273, list(range(17275,17285)), "table_rows_text_layer_located"),
    _chen_group("五○七○", 17298, list(range(17300,17310)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五○八○", 17311, list(range(17318,17328)), "title_followed_by_branch_header_then_ten_entries"),
    _chen_group("五○九○", 17329, list(range(17331,17341))),
    _chen_group("五一○○", 17342, list(range(17343,17353))),
    {
        "collection": "辰", "raw_group_marker": "五一二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 17358,
        "pdf_text_lines": "17356-17367", "layout_status": "sequence_1_precedes_table_group_header",
        "entry_count": 10,
        "entries": [{"entry_sequence": 1, "pdf_text_line": 17356}] +
                   [{"entry_sequence": n, "pdf_text_line": line} for n,line in enumerate(range(17358,17367),2)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _chen_group("五一三○", 17369, list(range(17369,17379)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五一四○", 17381, list(range(17381,17391)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五一五○", 17411, list(range(17413,17423)), "multi_line_age_clause_spans"),
    _chen_group("五一六○", 17425, list(range(17426,17436))),
    _chen_group("五一七○", 17436, list(range(17442,17452)), "header_then_page_break_before_ten_entries"),
    _chen_group("五一八○", 17453, list(range(17454,17464))),
    _chen_group("五一九○", 17465, list(range(17467,17477))),
    _chen_group("五二一○", 17483, list(range(17484,17494)), "table_rows_text_layer_located"),
    _chen_group("五二二○", 17496, list(range(17496,17506)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五二三○", 17508, list(range(17508,17518)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五二四○", 17535, list(range(17537,17547)), "sequence_1_missing_sequence_10_repeated"),
    _chen_group("五二五○", 17548, list(range(17549,17559))),
    _chen_group("五二七○", 17564, list(range(17564,17574)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五二八○", 17576, list(range(17576,17586)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五二九○", 17588, list(range(17588,17598)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五三○○", 17616, list(range(17617,17627))),
    _chen_group("五三一○", 17628, list(range(17630,17640))),
    _chen_group("五三三○", 17653, list(range(17655,17665))),
    _chen_group("五三四○", 17666, list(range(17667,17677))),
    _chen_group("五三五○", 17678, list(range(17682,17692))),
    _chen_group("五三六○", 17693, list(range(17694,17704))),
    _chen_group("五三七○", 17705, list(range(17707,17717))),
    _chen_group("五三八○", 17718, list(range(17734,17744)), "sequence_age_table_rows_after_sequence_key"),
    _chen_group("五三九○", 17745, list(range(17759,17769)), "sequence_age_table_rows_after_sequence_key"),
    _chen_group("五四○○", 17770, list(range(17784,17794)), "sequence_age_table_rows_after_sequence_key"),
    _chen_group("五四一○", 17795, list(range(17799,17809)), "first_occurrence_before_repeated_marker"),
    _chen_group("五四一○", 17810, list(range(17811,17821)), "repeated_marker_second_occurrence", occurrence=2),
    _chen_group("五四三○", 17822, list(range(17824,17834))),
    _chen_group("五四四○", 17837, list(range(17840,17850))),
    _chen_group("五四五○", 17851, list(range(17853,17863))),
    _chen_group("五四六○", 17864, list(range(17865,17875))),
    _chen_group("五四七○", 17876, list(range(17884,17894)), "page_header_age_line_before_ten_entries"),
    _chen_group("五四八○", 17895, list(range(17896,17906))),
    _chen_group("五四九○", 17906, list(range(17907,17917))),
    _chen_group("五五一○", 17926, list(range(17926,17936)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五五二○", 17938, list(range(17938,17948)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五五三○", 17950, list(range(17950,17960)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五五四○", 17963, list(range(17964,17974))),
    _chen_group("五五五○", 17975, list(range(17976,17986))),
    _chen_group("五五六○", 17986, list(range(17987,17997))),
    _chen_group("五五七○", 18011, list(range(18012,18022))),
    _chen_group("五五八○", 18023, list(range(18025,18035))),
    _chen_group("五六○○", 18045, list(range(18045,18055)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五六一○", 18059, list(range(18059,18069)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五六二○", 18073, list(range(18073,18083)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五六三○", 18090, list(range(18090,18100)), "sequence_10_precedes_sequences_1_to_9"),
    _chen_group("五六四○", 18102, list(range(18102,18112)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五六五○", 18114, list(range(18114,18124)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五六六○", 18130, list(range(18131,18141)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五六七○", 18143, list(range(18143,18153)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _chen_group("五六九○", 18187, list(range(18189,18199))),
    {
        "collection": "辰", "raw_group_marker": "五七○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 18201,
        "pdf_text_lines": "18201-18213", "layout_status": "duplicate_sequence_labels_split_across_rows",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 18202},
            {"entry_sequence": 2, "pdf_text_line": 18203},
            {"entry_sequence": 3, "pdf_text_line": 18204, "record_span": "18204-18205"},
            {"entry_sequence": 4, "pdf_text_line": 18206, "record_span": "18206-18207"},
            {"entry_sequence": 5, "pdf_text_line": 18208},
            {"entry_sequence": 6, "pdf_text_line": 18209},
            {"entry_sequence": 7, "pdf_text_line": 18210},
            {"entry_sequence": 8, "pdf_text_line": 18211},
            {"entry_sequence": 9, "pdf_text_line": 18212},
            {"entry_sequence": 10, "pdf_text_line": 18213}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _chen_group("五七二○", 18219, list(range(18221,18231))),
    _chen_group("五七三○", 18232, list(range(18233,18243))),
    _chen_group("五七四○", 18244, list(range(18246,18256))),
    _chen_group("五七五○", 18271, list(range(18273,18283))),
    _chen_group("五七六○", 18284, list(range(18285,18295))),
    {
        "collection": "辰", "raw_group_marker": "五七七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 18296,
        "pdf_text_lines": "18296-18338", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 18300, "record_span": "18300-18306"},
            {"entry_sequence": 2, "pdf_text_line": 18308, "record_span": "18308-18310"},
            {"entry_sequence": 3, "pdf_text_line": 18312, "record_span": "18312-18313"},
            {"entry_sequence": 4, "pdf_text_line": 18315, "record_span": "18315-18317"},
            {"entry_sequence": 5, "pdf_text_line": 18319, "record_span": "18319-18321"},
            {"entry_sequence": 6, "pdf_text_line": 18323, "record_span": "18323-18325"},
            {"entry_sequence": 7, "pdf_text_line": 18327, "record_span": "18327-18329"},
            {"entry_sequence": 8, "pdf_text_line": 18331, "record_span": "18331-18332"},
            {"entry_sequence": 9, "pdf_text_line": 18334, "record_span": "18334-18335"},
            {"entry_sequence": 10, "pdf_text_line": 18337, "record_span": "18337-18338"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _chen_group("五七八○", 18340, [18342,18346,18350,18354,18358,18362,18366,18370,18374,18378], "sequences_2_to_11_only", sequence_start=2),
    _chen_group("五七九○", 18381, [18383,18387,18391,18395,18399,18403,18407,18411,18415,18419], "sequences_2_to_11_only", sequence_start=2),
    _chen_group("五八○○", 18423, list(range(18426,18436))),
    _chen_group("五八一○", 18437, list(range(18439,18448)), "sequence_1_missing_nine_rows_only", sequence_start=2),
    _chen_group("五八二○", 18449, list(range(18450,18459)), "sequence_1_missing_extra_unlabeled_line_after_sequence_10", sequence_start=2),
    _chen_group("五八三○", 18461, list(range(18467,18477)), "table_rows_text_layer_located"),
    _chen_group("五八四○", 18479, list(range(18481,18491)), "table_rows_text_layer_located"),
    _chen_group("五八五○", 18492, list(range(18494,18504)), "table_rows_text_layer_located"),
    _chen_group("五八七○", 18518, list(range(18520,18530))),
    _chen_group("五八八○", 18531, list(range(18532,18542))),
    _chen_group("五八九○", 18543, list(range(18547,18557)), "header_then_page_break_before_ten_entries"),
    _chen_group("五九○○", 18558, list(range(18559,18569))),
    _chen_group("五九一○", 18570, list(range(18576,18586)), "header_then_page_break_before_ten_entries"),
    _chen_group("五九三○", 18591, list(range(18594,18604)), "table_rows_text_layer_located"),
    _chen_group("五九四○", 18605, list(range(18608,18618)), "table_rows_text_layer_located"),
    _chen_group("五九五○", 18619, list(range(18622,18632)), "table_rows_text_layer_located"),
    _chen_group("五九六○", 18638, list(range(18640,18650)), "first_ten_entry_block_only"),
    _chen_group("五九七○", 18661, list(range(18663,18673))),
    _chen_group("五九八○", 18674, list(range(18681,18691)), "section_marker_between_header_and_entries"),
    _chen_group("五九九○", 18691, list(range(18693,18703))),
]

CHEN_GROUP_ANOMALIES = [
    {"raw_group_marker": "五○五○", "pdf_text_line": 17269,
     "status": "marker_seen_body_not_located_before_5060"},
    {"raw_group_marker": "五一一○", "pdf_text_line": None,
     "status": "no_independent_marker_sequence_1_line_precedes_5120"},
    {"raw_group_marker": "五二○○", "pdf_text_line": 17478,
     "status": "marker_seen_body_not_located_before_5210"},
    {"raw_group_marker": "五二六○", "pdf_text_line": 17560,
     "status": "marker_seen_body_not_located_before_5270"},
    {"raw_group_marker": "五三二○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_before_unheaded_ten_entry_block"},
    {"raw_group_marker": "五四二○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_between_repeated_5410_and_5430"},
    {"raw_group_marker": "五五○○", "pdf_text_line": 17922,
     "status": "marker_seen_body_not_located_before_5510"},
    {"raw_group_marker": "五五九○", "pdf_text_line": 18036,
     "status": "marker_seen_body_not_located_before_5600"},
    {"raw_group_marker": "五六八○", "pdf_text_line": None,
     "status": "expected_group_marker_missing_before_unheaded_body_5690"},
    {"raw_group_marker": "五七一○", "pdf_text_line": 18215,
     "status": "marker_seen_body_not_located_before_5720"},
    {"raw_group_marker": "五八六○", "pdf_text_line": None,
     "status": "expected_marker_not_seen_before_unheaded_block"},
    {"raw_group_marker": "五九二○", "pdf_text_line": 18587,
     "status": "marker_seen_body_not_located_before_5930"}
]

CHEN_UNASSIGNED_BLOCKS = [
    {"block_id": "chen_unheaded_entries_before_5030",
     "pdf_text_lines": "17233-17242", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chen_unheaded_ten_entries_after_5230",
     "pdf_text_lines": "17524-17534", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chen_unheaded_ten_entries_before_5330",
     "pdf_text_lines": "17641-17651", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chen_possible_5680_body",
     "pdf_text_lines": "18175-18185", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chen_unheaded_entries_after_internal_tiesuanpan",
     "pdf_text_lines": "18260-18269", "entry_count_candidate": 10,
     "status": "internal_subsection_block_not_assigned_to_numbered_group"},
    {"block_id": "chen_possible_5860_body",
     "pdf_text_lines": "18507-18516", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chen_second_5960_like_block",
     "pdf_text_lines": "18650-18659", "entry_count_candidate": 10,
     "status": "repeated_sequence_block_without_group_marker_do_not_assign"}
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
     "note": "位于二三二○表格之后、二三三○标题之前，保留为独立无组号块。"},
    {"block_id": "chou_possible_2390_group_body",
     "pdf_text_lines": "13161-13190", "entry_count_candidate": 10,
     "status": "group_boundary_ambiguous_do_not_promote",
     "note": "前一行13159出现二三九○字样，未见独立标题。"},
    {"block_id": "chou_possible_2400_group_body",
     "pdf_text_lines": "13192-13223", "entry_count_candidate": 10,
     "status": "group_boundary_ambiguous_do_not_promote",
     "note": "前一行13190出现二四○○字样，未见独立标题。"},
    {"block_id": "chou_unheaded_entries_before_2480",
     "pdf_text_lines": "13318-13329", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign",
     "note": "位于二四七○表格之后、二四八○标题之前，保留为独立无组号块。"},
    {"block_id": "chou_possible_2680_group_body",
     "pdf_text_lines": "13687-13697", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign",
     "note": "位于二六七○之后、二六九○之前，未见独立组号。"},
    {"block_id": "chou_possible_2710_group_body",
     "pdf_text_lines": "13726-13747", "entry_count_candidate": 10,
     "status": "group_boundary_ambiguous_do_not_promote",
     "note": "前置原始标题为二七○，十条正文无独立二七一○标题。"},
    {"block_id": "chou_possible_2890_group_body",
     "pdf_text_lines": "14032-14042", "entry_count_candidate": 10,
     "status": "group_boundary_ambiguous_do_not_promote",
     "note": "二八九○标题之后出现原始短标记二○○，其后有十条内容，组界待图像核验。"},
    {"block_id": "chou_unheaded_entries_after_292",
     "pdf_text_lines": "14071-14080", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chou_unheaded_entries_before_2990",
     "pdf_text_lines": "14150-14159", "entry_count_candidate": 10,
     "status": "group_marker_missing_do_not_assign"},
    {"block_id": "chen_unheaded_ten_entries_before_5330", "pdf_text_lines": "17641-17651", "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"}
]


def _si_group(raw_marker, header_line, entry_lines, layout_status="text_layer_rows_located_image_check_pending"):
    return {
        "collection": "巳", "raw_group_marker": raw_marker, "occurrence": 1,
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": header_line,
        "pdf_text_lines": f"{header_line}-{entry_lines[-1]}",
        "layout_status": layout_status, "entry_count": len(entry_lines),
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate(entry_lines,1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    }


SI_GROUP_INDEX = [
    _si_group("六○一○", 18719, list(range(18721,18731)), "heading_then_ten_entries"),
    _si_group("六○二○", 18760, list(range(18766,18776)), "heading_then_page_header_then_ten_entries"),
    _si_group("六○三○", 18777, list(range(18778,18788)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六○四○", 18789, list(range(18791,18801))),
    _si_group("六○五○", 18802, list(range(18809,18819)), "heading_then_page_header_before_ten_entries"),
    _si_group("六○六○", 18820, list(range(18821,18831))),
    _si_group("六○七○", 18832, list(range(18834,18844))),
    _si_group("六○八○", 18845, list(range(18865,18875)), "sequence_key_rows_then_clause_rows"),
    _si_group("六○九○", 18876, list(range(18889,18899)), "sequence_key_rows_then_clause_rows"),
    _si_group("六一○○", 18900, list(range(18912,18922)), "sequence_key_rows_then_clause_rows"),
    _si_group("六一一○", 18923, list(range(18930,18940)), "page_header_before_ten_entries"),
    _si_group("六一二○", 18941, list(range(18943,18953))),
    _si_group("六一三○", 18954, list(range(18955,18965))),
    _si_group("六一五○", 18973, list(range(18973,18983)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六一六○", 18985, list(range(18985,18995)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六一七○", 18997, list(range(18997,19007)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六一八○", 19021, list(range(19023,19033))),
    _si_group("六一九○", 19034, list(range(19035,19045))),
    {
        "collection": "巳", "raw_group_marker": "六二○", "occurrence": 1,
        "normalized_group_marker_candidate": "六二一○",
        "group_header_pdf_line": 19054, "pdf_text_lines": "19054-19064",
        "layout_status": "short_raw_marker_candidate_6210_followed_by_separate_age_block",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate(range(19055,19065),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _si_group("六二二○", 19076, list(range(19077,19087))),
    _si_group("六二三○", 19099, list(range(19100,19110))),
    _si_group("六二四○", 19140, list(range(19142,19152)), "table_rows_text_layer_located"),
    _si_group("六二五○", 19154, list(range(19156,19166)), "table_rows_text_layer_located"),
    _si_group("六二六○", 19167, list(range(19174,19184)), "section_header_then_ten_entries"),
    _si_group("六二七○", 19184, list(range(19186,19196))),
    _si_group("六二八○", 19196, list(range(19197,19207))),
    _si_group("六二九○", 19207, list(range(19213,19223)), "page_header_before_ten_entries"),
    _si_group("六三○○", 19224, list(range(19225,19235))),
    _si_group("六三一○", 19236, list(range(19238,19248))),
    _si_group("六三三○", 19265, list(range(19267,19277)), "page_header_before_ten_entries"),
    _si_group("六三四○", 19278, list(range(19279,19289))),
    _si_group("六三五○", 19290, list(range(19294,19304)), "page_header_before_ten_entries"),
    _si_group("六三六○", 19305, list(range(19306,19316))),
    _si_group("六三七○", 19317, list(range(19319,19329))),
    {
        "collection": "巳", "raw_group_marker": "六三九○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 19344,
        "pdf_text_lines": "19344-19366", "layout_status": "age_rows_then_clause_rows",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(19346,19356),range(19357,19367)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "巳", "raw_group_marker": "六四○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 19368,
        "pdf_text_lines": "19368-19392", "layout_status": "age_rows_then_clause_rows",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(19370,19380),range(19382,19392)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _si_group("六四二○", 19393, list(range(19395,19405))),
    _si_group("六四三○", 19406, list(range(19407,19417))),
    _si_group("六四五○", 19428, list(range(19430,19440)), "page_header_before_ten_entries"),
    {
        "collection": "巳", "raw_group_marker": "六四六○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 19441,
        "pdf_text_lines": "19441-19462", "layout_status": "age_rows_then_clause_rows",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(19442,19452),range(19452,19462)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "巳", "raw_group_marker": "六四六五○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 19463,
        "pdf_text_lines": "19463-19484", "layout_status": "non_ten_increment_group_marker_age_rows_then_clause_rows",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(19465,19475),range(19475,19485)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _si_group("六四六七○", 19485, [19493,19494,19495,19497,19498,19499,19500,19501,19502,19503], "entry_3_spans_two_age_lines"),
    _si_group("六四八○", 19505, list(range(19506,19516))),
    _si_group("六四九○", 19517, list(range(19519,19529))),
    _si_group("六五一○", 19536, list(range(19536,19546)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六五三○", 19559, list(range(19560,19570)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六五四○", 19586, list(range(19588,19598))),
    _si_group("六五五○", 19599, list(range(19600,19610))),
    _si_group("六五六○", 19613, list(range(19618,19628)), "page_header_and_age_marker_before_ten_entries"),
    _si_group("六六○○", 19696, list(range(19698,19708))),
    _si_group("六六一○", 19709, list(range(19711,19721))),
    _si_group("六六二○", 19722, list(range(19725,19735)), "page_header_before_ten_entries"),
    _si_group("六六三○", 19736, list(range(19738,19748))),
    _si_group("六六四○", 19749, list(range(19750,19760))),
    _si_group("六六五○", 19761, list(range(19767,19777)), "page_header_before_ten_entries"),
    {
        "collection": "巳", "raw_group_marker": "六六六○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 19778,
        "pdf_text_lines": "19778-19799", "layout_status": "age_rows_then_clause_rows",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(19780,19790),range(19790,19800)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "巳", "raw_group_marker": "六六七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 19801,
        "pdf_text_lines": "19801-19824", "layout_status": "age_rows_then_clause_rows",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(19803,19813),range(19814,19824)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _si_group("六六八○", 19825, [19837,19838,19839,19840,19841,19842,19843,19844,19846,19847], "entry_8_spans_two_age_lines"),
    _si_group("六六九○", 19849, list(range(19851,19861))),
    {
        "collection": "巳", "raw_group_marker": "六七一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 19866,
        "pdf_text_lines": "19866-19884", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 19867},
            {"entry_sequence": 2, "pdf_text_line": 19868},
            {"entry_sequence": 3, "pdf_text_line": 19869, "record_span": "19869-19871"},
            {"entry_sequence": 4, "pdf_text_line": 19872, "record_span": "19872-19873"},
            {"entry_sequence": 5, "pdf_text_line": 19874, "record_span": "19874-19876"},
            {"entry_sequence": 6, "pdf_text_line": 19877, "record_span": "19877-19879"},
            {"entry_sequence": 7, "pdf_text_line": 19880},
            {"entry_sequence": 8, "pdf_text_line": 19881},
            {"entry_sequence": 9, "pdf_text_line": 19882},
            {"entry_sequence": 10, "pdf_text_line": 19883}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _si_group("六七二○", 19887, list(range(19887,19897)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六七三○", 19899, list(range(19899,19909)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六七四○", 19911, list(range(19911,19921)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _si_group("六八○○", 19993, list(range(19994,20004)), "table_rows_text_layer_located_title_row_is_entry_1"),
    {
        "collection": "巳", "raw_group_marker": "八八一○", "occurrence": 1,
        "normalized_group_marker_candidate": "六八一○", "group_header_pdf_line": 20010,
        "pdf_text_lines": "20010-20020", "layout_status": "raw_marker_ocr_variant_candidate_6810",
        "entry_count": 10, "entries": [{"entry_sequence": n, "pdf_text_line": line} for n,line in enumerate(range(20010,20020),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "巳", "raw_group_marker": "八八二○", "occurrence": 1,
        "normalized_group_marker_candidate": "六八二○", "group_header_pdf_line": 20022,
        "pdf_text_lines": "20022-20032", "layout_status": "raw_marker_ocr_variant_candidate_6820",
        "entry_count": 10, "entries": [{"entry_sequence": n, "pdf_text_line": line} for n,line in enumerate(range(20022,20032),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "巳", "raw_group_marker": "八八三○", "occurrence": 1,
        "normalized_group_marker_candidate": "六八三○", "group_header_pdf_line": 20034,
        "pdf_text_lines": "20034-20044", "layout_status": "raw_marker_ocr_variant_candidate_6830",
        "entry_count": 10, "entries": [{"entry_sequence": n, "pdf_text_line": line} for n,line in enumerate(range(20034,20044),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _si_group("六八四○", 20060, list(range(20062,20072))),
    _si_group("六八五○", 20073, list(range(20074,20084))),
    _si_group("六八七○", 20092, list(range(20095,20105)), "table_header_then_ten_entries"),
    _si_group("六八八○", 20106, list(range(20109,20119)), "table_rows_text_layer_located"),
    _si_group("六八九○", 20120, list(range(20123,20133)), "table_rows_text_layer_located"),
    {
        "collection": "巳", "raw_group_marker": "六九○", "occurrence": 1,
        "normalized_group_marker_candidate": "六九○○", "group_header_pdf_line": 20136,
        "pdf_text_lines": "20136-20148", "layout_status": "short_marker_first_ten_row_table_only",
        "entry_count": 10, "entries": [{"entry_sequence": n, "pdf_text_line": line} for n,line in enumerate(range(20138,20148),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _si_group("六九三○", 20181, list(range(20185,20195)), "page_header_before_ten_entries"),
    _si_group("六九四○", 20196, list(range(20199,20209)), "table_rows_text_layer_located"),
    _si_group("六九五○", 20210, list(range(20213,20223)), "table_rows_text_layer_located"),
    _si_group("六九六○", 20237, list(range(20238,20248))),
    _si_group("六九七○", 20249, list(range(20251,20261))),
]

SI_GROUP_ANOMALIES = [
    {"raw_group_marker": "六○○○", "pdf_text_line": None,
     "status": "ten_unheaded_entries_at_collection_start_no_explicit_group_marker"},
    {"raw_group_marker": "六一四○", "pdf_text_line": 18966,
     "status": "marker_seen_body_not_located_before_6150"},
    {"raw_group_marker": "六二○○", "pdf_text_line": 19046,
     "status": "marker_seen_body_not_located_before_short_raw_marker_620"},
    {"raw_group_marker": "六三二○", "pdf_text_line": None,
     "status": "unheaded_ten_entry_block_between_6310_and_6330"},
    {"raw_group_marker": "六三八○", "pdf_text_line": None,
     "status": "unheaded_ten_entry_block_between_6370_and_6390"},
    {"raw_group_marker": "六四一○", "pdf_text_line": None,
     "status": "age_clause_block_remains_with_6400_heading_not_separate_group"},
    {"raw_group_marker": "六四四○", "pdf_text_line": 19418,
     "status": "marker_seen_body_not_located_before_6450"},
    {"raw_group_marker": "六五○○", "pdf_text_line": 19530,
     "status": "marker_seen_body_not_located_before_6510"},
    {"raw_group_marker": "六五二○", "pdf_text_line": None,
     "status": "unheaded_ten_entry_candidate_before_6530"},
    {"raw_group_marker": "六五七○", "pdf_text_line": 19628,
     "status": "complex_age_subblocks_10_plus_10_plus_10_alignment_unresolved"},
    {"raw_group_marker": "六五八○", "pdf_text_line": 19649,
     "status": "age_subheading_not_confirmed_as_independent_group"},
    {"raw_group_marker": "六五九○", "pdf_text_line": 19670,
     "status": "age_subheading_not_confirmed_as_independent_group"},
    {"raw_group_marker": "六七○○", "pdf_text_line": None,
     "status": "expected_marker_missing_between_6690_and_6710"},
    {"raw_group_marker": "六八六○", "pdf_text_line": 20085,
     "status": "marker_seen_body_not_located_before_6870"},
    {"raw_group_marker": "六九一○", "pdf_text_line": None,
     "status": "expected_marker_missing_in_6900_short_marker_section"},
    {"raw_group_marker": "六九二○", "pdf_text_line": None,
     "status": "expected_marker_missing_in_6900_short_marker_section"},
    {"raw_group_marker": "六九八○", "pdf_text_line": 20262,
     "status": "complex_two_or_more_subblocks_alignment_unresolved"}
]

SI_UNASSIGNED_BLOCKS = [
    {"block_id": "si_unheaded_entries_before_6010", "pdf_text_lines": "18708-18717",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "si_age_data_after_short_6210_candidate", "pdf_text_lines": "19065-19074",
     "entry_count_candidate": 10, "status": "separate_age_column_block_alignment_pending"},
    {"block_id": "si_age_data_after_6220", "pdf_text_lines": "19088-19097",
     "entry_count_candidate": 10, "status": "separate_age_column_block_alignment_pending"},
    {"block_id": "si_age_data_after_6230", "pdf_text_lines": "19110-19120",
     "entry_count_candidate": 11, "status": "separate_age_column_block_alignment_pending"},
    {"block_id": "si_unheaded_entries_between_6310_and_6330", "pdf_text_lines": "19254-19263",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "si_unheaded_entries_between_6370_and_6390", "pdf_text_lines": "19333-19342",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "si_possible_6520_body", "pdf_text_lines": "19547-19556",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "si_complex_6570_age_subblocks", "pdf_text_lines": "19629-19680",
     "entry_count_candidate": 30, "status": "age_subblocks_and_clause_block_alignment_unresolved"},
    {"block_id": "si_possible_6700_fragment_after_6690", "pdf_text_lines": "19861-19864",
     "entry_count_candidate": 4, "status": "group_boundary_unresolved_do_not_assign"},
    {"block_id": "si_second_and_third_tables_after_690_short_marker", "pdf_text_lines": "20150-20172",
     "entry_count_candidate": 20, "status": "no_independent_group_markers_do_not_assign"},
    {"block_id": "si_visual_candidate_6990", "pdf_text_lines": "20267-20296",
     "entry_count_candidate": 10, "status": "marker_visible_in_page_visual_description_not_text_layer_heading"},
    {"block_id": "si_visual_candidate_7000", "pdf_text_lines": "20298-20328",
     "entry_count_candidate": 10, "status": "marker_visible_in_page_visual_description_not_text_layer_heading"}
]


def _wu_group(raw_marker, header_line, entry_lines, layout_status="text_layer_rows_located_image_check_pending"):
    return {
        "collection": "午", "raw_group_marker": raw_marker, "occurrence": 1,
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": header_line,
        "pdf_text_lines": f"{header_line}-{entry_lines[-1]}",
        "layout_status": layout_status, "entry_count": len(entry_lines),
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate(entry_lines,1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    }


WU_GROUP_INDEX = [
    _wu_group("七○一○", 20334, list(range(20334,20344)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七○二○", 20346, list(range(20346,20356)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七○三○", 20370, list(range(20372,20382))),
    _wu_group("七○四○", 20383, list(range(20384,20394))),
    _wu_group("七○五○", 20395, list(range(20399,20409)), "page_header_before_ten_entries"),
    _wu_group("七○六○", 20410, list(range(20411,20421))),
    _wu_group("七○七○", 20422, list(range(20424,20434))),
    _wu_group("七○八○", 20435, list(range(20438,20448)), "page_header_before_ten_entries"),
    _wu_group("七○九○", 20449, list(range(20451,20461))),
    _wu_group("七一○○", 20462, list(range(20463,20473))),
    _wu_group("七一一○", 20474, list(range(20478,20488)), "page_header_before_ten_entries"),
    _wu_group("七一二○", 20489, list(range(20490,20500))),
    _wu_group("七一三○", 20501, list(range(20503,20513))),
    {
        "collection": "午", "raw_group_marker": "七一四○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 20514,
        "pdf_text_lines": "20514-20536", "layout_status": "age_key_rows_then_ten_clause_rows",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate(range(20527,20537),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wu_group("七一八○", 20569, list(range(20571,20581)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七一九○", 20582, list(range(20584,20594)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七二○○", 20595, list(range(20597,20607)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七二二○", 20637, list(range(20638,20648))),
    _wu_group("七二三○", 20649, list(range(20659,20669)), "table_rows_text_layer_located"),
    _wu_group("七二四○", 20671, list(range(20675,20685)), "table_rows_text_layer_located"),
    _wu_group("七二五○", 20687, list(range(20691,20701)), "table_rows_text_layer_located"),
    {
        "collection": "午", "raw_group_marker": "七一七○", "occurrence": 1,
        "normalized_group_marker_candidate": "七二七○", "group_header_pdf_line": 20710,
        "pdf_text_lines": "20710-20724", "layout_status": "raw_marker_candidate_7270_after_7260_header",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate(range(20714,20724),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wu_group("七二八○", 20726, list(range(20730,20740)), "table_rows_text_layer_located"),
    _wu_group("七二九○", 20742, list(range(20746,20756)), "table_rows_text_layer_located"),
    _wu_group("七三○○", 20760, list(range(20763,20773)), "table_rows_text_layer_located"),
    _wu_group("七三二○", 20786, list(range(20789,20799)), "table_rows_text_layer_located"),
    _wu_group("七三三○", 20807, list(range(20810,20820)), "table_rows_text_layer_located"),
    _wu_group("七三四○", 20821, list(range(20824,20834)), "table_rows_text_layer_located"),
    _wu_group("七三五○", 20835, list(range(20838,20848)), "table_rows_text_layer_located"),
    _wu_group("七三六○", 20861, list(range(20863,20873))),
    _wu_group("七三七○", 20874, list(range(20875,20885))),
    _wu_group("七三九○", 20888, list(range(20890,20900)), "table_rows_text_layer_located"),
    {
        "collection": "午", "raw_group_marker": "七四一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 20926,
        "pdf_text_lines": "20926-20972", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 20935, "record_span": "20935-20938"},
            {"entry_sequence": 2, "pdf_text_line": 20940, "record_span": "20940-20942"},
            {"entry_sequence": 3, "pdf_text_line": 20944, "record_span": "20944-20945"},
            {"entry_sequence": 4, "pdf_text_line": 20947, "record_span": "20947-20949"},
            {"entry_sequence": 5, "pdf_text_line": 20951, "record_span": "20951-20953"},
            {"entry_sequence": 6, "pdf_text_line": 20955, "record_span": "20955-20957"},
            {"entry_sequence": 7, "pdf_text_line": 20959, "record_span": "20959-20961"},
            {"entry_sequence": 8, "pdf_text_line": 20963, "record_span": "20963-20965"},
            {"entry_sequence": 9, "pdf_text_line": 20966, "record_span": "20966-20968"},
            {"entry_sequence": 10, "pdf_text_line": 20970, "record_span": "20970-20972"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "七四二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 20974,
        "pdf_text_lines": "20974-21012", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 20976, "record_span": "20976-20977"},
            {"entry_sequence": 2, "pdf_text_line": 20979, "record_span": "20979-20982"},
            {"entry_sequence": 3, "pdf_text_line": 20984, "record_span": "20984-20987"},
            {"entry_sequence": 4, "pdf_text_line": 20989},
            {"entry_sequence": 5, "pdf_text_line": 20991, "record_span": "20991-20993"},
            {"entry_sequence": 6, "pdf_text_line": 20995, "record_span": "20995-20997"},
            {"entry_sequence": 7, "pdf_text_line": 20999, "record_span": "20999-21001"},
            {"entry_sequence": 8, "pdf_text_line": 21003, "record_span": "21003-21005"},
            {"entry_sequence": 9, "pdf_text_line": 21007, "record_span": "21007-21009"},
            {"entry_sequence": 10, "pdf_text_line": 21011}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "七四三○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21013,
        "pdf_text_lines": "21013-21056", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21019, "record_span": "21019-21022"},
            {"entry_sequence": 2, "pdf_text_line": 21024, "record_span": "21024-21026"},
            {"entry_sequence": 3, "pdf_text_line": 21028, "record_span": "21028-21031"},
            {"entry_sequence": 4, "pdf_text_line": 21033, "record_span": "21033-21036"},
            {"entry_sequence": 5, "pdf_text_line": 21038, "record_span": "21038-21039"},
            {"entry_sequence": 6, "pdf_text_line": 21041, "record_span": "21041-21042"},
            {"entry_sequence": 7, "pdf_text_line": 21044, "record_span": "21044-21045"},
            {"entry_sequence": 8, "pdf_text_line": 21047, "record_span": "21047-21049"},
            {"entry_sequence": 9, "pdf_text_line": 21051, "record_span": "21051-21053"},
            {"entry_sequence": 10, "pdf_text_line": 21055, "record_span": "21055-21056"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wu_group("七四五○", 21065, list(range(21068,21078)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七四六○", 21079, list(range(21082,21092)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七四七○", 21093, list(range(21095,21105)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七四八○", 21123, list(range(21124,21134))),
    _wu_group("七四九○", 21135, list(range(21137,21147))),
    {
        "collection": "午", "raw_group_marker": "七五○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21148,
        "pdf_text_lines": "21148-21163", "layout_status": "ten_entries_with_age_and_clause_lines_spanning",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21151},
            {"entry_sequence": 2, "pdf_text_line": 21152},
            {"entry_sequence": 3, "pdf_text_line": 21153},
            {"entry_sequence": 4, "pdf_text_line": 21154, "record_span": "21154-21155"},
            {"entry_sequence": 5, "pdf_text_line": 21156},
            {"entry_sequence": 6, "pdf_text_line": 21157, "record_span": "21157-21158"},
            {"entry_sequence": 7, "pdf_text_line": 21159},
            {"entry_sequence": 8, "pdf_text_line": 21160, "record_span": "21160-21161"},
            {"entry_sequence": 9, "pdf_text_line": 21162},
            {"entry_sequence": 10, "pdf_text_line": 21163}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "七五一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21165,
        "pdf_text_lines": "21165-21183", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21167, "record_span": "21167-21168"},
            {"entry_sequence": 2, "pdf_text_line": 21169},
            {"entry_sequence": 3, "pdf_text_line": 21170, "record_span": "21170-21171"},
            {"entry_sequence": 4, "pdf_text_line": 21172},
            {"entry_sequence": 5, "pdf_text_line": 21173, "record_span": "21173-21174"},
            {"entry_sequence": 6, "pdf_text_line": 21175, "record_span": "21175-21176"},
            {"entry_sequence": 7, "pdf_text_line": 21177, "record_span": "21177-21178"},
            {"entry_sequence": 8, "pdf_text_line": 21179, "record_span": "21179-21180"},
            {"entry_sequence": 9, "pdf_text_line": 21181},
            {"entry_sequence": 10, "pdf_text_line": 21182, "record_span": "21182-21183"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "七五二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21185,
        "pdf_text_lines": "21185-21200", "layout_status": "multi_line_age_clause_spans",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21186},
            {"entry_sequence": 2, "pdf_text_line": 21187},
            {"entry_sequence": 3, "pdf_text_line": 21188, "record_span": "21188-21189"},
            {"entry_sequence": 4, "pdf_text_line": 21190, "record_span": "21190-21191"},
            {"entry_sequence": 5, "pdf_text_line": 21192, "record_span": "21192-21193"},
            {"entry_sequence": 6, "pdf_text_line": 21194},
            {"entry_sequence": 7, "pdf_text_line": 21195},
            {"entry_sequence": 8, "pdf_text_line": 21196, "record_span": "21196-21197"},
            {"entry_sequence": 9, "pdf_text_line": 21198},
            {"entry_sequence": 10, "pdf_text_line": 21199, "record_span": "21199-21200"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wu_group("七五三○", 21202, list(range(21206,21216)), "page_header_before_ten_entries"),
    _wu_group("七五四○", 21217, list(range(21218,21228))),
    {
        "collection": "午", "raw_group_marker": "七五五○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21229,
        "pdf_text_lines": "21229-21240", "layout_status": "sequence_1_missing_nine_entries_only",
        "entry_count": 9,
        "entries": [{"entry_sequence": n, "pdf_text_line": line, "record_span": span}
                    for n,line,span in zip(range(2,11),
                        [21231,21232,21233,21234,21235,21236,21237,21238,21239],
                        ["21231","21232","21233","21234","21235","21236","21237","21238","21239-21240"])],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "一九五七○", "occurrence": 1,
        "normalized_group_marker_candidate": "七五七○", "group_header_pdf_line": 21246,
        "pdf_text_lines": "21246-21256", "layout_status": "raw_ocr_marker_variant_candidate_7570",
        "entry_count": 10, "entries": [{"entry_sequence": n, "pdf_text_line": line}
                                      for n,line in enumerate(range(21247,21257),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "一九五八○", "occurrence": 1,
        "normalized_group_marker_candidate": "七五八○", "group_header_pdf_line": 21258,
        "pdf_text_lines": "21258-21269", "layout_status": "raw_ocr_marker_variant_candidate_7580",
        "entry_count": 10, "entries": [{"entry_sequence": n, "pdf_text_line": line}
                                      for n,line in enumerate(range(21260,21270),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "一九五九○", "occurrence": 1,
        "normalized_group_marker_candidate": "七五九○", "group_header_pdf_line": 21271,
        "pdf_text_lines": "21271-21281", "layout_status": "raw_ocr_marker_variant_candidate_7590",
        "entry_count": 10, "entries": [{"entry_sequence": n, "pdf_text_line": line}
                                      for n,line in enumerate(range(21272,21282),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wu_group("七六○○", 21299, list(range(21301,21311))),
    _wu_group("七六一○", 21312, list(range(21313,21323))),
    _wu_group("七六三○", 21331, list(range(21332,21342)), "age_sequence_rows_no_ordinal_labels"),
    _wu_group("七六四○", 21343, list(range(21344,21354))),
    _wu_group("七六五○", 21354, list(range(21355,21365))),
    _wu_group("七六六○", 21379, list(range(21380,21390))),
    _wu_group("七六七○", 21391, list(range(21393,21403))),
    _wu_group("七六八○", 21404, list(range(21407,21417))),
    _wu_group("七六九○", 21418, list(range(21420,21430))),
    _wu_group("七七○○", 21431, list(range(21432,21442))),
    _wu_group("七七二○", 21449, list(range(21451,21461))),
    _wu_group("七七三○", 21462, list(range(21463,21473))),
    _wu_group("七七四○", 21474, list(range(21476,21486))),
    _wu_group("七七五○", 21499, list(range(21501,21511))),
    _wu_group("七七六○", 21512, list(range(21513,21523))),
    _wu_group("七七八○", 21528, list(range(21530,21540)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七七九○", 21541, list(range(21543,21553)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七八○○", 21554, list(range(21556,21566)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七八一○", 21580, list(range(21582,21592))),
    _wu_group("七八二○", 21593, list(range(21594,21604))),
    _wu_group("七八四○", 21609, list(range(21611,21621))),
    _wu_group("七八五○", 21622, list(range(21623,21633))),
    _wu_group("七八六○", 21634, list(range(21636,21646))),
    {
        "collection": "午", "raw_group_marker": "七八七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21669,
        "pdf_text_lines": "21669-21690", "layout_status": "ten_entries_split_across_two_lines",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21671, "record_span": "21671-21672"},
            {"entry_sequence": 2, "pdf_text_line": 21673, "record_span": "21673-21674"},
            {"entry_sequence": 3, "pdf_text_line": 21675, "record_span": "21675-21676"},
            {"entry_sequence": 4, "pdf_text_line": 21677, "record_span": "21677-21678"},
            {"entry_sequence": 5, "pdf_text_line": 21679, "record_span": "21679-21680"},
            {"entry_sequence": 6, "pdf_text_line": 21681, "record_span": "21681-21682"},
            {"entry_sequence": 7, "pdf_text_line": 21683, "record_span": "21683-21684"},
            {"entry_sequence": 8, "pdf_text_line": 21685, "record_span": "21685-21686"},
            {"entry_sequence": 9, "pdf_text_line": 21687, "record_span": "21687-21688"},
            {"entry_sequence": 10, "pdf_text_line": 21689, "record_span": "21689-21690"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "七八八○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21692,
        "pdf_text_lines": "21692-21713", "layout_status": "ten_entries_split_across_two_lines",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21693, "record_span": "21693-21694"},
            {"entry_sequence": 2, "pdf_text_line": 21695, "record_span": "21695-21696"},
            {"entry_sequence": 3, "pdf_text_line": 21697, "record_span": "21697-21698"},
            {"entry_sequence": 4, "pdf_text_line": 21699, "record_span": "21699-21700"},
            {"entry_sequence": 5, "pdf_text_line": 21701, "record_span": "21701-21702"},
            {"entry_sequence": 6, "pdf_text_line": 21703, "record_span": "21703-21704"},
            {"entry_sequence": 7, "pdf_text_line": 21705, "record_span": "21705-21706"},
            {"entry_sequence": 8, "pdf_text_line": 21707, "record_span": "21707-21708"},
            {"entry_sequence": 9, "pdf_text_line": 21709, "record_span": "21709-21710"},
            {"entry_sequence": 10, "pdf_text_line": 21711, "record_span": "21711-21712"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wu_group("七九○○", 21718, list(range(21721,21731)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wu_group("七九三○", 21760, list(range(21762,21772))),
    _wu_group("七九四○", 21773, list(range(21774,21784))),
    _wu_group("七九五○", 21785, list(range(21787,21797))),
    {
        "collection": "午", "raw_group_marker": "七九六○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21835,
        "pdf_text_lines": "21835-21880", "layout_status": "ten_entries_split_across_age_and_clause_lines",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21837, "record_span": "21837-21839"},
            {"entry_sequence": 2, "pdf_text_line": 21841, "record_span": "21841-21844"},
            {"entry_sequence": 3, "pdf_text_line": 21846, "record_span": "21846-21847"},
            {"entry_sequence": 4, "pdf_text_line": 21849, "record_span": "21849-21852"},
            {"entry_sequence": 5, "pdf_text_line": 21854, "record_span": "21854-21855"},
            {"entry_sequence": 6, "pdf_text_line": 21857, "record_span": "21857-21860"},
            {"entry_sequence": 7, "pdf_text_line": 21862, "record_span": "21862-21865"},
            {"entry_sequence": 8, "pdf_text_line": 21867, "record_span": "21867-21870"},
            {"entry_sequence": 9, "pdf_text_line": 21872, "record_span": "21872-21875"},
            {"entry_sequence": 10, "pdf_text_line": 21877, "record_span": "21877-21879"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "午", "raw_group_marker": "七九七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21881,
        "pdf_text_lines": "21881-21920", "layout_status": "ten_entries_split_across_age_and_clause_lines",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21883, "record_span": "21883-21886"},
            {"entry_sequence": 2, "pdf_text_line": 21888, "record_span": "21888-21891"},
            {"entry_sequence": 3, "pdf_text_line": 21893, "record_span": "21893-21894"},
            {"entry_sequence": 4, "pdf_text_line": 21896, "record_span": "21896-21898"},
            {"entry_sequence": 5, "pdf_text_line": 21900, "record_span": "21900-21901"},
            {"entry_sequence": 6, "pdf_text_line": 21903, "record_span": "21903-21906"},
            {"entry_sequence": 7, "pdf_text_line": 21908, "record_span": "21908-21910"},
            {"entry_sequence": 8, "pdf_text_line": 21911, "record_span": "21911-21913"},
            {"entry_sequence": 9, "pdf_text_line": 21915, "record_span": "21915-21916"},
            {"entry_sequence": 10, "pdf_text_line": 21918, "record_span": "21918-21920"}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wu_group("七九九○", 21938, list(range(21940,21950)), "table_rows_text_layer_located"),
    {
        "collection": "午", "raw_group_marker": "八○一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 21958,
        "pdf_text_lines": "21958-21973", "layout_status": "multi_line_age_fields",
        "entry_count": 10,
        "entries": [
            {"entry_sequence": 1, "pdf_text_line": 21960},
            {"entry_sequence": 2, "pdf_text_line": 21961},
            {"entry_sequence": 3, "pdf_text_line": 21962},
            {"entry_sequence": 4, "pdf_text_line": 21963},
            {"entry_sequence": 5, "pdf_text_line": 21964, "record_span": "21964-21967"},
            {"entry_sequence": 6, "pdf_text_line": 21968},
            {"entry_sequence": 7, "pdf_text_line": 21969},
            {"entry_sequence": 8, "pdf_text_line": 21970},
            {"entry_sequence": 9, "pdf_text_line": 21971},
            {"entry_sequence": 10, "pdf_text_line": 21972}
        ],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
]

WU_GROUP_ANOMALIES = [
    {"raw_group_marker": "七一六○", "pdf_text_line": 20538,
     "status": "short_marker_fragment_candidate_7160"},
    {"raw_group_marker": "七一七○", "pdf_text_line": 20551,
     "status": "short_marker_fragment_candidate_7170"},
    {"raw_group_marker": "七二一○", "pdf_text_line": None,
     "status": "unheaded_ten_entry_block_before_7220"},
    {"raw_group_marker": "七二六○", "pdf_text_line": 20703,
     "status": "marker_seen_body_not_located_before_raw_7170_candidate"},
    {"raw_group_marker": "七三八○", "pdf_text_line": None,
     "status": "expected_marker_missing_between_7370_and_7390"},
    {"raw_group_marker": "七四○○", "pdf_text_line": None,
     "status": "unheaded_table_candidate_after_7390"},
    {"raw_group_marker": "七四四○", "pdf_text_line": 21058,
     "status": "marker_seen_body_not_located_before_7450"},
    {"raw_group_marker": "七五六○", "pdf_text_line": 21242,
     "status": "marker_seen_body_not_located_before_raw_7570"},
    {"raw_group_marker": "七六二○", "pdf_text_line": 21324,
     "status": "marker_seen_body_not_located_before_7630"},
    {"raw_group_marker": "七七一○", "pdf_text_line": 21443,
     "status": "marker_seen_body_not_located_before_7720"},
    {"raw_group_marker": "七七七○", "pdf_text_line": 21524,
     "status": "marker_seen_body_not_located_before_7780"},
    {"raw_group_marker": "七八三○", "pdf_text_line": 21605,
     "status": "marker_seen_body_not_located_before_7840"},
    {"raw_group_marker": "七八九○", "pdf_text_line": 21714,
     "status": "marker_seen_body_not_located_before_7900"},
    {"raw_group_marker": "七九一○", "pdf_text_line": None,
     "status": "possible_unheaded_table_after_7900"},
    {"raw_group_marker": "七九二○", "pdf_text_line": None,
     "status": "possible_unheaded_table_after_7900"},
    {"raw_group_marker": "七九八○", "pdf_text_line": None,
     "status": "unheaded_ten_entry_block_before_7990"},
    {"raw_group_marker": "八○○○", "pdf_text_line": 21951,
     "status": "marker_seen_body_not_located_before_8010"},
    {"raw_group_marker": "八○二○", "pdf_text_line": None,
     "status": "unheaded_block_after_8010_before_wei_collection"}
]
WU_UNASSIGNED_BLOCKS = [
    {"block_id": "wu_unheaded_ten_entries_after_7020", "pdf_text_lines": "20359-20368",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wu_possible_7160_fragment", "pdf_text_lines": "20538-20549",
     "entry_count_candidate": 10, "status": "short_marker_fragment_alignment_pending"},
    {"block_id": "wu_possible_7170_fragment", "pdf_text_lines": "20551-20563",
     "entry_count_candidate": 10, "status": "short_marker_fragment_alignment_pending"},
    {"block_id": "wu_unheaded_entries_before_7220", "pdf_text_lines": "20613-20623",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wu_possible_7310_table", "pdf_text_lines": "20775-20785",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wu_unheaded_entries_before_7360", "pdf_text_lines": "20850-20859",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wu_possible_7400_table", "pdf_text_lines": "20902-20924",
     "entry_count_candidate": 10, "status": "group_boundary_ambiguous_do_not_assign"},
    {"block_id": "wu_unheaded_entries_between_7590_and_7600", "pdf_text_lines": "21287-21297",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wu_possible_7910_table", "pdf_text_lines": "21733-21742",
     "entry_count_candidate": 10, "status": "second_table_after_7900_no_separate_heading_do_not_assign"},
    {"block_id": "wu_possible_7920_table", "pdf_text_lines": "21745-21754",
     "entry_count_candidate": 10, "status": "third_table_after_7900_no_separate_heading_do_not_assign"},
    {"block_id": "wu_possible_7980_body", "pdf_text_lines": "21926-21936",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wu_possible_8020_body", "pdf_text_lines": "21974-21988",
     "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"}
]


def _wei_group(raw_marker, header_line, entry_lines, layout_status="text_layer_rows_located_image_check_pending"):
    return {
        "collection": "未", "raw_group_marker": raw_marker, "occurrence": 1,
        "normalized_group_marker_candidate": None,
        "group_header_pdf_line": header_line,
        "pdf_text_lines": f"{header_line}-{entry_lines[-1]}",
        "layout_status": layout_status, "entry_count": len(entry_lines),
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate(entry_lines,1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    }


WEI_GROUP_INDEX = [
    _wei_group("八○三○", 22026, list(range(22032,22042)), "three_headers_before_one_ten_entry_block"),
    _wei_group("八○六○", 22043, list(range(22044,22054))),
    _wei_group("八○七○", 22055, list(range(22057,22067))),
    {
        "collection": "未", "raw_group_marker": "一九八○", "occurrence": 1,
        "normalized_group_marker_candidate": "八○八○", "group_header_pdf_line": 22072,
        "pdf_text_lines": "22072-22084", "layout_status": "raw_ocr_marker_candidate_8080",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line} for n,line in enumerate(range(22074,22084),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八一二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22119,
        "pdf_text_lines": "22119-22119", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "source_row_line": 22119, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八一三○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22120,
        "pdf_text_lines": "22120-22120", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "source_row_line": 22120, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八一四○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22121,
        "pdf_text_lines": "22121-22121", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "source_row_line": 22121, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wei_group("八一五○", 22140, list(range(22141,22151))),
    _wei_group("八一六○", 22152, list(range(22154,22164))),
    _wei_group("八一八○", 22169, list(range(22170,22180))),
    _wei_group("八一九○", 22181, list(range(22183,22193))),
    _wei_group("八二○○", 22194, list(range(22195,22205))),
    _wei_group("八二一○", 22221, list(range(22222,22232))),
    _wei_group("八二二○", 22233, list(range(22235,22245))),
    _wei_group("八二四○", 22258, list(range(22260,22270))),
    _wei_group("八二五○", 22270, list(range(22271,22281))),
    _wei_group("八二七○", 22285, list(range(22285,22295)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wei_group("八二八○", 22297, list(range(22297,22307)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wei_group("八二九○", 22309, list(range(22309,22319)), "table_rows_text_layer_located_title_row_is_entry_1"),
    _wei_group("八三○○", 22335, list(range(22337,22347))),
    _wei_group("八三一○", 22348, list(range(22349,22359))),
    {
        "collection": "未", "raw_group_marker": "八三三○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22362,
        "pdf_text_lines": "22362-22374", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10, "entries": [{"entry_sequence": n, "source_row_line": 22365, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八三四○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22376,
        "pdf_text_lines": "22376-22388", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10, "entries": [{"entry_sequence": n, "source_row_line": 22379, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八三五○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22390,
        "pdf_text_lines": "22390-22402", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10, "entries": [{"entry_sequence": n, "source_row_line": 22393, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wei_group("八三六○", 22416, list(range(22418,22428))),
    _wei_group("八三七○", 22429, list(range(22430,22440))),
    {
        "collection": "未", "raw_group_marker": "八三九○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22450,
        "pdf_text_lines": "22450-22462", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10, "entries": [{"entry_sequence": n, "source_row_line": 22453, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八四○○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22464,
        "pdf_text_lines": "22464-22476", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10, "entries": [{"entry_sequence": n, "source_row_line": 22467, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八四一○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22478,
        "pdf_text_lines": "22478-22490", "layout_status": "single_table_row_contains_ten_clause_cells",
        "entry_count": 10, "entries": [{"entry_sequence": n, "source_row_line": 22481, "cell_sequence": n} for n in range(1,11)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八四二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22524,
        "pdf_text_lines": "22524-22560", "layout_status": "age_column_then_ten_clause_lines",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip([22537,22538,22539,22540,22541,22542,22543,22544,22545,22546],
                                                        range(22551,22561)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八四三○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22562,
        "pdf_text_lines": "22562-22596", "layout_status": "age_column_then_ten_clause_lines",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "age_data_line": age, "clause_text_line": clause}
                    for n,(age,clause) in enumerate(zip(range(22574,22584),range(22587,22597)),1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wei_group("八四四○", 22598, list(range(22606,22616)), "section_header_then_ten_entries"),
    _wei_group("八四五○", 22617, list(range(22618,22628))),
    _wei_group("八四六○", 22629, list(range(22631,22641))),
    _wei_group("八四八○", 22646, list(range(22649,22659)), "table_rows_text_layer_located"),
    _wei_group("八四九○", 22672, list(range(22677,22687)), "table_rows_text_layer_located"),
    _wei_group("八五一○", 22702, list(range(22704,22714))),
    {
        "collection": "未", "raw_group_marker": "八五二○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22715,
        "pdf_text_lines": "22715-22725", "layout_status": "duplicate_sequence_3_no_sequence_1",
        "entry_count": 10,
        "entries": [{"entry_sequence": raw, "pdf_text_line": line}
                    for raw,line in zip([2,3,3,4,5,6,7,8,9,10],range(22716,22726))],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wei_group("八五四○", 22742, list(range(22743,22753))),
    _wei_group("八五五○", 22754, list(range(22756,22766))),
    {
        "collection": "未", "raw_group_marker": "八五七○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22771,
        "pdf_text_lines": "22771-22782", "layout_status": "entry_9_spans_two_lines",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line,
                     **({"record_span": "22780-22781"} if n == 9 else {})}
                    for n,line in enumerate([22772,22773,22774,22775,22776,22777,22778,22779,22780,22782],1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八五八○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22784,
        "pdf_text_lines": "22784-22799", "layout_status": "multiple_age_values_spanning_lines",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate([22786,22787,22788,22790,22792,22793,22794,22796,22797,22799],1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    {
        "collection": "未", "raw_group_marker": "八五九○", "occurrence": 1,
        "normalized_group_marker_candidate": None, "group_header_pdf_line": 22801,
        "pdf_text_lines": "22801-22813", "layout_status": "entries_9_and_10_span_two_lines",
        "entry_count": 10,
        "entries": [{"entry_sequence": n, "pdf_text_line": line}
                    for n,line in enumerate([22802,22803,22804,22805,22806,22807,22808,22809,22810,22812],1)],
        "verification_status": "pdf_text_layer_only_image_check_pending"
    },
    _wei_group("八六○○", 22819, list(range(22824,22834)), "internal_64_hexagram_subsection_heading_before_ten_entries"),
    _wei_group("八六一○", 22835, list(range(22836,22846))),
    _wei_group("八六二○", 22846, list(range(22847,22857))),
    _wei_group("八六三○", 22864, list(range(22866,22876)), "table_rows_text_layer_located"),
]

WEI_GROUP_ANOMALIES = [
    {"raw_group_marker": "八○二○", "pdf_text_line": None, "status": "three_unheaded_blocks_before_8030"},
    {"raw_group_marker": "八○四○", "pdf_text_line": 22027, "status": "header_seen_body_not_located"},
    {"raw_group_marker": "八○五○", "pdf_text_line": 22028, "status": "header_seen_body_not_located"},
    {"raw_group_marker": "八○九○", "pdf_text_line": None, "status": "second_table_after_8080_candidate"},
    {"raw_group_marker": "八一○○", "pdf_text_line": None, "status": "third_table_after_8080_candidate"},
    {"raw_group_marker": "八一一○", "pdf_text_line": None, "status": "unheaded_ten_entry_block_before_8150"},
    {"raw_group_marker": "八一七○", "pdf_text_line": 22165, "status": "header_seen_body_not_located_before_8180"},
    {"raw_group_marker": "八二三○", "pdf_text_line": 22244, "status": "marker_embedded_in_8220_tenth_entry_not_separate_header"},
    {"raw_group_marker": "八二六○", "pdf_text_line": 22281, "status": "header_seen_body_not_located_before_8270"},
    {"raw_group_marker": "八三二○", "pdf_text_line": 22358, "status": "marker_embedded_in_8310_tenth_entry_not_separate_group"},
    {"raw_group_marker": "八三八○", "pdf_text_line": 22443, "status": "header_seen_body_not_located_before_8390"},
    {"raw_group_marker": "八四七○", "pdf_text_line": 22642, "status": "header_seen_body_not_located_before_8480"},
    {"raw_group_marker": "八五○○", "pdf_text_line": None, "status": "unheaded_ten_entry_block_before_8510"},
    {"raw_group_marker": "八五六○", "pdf_text_line": 22767, "status": "header_seen_body_not_located_before_8570"}
]

WEI_UNASSIGNED_BLOCKS = [
    {"block_id": "wei_unheaded_block_before_8030_a", "pdf_text_lines": "21994-22003", "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wei_unheaded_block_before_8030_b", "pdf_text_lines": "22005-22014", "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wei_unheaded_block_before_8030_c", "pdf_text_lines": "22015-22024", "entry_count_candidate": 10, "status": "group_marker_missing_do_not_assign"},
    {"block_id": "wei_second_table_after_8080", "pdf_text_lines": "22086-22095", "entry_count_candidate": 10, "status": "possible_8090_no_heading"},
    {"block_id": "wei_third_table_after_8080", "pdf_text_lines": "22098-22107", "entry_count_candidate": 10, "status": "possible_8100_no_heading"},
    {"block_id": "wei_unheaded_block_before_8150", "pdf_text_lines": "22129-22138", "entry_count_candidate": 10, "status": "possible_8110_no_heading"},
    {"block_id": "wei_second_table_after_8480", "pdf_text_lines": "22661-22670", "entry_count_candidate": 10, "status": "possible_8485_no_heading"},
    {"block_id": "wei_unheaded_block_before_8510", "pdf_text_lines": "22691-22700", "entry_count_candidate": 10, "status": "possible_8500_no_heading"}
]


def get_collection_branch_group_index(branch):
    if branch == "子":
        return get_group_index()
    if branch == "未":
        return {
            "edition": EDITION, "collection": "未集",
            "status": "partial_text_layer_index_image_verification_pending",
            "group_count": len(WEI_GROUP_INDEX),
            "entry_count": sum(len(group["entries"]) for group in WEI_GROUP_INDEX),
            "groups": [dict(group, entries=[dict(entry) for entry in group["entries"]]) for group in WEI_GROUP_INDEX],
            "group_anomalies": [dict(item) for item in WEI_GROUP_ANOMALIES],
            "unassigned_blocks": [dict(item) for item in WEI_UNASSIGNED_BLOCKS],
            "limitations": [
                "未集目前仅完成开头已定位组号的结构索引，不代表全篇完成。",
                "单行表格含十个断语单元时，按单元格序号记录，不展开复制正文。",
                "OCR候选组号与无组号表格分开保存，不自动归并。",
                "该结构索引不是坤集密码表，不可用于自动考刻、定数或断命。"
            ]
        }
    if branch == "午":
        return {
            "edition": EDITION, "collection": "午集",
            "status": "partial_text_layer_index_image_verification_pending",
            "group_count": len(WU_GROUP_INDEX),
            "entry_count": sum(len(group["entries"]) for group in WU_GROUP_INDEX),
            "groups": [dict(group, entries=[dict(entry) for entry in group["entries"]]) for group in WU_GROUP_INDEX],
            "group_anomalies": [dict(item) for item in WU_GROUP_ANOMALIES],
            "unassigned_blocks": [dict(item) for item in WU_UNASSIGNED_BLOCKS],
            "limitations": [
                "午集目前仅完成开头已定位组号的结构索引，不代表全篇完成。",
                "仅依据PDF文本层保存组号、序号和行位，扫描图像逐字核验待完成。",
                "无组号块不自动归并到相邻组。",
                "该结构索引不是坤集密码表，不可用于自动考刻、定数或断命。"
            ]
        }
    if branch == "巳":
        return {
            "edition": EDITION, "collection": "巳集",
            "status": "partial_text_layer_index_image_verification_pending",
            "group_count": len(SI_GROUP_INDEX),
            "entry_count": sum(len(group["entries"]) for group in SI_GROUP_INDEX),
            "groups": [dict(group, entries=[dict(entry) for entry in group["entries"]]) for group in SI_GROUP_INDEX],
            "group_anomalies": [dict(item) for item in SI_GROUP_ANOMALIES],
            "unassigned_blocks": [dict(item) for item in SI_UNASSIGNED_BLOCKS],
            "limitations": [
                "巳集目前仅完成开头已定位组号的结构索引，不代表全篇完成。",
                "仅依据PDF文本层保存组号、序号和行位，扫描图像逐字核验待完成。",
                "无组号开头十条内容不自动归入六○一○。",
                "该结构索引不是坤集密码表，不可用于自动考刻、定数或断命。"
            ]
        }
    if branch == "辰":
        return {
            "edition": EDITION, "collection": "辰集",
            "status": "partial_text_layer_index_image_verification_pending",
            "group_count": len(CHEN_GROUP_INDEX),
            "entry_count": sum(len(group["entries"]) for group in CHEN_GROUP_INDEX),
            "groups": [dict(group, entries=[dict(entry) for entry in group["entries"]]) for group in CHEN_GROUP_INDEX],
            "group_anomalies": [dict(item) for item in CHEN_GROUP_ANOMALIES],
            "unassigned_blocks": [dict(item) for item in CHEN_UNASSIGNED_BLOCKS],
            "limitations": [
                "辰集目前仅完成已定位组号的结构索引，不代表全篇完成。",
                "仅依据PDF文本层保存组号、序号与跨行范围，扫描图像逐字核验待完成。",
                "缺组标题、无组号块和多行表格单独保存，不自动补造。",
                "该结构索引不是坤集密码表，不可用于自动考刻、定数或断命。"
            ]
        }
    if branch == "卯":
        return {
            "edition": EDITION, "collection": "卯集",
            "status": "partial_text_layer_index_image_verification_pending",
            "group_count": len(MAO_GROUP_INDEX),
            "entry_count": sum(len(group["entries"]) for group in MAO_GROUP_INDEX),
            "groups": [dict(group, entries=[dict(entry) for entry in group["entries"]])
                       for group in MAO_GROUP_INDEX],
            "group_anomalies": [dict(item) for item in MAO_GROUP_ANOMALIES],
            "unassigned_blocks": [dict(item) for item in MAO_UNASSIGNED_BLOCKS],
            "limitations": [
                "本批仅索引卯集已定位组号的结构记录，不能代表卯集全部内容。",
                "组号、序号及跨页字段仅依据PDF文本层，仍待扫描图像复核。",
                "缺组标题与无组号十条块单独保存，不按编号顺序自动补造。",
                "该结构索引不是坤集密码表，不可用于自动考刻、定数或断命。"
            ]
        }
    if branch == "寅":
        return {
            "edition": EDITION, "collection": "寅集",
            "status": "partial_text_layer_index_image_verification_pending",
            "group_count": len(YIN_GROUP_INDEX),
            "entry_count": sum(len(group["entries"]) for group in YIN_GROUP_INDEX),
            "groups": [dict(group, entries=[dict(entry) for entry in group["entries"]])
                       for group in YIN_GROUP_INDEX],
            "group_anomalies": [dict(item) for item in YIN_GROUP_ANOMALIES],
            "unassigned_blocks": [dict(item) for item in YIN_UNASSIGNED_BLOCKS],
            "limitations": [
                "本批仅索引寅集已定位组号的结构记录，不能代表寅集全部内容。",
                "PDF文本层中的组号、序号及跨行字段仍待扫描图像核验。",
                "实集标题及无组号内容单独保存，不强行归入编号组。",
                "该结构索引不是坤集密码表，不可用于自动考刻、定数或断命。"
            ]
        }
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
                 {"indexed_groups": len(CHOU_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in CHOU_GROUP_INDEX)} if branch == "丑" else
                 {"indexed_groups": len(YIN_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in YIN_GROUP_INDEX)} if branch == "寅" else
                 {"indexed_groups": len(MAO_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in MAO_GROUP_INDEX)} if branch == "卯" else
                 {"indexed_groups": len(CHEN_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in CHEN_GROUP_INDEX)} if branch == "辰" else
                 {"indexed_groups": len(SI_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in SI_GROUP_INDEX)} if branch == "巳" else
                 {"indexed_groups": len(WU_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in WU_GROUP_INDEX)} if branch == "午" else
                 {"indexed_groups": len(WEI_GROUP_INDEX), "indexed_entries": sum(len(group["entries"]) for group in WEI_GROUP_INDEX)} if branch == "未" else {})
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
    if branch in ("丑", "寅", "卯", "辰", "巳", "午", "未"):
        index = get_collection_branch_group_index(branch)
        return {
            "edition": EDITION,
            "collection": f"{branch}集",
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
