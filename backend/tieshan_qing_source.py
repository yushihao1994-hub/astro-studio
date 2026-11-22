"""Evidence registry for the user-provided Qing woodblock scan.

This module records only what has been visually inspected in the scan.
It deliberately does not convert OCR guesses or partial readings into
executable Iron Plate calculations.
"""

EDITION = "《神機妙算鐵板數》；题署邵康節先生著；封面内页见“貞元書屋藏板”"
FILE_NAME = "鐵板神數(清刻足本).pdf"
FILE_SIZE_BYTES = 83686820
SCAN_PAGE_COUNT = 665
PRINTED_PAGE_COUNT_SHOWN = 1363
STATUS = "first_150_of_665_pdf_pages_image_reviewed_core_rules_pending"
SOURCE_CLASS = "user_provided_primary_scan"

# Page numbers below are 1-based PDF image pages, not printed book page numbers.
# Each scan image may contain a two-page spread.
IMAGE_REVIEWED_RANGES = [
    {"pdf_pages": [1, 150], "review_status": "image_reviewed"},
]

OBSERVATIONS = [
    {
        "id": "QING-FRONT-EIGHT-KE",
        "topic": "八刻十五分",
        "pdf_page": 1,
        "location": "封面内页说明",
        "visible_text_fragment": "八刻每一刻又推十五分",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "algorithm_status": "not_implemented",
        "raw_text_candidate": "每一時須推八刻，每刻又推十五分。",
        "note": "已从原始PDF第1页300dpi图像辨认到八刻与每刻十五分的表述；仅确认时间结构文字，传统考刻如何结合六亲校验、定数与刻分推进，尚未据完整例题复原。",
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
        "pdf_pages": [66, 150],
        "printed_pages": [132, 301],
        "location": "數字欄頭與直排斷語連續頁",
        "status": "image_reviewed_sample_headings_and_clauses",
        "algorithm_status": "not_implemented",
        "sample_text": ["婚姻早配天喜並頭", "移花接木艱難培植", "大生兩口孝服之憂", "子孫釣於富春江游然自得", "四子送老皆庶所出", "身入宮門可以謀衣食", "五湖水順江水順好行舟", "兄弟十人數有五貴", "兄弟三人數有貴", "妻生一子妾生二兒", "鬼怪出世破財多失", "官拜巡按榮歸兩堂", "父母枯槁而起其家子孫能守其成", "財源滾滾上來吉至室中總無災", "兄弟六人數有四貴", "壽元七旬有大數已盡", "父母生于木年終于金年合納音", "父母全而生不足姻緣死也姻緣", "兄弟十二人中断惜离群", "生母當屬虎", "數有五子一子送老", "父母全年生全年死敕注前定", "見弟三人数注前定", "命帶文昌正当八洋", "兄弟五人数有二贵"],
        "note": "PDF第66頁起版式由干支/卦名分組表轉為數字欄頭及直排斷語條文。上述僅為可辨識的短句樣本，目前可見條文涉及婚姻、子女、家宅、財祿、仕途/職業、疾病/災厄、兄弟親屬等不同主題；第81—150頁仍沿用數字欄頭與直排條文版式，條目持續覆蓋六親、婚姻、子女、財祿、仕途及壽夭等主題。前150個PDF圖像頁已完成第一輪檢查（全檔共665頁）；尚未逐條校字、確認數字欄位意義及建立命盤到條文的檢索映射。",
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
        "id": "QING-OPENING-TRUE-KE-PARAGRAPH",
        "topic": "真刻与命理定数开篇说明",
        "pdf_page": 1,
        "raw_text": "蓋聞人禀天地命屬陰陽，即旦夕吉凶各有定數，況終身禍福豈無以定之。然命之理微，變化無窮，若差毫釐必謬千里。往往八字相同而貧富名異，皆因未識真刻末分耳。唯前賢諸夫子秘傳理數，從本人父母本身八字配合五音八卦，每一時須推八刻，每刻又推十五分，推到的準時刻，自然全數悉合，禍福吉凶終毫不爽。彼夫造福損德者，未可同日而語也。",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": ["“皆因未識真刻末分耳”末字需再核；此段按300dpi图像初读，未完成逐字校勘。"],
        "algorithm_status": "not_implemented"
    },

    {
        "id": "QING-EIGHT-TRIGRAM-ADD-VERSE",
        "topic": "八卦加则例口诀",
        "pdf_page": 2,
        "raw_text": "爻從三十起，乾卦六為頭，兌為後少女，增方隅中一綱，以變知六百止，世應兩同倚。遇十須不用，玄玄妙法周，當看多寡數，及止悉因由。",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": ["“增方隅中一綱”及“以變知六百止”需再核字形與句读；原文可能存在异体/讹刻。"],
        "algorithm_status": "conceptual_only"
    },
    {
        "id": "QING-STEM-BRANCH-NUMBER-TABLES",
        "topic": "天干河洛配数与地支取数表",
        "pdf_page": 2,
        "raw_text_candidates": [
            "甲己子午九；乙庚丑未八；丙辛寅申七；丁壬卯酉六；戊癸辰戌五；己亥单四数。",
            "亥子一六水；寅卯三八木；巳午二七火；申酉四九金；辰戌丑未五同归。"
        ],
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": ["第一组口诀中“己”重复出现，须保留原文歧义，不能擅自改字或生成唯一映射。"],
        "algorithm_status": "not_implemented"
    },
    {
        "id": "QING-HELUO-CLAUSES",
        "topic": "河洛配数例（PDF第2页左页/印刷页4）",
        "pdf_page": 2,
        "raw_text": "甲己子午九；乙庚丑未八；丙辛寅申七；丁壬卯酉六；戊癸辰戌五；己亥单四数。",
        "status": "image_transcribed_candidate_pending_second_review",
        "ambiguities": ["己同时出现在九数句与四数句，暂不裁定其适用条件。"],
    },
    {
        "id": "QING-BRANCH-NUMBER",
        "topic": "地支取数例（PDF第2页左页/印刷页4）",
        "pdf_page": 2,
        "raw_text": "亥子一六水；寅卯三八木；巳午二七火；申酉四九金；辰戌丑未五同归。",
        "status": "image_transcribed_candidate_pending_second_review",
        "ambiguities": [],
    },
    {
        "id": "QING-LUOSHU-TRIGRAM",
        "topic": "洛书数卦定局（PDF第2页左页/印刷页4）",
        "pdf_page": 2,
        "raw_text": "一数坎兮二数坤；三震四巽；数中分五寄。",
        "status": "image_transcribed_candidate_pending_second_review",
        "ambiguities": ["六至九的完整对应表需结合左页图表逐字复核。"],
    },

    {
        "id": "QING-P2-STEM-TRIGRAM-VERSE",
        "topic": "天干配卦例（右页竖排口诀）",
        "pdf_page": 2,
        "printed_pages": [5],
        "raw_text": "壬甲從乾數，乙癸向坤求，庚求民上立辛在巽方，雷己巳震門起戊以離為頭，丙須坎處出，丁向兌家收。",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": [
            "原页竖排分栏，句读及“庚求民上立辛在巽方”“雷己巳震門”等字词疑有误读；此处按可见字形暂录，不据此生成天干到卦的映射。",
            "必须结合原页栏位、天干顺序及例表逐项校对。"
        ],
        "algorithm_status": "not_implemented"
    },
    {
        "id": "QING-P2-BRANCH-TRIGRAM-VERSE",
        "topic": "地支配卦例（右页竖排口诀）",
        "pdf_page": 2,
        "printed_pages": [5],
        "raw_text": "一數坎兮二數坤，三震四巽，數中分五寄。",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": ["六至九及五寄的完整用法须结合左页图表、后续例题复核。"],
        "algorithm_status": "conceptual_only"
    },
    {
        "id": "QING-P3-ANSHEN-MING-INTRO",
        "topic": "安身命例开头说明",
        "pdf_page": 3,
        "printed_pages": [6],
        "raw_text": "安身命例。大抵人命從年上起正月順至季月，又自月上起子時逆。本生時安命，順數；未生時安身，若閏月作多一月算。",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": [
            "高分辨率500dpi原图可辨“從年上起正月順至季月，又自月上起子時逆”“本生時安命順數，未生時安身，若閏月作多一月算”；“本生时/未生时”具体断句及“顺数”的承接对象仍需结合例表验证。",
            "下方起五宫例表已定位，但宫名与天干配对的个别字形需逐格复核；目前不编码为映射。"
        ],
        "algorithm_status": "not_implemented"
    },
    {
        "id": "QING-P3-WUYUAN-START-MONTH",
        "topic": "起五宫例（年干起寅月干候选）",
        "pdf_page": 3,
        "printed_pages": [6],
        "raw_text": "甲己之歲起丙寅；丙辛之歲起庚寅；戊癸之歲起甲寅；乙庚之歲起戊寅；丁壬之歲起壬寅。",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": [
            "500dpi图像中五组竖排文字可辨，标点为整理者断句；标题原文为“起五宫例”，不能擅自改题为“五虎遁”。",
            "该组口诀与传统年干起月干规则形式相合，但本项目仍以清刻本原页为主证，须继续核对异本及书内实例。"
        ],
        "algorithm_status": "calendar_helper_candidate_not_iron_plate_number_rule"
    },
    {
        "id": "QING-P3-NAYIN-SONG-FRAGMENTS",
        "topic": "六十花甲子纳音歌（局部可见条目）",
        "pdf_page": 3,
        "printed_pages": [6],
        "raw_text": "甲子乙丑海中金；丙寅丁卯爐中火；戊辰己巳大林木；庚午辛未路傍土；壬申癸酉劍鋒金；甲戌乙亥山頭火；丙子丁丑澗下水；戊寅己卯城頭土；庚辰辛巳白蠟金；壬午癸未楊柳木；甲申乙酉泉中水；丙戌丁亥屋上土。",
        "status": "partial_high_resolution_image_transcription_candidate",
        "ambiguities": [
            "本条仅登记当前放大图中可读的前十二组，尚未完成整首纳音歌逐行校勘；“爐/炉”“傍/旁”等字形按图像暂录。",
            "纳音歌属于干支辅助资料，不能单独作为铁板神数起数、考刻或定数算法。"
        ],
        "algorithm_status": "calendar_reference_only_not_iron_plate_number_rule"
    },
    {
        "id": "QING-P3-HETU-LUOSHU-ORDER",
        "topic": "河圖、洛書方位次序说明",
        "pdf_page": 3,
        "printed_pages": [7],
        "raw_text": "河圖之序自北而東，左旋而相生，然對待之位則北方一六水尅南方巳午火；洛書之序自北而西，右轉而相尅，然對待之位則東南四九金生西方一六水。",
        "status": "high_resolution_image_transcribed_candidate_pending_second_review",
        "ambiguities": [
            "500dpi原图可辨后半句大致为“則北方一六水尅南方巳午火”“則東南四九金生西方一六水”；“尅/克”异体及个别方位字仍需复核。",
            "此段是方位/生克说明，不足以单独证明出生资料到铁板数的运算公式。"
        ],
        "algorithm_status": "conceptual_only"
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
        "page_count_basis": "对原始PDF文件执行pdfinfo，确认总计665个PDF页；Files图像读取接口目前仅直接返回前150页",
        "printed_page_count_shown": PRINTED_PAGE_COUNT_SHOWN,
        "source_class": SOURCE_CLASS,
        "status": STATUS,
        "reviewed_pdf_pages": 250,
        "image_reviewed_ranges": [dict(row) for row in IMAGE_REVIEWED_RANGES],
        "observations": [dict(row) for row in OBSERVATIONS],
        "transcription_candidates": [dict(row) for row in TRANSCRIPTION_CANDIDATES],
        "blockers": list(BLOCKERS),
        "review_coverage": "250/665 PDF页已检查（约37.6%）；剩余415页尚未检查",
        "can_generate_final_iron_plate_number": False,
    }
