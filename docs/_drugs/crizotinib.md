---
layout: default
title: Crizotinib
parent: 僅模型預測 (L5)
nav_order: 93
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: From ALK-Positive Non-Small Cell Lung Cancer to Fibromatosis, Gingival

## One-Sentence Summary

Crizotinib is an oral ALK/ROS1/MET tyrosine kinase inhibitor; formal Taiwan regulatory and DrugBank MOA records are currently missing from this evidence pack, but literature embedded in this candidate set consistently identifies its established use as ALK/ROS1-rearranged non-small cell lung cancer (NSCLC). The TxGNN model's top-ranked prediction in this batch is **Gingival Fibromatosis (Fibromatosis, Gingival)**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, making it a purely computational hypothesis with no mechanistic corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in Taiwan regulatory data (drug not marketed, 0 licenses); literature in this evidence pack indicates established use is ALK/ROS1-positive NSCLC |
| Predicted New Indication | Fibromatosis, Gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for crizotinib is not directly recorded in this evidence pack (Data Gap DG002, High severity). Based on literature evidence attached elsewhere in this same candidate set, crizotinib is known to be an ATP-competitive small-molecule inhibitor of the receptor tyrosine kinases ALK, ROS1, and c-Met/MET, approved for NSCLC harboring EML4-ALK rearrangements and ROS1 fusions.

Gingival fibromatosis is a benign, non-neoplastic fibrous overgrowth of gingival connective tissue, typically driven by genetic (e.g., *SOS1*) or drug-induced fibroblast proliferation pathways — a biology unrelated to ALK/ROS1/MET receptor tyrosine kinase signaling. The evidence pack's own rationale for this candidate states explicitly: *"無任何機轉關聯報導；牙齦纖維瘤病與 ALK/ROS1/MET 路徑無已知連結，僅為 TxGNN 純預測分數"* (no mechanistic linkage reported; no known connection between ALK/ROS1/MET and gingival fibromatosis pathogenesis — this is a pure TxGNN score with no supporting biology).

Notably, this same candidate batch contains several other crizotinib-predicted indications with markedly stronger evidence — e.g., rank 4 "lung hilum carcinoma" (L3, Proceed with Guardrails) and rank 5 "lung benign neoplasm" (L1, 20 publications, though likely an ontology-label mismatch pointing back to crizotinib's already-known ALK/ROS1-positive NSCLC indication). This suggests the model's true, biologically grounded signal for crizotinib clusters around lung/ALK-ROS1-driven tumors, not gingival fibromatosis, reinforcing that the top-ranked prediction here should be treated with caution rather than as the strongest repurposing candidate in this set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No marketing authorizations currently registered in Taiwan — crizotinib is not marketed in Taiwan under this candidate record (0 licenses).

---

## Cytotoxicity

Crizotinib is an antineoplastic agent (targeted therapy) based on literature embedded in this evidence pack, though formal DrugBank category/toxicity fields were not provided.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor), not conventional cytotoxic chemotherapy |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no toxicity data provided in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA warnings/contraindications data acquisition is currently flagged as a Blocking data gap (DG001) — this must be resolved before any S1 safety assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gingival Fibromatosis) has an L5 evidence level — no clinical trials, no publications, and no plausible mechanistic link to crizotinib's known ALK/ROS1/MET targets. Combined with a Blocking gap in TFDA label data and a High-severity gap in confirmed MOA, this specific candidate does not meet the minimum evidence bar to advance.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — Blocking gap DG001
- Confirmed DrugBank MOA record — High severity gap DG002
- Preclinical or mechanistic evidence directly linking ALK/ROS1/MET signaling to gingival fibromatosis pathogenesis
- Re-evaluate this candidate set's higher-evidence entries (rank 4 "lung hilum carcinoma," L3; rank 5 "lung benign neoplasm," L1) as more promising repurposing directions, pending ontology-label verification against crizotinib's known NSCLC indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

