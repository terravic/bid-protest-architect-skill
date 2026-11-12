#!/usr/bin/env python3
"""
Formal GAO Pleading Generator

Transforms dynamic audit findings from any user-supplied procurement corpus
into a formal Bid Protest Pleading formatted for the Government Accountability
Office (GAO) or Agency-Level Protest.
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import argparse
from datetime import datetime
from typing import List, Optional
from scripts.bid_protest_analyzer import BidProtestAnalyzer
from scripts.corpus_indexer import format_currency


def generate_formal_filing(
    data_dir: str,
    output_path: str,
    counsel_name: str = "Jane Doe, Esq.",
    firm_name: str = "Sterling, Vance & Associates, LLP",
    file_paths: Optional[List[str]] = None,
    grounds_json: Optional[str] = None,
) -> str:
    analyzer = BidProtestAnalyzer(
        data_dir=data_dir,
        file_paths=file_paths,
        grounds_override_path=grounds_json,
    )
    analyzer.load_corpus()
    grounds = analyzer.run_investigation()
    deadlines = analyzer.get_deadlines()
    idx = analyzer.procurement_index
    prot = idx["offerors"]["protester"]
    awd = idx["offerors"]["awardee"]
    sol_id = idx.get("solicitation_id", "SOL-UNSPECIFIED")
    agency = idx.get("issuing_agency", "Federal Contracting Agency")
    prog_title = idx.get("program_title", "Federal Procurement")
    prot_short = prot.get("short_name", prot["name"])
    awd_short = awd.get("short_name", awd["name"])
    rfp_date = idx.get("timeline", {}).get("rfp_issued", "2026-04-15")
    q_due = idx.get("debriefing", {}).get("questions_due", deadlines["debriefing_received"])

    filing_lines = [
        "# BEFORE THE COMPTROLLER GENERAL OF THE UNITED STATES",
        "# GOVERNMENT ACCOUNTABILITY OFFICE",
        "# WASHINGTON, D.C. 20548",
        "",
        "**IN THE MATTER OF**:",
        f"**{prot['name'].upper()}**,",
        "*Protester*,",
        "",
        f"**SOLICITATION NO.**: {sol_id}",
        f"**ISSUING AGENCY**: {agency}",
        "",
        "---",
        "",
        "## FORMAL BID PROTEST",
        "",
        f"{prot['name']} (\"{prot_short}\" or \"Protester\"), by and through its designated counsel, {counsel_name} of {firm_name}, hereby files this formal Bid Protest pursuant to 31 U.S.C. §§ 3551-3556 and 4 C.F.R. Part 21 challenging the contract award under Request for Proposals (\"RFP\") No. {sol_id} ({prog_title}) to {awd['name']} (\"{awd_short}\" or \"Awardee\").",
        "",
        "### I. JURISDICTION, TIMELINESS, AND CICA AUTOMATIC STAY",
        "1. **Jurisdiction**: The Comptroller General has jurisdiction over this procurement pursuant to the Competition in Contracting Act of 1984 (\"CICA\"), 31 U.S.C. § 3551 *et seq.*",
        f"2. **Timeliness**: Protester received a written debriefing on {deadlines['debriefing_received']}. Protester submitted timely debriefing questions ({q_due}), and the Agency concluded the required debriefing on {deadlines['debriefing_concluded']}. Under 4 C.F.R. § 21.2(a)(2) and 31 U.S.C. § 3553(d)(4), filing on or before {deadlines['cica_stay_deadline']} triggers the mandatory statutory stay of contract performance.",
        "3. **Interested Party Standing**: Protester is an \"interested party\" under 4 C.F.R. § 21.0(a)(1) as an actual offeror whose direct economic interest is affected by the award and who stands next in line for award under a lawful evaluation.",
        "",
        "### II. STATEMENT OF FACTS",
        f"1. The Agency issued Solicitation No. {sol_id} ({rfp_date}) for {prog_title} as a {idx.get('contract_type', 'Firm-Fixed-Price')} procurement.",
        f"2. Section M specified an evaluation basis of {idx.get('evaluation_basis', 'Best Value Tradeoff')} ({idx.get('non_price_vs_price_weight', '')}).",
        f"3. {prot['name']} submitted a proposal evaluated at {format_currency(prot.get('evaluated_price'))}.",
        f"4. The Agency selected {awd['name']} for award at an evaluated price of {format_currency(awd.get('evaluated_price'))}.",
        "",
        "### III. GROUNDS FOR PROTEST",
        "",
    ]

    for g in grounds:
        filing_lines.extend([
            f"#### {g.count_id}: {g.title.upper()} ({g.far_citation})",
            f"1. *Applicable Legal Standard*: Under {g.far_citation} and established GAO precedent (*{g.gao_precedent}*), the Agency is legally required to evaluate proposals strictly in accordance with the stated terms of the solicitation and treat all offerors equally.",
            f"2. *Agency Error & Contemporaneous Record*: {g.factual_basis} {g.agency_error}",
            f"3. *Competitive Prejudice*: {g.prejudice_analysis}",
            f"4. *Rebuttal to Discretion Claims*: {g.agency_defense_rebuttal}",
            "",
        ])

    filing_lines.extend([
        "### IV. REQUEST FOR DOCUMENT PRODUCTION (4 C.F.R. § 21.3(c))",
        "Protester requests that the Agency produce in its Agency Report:",
        "1. Complete, unredacted Technical Evaluation Team (TET) individual and consensus evaluation scorecards and worksheets.",
        f"2. Complete technical, staffing, past performance, and price proposal volumes submitted by {awd['name']}.",
        "3. Source Selection Advisory Council (SSAC) briefings and the complete Source Selection Decision Document (SSDD).",
        "4. All contemporaneous discussions/Evaluation Notices, OCI investigations, and price/cost evaluations.",
        "",
        "### V. PRAYER FOR RELIEF",
        "WHEREFORE, Protester respectfully requests that the Comptroller General:",
        "1. **SUSTAIN** this protest on all counts;",
        "2. **RECOMMEND** that the Agency immediately suspend contract performance pursuant to 31 U.S.C. § 3553(d)(4);",
        f"3. **RECOMMEND** that the Agency re-evaluate proposals in accordance with the solicitation or terminate the award to {awd_short} and make award to {prot_short}; and",
        "4. **AWARD** Protester its reasonable costs of filing and pursuing this protest, including reasonable attorneys' fees, pursuant to 4 C.F.R. § 21.8(d).",
        "",
        "Respectfully submitted,",
        "",
        f"**{counsel_name}**  ",
        f"*{firm_name}*  ",
        f"Counsel for Protester, {prot['name']}  ",
        f"Dated: {datetime.now().strftime('%B %d, %Y')}",
    ])

    filing_text = "\n".join(filing_lines)
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(filing_text)

    print(f"Formal GAO Protest Pleading successfully generated: {output_path}")
    return filing_text


def main() -> None:
    parser = argparse.ArgumentParser(description="Formal GAO Pleading Generator")
    parser.add_argument("--data", default="synthetic_data", help="Procurement dataset directory or file")
    parser.add_argument("--files", nargs="*", default=[], help="Additional explicit procurement files")
    parser.add_argument("--grounds-json", default=None, help="Optional JSON file with validated protest grounds")
    parser.add_argument("--output", default="output/gao_formal_protest_filing.md", help="Output path for filing")
    parser.add_argument("--counsel", default="Jane Doe, Esq.", help="Name of filing attorney")
    parser.add_argument("--firm", default="Sterling, Vance & Associates, LLP", help="Law firm name")

    args = parser.parse_args()
    generate_formal_filing(args.data, args.output, args.counsel, args.firm, args.files, args.grounds_json)


if __name__ == "__main__":
    main()
