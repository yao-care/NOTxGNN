---
layout: default
title: Avibactam
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
---

# Avibactam
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

# Avibactam: From No Approved Indication to Streptococcal Pneumonia

## One-Sentence Summary

Avibactam has no approved original indication or regulatory market presence recorded in this evidence pack — it is a non-β-lactam β-lactamase inhibitor that must be co-administered with a β-lactam antibiotic (e.g., ceftazidime) rather than used alone. The TxGNN model predicts a possible signal for **Streptococcal Pneumonia**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale explicitly flags this link as biologically weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication recorded (drug not marketed; original indication data unavailable) |
| Predicted New Indication | Streptococcal pneumonia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured drug record. Based on the mechanistic notes attached to the predictions themselves, avibactam is known to have no intrinsic antibacterial activity — it functions as a non-β-lactam β-lactamase inhibitor and is only clinically useful in combination with a β-lactam antibiotic such as ceftazidime, primarily against Ambler class A/C/D β-lactamase-producing Gram-negative organisms.

This background is important context for evaluating the top prediction, *Streptococcal pneumonia*: the model's own rationale states that pneumococcal resistance arises mainly from penicillin-binding protein (PBP) alterations rather than β-lactamase production, meaning avibactam's core mechanism does not directly address this pathogen's resistance pathway. The mechanistic link is therefore assessed as weak.

The remaining five predicted indications (influenza susceptibility, ureter tuberculosis, urinary schistosomiasis, hyperamylasemia, polyclonal hyperviscosity syndrome) span viral, mycobacterial, parasitic, metabolic, and immunologic disease categories with no plausible connection to β-lactamase inhibition, and are explicitly annotated in the evidence pack as likely graph-based false positives. None of the six predictions is supported by any clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Avibactam has no marketing authorization in Norway (0 licenses on record); no product or approved-indication data is available for this drug in the current dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (streptococcal pneumonia) has zero supporting clinical trials or literature and is undermined by the model's own mechanistic analysis, which notes that avibactam's β-lactamase inhibition does not address the PBP-mediated resistance typical of *S. pneumoniae*. All six predicted indications sit at evidence level L5 (model prediction only), and the remaining five candidates (influenza, ureter tuberculosis, urinary schistosomiasis, hyperamylasemia, polyclonal hyperviscosity syndrome) show no biological plausibility and are flagged as probable false positives — none warrants further evaluation at this time.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature — currently a High-severity data gap (DG002)
- Original approved indication and market authorization records, since none exist in this dataset
- Any preclinical or in-vitro evidence specifically testing avibactam (alone or in combination) against *S. pneumoniae* before this signal can be escalated beyond S0/Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

