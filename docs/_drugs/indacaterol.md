---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From Chronic Obstructive Airway Disease to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is a long-acting β2-adrenergic receptor agonist (LABA) used in respiratory disease (COPD/asthma) based on the trial and mechanistic evidence in this pack; formal original-indication text could not be confirmed because the drug is currently unlicensed in the target market.
The TxGNN model's top-ranked prediction is **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this pairing has **0 clinical trials** and **0 publications** supporting it, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph false positive.
Across all 10 top-ranked TxGNN predictions for this drug, only one ("bronchial disease," rank 7) has strong clinical evidence (L1) — but that signal simply reconfirms the drug's known LABA pharmacology rather than representing a novel repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed by local license data (0 authorizations on file); drug class evidence points to COPD/asthma (LABA) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank MOA field is a data gap). Based on the mechanistic evidence embedded throughout this pack's clinical trial and rationale entries, indacaterol is a long-acting β2-adrenergic receptor agonist that produces bronchodilation via direct action on airway smooth muscle β2 receptors — the pharmacological basis for its established use in obstructive airway disease.

NSIAD, in contrast, is a hereditary disorder caused by gain-of-function mutations in the vasopressin V2 receptor, which drives renal water retention independent of any β2-adrenergic pathway. There is no known pharmacological, receptor-level, or physiological overlap between LABA activity and V2-receptor-mediated free water handling. The evidence pack's own repurposing rationale for this candidate explicitly characterizes it as a **graph-association false positive** rather than a genuine mechanistic hypothesis, and no clinical trials or literature exist to counter that assessment.

For context, of the 10 highest-ranked TxGNN predictions for indacaterol, nine (NSIAD, headache disorder, trigeminal autonomic cephalalgia, paratenonitis, calcific tendinitis, hypertrichosis, myositis, anaphylaxis, Ambras-type hypertrichosis) are flagged in the source rationale as lacking mechanistic plausibility or reflecting adverse-event signals mistaken for therapeutic ones. The tenth ("bronchial disease") is well supported (L1, multiple Phase 3 RCTs) but represents the drug's **already-established** LABA pharmacology, not a new indication. Taken together, this evidence pack does not currently surface a credible novel repurposing candidate for indacaterol.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No authorizations are on file — this product is currently **not marketed** in the target jurisdiction, and no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. Note that key warnings, contraindications, and drug-drug interaction data are all currently unavailable (flagged as a **Blocking** data gap — DG001: TFDA-equivalent package insert warnings/contraindications not yet sourced), which by itself precludes a full safety assessment (S1 stage) for any indication of this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (NSIAD) has no mechanistic plausibility, no clinical trials, and no literature support, and is explicitly assessed as a likely false positive. The only well-evidenced prediction in this pack ("bronchial disease") does not constitute a new indication. No repurposing case currently exists that would justify advancing past the earliest evaluation stage.

**To proceed, the following is needed:**
- TFDA-equivalent package insert (warnings/contraindications) — currently blocking (DG001)
- Detailed mechanism of action data from DrugBank — currently high-severity gap (DG002)
- A genuine mechanistic or preclinical rationale linking β2-adrenergic signaling to V2-receptor-mediated antidiuresis, if this candidate is to be pursued further
- If pursuing the "bronchial disease" signal instead, reframe as label-extension/on-mechanism confirmation rather than repurposing, and source formal local regulatory indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

