import os

files = {}

files['synthetic_data/solicitation_rfp_section_lm.md'] = """# SOLICITATION NO. HHS-CMS-2026-CLOUD-009
## Title: Federal Healthcare Infrastructure Security & Cloud Modernization (FHIS-CM)
**Issuing Agency**: Department of Health and Human Services (HHS) / Centers for Medicare & Medicaid Services (CMS)  
**Contract Type**: Firm-Fixed-Price (FFP)  
**Competition**: Full and Open Competition under FAR Part 15 (Contracting by Negotiation)  
**Date Issued**: April 15, 2026  

---

# SECTION L - INSTRUCTIONS, CONDITIONS, AND NOTICES TO OFFERORS

### L.1 General Submission Instructions
Offerors shall submit proposals organized into the following distinct volumes:
- Volume I: Factor 1 - Technical & Cloud Architecture Approach
- Volume II: Factor 2 - Key Personnel and Management Plan
- Volume III: Factor 3 - Past Performance
- Volume IV: Factor 4 - Cost/Price Proposal (Firm-Fixed-Price)

### L.2 Proposal Format and Page Limitations
All volumes must be in 11-point serif font, 1-inch margins.
- Volume I: Maximum 60 pages
- Volume II: Maximum 30 pages (including resumes and letters of commitment)
- Volume III: Maximum 20 pages (up to 3 past performance references)
- Volume IV: No page limit

### L.3 Instructions for Factor 1: Technical & Cloud Architecture Approach
Offerors must demonstrate a proven, secure multi-region cloud architecture meeting FedRAMP High baseline requirements, Zero Trust Architecture (NIST SP 800-207), and continuous automated compliance monitoring.
- **L.3.1 Mandatory SLA Requirement**: The contractor shall guarantee a minimum monthly service availability uptime of **99.99%** (excluding pre-approved scheduled maintenance). Proposals offering an availability SLA below 99.99% will be deemed non-compliant and ineligible for award.
- **L.3.2 Disaster Recovery (DR)**: Offerors must demonstrate an automated cloud-native RTO (Recovery Time Objective) under 15 minutes and RPO (Recovery Point Objective) under 1 minute across active-active cloud regions.

### L.4 Instructions for Factor 2: Key Personnel and Management Plan
The offeror shall propose resumes and signed letters of commitment for three (3) mandatory Key Personnel positions:
1. **Key Personnel Position 1: Lead Cloud Solutions Architect**
   - *Mandatory Minimum Qualification*: Minimum of **ten (10) years** of direct experience architecting federal cloud solutions in FedRAMP High authorized government cloud environments, holding active Certified Cloud Solutions Architect Professional certification and a current CISSP certification.
2. **Key Personnel Position 2: Chief Information Security Officer (CISO) / Security Lead**
   - *Mandatory Minimum Qualification*: Minimum of eight (8) years specialized federal cybersecurity experience and active CISSP/CISM certification.
3. **Key Personnel Position 3: Senior DevSecOps Engineering Lead**
   - *Mandatory Minimum Qualification*: Minimum of seven (7) years experience in CI/CD pipeline automation and container orchestration.

*Note*: Failure to satisfy the mandatory minimum qualifications for any Key Personnel position will result in a rating of Unacceptable for Factor 2.

### L.5 Instructions for Factor 3: Past Performance
Offerors shall submit up to three (3) relevant past performance references for contracts performed within the past three (3) years. To be considered "relevant", each reference must involve federal cloud engineering of **similar size (annual value >= $15,000,000 or total contract value >= $50,000,000)**, **scope (multi-region cloud migration, FedRAMP High)**, and **complexity (federal civilian/defense healthcare systems)**.

### L.6 Instructions for Factor 4: Cost/Price Proposal
Offerors shall submit firm-fixed-prices for the 1-year Base Period and four (4) 1-year Option Periods using the pricing template in Attachment J-4.

---

# SECTION M - EVALUATION FACTORS FOR AWARD

### M.1 Basis for Award (FAR 15.101-1 Best Value Tradeoff)
Award will be made to the responsible Offeror whose proposal conforms to the solicitation and represents the **Best Value** to the Government, price and non-price factors considered.

**Relative Importance of Factors**:
- **Factor 1 (Technical & Cloud Architecture Approach)** is the most important non-price factor.
- **Factor 1** is significantly more important than **Factor 2 (Key Personnel)**.
- **Factor 2** is more important than **Factor 3 (Past Performance)**.
- When combined, all non-price factors (**Factors 1, 2, and 3**) are **significantly more important than Factor 4 (Price)**.

As technical proposals become more equal in technical merit, price will become more important in the tradeoff decision. However, the Government is willing to pay a substantial price premium for superior technical merit and lower operational risk.

### M.2 Evaluation Ratings Scale
The Technical Evaluation Team (TET) will evaluate Factors 1 and 2 using the following adjectival rating scale:
- **Outstanding**: Proposal exceeds requirements in multiple significant ways; numerous strengths with no weaknesses; exceptionally low risk.
- **Good**: Proposal exceeds requirements; strengths outweigh any weaknesses; low risk.
- **Acceptable**: Proposal meets requirements; minimal weaknesses; moderate risk.
- **Marginal**: Proposal fails to meet some requirements; weaknesses outweigh strengths; high risk.
- **Unacceptable**: Proposal fails to satisfy mandatory minimum requirements; uncorrectable deficiencies.

Past Performance (Factor 3) will be evaluated as: Substantial Confidence, Satisfactory Confidence, Neutral Confidence, Limited Confidence, or No Confidence.

### M.3 Unstated Criteria Prohibition
Evaluation will be conducted strictly against the evaluation criteria set forth in Section M. No extraneous requirements, unstated preferences, or non-solicited capabilities will form the basis for assigning weaknesses or strengths.
"""

