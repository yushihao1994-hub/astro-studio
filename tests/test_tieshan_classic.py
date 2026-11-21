import unittest

from backend.tieshan_classic import (
    BRANCH_NUMBER_CLASSES,
    DAY_MASTER_BRANCH_TO_TRIGRAM,
    HELUO_NUMBER_CLAUSES,
    LUOSHU_NUMBER_TO_TRIGRAM,
    STEM_TO_TRIGRAM,
    derive_classic_reference,
    derive_body_life_palaces,
)


class ClassicReferenceTests(unittest.TestCase):
    def test_stem_trigram_mapping(self):
        self.assertEqual(STEM_TO_TRIGRAM["甲"], "乾")
        self.assertEqual(STEM_TO_TRIGRAM["丙"], "艮")
        self.assertEqual(STEM_TO_TRIGRAM["丁"], "兑")

    def test_luoshu_number_to_trigram_is_separate(self):
        self.assertEqual(LUOSHU_NUMBER_TO_TRIGRAM[1], "坎")
        self.assertEqual(LUOSHU_NUMBER_TO_TRIGRAM[5], "中宫")
        self.assertEqual(LUOSHU_NUMBER_TO_TRIGRAM[9], "离")

    def test_day_master_branch_table(self):
        self.assertEqual(DAY_MASTER_BRANCH_TO_TRIGRAM["子"], "坎")
        self.assertEqual(DAY_MASTER_BRANCH_TO_TRIGRAM["未"], "坤")
        self.assertEqual(DAY_MASTER_BRANCH_TO_TRIGRAM["戌"], "乾")
        self.assertEqual(DAY_MASTER_BRANCH_TO_TRIGRAM["辰"], "巽")

    def test_heluo_preserves_source_overlap_for_ji(self):
        matches = [x["number"] for x in HELUO_NUMBER_CLAUSES if "己" in x["members"]]
        self.assertEqual(matches, [9, 4])

    def test_branch_number_classes(self):
        self.assertEqual(BRANCH_NUMBER_CLASSES["子"], (1, 6))
        self.assertEqual(BRANCH_NUMBER_CLASSES["卯"], (3, 8))
        self.assertEqual(BRANCH_NUMBER_CLASSES["未"], (5,))

    def test_body_life_palace_direction_and_source(self):
        result = derive_body_life_palaces(1, "子")
        self.assertEqual(result["month_palace"], "寅")
        self.assertEqual(result["life_palace"], "寅")
        self.assertEqual(result["body_palace"], "寅")
        result = derive_body_life_palaces(1, "丑")
        self.assertEqual(result["life_palace"], "丑")
        self.assertEqual(result["body_palace"], "卯")
        self.assertIn("闰月", " ".join(result["limitations"]))

    def test_leap_month_advances_one_additional_month(self):
        regular = derive_body_life_palaces(2, "子", False)
        leap = derive_body_life_palaces(2, "子", True)
        self.assertEqual(regular["month_palace"], "卯")
        self.assertEqual(leap["month_palace"], "辰")
        self.assertEqual(leap["effective_lunar_month_count"], 3)

    def test_eight_trigram_addition_is_registered_but_not_faked_as_algorithm(self):
        result = derive_classic_reference({"year":{"stem":"甲","branch":"子"}})
        rule = result["eight_trigram_addition"]
        self.assertEqual(rule["status"], "source_explained_not_executable")
        self.assertEqual(len(rule["clauses"]), 9)
        self.assertTrue(all(x["algorithm_status"] == "conceptual_only" for x in rule["clauses"]))

    def test_body_life_palace_validates_inputs(self):
        with self.assertRaises(ValueError):
            derive_body_life_palaces(0, "子")
        with self.assertRaises(ValueError):
            derive_body_life_palaces(3, "未知")

    def test_derived_data_labels_version_and_limits(self):
        pillars = {
            "year": {"stem": "甲", "branch": "子"},
            "month": {"stem": "己", "branch": "丑"},
            "day": {"stem": "丙", "branch": "寅"},
            "hour": {"stem": "丁", "branch": "卯"},
        }
        result = derive_classic_reference(pillars)
        self.assertEqual(result["lineage_status"], "secondary_compilation_reference_only")
        self.assertEqual(result["pillars"]["year"]["day_master_branch_trigram"], "坎")
        self.assertEqual(len(result["pillars"]["month"]["stem_heluo_clauses"]), 2)
        self.assertTrue(any("不能混为一张表" in x for x in result["limitations"]))


if __name__ == "__main__":
    unittest.main()
