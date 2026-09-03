---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 9
---

# Insulin Lispro
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

> Insulin lispro is a rapid-acting insulin analog originally used to achieve glycemic control in diabetes mellitus.
> The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**,
> but currently **no clinical trials and no published literature** support this direction, and no plausible biological mechanism connecting the two has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (glycemic control) — not documented in the current Taiwan regulatory dataset |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin lispro is a rapid-acting insulin analog whose efficacy in glycemic control for diabetes mellitus is well established, acting via the insulin receptor to promote glucose uptake and regulate metabolism.

However, no known mechanistic relationship exists between insulin signaling and autoimmune oophoritis, which is an autoimmune inflammatory process affecting ovarian tissue. There is no established pathway by which insulin (or lispro specifically) would modulate this disease process.

Given the absence of any supporting clinical trials or literature, this high TxGNN score likely reflects noise or an indirect comorbidity association captured in the model's embedding space, rather than a genuine, mechanistically grounded treatment signal. This prediction should be treated as hypothesis-generating only, not as a basis for clinical action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Insulin Lispro is currently not marketed (未上市), and no product authorization records are available in this dataset (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported only by a raw TxGNN model score (L5), with no clinical trials, no literature, and no identifiable biological mechanism linking insulin lispro to autoimmune oophoritis. The evidence base is insufficient to justify further investment at this time.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently a Blocking data gap — required before any safety pre-assessment)
- Mechanism of action (MOA) data from DrugBank
- Preclinical or mechanistic studies specifically linking insulin signaling to autoimmune oophoritis pathophysiology
- If no such evidence emerges, this candidate should remain deprioritized

**Note:** Among the other predicted indications in this evidence pack, *pancreatic agenesis* (rank 7, L3, "Proceed with Guardrails") has a mechanistically direct rationale — insulin is the established standard of care for neonatal diabetes secondary to pancreatic agenesis — and may warrant a separate, dedicated evaluation report rather than being treated as this candidate's primary signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

