#!/usr/bin/env python3
"""
Unit and Integration Tests for Bid Protest Analyzer
"""

import os
import sys
import unittest

# Ensure root directory is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.bid_protest_analyzer import BidProtestAnalyzer, TimelinessCalculator, ProtestGround

class TestTimelinessCalculator(unittest.TestCase):
    def test_deadline_calculation_weekday(self):
        # 2026-08-10 was a Monday. 2026-08-14 was a Friday.
        deadlines = TimelinessCalculator.calculate_deadlines("2026-08-10", "2026-08-14")
        self.assertIn("August 14, 2026", deadlines["debriefing_concluded"])
        self.assertIn("August 19, 2026", deadlines["cica_stay_deadline"])
        self.assertIn("August 24, 2026", deadlines["gao_statutory_deadline"])
        self.assertTrue(deadlines["is_timely"])

    def test_weekend_rollover(self):
        # If debriefing concluded on a Tuesday, 5 days later is Sunday -> rolls to Monday
        deadlines = TimelinessCalculator.calculate_deadlines("2026-08-04", "2026-08-04")
        # 2026-08-04 + 5 days = 2026-08-09 (Sunday) -> rolls to 2026-08-10 (Monday)
        self.assertIn("August 10, 2026", deadlines["cica_stay_deadline"])

class TestBidProtestAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = os.path.join(ROOT_DIR, "synthetic_data")
        cls.analyzer = BidProtestAnalyzer(cls.data_dir)
        cls.analyzer.load_corpus()

    def test_corpus_loaded(self):
        self.assertGreaterEqual(len(self.analyzer.corpus_files), 5)
        self.assertIn("solicitation_rfp_section_lm.md", self.analyzer.corpus_files)
        self.assertIn("proposal_nexus_awardee.md", self.analyzer.corpus_files)
        self.assertIn("technical_evaluation_report.md", self.analyzer.corpus_files)

    def test_run_investigation_finds_five_counts(self):
        grounds = self.analyzer.run_investigation()
        self.assertEqual(len(grounds), 5)
        
        # Verify Count IDs and category codes
        count_ids = [g.count_id for g in grounds]
        self.assertIn("COUNT I", count_ids)
        self.assertIn("COUNT II", count_ids)
        self.assertIn("COUNT III", count_ids)
        self.assertIn("COUNT IV", count_ids)
        self.assertIn("COUNT V", count_ids)

        categories = [g.category_code for g in grounds]
        self.assertIn("GR-01", categories) # Unstated Criteria
        self.assertIn("GR-03", categories) # Mandatory Minimum Waiver
        self.assertIn("GR-04", categories) # Past Performance
        self.assertIn("GR-05", categories) # Defective Tradeoff

    def test_prejudice_analysis_present(self):
        grounds = self.analyzer.run_investigation()
        for g in grounds:
            self.assertTrue(len(g.prejudice_analysis) > 20, f"Prejudice missing for {g.count_id}")
            self.assertTrue(g.viability_score >= 80, f"Viability score too low for {g.count_id}")

    def test_report_generation(self):
        report = self.analyzer.generate_report()
        self.assertIn("# MASTER BID PROTEST AUDIT REPORT", report)
        self.assertIn("CICA Automatic Stay Deadline", report)
        self.assertIn("Unstated Evaluation Criteria", report)
        self.assertIn("FAR 15.308", report)

if __name__ == "__main__":
    unittest.main()
