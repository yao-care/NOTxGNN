---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: From Diabetic Macular Edema to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Ranibizumab is an anti-VEGF (vascular endothelial growth factor) antibody fragment, with established use in neovascular eye diseases such as diabetic macular edema (DME) and wet age-related macular degeneration.
> The TxGNN model predicts it may also be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> with **6 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular (wet) age-related macular degeneration / diabetic macular edema — Ranibizumab's globally established anti-VEGF ophthalmic indications (not documented in this evidence pack's local license data) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Ranibizumab is a humanized anti-VEGF-A Fab fragment, part of the anti-VEGF ophthalmic therapeutic class, and its efficacy in neovascular retinal diseases (including diabetic macular edema) has been proven; mechanistically, it may also be applicable to severe nonproliferative diabetic retinopathy (NPDR).

VEGF is a central driver of vascular leakage and neovascularization in diabetic retinopathy. Ranibizumab directly blocks this pathway by binding VEGF-A. Diabetic macular edema (an already-established anti-VEGF indication) and severe NPDR are both stages along the same diabetic retinal disease continuum, meaning this prediction represents an extension of an already-validated mechanism-disease relationship rather than a novel, unrelated application.

This is supported by multiple large completed Phase 3 RCTs (e.g., the DRCR.net Protocol I program, RIDE/RISE, and the Pavilion trial evaluating a Port Delivery System with ranibizumab specifically in NPDR without center-involved DME), which collectively show that anti-VEGF therapy can delay or reverse progression along the DR severity scale — reinforcing that this is a mechanistically coherent, evidence-backed extension rather than a purely model-driven prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Completed | 691 | Compared laser alone, laser+triamcinolone, laser+ranibizumab, and ranibizumab alone for diabetic macular edema |
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Completed | 174 | Port Delivery System with ranibizumab vs comparator arm in diabetic retinopathy without center-involved DME — efficacy, safety, PK |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Completed | 399 | Intravitreal anti-VEGF for prevention of vision-threatening complications in high-risk diabetic retinopathy eyes |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Completed | 25 | Intravitreal ranibizumab in NPDR with macular edema — effects on microaneurysm turnover and non-perfused retinal area |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Unknown | 118 | Ranibizumab vs sham injections for prevention of progression in high-risk diabetic retinopathy |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Unknown | 1000 | Real-world observational study of anti-VEGF therapy (ranibizumab, aflibercept, conbercept) in exudative AMD, proliferative DR, macular edema, and CNV |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion trial: Port Delivery System with ranibizumab vs monitoring in NPDR without macular edema |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematic Review | Health Technology Assessment | Anti-VEGF drugs vs laser photocoagulation for diabetic retinopathy — systematic review and meta-analysis |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic Review | Health Technology Assessment | Anti-VEGF vs laser photocoagulation for diabetic retinopathy — systematic review and economic analysis |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Post-hoc RCT Analysis | Clinical Ophthalmology | Predictors of early DR regression with ranibizumab in the RIDE/RISE trials |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Meta-Analysis | Ophthalmology Retina | Baseline DR severity and time to DME resolution with ranibizumab — Phase 3 meta-analysis |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Post-hoc RCT Analysis | BMJ Open Ophthalmology | Effect of less aggressive ranibizumab treatment on Diabetic Retinopathy Severity Scale scores — RIDE/RISE open-label extension |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | Post-hoc RCT Analysis | Ophthalmic Surgery, Lasers & Imaging Retina | Course of DR in untreated fellow eyes in RIDE and RISE |
| [30973596](https://pubmed.ncbi.nlm.nih.gov/30973596/) | 2019 | Cohort | JAMA Ophthalmology | Retinal nonperfusion characteristics in severe NPDR and PDR on ultra-widefield angiography |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | Modeling/Simulation | BMJ Open Ophthalmology | Simulation of long-term impact of intravitreal anti-VEGF therapy in severe NPDR |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Overview of ranibizumab for the treatment of diabetic retinopathy |

---

## Norway Market Information

Ranibizumab currently holds no marketing authorization record in this evidence pack (Market status: **Not Marketed**, Total authorizations: **0**). No product-level licensing information is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and DDI data are flagged as a blocking data gap [DG001] in the evidence pack and require retrieval from the local regulatory authority's approved product label before proceeding to safety review.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 is supported by multiple completed Phase 3 RCTs (DRCR.net Protocol I, RIDE/RISE, the Pavilion PDS trial) demonstrating anti-VEGF efficacy across the diabetic retinopathy severity spectrum, and the mechanistic rationale is strong since DME is already an established ranibizumab indication. However, the drug is not currently marketed in this jurisdiction, and safety/regulatory documentation is incomplete.

**To proceed, the following is needed:**
- Local product label (warnings, contraindications, DDI) — currently a blocking data gap (DG001)
- Detailed mechanism of action documentation from DrugBank (DG002)
- Local market entry / registration status assessment, since the drug is currently not marketed in this jurisdiction
- Confirmation of outcome for the still-"Unknown" status trial (NCT03452657) before finalizing the evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

