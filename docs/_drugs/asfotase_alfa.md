---
layout: default
title: Asfotase Alfa
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Asfotase Alfa
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

# Asfotase Alfa: From Hypophosphatasia to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

> Asfotase alfa is a bone-targeted enzyme replacement therapy originally developed for hypophosphatasia (HPP).
> The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation (OXPHOS) disorder due to nuclear DNA anomalies**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the accompanying mechanistic review found no known biological link between the two conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypophosphatasia (HPP) — enzyme replacement therapy |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not currently available for this drug. Based on known information, asfotase alfa is a bone-targeted recombinant human tissue-nonspecific alkaline phosphatase (TNSALP), used as enzyme replacement therapy for hypophosphatasia. Its mechanism involves restoring bone matrix mineralization by hydrolyzing extracellular inorganic pyrophosphate, which otherwise accumulates and inhibits mineralization in HPP patients.

The top-ranked predicted indication, mitochondrial OXPHOS disorder due to nuclear DNA anomalies, is pathophysiologically distinct: it arises from defects in the mitochondrial respiratory chain, not from impaired bone mineralization. The evidence pack's own mechanistic review explicitly notes there is **no known biological intersection** between the ALP-mediated bone mineralization pathway and OXPHOS pathology — the prediction appears to be driven purely by network embedding similarity in TxGNN, not by a testable biological hypothesis.

This pattern repeats across the remaining nine predicted indications (rank 2–10): most connections are attributed to superficial phenotypic overlap (e.g., other skeletal disorders such as Steel syndrome, Scheie/Hurler syndrome, lysosomal storage diseases) or shared treatment modality (enzyme replacement therapy) rather than a shared molecular target or pathway. Several candidates (e.g., esophageal varices, exocrine pancreatic insufficiency, familial apolipoprotein C-II deficiency) have no discernible mechanistic rationale at all. Given the complete absence of supporting clinical or literature evidence, none of the top 10 predictions currently warrant further investment beyond exploratory hypothesis generation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Asfotase alfa currently holds no market authorization in Norway (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a TxGNN similarity score with no clinical trials, no literature, and — per the evidence pack's own mechanistic review — no identifiable biological link to the drug's known mode of action. Evidence level is L5 (model prediction only), which does not meet the threshold for further development investment.

**To proceed, the following is needed:**
- Structured mechanism-of-action (MOA) data from DrugBank or primary literature
- TFDA/regulatory label warnings and contraindications (currently blocking safety pre-screening, per DG001)
- Preclinical or mechanistic studies establishing a plausible link between TNSALP-mediated bone mineralization and mitochondrial OXPHOS pathology, if this indication is to be pursued further
- Continued monitoring for new clinical trial registrations or publications on any of the top 10 candidates before re-evaluating decision stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