files['synthetic_data/proposal_apex_protester.md'] = """# PROPOSAL EXCERPT: OFFEROR APEX
**Solicitation**: HHS-CMS-2026-CLOUD-009 (FHIS-CM)  
**Offeror**: Apex Federal (CAGE: 4K9L2, UEI: 839201948)  
**Role**: Incumbent Prime Contractor  
**Submitted Price (Volume IV)**: $94,500,000.00 (Firm-Fixed-Price)  

---

## Volume I: Factor 1 - Technical & Cloud Architecture Approach

### 1.1 Architecture & Availability SLA (Section L.3.1 Compliance)
Apex guarantees a monthly service availability uptime SLA of **99.999%** ("Five Nines") across our multi-region FedRAMP High cloud deployment. This exceeds the mandatory Section L.3.1 requirement of 99.99%.
- **Active-Active Cross-Region Failover**: Sub-minute data synchronization across FedRAMP High government cloud regions (US-East / US-West). RTO is verified at 4.2 minutes (exceeding the 15-minute mandate), and RPO is 0 seconds with synchronous database replication.
- **Zero Trust Implementation**: NIST SP 800-207 compliant micro-segmentation, identity-aware proxies, automated mTLS encryption at rest and in transit (FIPS 140-3).

---

## Volume II: Factor 2 - Key Personnel and Management Plan

### 2.1 Proposed Key Personnel (Section L.4 Compliance)
1. **Lead Cloud Solutions Architect: Dr. Elena Vance, Ph.D.**
   - *Experience*: **14 years** of federal cloud architecture experience across FedRAMP High government cloud enclaves.
   - *Certifications*: Certified Cloud Solutions Architect - Professional (Active #CSA-99281), Certified Federal Cloud Fellow, CISSP (#498210, Current).
   - *Letter of Commitment*: Fully executed, enclosed on Page 12.
2. **CISO / Security Lead: Marcus Thorne**
   - *Experience*: 11 years federal cybersecurity leadership, CISSP, CISM.
3. **Senior DevSecOps Lead: Sarah Chen**
   - *Experience*: 9 years container orchestration and automated CI/CD deployment.

---

## Volume III: Factor 3 - Past Performance

### 3.1 Reference 1: Centers for Medicare & Medicaid Services - Current Cloud Platform (Incumbent Contract)
- **Contract Number**: HHS-CMS-2021-0044 | **Value**: $91,200,000.00 | **Period**: 2021 - 2026
- **Relevance**: Direct incumbent contract of identical size, scope, and complexity. Managed 150+ microservices on FedRAMP High government cloud infrastructure.
- **CPARS Rating**: Quality: Exceptional | Schedule: Exceptional | Cost Control: Exceptional | Management: Exceptional.

### 3.2 Reference 2: Defense Health Agency (DHA) - Electronic Health Record Cloud Enclave
- **Contract Number**: HT0011-22-C-0019 | **Value**: $64,500,000.00 | **Period**: 2022 - 2025
- **Relevance**: Highly relevant healthcare cloud modernization on FedRAMP High government cloud infrastructure.
- **CPARS Rating**: Quality: Exceptional | Management: Very Good | Regulatory Compliance: Exceptional.
"""

