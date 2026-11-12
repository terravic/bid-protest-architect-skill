# Bid Protest Architect Skill

An analytical skill, Python command-line toolkit, and standalone interactive HTML workspace (`dashboard.html`) for auditing U.S. Federal Government contract awards under the Federal Acquisition Regulation (FAR) and Title 4 of the Code of Federal Regulations (4 C.F.R. Part 21).

This repository parses solicitations (Sections L and M), offeror proposals, Technical Evaluation Team (TET) consensus reports, Source Selection Decision Documents (SSDDs), and post-award debriefing letters across `.md`, `.txt`, `.docx`, `.pdf`, `.csv`, `.html`, and `.json` formats to calculate statutory deadlines, cross-examine evaluation records across eight protest grounds, and generate structured audit reports, draft Government Accountability Office (GAO) pleadings, and interactive visual workspaces.

> **Legal Disclaimer and Practitioner Notice**: This repository, its scripts, and its generated outputs are provided solely for informational, analytical, and workflow preparation purposes. They do not constitute legal advice, a legal opinion, or legal representation, and their use does not create an attorney-client relationship. Consult licensed government contracts counsel before filing any protest with an executive agency, the GAO, or the U.S. Court of Federal Claims.

---

## Table of Contents

1. [Overview and Core Capabilities](#1-overview-and-core-capabilities)
2. [Non-Technical User Guide](#2-non-technical-user-guide)
3. [Required Procurement Documents](#3-required-procurement-documents)
4. [System Architecture and Audit Pipeline](#4-system-architecture-and-audit-pipeline)
5. [Command-Line Interface Reference](#5-command-line-interface-reference)
6. [Interactive Dashboard Workspace (`dashboard.html`)](#6-interactive-dashboard-workspace-dashboardhtml)
7. [Synthetic Benchmark Dataset](#7-synthetic-benchmark-dataset)
8. [Testing and Validation](#8-testing-and-validation)
9. [Project Structure](#9-project-structure)
10. [Statutory and Regulatory Framework](#10-statutory-and-regulatory-framework)
11. [License](#11-license)

---

## 1. Overview and Core Capabilities

A federal bid protest challenges the terms of a solicitation or the award of a federal contract when an agency deviates from stated evaluation criteria, waives mandatory requirements, conducts unequal evaluations, or makes an unsupported source selection decision.

Core functions provided in this project:
- **Multi-Format Document Parsing**: Reads user-supplied procurement files in `.md`, `.txt`, `.docx`, `.pdf`, `.csv`, `.tsv`, `.html`, `.xml`, and `.json` formats using Python standard library modules or in-browser file readers.
- **Statutory Deadline Calculation**: Computes the 5-calendar-day Competition in Contracting Act (CICA) automatic stay window (`31 U.S.C. 3553(d)(4)`) and the 10-calendar-day GAO filing deadline (`4 C.F.R. 21.2(a)(2)`), automatically rolling weekend dates to the next business day.
- **Eight-Ground Cross-Examination**: Audits records for unstated evaluation criteria (`GR-01`), disparate treatment (`GR-02`), waived mandatory minimums (`GR-03`), flawed past performance relevance (`GR-04`), defective cost-technical tradeoffs (`GR-05`), unequal discussions (`GR-06`), organizational conflicts of interest (`GR-07`), and flawed cost/price realism (`GR-08`).
- **Competitive Prejudice and Red-Team Verification**: Evaluates whether correcting an identified agency error gives the protester a substantial chance of award (`404 F.3d 1346`) and tests each count against anticipated agency defenses.
- **Document and Dashboard Synthesis**: Outputs a Markdown audit report (`output/master_bid_protest_report.md`), a structured JSON model (`output/audit_results.json`), a draft GAO pleading (`output/gao_formal_protest_filing.md`), and a standalone interactive dashboard (`dashboard.html`).

---

## 2. Non-Technical User Guide

You do not need programming experience to use this tool. Below are three practical ways capture managers, proposal leads, contract administrators, and legal staff can evaluate a contract award decision.

### Workflow A: Auditing Documents Directly in Your Web Browser

Use this approach right after receiving a post-award debriefing letter when you want to inspect deadlines and potential evaluation errors on your computer without using commands.

1. Locate `dashboard.html` in the project folder and double-click it to open it in any standard web browser.
2. Click the **Load Corpus** button in the top bar.
3. Drag and drop your procurement files into the upload box (for example, your RFP `Section_L_and_M.docx`, your `Proposal_Summary.pdf`, and your `Debriefing_Letter.txt`), or paste copied paragraphs into the **Verbatim Text Excerpt** box and click **Add Document to Corpus**.
4. Confirm or enter the date your debriefing concluded in the **Debriefing Concluded** date field, then click **Run 8-Ground Audit**.
5. Review the updated panels:
   - The top row shows your exact **CICA Automatic Stay Window** deadline (to pause contract performance during a protest) and overall viability score.
   - The **Section L & M Mandatory Compliance & Offeror Matrix** highlights side-by-side differences between what the RFP required and what each bidder received credit for.
   - Click any row in the **Sustained GAO Protest Grounds Ledger** at the bottom to read the plain-English factual summary, why the error affected your chance of winning, and how the agency is likely to respond.
6. Click **Export Pleading** to download a structured Markdown draft to share with your company's legal counsel.

**Real-World Example 1 (IT Services Contract Debriefing)**:
> Suppose your team bid $14.2M on a federal help-desk solicitation requiring a Project Manager with at least 8 years of federal IT service management experience. Your debriefing letter states that the contract went to a $12.9M bidder, and also notes that your technical score was lowered because you did not propose an "automated voice-biometrics system" -- a feature never mentioned in the RFP. By dropping the RFP and debriefing letter into `dashboard.html` and clicking **Run 8-Ground Audit**, the workspace flags the unstated voice-biometrics penalty under `FAR 15.305(a)`, computes your 5-day CICA stay deadline from the debriefing close date, and organizes the exact RFP section references for your attorney to review before the deadline expires.

### Workflow B: Using Plain-Language Requests in an Assistant Interface

If this skill is loaded into an assistant environment with access to your project folder, place your procurement documents into a subfolder (for example, `my_procurement_case/`) and paste a plain-English request.

**Real-World Example 2 (Healthcare Cloud Modernization Award Review)**:
```text
Please review our contract award documents in the my_procurement_case/ folder using the Bid Protest Architect skill.

We just finished our written debriefing Q&A on Friday, October 9, 2026. Please tell us:
1. The exact date and time we must file by to pause contract Transition-In under the 5-day CICA automatic stay rule.
2. Whether the agency penalized us for anything that was not actually required in Section L or Section M of the RFP.
3. Whether the winning bidder failed any mandatory minimum requirements in the solicitation.
4. Which issues are strong enough to send to outside protest counsel, and generate an updated dashboard.html and summary report for our executive briefing.
```

**Real-World Example 3 (Quick Deadline Check During Debriefing Q&A)**:
```text
We received a written post-award debriefing on Monday, November 2, 2026. We submitted follow-up questions on November 4, and the Contracting Officer sent written answers closing the debriefing on Friday, November 6, 2026. What is our 5-day CICA automatic stay deadline and our 10-day GAO filing deadline?
```
*(In this example, 5 calendar days after Friday, November 6 falls on Wednesday, November 11; 10 calendar days falls on Monday, November 16. If either deadline had landed on a Saturday or Sunday, the calculator rolls it forward to Monday.)*

---

## 3. Required Procurement Documents

You can run an audit with as little as an RFP and a debriefing letter, and add additional records if outside counsel obtains the agency record under a GAO Protective Order:

| Document Type | Role in the Audit | Key Information Extracted |
|---|---|---|
| **Solicitation / RFP (Sections L & M)** | Establishes binding rules and evaluation weights | Mandatory minimums (`shall`, `must`), SLA floors, experience thresholds, factor importance order |
| **Post-Award Debriefing Letter & Q&A** | Establishes filing deadlines and disclosed weaknesses | Debriefing delivery date, Q&A conclusion date, evaluated prices, factor ratings, assigned weaknesses |
| **Protester Proposal Volumes** | Verifies compliance and technical strengths | Proposed SLA/RTO figures, key personnel resumes and credentials, relevant past performance values |
| **Awardee Proposal / Redacted Excerpts** | Identifies non-compliance with mandatory terms | Exceptions to SLAs, staffing experience shortfalls, commercial or sub-threshold references |
| **TET Consensus Report** | Identifies unstated criteria and unequal treatment | Evaluator strengths, significant weaknesses, deficiencies, and waiver rationales |
| **Source Selection Decision (SSDD)** | Evaluates the FAR 15.308 tradeoff justification | SSA comparative narrative, price-premium reasoning, and reliance on flawed underlying scores |
| **Discussions / OCI / Cost Worksheets** | Supports specialized protest counts (`GR-06..GR-08`) | Evaluation Notices (ENs), conflict-of-interest disclosures, and FAR 15.404-1(d) realism adjustments |

---

## 4. System Architecture and Audit Pipeline

```
+-------------------------------------------------------------------+
|  Input Documents (.md, .txt, .docx, .pdf, .csv, .html, .json)     |
+---------------------------------+---------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|  1. Corpus Indexer (scripts/corpus_indexer.py)                    |
|     - Classifies document roles & strips markup                   |
|     - Extracts Section L minimums, Section M weights & timelines  |
+---------------------------------+---------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
|  2. Timeliness & 8-Ground Analyzer (scripts/bid_protest_analyzer) |
|     - Computes 5-day CICA stay & 10-day GAO filing deadlines      |
|     - Cross-examines GR-01 through GR-08 with file:line citations |
|     - Applies competitive prejudice & agency-defense checks       |
+---------------------------------+---------------------------------+
                                  |
             +--------------------+--------------------+
             |                                         |
             v                                         v
+------------------------------------+   +--------------------------+
|  3. Written Audit & Pleading       |   |  4. Interactive UI       |
|     - master_bid_protest_report.md |   |     - build_dashboard.py |
|     - gao_formal_protest_filing.md |   |     - dashboard.html     |
|     - audit_results.json           |   |     - Optional HTTP/SSE  |
+------------------------------------+   +--------------------------+
```

---

## 5. Command-Line Interface Reference

All core scripts require Python 3.9 or newer and run using the Python standard library.

### 1. Index a Procurement Folder or File List
```bash
python3 scripts/corpus_indexer.py --data synthetic_data --output scratch/procurement_index.json
```
To index specific user files across formats:
```bash
python3 scripts/corpus_indexer.py --data path/to/rfp_folder --files debriefing.pdf proposal_notes.docx --output scratch/procurement_index.json
```

### 2. Run the 8-Ground Bid Protest Analyzer
```bash
python3 scripts/bid_protest_analyzer.py --data synthetic_data --output output/master_bid_protest_report.md --json-output output/audit_results.json
```

### 3. Generate a Draft GAO Protest Pleading
```bash
python3 scripts/generate_protest_filing.py --data synthetic_data --output output/gao_formal_protest_filing.md --counsel "Designated Protest Counsel" --firm "Procurement Legal Practice"
```

### 4. Run Corpus Search Retrieval Diagnostics
```bash
python3 scripts/search_diagnostics.py --data synthetic_data
```

### 5. Build or Serve the Interactive Dashboard (`dashboard.html`)
Compile a standalone `dashboard.html` file from any directory:
```bash
python3 scripts/build_dashboard.py --data synthetic_data --output dashboard.html
```
Start the optional local HTTP server with live Server-Sent Events (SSE) file watching:
```bash
python3 scripts/build_dashboard.py --data synthetic_data --output dashboard.html --serve --port 8765
```

---

## 6. Interactive Dashboard Workspace (`dashboard.html`)

`dashboard.html` follows the layout, typography, and color specifications defined in [DESIGN.md](DESIGN.md) and [prd.md](prd.md):
- **Single-Level Bento Grid**: 12-column flat layout with `1px solid` structural borders, `Instrument Serif` display headers, `DM Sans` UI controls, and `IBM Plex Mono` (`tabular-nums`) numerical tables.
- **Light, Dark, and System Theme Selector**: Three side-by-side SVG icon buttons (`#theme-btn-light`, `#theme-btn-dark`, `#theme-btn-system`) with `localStorage` persistence, real-time OS appearance tracking, and host OS fallback detection.
- **Interactive Relationship Node Map**: Deterministic 3-tier 3D WebGL spatial graph (paired with an automatic 2D projection fallback) linking solicitation clauses, evaluation findings, and sustained protest counts.
- **Factor Rating Shift and Tradeoff Plot**: Responsive 2D SVG chart comparing as-evaluated TET ratings against solicitation-compliant ratings and evaluated prices.
- **Client-Side Multi-Document Loader**: Built-in file dropzone and text composer enabling offline multi-document auditing and Markdown/JSON export directly in the browser.

---

## 7. Synthetic Benchmark Dataset

The `synthetic_data/` directory provides a non-PHI/PII benchmark procurement package (`HHS-CMS-2026-CLOUD-009`) containing five embedded procurement errors for regression testing:
1. **Unstated Evaluation Criteria (`GR-01`, `FAR 15.305`)**: Penalty assigned to Protester (Apex Federal) for omitting an unlisted on-premises mainframe hardware bridge.
2. **Waived Key Personnel Minimums (`GR-03`, `FAR 15.206`)**: Acceptance of Awardee (Nexus Systems) Lead Cloud Architect with 4 years experience and missing credentials against a mandatory 10-year minimum.
3. **Unenforced Mandatory SLA Floor (`GR-03`, `FAR 15.206`)**: Acceptance of a 99.95% availability SLA below the mandatory 99.99% threshold in Section L.3.1.
4. **Flawed Past Performance Relevance (`GR-04`, `FAR 15.305(a)(2)`)**: Favorable confidence rating assigned to $3.2M and $8.5M commercial/state web portals against a $50M+ federal healthcare cloud threshold.
5. **Defective Best Value Tradeoff (`GR-05`, `FAR 15.308`)**: Mechanical selection of the lower-priced proposal relying on flawed technical ratings despite Section M weighting non-price factors significantly above price.

---

## 8. Testing and Validation

Run the unit and integration test suite using `pytest` or `unittest`:

```bash
pytest tests/ -v
```
or:
```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Test modules:
- `tests/test_analyzer.py`: Validates 5-day CICA stay and 10-day GAO deadline math, weekend rollovers, 5-count synthetic benchmark detection, prejudice analysis, and report output.
- `tests/test_search_diagnostics.py`: Validates Markdown normalization, lexical/phrase scoring, and retrieval accuracy across query strategies.
- `tests/test_dynamic_user_corpus.py`: Validates multi-format user corpus ingestion (`.docx`, `.html`, `.md`), Grounds `GR-01` through `GR-08`, structured JSON overrides, `DESIGN.md` token/component specifications, and relative-path / ASCII repository hygiene.

---

## 9. Project Structure

```text
bid-protest-architect-skill/
  .gitignore
  DESIGN.md
  LICENSE
  README.md
  SKILL.md
  dashboard.html
  prd.md
  pyproject.toml
  requirements.txt
  examples/
    sample_prompts.md
    sample_run_output.md
  output/
    audit_results.json
    gao_formal_protest_filing.md
    master_bid_protest_report.md
  references/
    agent_orchestration_patterns.md
    gao_precedents_handbook.md
    protest_grounds_taxonomy.md
    search_optimization_guide.md
  resources/
    checklists/
      protest_viability_checklist.md
    templates/
      bid_protest_report_template.md
      dashboard_template.html
      gao_formal_protest_template.md
  scratch/
    procurement_index.json
  scripts/
    bid_protest_analyzer.py
    build_dashboard.py
    build_docs.py
    build_synthetic_data.py
    corpus_indexer.py
    generate_protest_filing.py
    search_diagnostics.py
  synthetic_data/
    README.md
    debriefing_letter.md
    proposal_apex_protester.md
    proposal_nexus_awardee.md
    solicitation_rfp_section_lm.md
    ssdd_source_selection_decision.md
    technical_evaluation_report.md
  tests/
    test_analyzer.py
    test_dynamic_user_corpus.py
    test_search_diagnostics.py
```

---

## 10. Statutory and Regulatory Framework

- **FAR Part 15**: Contracting by Negotiation (`FAR 15.101-1` Best Value Continuum, `FAR 15.206` Amending the Solicitation, `FAR 15.305` Proposal Evaluation, `FAR 15.306` Exchanges with Offerors, `FAR 15.308` Source Selection Decision, `FAR 15.404-1(d)` Cost Realism Analysis, `FAR 15.506` Postaward Debriefing).
- **FAR Subpart 9.5**: Organizational and Consultant Conflicts of Interest.
- **31 U.S.C. 3551-3556**: Competition in Contracting Act (CICA), including `31 U.S.C. 3553(d)(4)` Automatic Stay of Performance.
- **28 U.S.C. 1491(b)(1)**: Tucker Act bid protest jurisdiction before the U.S. Court of Federal Claims.
- **4 C.F.R. Part 21**: Government Accountability Office Bid Protest Regulations (`4 C.F.R. 21.0(a)(1)` Interested Party Standing, `4 C.F.R. 21.2` Timeliness, `4 C.F.R. 21.3(c)` Document Production).
- **Controlling Decisions**: GAO Decisions `B-400760`, `B-416916`, `B-409651`, `B-400394`, `B-404153`, `B-416211`, `B-414223`, `B-293134`, `B-415755`, `B-414886`, `B-404033`, `B-413721`, and `404 F.3d 1346 (Fed. Cir. 2005)`.

---

## 11. License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for full terms.
