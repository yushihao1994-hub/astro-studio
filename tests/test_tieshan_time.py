import unittest

from backend.tieshan_time import derive_eight_ke


class EightKeTests(unittest.TestCase):
    def test_first_and_last_zi_ke(self):
        first = derive_eight_ke("23:00", "子")
        self.assertEqual(first["ke_number"], 1)
        self.assertEqual(first["segment_start"], "23:00")
        self.assertEqual(first["segment_end"], "23:15")
        last = derive_eight_ke("00:59", "子")
        self.assertEqual(last["ke_number"], 8)
        self.assertEqual(last["segment_start"], "00:45")
        self.assertEqual(last["segment_end"], "01:00")

    def test_branch_boundary(self):
        self.assertEqual(derive_eight_ke("01:00", "丑")["ke_number"], 1)
        self.assertEqual(derive_eight_ke("03:00", "寅")["ke_number"], 1)
        self.assertEqual(derive_eight_ke("09:00", "巳")["ke_number"], 1)

    def test_mid_branch_quarter(self):
        result = derive_eight_ke("10:20", "巳")
        self.assertEqual(result["ke_number"], 6)
        self.assertEqual(result["segment_start"], "10:15")
        self.assertEqual(result["segment_end"], "10:30")
        self.assertEqual(result["status"], "clock_time_partition_only")

    def test_rejects_branch_mismatch(self):
        with self.assertRaises(ValueError):
            derive_eight_ke("10:20", "辰")

    def test_rejects_invalid_time(self):
        for value in ("24:00", "12:60", "abc", "9:00"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    derive_eight_ke(value, "午")


if __name__ == "__main__":
    unittest.main()
