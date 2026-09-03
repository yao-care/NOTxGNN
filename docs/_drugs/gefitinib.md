---
layout: default
title: Gefitinib
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Gefitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using no additional skill — this is a direct report-generation task with a fully specified template; I'll produce the Markdown report following it exactly.

# Gefitinib: From Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

> Gefitinib is a first-generation EGFR tyrosine kinase inhibitor (EGFR-TKI) known clinically for the treatment of EGFR-mutant non-small cell lung cancer (NSCLC).
> The TxGNN model predicts it may be effective for **Fibromatosis, Gingival**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a model-score-only prediction with no mechanistic or empirical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local regulatory registry (0 licenses on file). Based on known pharmacology, gefitinib is an EGFR-TKI indicated for EGFR mutation-positive non-small cell lung cancer (NSCLC). |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the local registry (data gap DG002). Based on known pharmacological information from the evidence pack itself, gefitinib is a first-generation EGFR tyrosine kinase inhibitor that blocks EGFR autophosphorylation and downstream RAS/MEK/ERK signalling, and it is the standard-of-care mechanism for EGFR-mutant NSCLC.

Gingival fibromatosis, however, is a benign connective-tissue overgrowth disorder with no established link to EGFR-driven oncogenic signalling. The evidence pack's own mechanistic assessment for this candidate states explicitly that there is **no known mechanistic connection** between gefitinib's EGFR-TKI activity and gingival fibromatosis, and no clinical trial or literature evidence exists to support the association. This candidate therefore appears to be a pure knowledge-graph score artifact (TxGNN rank 1590) rather than a biologically grounded repurposing hypothesis.

It is worth noting that several lower-ranked predictions in this evidence pack (e.g., lung hilum carcinoma, lung germ cell tumor, pulmonary sulcus neoplasm) are anatomically and mechanistically closer to gefitinib's established NSCLC indication, though even these lack indication-specific trial or literature confirmation. See Conclusion for further discussion.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Gefitinib currently holds **no marketing authorization** in Norway (0 licenses on file; market status: 未上市 / Not Marketed).

---

## Cytotoxicity

Gefitinib is an antineoplastic agent (original indication class: NSCLC; drug class confirmed across the evidence pack's own mechanistic rationales as an EGFR tyrosine kinase inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (EGFR tyrosine kinase inhibitor; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The featured prediction (gingival fibromatosis, TxGNN score 99.89%) has no clinical trial or literature support and no plausible mechanistic link — it is a model-score-only (L5) association. This is compounded by a **Blocking** data gap (DG001: TFDA/local label warnings and contraindications unavailable), which prevents even an initial safety screen (S1), and by the drug having zero marketing authorizations locally.

**To proceed, the following is needed:**
- Resolve DG001 (obtain and parse the official package insert for warnings/contraindications) before any S1 safety evaluation can occur.
- Resolve DG002 (confirm MOA via DrugBank API) to properly document mechanistic rationale.
- If gingival fibromatosis remains the target, generate a specific mechanistic hypothesis and seek preclinical/case-level evidence — none currently exists.
- Consider re-scoping evaluation toward the more anatomically plausible candidates in this pack (rank 5, lung hilum carcinoma, which reached decision_stage S1 / "Research Question"), which — while still weakly supported — are mechanistically closer to gefitinib's established NSCLC activity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

