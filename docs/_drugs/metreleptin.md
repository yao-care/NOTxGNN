---
layout: default
title: Metreleptin
parent: 僅模型預測 (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: From Leptin Deficiency (Lipodystrophy) to Familial Generalized Lentiginosis

## One-Sentence Summary

Metreleptin is a recombinant leptin analog used to treat leptin deficiency in generalized lipodystrophy. The TxGNN model's top prediction is **Familial Generalized Lentiginosis**, with a **99.71%** prediction score, but there are currently **0 clinical trials** and **0 publications** supporting this direction — the evidence pack's own mechanistic analysis also finds no plausible biological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in evidence pack (data gap). Metreleptin is generally known as treatment for leptin deficiency associated with generalized lipodystrophy |
| Predicted New Indication | Familial Generalized Lentiginosis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on the limited information in the evidence pack, metreleptin acts as a leptin receptor agonist, primarily regulating hypothalamic energy metabolism and adipose tissue signaling.

Familial generalized lentiginosis is an autosomal dominant pigmentary skin disorder. The evidence pack's own rationale analysis states there is **no known mechanistic connection** between the leptin signaling pathway and this disease's pathology, and no hypothesis could be established given the missing MOA data.

The same pattern holds across all top-10 TxGNN candidates for this drug (see disease list in source data): rare pigmentary syndromes (gastrocutaneous syndrome, Moynahan syndrome, acromelanosis, etc.), tumor entities driven by unrelated pathways (rhabdoid tumor via SMARCB1/INI1 loss, schwannoma via NF2/merlin loss), and other rare multisystem syndromes — none of which have an established or plausible link to leptin receptor signaling per the provided rationale. This suggests the prediction is driven primarily by network-based similarity in the TxGNN model rather than a defensible biological mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Metreleptin currently holds **no marketing authorizations in Norway** (0 licenses on record); the drug is not marketed in this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/label-level warnings and contraindications (DG001) are flagged as a **Blocking** data gap in the source evidence pack, meaning a formal safety (S1) evaluation cannot currently be completed for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top-10 predicted indications for metreleptin sit at evidence level L5 (model prediction only — no clinical trials, no literature), and the evidence pack's own mechanistic review found no plausible biological rationale linking leptin receptor signaling to any of the candidate diseases. Combined with a Blocking-severity safety data gap and zero market presence in Norway, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/Norway label warnings, contraindications, and DDI data (DG001, Blocking)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Targeted literature/clinical trial search specific to top-ranked candidate diseases to check for any evidence TxGNN's training data may not surface
- Independent pharmacological plausibility review before allocating further evaluation resources to this drug-indication pair
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

