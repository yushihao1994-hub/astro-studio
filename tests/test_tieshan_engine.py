import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "backend"))
from tieshan_engine import build_tieshan_foundation, ENGINE_VERSION, PRIMARY_REFERENCE, QING_REFERENCE_STATUS, is_kaoke_attestation_trusted
from tieshan_qing_source import get_qing_source_reference

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
    def test_kunji_editorial_metadata_is_available_but_cipher_stays_blocked(self):
        r=build_tieshan_foundation({},self.pillars)
        kunji=r["available_foundations"]["kunji_reference"]
        self.assertEqual(kunji["status"],"partial_metadata_not_full_cipher")
        self.assertEqual(len(kunji["published_examples"]),7)
        rule_ids={x["id"] for x in r["rule_registry"]}
        self.assertIn("KUNJI-CIPHER-EDITORIAL",rule_ids)
        self.assertIn("QIAN-EIGHT-TRIGRAM-ADD",rule_ids)
        status={x["key"]:x["status"] for x in r["workflow"]}
        self.assertEqual(status["cipher_lookup"],"blocked")
        self.assertFalse(r["can_generate_final_iron_plate_number"])

    def test_qing_scan_is_primary_but_not_verified_for_calculation(self):
        source=get_qing_source_reference()
        self.assertEqual(source["source_class"],"user_provided_primary_scan")
        self.assertEqual(source["scan_page_count"],665)
        self.assertEqual(source["reviewed_pdf_pages"],665)
        self.assertIn({"pdf_pages":[151,250],"review_status":"layout_and_section_continuity_reviewed_transcription_pending"},source["image_reviewed_ranges"])
        self.assertIn({"pdf_pages":[251,350],"review_status":"layout_and_section_continuity_reviewed_transcription_pending"},source["image_reviewed_ranges"])
        self.assertIn("665/665",source["review_coverage"])
        self.assertIn({"pdf_pages":[351,450],"review_status":"layout_and_section_continuity_reviewed_transcription_pending"},source["image_reviewed_ranges"])
        self.assertIn({"pdf_pages":[451,550],"review_status":"layout_and_section_continuity_reviewed_transcription_pending"},source["image_reviewed_ranges"])
        self.assertIn({"pdf_pages":[551,650],"review_status":"layout_and_section_continuity_reviewed_transcription_pending"},source["image_reviewed_ranges"])
        self.assertIn({"pdf_pages":[651,665],"review_status":"layout_and_section_continuity_reviewed_transcription_pending"},source["image_reviewed_ranges"])
        self.assertIn("665/665",source["review_coverage"])
        self.assertIn("清刻",PRIMARY_REFERENCE)
        self.assertIn("待",QING_REFERENCE_STATUS)
        self.assertFalse(source["can_generate_final_iron_plate_number"])
        r=build_tieshan_foundation({},self.pillars)
        self.assertEqual(r["available_foundations"]["qing_source_reference"]["status"],source["status"])
        self.assertEqual(r["overall_status"],"foundation_only")
        candidates=source.get("transcription_candidates",[])
        self.assertIn("QING-HELUO-CLAUSES",{x["id"] for x in candidates})
        self.assertIn("己亥单四数",next(x for x in candidates if x["id"]=="QING-HELUO-CLAUSES")["raw_text"])


    def test_modern_qianji_rules_are_never_mislabeled_as_qing_verified(self):
        r=build_tieshan_foundation({},self.pillars)
        qian=[x for x in r["rule_registry"] if x["id"].startswith("QIAN-")]
        self.assertTrue(qian)
        self.assertTrue(all(x["status"].startswith("modern_comparator_only") for x in qian))
        self.assertTrue(all(x.get("source_kind") == "modern_edition_comparator" for x in qian))
        qing=[x for x in r["rule_registry"] if x["id"].startswith("QING-")]
        self.assertTrue(qing)
        self.assertFalse(any(x["status"] == "verified_table" for x in qing))


    def test_client_cannot_forge_verified_kaoke_attestation(self):
        forged={"status":"verified","number":"1234","source":"client"}
        self.assertFalse(is_kaoke_attestation_trusted(forged))
        self.assertFalse(is_kaoke_attestation_trusted({"status":"verified"}))
        self.assertFalse(is_kaoke_attestation_trusted(None))


    def test_opening_page_transcriptions_are_traceable_but_not_executable(self):
        source=get_qing_source_reference()
        candidates={x["id"]:x for x in source["transcription_candidates"]}
        expected={
            "QING-HELUO-CLAUSES",
            "QING-EIGHT-TRIGRAM-ADD-VERSE",
            "QING-P3-ANSHEN-MING-INTRO",
            "QING-P3-HETU-LUOSHU-ORDER",
            "QING-P2-STEM-TRIGRAM-VERSE",
            "QING-P2-BRANCH-TRIGRAM-VERSE",
        }
        self.assertTrue(expected.issubset(set(candidates)))
        for key in expected:
            self.assertNotIn("verified",candidates[key]["status"])
            self.assertNotEqual(candidates[key].get("algorithm_status"),"verified")
        self.assertTrue("己亥單四數" in candidates["QING-HELUO-CLAUSES"]["raw_text"] or "己亥单四数" in candidates["QING-HELUO-CLAUSES"]["raw_text"])
        self.assertFalse(source["can_generate_final_iron_plate_number"])


    def test_qing_transcription_candidate_ids_are_unique_and_page_scoped(self):
        source=get_qing_source_reference()
        candidates=source["transcription_candidates"]
        ids=[x["id"] for x in candidates]
        self.assertEqual(len(ids),len(set(ids)))
        by_id={x["id"]:x for x in candidates}
        self.assertEqual(by_id["QING-HELUO-CLAUSES"]["pdf_page"],2)
        self.assertEqual(by_id["QING-EIGHT-TRIGRAM-ADD-VERSE"]["pdf_page"],2)
        self.assertEqual(by_id["QING-P3-ANSHEN-MING-INTRO"]["pdf_page"],3)
        self.assertEqual(by_id["QING-P3-HETU-LUOSHU-ORDER"]["pdf_page"],3)


    def test_page3_calendar_helpers_are_registered_but_not_number_rules(self):
        source=get_qing_source_reference()
        by_id={x["id"]:x for x in source["transcription_candidates"]}
        self.assertIn("QING-P3-WUYUAN-START-MONTH",by_id)
        self.assertIn("甲己之歲起丙寅",by_id["QING-P3-WUYUAN-START-MONTH"]["raw_text"])
        self.assertEqual(by_id["QING-P3-WUYUAN-START-MONTH"]["algorithm_status"],"calendar_helper_candidate_not_iron_plate_number_rule")
        self.assertIn("QING-P3-NAYIN-SONG-FRAGMENTS",by_id)
        self.assertEqual(by_id["QING-P3-NAYIN-SONG-FRAGMENTS"]["algorithm_status"],"calendar_reference_only_not_iron_plate_number_rule")
        self.assertFalse(source["can_generate_final_iron_plate_number"])


    def test_qing_page2_add_rule_verse_has_high_resolution_second_review_record(self):
        source=get_qing_source_reference()
        by_id={x["id"]:x for x in source["transcription_candidates"]}
        item=by_id["QING-P2-ADD-VERSE-HIGHRES-SECOND-REVIEW"]
        self.assertEqual(item["pdf_page"],2)
        self.assertIn("爻從三十起",item["raw_text"])
        self.assertIn("增方隅中一綱收",item["raw_text"])
        self.assertEqual(item["algorithm_status"],"not_implemented")
        self.assertFalse(source["can_generate_final_iron_plate_number"])

    def test_requires_four_pillars(self):
        with self.assertRaises(ValueError):
            build_tieshan_foundation({}, {"year":self.pillars["year"]})

if __name__ == "__main__": unittest.main()