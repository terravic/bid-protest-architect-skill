---
name: bid-protest-architect
description: >-
  Expert legal and technical analysis of federal government procurement documents
  (RFPs, proposals, TET reports, SSDDs, debriefings) to identify, validate, and draft
  defensible GAO and Court of Federal Claims (COFC) bid protest grounds under the FAR.
  Use when analyzing contract awards, investigating evaluation discrepancies, calculating
  statutory CICA stay deadlines, diagnosing search retrieval accuracy, or generating
  formal bid protest audit reports and pleadings.
---

# Bid Protest AI Architect Skill

This skill guides agents and legal specialists through the systematic audit of federal procurement records under the Federal Acquisition Regulation (FAR) and Title 4 of the Code of Federal Regulations (4 C.F.R. Part 21).

> **Disclaimer**: This skill assists in auditing procurement packages and organizing factual grounds for protest. It provides analytical workflow assistance and does not constitute formal legal advice. All findings and filings should be reviewed by qualified legal counsel.

## Operational Workflow Overview

```
[Phase 1: Jurisdictional Gate] ──► Timeliness & Standing (5-Day CICA Stay, 10-Day GAO Rule)
          │
          ▼
[Phase 2: Baseline Extraction] ──► Parse Section L (Mandatory Minimums) & Section M (Weights)
          │
          ▼
[Phase 3: 8-Ground Audit]      ──► Cross-examine RFP vs TET vs SSDD vs Proposals
          │
          ▼
[Phase 4: Adversarial Red-Team]──► Stress-test grounds from Agency Defense perspective
          │
          ▼
[Phase 5: Synthesis]           ──► Generate Master Audit Report & Formal GAO Pleading Draft
```

---

## Step-by-Step Execution Procedure

### Step 1: Verify Jurisdictional Prerequisites (Timeliness & Standing)
1. **Check Debriefing Dates**:
   - Extract the date the written debriefing was received and the date the agency concluded written responses to debriefing questions.
   - Run or reference [TimelinessCalculator](scripts/bid_protest_analyzer.py):
     - **CICA Automatic Stay Window**: Must file within **five (5) calendar days** of debriefing completion (*31 U.S.C. § 3553(d)(4)*).
     - **GAO Statutory Filing Deadline**: Must file within **ten (10) calendar days** (*4 C.F.R. § 21.2(a)(2)*).
2. **Verify Interested Party Standing**:
   - Confirm protester was an actual offeror with direct economic interest who is next in line for award (*4 C.F.R. § 21.0(a)(1)*).
   - Review [protest_viability_checklist.md](resources/checklists/protest_viability_checklist.md).

### Step 2: Establish the RFP Evaluation Baseline
1. Parse **Section L** (Instructions to Offerors) for binding mandatory requirements (`shall`, `must`, minimum years of experience, certifications, SLAs).
2. Parse **Section M** (Evaluation Factors for Award) for relative factor hierarchies (e.g. *Non-Price factors combined are significantly more important than Price*).
3. Extract the adjectival rating scale definitions (Outstanding, Good, Acceptable, Marginal, Unacceptable).

### Step 3: Execute the 8-Ground Cross-Examination Audit
Investigate the procurement corpus across the 8 primary protest grounds defined in [protest_grounds_taxonomy.md](references/protest_grounds_taxonomy.md):
- **Ground 1 (Unstated Criteria)**: Cross-check every assigned weakness in the TET report against Section M factors (*FAR 15.305; Alion Science & Tech.*).
- **Ground 2 (Disparate Treatment)**: Compare offeror evaluations side-by-side on identical features (*FAR 1.102-2; Raytheon Co.*).
- **Ground 3 (Waiver of Mandatory Requirements)**: Verify if the awardee failed any Section L mandatory minimums (*FAR 15.206; ArmorWorks Enterprises*).
- **Ground 4 (Flawed Past Performance)**: Verify awardee reference relevance against dollar thresholds and FedRAMP scope (*FAR 15.305(a)(2); Fluor Fed. Sols.*).
- **Ground 5 (Defective Tradeoff Decision)**: Verify whether the SSA conducted a qualitative tradeoff or mechanically converted the evaluation into an improper LPTA (*FAR 15.308; Blue Rock Structures*).
- **Grounds 6-8 (Discussions / OCI / Price Realism)**: Review for unequal discussions (*FAR 15.306*) and conflicts of interest (*FAR 9.5*).

### Step 4: Apply Adversarial Red-Team Critique
Stress-test each potential count before inclusion:
1. **Agency Discretion Test**: Can the agency defend this as a matter of reasonable evaluative discretion?
2. **Prejudice Test (*Bannum* Standard)**: But for this error, would the protester have had a substantial chance of receiving award?
3. Only advance grounds with a **Viability Rating >= 80%**.

### Step 5: Generate Master Report & Formal Pleading Draft
1. Use the template in [bid_protest_report_template.md](resources/templates/bid_protest_report_template.md).
2. Or execute the automated CLI:
   ```bash
   python3 scripts/bid_protest_analyzer.py --data synthetic_data --output output/master_bid_protest_report.md
   python3 scripts/generate_protest_filing.py --data synthetic_data --output output/gao_formal_protest_filing.md
   ```

---

## Technical Helpers & Scripts

- [bid_protest_analyzer.py](scripts/bid_protest_analyzer.py): Automated end-to-end legal ground analyzer, prejudice calculator, and markdown report builder.
- [search_diagnostics.py](scripts/search_diagnostics.py): Benchmark comparator diagnosing retrieval accuracy between ADK tool wrappers, direct UI queries, and optimized legal RAG.
- [corpus_indexer.py](scripts/corpus_indexer.py): Structured JSON parser and evaluation matrix extractor.
- [generate_protest_filing.py](scripts/generate_protest_filing.py): Generates formal legal pleadings formatted for GAO docketing.

---

## Detailed References

- [gao_precedents_handbook.md](references/gao_precedents_handbook.md): Case law principles, standards of review, and landmark citations.
- [protest_grounds_taxonomy.md](references/protest_grounds_taxonomy.md): 8-ground legal taxonomy with required documentary evidence.
- [search_optimization_guide.md](references/search_optimization_guide.md): Guide to legal term-of-art query expansion and hybrid RAG retrieval.
- [agent_orchestration_patterns.md](references/agent_orchestration_patterns.md): Multi-agent architecture specifications.
