# Multi-Agent Orchestration Patterns for Bid Protest Analysis

This document specifies the multi-stage orchestration architecture implemented in this skill for automated or interactive Python execution.

---

## Architecture Blueprint

```
                             +------------------------------+
                             |       Legal Specialist       |
                             |  (User / Reviewing Counsel)  |
                             +--------------+---------------+
                                            |
                                            v
                             +------------------------------+
                             |       Root Orchestrator      |
                             |   - Timeliness & Standing    |
                             |   - Category Pipeline        |
                             +--------------+---------------+
                                            |
                    +-----------------------+-----------------------+
                    v                                               v
     +-----------------------------+                 +-----------------------------+
     |     Category Processor      |                 |     RFP Matrix Extractor    |
     |  - Section L vs Section M   |                 |  - Factor Weights & Ratings |
     +--------------+--------------+                 +--------------+--------------+
                    |                                               |
                    +-----------------------+-----------------------+
                                            |
                                            v
                             +------------------------------+
                             |     Protest Strategist       |
                             |  - Generates 8-Ground Audits |
                             |  - Multi-Query Formulations  |
                             +--------------+---------------+
                                            |
                                            v
                             +------------------------------+
                             |    Document Investigator     |
                             |  - Hybrid Lexical Search     |
                             |  - Cross-Doc Evidence Mining |
                             +--------------+---------------+
                                            |
                                            v
                             +------------------------------+
                             |   Adversarial Critique Gate  |
                             |  - Agency Defense Red Team   |
                             |  - Pass / Fail / Follow-up   |
                             +--------------+---------------+
                                            | Pass
                                            v
                             +------------------------------+
                             |   Report & Pleading Builder  |
                             |  - Markdown Master Report    |
                             |  - Formal GAO Filing Draft   |
                             |  - Interactive Dashboard     |
                             +------------------------------+
```

---

## Stage Specifications

### 1. Root Orchestrator
- **Objective**: Coordinate workflow execution, accept user document paths, and verify jurisdictional prerequisites:
  - **Timeliness Verification**: Calculates the 5-day debriefing window (for the CICA automatic stay) and the 10-day GAO statutory filing deadline under 4 C.F.R. 21.2.
  - **Interested Party Standing**: Confirms the protester was an actual offeror whose direct economic interest is affected by the award (e.g., next in line for award under FAR 15.308).

### 2. Category Processor & RFP Matrix Extractor
- **Objective**: Parse Section L (instructions to offerors) and Section M (evaluation factors for award).
- **Extracted Baseline Structure**:
  - Evaluation factors, subfactors, and relative weight hierarchies.
  - Mandatory minimum requirements (`shall`, `must`, numerical threshold metrics).
  - Adjectival rating definitions (Outstanding, Good, Acceptable, Marginal, Unacceptable).

### 3. Protest Strategist
- **Objective**: Formulate targeted audit checks across the 8 primary protest grounds:
  - *Check 1*: Did the agency penalize a proposal for omitting a feature not specified in Section M?
  - *Check 2*: Were mandatory Section L requirements waived for the awardee without solicitation amendment?
  - *Check 3*: Did the agency evaluate indistinguishable proposal features unequally?
  - *Check 4*: Did the SSA document a qualitative tradeoff justifying price versus technical superiority?

### 4. Document Investigator
- **Objective**: Execute multi-query searches across the loaded procurement corpus (RFP, proposals, TET report, SSDD, debriefing, discussions, OCI, cost worksheets).
- **Outputs**: Structured findings with verbatim excerpts, `file:line` provenance citations, and quantitative score variances.

### 5. Adversarial Critique Gate ("Agency Defense Red Team")
- **Objective**: Stress-test each proposed ground from the perspective of agency defense counsel:
  - **Criterion A (Agency Discretion)**: Can the finding be defended as reasonable technical judgment?
  - **Criterion B (Competitive Prejudice)**: But for this error, would the protester have had a substantial chance of receiving the award?
  - **Criterion C (Consistency)**: Did the protester's proposal satisfy the same requirement?
- **Routing Decision**:
  - `PASS`: Viability rating >= 80% advances to synthesis.
  - `FAIL / FOLLOW-UP`: Filtered out or returned for supplemental document review.

### 6. Report, Pleading & Dashboard Builder
- **Objective**: Emit `output/master_bid_protest_report.md`, `output/gao_formal_protest_filing.md`, `output/audit_results.json`, and standalone `dashboard.html`.
