# Legal & Procurement Corpus Retrieval Guide

## 1. Principles of Legal & Procurement Information Retrieval

Analysis of federal procurement records presents distinct retrieval requirements compared to general document search:

1. **Specificity of Binding Solicitation Terms**:
   - In federal procurement, terms such as `shall`, `must`, and `mandatory minimum` carry binding legal weight under FAR 15.206.
   - Locating mandatory qualifications requires matching exact Section L clauses rather than general narrative summaries.

2. **Tabular Structure Preservation**:
   - Solicitations and source selection records rely on structured matrices (Section M evaluation factors, adjectival scoring tables, CPARS past performance records, and pricing schedules).
   - Preserving row and column associations maintains alignment between offeror proposals and evaluator consensus notes.

3. **Multi-Faceted Audit Queries**:
   - Effective procurement audits query across four linked dimensions: solicitation clauses, offeror commitments, evaluator scoring justifications, and FAR regulatory standards.

---

## 2. Retrieval Pipeline Architecture

The skill implements a structured 4-variant query expansion pipeline:

```
[Audit Objective]
        |
        v
[Legal Query Expander] ---> Generates 4 Query Variants:
        |                    +-- 1. Solicitation Clause Pattern (e.g., "Section L.4 mandatory experience")
        |                    +-- 2. FAR Regulatory Rule (e.g., "FAR 15.305 unstated evaluation criteria")
        |                    +-- 3. Offeror Comparative Pair (e.g., "Apex 14 years vs Nexus 4 years")
        |                    +-- 4. Evaluation Record Cross-Reference (e.g., "TET Consensus Key Personnel")
        |
        v
[Hybrid Lexical & Semantic Index]
        | +-- Exact phrase and boolean token matching (BM25)
        | +-- Optional dense vector similarity scoring
        | +-- Line-level citation extraction (file:line)
        |
        v
[Structured Matrix Alignment] ---> Maps findings into JSON compliance matrix
```

---

## 3. Local & Hybrid Search Execution

Use `scripts/search_diagnostics.py` or `LocalCorpusEngine` to execute exact-phrase and lexical retrieval across local procurement directories:

```python
from scripts.search_diagnostics import LocalCorpusEngine

def query_procurement_corpus(data_dir: str, query_text: str):
    engine = LocalCorpusEngine(data_dir=data_dir)
    matches = engine.search(query_text, top_k=5)
    return [
        {"document": doc_name, "score": score, "preview": snippet}
        for doc_name, score, snippet in matches
    ]
```

---

## 4. Query Formulation Reference for Bid Protest Audits

| Investigation Area | Natural Language Query | Optimized Legal Query |
|---|---|---|
| **Unstated Criteria** | *"Did the agency use unstated criteria against the protester?"* | `"Significant Weakness" "mainframe" "datacenter" Apex` |
| **Mandatory Minimums** | *"Did awardee meet all requirements?"* | `"99.95%" SLA uptime availability Nexus` |
| **Key Personnel** | *"What are the qualifications of awardee key personnel?"* | `"Johnathan Brooks" "Lead Cloud Solutions Architect" experience` |
| **Tradeoff Rationale** | *"Explain the SSA decision"* | `"Source Selection Authority" "tradeoff" "price premium" Nexus` |
