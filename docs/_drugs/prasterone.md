---
layout: default
title: Prasterone
parent: 僅模型預測 (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
---

# Prasterone
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

# Prasterone: From Unspecified Original Indication to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

> Prasterone (DHEA, DB01708) is an adrenal steroid hormone precursor; no approved indication data is available in this evidence pack, and the drug is not currently marketed in Norway.
> The TxGNN model's top prediction is **Heparin Cofactor 2 Deficiency**, but this candidate has **no supporting clinical trials or literature**, and the proposed mechanism runs counter to known androgen pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (no license/indication records available) |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.99% (rank 223 of full disease list) |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for prasterone. Based on known pharmacological classification, prasterone (DHEA) is an adrenal steroid precursor that is peripherally converted into androgens and estrogens; this general class-level fact is not specific enough to establish a mechanistic bridge to heparin cofactor II deficiency.

Heparin cofactor II deficiency is a hereditary disorder in which the therapeutic goal is to **restore anticoagulant activity**. Androgens, however, are generally associated with **pro-coagulant effects** — increased clotting factor synthesis and reduced natural anticoagulant activity (a pattern also reflected in this same evidence pack's other top predictions, such as antithrombin deficiency and protein S deficiency, all flagged with the same directional concern). This places the predicted indication in mechanistic tension with the drug's known pharmacology rather than in support of it.

Given the absence of any clinical trials, published literature, or documented MOA linking prasterone to this disease, this ranks as a pure network-topology prediction (L5) with a plausible biological argument *against* efficacy rather than for it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Prasterone currently holds **no marketing authorizations in Norway** (market status: Not Marketed; total authorizations: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/label warnings and contraindications data are currently unavailable — see data gaps below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (heparin cofactor 2 deficiency) has zero clinical or literature evidence and its proposed pharmacology conflicts with androgens' known pro-coagulant tendency, making it biologically implausible as currently framed. Combined with missing MOA and safety label data, this candidate does not meet the bar to advance past S0.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (blocking gap — required before any S1 safety screening)
- Confirmed mechanism of action data from DrugBank or primary literature
- Experimental or clinical evidence on DHEA's effect on heparin cofactor II / antithrombin / protein S activity, given the directional safety concern raised above
- Consider deprioritizing this top-ranked candidate: within this same prediction batch, **scleroderma (rank 7)** has stronger biological rationale (L4 evidence, 6 observational studies consistently showing DHEA-S deficiency correlating with disease severity, decision stage S1 "Research Question") and may be a more productive candidate to pursue next.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

