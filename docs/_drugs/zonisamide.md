---
layout: default
title: Zonisamide
parent: 僅模型預測 (L5)
nav_order: 393
evidence_level: L5
indication_count: 10
---

# Zonisamide
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

# Zonisamide: From Epilepsy (Partial Seizures) to Tourette Syndrome

## One-Sentence Summary

Zonisamide is a broad-spectrum antiepileptic drug, classically used as adjunctive therapy for partial seizures. The TxGNN model predicts it may be effective for **Tourette syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, partial seizures (adjunctive therapy) — inferred from known drug classification; no Norway license record available (drug not currently marketed) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, zonisamide is classified as a broad-spectrum anticonvulsant (multiple mechanisms including Na⁺ and T-type Ca²⁺ channel blockade), its efficacy in epilepsy/partial seizures has been proven, and mechanistically it may theoretically be applicable to tic disorders.

The rationale for Tourette syndrome specifically rests on zonisamide's dopaminergic modulatory activity, loosely analogous to case reports of other antiepileptic drugs used off-label for tic disorders. However, this dataset contains no clinical trials or literature directly supporting this indication — the association is derived purely from the TxGNN knowledge-graph prediction, not from any observed or documented efficacy signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Norway Market Information

Zonisamide currently holds no marketing authorizations in Norway (market status: Not Marketed, 0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Tourette syndrome) has no supporting clinical trials or literature — it is evidence level L5, a pure model-based association with no observed efficacy or safety signal, so it cannot proceed without further validation.

**To proceed, the following is needed:**
- TFDA/local regulatory label data (warnings, contraindications) — currently a blocking data gap
- Detailed mechanism of action (MOA) documentation
- Preclinical or case-level evidence directly linking zonisamide to tic-disorder symptom reduction
- **Note for prioritization:** other candidates in this evidence pack are far better supported and merit separate review — notably *absence epilepsy* (rank 8, evidence level L1, decision stage S3, "Proceed with Guardrails," backed by a completed Phase 3 RCT with n=583 directly comparing zonisamide to carbamazepine). This is likely a more actionable repurposing candidate than the top TxGNN-ranked indication.
- Caution: predictions for *methemoglobinemia* (ranks 3, 4, 6) may reflect an **adverse-effect direction rather than a therapeutic one**, since zonisamide is a sulfonamide derivative and sulfonamides are known to induce (not treat) methemoglobinemia — these should be flagged as likely false positives during safety review, not pursued as indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

