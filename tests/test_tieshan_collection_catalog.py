import unittest

from backend.tieshan_collection_catalog import get_collection_sample


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

    def test_catalog_disclaims_ocr_verification_and_automatic_divination(self):
        data = get_collection_sample("子")
        joined = "；".join(data["limitations"])
        self.assertIn("OCR错误", joined)
        self.assertIn("不得用于自动考刻", joined)


if __name__ == "__main__":
    unittest.main()
