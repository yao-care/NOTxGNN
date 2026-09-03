---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 1
---

# Levodopa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Levodopa: From Parkinson's Disease (Unconfirmed) to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor conventionally associated with Parkinson's disease treatment, though the original indication is not documented in this evidence pack.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but currently **0 clinical trials** and **0 publications** support this direction — the score reflects a model-only prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (`original_indications` empty) |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a **High-severity data gap**). Based on general pharmacological knowledge, levodopa is a dopamine precursor converted by DOPA decarboxylase (DDC) into dopamine, acting primarily on the nigrostriatal dopaminergic pathway.

Rasmussen subacute encephalitis is a unilateral, autoimmune/inflammatory epileptic encephalopathy driven by T-cell mediated neuronal destruction and chronic inflammation — a mechanism with no established connection to dopamine synthesis or transmission.

The TxGNN score of 0.99 likely reflects a topological association within the knowledge graph (possibly via shared epilepsy or neurodegenerative disease nodes) rather than a pharmacologically interpretable mechanism. **No mechanistic rationale currently supports this prediction**, and it should be treated as a hypothesis-generating signal only, not an actionable candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Levodopa is currently **not marketed** in Norway under this evidence pack, and no authorization records are available (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings/contraindications retrieval is flagged as a **Blocking** data gap in this evidence pack and must be resolved before any safety assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is supported only by an L5 model prediction with no clinical trials, no literature, and no plausible mechanistic link to the predicted indication. A Blocking data gap on regulatory safety information further precludes any safety pre-assessment.

**To proceed, the following is needed:**
- TFDA/official label data (warnings, contraindications) — currently blocking S1 safety review
- Confirmed mechanism of action (MOA) via DrugBank or primary literature
- Confirmed original indication(s) for this candidate
- Preclinical or case-level evidence connecting dopaminergic mechanisms to Rasmussen encephalitis pathology, before further evaluation is warranted
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

