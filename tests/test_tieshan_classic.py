import unittest

from backend.tieshan_classic import (
    BRANCH_TO_TRIGRAM,
    BRANCH_NUMBER_CLASSES,
    HELUO_NUMBER_BY_CHARACTER,
    STEM_TO_TRIGRAM,
    derive_classic_reference,
)


class ClassicReferenceTests(unittest.TestCase):
    def test_stem_trigram_mapping(self):
        self.assertEqual(STEM_TO_TRIGRAM["甲"], "乾")
        self.assertEqual(STEM_TO_TRIGRAM["丁"], "兑")
        self.assertEqual(STEM_TO_TRIGRAM["己"], "离")

    def test_branch_trigram_mapping_from_transcribed_verse(self):
        expected = {
            "亥": "坎", "子": "坎", "寅": "震", "巳": "离",
            "午": "离", "丑": "坤", "卯": "乾", "酉": "乾",
            "辰": "兑", "未": "艮", "申": "艮", "戌": "巽",
        }
        self.assertEqual(BRANCH_TO_TRIGRAM, expected)

    def test_heluo_number_classes(self):
        self.assertEqual(HELUO_NUMBER_BY_CHARACTER["甲"], 9)
        self.assertEqual(HELUO_NUMBER_BY_CHARACTER["亥"], 4)
        self.assertEqual(BRANCH_NUMBER_CLASSES["子"], (1, 6))
        self.assertEqual(BRANCH_NUMBER_CLASSES["未"], (5,))

    def test_result_does_not_claim_complete_lineage(self):
        pillars = {
            "year": {"stem": "甲", "branch": "子"},
            "month": {"stem": "己", "branch": "丑"},
            "day": {"stem": "丙", "branch": "寅"},
            "hour": {"stem": "丁", "branch": "卯"},
        }
        result = derive_classic_reference(pillars)
        self.assertEqual(result["lineage_status"], "secondary_compilation_reference_only")
        self.assertEqual(result["pillars"]["year"]["branch_trigram"], "坎")
        self.assertEqual(result["pillars"]["month"]["branch_trigram"], "坤")
        self.assertIn("尚未实现考刻", "；".join(result["limitations"]))


if __name__ == "__main__":
    unittest.main()
