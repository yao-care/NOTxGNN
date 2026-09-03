---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab: From Thyroid Eye Disease to Monosomy X

## One-Sentence Summary

Teprotumumab is an IGF-1R antagonist known for treating thyroid eye disease (Graves' ophthalmopathy). The TxGNN model predicts it may be effective for **Monosomy X** (a Turner syndrome karyotype), but this is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags a potential mechanistic contradiction rather than a genuine pharmacological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid eye disease (Graves' ophthalmopathy) — inferred from the drug's known clinical use; no Norway regulatory license data is available |
| Predicted New Indication | Monosomy X |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record (`original_moa: [Data Gap]`). Based on information embedded elsewhere in this evidence pack, teprotumumab is known to act as an **IGF-1R (insulin-like growth factor-1 receptor) antagonist**, used clinically to reduce orbital inflammation and fibrosis in thyroid eye disease.

Monosomy X is a karyotype associated with Turner syndrome. Growth impairment in Turner syndrome is conventionally managed by **promoting** GH/IGF-1 signaling — the opposite pharmacological direction from teprotumumab's IGF-1R **blockade**. The evidence pack's own rationale explicitly notes this direction conflict and suggests the prediction more likely reflects a knowledge-graph proximity artifact (shared "IGF-1R" or "X-chromosome disorder" nodes) than a validated mechanistic relationship.

Given this direct conflict between the drug's known pharmacology and the biological need of the predicted indication, and the complete absence of clinical or preclinical corroboration, this prediction should be treated as exploratory only, not as a credible repurposing lead at this stage.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Teprotumumab is currently **not marketed** in Norway (0 authorizations on file; no license records available).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Monosomy X, part of the Turner syndrome spectrum) has zero clinical trial or literature support, and the pack's own mechanistic analysis suggests the drug's IGF-1R-blocking action may run counter to the growth-promotion need in this condition. Combined with the drug's non-marketed status in Norway, there is no basis to advance beyond hypothesis generation.

**To proceed, the following is needed:**
- Confirmed MOA and original indication data (currently `[Data Gap]`) from DrugBank/manufacturer sources
- Preclinical or mechanistic studies clarifying any plausible role of IGF-1R modulation in Turner syndrome/monosomy X biology
- TFDA-equivalent safety data — warnings, contraindications, and DDI (currently all `[Data Gap]` or not found)
- Any emerging clinical case reports or trials before re-evaluating this candidate

*Note: This evidence pack contains 9 additional candidate indications (rank 2–10, including esophageal varices, mixed gonadal dysgenesis, and related X-chromosome/vascular conditions), all scored L5/Hold with no supporting trials or literature and similarly weak or unresolved mechanistic rationale. None currently warrant progression.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

