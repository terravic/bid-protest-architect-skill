#!/usr/bin/env python3
"""
Integration & DESIGN.md Compliance Tests for User-Supplied Real Corpora and Dashboard
"""

import os
import re
import sys
import json
import zipfile
import tempfile
import unittest
from html.parser import HTMLParser

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.corpus_indexer import ProcurementCorpusIndexer
from scripts.bid_protest_analyzer import BidProtestAnalyzer
from scripts.generate_protest_filing import generate_formal_filing
from scripts.search_diagnostics import run_diagnostics
from scripts.build_dashboard import build_dashboard_html


def _write_minimal_docx(path: str, paragraphs: list) -> None:
    """Creates a genuine .docx ZIP package with word/document.xml for testing."""
    p_xml = "".join(
        f'<w:p><w:r><w:t>{p.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</w:t></w:r></w:p>'
        for p in paragraphs
    )
    doc_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        f"<w:body>{p_xml}</w:body></w:document>"
    )
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("word/document.xml", doc_xml)


class ThemeButtonTextChecker(HTMLParser):
    """Verifies #theme-btn-light, #theme-btn-dark, #theme-btn-system contain icons only."""

    def __init__(self) -> None:
        super().__init__()
        self.buttons = {}
        self._active_id = None
        self._svg_depth = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        attr_map = dict(attrs)
        if tag == "button" and attr_map.get("id") in ("theme-btn-light", "theme-btn-dark", "theme-btn-system"):
            self._active_id = attr_map["id"]
            self.buttons[self._active_id] = {"attrs": attr_map, "has_svg": False, "text": ""}
        elif self._active_id and tag == "svg":
            self._svg_depth += 1
            self.buttons[self._active_id]["has_svg"] = True

    def handle_endtag(self, tag: str) -> None:
        if self._active_id and tag == "svg" and self._svg_depth > 0:
            self._svg_depth -= 1
        elif self._active_id and tag == "button":
            self._active_id = None

    def handle_data(self, data: str) -> None:
        if self._active_id and self._svg_depth == 0:
            self.buttons[self._active_id]["text"] += data.strip()


