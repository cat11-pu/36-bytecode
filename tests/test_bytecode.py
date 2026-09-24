import unittest

from bytecode import Verifier
from verifyapi import Checker


class TestVerifier(unittest.TestCase):
    def test_plain_halt_is_ok(self):
        self.assertTrue(Verifier().verify([["HALT"]])["ok"])

    def test_unknown_opcode(self):
        result = Verifier().verify([["NOPE"]])
        self.assertFalse(result["ok"])
        self.assertEqual(result["reason"], "unknown_opcode")

    def test_bad_arity(self):
        self.assertEqual(Verifier().verify([["PUSH"]])["reason"], "bad_arity")

    def test_stats_shape(self):
        self.assertIn("checked", Verifier().stats())

    def test_checker_wraps_verifier(self):
        checker = Checker()
        checker.verify([["HALT"]])
        self.assertEqual(checker.verifier.stats()["checked"], 1)


if __name__ == "__main__":
    unittest.main()
