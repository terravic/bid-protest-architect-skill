---
name: bid-protest-architect
description: >-
  Expert legal and technical analysis of federal government procurement documents
  (RFPs, proposals, TET reports, SSDDs, debriefings, discussions, OCI, cost realism)
  to identify, validate, and draft defensible GAO and Court of Federal Claims (COFC)
  bid protest grounds under the FAR, and build standalone interactive evidentiary
  dashboards. Use when analyzing real user-supplied contract awards, investigating
  evaluation discrepancies, calculating statutory CICA stay deadlines, diagnosing
  search retrieval accuracy, or generating formal bid protest audit reports,
  pleadings, and interactive dashboards.
---

# Bid Protest AI Architect Skill

This skill guides agents and legal specialists through the systematic audit of **user-supplied real federal procurement records** (or synthetic benchmark packages) under the Federal Acquisition Regulation (FAR) and Title 4 of the Code of Federal Regulations (4 C.F.R. Part 21).

> **Disclaimer**: This skill assists in auditing procurement packages and organizing factual grounds for protest. It provides analytical workflow assistance and does not constitute formal legal advice. All findings and filings should be reviewed by qualified legal counsel.

## Operational Workflow Overview

```
[Phase 0: Corpus Ingestion]    ──► Load user RFP, Proposals, TET, SSDD, Debriefing (.md/.txt/.docx/.pdf/.csv/.html/.json)
          │
          ▼
[Phase 1: Jurisdictional Gate] ──► Timeliness & Standing (5-Day CICA Stay, 10-Day GAO Rule)
          │
          ▼
[Phase 2: Baseline Extraction] ──► Parse Section L (Mandatory Minimums) & Section M (Weights)
          │
          ▼
[Phase 3: 8-Ground Audit]      ──► Cross-examine RFP vs TET vs SSDD vs Proposals (GR-01..GR-08)
          │
          ▼
[Phase 4: Adversarial Red-Team]──► Stress-test grounds from Agency Defense perspective
          │
          ▼
[Phase 5: Synthesis & UI]      ──► Emit Master Report, GAO Pleading Draft & Standalone dashboard.html
```

---

## Processing User-Supplied Real Procurement Data

This skill processes **real procurement documents** supplied either via the agent harness prompt or directly inside `dashboard.html`:

### Pathway A: Via Agent Harness Prompt & Python CLI
When a user provides paths to real procurement documents (a folder or individual files in `.md`, `.txt`, `.docx`, `.pdf`, `.csv`, `.html`, or `.json`) or pastes excerpts in chat:
1. **Stage or point directly to user files**:
   - Pass a user directory via `--data /path/to/user_protest_docs` or explicit files via `--files rfp.pdf awardee_excerpt.docx debriefing.md`.
   - If the user pasted raw excerpts in the prompt, save them into a workspace subfolder (e.g., `scratch/user_case/`) and run the pipeline against that directory.
2. **Enrich with LLM semantic legal analysis (optional hybrid mode)**:
   - For nuanced unstructured prose, inspect the loaded files, write structured JSON overrides (`--grounds-json scratch/agent_grounds.json` and/or `--index-json scratch/agent_index.json`), and pass them to the scripts so deterministic deadline math, report formatting, and `dashboard.html` visualization combine with deep legal reasoning.
3. **Execute the end-to-end pipeline**:
   ```bash
   python3 scripts/corpus_indexer.py --data <user_dir> --output scratch/procurement_index.json
   python3 scripts/bid_protest_analyzer.py --data <user_dir> --output output/master_bid_protest_report.md --json-output output/audit_results.json
   python3 scripts/generate_protest_filing.py --data <user_dir> --output output/gao_formal_protest_filing.md
   python3 scripts/build_dashboard.py --data <user_dir> --output dashboard.html
   ```

### Pathway B: Direct Multi-Document Loading Inside `dashboard.html`
Users can open `dashboard.html` directly from disk (`file://`), in the Canvas artifact preview, or over HTTP (`python3 scripts/build_dashboard.py --serve`), click **Load Corpus**, and drag-and-drop or paste any combination of real procurement documents (`.md`, `.txt`, `.docx`, `.pdf`, `.csv`, `.html`, `.json`) to recompute statutory deadlines, compliance matrices, 8-ground viability scores, 3D provenance graphs, and downloadable GAO pleadings directly in the browser.

---

## Step-by-Step Execution Procedure

### Step 1: Verify Jurisdictional Prerequisites (Timeliness & Standing)
1. **Check Debriefing Dates**:
   - Extract the date the written debriefing was received and the date the agency concluded written responses to debriefing questions.
   - Run or reference [TimelinessCalculator](scripts/bid_protest_analyzer.py):
     - **CICA Automatic Stay Window**: Must file within **five (5) calendar days** of debriefing completion (*31 U.S.C. § 3553(d)(4)*), rolling weekend expirations to the next business day.
     - **GAO Statutory Filing Deadline**: Must file within **ten (10) calendar days** (*4 C.F.R. § 21.2(a)(2)*).
