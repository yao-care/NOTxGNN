---
layout: default
title: Selpercatinib
parent: 僅模型預測 (L5)
nav_order: 322
evidence_level: L5
indication_count: 3
---

# Selpercatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Selpercatinib: From RET Fusion-Positive NSCLC to Pulmonary Hypertension

## One-Sentence Summary

Selpercatinib is a selective RET tyrosine kinase inhibitor currently used for RET fusion/mutation-positive non-small cell lung cancer and medullary thyroid carcinoma. The TxGNN model predicts a possible link to **Pulmonary Hypertension**, but the only 3 supporting publications are pharmacovigilance/adverse-event and case-report studies — meaning this signal may reflect a **cardiovascular safety risk of selpercatinib rather than a therapeutic opportunity**. No clinical trials, official Taiwan MOA data, or package insert warnings are currently available to confirm either direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | RET fusion/mutation-positive NSCLC, medullary thyroid carcinoma (per known approved use referenced in evidence; no formal Taiwan license record available) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L4 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field marked as data gap). Based on known information, selpercatinib is a highly selective RET tyrosine kinase inhibitor, approved for RET fusion/mutation-positive NSCLC and medullary thyroid carcinoma. RET signaling has been reported in some literature to play a role in pulmonary vascular remodeling, but this is an indirect, non-mainstream mechanistic hypothesis with no established theoretical basis for selpercatinib as a **treatment** for pulmonary hypertension.

More importantly, at least 2 of the 3 retrieved publications are adverse-event/pharmacovigilance database analyses comparing selpercatinib and pralsetinib safety profiles. This raises the possibility that pulmonary hypertension appears in the data as a reported **adverse event** of selpercatinib (e.g., cardiovascular toxicity) rather than a disease it could treat — which would be the opposite interpretation from what TxGNN's "predicted indication" framing suggests. This distinction must be clarified before any further evaluation.

The other two predicted indications (migraine disorder, migraine with brainstem aura) have no supporting literature or trials at all and are considered likely embedding-space false positives, as RET signaling has no established connection to trigeminovascular/CGRP pathways or channelopathy-related migraine subtypes.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34178121](https://pubmed.ncbi.nlm.nih.gov/34178121/) | 2021 | Retrospective cohort | Ther Adv Med Oncol | Real-world efficacy of selpercatinib in RET fusion-positive NSCLC (SIREN access-program analysis); no pulmonary hypertension outcome data |
| [39372206](https://pubmed.ncbi.nlm.nih.gov/39372206/) | 2024 | Real-world/Pharmacovigilance | Front Pharmacol | FAERS-based comparison of adverse event profiles between pralsetinib and selpercatinib — pulmonary hypertension may appear here as a reported AE, not a treated condition |
| [41918669](https://pubmed.ncbi.nlm.nih.gov/41918669/) | 2026 | Case report | Cureus | Case of RET M918T-mutated MEN2B metastatic medullary thyroid carcinoma on targeted therapy; management challenges, no PH treatment data |

## Cytotoxicity

Selpercatinib is a targeted anticancer therapy (kinase inhibitor), applicable per DrugBank/known drug class.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (selective RET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pulmonary hypertension, L4) is supported only by adverse-event/case-report literature that may actually indicate a safety risk rather than therapeutic potential, and the remaining two predictions (migraine, migraine with brainstem aura) have no supporting evidence at all (L5). Combined with the blocking data gap on Taiwan package insert warnings/contraindications, there is insufficient basis to advance any of these candidates.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank — currently high-severity gap (DG002)
- Clarification of whether the pulmonary hypertension signal in FAERS-based literature represents an adverse event vs. a treatable indication
- Preclinical or mechanistic evidence directly linking RET inhibition to pulmonary vascular remodeling, if this direction is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

