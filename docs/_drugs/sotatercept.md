---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Pulmonary Arterial Hypertension to Acute Lymphoblastic Leukemia

## One-Sentence Summary

> Sotatercept (DB12118) is an ActRIIA-Fc fusion protein currently marketed for pulmonary arterial hypertension (PAH), acting as an activin/TGF-β superfamily signaling trap.
> The TxGNN model predicts it may be effective for **Acute Lymphoblastic Leukemia**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-topology signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured data (licenses empty); drug is known globally as treatment for pulmonary arterial hypertension per rationale text |
| Predicted New Indication | Acute Lymphoblastic Leukemia (disease) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record (`original_moa` = Data Gap). Based on contextual information embedded in the evidence pack's rationale text, sotatercept is described as an ActRIIA-Fc fusion protein that traps activin/TGF-β superfamily ligands, primarily regulating erythrocyte maturation and vascular remodeling — mechanisms consistent with its known approved use in pulmonary arterial hypertension (PAH).

There is no known pathophysiological connection between PAH and acute lymphoblastic leukemia. The evidence pack itself states plainly: *"與 ALL 之間無已知病理生理學連結，TxGNN 高分僅反映 knowledge graph 拓撲相似性，非機轉證據"* — i.e., the high TxGNN score reflects graph-topology similarity in the knowledge graph rather than any biological mechanism linking the two conditions.

Notably, 9 of the 10 predicted indications in this evidence pack (severe diabetic retinopathy, drug-induced osteoporosis, HER2+ breast carcinoma, multiple rare urothelial carcinoma subtypes, etc.) show the same pattern: high TxGNN scores with zero supporting trials or literature. The repeated clustering of urothelial carcinoma subtypes (ranks 7–10) in particular suggests a systematic model artifact — likely node sparsity in the knowledge graph for these rare cancer subtypes — rather than a genuine repurposing signal. None of the 10 candidates currently rise above L5 evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Sotatercept is currently **not marketed in Norway** — no product authorizations are on record (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `taiwan_regulatory` warnings/contraindications and TFDA label data are flagged as a **Blocking** data gap (DG001) in this evidence pack — safety review cannot proceed to Stage S1 until this is resolved.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (acute lymphoblastic leukemia) — and all 9 other candidates in this pack — rest entirely on TxGNN topological scoring (L5) with zero clinical trials and zero literature support. There is no plausible mechanistic bridge between sotatercept's known activin-trap/PAH pharmacology and hematologic malignancy. Several lower-ranked candidates further suggest model noise from sparse graph nodes (e.g., repeated rare urothelial carcinoma subtypes) rather than genuine signal.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/regulatory label warnings and contraindications before any S1 safety screening can begin
- Resolve DG002 (High): obtain confirmed mechanism of action (MOA) from DrugBank API to properly evaluate mechanistic plausibility
- If pursuing the ALL hypothesis further, commission a targeted literature/preclinical search specifically on activin/TGF-β signaling in leukemic bone marrow niches before any trial-stage investment
- Given the pattern of clustered, unsupported urothelial carcinoma predictions, consider flagging this drug's KG neighborhood for review of potential data sparsity artifacts in the underlying TxGNN model
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

