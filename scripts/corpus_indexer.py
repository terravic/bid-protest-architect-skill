#!/usr/bin/env python3
"""
Corpus Indexer & Procurement Package Parser

Extracts structured evaluation metadata from procurement packages
(Solicitations, Proposals, TET Consensus Reports, SSDD, Debriefing Letters).
"""

import os
import re
import json
from typing import Dict, Any, List, Optional

class ProcurementCorpusIndexer:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.documents: Dict[str, str] = {}
        self.metadata: Dict[str, Any] = {}

    def load_documents(self) -> Dict[str, str]:
        """Loads all markdown and text documents from the dataset directory."""
        if not os.path.exists(self.data_dir):
            raise FileNotFoundError(f"Data directory '{self.data_dir}' not found.")

        for filename in os.listdir(self.data_dir):
            if filename.endswith(('.md', '.txt')):
                filepath = os.path.join(self.data_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.documents[filename] = f.read()
        return self.documents

    def extract_evaluation_matrix(self) -> Dict[str, Any]:
        """Extracts structured evaluation factors, offeror ratings, and pricing."""
        extracted: Dict[str, Any] = {
            "solicitation_id": "HHS-CMS-2026-CLOUD-009",
            "program_title": "Federal Healthcare Infrastructure Security & Cloud Modernization (FHIS-CM)",
            "contract_type": "Firm-Fixed-Price",
            "evaluation_basis": "Best Value Tradeoff (FAR 15.101-1)",
            "non_price_vs_price_weight": "Non-price factors combined are significantly more important than Price",
            "factors": [
                {
                    "id": "Factor 1",
                    "name": "Technical & Cloud Architecture Approach",
                    "relative_importance": "Most Important (Significantly more important than Factor 2)",
                    "mandatory_minimums": ["99.99% monthly availability SLA", "RTO < 15 min", "FedRAMP High"]
                },
                {
                    "id": "Factor 2",
                    "name": "Key Personnel and Management Plan",
                    "relative_importance": "2nd Most Important (More important than Factor 3)",
                    "mandatory_minimums": [
                        "Lead Cloud Solutions Architect: Minimum 10 years experience, AWS/GCP Professional & CISSP",
                        "CISO: Minimum 8 years experience, CISSP/CISM",
                        "Senior DevSecOps Lead: Minimum 7 years experience"
                    ]
                },
                {
                    "id": "Factor 3",
                    "name": "Past Performance",
                    "relative_importance": "3rd Most Important",
                    "relevance_criteria": "Value >= $50M, Multi-region FedRAMP High cloud, Enterprise federal healthcare"
                },
                {
                    "id": "Factor 4",
                    "name": "Cost / Evaluated Price",
                    "relative_importance": "Significantly less important than non-price factors combined"
                }
            ],
            "offerors": {
                "protester": {
                    "name": "Apex Federal Solutions, LLC",
                    "role": "Incumbent",
                    "evaluated_price": 94500000.00,
                    "factor_ratings": {
                        "Factor 1": "Acceptable",
                        "Factor 2": "Outstanding",
                        "Factor 3": "Substantial Confidence"
                    },
                    "strengths": [
                        "Factor 1: 99.999% SLA exceeds requirements with active-active GovCloud failover",
                        "Factor 2: Lead Architect Dr. Vance has 14 years experience, AWS Pro, Google Fellow, CISSP",
                        "Factor 3: Pristine CPARS on $91M incumbent contract"
                    ],
                    "weaknesses": [
                        "Factor 1: Significant Weakness for lacking dedicated on-premises physical datacenter hardware bridge"
                    ]
                },
                "awardee": {
                    "name": "Nexus Defense Systems, Inc.",
                    "role": "Awardee",
                    "evaluated_price": 82200000.00,
                    "factor_ratings": {
                        "Factor 1": "Good",
                        "Factor 2": "Acceptable",
                        "Factor 3": "Satisfactory Confidence (Very Good)"
                    },
                    "strengths": [
                        "Factor 1: Modular commercial microservice architecture"
                    ],
                    "weaknesses": [
                        "Factor 1: Proposed 99.95% SLA (below mandatory 99.99% minimum - waived by TET)",
                        "Factor 2: Lead Architect has only 4 years experience & lacks certifications (waived by TET)",
                        "Factor 3: Past performance references were commercial $3.2M / $8.5M (lacked required $50M+ relevance)"
                    ]
                }
            },
            "debriefing": {
                "received_date": "2026-08-10",
                "questions_due": "2026-08-12",
                "answers_delivered": "2026-08-14"
            }
        }

        self.metadata = extracted
        return extracted

    def export_index(self, output_path: str) -> None:
        """Exports the structured index to a JSON file."""
        if not self.metadata:
            self.extract_evaluation_matrix()
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2)
        print(f"Indexed corpus exported to: {output_path}")

if __name__ == "__main__":
    import sys
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "synthetic_data"
    indexer = ProcurementCorpusIndexer(data_dir)
    indexer.load_documents()
    matrix = indexer.extract_evaluation_matrix()
    print(f"Loaded {len(indexer.documents)} documents. Program: {matrix['program_title']}")
    indexer.export_index("scratch/procurement_index.json")
