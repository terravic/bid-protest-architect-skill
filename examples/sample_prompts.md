# Sample Prompts for Agent Execution

Use these prompts to execute the Bid Protest Architect Skill on real procurement files or on the included `synthetic_data/` benchmark package.

---

## Prompt 1: End-to-End Audit on User-Supplied Real Documents

```text
Run the Bid Protest Architect Skill on the procurement documents in <your_folder_path>/.

1. Verify timeliness and CICA automatic stay deadlines from our debriefing delivery and Q&A completion dates.
2. Parse Section L mandatory minimums and Section M evaluation weights into a structured baseline.
3. Cross-examine all 8 bid protest grounds across the solicitation, proposals, technical evaluation report, SSDD, and debriefing records.
4. Stress-test each potential ground from the agency defense perspective and retain only grounds with >= 80% viability.
5. Generate output/master_bid_protest_report.md, output/gao_formal_protest_filing.md, output/audit_results.json, and dashboard.html.
```

---

## Prompt 2: End-to-End Audit on the Synthetic Benchmark Package

```text
Execute the Bid Protest Architect Skill on the procurement package in synthetic_data/.

Analyze synthetic_data/solicitation_rfp_section_lm.md, synthetic_data/proposal_apex_protester.md, synthetic_data/proposal_nexus_awardee.md, synthetic_data/technical_evaluation_report.md, synthetic_data/ssdd_source_selection_decision.md, and synthetic_data/debriefing_letter.md, then generate the audit report, GAO pleading draft, and standalone dashboard.html.
```

---

## Prompt 3: Targeted Investigation of Mandatory Minimums & Unstated Criteria

```text
Focus on Factor 1 (Technical) and Factor 2 (Key Personnel) in our procurement files:
1. Compare how the TET evaluated each offeror's Key Personnel qualifications against Section L.4 mandatory minimums.
2. Check whether the TET assigned any weaknesses to our proposal for items absent from Section L and Section M.
3. Provide verbatim quotes, line citations, FAR authorities, and GAO decision numbers for each finding.
```

---

## Prompt 4: Statutory Timeliness & CICA Automatic Stay Calculation

```text
We received our written post-award debriefing on August 10, 2026, and the agency delivered written answers to our timely debriefing questions on August 14, 2026.
1. Calculate the exact deadline to file a GAO protest and trigger the automatic CICA stay of performance under 31 U.S.C. 3553(d)(4).
2. Calculate the 10-day statutory GAO filing deadline under 4 C.F.R. 21.2(a)(2).
3. List the interested-party standing requirements under 4 C.F.R. 21.0(a)(1).
```
