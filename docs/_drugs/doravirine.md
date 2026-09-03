---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 3
---

# Doravirine
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

Using the evidence pack as provided, here is the evaluation report.

---

# Doravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) developed for HIV-1 infection. The TxGNN model's top-ranked prediction suggests possible relevance to **feline acquired immunodeficiency syndrome (FIV)** — a veterinary lentivirus infection, not a human disease — and this direction is currently supported by **no clinical trials and no literature**, corresponding to the lowest evidence tier (L5, model prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (based on drug-class context in the evidence pack; not confirmed via Norway regulatory data, as the drug is not marketed there) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for doravirine is not available in this evidence pack (flagged as a High-severity data gap). Based on the drug-class context referenced throughout the evidence pack's repurposing rationale, doravirine belongs to the non-nucleoside reverse transcriptase inhibitor (NNRTI) class — antiretrovirals whose activity depends on binding a highly specific pocket within the HIV-1 reverse transcriptase (RT) enzyme.

The top-ranked prediction, FIV, appears to arise from knowledge-graph semantic similarity between "antiretroviral drugs" and "lentivirus infections" in general, rather than from direct pharmacological or clinical evidence. FIV is caused by a lentivirus that, while distantly related to HIV-1, has a reverse-transcriptase structure that differs substantially from it. NNRTIs are well known to be highly sequence-specific to the HIV-1 non-nucleoside binding pocket — the same drug class (e.g., efavirenz, nevirapine) shows little to no cross-reactivity even against the closely related HIV-2, let alone FIV. FIV is also a veterinary (feline) disease model, not a human indication, placing it outside the conventional scope of human drug repurposing.

The evidence pack's own mechanistic assessment for this candidate explicitly characterizes it as likely embedding-space noise rather than a biologically plausible repurposing signal. Two lower-confidence candidates were also reviewed for context: simian immunodeficiency virus (SIV) infection (rank 2 — mechanistically plausible in principle as another lentivirus, but lacking direct cross-reactivity evidence and, like FIV, not a human indication) and a rare neurodevelopmental disorder (rank 3 — no biological rationale connects it to reverse-transcriptase inhibition, and it is flagged as a probable false positive). Neither strengthens the case for the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: One literature item was retrieved under the rank-2 candidate (SIV infection) — [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/), a 2020 review on islatravir. This concerns a different drug (islatravir, not doravirine) and therefore does not constitute direct supporting evidence for doravirine.*

---

## Norway Market Information

Doravirine currently holds no marketing authorization in Norway (market status: 未上市 / Not Marketed; 0 licenses on file). No product, dosage form, or approved-indication data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA package insert warnings/contraindications and DDI data are currently unavailable (DDI query status: not found) — this is recorded as a **Blocking** data gap (DG001) that prevents proceeding to safety (S1) evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 (model prediction only, no clinical trials or literature), and the underlying mechanistic rationale for the top-ranked indication (FIV) is weak — FIV is a non-human veterinary disease with no established cross-reactivity data for NNRTIs. Combined with the absence of Norway market presence and a Blocking safety data gap, this candidate does not currently meet the bar for further evaluation.

**To proceed, the following is needed:**
- TFDA/Norway package insert (warnings, contraindications) — Blocking gap (DG001), required before any S1 safety evaluation
- Confirmed mechanism of action (MOA) documentation — High-priority gap (DG002)
- Direct pharmacological or in vitro evidence of doravirine activity against FIV or other non-HIV-1 lentiviruses
- Direct (drug-specific) literature or trial evidence for the SIV-infection candidate, since the current literature match concerns a different drug (islatravir)
- Clarification of clinical relevance, since the top-ranked prediction is a veterinary indication rather than a human disease target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

