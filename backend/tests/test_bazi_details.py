import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bazi_details import derive_bazi_details

class BaziDetailsTests(unittest.TestCase):
    def setUp(self):
        self.pillars = {
            "year":{"stem":"甲","branch":"子","index":0},
            "month":{"stem":"丙","branch":"寅","index":2},
            "day":{"stem":"甲","branch":"戌","index":10},
            "hour":{"stem":"己","branch":"巳","index":5},
        }
    def test_nayin(self):
        r=derive_bazi_details(self.pillars)
        self.assertEqual(r["pillars"]["year"]["nayin"],"海中金")
        self.assertEqual(r["pillars"]["month"]["nayin"],"炉中火")
    def test_void(self):
        r=derive_bazi_details(self.pillars)
        self.assertEqual(r["pillars"]["year"]["xun_void"],["戌","亥"])
        self.assertEqual(r["pillars"]["day"]["day_xun_void"],["申","酉"])
    def test_growth(self):
        r=derive_bazi_details(self.pillars)
        self.assertEqual(r["pillars"]["day"]["day_master_growth_stage"],"长生")
        self.assertEqual(r["pillars"]["year"]["day_master_growth_stage"],"帝旺")
    def test_incomplete(self):
        with self.assertRaises(ValueError):
            derive_bazi_details({"year":self.pillars["year"]})

if __name__ == "__main__": unittest.main()
