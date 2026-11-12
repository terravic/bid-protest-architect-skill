# Synthetic Federal Procurement Dataset: Healthcare Cloud Modernization

This dataset is a synthetic, non-PHI/PII federal procurement package modeled on a civilian healthcare agency procurement (Department of Health and Human Services / Centers for Medicare & Medicaid Services).

## Scenario Overview
- **RFP Number**: `HHS-CMS-2026-CLOUD-009`
- **Project Title**: Federal Healthcare Infrastructure Security & Cloud Modernization (FHIS-CM)
- **Contract Type**: Firm-Fixed-Price (FFP)
- **Procurement Strategy**: Best Value Tradeoff (FAR 15.101-1), where Non-Price Factors combined are significantly more important than Price.
- **Estimated Value**: $80,000,000 - $100,000,000 over 5 years (1 Base Year + 4 Option Years)
- **Competitors**:
  - **Apex Federal (Protester / Incumbent)**: Total Evaluated Price: $94,500,000.00. Compliant technical approach, FedRAMP High, 99.999% uptime SLA, 14-year veteran Lead Cloud Architect.
  - **Nexus Systems (Awardee / Challenger)**: Total Evaluated Price: $82,200,000.00. Proposed 99.95% SLA (below mandatory minimum), under-qualified key personnel, commercial retail past performance.

---

## Embedded Protest Grounds (For Testing & Verification)

The dataset contains 5 bid protest grounds embedded for verification by the analyzer and diagnostic tools:

| # | Protest Ground | FAR / Legal Citation | Embedded Fact / Flaw in Data |
|---|---|---|---|
| **1** | **Unstated Evaluation Criteria** | FAR 15.303, FAR 15.305 | TET assigned a "Significant Weakness" to Apex for lacking an "on-premises physical datacenter hardware bridge facility", which was not required in Section L or M. |
| **2** | **Waiver of Key Personnel Minimums** | FAR 15.206, FAR 15.305 | Nexus proposed a Lead Cloud Architect with 4 years of cloud experience (Section L mandatory minimum was 10 years and required certifications). Agency waived this requirement with an "Acceptable" rating. |
| **3** | **Failure to Enforce Mandatory SLA Minimum** | FAR 15.206, FAR 15.305 | Nexus proposed a 99.95% monthly uptime SLA. Section L.3.1 established a mandatory minimum threshold of 99.99% monthly availability. |
| **4** | **Flawed Past Performance Evaluation** | FAR 15.305(a)(2) | Agency rated Nexus "Satisfactory Confidence (Very Good)" on Past Performance based on commercial/state web contracts ($3.2M and $8.5M) despite Section L.5 requiring $50M+ federal healthcare cloud scope. |
| **5** | **Defective Best Value Tradeoff Decision** | FAR 15.308 | The Source Selection Authority (SSA) mechanically selected the lower-priced offeror based on flawed underlying ratings despite Section M stating non-price factors were significantly more important than Price. |

---

## Included Files in this Package

1. `synthetic_data/solicitation_rfp_section_lm.md` - Solicitation RFP Sections L (Instructions to Offerors) and M (Evaluation Factors for Award).
2. `synthetic_data/proposal_apex_protester.md` - Excerpt of Protester (Apex Federal) technical, personnel, and past performance submission.
3. `synthetic_data/proposal_nexus_awardee.md` - Excerpt of Awardee (Nexus Systems) technical, personnel, and past performance submission.
4. `synthetic_data/technical_evaluation_report.md` - Technical Evaluation Team (TET) consensus scoring report.
5. `synthetic_data/ssdd_source_selection_decision.md` - Source Selection Decision Document (SSDD) signed by the Source Selection Authority (SSA).
6. `synthetic_data/debriefing_letter.md` - Post-award written debriefing provided to Apex Federal with statutory debriefing timeline.
