---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 1
---

# Mometasone
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

# Mometasone: From Corticosteroid-Responsive Dermatologic/Allergic Conditions to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

> Mometasone is a corticosteroid conventionally used to treat inflammatory dermatologic and allergic conditions (specific original indication not recorded in this evidence pack).
> The TxGNN model predicts it may be effective for **Primary Cutaneous T-Cell Lymphoma**,
> but currently **0 clinical trials** and only **2 case-report publications** are available, and one of them actually reports treatment failure with mometasone in a related condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (no `original_indications` or Norway license text available); mometasone is generally classified as a corticosteroid |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 (model prediction only — no direct supporting studies) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack. Based on general pharmacological knowledge, mometasone is a corticosteroid with anti-inflammatory and immunosuppressive properties, commonly used for inflammatory skin and allergic/respiratory conditions. A plausible mechanistic rationale for its use in cutaneous T-cell lymphoma (CTCL) is that topical corticosteroids can suppress cutaneous lymphocytic infiltration and inflammation, which is part of standard supportive/adjunct management in early-stage mycosis fungoides (a form of CTCL).

However, the two literature items retrieved for this prediction do not provide direct positive support: one describes a case of cutaneous pseudolymphoma (a *mimicker* of CTCL, not CTCL itself) in which mometasone treatment was **unsuccessful**, and the other is a pediatric mycosis fungoides case report whose abstract does not mention mometasone at all. This means the model's high score is not currently corroborated by direct clinical evidence — the association appears to be driven by network/embedding similarity rather than documented efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proceedings (Baylor University Medical Center) | Cutaneous pseudolymphoma (a CTCL mimic) on the nose; **mometasone and tacrolimus were both unsuccessful**; case eventually treated with tapinarof |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | Journal of Cutaneous Pathology | Pediatric (11-year-old) CD8+CD56+ mycosis fungoides (a primary CTCL subtype); abstract does not mention mometasone treatment |

⚠️ Neither publication demonstrates efficacy of mometasone for primary cutaneous T-cell lymphoma; one explicitly documents treatment failure in a related but distinct diagnosis.

---

## Norway Market Information

Mometasone is currently **not marketed** in Norway under this evidence pack (`market_status: 未上市`, 0 authorizations on file). No product license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications and drug-drug interaction data are listed as data gaps (DG001, blocking severity) in the evidence pack meta section and must be resolved before any clinical safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no clinical trial evidence and the only two literature citations do not support — and in one case contradict — efficacy for this indication. Combined with missing MOA data and a blocking gap in TFDA safety/label information, this candidate does not yet meet the threshold for further evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA label warnings/contraindications) — currently blocking safety evaluation
- Resolve DG002 (mechanism of action) via DrugBank to assess mechanistic plausibility for CTCL
- Identify literature or preclinical studies specifically evaluating corticosteroids (mometasone or class) in primary cutaneous T-cell lymphoma/mycosis fungoides, rather than tangential case reports
- Reassess whether the two retrieved case reports are genuinely relevant, given one shows treatment failure in a differential-diagnosis condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

