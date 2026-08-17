#!/usr/bin/env python3
"""
Unit Tests for Search Diagnostics and Query Optimization
"""

import os
import sys
import unittest

# Ensure root directory is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.search_diagnostics import LocalCorpusEngine, clean_text, run_diagnostics, BENCHMARK_QUERIES

class TestSearchDiagnostics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = os.path.join(ROOT_DIR, "synthetic_data")
        cls.engine = LocalCorpusEngine(cls.data_dir)

    def test_corpus_loaded(self):
        self.assertGreaterEqual(len(self.engine.documents), 5)
        # Excludes README
        self.assertNotIn("README.md", self.engine.documents)

    def test_clean_text_strips_markdown(self):
        raw = "## **Four (4) years** of `cloud` experience"
        cleaned = clean_text(raw)
        self.assertEqual(cleaned, "four (4) years of cloud experience")

    def test_benchmark_queries_accuracy(self):
        results = run_diagnostics(self.data_dir)
        # Natural language query baseline
        self.assertLessEqual(results["naive"]["accuracy"], 60.0)
        # Optimized legal query expansion achieves 100% precision across benchmark queries
        self.assertEqual(results["optimized"]["accuracy"], 100.0)
        self.assertEqual(results["optimized"]["hits"], 5)

if __name__ == "__main__":
    unittest.main()
