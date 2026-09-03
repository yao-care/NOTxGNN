---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 1
---

# Lapatinib
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

# Lapatinib: From an Unrecorded Original Indication to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

The evidence pack for Lapatinib (DrugBank DB01259) does not contain the original approved indication or mechanism of action — both are recorded as data gaps. The TxGNN model predicts a possible new indication for **Dermatofibrosarcoma Protuberans (DFSP)**, but this prediction is currently supported by **no clinical trials and no published literature**, and the drug is not marketed in Norway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Norway license records and `original_indications` is empty in the evidence pack |
| Predicted New Indication | Dermatofibrosarcoma Protuberans |
| TxGNN Prediction Score | 99.30% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for lapatinib is not available in this evidence pack, and no original indication is recorded either, so a direct mechanistic bridge between the original use and DFSP cannot be established from the data provided.

Based on general knowledge encoded in the model's rationale, DFSP is driven primarily by a **COL1A1-PDGFB fusion** that causes constitutive PDGFRB activation, and its standard targeted therapy is imatinib (a PDGFR inhibitor). Lapatinib's known targets — EGFR and HER2 — do not directly overlap with PDGFRB. The proposed link relies only on a theoretical, unconfirmed possibility of off-target PDGFR cross-inhibition, with no experimental or clinical data to support it.

Given the missing MOA data and the absence of a validated original indication, the mechanistic plausibility of this prediction is weak and should be treated as hypothesis-generating only, not as evidence of therapeutic relevance.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Lapatinib currently holds no market authorization in Norway (0 licenses on file; market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is zero clinical trial or literature support, the mechanistic rationale linking lapatinib (EGFR/HER2 inhibitor) to DFSP (PDGFRB-driven) is weak and speculative, and critical drug-level data (MOA, TFDA/label warnings and contraindications) are missing — one of which (label warnings/contraindications) is flagged as a **Blocking** data gap that prevents even an initial S1 safety assessment.

**To proceed, the following is needed:**
- Original indication and label data for lapatinib (currently entirely absent from the evidence pack)
- Mechanism of action data (DG002) to properly evaluate the EGFR/HER2–PDGFRB rationale gap
- TFDA/Norway label warnings and contraindications (DG001, Blocking) before any safety review can begin
- At minimum, preclinical or case-level evidence connecting HER2/EGFR inhibition to DFSP biology before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

