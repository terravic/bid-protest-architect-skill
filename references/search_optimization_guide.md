# Vertex AI Search & Legal Corpus Retrieval Guide

## 1. Principles of Legal & Procurement Information Retrieval

Forensic analysis of federal procurement records presents unique challenges for standard Information Retrieval (IR) systems:

1. **Semantic Specificity of Legal Terms of Art**:
   - In federal procurement, terms like `shall`, `must`, and `mandatory minimum` carry strict statutory weight under FAR 15.206.
   - Searching for "mandatory qualification" requires locating binding Section L clauses rather than general narrative descriptions.

2. **Tabular Structure Preservation**:
   - Solicitations and Source Selection records rely heavily on structured matrices (Section M evaluation factors, adjectival scoring tables, CPARS past performance charts, and pricing schedules).
   - Preserving row and column associations ensures factual alignment between offeror proposals and evaluators' consensus notes.

3. **Multi-Faceted Audit Queries**:
   - Effective legal investigations require querying multiple dimensions simultaneously: exact RFP clauses, offeror factual submissions, evaluator scoring justifications, and FAR statutory standards.

---

## 2. Technical Architecture

The skill implements a structured 4-tier legal retrieval pipeline:

```
[User / Agent Goal]
        │
        ▼
[Legal Query Expander] ──► Generates 4 Query Variants:
        │                   ├─ 1. Exact Legal Ground Pattern (e.g., "Section L.4 mandatory experience")
        │                   ├─ 2. FAR Statutory Rule (e.g., "FAR 15.305 unstated evaluation criteria")
        │                   ├─ 3. Offeror Comparative Pair (e.g., "Apex 14 years vs Nexus 4 years")
        │                   └─ 4. Adjectival Rating Cross-Reference (e.g., "TET Consensus Key Personnel")
        │
        ▼
[Direct Vertex AI Search / Hybrid Engine]
        │ ├─ Direct REST/gRPC API invocation
        │ ├─ Hybrid Search (Dense Embeddings + Sparse BM25)
        │ ├─ Snippet Spec: max_snippet_count=5, extractive_answers_spec
        │ └─ Custom Relevance Reranking
        │
        ▼
[Structured Matrix Alignment] ──► Maps findings into unified JSON evaluation matrix
```

---

## 3. Direct Vertex AI Search Configuration

When configuring Vertex AI Search (via `google-cloud-discoveryengine` or REST API) for procurement document corpora, use the following production configuration:

```python
from google.cloud import discoveryengine_v1 as discoveryengine

def search_procurement_corpus(project_id, location, data_store_id, query_text):
    client = discoveryengine.SearchServiceClient()
    serving_config = client.serving_config_path(
        project=project_id,
        location=location,
        data_store=data_store_id,
        serving_config="default_config",
    )

    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=query_text,
        page_size=10,
        content_search_spec=discoveryengine.SearchRequest.ContentSearchSpec(
            snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
                return_snippet=True,
                max_snippet_count=5,
            ),
            extractive_content_spec=discoveryengine.SearchRequest.ContentSearchSpec.ExtractiveContentSpec(
                max_extractive_answer_count=3,
                max_extractive_segment_count=3,
                return_extractive_segment_score=True,
            ),
            summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                summary_result_count=5,
                include_citations=True,
            ),
        ),
        query_expansion_spec=discoveryengine.SearchRequest.QueryExpansionSpec(
            condition=discoveryengine.SearchRequest.QueryExpansionSpec.Condition.AUTO,
        ),
        spell_correction_spec=discoveryengine.SearchRequest.SpellCorrectionSpec(
            mode=discoveryengine.SearchRequest.SpellCorrectionSpec.Mode.AUTO,
        ),
    )

    response = client.search(request)
    return response
```

---

## 4. Query Engineering Reference for Bid Protest Audits

| Investigation Area | Natural Language Query | Optimized Legal Query |
|---|---|---|
| **Unstated Criteria** | *"Did the agency use unstated criteria against the protester?"* | `("Significant Weakness" OR "Weakness") AND ("Section M" OR "evaluation factor") AND NOT ("Section L" OR "SOW")` |
| **Mandatory Minimums** | *"Did awardee meet all requirements?"* | `("shall" OR "mandatory minimum" OR "must") AND ("SLA" OR "certification" OR "years of experience")` |
| **Disparate Treatment** | *"Was scoring fair between companies?"* | `("Lead Cloud Solutions Architect" OR "Key Personnel") AND ("years of experience" OR "certification") AND ("Acceptable" OR "Outstanding")` |
| **Tradeoff Rationale** | *"Explain the SSA decision"* | `("Source Selection Decision" OR "SSDD") AND ("tradeoff" OR "price premium" OR "technically superior") AND "FAR 15.308"` |
