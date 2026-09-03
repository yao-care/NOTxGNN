---
layout: default
title: Pegvaliase
parent: 僅模型預測 (L5)
nav_order: 271
evidence_level: L5
indication_count: 3
---

# Pegvaliase
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

# Pegvaliase: From Phenylketonuria to Diabetic Retinopathy

## One-Sentence Summary

Pegvaliase is a PEGylated phenylalanine ammonia lyase (PAL) enzyme substitution therapy originally used to control blood phenylalanine levels in **phenylketonuria (PKU)**.
The TxGNN model predicts it may be effective for **Diabetic Retinopathy**, but currently **no clinical trials and no literature** support this direction — the prediction is model-output only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Phenylketonuria (PKU) — control of blood phenylalanine levels |
| Predicted New Indication | Diabetic Retinopathy |
| TxGNN Prediction Score | 99.17% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note:** Two closely related indications were also flagged with near-identical scores and the same L5/Hold status: *severe nonproliferative diabetic retinopathy* (99.16%) and *diabetic cataract* (99.11%). None have any supporting trials or literature.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA: Data Gap). Based on known information, pegvaliase is an enzyme substitution therapy that metabolizes phenylalanine into trans-cinnamic acid and ammonia, and its efficacy in phenylketonuria is well established.

However, this mechanism has **no known biological overlap** with the pathophysiology of diabetic retinopathy, which is primarily driven by VEGF-mediated neovascularization, chronic hyperglycemia, oxidative stress, polyol pathway activation, and AGE accumulation. There is no plausible pharmacological pathway connecting phenylalanine metabolism to retinal microvascular disease.

Given that this drug node also has no recorded MOA and zero DDI entries in the knowledge graph, the sparse connectivity around pegvaliase likely produced a spurious high-confidence prediction rather than a genuine biological signal. This assessment is consistent with the evidence pack's own repurposing rationale, which explicitly flags the score as a probable false positive driven by data sparsity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Pegvaliase is **not currently marketed in Norway** and holds no marketing authorizations on record (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged in the evidence pack as a Blocking data gap — DG001 — meaning this candidate cannot proceed to S1 safety review until label data is obtained.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence supporting this indication, the mechanistic link between PAL enzyme substitution and diabetic retinopathy is biologically implausible, and the underlying MOA/DDI data gaps suggest the high TxGNN score may be an artifact of graph sparsity rather than a genuine signal. A Blocking data gap (missing TFDA warnings/contraindications) also prevents any safety review at this stage.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — resolves Blocking gap DG001
- Verified mechanism of action from DrugBank or primary literature — resolves High-priority gap DG002
- Preclinical or mechanistic evidence establishing a biological rationale linking PAL/phenylalanine metabolism to diabetic retinal disease
- At minimum, one observational study or case report before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

