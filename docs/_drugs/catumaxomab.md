---
layout: default
title: Catumaxomab
parent: 僅模型預測 (L5)
nav_order: 79
evidence_level: L5
indication_count: 3
---

# Catumaxomab
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

Using no formal skill here — this is a direct documentation/report-writing task with a fixed template, not a coding or debugging task requiring skill workflows.

Note: The evidence pack uses field name `taiwan_regulatory` and `candidate_id: TW-...`, with Chinese-language field values (e.g., `market_status: "未上市"`), confirming this is a **Taiwan** market context — I've labeled the market section accordingly rather than "Norway" (the latter appears to be a template artifact from a different country's report).

---

# Catumaxomab: From Not Available to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Catumaxomab's original indication and mechanism of action are not documented in this evidence pack (Data Gap DG002, High severity).
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but this is a **model-score-only prediction (L5)** — no clinical trials or literature currently support it, and two other candidates (drug-induced osteoporosis, diabetic retinopathy) show the same pattern.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no data provided; see Data Gap DG002) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.64% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for catumaxomab in this evidence pack (Data Gap DG002, High severity), and no original indication was provided either. This means the pharmacological relationship between catumaxomab's established use and the predicted new indications cannot be established from the data on hand.

More importantly, the evidence pack's own repurposing rationale argues **against** mechanistic plausibility for all three ranked candidates. The rationale text describes catumaxomab as a trifunctional bispecific antibody (anti-EpCAM × anti-CD3) that works via T-cell–mediated tumor cytolysis, requires intraperitoneal administration, and carries a known risk of systemic cytokine release reaction. It explicitly states there is **no known biological link** between this mechanism and either the vascular/metabolic pathology of diabetic retinopathy (ranks 1 and 3) or osteoclast/osteoblast bone-remodeling pathways (rank 2), and flags "high mechanistic implausibility."

Given that the high TxGNN scores (>99% for all three) are not corroborated by any mechanistic, preclinical, or clinical evidence — and are directly contradicted by the model's own rationale text — these candidates should be treated as model-only statistical signals rather than scientifically supported repurposing hypotheses at this time.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Catumaxomab is **not marketed in Taiwan** (0 authorizations on record). No product license or approved-indication data is available in this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings/contraindications data is a **Blocking** data gap — DG001 — and must be resolved before any safety assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model score only) for all three predicted indications, with zero supporting clinical trials or literature. The model's own mechanistic rationale argues against plausibility, the drug is unmarketed in Taiwan, and a Blocking-severity safety data gap (TFDA warnings/contraindications) remains unresolved.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (resolves DG001, Blocking — required before any S1 safety screening)
- Catumaxomab mechanism of action detail from DrugBank (resolves DG002, High)
- Original indication and approved clinical usage history for catumaxomab
- Any preclinical or clinical evidence directly linking EpCAM×CD3 T-cell engagement to diabetic retinopathy or osteoporosis pathophysiology, if this candidate is to be revisited
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

