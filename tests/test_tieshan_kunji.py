import unittest

from backend.tieshan_kunji import (
    PUBLISHED_CIPHER_EXAMPLES,
    STEM_TO_CIPHER_DIGIT,
    get_kunji_reference,
)


class KunjiReferenceTests(unittest.TestCase):
    def test_stem_cipher_digits_match_editorial_legend(self):
        self.assertEqual(STEM_TO_CIPHER_DIGIT["甲"], "1")
        self.assertEqual(STEM_TO_CIPHER_DIGIT["壬"], "5")
        self.assertEqual(STEM_TO_CIPHER_DIGIT["乙"], "6")
        self.assertEqual(STEM_TO_CIPHER_DIGIT["癸"], "0")

    def test_published_examples_are_preserved_without_generalization(self):
        reference = get_kunji_reference()
        examples = {row["code"]: row["number"] for row in PUBLISHED_CIPHER_EXAMPLES}
        self.assertEqual(examples["辛月月戊"], "9003")
        self.assertEqual(examples["庚丁庚乙"], "4746")
        self.assertEqual(examples["丙月辛辛"], "2099")
        self.assertEqual(examples["戊己月辛"], "3809")
        self.assertEqual(examples["辛丁乙丁"], "9767")
        self.assertEqual(examples["丙庚月戌"], "2403")
        self.assertEqual(reference["status"], "partial_metadata_not_full_cipher")

    def test_example_audit_marks_unexplained_branch_digit(self):
        from backend.tieshan_kunji import PUBLISHED_CIPHER_EXAMPLES, audit_published_example
        rows = [audit_published_example(x) for x in PUBLISHED_CIPHER_EXAMPLES]
        self.assertTrue(all(x["full_match"] for x in rows[:-1]))
        self.assertEqual(rows[-1]["known_symbol_digits"], "240")
        self.assertEqual(rows[-1]["unresolved_symbols"], ["戌"])
        self.assertEqual(rows[-1]["published_number"], "2403")
        self.assertEqual(rows[-1]["status"], "partial_match_requires_source_rule")

    def test_no_full_cipher_or_auto_advancement_claim(self):
        reference = get_kunji_reference()
        self.assertTrue(reference["advancement_note"]["not_implemented"])
        self.assertTrue(any("不等于清刻本" in item for item in reference["limitations"]))
        self.assertTrue(any("戌" in item and "无法" in item for item in reference["limitations"]))


if __name__ == "__main__":
    unittest.main()