2. **Verify Interested Party Standing**:
   - Confirm protester was an actual offeror with direct economic interest who is next in line for award (*4 C.F.R. § 21.0(a)(1)*).
   - Review [protest_viability_checklist.md](resources/checklists/protest_viability_checklist.md).

### Step 2: Establish the RFP Evaluation Baseline
1. Parse **Section L** (Instructions to Offerors) for binding mandatory requirements (`shall`, `must`, minimum years of experience, certifications, SLAs, RTOs).
2. Parse **Section M** (Evaluation Factors for Award) for relative factor hierarchies (e.g. *Non-Price factors combined are significantly more important than Price*).
3. Extract the adjectival rating scale definitions (Outstanding, Good, Acceptable, Marginal, Unacceptable).

### Step 3: Execute the 8-Ground Cross-Examination Audit
Investigate the procurement corpus across the 8 primary protest grounds defined in [protest_grounds_taxonomy.md](references/protest_grounds_taxonomy.md):
- **Ground 1 (`GR-01` Unstated Criteria)**: Cross-check every assigned weakness in the TET report against Section M factors (*FAR 15.305; Alion Science & Tech.*).
- **Ground 2 (`GR-02` Disparate Treatment)**: Compare offeror evaluations side-by-side on identical features (*FAR 1.102-2; Raytheon Co.*).
- **Ground 3 (`GR-03` Waiver of Mandatory Requirements)**: Verify if the awardee failed any Section L mandatory minimums (*FAR 15.206; ArmorWorks Enterprises*).
- **Ground 4 (`GR-04` Flawed Past Performance)**: Verify awardee reference relevance against dollar thresholds and scope (*FAR 15.305(a)(2); Fluor Fed. Sols.*).
- **Ground 5 (`GR-05` Defective Tradeoff Decision)**: Verify whether the SSA conducted a qualitative tradeoff or mechanically converted the evaluation into an improper LPTA (*FAR 15.308; Blue Rock Structures*).
- **Grounds 6–8 (`GR-06` Discussions / `GR-07` OCI / `GR-08` Cost & Price Realism)**: Audit Evaluation Notices (*FAR 15.306(d)*), unmitigated conflicts (*FAR 9.5*), and realism adjustments (*FAR 15.404-1(d)*).

### Step 4: Apply Adversarial Red-Team Critique
Stress-test each potential count before inclusion:
1. **Agency Discretion Test**: Can the agency defend this as a matter of reasonable evaluative discretion?
2. **Prejudice Test (*Bannum* Standard)**: But for this error, would the protester have had a substantial chance of receiving award?
3. Only advance grounds with a **Viability Rating >= 80%**.

### Step 5: Generate Master Report, Formal Pleading & Interactive Dashboard
Follow [`DESIGN.md`](DESIGN.md) when emitting or customizing `dashboard.html` via [`build_dashboard.py`](scripts/build_dashboard.py).

---

## Technical Helpers & Scripts

- [corpus_indexer.py](scripts/corpus_indexer.py): Multi-format procurement parser (`.md`, `.txt`, `.docx`, `.pdf`, `.csv`, `.html`, `.json`) and quantitative compliance extractor.
- [bid_protest_analyzer.py](scripts/bid_protest_analyzer.py): Dynamic 8-ground FAR/GAO analyzer, prejudice calculator, and Markdown/JSON report builder.
- [generate_protest_filing.py](scripts/generate_protest_filing.py): Generates formal legal pleadings formatted for GAO docketing from any indexed corpus.
- [search_diagnostics.py](scripts/search_diagnostics.py): Corpus retrieval accuracy comparator across Naive, Direct Keyword, and Optimized Legal RAG queries.
- [build_dashboard.py](scripts/build_dashboard.py): Standalone `dashboard.html` compiler with native OS theme fallback and optional live HTTP/SSE server.

---

## Detailed References

- [DESIGN.md](DESIGN.md): Visual hierarchy, theme tokens, typography, and interactive component specification for `dashboard.html`.
- [gao_precedents_handbook.md](references/gao_precedents_handbook.md): Case law principles, standards of review, and landmark citations.
- [protest_grounds_taxonomy.md](references/protest_grounds_taxonomy.md): 8-ground legal taxonomy with required documentary evidence.
- [search_optimization_guide.md](references/search_optimization_guide.md): Guide to legal term-of-art query expansion and hybrid RAG retrieval.
- [agent_orchestration_patterns.md](references/agent_orchestration_patterns.md): Multi-agent architecture specifications.
