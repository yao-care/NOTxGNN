---
layout: default
title: Oritavancin
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 3
---

# Oritavancin
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

# Oritavancin: From Gram-Positive Bacterial Infections to Bacteroidaceae Infectious Disease

## One-Sentence Summary

> Oritavancin is a lipoglycopeptide antibiotic whose known spectrum of activity is limited to gram-positive bacteria.
> The TxGNN model predicts it may be effective for **Bacteroidaceae Infectious Disease**,
> but this prediction has **no supporting clinical trials or literature**, and the evidence pack's own mechanistic analysis indicates the prediction is **biologically implausible**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this evidence pack (drug not marketed in Taiwan; no approved indication text available). Known drug class: lipoglycopeptide antibiotic active against gram-positive organisms. |
| Predicted New Indication | Bacteroidaceae infectious disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap in this evidence pack (`original_moa: [Data Gap]`). However, the repurposing rationale attached to the top prediction describes oritavancin as a lipoglycopeptide antibiotic that binds the D-Ala-D-Ala terminus of cell wall precursors, inhibiting peptidoglycan synthesis — a mechanism effective **only against gram-positive bacteria**.

Bacteroidaceae are gram-negative anaerobes whose outer membrane structurally blocks penetration by large glycopeptide molecules. According to the evidence pack itself, this makes the mechanistic link between oritavancin and the predicted indication **contradictory to the drug's known antibacterial spectrum**, rather than supportive of it.

The same pattern holds for the other two top-ranked predictions in this evidence pack:
- **Ophthalmic herpes zoster** is a viral infection; oritavancin has no known antiviral activity.
- **Mycoplasma pneumoniae pneumonia** involves a cell-wall-deficient organism, which is intrinsically resistant to cell-wall-synthesis inhibitors like oritavancin.

All three top TxGNN-ranked predictions for this drug carry high similarity scores but are flagged, by the evidence pack's own mechanistic annotations, as pharmacologically inconsistent with oritavancin's established mode of action. This strongly suggests these are model-noise predictions rather than genuine repurposing candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Taiwan Market Information

No marketing authorizations currently exist in Taiwan — oritavancin is not marketed in this jurisdiction (`market_status: 未上市`, `total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is numerically high (99.48%), but evidence level is L5 — no clinical trials, no literature, and no real-world exposure data support this prediction. More importantly, the evidence pack's own mechanistic rationale explicitly contradicts the prediction: oritavancin's gram-positive-selective, cell-wall-dependent mechanism is incompatible with a gram-negative anaerobic target (Bacteroidaceae), and the same disqualifying logic applies to the other two ranked candidates (a viral infection and a cell-wall-deficient organism). This is a case where the model score should not override mechanistic plausibility.

**To proceed, the following is needed:**
- Confirmed MOA and approved indication data from DrugBank/manufacturer labeling (currently marked as data gaps: DG001, DG002)
- TFDA/regulatory package insert with warnings and contraindications
- Independent review of why TxGNN assigned high scores to mechanistically contradicted indications (possible model calibration issue for this drug node)
- If pursued further, in vitro susceptibility data against Bacteroidaceae species before any preclinical or clinical investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

