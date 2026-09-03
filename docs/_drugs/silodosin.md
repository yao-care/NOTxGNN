---
layout: default
title: Silodosin
parent: 僅模型預測 (L5)
nav_order: 323
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Silodosin: From Benign Prostatic Hyperplasia (BPH) to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Silodosin is a highly selective α1A-adrenergic receptor antagonist, clinically known for treating benign prostatic hyperplasia (BPH)-related lower urinary tract symptoms by acting on prostate/bladder-neck smooth muscle. The TxGNN model predicts a possible link to **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital hair-overgrowth disorder, but this is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags no identifiable mechanistic connection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally provided (`original_indications` is empty; `original_moa` is flagged as a data gap). Prediction-rationale text references silodosin's known action on prostate/bladder-neck smooth muscle, consistent with its established BPH use. |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.99% (global rank 153) |
| Evidence Level | L5 (model prediction only — no trials, no literature) |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack — it is explicitly listed as a data gap (DrugBank MOA query, severity High; TFDA label, severity Blocking). Based on the mechanistic notes attached to each prediction, silodosin is understood as a highly selective α1A-adrenergic receptor antagonist acting primarily on prostate and bladder-neck smooth muscle — the pharmacological basis for its known BPH use.

Ambras type hypertrichosis universalis congenita is a rare congenital disorder linked to chromosomal rearrangements near hair-follicle developmental genes (e.g., near *TRPS1*) — a biological pathway with no known intersection with α1A-adrenergic signaling. The evidence pack's own rationale field states directly that there is **no identifiable mechanistic link** here.

This should therefore be read as a pure embedding-similarity output from the TxGNN model, not a mechanistically grounded hypothesis. The same pattern holds across all six candidates in this pack: none have a plausible mechanistic rationale, none have clinical trials, and the one candidate with attached literature (rank 3, "malformation syndrome with odontal/periodontal component," 20 papers) was found on inspection to be an irrelevant keyword mismatch — none of those papers mention silodosin or α1-adrenergic pharmacology at all.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

No market authorization records are currently available for silodosin (market status: Not Marketed; 0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- All six candidates in this evidence pack are TxGNN outputs only (Evidence Level L5), with no clinical trials and no mechanistically plausible rationale; the one candidate with associated literature turned out to be an unrelated keyword mismatch. There is currently no basis to advance any candidate for silodosin.

**To proceed, the following is needed:**
- TFDA-equivalent label (warnings/contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Formal original-indication/approved-labeling data (currently empty in this pack)
- Should any future TxGNN candidate for silodosin show a biologically plausible α1A-adrenergic mechanism, dedicated clinical-trial and literature evidence collection for that specific candidate before re-scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