files['synthetic_data/proposal_nexus_awardee.md'] = """# PROPOSAL EXCERPT: OFFEROR NEXUS
**Solicitation**: HHS-CMS-2026-CLOUD-009 (FHIS-CM)  
**Offeror**: Nexus Systems (CAGE: 7Z8P1, UEI: 120495831)  
**Role**: Non-Incumbent Awardee  
**Submitted Price (Volume IV)**: $82,200,000.00 (Firm-Fixed-Price)  

---

## Volume I: Factor 1 - Technical & Cloud Architecture Approach

### 1.1 Architecture & Availability SLA (Section L.3.1 Compliance)
Nexus proposes a scalable commercial off-the-shelf container framework on public cloud infrastructure.
- **Target SLA**: Nexus targets a monthly availability of **99.95%** uptime for standard container instances during business operational hours.
- **Disaster Recovery**: RTO of 45 minutes using warm standby snapshot restore across availability zones.

---

## Volume II: Factor 2 - Key Personnel and Management Plan

### 2.1 Proposed Key Personnel (Section L.4 Compliance)
1. **Lead Cloud Solutions Architect: Johnathan Brooks**
   - *Experience*: **Four (4) years** of total IT cloud engineering experience (primarily commercial e-commerce web deployment, joined Nexus in 2023).
   - *Certifications*: Cloud Solutions Architect - Associate (Earned 2023). *Note: Does not possess Certified Cloud Solutions Architect Professional certification, and does not possess CISSP.*
   - *Letter of Commitment*: Enclosed.
2. **CISO / Security Lead: Robert Miller**
   - *Experience*: 5 years cybersecurity experience, entry-level security certification.
3. **Senior DevSecOps Lead: Travis Cole**
   - *Experience*: 6 years CI/CD pipeline automation.

---

## Volume III: Factor 3 - Past Performance

### 3.1 Reference 1: Retail Storefront Portal - E-Commerce Web Catalog Optimization
- **Customer**: Commercial Retail Client | **Value**: $3,200,000.00 | **Period**: 2024 - 2025
- **Description**: Replatformed e-commerce catalog to public cloud containers.
- **Relevance**: Commercial retail web deployment (Non-federal, non-government cloud, not FedRAMP High, value $3.2M vs $50M+ requirement).

### 3.2 Reference 2: State Department of Motor Vehicles - Web Portal
- **Customer**: State DOT | **Value**: $8,500,000.00 | **Period**: 2023 - 2024
- **Description**: Frontend web portal hosting.
"""

