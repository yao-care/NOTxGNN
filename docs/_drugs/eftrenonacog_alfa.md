---
layout: default
title: Eftrenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 123
evidence_level: L5
indication_count: 3
---

# Eftrenonacog Alfa
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

# Eftrenonacog Alfa: From Hemophilia B to Pseudo-von Willebrand Disease

## One-Sentence Summary

Eftrenonacog alfa is a recombinant Factor IX-Fc fusion protein used as coagulation factor replacement therapy for Hemophilia B.
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**,
but this signal is currently supported by **0 clinical trials** and **0 publications**, and the underlying mechanistic rationale itself raises concerns about a false-positive prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hemophilia B (based on known drug class; formal indication text not available in this dataset) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this record. Based on known pharmacology, eftrenonacog alfa is a recombinant Factor IX-Fc fusion protein that replaces deficient endogenous Factor IX in the intrinsic coagulation pathway, and its efficacy in Hemophilia B is well established.

However, the top three TxGNN-predicted indications for this drug — pseudo-von Willebrand disease, primary release disorder of platelets, and Glanzmann thrombasthenia — are all **platelet-level disorders** (abnormal GPIb–vWF affinity, defective granule release, and GPIIb/IIIa receptor deficiency, respectively), not coagulation factor deficiencies. Factor IX replacement acts on thrombin generation and has no known mechanism to correct platelet receptor or granule defects.

This mismatch suggests the high TxGNN scores likely reflect clustering of "bleeding disorder" nodes within the knowledge graph rather than genuine shared pharmacology. All three candidates should be treated as low-confidence, mechanism-unclear signals pending further validation, not as pharmacologically grounded repurposing hypotheses.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

This drug is not currently marketed in Norway (0 authorizations on record); no license or product information is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only (L5) prediction with no supporting clinical trials or literature, and the proposed mechanistic link between Factor IX replacement and platelet-function disorders is weak — the pattern is more consistent with knowledge-graph node clustering than true pharmacological relevance.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (currently a blocking data gap, DG002)
- TFDA/manufacturer labeling with warnings and contraindications, required before any safety pre-screening (blocking data gap, DG001)
- Independent mechanistic or preclinical evidence directly linking Factor IX pathway activity to platelet-vWF or platelet-receptor disorders
- Real-world case reports or registry data on Factor IX products used in these platelet disorders, if any exist, to distinguish true signal from prediction artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

