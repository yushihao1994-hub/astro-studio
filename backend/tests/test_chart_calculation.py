import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import calculate_chart


class ChartCalculationRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chart = calculate_chart({
            "birth_date": "1994-05-26",
            "birth_time": "10:20",
            "place": "河南省周口市郸城县白马镇",
        })
        cls.planets = {item["name"]: item for item in cls.chart["planets"]}

    def test_birth_timezone_is_derived_from_location(self):
        self.assertEqual(self.chart["birth"]["timezone"], "Asia/Shanghai")
        self.assertEqual(self.chart["birth"]["utc_datetime"], "1994-05-26T02:20:00+00:00")

    def test_core_positions_and_houses_are_calculated(self):
        self.assertEqual(self.planets["太阳"]["sign"], "双子座")
        self.assertEqual(self.planets["太阳"]["house"], 10)
        self.assertEqual(self.planets["月亮"]["sign"], "射手座")
        self.assertEqual(self.planets["月亮"]["house"], 5)
        self.assertEqual(self.planets["金星"]["sign"], "巨蟹座")
        self.assertEqual(self.planets["金星"]["house"], 11)
        self.assertEqual(self.planets["火星"]["sign"], "金牛座")
        self.assertEqual(self.planets["火星"]["house"], 9)

    def test_water_grand_trine_is_detected(self):
        matches = [
            item for item in self.chart["patterns"]
            if item["name"] == "大三角"
            and set(item["planets"]) == {"金星", "木星", "土星"}
        ]
        self.assertTrue(matches, "应识别金星、木星、土星构成的水象大三角")

    def test_relationship_titles_and_plain_copy_stay_aligned(self):
        sections = self.chart["analysis"]["relationship"]["sections"]
        expected = [
            "容易被什么样的人吸引",
            "恋爱中需要怎样的相处节奏",
            "表达好感、推进关系和处理争执",
            "长期伴侣与婚姻：什么样的关系更能走得久",
            "亲密、信任与金钱边界",
            "需要警惕的感情盲点",
            "择偶时怎样判断是否适合结婚",
        ]
        self.assertEqual([item["title"] for item in sections[:7]], expected)
        self.assertTrue(all(item.get("plain_content") for item in sections))

    def test_every_visible_section_has_plain_language_content(self):
        report = self.chart["analysis"]
        all_sections = (
            report["relationship"]["sections"]
            + report["finance"]["sections"]
            + self.chart["natal_profile"]["sections"]
        )
        self.assertTrue(all(item.get("plain_content") for item in all_sections))


if __name__ == "__main__":
    unittest.main()