files['synthetic_data/technical_evaluation_report.md'] = """# TECHNICAL EVALUATION TEAM (TET) CONSENSUS EVALUATION REPORT
**Solicitation**: HHS-CMS-2026-CLOUD-009 (FHIS-CM)  
**Date of Consensus**: July 22, 2026  
**Chairperson**: Lead Technical Evaluator, CMS Office of Information Technology  

---

## 1. Summary of Consensus Ratings

| Offeror | Factor 1: Technical & Cloud Architecture | Factor 2: Key Personnel & Management | Factor 3: Past Performance | Factor 4: Evaluated Price |
|---|---|---|---|---|
| **Nexus Systems** | **Good** | **Acceptable** | **Very Good (Satisfactory Confidence)** | **$82,200,000.00** |
| **Apex Federal** | **Acceptable** | **Outstanding** | **Substantial Confidence** | **$94,500,000.00** |

---

## 2. Detailed Findings: Apex Federal (Incumbent)

### Factor 1: Technical & Cloud Architecture Approach - Rating: Acceptable
- **Strength 1**: Proposed 99.999% SLA exceeds requirements with multi-region FedRAMP High government cloud architecture.
- **Significant Weakness 1 (UNSTATED CRITERIA)**: The TET assigned a Significant Weakness because Apex "did not propose a dedicated on-premises physical datacenter hardware bridge facility to connect with legacy Baltimore CMS mainframe hardware." *(Note: Section L & M do not mention or require on-premises physical datacenter hardware).*
- **Overall Factor 1 Rationale**: Despite strong cloud design, the Significant Weakness regarding legacy mainframe hardware bridge reduced Apex's technical rating from Outstanding to Acceptable.

### Factor 2: Key Personnel and Management Plan - Rating: Outstanding
- **Strength 1**: Dr. Elena Vance possesses 14 years of federal cloud experience, active Certified Cloud Solutions Architect Professional, Certified Federal Cloud Fellow, and CISSP certifications.
- **Strength 2**: All three key personnel exceed mandatory experience thresholds with verified records.

### Factor 3: Past Performance - Rating: Substantial Confidence
- Both submitted references were directly relevant federal healthcare cloud contracts ($91.2M and $64.5M) with Exceptional CPARS ratings.

---

## 3. Detailed Findings: Nexus Systems (Awardee)

### Factor 1: Technical & Cloud Architecture Approach - Rating: Good
- **Strength 1**: Commercial microservice architecture is modular and cost-efficient.
- **Note on SLA (FAILURE TO ENFORCE MANDATORY MINIMUM)**: The TET noted that Nexus proposed a 99.95% availability SLA. The TET determined that "99.95% is acceptable for general web workloads," despite Section L.3.1 mandating a 99.99% minimum threshold. No deficiency was assigned.

### Factor 2: Key Personnel and Management Plan - Rating: Acceptable
- **Note on Lead Architect (DISPARATE TREATMENT / WAIVER OF MANDATORY MINIMUM)**: The TET evaluated Johnathan Brooks (Lead Cloud Architect). Although Mr. Brooks possesses only 4 years of cloud experience and lacks Cloud Architect Professional and CISSP certifications (Section L.4 mandated 10 years, Cloud Architect Professional, and CISSP), the TET stated: "The candidate possesses good commercial aptitude which compensates for the shortage in required years of experience." A rating of Acceptable was awarded.

### Factor 3: Past Performance - Rating: Satisfactory Confidence (Very Good)
- **Note on Relevance (FLAWED EVALUATION)**: Evaluated Retail Storefront Portal ($3.2M) and State DMV ($8.5M). Even though neither contract met the Section L.5 relevance threshold ($50M+ total value, FedRAMP High, federal healthcare cloud), the TET concluded that "commercial web hosting demonstrates general competence."
"""

