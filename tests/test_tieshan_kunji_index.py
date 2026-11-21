import unittest

from backend.tieshan_kunji_index import get_kunji_glossary


class KunjiGlossaryIndexTests(unittest.TestCase):
    def test_index_is_explicitly_not_a_cipher_or_full_clause_library(self):
        data = get_kunji_glossary()
        self.assertEqual(data["status"], "editorial_glossary_index_only")
        self.assertGreater(data["entry_count"], 80)
        self.assertIn("不是清刻本原始分类全貌", "；".join(data["limitations"]))
        self.assertIn("尚未取得各集完整条文", "；".join(data["limitations"]))

    def test_twelve_branch_collections_are_separate_and_ordered(self):
        rows = get_kunji_glossary()["twelve_branch_collections"]
        self.assertEqual([x["branch"] for x in rows], list("子丑寅卯辰巳午未申酉戌亥"))
        self.assertEqual([x["order"] for x in rows], list(range(1, 13)))
        self.assertEqual([x["printed_page_start"] for x in rows], [138, 172, 206, 240, 274, 308, 342, 376, 410, 444, 478, 512])
        you = next(x for x in rows if x["branch"] == "酉")
        self.assertIn("西集", you["source_variant"])

    def test_repeated_labels_keep_distinct_source_locations(self):
        rows = get_kunji_glossary()["entries"]
        repeated = [x for x in rows if x["term"] == "比"]
        self.assertGreaterEqual(len(repeated), 2)
        self.assertNotEqual(repeated[0]["lines"], repeated[1]["lines"])


if __name__ == "__main__":
    unittest.main()
