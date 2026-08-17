# Multi-Agent Orchestration Patterns for Bid Protest Analysis

This document describes the multi-agent architecture implemented in this skill, designed for execution across Google Agent Development Kit (ADK), Gemini Enterprise, Antigravity, LangGraph, or standalone Python orchestration.

---

## Architecture Blueprint

```
                             ┌──────────────────────────────┐
                             │        Legal Expert          │
                             │  (User / Principal Attorney) │
                             └──────────────┬───────────────┘
                                            │
                                            ▼
                             ┌──────────────────────────────┐
                             │       Root Orchestrator      │
                             │   - Timeliness & Standing    │
                             │   - Category Pipeline        │
                             └──────────────┬───────────────┘
                                            │
                    ┌───────────────────────┴───────────────────────┐
                    ▼                                               ▼
     ┌─────────────────────────────┐                 ┌─────────────────────────────┐
     │     Category Processor      │                 │     RFP Matrix Extractor    │
     │  - Section L vs Section M   │                 │  - Factor Weights & Ratings │
     └──────────────┬──────────────┘                 └──────────────┬──────────────┘
                    │                                               │
                    └───────────────────────┬───────────────────────┘
                                            │
                                            ▼
                             ┌──────────────────────────────┐
                             │     Protest Strategist       │
                             │  - Generates 8-Ground Audits │
                             │  - Multi-Query Formulations  │
                             └──────────────┬───────────────┘
                                            │
                                            ▼
                             ┌──────────────────────────────┐
                             │    Document Investigator     │
                             │  - Hybrid Search / Vertex    │
                             │  - Cross-Doc Evidence Mining │
                             └──────────────┬───────────────┘
                                            │
                                            ▼
                             ┌──────────────────────────────┐
                             │   Adversarial Critique Agent │
                             │  - Red Team / Agency Counsel │
                             │  - Pass / Fail / Follow-up   │
                             └──────────────┬───────────────┘
                                            │ Pass
                                            ▼
                             ┌──────────────────────────────┐
                             │   Report & Pleading Builder  │
                             │  - Markdown Master Report    │
                             │  - Formal GAO Filing Draft   │
                             └──────────────────────────────┘
```

---

## Agent Personas & Operational Specifications

### 1. Root Orchestrator
- **Objective**: Manage the global workflow, accept focus areas, and verify jurisdictional prerequisites:
  - **Timeliness Verification**: Calculates 5-day debriefing window (for CICA automatic stay) and 10-day GAO statutory limit under 4 C.F.R. § 21.2.
  - **Interested Party Standing**: Confirms protester was an actual offeror whose direct economic interest would be affected by the award (e.g., next in line for award under FAR 15.308).

### 2. Category Processor & RFP Matrix Extractor
- **Objective**: Deterministically parse Section L (instructions to offerors) and Section M (evaluation factors for award).
- **Extracted Baseline Structure**:
  - Evaluation factors, subfactors, and relative weight hierarchies.
  - Mandatory minimum requirements ("shall", "must", threshold metrics).
  - Adjectival rating definitions (Outstanding, Good, Acceptable, Marginal, Unacceptable).

### 3. Protest Strategist
- **Objective**: Generate tailored audit questions across the 8 primary protest grounds:
  - *Audit Question 1*: Did the agency evaluate any feature not specified in Section M?
  - *Audit Question 2*: Were mandatory Section L requirements waived for the awardee?
  - *Audit Question 3*: Did the agency evaluate identical strengths or weaknesses disparately?
  - *Audit Question 4*: Did the SSA document a rational tradeoff justifying why technical superiority was not selected?

### 4. Document Investigator
- **Objective**: Execute multi-query searches against the procurement corpus (RFP, proposals, TET, SSDD, Debriefing).
- **Accumulated Investigator Outputs**: Maintains structured findings with verbatim citations, page references, and extracted score deltas.

### 5. Adversarial Critique Agent ("The Agency Counsel Red Team")
- **Objective**: Rigorously stress-test every proposed ground from the perspective of Government Agency Defense Counsel.
- **Evaluation Criteria**:
  - **Criterion A: Agency Discretion**: Is this an area of broad agency discretion (e.g. subjective scoring nuance)?
  - **Criterion B: Competitive Prejudice**: Would correcting this error actually give the protester a substantial chance of winning the contract?
  - **Criterion C: Self-Contradiction**: Did the protester's own proposal commit a similar flaw?
- **Routing Decision**:
  - `PASS`: Strength rating >= 80% -> Sent to Report Summarizer.
  - `FAIL / FOLLOW-UP`: Sent back to Investigator with specific factual prompts.

### 6. Report Summarizer & Pleading Generator
- **Objective**: Synthesize the validated grounds into the standardized **Master Bid Protest Report (Markdown)** and **GAO Formal Protest Pleading**.
