# Synthetic Federal Procurement Dataset: Project TITAN-HEALTH / Cloud Modernization

This dataset is a fully synthetic, non-PHI/PII federal procurement package modeled on a realistic civilian/defense healthcare agency procurement (*U.S. Department of Health and Human Services / Centers for Medicare & Medicaid Services*).

## Scenario Overview
- **RFP Number**: `HHS-CMS-2026-CLOUD-009`
- **Project Title**: Federal Healthcare Infrastructure Security & Cloud Modernization (FHIS-CM)
- **Contract Type**: Firm-Fixed-Price (FFP) with Performance Incentives
- **Procurement Strategy**: Best Value Tradeoff (FAR 15.101-1), where Non-Price Factors combined are significantly more important than Price.
- **Estimated Value**: 0M - 00M over 5 years (1 Base Year + 4 Option Years)
- **Competitors**:
  - **Apex Federal Solutions (Protester / Incumbent)**: Total Evaluated Price: 4,500,000. Exceptional technical score, FedRAMP High, proven 99.999% uptime, 10+ year veteran cloud architects.
  - **Nexus Defense Systems (Awardee / Challenger)**: Total Evaluated Price: 2,200,000. Lower technical rating, proposed 99.95% SLA (below mandatory minimum), under-qualified key personnel, commercial past performance.

---

## Embedded Protest Grounds (For Testing & Verification)

The dataset contains **5 distinct, legally viable bid protest grounds** intentionally embedded for detection by the skill and diagnostic tools:

| # | Protest Ground | FAR / Legal Citation | Embedded Fact / Flaw in Data |
|---|---|---|---|
| **1** | **Unstated Evaluation Criteria** | FAR 15.303, FAR 15.305 | TET assigned a "Significant Weakness" to Apex for lacking an "on-premises legacy mainframe bridge facility", which was never required in Section L or M. |
| **2** | **Disparate / Unequal Treatment in Key Personnel** | FAR 1.102-2(c)(3), FAR 15.305 | Nexus proposed a Lead Cloud Architect with only 4 years of cloud experience (Section L mandatory minimum was 10 years). Agency waived this requirement for Nexus with an "Acceptable" rating while strictly penalizing Apex. |
| **3** | **Failure to Enforce Mandatory Minimum Requirement** | FAR 15.206, FAR 15.305 | Nexus proposed a 99.95% monthly uptime SLA. Section L.4.2 specifically established a mandatory minimum threshold of 99.99% monthly availability. Nexus proposal was non-compliant. |
| **4** | **Flawed Past Performance Evaluation** | FAR 15.305(a)(2) | Agency rated Nexus "Very Good" on Past Performance based on a commercial retail web app contract (M value) despite Section M requirement that past performance must be of similar size, scope (0M+), and complexity (GovCloud / FedRAMP High). |
| **5** | **Defective Best Value Tradeoff Decision** | FAR 15.308 | The Source Selection Authority (SSA) mechanically selected the lowest-priced offeror without conducting the required qualitative tradeoff analysis or explaining why technical superiority was discarded, despite Section M stating Technical was significantly more important than Price. |

---

## Included Files in this Package

1. `solicitation_rfp_section_lm.md` - Solicitation RFP Sections L (Instructions to Offerors) and M (Evaluation Factors for Award).
2. `proposal_apex_protester.md` - Excerpt of Protester (Apex Federal Solutions) technical, personnel, and past performance submission.
3. `proposal_nexus_awardee.md` - Excerpt of Awardee (Nexus Defense Systems) technical, personnel, and past performance submission.
4. `technical_evaluation_report.md` - Source Selection Evaluation Board (SSEB) / Technical Evaluation Team (TET) consensus scoring report.
5. `ssdd_source_selection_decision.md` - Official Source Selection Decision Document (SSDD) signed by the Source Selection Authority (SSA).
6. `debriefing_letter.md` - Post-award written debriefing provided to Apex Federal Solutions with formal debriefing timeline.
