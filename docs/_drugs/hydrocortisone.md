---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 169
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: From Corticosteroid/Anti-inflammatory Therapy to Alopecia Areata

## One-Sentence Summary

> Hydrocortisone is a glucocorticoid classically used for adrenocortical insufficiency and as an anti-inflammatory/immunosuppressive agent (specific approved-indication text is not documented in this evidence pack).
> The TxGNN model predicts it may be effective for **Alopecia Areata**,
> with **4 clinical trials** (including 1 completed Phase 3 RCT) and **21 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (`taiwan_regulatory.licenses` and `drug.original_indications` are both empty). General pharmacological class: corticosteroid, used for adrenal insufficiency / inflammatory-immune conditions |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa`: Data Gap). Based on general pharmacological knowledge, hydrocortisone is a corticosteroid class agent whose anti-inflammatory and immunosuppressive activity is well established across dermatologic and endocrine indications; specific TFDA/Norway-approved indication text is not present in this evidence pack.

Alopecia areata is a T-cell-mediated autoimmune attack on hair follicles. Topical corticosteroids, including hydrocortisone, are believed to act by suppressing local cytokine release and lymphocytic infiltration, thereby helping to restore the hair follicle's immune privilege. This is an established, widely used mechanism in dermatology rather than a novel hypothesis — it is directly reflected in the completed Phase 3 pediatric RCT (NCT01453686 / PMID 24226568) comparing hydrocortisone 1% cream with clobetasol propionate 0.05% cream, and echoed by decades of older case-series literature describing intradermal/intracutaneous hydrocortisone injection for alopecia areata and alopecia totalis.

Because hydrocortisone's anti-inflammatory mechanism is generic to the corticosteroid class rather than specific to any single original indication, its mechanistic applicability to an inflammatory/autoimmune dermatologic condition such as alopecia areata is biologically plausible even without a clearly recorded "original indication" in this pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | RCT directly comparing clobetasol propionate 0.05% cream vs. hydrocortisone 1% cream in children with alopecia areata — highest-relevance trial (Grade A) |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Completed | 18 | Evaluated adrenal function impact of intralesional triamcinolone (not hydrocortisone) in alopecia areata — indirect relevance |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | Not yet recruiting | 72 | Four-arm dose-response study of hair growth products vs. placebo in androgenic alopecia; corticosteroid arm composition not yet confirmed |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Studied steroid metabolome effects on bone strength/density in adrenal adenoma patients — not directly related to AA treatment efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Published RCT results: hydrocortisone 1% vs. clobetasol propionate 0.05% for alopecia areata in children |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Cohort/Interventional | Clinical and Experimental Dermatology | Retrospective analysis of topical corticosteroid under occlusion for severe alopecia areata (including alopecia totalis/universalis) in children |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Review | Journal of Cosmetic Dermatology | Systematic review/meta-analysis of AA treatment landscape, including corticosteroid comparators |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case series | Medical Times | Early case series treating alopecia areata, partialis and totalis with cortisone, hydrocortisone, prednisone and prednisolone |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | JEADV | Reviews HPA-axis/cortisol activity in alopecia areata pathophysiology |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Case series | Vestnik Dermatologii i Venerologii | Treatment of alopecia areata and total alopecia with intracutaneous hydrocortisone injections |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Case report | Der Hautarzt | Hair regrowth in alopecia areata/maligna after intracutaneous hydrocortisone injection |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Case report | Actas Dermo-Sifiliográficas | Treatment of alopecia areata with intradermal hydrocortisone injections |
| [22381765](https://pubmed.ncbi.nlm.nih.gov/22381765/) | 2012 | Mechanistic | Journal of Southern Medical University | Serum cortisol and glucocorticoid receptor mRNA expression in severe alopecia areata |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case report | Journal of the American Academy of Dermatology | Describes 4 cases of congenital alopecia areata, treatments included topical corticosteroids |

---

## Norway Market Information

Hydrocortisone currently has **no market authorizations on record** in this dataset (`market_status`: 未上市 / Not marketed; `total_licenses`: 0). No license table is available to display.

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and `ddi` are all marked as data gaps in this evidence pack; DG001 flags TFDA label warnings/contraindications as a **Blocking** data gap.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The lead prediction (alopecia areata) is supported by a completed Phase 3 pediatric RCT (NCT01453686/PMID 24226568) directly comparing hydrocortisone with an active corticosteroid comparator, reinforced by decades of case-series literature on hydrocortisone injection for alopecia areata — yielding an L1 evidence level. However, the drug is not currently marketed in Norway, and both mechanism-of-action data and TFDA-equivalent safety labeling (warnings/contraindications) are missing, preventing a full S1 safety assessment.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings and contraindications (DG001 — Blocking; required before initial safety screening)
- Detailed mechanism-of-action data from DrugBank (DG002)
- Confirmation of Norway market/registration pathway, since the drug currently has zero authorizations on record
- A formal drug interaction (DDI) profile, since the current query returned no results
- Clarification of the specific original approved indication(s), which were not populated in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

