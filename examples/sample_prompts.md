# Plug-and-Play Sample Prompts for Agent Harnesses

Use these sample prompts to interact with the Bid Protest Architect Skill across **Gemini Enterprise App**, **Antigravity**, **Claude**, **ChatGPT / OpenAI Assistants**, and **Google ADK**.

---

## Prompt 1: Complete End-to-End Bid Protest Audit (Recommended)

```text
Please execute the Bid Protest Architect Skill on our procurement package located in the synthetic_data/ directory.

Analyze the solicitation (solicitation_rfp_section_lm.md), the protester's proposal (proposal_apex_protester.md), the awardee's proposal (proposal_nexus_awardee.md), the technical evaluation report (technical_evaluation_report.md), the SSDD (ssdd_source_selection_decision.md), and our debriefing letter (debriefing_letter.md).

Please:
1. Verify timeliness and CICA stay deadlines based on our debriefing date.
2. Extract Section L and Section M requirements into an evaluation baseline.
3. Investigate all 8 standard bid protest grounds (especially unstated criteria, disparate treatment, mandatory minimums, past performance, and tradeoff rationales).
4. Apply an adversarial critique red-team to eliminate weak arguments.
5. Generate the complete Master Bid Protest Audit Report with FAR citations and GAO precedents.
```

---

## Prompt 2: Targeted Investigation for Disparate Treatment & Unstated Criteria

```text
Focus your analysis on Factor 1 (Technical) and Factor 2 (Key Personnel) in our procurement documents:
1. Compare how the TET evaluated Apex vs Nexus on Key Personnel qualifications against Section L.4 requirements.
2. Check if the TET assigned any weaknesses to Apex that were not listed as evaluation criteria in Section M.
3. Provide the exact quotes, page numbers, and applicable GAO case citations for any identified grounds.
```

---

## Prompt 3: Timeliness & CICA Automatic Stay Calculator

```text
We received our post-award debriefing letter on August 10, 2026. The agency answered our debriefing questions on August 14, 2026.
1. Calculate our exact deadline to file a GAO protest and obtain an automatic CICA stay of contract performance.
2. Calculate the final statutory GAO filing deadline.
3. Confirm if we have interested party standing to file.
```

---

## Prompt 4: Running Standalone Python Scripts & Search Diagnostics

```text
Run the automated bid protest analyzer CLI on the synthetic data package and export the report to output/protest_report.md. Also run the search diagnostics script to compare direct API vs hybrid retrieval accuracy.
```
