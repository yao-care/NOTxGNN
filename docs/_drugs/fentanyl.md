---
layout: default
title: Fentanyl
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 2
---

# Fentanyl
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Fentanyl: From Pain Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent synthetic opioid (mu-opioid receptor agonist) generally used for management of moderate-to-severe pain. The TxGNN model predicts a possible association with **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, with a prediction score of **99.46%**, but currently **zero clinical trials and zero publications** support this direction in the evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (fentanyl is generally known as an opioid analgesic for moderate-to-severe pain) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% (model rank 5778) |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for fentanyl in this evidence pack (flagged as data gap DG002, High severity). Based on general pharmacological knowledge, fentanyl is a potent synthetic opioid and mu-opioid receptor (MOR) agonist clinically used for management of moderate-to-severe pain, including perioperative and breakthrough cancer pain.

The TxGNN model predicts a possible association with nephrogenic syndrome of inappropriate antidiuresis (NSIAD), a rare condition typically caused by a gain-of-function mutation in the vasopressin V2 receptor (AVPR2) that leads to inappropriate water retention independent of ADH levels. Opioids are known to influence antidiuretic hormone (ADH/vasopressin) release, which offers a theoretical point of mechanistic overlap, but the evidence pack does not include a completed mechanistic rationale, similarity analysis, clinical trials, or literature for this candidate (`repurposing_rationale` and `route_compatibility` are marked "pending"). As a result, the biological plausibility of this link cannot currently be substantiated beyond the raw model score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warnings and contraindications for fentanyl have not yet been retrieved — this is flagged as a Blocking data gap (DG001) that must be resolved before any S1 safety review.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high, but there is no supporting clinical trial or literature evidence (Evidence Level L5), no completed mechanistic rationale, and critical safety data (warnings/contraindications) has not yet been obtained — a Blocking gap. Fentanyl is also not currently marketed in Norway, so there is no existing regulatory foothold to build on.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (DG001, Blocking — required before S1 safety review)
- Mechanism of action data for fentanyl (DG002)
- Completed mechanistic rationale and similarity analysis linking opioid pharmacology to NSIAD
- Clinical trial and literature search specifically targeting fentanyl/opioids and NSIAD or SIADH-related conditions
- Norway market/regulatory pathway assessment if repurposing is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

