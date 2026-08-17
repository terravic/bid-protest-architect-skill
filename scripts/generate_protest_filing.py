#!/usr/bin/env python3
"""
Formal GAO Pleading Generator

Transforms audit findings into a formal Bid Protest Pleading formatted
for the Government Accountability Office (GAO) or Agency-Level Protest.
"""

import os
import sys

# Ensure root directory is on sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import json
import argparse
from datetime import datetime
from scripts.bid_protest_analyzer import BidProtestAnalyzer, TimelinessCalculator

def generate_formal_filing(data_dir: str, output_path: str, counsel_name: str = "Jane Doe, Esq.", firm_name: str = "Sterling, Vance & Associates, LLP") -> str:
    analyzer = BidProtestAnalyzer(data_dir)
    analyzer.load_corpus()
    grounds = analyzer.run_investigation()
    deadlines = TimelinessCalculator.calculate_deadlines("2026-08-10", "2026-08-14")

    filing_lines = [
        "# BEFORE THE COMPTROLLER GENERAL OF THE UNITED STATES",
        "# GOVERNMENT ACCOUNTABILITY OFFICE",
        "# WASHINGTON, D.C. 20548",
        "",
        "**IN THE MATTER OF**:",
        "**APEX FEDERAL SOLUTIONS, LLC**,",
        "*Protester*,",
        "",
        "**SOLICITATION NO.**: HHS-CMS-2026-CLOUD-009",
        "**ISSUING AGENCY**: Department of Health and Human Services (HHS) / Centers for Medicare & Medicaid Services (CMS)",
        "",
        "---",
        "",
        "## FORMAL BID PROTEST",
        "",
        f"Apex Federal Solutions, LLC (\"Apex\" or \"Protester\"), by and through its designated counsel, {counsel_name} of {firm_name}, hereby files this formal Bid Protest pursuant to 31 U.S.C. §§ 3551-3556 and 4 C.F.R. Part 21 challenging the contract award under Request for Proposals (\"RFP\") No. HHS-CMS-2026-CLOUD-009 to Nexus Defense Systems, Inc. (\"Nexus\" or \"Awardee\").",
        "",
        "### I. JURISDICTION, TIMELINESS, AND CICA AUTOMATIC STAY",
        "1. **Jurisdiction**: The Comptroller General has jurisdiction over this procurement pursuant to the Competition in Contracting Act of 1984 (\"CICA\"), 31 U.S.C. § 3551 *et seq.*",
        f"2. **Timeliness**: Protester received a written debriefing on {deadlines['debriefing_received']}. Protester submitted timely debriefing questions on August 12, 2026, and the Agency delivered written responses on {deadlines['debriefing_concluded']}. Under 4 C.F.R. § 21.2(a)(2) and 31 U.S.C. § 3553(d)(4), this protest is filed within five (5) days of the conclusion of the required debriefing, thereby triggering the mandatory statutory stay of contract performance.",
        "3. **Interested Party Standing**: Protester is an \"interested party\" under 4 C.F.R. § 21.0(a)(1) as an actual offeror whose direct economic interest is affected by the award. Protester submitted an exceptional technical proposal and is next in line for contract award.",
        "",
        "### II. STATEMENT OF FACTS",
        "1. On April 15, 2026, CMS issued RFP No. HHS-CMS-2026-CLOUD-009 seeking enterprise cloud modernization services.",
        "2. Section M.1 specified that award would be made on a Best Value Tradeoff basis where Non-Price Factors (Factors 1, 2, and 3) combined were *significantly more important than Price*.",
        "3. Factor 1 (Technical) was designated the most important factor, followed by Factor 2 (Key Personnel) and Factor 3 (Past Performance).",
        "4. Protester submitted a fully compliant proposal priced at $94,500,000.00 offering a 99.999% SLA and 14-year veteran key personnel.",
        "5. Awardee submitted a proposal priced at $82,200,000.00 offering a non-compliant 99.95% SLA and an under-qualified Lead Architect.",
        "",
        "### III. GROUNDS FOR PROTEST",
        ""
    ]

    for g in grounds:
        filing_lines.extend([
            f"#### {g.count_id}: {g.title.upper()} ({g.far_citation})",
            f"1. *Applicable Legal Standard*: Under {g.far_citation} and established GAO precedent (*{g.gao_precedent}*), the Agency is legally required to evaluate proposals strictly in accordance with the stated terms of the solicitation and treat all offerors equally.",
            f"2. *Agency Error & Contemporaneous Record*: {g.factual_basis} {g.agency_error}",
            f"3. *Competitive Prejudice*: {g.prejudice_analysis}",
            f"4. *Rebuttal to Discretion Claims*: {g.agency_defense_rebuttal}",
            ""
        ])

    filing_lines.extend([
        "### IV. REQUEST FOR DOCUMENT PRODUCTION (4 C.F.R. § 21.3(c))",
        "Protester requests that the Agency produce in its Agency Report:",
        "1. The complete, unredacted Technical Evaluation Team (TET) individual and consensus evaluation scorecards.",
        "2. Complete technical proposal Volume I and Volume II submitted by Nexus Defense Systems, Inc.",
        "3. The Source Selection Advisory Council (SSAC) report and all written documentation provided to the SSA.",
        "4. All contemporaneous price realism and cost reasonableness analyses.",
        "",
        "### V. PRAYER FOR RELIEF",
        "WHEREFORE, Protester respectfully requests that the Comptroller General:",
        "1. **SUSTAIN** this protest on all counts;",
        "2. **RECOMMEND** that the Agency immediately suspend performance pursuant to 31 U.S.C. § 3553(d)(4);",
        "3. **RECOMMEND** that the Agency re-evaluate proposals in accordance with the mandatory terms of the RFP or terminate the award to Nexus and award the contract to Protester; and",
        "4. **AWARD** Protester its reasonable costs of filing and pursuing this protest, including reasonable attorneys' fees, pursuant to 4 C.F.R. § 21.8(d).",
        "",
        "Respectfully submitted,",
        "",
        f"**{counsel_name}**  ",
        f"*{firm_name}*  ",
        "Counsel for Protester, Apex Federal Solutions, LLC  ",
        f"Dated: {datetime.now().strftime('%B %d, %Y')}"
    ])

    filing_text = "\n".join(filing_lines)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(filing_text)

    print(f"Formal GAO Protest Pleading successfully generated: {output_path}")
    return filing_text

def main():
    parser = argparse.ArgumentParser(description="Formal GAO Pleading Generator")
    parser.add_argument("--data", default="synthetic_data", help="Procurement dataset directory")
    parser.add_argument("--output", default="output/gao_formal_protest_filing.md", help="Output path for filing")
    parser.add_argument("--counsel", default="Jane Doe, Esq.", help="Name of filing attorney")
    parser.add_argument("--firm", default="Sterling, Vance & Associates, LLP", help="Law firm name")

    args = parser.parse_args()
    generate_formal_filing(args.data, args.output, args.counsel, args.firm)

if __name__ == "__main__":
    main()