class TestDynamicUserCorpus(unittest.TestCase):
    def test_custom_dod_multiformat_corpus_end_to_end(self):
        """Verifies real multi-format (.docx, .html, .csv, .md) user corpus ingestion & GR-01..GR-08."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # 1. Solicitation in .docx format
            rfp_docx = os.path.join(tmpdir, "usaf_solicitation_rfp.docx")
            _write_minimal_docx(
                rfp_docx,
                [
                    "SOLICITATION NO. FA8730-26-R-0042",
                    "Title: USAF Tactical Zero-Trust Telemetry Mesh (ABMS-ZTM)",
                    "Issuing Agency: Department of the Air Force / AFLCMC",
                    "Contract Type: Cost-Plus-Fixed-Fee",
                    "Date Issued: May 18, 2026",
                    "SECTION L & SECTION M",
                    "Factor 1: Mission Architecture - Most Important. Mandatory minimum availability uptime of 99.99%.",
                    "Key Personnel Position 1: Chief Mission Architect - Minimum of 12 years experience and TS/SCI.",
                    "Factor 3: Past Performance - total contract value >= $75,000,000.",
                    "Non-price factors combined are significantly more important than Price. FAR 15.404-1(d) cost realism required.",
                ],
            )

            # 2. Protester Proposal in .md
            with open(os.path.join(tmpdir, "protester_vanguard_proposal.md"), "w", encoding="utf-8") as f:
                f.write(
                    "**Offeror**: Vanguard Cyber Systems, LLC (CAGE: 9A2B1)\n"
                    "**Submitted Price**: $118,400,000.00\n"
                    "1. **Chief Mission Architect: Dr. Alan Grant**\n"
                    "   - Experience: 16 years federal defense architecture experience.\n"
                    "   - Certifications: AWS Professional, CISSP.\n"
                    "### 3.1 Reference 1: AFLCMC Mesh\n"
                    "- Value: $110,000,000.00\n"
                )

            # 3. Awardee Proposal in .html
            with open(os.path.join(tmpdir, "awardee_stratos_proposal.html"), "w", encoding="utf-8") as f:
                f.write(
                    "<html><body>"
                    "<p><b>Offeror</b>: Stratos Defense Group, Inc.</p>"
                    "<p><b>Submitted Price</b>: $96,100,000.00</p>"
                    "<p>Target SLA: monthly availability of 99.90% uptime.</p>"
                    "<p>1. Chief Mission Architect: Evan Ross</p>"
                    "<p>Experience: 5 years total IT cloud experience. Does not possess CISSP.</p>"
                    "</body></html>"
                )

            # 4. TET + Discussions + OCI + Cost Realism in .md & .csv
            with open(os.path.join(tmpdir, "tet_consensus_and_en.md"), "w", encoding="utf-8") as f:
                f.write(
                    "# TECHNICAL EVALUATION TEAM CONSENSUS REPORT\n"
                    "| Offeror | Factor 1: Architecture | Factor 2: Key Personnel | Factor 3: Past Performance | Factor 4: Price |\n"
                    "|---|---|---|---|---|\n"
                    "| Stratos Defense Group, Inc. | Good | Acceptable | Satisfactory Confidence | $96,100,000.00 |\n"
                    "| Vanguard Cyber Systems, LLC | Acceptable | Outstanding | Substantial Confidence | $118,400,000.00 |\n\n"
                    "## Detailed Findings: Vanguard\n"
                    "### Factor 1\n"
                    "- Significant Weakness: Vanguard did not propose \"an optical ground relay station.\" Neither Section L nor Section M mentions optical ground relays (unstated criteria). Reduced Vanguard from Outstanding to Acceptable.\n"
                    "- Unequal discussions under FAR 15.306: Evaluation Notice issued only to awardee Stratos.\n"
                    "- Unmitigated OCI under FAR 9.5: Stratos subcontractor had unequal access to information.\n"
                    "- Failed to conduct a cost realism evaluation under FAR 15.404-1(d) on Stratos unrealistically low labor rates.\n"
                )

            with open(os.path.join(tmpdir, "ssdd_and_debriefing.md"), "w", encoding="utf-8") as f:
                f.write(
                    "# POST-AWARD DEBRIEFING LETTER\n"
                    "**DATE OF DEBRIEFING DELIVERY**: September 14, 2026\n"
                    "Agency responses to timely debriefing questions will be delivered by September 18, 2026.\n"
                    "I hereby select Stratos Defense Group, Inc. for award in the amount of $96,100,000.00 under a best value tradeoff.\n"
                )

            indexer = ProcurementCorpusIndexer(data_dir=tmpdir)
            indexer.load_documents()
            matrix = indexer.extract_evaluation_matrix()

            self.assertEqual(matrix["solicitation_id"], "FA8730-26-R-0042")
            self.assertIn("Vanguard", matrix["offerors"]["protester"]["name"])
            self.assertIn("Stratos", matrix["offerors"]["awardee"]["name"])
            self.assertEqual(matrix["offerors"]["protester"]["evaluated_price"], 118400000.0)
            self.assertEqual(matrix["offerors"]["awardee"]["evaluated_price"], 96100000.0)

            analyzer = BidProtestAnalyzer(data_dir=tmpdir)
            grounds = analyzer.run_investigation()
            codes = {g.category_code for g in grounds}
            self.assertIn("GR-01", codes)
            self.assertIn("GR-03", codes)
            self.assertIn("GR-05", codes)
            self.assertIn("GR-06", codes)
            self.assertIn("GR-07", codes)
            self.assertIn("GR-08", codes)

            deadlines = analyzer.get_deadlines()
            # Sept 18, 2026 (Fri) + 5 days = Sept 23, 2026 (Wed)
            self.assertEqual(deadlines["cica_stay_iso"], "2026-09-23")

            filing_out = os.path.join(tmpdir, "filing.md")
            filing_txt = generate_formal_filing(tmpdir, filing_out)
            self.assertIn("FA8730-26-R-0042", filing_txt)
            self.assertIn("VANGUARD CYBER SYSTEMS, LLC", filing_txt)

            diag = run_diagnostics(tmpdir)
            self.assertGreaterEqual(diag["optimized"]["accuracy"], 80.0)

            dash_out = os.path.join(tmpdir, "custom_dashboard.html")
            build_dashboard_html(output_path=dash_out, data_dir=tmpdir)
            with open(dash_out, "r", encoding="utf-8") as f:
                dash_html = f.read()
            self.assertIn("FA8730-26-R-0042", dash_html)
            self.assertIn("Vanguard Cyber Systems, LLC", dash_html)

    def test_agent_grounds_json_override(self):
        """Verifies agent harness can supply custom structured grounds JSON."""
        with tempfile.TemporaryDirectory() as tmpdir:
            grounds_path = os.path.join(tmpdir, "agent_grounds.json")
            custom_grounds = [
                {
                    "count_id": "COUNT I",
                    "title": "Custom Agent-Identified Solicitation Ambiguity",
                    "category_code": "GR-01",
                    "far_citation": "FAR 15.305(a)",
                    "gao_precedent": "Vistronix, LLC, B-416916",
                    "factual_basis": "Custom factual basis from agent prompt.",
                    "agency_error": "Custom agency error.",
                    "prejudice_analysis": "Custom prejudice analysis exceeding twenty characters.",
                    "agency_defense_rebuttal": "Custom rebuttal.",
                    "viability_score": 94,
                    "target_factor": "Factor 1",
                }
            ]
            with open(grounds_path, "w", encoding="utf-8") as f:
                json.dump(custom_grounds, f)

            analyzer = BidProtestAnalyzer(
                data_dir=os.path.join(ROOT_DIR, "synthetic_data"),
                grounds_override_path=grounds_path,
            )
            grounds = analyzer.run_investigation()
            self.assertEqual(len(grounds), 1)
            self.assertEqual(grounds[0].title, "Custom Agent-Identified Solicitation Ambiguity")


class TestDashboardDesignCompliance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dashboard_path = os.path.join(ROOT_DIR, "dashboard.html")
        with open(cls.dashboard_path, "r", encoding="utf-8") as f:
            cls.html = f.read()

    def test_required_hex_tokens_present(self):
        required_tokens = [
            "#FAFAF9", "#FFFFFF", "#E7E5E4", "#1C1917", "#787774",
            "#0D0E11", "#16171D", "#292A30", "#ECE8E2", "#9A9895",
            "#0D9488", "#D97706", "#4F46E5", "#059669", "#E11D48",
        ]
        upper_html = self.html.upper()
        for token in required_tokens:
            self.assertIn(token, upper_html, f"Missing DESIGN.md color token {token}")

    def test_three_icon_only_theme_buttons(self):
        checker = ThemeButtonTextChecker()
        checker.feed(self.html)
        for btn_id, expected_mode in (
            ("theme-btn-light", "light"),
            ("theme-btn-dark", "dark"),
            ("theme-btn-system", "system"),
        ):
            self.assertIn(btn_id, checker.buttons, f"Missing {btn_id}")
            info = checker.buttons[btn_id]
            self.assertTrue(info["has_svg"], f"{btn_id} must contain an SVG icon")
            self.assertEqual(info["text"], "", f"{btn_id} must be icon-only with zero text")
            self.assertEqual(info["attrs"].get("data-theme-mode"), expected_mode)

    def test_typography_and_forbidden_words(self):
        self.assertIn("Instrument Serif", self.html)
        self.assertIn("DM Sans", self.html)
        self.assertIn("IBM Plex Mono", self.html)
        self.assertIn("tabular-nums", self.html)
        self.assertIsNone(re.search(r"\bInter\b", self.html), "Generic Inter font is prohibited by DESIGN.md")
        self.assertIsNone(re.search(r"\bRoboto\b", self.html), "Generic Roboto font is prohibited by DESIGN.md")
        self.assertIsNone(re.search(r"physics", self.html, re.IGNORECASE), "Forbidden word found in dashboard.html")

    def test_empirical_data_and_webgl_fallback_present(self):
        self.assertIn("HHS-CMS-2026-CLOUD-009", self.html)
        self.assertIn("Apex Federal Solutions, LLC", self.html)
        self.assertIn("Nexus Defense Systems, Inc.", self.html)
        self.assertIn("Interactive Relationship Node Map", self.html)
        self.assertIn("2D Projection Fallback", self.html)
        self.assertIn("extractDocxBrowser", self.html)


if __name__ == "__main__":
    unittest.main()
