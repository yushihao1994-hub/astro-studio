import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend"))
from tieshan_engine import build_tieshan_foundation, ENGINE_VERSION

class TieshanFoundationEngineTests(unittest.TestCase):
    def setUp(self):
        self.pillars = {
            "year":{"name":"甲戌","stem":"甲","branch":"戌"},
            "month":{"name":"己巳","stem":"己","branch":"巳"},
            "day":{"name":"甲子","stem":"甲","branch":"子"},
            "hour":{"name":"己巳","stem":"己","branch":"巳"},
        }
    def test_engine_never_claims_final_number(self):
        r=build_tieshan_foundation({},self.pillars)
        self.assertEqual(r["overall_status"],"foundation_only")
        self.assertFalse(r["can_generate_final_iron_plate_number"])
        self.assertEqual(r["engine_version"],ENGINE_VERSION)
    def test_unverified_stages_are_blocked(self):
        r=build_tieshan_foundation({},self.pillars)
        status={x["key"]:x["status"] for x in r["workflow"]}
        self.assertEqual(status["start_number"],"blocked")
        self.assertEqual(status["six_relatives"],"blocked")
        self.assertEqual(status["cipher_lookup"],"blocked")
    def test_verified_inputs_are_preserved(self):
        r=build_tieshan_foundation({"timezone":"Asia/Shanghai"},self.pillars,{"ke_label":"巳时第2刻"},{"life_palace":"寅"},{"pillars":{"year":{}}})
        self.assertTrue(r["available_foundations"]["eight_ke"])
        self.assertTrue(r["available_foundations"]["body_life_palaces"])
        self.assertEqual(r["four_pillars"]["year"]["name"],"甲戌")
        self.assertEqual(next(x for x in r["workflow"] if x["key"]=="classic_tables")["status"],"partial")
    def test_requires_four_pillars(self):
        with self.assertRaises(ValueError):
            build_tieshan_foundation({}, {"year":self.pillars["year"]})

if __name__ == "__main__": unittest.main()