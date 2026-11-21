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
        self.assertEqual(data["status"], "not_transcribed")
        self.assertEqual(data["entry_count"], 0)
        self.assertEqual(data["entries"], [])

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

    def test_group_index_contains_twenty_eight_groups_and_two_hundred_seventy_nine_entries(self):
        data = get_group_index()
        self.assertEqual(data["group_count"], 28)
        self.assertEqual(data["entry_count"], 279)
        self.assertEqual(
            [g["group_marker"] for g in data["groups"]],
            ["一〇八〇", "一〇九〇", "一一〇〇", "一一一〇", "一一二〇", "一一三〇", "一一四〇", "一一五〇", "一一六〇", "一一七〇", "一一八〇", "一一九〇", "一二〇〇", "一二二〇", "一二三〇", "一二四〇", "一二五〇", "一二六〇", "一二七〇", "一二八〇", "一三二〇", "一三三〇", "一三四〇", "一三五〇", "一三六〇", "一三八〇", "一四〇〇", "一四一〇"]
        )
        self.assertEqual([len(g["entries"]) for g in data["groups"]], [10] * 15 + [9] + [10] * 12)

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
        self.assertEqual(data["group_count"], 24)
        self.assertEqual(data["entry_count"], 239)
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
        self.assertEqual(data["unassigned_blocks"][1]["pdf_text_lines"], "11202-11213")
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
    def test_catalog_disclaims_ocr_verification_and_automatic_divination(self):
        data = get_collection_sample("子")
        joined = "；".join(data["limitations"])
        self.assertIn("OCR错误", joined)
        self.assertIn("不得用于自动考刻", joined)


if __name__ == "__main__":
    unittest.main()
