import unittest
from datetime import date

from backend.chinese_calendar import lunar_month_options, lunar_to_solar, solar_to_lunar


class ChineseCalendarTests(unittest.TestCase):
    def test_lunar_to_solar_known_date(self):
        self.assertEqual(lunar_to_solar(1986, 4, 21), date(1986, 5, 29))

    def test_solar_to_lunar_round_trip(self):
        result = solar_to_lunar("1986-05-29")
        self.assertEqual((result["year"], result["month"], result["day"]), (1986, 4, 21))
        self.assertFalse(result["is_leap"])

    def test_leap_month_is_listed_as_negative_month(self):
        months = lunar_month_options(2023)
        self.assertEqual(len(months), 13)
        leap_months = [item for item in months if item["is_leap"]]
        self.assertEqual(len(leap_months), 1)
        self.assertEqual(leap_months[0]["month"], 2)
        self.assertEqual(leap_months[0]["value"], "-2")

    def test_normal_lunar_year_has_twelve_months(self):
        self.assertEqual(len(lunar_month_options(2024)), 12)

    def test_invalid_lunar_date_is_rejected(self):
        with self.assertRaises(ValueError):
            lunar_to_solar(2023, -2, 31)
        with self.assertRaises(ValueError):
            lunar_to_solar(2023, -7, 1)

    def test_supported_year_range_is_enforced(self):
        with self.assertRaises(ValueError):
            lunar_month_options(1800)


if __name__ == "__main__":
    unittest.main()
