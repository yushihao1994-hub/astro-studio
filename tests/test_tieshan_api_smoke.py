import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "backend"))

import app as backend_app


class IronPlateApiSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        backend_app.app.config.update(TESTING=True)
        cls.client = backend_app.app.test_client()

    def test_health_endpoint_reports_expected_service(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["service"], "astro-studio-api")
        self.assertEqual(body["engine"], "pyswisseph-moshier")

    def test_lunar_months_endpoint_returns_month_options(self):
        response = self.client.get("/api/tieshan/calendar/months?year=2024")
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["year"], 2024)
        self.assertTrue(body["months"])
        self.assertTrue(all("value" in item and "days" in item for item in body["months"]))

    def test_lunar_months_rejects_invalid_year(self):
        response = self.client.get("/api/tieshan/calendar/months?year=not-a-year")
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.get_json()["ok"])

    def test_pillars_endpoint_calculates_known_birth_with_explicit_coordinates(self):
        response = self.client.post(
            "/api/tieshan/pillars",
            json={
                "birth_year": 1994,
                "birth_month": 5,
                "birth_day": 26,
                "birth_time": "10:20",
                "calendar": "solar",
                "gender": "男",
                "place": "河南省周口市郸城县白马镇",
                "latitude": 33.578217,
                "longitude": 115.514567,
                "timezone": "Asia/Shanghai",
            },
        )
        self.assertEqual(response.status_code, 200, response.get_json())
        body = response.get_json()
        self.assertTrue(body["ok"])
        self.assertEqual(set(("year", "month", "day", "hour")), set(body["pillars"]))
        self.assertTrue(body["birth"]["converted_solar_date"])
        self.assertIn("eight_ke", body)
        self.assertIn("iron_plate_engine", body)

    def test_pillars_endpoint_returns_clear_validation_error(self):
        response = self.client.post(
            "/api/tieshan/pillars",
            json={
                "birth_year": 1994,
                "birth_month": 2,
                "birth_day": 30,
                "birth_time": "10:20",
                "calendar": "solar",
                "latitude": 33.578217,
                "longitude": 115.514567,
                "timezone": "Asia/Shanghai",
            },
        )
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.get_json()["ok"])

    def test_ai_endpoint_uses_calculated_evidence_and_returns_report_shape(self):
        fake_report = {
            "summary": "测试摘要",
            "sections": [{"title": "性格", "conclusion": "测试结论", "reasoning": "测试依据", "advice": "测试建议"}],
            "limitations": ["仅为四柱基础文化解读"],
        }
        with patch.object(backend_app, "analyze_tieshan_profile", return_value=fake_report) as mocked:
            response = self.client.post(
                "/api/tieshan/analyze",
                json={
                    "pillars": {
                        "year": {"name": "甲戌"},
                        "month": {"name": "己巳"},
                        "day": {"name": "乙亥"},
                        "hour": {"name": "辛巳"},
                    },
                    "birth": {"date": "1994-05-26", "time": "10:20"},
                    "gender": "男",
                    "derived": {},
                },
            )
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["analysis_type"], "四柱基础文化解读")
        self.assertEqual(body["analysis"]["summary"], "测试摘要")
        mocked.assert_called_once()

    def test_finance_and_marriage_endpoints_use_dedicated_topics(self):
        fake_report = {
            "summary": "专项测试摘要",
            "sections": [
                {"title": "专题", "conclusion": "结论", "reasoning": "依据", "advice": "建议"}
                for _ in range(6)
            ],
            "limitations": ["四柱基础文化解读"],
        }
        pillars = {
            "year": {"name": "甲戌", "stem": "甲", "branch": "戌"},
            "month": {"name": "己巳", "stem": "己", "branch": "巳"},
            "day": {"name": "乙亥", "stem": "乙", "branch": "亥"},
            "hour": {"name": "辛巳", "stem": "辛", "branch": "巳"},
        }
        for topic, path, label in (
            ("finance", "/api/tieshan/finance", "财运专项预测"),
            ("marriage", "/api/tieshan/marriage", "婚姻专项预测"),
        ):
            with self.subTest(topic=topic):
                with patch.object(backend_app, "analyze_tieshan_topic", return_value=fake_report) as mocked:
                    response = self.client.post(
                        path,
                        json={"pillars": pillars, "birth": {}, "gender": "男", "derived": {}},
                    )
                self.assertEqual(response.status_code, 200, response.get_json())
                body = response.get_json()
                self.assertTrue(body["ok"])
                self.assertEqual(body["topic"], topic)
                self.assertEqual(body["analysis_type"], label)
                self.assertEqual(len(body["analysis"]["sections"]), 6)
                mocked.assert_called_once_with(topic, pillars, {}, "男", {})

    def test_hai_collection_endpoint_does_not_claim_unverified_groups(self):
        response = self.client.get("/api/tieshan/collections/亥/groups")
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertTrue(body["ok"])
        self.assertEqual(body["index"]["group_count"], 0)
        self.assertEqual(body["index"]["entry_count"], 0)


if __name__ == "__main__":
    unittest.main()
