import unittest

from backend.tieshan_collection_catalog import get_collection_sample, get_group_index


class TieshanCollectionCatalogTests(unittest.TestCase):
    def test_child_collection_sample_has_ten_source_located_records(self):
        data = get_collection_sample("子")
        self.assertEqual(data["status"], "sample_transcription_ocr_not_image_verified")
        self.assertEqual(data["entry_count"], 10)
        self.assertEqual([x["entry_sequence"] for x in data["entries"]], list(range(1, 11)))
        self.assertTrue(all(x["group_marker"] == "一〇八〇" for x in data["entries"]))
        self.assertTrue(all(x["pdf_text_lines"] for x in data["entries"]))

    def test_missing_corresponding_numbers_are_not_filled_in(self):
        data = get_collection_sample("子")
        self.assertIsNone(data["entries"][2]["raw_number_text"])
        self.assertIsNone(data["entries"][3]["raw_number_text"])
        self.assertIsNone(data["entries"][4]["raw_number_text"])

    def test_source_number_forms_are_preserved(self):
        data = get_collection_sample("子")
        self.assertEqual(data["entries"][0]["raw_number_text"], "卅四")
        self.assertEqual(data["entries"][1]["raw_number_text"], "卅三")
        self.assertIsNone(data["entries"][0]["printed_page"])

    def test_other_collections_are_not_fabricated(self):
        data = get_collection_sample("丑")
        self.assertEqual(data["status"], "partial_text_layer_index_image_verification_pending")
        self.assertEqual(data["entry_count"], 789)
        self.assertEqual(data["entries"], [])
        self.assertEqual(data["group_index"]["group_count"], 79)

    def test_age_markers_are_separate_lists_not_clause_numbers(self):
        data = get_collection_sample("子")
        self.assertTrue(all(isinstance(x["age_markers"], list) for x in data["entries"]))
        self.assertTrue(all(x["age_marker_text"] is None for x in data["entries"]))
        self.assertEqual(data["schema_version"], "0.2.0")

    def test_layout_patterns_keep_text_layer_evidence_and_unverified_status(self):
        data = get_collection_sample("子")
        patterns = data["layout_patterns"]
        ids = [x["pattern_id"] for x in patterns]
        self.assertIn("repeated_collection_headers", ids)
        self.assertIn("optional_corresponding_number", ids)
        self.assertIn("age_markers_are_independent", ids)
        self.assertTrue(all("image_check_pending" in x["status"] or
                            "page_image_verification" in x["status"]
                            for x in patterns))

    def test_group_index_contains_seventy_five_groups_and_seven_hundred_forty_seven_entries(self):
        data = get_group_index()
        self.assertEqual(data["group_count"], 75)
        self.assertEqual(data["entry_count"], 747)
        self.assertEqual(
            [g["group_marker"] for g in data["groups"]],
            ["一〇八〇", "一〇九〇", "一一〇〇", "一一一〇", "一一二〇", "一一三〇", "一一四〇", "一一五〇", "一一六〇", "一一七〇", "一一八〇", "一一九〇", "一二〇〇", "一二二〇", "一二三〇", "一二四〇", "一二五〇", "一二六〇", "一二七〇", "一二八〇", "一三二〇", "一三三〇", "一三四〇", "一三五〇", "一三六〇", "一三八〇", "一四〇〇", "一四一〇", "一四二〇", "一四三〇", "一四四〇", "一四五〇", "一四六〇", "一四八〇", "一四九〇", "一五〇〇", "一五一〇", "一五三〇", "一五四〇", "一五五〇", "一五六〇", "一六〇〇", "一六二〇", "一六三〇", "一六四〇", "一六五〇", "一六六〇", "一六七〇", "一七〇〇", "一七二〇", "一七三〇", "一七五〇", "一七六〇", "一七七〇", "一七八〇","一七九〇","一八〇〇","一八一〇","一八二〇","一八四〇","一八五〇","一八六〇","一八七〇","一八八〇","一八九〇","一九〇〇","一九一〇","一九三〇","一九四〇","一九五〇","一九六〇","一九七〇","一九八〇","一九九〇","二〇一〇"]
        )
        self.assertEqual([len(g["entries"]) for g in data["groups"]], [10] * 15 + [9] + [10] * 31 + [10,10,9,9,10,10,10] + [10] * 21)

    def test_1090_missing_number_fields_remain_empty(self):
        data = get_group_index()
        group = data["groups"][1]
        self.assertIsNone(group["entries"][1]["raw_number_text"])
        self.assertFalse(group["entries"][1]["number_field_present"])
        self.assertIsNone(group["entries"][8]["raw_number_text"])

    def test_inline_number_is_not_misclassified_as_corresponding_number(self):
        data = get_group_index()
        group = data["groups"][2]
        inline_number_entry = group["entries"][8]
        self.assertIsNone(inline_number_entry["raw_number_text"])
        self.assertFalse(inline_number_entry["number_field_present"])
        self.assertIn("条文句子内部含数字", inline_number_entry["note"])

    def test_group_index_preserves_pdf_line_references(self):
        data = get_group_index()
        self.assertEqual(data["groups"][1]["entries"][0]["pdf_text_lines"], "10682")
        self.assertEqual(data["groups"][2]["entries"][9]["pdf_text_lines"], "10704")

    def test_1110_to_1130_groups_keep_age_candidates_unassigned(self):
        data = get_group_index()
        self.assertEqual(data["group_count"], 75)
        self.assertEqual(data["entry_count"], 747)
        expected = {
            "一一一〇": {4: "五十三／五十四", 5: "五十七／五十八", 7: "三十三／三十四"},
            "一一二〇": {3: "四十九／五十七／五十五／五十八",
                        5: "三十三／三十四／三十七／三十八",
                        8: "四十五／四十六／四十九／五十"},
            "一一三〇": {1: "十五／十六／四十三／四十四",
                        5: "十三／十四／三十七／三十八",
                        6: "六十三／六十四", 8: "六十九／七十",
                        10: "三十三／三十四"},
        }
        for group in data["groups"][3:6]:
            self.assertEqual(group["layout_status"], "text_layer_located_layout_unverified")
            candidates = {x["entry_sequence_hint"]: x["raw_text"]
                          for x in group["age_marker_candidates"]}
            self.assertEqual(candidates, expected[group["group_marker"]])
            for entry in group["entries"]:
                self.assertIsNone(entry["number_field_present"])
                self.assertIsNone(entry["content_present"])
                if entry["age_marker_text"]:
                    self.assertEqual(entry["age_marker_association_status"],
                                     "needs_layout_verification")
                    self.assertEqual(entry["age_markers"], [])

    def test_1140_uses_distinct_sequence_age_clause_layout(self):
        data = get_group_index()
        group = data["groups"][6]
        self.assertEqual(group["group_marker"], "一一四〇")
        self.assertEqual(group["layout_status"],
                         "sequential_number_age_lines_then_clause")
        self.assertEqual(group["pdf_text_lines"], "10764-10809")
        expected = [
            ["四十九", "五十"], ["五十", "五十一"], ["五十二"],
            ["五十三"], ["五十四"], ["五十五"], ["五十六"],
            ["十七"], ["十八"], ["五十七", "五十八", "五十九"]
        ]
        self.assertEqual([e["age_markers"] for e in group["entries"]], expected)
        self.assertTrue(all(e["raw_number_text"] is None and
                            e["number_field_present"] is False
                            for e in group["entries"]))
        self.assertTrue(all(e["content_present"] is True and
                            e["age_marker_association_status"] ==
                            "text_layer_sequence_associated_image_check_pending"
                            for e in group["entries"]))

    def test_1150_reuses_sequence_age_clause_layout_with_optional_ages(self):
        data = get_group_index()
        group = data["groups"][7]
        self.assertEqual(group["group_marker"], "一一五〇")
        self.assertEqual(group["layout_status"],
                         "sequential_number_age_lines_then_clause")
        self.assertEqual(group["pdf_text_lines"], "10811-10858")
        expected = [
            [], ["三十五", "三十六"], ["五十七", "五十八", "五十九"],
            ["四十一", "四十二"], [], [],
            ["三十五", "三十六"], ["三十二", "三十三"],
            ["三十三", "三十四"], ["三十三", "三十四", "三十五", "三十六"]
        ]
        self.assertEqual([e["age_markers"] for e in group["entries"]], expected)
        self.assertTrue(all(e["number_field_present"] is False and
                            e["content_present"] is True
                            for e in group["entries"]))
        self.assertEqual(group["entries"][0]["age_marker_association_status"],
                         "age_not_listed_in_text_layer")

    def test_1160_reuses_sequence_age_clause_layout(self):
        data = get_group_index()
        group = data["groups"][8]
        self.assertEqual(group["group_marker"], "一一六〇")
        self.assertEqual(group["layout_status"],
                         "sequential_number_age_lines_then_clause")
        self.assertEqual(group["pdf_text_lines"], "10860-10902")
        expected = [
            [], ["三十七", "三十八"], ["三十九"], ["五十五", "五十六"],
            [], [], ["三十五", "三十六"], ["四十二", "四十三"],
            ["四十四", "四十五", "四十六"], ["五十八"]
        ]
        self.assertEqual([e["age_markers"] for e in group["entries"]], expected)
        self.assertTrue(all(e["number_field_present"] is False and
                            e["content_present"] is True
                            for e in group["entries"]))

    def test_new_group_line_ranges_are_group_level_only(self):
        data = get_group_index()
        self.assertEqual(
            [g["pdf_text_lines"] for g in data["groups"][3:7]],
            ["10707-10719", "10721-10741", "10743-10762", "10764-10809"]
        )
        self.assertTrue(all(e["pdf_text_lines"] is None
                            for g in data["groups"][3:6] for e in g["entries"]))


    def test_1170_to_1230_keep_ocr_markers_and_missing_1210_gap(self):
        data = get_group_index()
        self.assertEqual(data['groups'][9]['pdf_text_lines'], '10904-10917')
        self.assertEqual(data['groups'][9]['source_header_ocr']['raw_text'], '康节报具全书')
        self.assertEqual(data['groups'][9]['source_header_ocr']['normalized_candidate'], '康节说易全书')
        self.assertEqual(data['groups'][10]['raw_group_marker'], '一九〇')
        self.assertEqual(data['groups'][10]['normalized_group_marker_candidate'], '一一八〇')
        self.assertEqual(data['groups'][10]['normalization_status'], 'probable_ocr_correction_pending_image_check')
        self.assertEqual(data['groups'][11]['raw_group_marker'], '一九一')
        self.assertEqual(data['groups'][11]['normalized_group_marker_candidate'], '一一九〇')
        self.assertEqual(data['groups'][12]['pdf_text_lines'], '10944-10956')
        self.assertEqual(data['groups'][13]['pdf_text_lines'], '10958-10968')
        self.assertEqual(data['groups'][14]['pdf_text_lines'], '10970-10980')
        self.assertEqual(data['groups'][14]['age_marker_ambiguities'][0]['raw_token'], '三十作')
        self.assertIn('三十作', data['groups'][14]['entries'][4]['age_marker_text'])
        self.assertEqual(data['group_gaps'][0]['expected_group_marker'], '一二一〇')
        self.assertIn('do not fabricate', data['group_gaps'][0]['action'])


    def test_1240_to_1260_keep_table_source_column_uninterpreted(self):
        data = get_group_index()
        groups = data["groups"][15:18]
        self.assertEqual([g["layout_status"] for g in groups],
                         ["table_rows_year_sequence_clause"] * 3)
        self.assertEqual([len(g["entries"]) for g in groups], [9, 10, 10])
        self.assertEqual(groups[0]["entries"][0]["source_index_text"], "四十七／四十八")
        self.assertIsNone(groups[0]["entries"][0]["raw_number_text"])
        self.assertEqual(groups[1]["entries"][6]["source_index_text"],
                         "三十四／十三／五十三／十三")
        self.assertEqual(groups[2]["entries"][6]["source_index_text"],
                         "六十九／六十／三十三／三十三／五十三／五十四")
        self.assertTrue(all(e["age_markers"] == [] for g in groups for e in g["entries"]))
        self.assertTrue(all(e["number_field_present"] is None
                            for g in groups for e in g["entries"]))


    def test_1270_and_1280_age_markers_are_kept_in_source_order(self):
        data = get_group_index()
        g1270, g1280 = data["groups"][18:20]
        self.assertEqual(g1270["pdf_text_lines"], "11069-11109")
        self.assertEqual(g1270["entries"][0]["age_markers"],
                         ["三十六", "三十七", "三十九"])
        self.assertEqual(g1270["entries"][3]["age_markers"], ["五十七", "三十八"])
        self.assertEqual(g1270["entries"][9]["age_markers"], ["五十三", "五十四"])
        self.assertEqual(g1280["pdf_text_lines"], "11111-11151")
        self.assertEqual(g1280["entries"][5]["age_markers"],
                         ["五十五", "五十六", "三十二", "三十三", "三十三", "三十三", "三十四"])
        self.assertEqual(g1280["entries"][8]["age_markers"], ["四十五", "四十六"])
        self.assertTrue(all(e["raw_number_text"] is None
                            for g in (g1270, g1280) for e in g["entries"]))

    def test_unheaded_block_and_1290_to_1310_anomalies_are_not_fabricated(self):
        data = get_group_index()
        self.assertEqual(data["unassigned_blocks"][0]["pdf_text_lines"], "11028-11067")
        self.assertEqual(data["unassigned_blocks"][0]["entry_count"], 10)
        self.assertEqual(data["unassigned_blocks"][0]["status"],
                         "group_marker_missing_do_not_assign")
        anomalies = data["group_anomalies"]
        self.assertEqual(anomalies[0]["raw_group_marker"], "一二九〇")
        self.assertEqual(anomalies[2]["raw_group_marker"], "一二〇〇")
        self.assertEqual(anomalies[2]["normalized_group_marker_candidate"], "一三〇〇")
        self.assertEqual(anomalies[2]["status"],
                         "probable_ocr_correction_pending_image_check")
        self.assertEqual(anomalies[3]["expected_group_marker"], "一三一〇")

    def test_1320_and_1330_preserve_different_table_and_sequential_layouts(self):
        data = get_group_index()
        g1320, g1330 = data["groups"][20:22]
        self.assertEqual(g1320["layout_status"], "table_rows_year_sequence_clause")
        self.assertEqual(g1320["layout_note"], "PDF表头为“序号／干支/岁数／内容”；第二列原文值保留为来源字段，不解释成密码数。")
        self.assertEqual(g1320["entries"][8]["source_index_text"], "四十四／四十五")
        self.assertEqual(g1320["entries"][9]["source_index_text"], "三十七／三十八")
        self.assertEqual(g1330["layout_status"], "sequential_number_age_lines_then_clause")
        self.assertEqual(g1330["entries"][1]["age_markers"], ["三十五"])
        self.assertEqual(g1330["entries"][7]["age_markers"], ["三十七"])
        self.assertEqual(g1330["entries"][9]["age_markers"], ["四十七"])
        self.assertTrue(all(e["number_field_present"] is False and e["content_present"] is True for e in g1330["entries"]))

    def test_probable_1300_and_second_unheaded_block_remain_separate(self):
        data = get_group_index()
        candidate = data["candidate_groups"][0]
        self.assertEqual(candidate["raw_group_marker"], "一二〇〇")
        self.assertEqual(candidate["normalized_group_marker_candidate"], "一三〇〇")
        self.assertEqual(candidate["entries"][0]["raw_age_column_text"], "六十一")
        self.assertIsNone(candidate["entries"][7]["raw_age_column_text"])
        block = next(x for x in data["unassigned_blocks"] if x["block_id"] == "child_collection_unheaded_block_after_1320")
        self.assertEqual(block["pdf_text_lines"], "11202-11213")
        self.assertEqual(data["unassigned_blocks"][1]["entry_count"], 10)
    def test_1340_and_1350_keep_age_markers_and_no_number_column(self):
        data = get_group_index()
        g1340, g1350 = data["groups"][22:24]
        self.assertEqual(g1340["pdf_text_lines"], "11227-11238")
        self.assertEqual(g1340["entries"][0]["age_markers"], ["十", "三十七"])
        self.assertEqual(g1340["entries"][4]["age_markers"], ["九", "十七"])
        self.assertEqual(g1340["entries"][8]["age_markers"], ["三十九"])
        self.assertEqual(g1350["pdf_text_lines"], "11240-11252")
        self.assertTrue(all(e["age_markers"] == [] for e in g1350["entries"]))
        self.assertTrue(all(e["number_field_present"] is False and e["content_present"] is True
                            for g in (g1340, g1350) for e in g["entries"]))
    def test_1360_and_1380_keep_raw_ocr_labels_and_candidates(self):
        data = get_group_index()
        g1360, g1380 = data["groups"][24:26]
        self.assertEqual(g1360["raw_group_marker"], "二三六〇")
        self.assertEqual(g1360["group_marker"], "一三六〇")
        self.assertEqual(g1360["normalization_status"], "probable_ocr_correction_pending_image_check")
        self.assertEqual(g1360["pdf_text_lines"], "11254-11265")
        self.assertEqual(g1380["raw_group_marker"], "二三八〇")
        self.assertEqual(g1380["group_marker"], "一三八〇")
        self.assertEqual(g1380["pdf_text_lines"], "11267-11277")
        self.assertTrue(all(e["content_present"] is True for g in (g1360,g1380) for e in g["entries"]))
        self.assertTrue(all(e["age_markers"] == [] for g in (g1360,g1380) for e in g["entries"]))

    def test_1400_and_probable_1410_preserve_age_markers(self):
        data = get_group_index()
        g1400, g1410 = data["groups"][26:28]
        self.assertEqual(g1400["pdf_text_lines"], "11317-11354")
        self.assertEqual(g1400["entries"][3]["age_markers"], ["六十三","六十四","四十三","四十四"])
        self.assertEqual(g1400["entries"][5]["age_markers"], ["三十三","三十四","五十三","五十四"])
        self.assertEqual(g1410["raw_group_marker"], "一四〇")
        self.assertEqual(g1410["group_marker"], "一四一〇")
        self.assertEqual(g1410["entries"][7]["age_markers"], ["四十七","四十八"])
        self.assertTrue(all(e["number_field_present"] is False and e["content_present"] is True
                            for g in (g1400,g1410) for e in g["entries"]))

    def test_unheaded_block_after_1380_is_not_assigned_to_neighboring_group(self):
        data = get_group_index()
        block = next(x for x in data["unassigned_blocks"]
                     if x["block_id"] == "child_collection_unheaded_block_after_1380_candidate")
        self.assertEqual(block["entry_count"], 10)
        self.assertEqual(block["pdf_text_lines"], "11279-11315")
        anomalies = data["group_anomalies"]
        self.assertTrue(any(x.get("expected_group_marker") == "一三七〇" for x in anomalies))
        self.assertTrue(any(x.get("expected_group_marker") == "一三九〇" for x in anomalies))
    def test_1420_table_keeps_age_column_as_source_text(self):
        data = get_group_index()
        group = data["groups"][28]
        self.assertEqual(group["layout_status"], "table_rows_year_sequence_clause")
        self.assertEqual(group["entries"][0]["source_index_text"], "三十九")
        self.assertEqual(group["entries"][9]["source_index_text"], "四十二")
        self.assertIn("待页面图像核验", group["layout_note"])
        self.assertEqual(group["entries"][0]["pdf_text_lines"], "11394;11405")

    def test_1430_and_1440_keep_multiple_age_candidates_in_source_order(self):
        data = get_group_index()
        g1430, g1440 = data["groups"][29:31]
        self.assertEqual(g1430["entries"][3]["age_markers"], ["十","四十七","七十八","七十七"])
        self.assertEqual(g1430["entries"][5]["age_markers"], ["三十七","十八"])
        self.assertEqual(g1440["entries"][0]["age_markers"], ["八十九","九十"])
        self.assertEqual(g1440["entries"][4]["age_markers"], ["七十九","四十二"])
        self.assertEqual(g1440["entries"][9]["age_markers"], ["三十五","三十六"])

    def test_1450_and_1460_have_ten_source_located_entries_without_age_text(self):
        data = get_group_index()
        g1450, g1460 = data["groups"][31:33]
        self.assertEqual(g1450["pdf_text_lines"], "11489-11500")
        self.assertEqual(g1460["pdf_text_lines"], "11501-11511")
        self.assertTrue(all(e["age_markers"] == [] for g in (g1450,g1460) for e in g["entries"]))
        self.assertTrue(all(e["content_present"] is True for g in (g1450,g1460) for e in g["entries"]))

    def test_unheaded_block_after_1440_is_not_assigned(self):
        data = get_group_index()
        block = next(x for x in data["unassigned_blocks"]
                     if x["block_id"] == "child_collection_unheaded_block_after_1440")
        self.assertEqual(block["entry_count"], 10)
        self.assertEqual(block["pdf_text_lines"], "11476-11488")
    def test_1480_to_1500_table_index_preserves_source_numbers(self):
        data = get_group_index()
        g1480, g1490, g1500 = data["groups"][33:36]
        self.assertEqual(g1480["entries"][0]["source_index_text"], "十七")
        self.assertEqual(g1480["entries"][9]["source_index_text"], "五十四")
        self.assertEqual(g1490["entries"][7]["source_index_text"], "六十")
        self.assertEqual(g1500["entries"][0]["source_index_text"], "二十一")
        self.assertEqual(g1500["entries"][9]["source_index_text"], "四十八")

    def test_1510_1530_and_1550_keep_age_candidates_and_line_spans(self):
        data = get_group_index()
        g1510, g1530, g1550 = data["groups"][36], data["groups"][37], data["groups"][39]
        self.assertEqual(g1510["entries"][8]["age_markers"], ["三七十三","七十四"])
        self.assertEqual(g1510["entries"][8]["pdf_text_lines"], "11573-11574")
        self.assertEqual(g1530["entries"][8]["age_markers"], ["三十二","三十二","三十二"])
        self.assertEqual(g1530["entries"][9]["age_markers"], ["九百"])
        self.assertEqual(g1550["entries"][6]["age_markers"], ["三十六"])
        self.assertTrue(all(e["content_present"] is True for g in (g1510,g1530,g1550) for e in g["entries"]))

    def test_1520_ocr_candidate_and_1470_missing_content_are_not_promoted(self):
        data = get_group_index()
        candidate = next(x for x in data["candidate_groups"] if x["raw_group_marker"] == "二五二〇")
        self.assertEqual(candidate["normalized_group_marker_candidate"], "一五二〇")
        self.assertEqual(candidate["entries"][0]["raw_age_column_text"], "三十一")
        self.assertTrue(any(x.get("raw_group_marker") == "一四七〇" and
                            x["status"] == "group_marker_seen_content_not_located_before_next_header"
                            for x in data["group_anomalies"]))

    def test_unheaded_block_after_1530_remains_unassigned(self):
        data = get_group_index()
        block = next(x for x in data["unassigned_blocks"]
                     if x["block_id"] == "child_collection_unheaded_block_after_1530")
        self.assertEqual(block["entry_count"], 10)
        self.assertEqual(block["pdf_text_lines"], "11605-11625")

    def test_1560_group_keeps_sixteen_number_sequence_unassigned(self):
        data = get_group_index()
        group = next(g for g in data["groups"] if g["group_marker"] == "一五六〇")
        self.assertEqual(group["layout_status"], "layout_alignment_unresolved")
        self.assertEqual(len(group["unassigned_number_sequence"]["raw_values"]), 16)
        self.assertEqual(group["unassigned_number_sequence"]["pdf_text_lines"], "11687-11702")
        self.assertTrue(all(e["raw_number_text"] is None and e["content_present"] is True
                            for e in group["entries"]))
        self.assertEqual(group["entries"][-1]["pdf_text_lines"], "11713")


    def test_1560_unassigned_number_sequence_is_exposed_in_api_index(self):
        data = get_group_index()
        group = next(g for g in data["groups"] if g["group_marker"] == "一五六〇")
        self.assertEqual(len(group["unassigned_number_sequence"]["raw_values"]), 16)

    def test_1600_to_1660_groups_and_gaps_are_indexed_without_fabrication(self):
        data = get_group_index()
        by_marker = {g["group_marker"]: g for g in data["groups"]}
        markers = [by_marker[x]["group_marker"] for x in ["一六〇〇","一六二〇","一六三〇","一六四〇","一六五〇","一六六〇"]]
        self.assertEqual(markers, ["一六〇〇","一六二〇","一六三〇","一六四〇","一六五〇","一六六〇"])
        gaps = {g["expected_group_marker"] for g in data["group_gaps"]}
        self.assertIn("一六一〇", gaps)
        last_1660 = by_marker["一六六〇"]
        self.assertEqual(len(last_1660["entries"]), 10)
        self.assertTrue(all(e["raw_number_text"] is None for e in last_1660["entries"]))
        self.assertIn("child_collection_unheaded_block_after_1650",
                      {b["block_id"] for b in data["unassigned_blocks"]})
        anomalies = {a.get("raw_group_marker") for a in data["group_anomalies"]}
        self.assertIn("一六二〇", anomalies)
        self.assertIn("一六三", anomalies)

    def test_unheaded_blocks_and_1570_to_1590_ocr_candidates_stay_separate(self):
        data = get_group_index()
        ids = {x["block_id"] for x in data["unassigned_blocks"]}
        self.assertIn("child_collection_unheaded_block_after_1560", ids)
        self.assertIn("child_collection_unheaded_block_after_first_1560_orphan", ids)
        candidates = {x["raw_group_marker"]: x["normalized_group_marker_candidate"]
                      for x in data["candidate_groups"]}
        self.assertEqual(candidates["五七〇"], "一五七〇")
        self.assertEqual(candidates["五八〇"], "一五八〇")
        self.assertEqual(candidates["五九〇"], "一五九〇")

    def test_catalog_disclaims_ocr_verification_and_automatic_divination(self):
        data = get_collection_sample("子")
        joined = "；".join(data["limitations"])
        self.assertIn("OCR错误", joined)
        self.assertIn("不得用于自动考刻", joined)


    def test_1670_to_1770_keeps_marker_gaps_and_duplicates_separate(self):
        data = get_group_index()
        by = {g["group_marker"]: g for g in data["groups"]}
        self.assertEqual(by["一六七〇"]["pdf_text_lines"], "11928-11939")
        self.assertEqual(len(by["一七二〇"]["entries"]), 9)
        self.assertEqual(by["一七二〇"]["entries"][0]["entry_sequence"], 2)
        self.assertEqual(len(by["一七三〇"]["entries"]), 9)
        self.assertEqual(by["一七七〇"]["pdf_text_lines"], "12058-12068")
        gaps = {x["expected_group_marker"] for x in data["group_gaps"]}
        self.assertTrue({"一六八〇","一七一〇","一七四〇"}.issubset(gaps))
        candidates = {(x["raw_group_marker"],x["normalized_group_marker_candidate"]) for x in data["candidate_groups"]}
        self.assertIn(("一九〇","一六九〇"), candidates)
        self.assertIn(("一七〇〇","一七一〇"), candidates)
        self.assertIn("child_collection_unheaded_block_after_duplicate_1700",{x["block_id"] for x in data["unassigned_blocks"]})

    def test_late_child_collection_groups_keep_missing_markers_and_unheaded_section(self):
        data = get_group_index()
        by = {g["group_marker"]: g for g in data["groups"]}
        self.assertEqual(by["一八一〇"]["pdf_text_lines"], "12216-12264")
        self.assertEqual(by["一八九〇"]["age_marker_candidates"][0]["raw_text"], "九十岁")
        self.assertEqual(by["一九六〇"]["entries"][0]["raw_number_text"], "二十三")
        self.assertEqual(by["二〇一〇"]["entry_count"], 10)
        gaps = {x["expected_group_marker"] for x in data["group_gaps"]}
        self.assertTrue({"一八三〇","一九二〇","二〇〇〇","二〇二〇"}.issubset(gaps))
        blocks = {x["block_id"] for x in data["unassigned_blocks"]}
        self.assertIn("child_collection_unheaded_block_niu_yang_after_1990", blocks)


    def test_all_twelve_collection_starts_are_registered_without_claiming_transcription(self):
        from backend.tieshan_collection_catalog import get_collection_progress
        data = get_collection_progress()
        self.assertEqual([x["collection"] for x in data["collections"]], list("子丑寅卯辰巳午未申酉戌亥"))
        self.assertEqual([x["printed_page_start"] for x in data["collections"]], [138,172,206,240,274,308,342,376,410,444,478,512])
        self.assertTrue(all(x["toc_status"] == "located_in_contents" for x in data["collections"]))
        self.assertEqual(data["collections"][0]["indexed_groups"], 75)
        self.assertEqual(data["collections"][1]["index_status"], "partial_text_layer_index")
        self.assertEqual(data["collections"][1]["indexed_groups"], 79)
        self.assertEqual(data["collections"][1]["indexed_entries"], 789)
        self.assertEqual(data["collections"][2]["index_status"], "partial_text_layer_index")
        self.assertEqual(data["collections"][3]["index_status"], "partial_text_layer_index")
        self.assertEqual(data["collections"][4]["index_status"], "partial_text_layer_index")
        self.assertTrue(all(x["index_status"] == "not_transcribed" for x in data["collections"][5:]))
        self.assertEqual(data["collections"][4]["pdf_text_line_start"], 17109)
        self.assertEqual(data["collections"][4]["indexed_groups"], 58)
        self.assertEqual(data["collections"][4]["indexed_entries"], 579)
        self.assertEqual(data["collections"][3]["pdf_text_line_start"], 15797)
        self.assertEqual(data["collections"][3]["indexed_groups"], 78)
        self.assertEqual(data["collections"][3]["indexed_entries"], 779)
        self.assertEqual(data["collections"][2]["pdf_text_line_start"], 14175)
        self.assertEqual(data["collections"][2]["pdf_text_line_end"], 15796)
        self.assertEqual(data["collections"][2]["indexed_groups"], 72)
        self.assertEqual(data["collections"][2]["indexed_entries"], 719)
        self.assertEqual(data["collections"][0]["pdf_text_line_start"], 10664)
        self.assertEqual(data["collections"][0]["pdf_text_line_end"], 12570)
        self.assertEqual(data["collections"][1]["pdf_text_line_start"], 12572)
        self.assertEqual(data["collections"][1]["pdf_text_line_end"], 14174)

    def test_yin_collection_initial_groups_and_unassigned_sections(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index, get_collection_sample
        data = get_collection_branch_group_index("寅")
        self.assertEqual(data["group_count"], 72)
        self.assertEqual(data["entry_count"], 719)
        expected = [("三○一○",14177),("三○二○",14190),("三○三○",14218),
                    ("三○四○",14230),("三○六○",14257),("三○七○",14274)]
        for marker,line in expected:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
            self.assertEqual(len(group["entries"]), 10)
        self.assertIn("yin_special_section_shiji_before_3030",
                      {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertTrue(any(x["raw_group_marker"] == "三○八○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "三一四○" for x in data["group_anomalies"]))
        self.assertIn("yin_unheaded_entries_before_3120", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_unheaded_entries_before_2340", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_special_section_shiji_after_3260", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_unheaded_entries_before_3330_a", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_unheaded_entries_before_3330_b", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_unheaded_entries_before_3330_c", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertTrue(any(x["raw_group_marker"] == "三三五○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "三四一○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "三四七○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "三五六○" for x in data["group_anomalies"]))
        self.assertIn("yin_special_section_shiji_before_3390", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_special_section_shenji", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_special_section_shiji_after_3680", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_special_section_shiji_after_3740", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("yin_special_section_shiji_after_3860", {x["block_id"] for x in data["unassigned_blocks"]})
        for marker,line in [("三五七○",15087),("三五八○",15099),("三六○○",15127),
                            ("三六一○",15140),("三六二○",15153),("三六三○",15180),
                            ("三六四○",15193),("三六六○",15212),("三六七○",15226),
                            ("三六八○",15240),("三六九○",15267),("三七○○",15279),
                            ("三七二○",15296),("三七三○",15308),("三七四○",15320),
                            ("三七五○",15348),("三七六○",15360),("三七八○",15380),
                            ("三七九○",15381),("三八○○",15382),("三八一○",15397),
                            ("三八二○",15421),("三八四○",15437),("三八五○",15451),
                            ("三八六○",15469)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
        repeated_3580 = [g for g in data["groups"] if g["raw_group_marker"] == "三五八○"]
        self.assertEqual([g["group_header_pdf_line"] for g in repeated_3580], [15099,15112])
        self.assertEqual(next(g for g in data["groups"] if g["group_header_pdf_line"] == 15153)["entry_count"], 9)
        for marker,line in [("三三九○",14757),("三四○○",14810),("三四二○",14847),
                            ("三四三○",14859),("三四四○",14872),("三四五○",14899),
                            ("三四六○",14911),("三四八○",14940),("三四九○",14954),
                            ("三五○○",14966),("三五一○",14996),("三五二○",15020),
                            ("三五三○",15043),("三五四○",15058),("三五五○",15070)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
        repeated_3460 = [g for g in data["groups"] if g["raw_group_marker"] == "三四六○"]
        self.assertEqual([g["group_header_pdf_line"] for g in repeated_3460], [14911,14924])
        for marker,line in [("三二一○",14453),("三二二○",14465),("三二三○",14477),
                            ("二三四○",14501),("二三五○",14514),("三二七○",14543),
                            ("三二八○",14556),("三二九○",14569),("三三三○",14621),
                            ("三三四○",14633),("三三六○",14655),("三三七○",14668),
                            ("三三八○",14680)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
            self.assertEqual(len(group["entries"]), 10)
        for marker,line in [("三○九○",14293),("三一○○",14306),("三一一○",14318),
                            ("三一二○",14343),("三一三○",14356),("三一五○",14372),
                            ("三一六○",14384),("三一七○",14396),("三一八○",14413),
                            ("三一九○",14426),("三二○○",14438)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
            self.assertEqual(len(group["entries"]), 10)
        sample = get_collection_sample("寅")
        self.assertEqual(sample["collection"], "寅集")
        self.assertEqual(sample["group_index"]["group_count"], 72)

    def test_mao_collection_initial_groups_and_gaps(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index, get_collection_sample
        data = get_collection_branch_group_index("卯")
        self.assertEqual(data["group_count"], 78)
        self.assertEqual(data["entry_count"], 779)
        expected = [("四○八○",15791),("四○九○",15809),("四一○○",15822),
                    ("四一二○",15836),("四一三○",15858),("四一五○",15884),
                    ("四一六○",15897),("四一八○",15924),("四一九○",15936),
                    ("四二○○",15949),("四二一○",15963),("四二二○",15976),
                    ("四二四○",15992),("四二五○",16004),("四二六○",16016)]
        for marker,line in expected:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
            self.assertEqual(len(group["entries"]), 10)
        self.assertEqual(len(data["unassigned_blocks"]), 12)
        self.assertTrue(any(x["raw_group_marker"] == "四二三○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "四三二○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "四四五○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "四五三○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "四五五○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "四五六○" for x in data["group_anomalies"]))
        self.assertIn("mao_bp_collection_subsection", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("mao_unheaded_table_after_4510", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("mao_possible_4550_table_a", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("mao_possible_4560_table_b", {x["block_id"] for x in data["unassigned_blocks"]})
        for block in ["mao_unheaded_entries_before_4690","mao_unheaded_entries_before_4750",
                      "mao_unheaded_entries_before_4780","mao_unheaded_entries_after_guaji"]:
            self.assertIn(block, {x["block_id"] for x in data["unassigned_blocks"]})
        for marker,line in [("四六四○",16563),("四六六",16580),("四六七",16592),
                            ("四六八",16604),("四六九○",16632),("四七○○",16646),
                            ("四七二○",16664),("四七三○",16677),("四七三○",16690),
                            ("四七五○",16720),("四七六○",16733),("四七八○",16760),
                            ("四七九○",16772)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
            self.assertEqual(len(group["entries"]), 10)
        for marker,line in [("四二七○",16046),("四二八○",16060),("四二九○",16075),
                            ("四三○○",16090),("四三一○",16102),("四三三○",16120),
                            ("四三四○",16132),("四三五○",16143),("四三六○",16157),
                            ("四三七○",16167),("四三二○",16177),("四三九○",16194),
                            ("四四○○",16209),("四四一○",16223),("四四二○",16252),
                            ("四四三○",16264),("四四四○",16277),("四四六○",16292),
                            ("四四七○",16303),("四四八○",16317),("四四九○",16330)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
        self.assertEqual(next(g for g in data["groups"] if g["group_header_pdf_line"] == 16060)["entry_count"], 9)
        for marker,line in [("四四九○",16342),("四五一○",16359),("四五二○",16385),
                            ("四五四○",16407),("四五七○",16451),("四五八○",16464),
                            ("四五九○",16476),("四六○",16496),("四六一",16509),
                            ("四六二",16521),("四六三○",16539),("四六四○",16551)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
            self.assertEqual(len(group["entries"]), 10)
        self.assertIn("mao_possible_4890_group_body", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertTrue(any(x["raw_group_marker"] == "四九二○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "五○○○" for x in data["group_anomalies"]))
        for marker,line in [("四八一○",16799),("四八二○",16812),("四八三○",16824),
                            ("四八四○",16839),("四八五○",16851),("四八六○",16864),
                            ("四八七○",16882),("四八八○",16895),("四九○○",16926),
                            ("四九一○",16949),("四九三○",16995),("四九四○",17021),
                            ("四九五○",17035),("四九六○",17053),("四九七○",17065),
                            ("四九八○",17078),("四九九○",17092)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
        sample = get_collection_sample("卯")
        self.assertEqual(sample["collection"], "卯集")
        self.assertEqual(sample["group_index"]["group_count"], 78)

    def test_chen_collection_initial_groups_and_unassigned_block(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index, get_collection_sample
        data = get_collection_branch_group_index("辰")
        self.assertEqual(data["group_count"], 58)
        self.assertEqual(data["entry_count"], 579)
        expected = [("五○一○",17112),("五○二○",17168),("五○三○",17244),
                    ("五○四○",17257),("五○六○",17273),("五○七○",17298),
                    ("五○八○",17311),("五○九○",17329),("五一○○",17342),
                    ("五一二○",17358),("五一三○",17369),("五一四○",17381),
                    ("五三三○",17653),("五三四○",17666),("五三五○",17678),
                    ("五三六○",17693),("五三七○",17705),("五三八○",17718),
                    ("五三九○",17745),("五四○○",17770),("五四一○",17795),
                    ("五四三○",17822),("五四四○",17837),("五四五○",17851),
                    ("五四六○",17864),("五四七○",17876),("五四八○",17895),("五四九○",17906)]
        for marker,line in expected:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
        self.assertEqual(next(g for g in data["groups"] if g["group_header_pdf_line"] == 17112)["entry_count"], 9)
        self.assertTrue(any(x["raw_group_marker"] == "五○五○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "五二○○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "五二六○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "五三二○" for x in data["group_anomalies"]))
        for block in ["chen_unheaded_ten_entries_before_5030","chen_unheaded_ten_entries_after_5230","chen_unheaded_ten_entries_before_5330"]:
            self.assertIn(block, {x["block_id"] for x in data["unassigned_blocks"]})
        for marker,line in [("五一五○",17411),("五一六○",17425),("五一七○",17436),
                            ("五一八○",17453),("五一九○",17465),("五二一○",17483),
                            ("五二二○",17496),("五二三○",17508),("五二四○",17535),
                            ("五二五○",17548),("五二七○",17564),("五二八○",17576),
                            ("五二九○",17588),("五三○○",17616),("五三一○",17628)]:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
        self.assertIn("chen_unheaded_ten_entries_before_5030",
                      {x["block_id"] for x in data["unassigned_blocks"]})
        sample = get_collection_sample("辰")
        self.assertEqual(sample["collection"], "辰集")
        self.assertEqual(sample["group_index"]["group_count"], 58)

    def test_collection_progress_exposes_chou_text_range_and_indexed_groups(self):
        from backend.tieshan_collection_catalog import get_collection_progress
        data = get_collection_progress()
        chou = next(x for x in data["collections"] if x["collection"] == "丑")
        self.assertEqual(chou["index_status"], "partial_text_layer_index")
        self.assertEqual(chou["indexed_groups"], 79)
        self.assertEqual(chou["indexed_entries"], 789)
        self.assertEqual(chou["pdf_text_line_start"], 12572)
        self.assertEqual(chou["pdf_text_line_end"], 14174)
        zi = next(x for x in data["collections"] if x["collection"] == "子")
        self.assertEqual(zi["indexed_groups"], 75)
        self.assertEqual(zi["indexed_entries"], 747)

    def test_chou_index_through_2350_is_indexed_without_transcribing_clause_text(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index, get_collection_progress
        data = get_collection_branch_group_index("丑")
        self.assertEqual(data["group_count"], 79)
        self.assertEqual(data["entry_count"], 789)
        self.assertEqual(data["groups"][0]["raw_group_marker"], "二○三○")
        self.assertEqual(data["groups"][0]["pdf_text_lines"], "12576-12586")
        raw_260 = next(g for g in data["groups"] if g["group_header_pdf_line"] == 12798)
        self.assertEqual(raw_260["raw_group_marker"], "二六○")
        self.assertEqual(raw_260["pdf_text_lines"], "12798-12809")
        for marker, line in [("二一八○",12824),("二一九○",12836),("二二一○",12851),("二二二○",12863),("二二五○",12906),("二二六○",12919)]:
            self.assertEqual(next(g for g in data["groups"] if g["group_header_pdf_line"] == line)["raw_group_marker"], marker)
        repeated_2230 = [g for g in data["groups"] if g["raw_group_marker"] == "二二三○"]
        repeated_2240 = [g for g in data["groups"] if g["raw_group_marker"] == "二二四○"]
        self.assertEqual([g["occurrence"] for g in repeated_2230], [1,2])
        self.assertEqual([g["occurrence"] for g in repeated_2240], [1,2])
        group_2350 = next(g for g in data["groups"] if g["group_header_pdf_line"] == 13044)
        self.assertEqual(group_2350["raw_group_marker"], "二三五○")
        self.assertEqual(len(group_2350["entries"]), 10)
        for marker, line in [("二三六○",13077),("二三七○",13101),("二三八○",13125)]:
            g = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(g["raw_group_marker"], marker)
            self.assertEqual(len(g["entries"]), 10)
            self.assertTrue(all(e.get("record_span") for e in g["entries"]))
        self.assertTrue(all("content" not in entry for group in data["groups"] for entry in group["entries"]))
        progress = get_collection_progress()
        chou = next(x for x in progress["collections"] if x["collection"] == "丑")
        self.assertEqual((chou["indexed_groups"], chou["indexed_entries"]), (79, 789))


    def test_chou_repeated_markers_and_2250_2260_are_separately_indexed(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index
        data = get_collection_branch_group_index("丑")
        groups = data["groups"]
        repeated_2230 = [g for g in groups if g["raw_group_marker"] == "二二三○"]
        repeated_2240 = [g for g in groups if g["raw_group_marker"] == "二二四○"]
        self.assertEqual([g["group_header_pdf_line"] for g in repeated_2230], [12744, 12875])
        self.assertEqual([g["group_header_pdf_line"] for g in repeated_2240], [12757, 12894])
        group_2250 = next(g for g in groups if g["raw_group_marker"] == "二二五○")
        group_2260 = next(g for g in groups if g["raw_group_marker"] == "二二六○")
        self.assertEqual(group_2250["group_header_pdf_line"], 12906)
        self.assertEqual(group_2260["group_header_pdf_line"], 12919)
        later = {g["raw_group_marker"]: g for g in groups if g["raw_group_marker"] in {"二三○○","二三一○","二三二○","二三三○","二三四○","二三五○"}}
        self.assertEqual(set(later), {"二三○○","二三一○","二三二○","二三三○","二三四○","二三五○"})
        self.assertEqual(later["二三○○"]["pdf_text_lines"], "12969-12978")
        self.assertEqual(later["二三三○"]["pdf_text_lines"], "13019-13030")
        self.assertEqual(later["二三五○"]["pdf_text_lines"], "13044-13076")
        self.assertEqual(later["二三五○"]["entries"][9]["record_span"], "13074-13076")
        anomalies = data["group_anomalies"]
        self.assertTrue(any(x["raw_group_marker"] == "二五○" and x["normalized_group_marker_candidate"] is None for x in anomalies))
        self.assertTrue(any(x["raw_group_marker"] == "二六○" and x["normalized_group_marker_candidate"] is None for x in anomalies))
        self.assertEqual(len(data["unassigned_blocks"]), 12)
        self.assertTrue(all(x["status"] in {"group_marker_missing_do_not_assign","group_boundary_ambiguous_do_not_promote"} for x in data["unassigned_blocks"]))
        self.assertIn("chou_unheaded_entries_before_2330", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("chou_possible_2390_group_body", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("chou_possible_2400_group_body", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("chou_possible_2680_group_body", {x["block_id"] for x in data["unassigned_blocks"]})
        for marker, line in [("二六一",13487),("二六○",13499),("二六二",13511),("二六三○",13546),("二六五○",13617),("二六六○",13642),("二六七○",13664),("二六九○",13699),("二七○○",13712)]:
            g = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(g["raw_group_marker"], marker)
            self.assertEqual(len(g["entries"]), 10)
        self.assertTrue(any(x["raw_group_marker"] == "二六四○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "二七四○" for x in data["group_anomalies"]))
        self.assertIn("chou_possible_2710_group_body", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("chou_possible_2890_group_body", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("chou_unheaded_entries_after_292", {x["block_id"] for x in data["unassigned_blocks"]})
        self.assertIn("chou_unheaded_entries_before_2990", {x["block_id"] for x in data["unassigned_blocks"]})
        for marker, line in [("二九○",14044),("二九二",14055),("二九三○",14082),("二九四○",14094),("二九六○",14111),("二九七○",14123),("二九八○",14136),("二九九○",14161)]:
            g = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(g["raw_group_marker"], marker)
            self.assertEqual(len(g["entries"]), 10)
        for marker, line in [("二七二○",13749),("二七三○",13773),("二七五○",13802),("二七六○",13813),("二七七○",13826),("二七八○",13840),("二七九○",13853),("二八○○",13865),("二八一○",13880),("二八二○",13906),("二八三○",13920),("二八四○",13933),("二八五○",13945),("二八六○",13956),("二八七○",13982),("二八八○",14005)]:
            g = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(g["raw_group_marker"], marker)
        group_2750 = next(g for g in data["groups"] if g["group_header_pdf_line"] == 13802)
        self.assertEqual(group_2750["entry_count"], 9)
        for marker, line in [("二四二○",13233),("二四三○",13247),("二四四○",13261),("二四五○",13279),("二四六○",13291),("二四七○",13303),("二四八○",13331),("二四九○",13344),("二五一○",13360),("二五二○",13373),("二五三○",13385),("二五四○",13410),("二五五○",13423),("二五七○",13443),("二五八○",13457),("二五九○",13471)]:
            g = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(g["raw_group_marker"], marker)
            self.assertEqual(len(g["entries"]), 10)

if __name__ == "__main__":
    unittest.main()




class ChouRawMarker2260Tests(unittest.TestCase):
    def test_raw_short_marker_is_indexed_without_normalization(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index
        data = get_collection_branch_group_index("丑")
        group = next(g for g in data["groups"] if g["raw_group_marker"] == "二六○")
        self.assertEqual(group["group_header_pdf_line"], 12798)
        self.assertEqual(group["pdf_text_lines"], "12798-12809")
        self.assertIsNone(group["normalized_group_marker_candidate"])
        self.assertEqual(len(group["entries"]), 10)
        self.assertTrue(all(e["pdf_text_line"] is None for e in group["entries"]))
        self.assertIn("chou_unheaded_entries_after_raw_marker_二六○",
                      {b["block_id"] for b in data["unassigned_blocks"]})


class ChenCollectionIndexTests(unittest.TestCase):
    def test_chen_first_batch_preserves_partial_and_unheaded_records(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index, get_collection_progress
        data = get_collection_branch_group_index("辰")
        self.assertEqual(data["group_count"], 44)
        self.assertEqual(data["entry_count"], 439)
        first = next(g for g in data["groups"] if g["raw_group_marker"] == "五○一○")
        self.assertEqual(first["entry_count"], 9)
        self.assertEqual([e["entry_sequence"] for e in first["entries"]], list(range(2, 11)))
        self.assertTrue(any(g["raw_group_marker"] == "五二三○" for g in data["groups"]))
        self.assertTrue(any(x["raw_group_marker"] == "五○五○" for x in data["group_anomalies"]))
        self.assertTrue(any(x["raw_group_marker"] == "五二○○" for x in data["group_anomalies"]))
        blocks = {x["block_id"] for x in data["unassigned_blocks"]}
        self.assertIn("chen_unheaded_ten_entries_before_5030", blocks)
        self.assertIn("chen_unheaded_ten_entries_before_5330", blocks)
        progress = get_collection_progress()
        chen = next(x for x in progress["collections"] if x["collection"] == "辰")
        self.assertEqual((chen["indexed_groups"], chen["indexed_entries"]), (58, 579))


class ChenCollectionIndexThrough5650Tests(unittest.TestCase):
    def test_later_chen_groups_and_5590_missing_body_are_registered(self):
        from backend.tieshan_collection_catalog import get_collection_branch_group_index
        data = get_collection_branch_group_index("辰")
        expected = [("五五一○",17926),("五五二○",17938),("五五三○",17950),
                    ("五五四○",17963),("五五五○",17975),("五五六○",17986),
                    ("五五七○",18011),("五五八○",18023),("五六○○",18045),
                    ("五六一○",18059),("五六二○",18073),("五六三○",18090),
                    ("五六四○",18102),("五六五○",18114)]
        for marker, line in expected:
            group = next(g for g in data["groups"] if g["group_header_pdf_line"] == line)
            self.assertEqual(group["raw_group_marker"], marker)
            self.assertEqual(len(group["entries"]), 10)
        self.assertTrue(any(x["raw_group_marker"] == "五五九○" for x in data["group_anomalies"]))
