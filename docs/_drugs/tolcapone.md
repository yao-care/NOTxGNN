---
layout: default
title: Tolcapone
parent: 僅模型預測 (L5)
nav_order: 362
evidence_level: L5
indication_count: 10
---

# Tolcapone
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

Using no specialized skill — this is a direct content-generation task with a fully specified template already provided; no coding, debugging, or brainstorming is required.

---

# Tolcapone: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Tolcapone is a catechol-O-methyltransferase (COMT) inhibitor, originally used as an adjunct to levodopa/carbidopa in Parkinson's disease. The TxGNN model's top-ranked prediction for this drug is **Rasmussen Subacute Encephalitis**, but this specific candidate currently has **0 clinical trials** and **0 publications** supporting it — the entire evidence base is the model score itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) — inferred from COMT-inhibitor classification cited in the evidence pack; no Norway market license on file to confirm approved wording |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the information available, Tolcapone is a COMT inhibitor used adjunctively with levodopa/carbidopa in Parkinson's disease, acting on catecholamine/dopamine metabolism.

Rasmussen encephalitis, however, is an autoimmune/inflammatory unilateral cortical disease with no established link to dopamine metabolism or the COMT pathway. The evidence pack's own rationale confirms this: there is no mechanistic connection, and no clinical trial or literature evidence exists for this pairing — it is purely a high TxGNN embedding-similarity score with no corroborating signal.

Notably, this same evidence pack contains two other candidates with clearer biological plausibility given Tolcapone's known pharmacology: **Lewy body dementia** (rank 6, L4, overlapping dopaminergic neurodegeneration) and **juvenile parkinsonism / Hunt's paralysis agitans** (rank 10, L4, mechanistically near-identical to the drug's core approved use). Neither has clinical trial or literature evidence in this dataset, but both merit consideration as more credible secondary hypotheses than the top-ranked score alone.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Currently no market authorization records in Norway — Tolcapone is not marketed in this territory.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rasmussen subacute encephalitis) has no clinical, literature, or mechanistic support (Evidence Level L5), and the drug is not currently marketed in Norway. Critical safety data — TFDA warnings/contraindications (Blocking gap) and detailed MOA (High-severity gap) — are also missing, precluding even an initial safety screen.

**To proceed, the following is needed:**
- TFDA/regulatory package insert: warnings, contraindications (DG001)
- Detailed MOA data from DrugBank (DG002)
- If pursuing repurposing further, re-scope the candidate indication toward the higher-plausibility L4 signals in this dataset (Lewy body dementia, juvenile parkinsonism) rather than the top TxGNN score alone, and seek dedicated literature/trial searches for those specific indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

