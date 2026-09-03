---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 1
---

# Caspofungin
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

# Caspofungin: From Antifungal Therapy to Gastrin Secretion Abnormality

## One-Sentence Summary

Caspofungin is an echinocandin-class antifungal agent; the evidence pack does not specify its Norway-approved indication (drug is currently unmarketed there).
The TxGNN model predicts a possible link to **Gastrin Secretion Abnormality**, but this prediction is supported by **zero clinical trials** and **zero publications**, and the accompanying mechanistic analysis explicitly finds no plausible biological pathway connecting the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (known drug class: echinocandin antifungal; no approved-indication text provided) |
| Predicted New Indication | Gastrin Secretion Abnormality |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only, no supporting trials/literature) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, the drug's `original_moa` field is marked as a data gap. However, the evidence pack's own mechanistic rationale identifies caspofungin as an echinocandin antifungal that inhibits fungal cell wall β-1,3-D-glucan synthase — a fungus-specific enzyme with no human homolog.

No known pharmacological pathway links this mechanism to gastrin secretion regulation (e.g., G-cell function, H+/K+-ATPase, somatostatin signaling, or CCK2 receptor activity). The original indication (systemic antifungal therapy) and the predicted new indication (a gastroenterological/endocrine disorder) share no obvious pathophysiological overlap.

Given the complete absence of clinical trials or literature, and the lack of any interpretable biological mechanism, this prediction is most likely a model artifact or a false-positive association within the knowledge graph rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

No authorizations on record — caspofungin is not currently marketed in Norway (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate sits at evidence level L5 (model score only) with no clinical trials, no literature, and no plausible mechanistic link — the evidence pack's own rationale argues against biological plausibility. It does not meet the minimum bar to advance past S0.

**To proceed, the following is needed:**
- Confirmed MOA and TFDA/regulatory label data (currently blocking safety review per DG001/DG002)
- Independent literature or preclinical evidence establishing a mechanistic link between echinocandin activity and gastrin regulation
- If no such evidence emerges, this candidate should be deprioritized as a likely false-positive prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

