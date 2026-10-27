#!/usr/bin/env python3
"""Tests for verify.py. Run: python3 -m unittest discover -s profanir"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify  # noqa: E402

BASE = Path(__file__).resolve().parent
T04 = {
    'before': 'Rétt er að taka fram að leigjandi má óska eftir framlengingu ef umsókn berst fyrir 1. desember.',
    'protected': ['má', 'ef'],
}


class SpanCounting(unittest.TestCase):
    def test_dropped_word_is_caught_even_if_it_occurs_inside_another_word(self):
        # „ef“ hverfur en „hefja“ bætist við: hlutstrengjatalning sæi enga breytingu.
        after = 'Leigjandi má óska eftir framlengingu og hefja ferlið berist umsókn fyrir 1. desember.'
        self.assertIn('protected_span_changed: ef', verify.check(T04, after))

    def test_word_inside_longer_word_does_not_count(self):
        after = 'Leigjandi fær málið ef umsókn berst fyrir 1. desember og óskar eftir framlengingu.'
        self.assertIn('protected_span_changed: má', verify.check(T04, after))

    def test_unchanged_words_pass(self):
        after = 'Leigjandi má óska eftir framlengingu ef umsókn berst fyrir 1. desember.'
        self.assertEqual(verify.check(T04, after), [])

    def test_spans_with_punctuation_and_code(self):
        case = {'before': 'Keyrðu `tool --dry-run`. Hún sagði: „Nei.“', 'protected': ['`tool --dry-run`', '„Nei.“']}
        self.assertEqual(verify.check(case, 'Hún sagði: „Nei.“ Keyrðu `tool --dry-run`.'), [])


class StoredResults(unittest.TestCase):
    def test_stored_outputs_pass_and_controls_are_detected(self):
        report = verify.build_report(BASE / 'nidurstodur.jsonl')
        self.assertEqual(report['mechanical_pass_count'], 18)
        detected = sum(n['mechanically_detected'] for n in report['negative_controls'])
        self.assertGreaterEqual(detected, verify.MIN_DETECTED)

    def test_default_run_does_not_rewrite_report_file(self):
        target = BASE / 'velraent-mat.json'
        before = target.stat().st_mtime_ns
        subprocess.run([sys.executable, str(BASE / 'verify.py')], check=True, capture_output=True)
        self.assertEqual(target.stat().st_mtime_ns, before)


if __name__ == '__main__':
    unittest.main()