files['synthetic_data/ssdd_source_selection_decision.md'] = """# SOURCE SELECTION DECISION DOCUMENT (SSDD)
**Solicitation**: HHS-CMS-2026-CLOUD-009  
**Program**: Federal Healthcare Infrastructure Security & Cloud Modernization (FHIS-CM)  
**Contracting Agency**: Department of Health and Human Services (HHS) / CMS  
**Source Selection Authority (SSA)**: Deputy Director, Office of Acquisition and Grants Management  
**Date**: August 1, 2026  

---

## 1. Executive Summary and Award Decision
Pursuant to FAR 15.308, I have reviewed the Technical Evaluation Team (TET) Consensus Report and the Price Evaluation Report.

I hereby select **Nexus Systems** for award in the amount of **$82,200,000.00**.

---

## 2. Comparative Assessment and Tradeoff Analysis

### Summary Matrix
| Offeror | Factor 1: Technical | Factor 2: Key Personnel | Factor 3: Past Performance | Evaluated Price |
|---|---|---|---|---|
| **Nexus Systems** | **Good** | **Acceptable** | **Satisfactory Confidence** | **$82,200,000.00** |
| **Apex Federal** | **Acceptable** | **Outstanding** | **Substantial Confidence** | **$94,500,000.00** |

### SSA Tradeoff Rationale
1. Under **Factor 1 (Technical & Cloud Architecture)**, Nexus received a higher rating of **Good**, whereas Apex received **Acceptable** due to a Significant Weakness for failing to provide an on-premises physical datacenter hardware bridge.
2. Under **Factor 2 (Key Personnel)**, Apex was rated **Outstanding**, while Nexus was rated **Acceptable**.
3. Under **Factor 3 (Past Performance)**, Apex received **Substantial Confidence**, while Nexus received **Satisfactory Confidence**.
4. Under **Factor 4 (Price)**, Nexus is **$12,300,000.00 (13.0%) lower in price** than Apex.

### Flawed Tradeoff Finding
Because Nexus received a higher rating on the single most important non-price factor (Factor 1: Good vs. Acceptable), and because Nexus offered a price that is $12.3M lower than Apex, I find that Nexus represents the Best Value to the Government. I find that Apex's advantages in Key Personnel and Past Performance do not warrant paying a $12.3M price premium.

*(Signed)*  
**Source Selection Authority, HHS/CMS**  
Date: August 1, 2026
"""

files['synthetic_data/debriefing_letter.md'] = """# FORMAL WRITTEN POST-AWARD DEBRIEFING LETTER
**TO**: Apex Federal  
**Attn**: David Sterling, VP of Federal Contracts  
**FROM**: Contracting Officer, HHS / CMS Office of Acquisition  
**DATE OF DEBRIEFING DELIVERY**: August 10, 2026  
**SOLICITATION**: HHS-CMS-2026-CLOUD-009 (FHIS-CM)  
**AWARD NOTICE**: Contract awarded to Nexus Systems ($82,200,000.00)  

---

## 1. Debriefing Information (FAR 15.506)

Dear Mr. Sterling:
This letter constitutes your formal post-award debriefing pursuant to FAR 15.506.

### Summary of Ratings:
- **Apex Technical (Factor 1)**: Acceptable
  - *Identified Weakness*: Significant Weakness assigned for failure to include an on-premises datacenter hardware bridge for legacy Baltimore CMS mainframe connectivity.
- **Apex Key Personnel (Factor 2)**: Outstanding
- **Apex Past Performance (Factor 3)**: Substantial Confidence
- **Apex Evaluated Price (Factor 4)**: $94,500,000.00

### Awardee (Nexus Systems) Ratings:
- **Nexus Technical (Factor 1)**: Good (Evaluated Price: $82,200,000.00)
- **Nexus Key Personnel (Factor 2)**: Acceptable
- **Nexus Past Performance (Factor 3)**: Satisfactory Confidence

---

## 2. Timeliness and Debriefing Question Procedures
Under 4 C.F.R. 21.2(a)(2) and FAR 15.506:
- Offerors may submit written debriefing questions within two (2) business days (by **August 12, 2026**).
- Agency responses to timely debriefing questions will be delivered by **August 14, 2026**.
- The statutory debriefing will officially close on the date the Agency delivers written answers to timely submitted questions.
- A protest to the Government Accountability Office (GAO) will be timely if filed within five (5) days after the debriefing date to invoke the automatic stay of performance (CICA stay under 31 U.S.C. 3553(d)(4)), or within ten (10) days of when the basis of protest is known.
"""

for path, content in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f'Wrote: {path}')
print('All synthetic data files rebuilt cleanly.')
