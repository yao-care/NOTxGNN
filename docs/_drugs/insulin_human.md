---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Insulin Human
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

# Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin Human is the biosynthetic equivalent of endogenous human insulin, originally used to control blood glucose in diabetes mellitus. The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale confirms no known mechanistic connection between the two.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes Mellitus (Type 1/2, glycaemic control) — not formally documented in Taiwan license data (drug is not marketed) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a data gap in the evidence pack). Based on general clinical knowledge, Insulin Human is used to replace or supplement endogenous insulin for glycaemic control in diabetes mellitus. It is not currently marketed in Taiwan, so no formal Taiwanese label text exists to cross-reference.

For the top-ranked prediction, autoimmune oophoritis, the evidence pack's own repurposing rationale states there is **no direct physiological connection** between insulin and autoimmune oophoritis. The high TxGNN score is most likely driven by indirect co-occurrence of autoimmune-disease nodes within the knowledge graph, rather than a biologically interpretable mechanism. This is a case where a high model confidence score does not correspond to a credible pharmacological hypothesis.

It is also worth noting that this evidence pack contains 10 predicted indications for insulin, and the pattern across them is informative: several (drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced localized lipoatrophy, idiopathic localized lipodystrophy) are very likely **reversed-causality artifacts** — insulin injection is a well-known *cause* of localized lipodystrophy, not a treatment for it. The only candidate in the batch with a coherent clinical rationale is rank 9, "pancreatic agenesis" (L3, decision stage S2, "Research Question"), where insulin replacement is already standard care for the resulting neonatal diabetes — but this reflects existing practice rather than a genuinely novel indication. None of the batch currently rises to a level warranting active investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Insulin Human is not currently marketed in Taiwan (0 authorizations on record), so no product licenses are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting insulin for autoimmune oophoritis, and the mechanistic rationale explicitly states there is no known pathophysiological link — this pattern is consistent with a spurious knowledge-graph co-occurrence rather than a genuine therapeutic signal.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications data (blocking gap — required before any S1 safety screening can proceed)
- DrugBank mechanism-of-action data (high-priority gap affecting mechanistic assessment)
- Any preclinical or immunological evidence directly linking insulin signaling to ovarian autoimmune pathology, before this candidate is reconsidered
- If further exploration in this drug's prediction batch is desired, redirect attention to rank 9 (pancreatic agenesis), which has a plausible mechanism and L3 evidence, rather than the top-scored but mechanistically unsupported candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

