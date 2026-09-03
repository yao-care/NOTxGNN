---
layout: default
title: Anakinra
parent: 僅模型預測 (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Anakinra
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

# Anakinra: From IL-1-Driven Inflammatory Disease to Familial Mediterranean Fever

## One-Sentence Summary

> Anakinra is a recombinant IL-1 receptor antagonist; the evidence pack does not contain a documented original indication (Anakinra holds **0 marketing authorizations in Norway**), but its IL-1-blocking mechanism is consistently referenced across the literature reviewed here. TxGNN screened **10 candidate indications** for this drug, and among them **Familial Mediterranean Fever (FMF)** shows by far the strongest real-world support — anakinra is already used clinically as second-line therapy for colchicine-resistant/intolerant FMF, backed by **18 publications** (though **0 registered clinical trials**) in this dataset.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — Anakinra has no marketing authorization in Norway (0 licenses); indication text unavailable from regulatory dataset |
| Predicted New Indication | Familial Mediterranean Fever (autosomal recessive) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured mechanism-of-action record is available for anakinra in this evidence pack (`original_moa` is a documented data gap, DG002). However, the mechanistic rationale text embedded across multiple predicted indications in this same evidence pack consistently and independently identifies anakinra as a **recombinant IL-1 receptor antagonist** that blocks IL-1α/β signaling — this is corroborating information drawn directly from the evidence, not an external assumption.

FMF is caused by *MEFV* gene mutations that produce a dysfunctional pyrin protein, leading to unregulated inflammasome activation and excessive IL-1β release. This creates a direct mechanistic match with anakinra's IL-1 blockade: the drug is not merely "theoretically" applicable — the literature reviewed here shows it is **already used in real-world clinical practice** as rescue/second-line therapy for FMF patients who fail or cannot tolerate colchicine (the first-line standard of care), including cases complicated by AA amyloidosis and renal failure.

Because Norway has no marketing authorization for anakinra on file, this "new indication" is best understood as a **known, internationally-supported off-label/guideline use** that is not yet reflected in local regulatory status — the gap here is regulatory/administrative rather than mechanistic or clinical.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21277619](https://pubmed.ncbi.nlm.nih.gov/21277619/) | 2011 | Case Series/Review | Semin Arthritis Rheum | IL-1 receptor antagonism (anakinra) and anti-IL-1 mAbs proposed as rational treatment given pyrin's role in IL-1 maturation/secretion |
| [23322405](https://pubmed.ncbi.nlm.nih.gov/23322405/) | 2013 | Review/Cohort | Clin Rev Allergy Immunol | Comprehensive review of IL-1β biological treatment (anakinra/canakinumab) in colchicine-refractory FMF |
| [19033248](https://pubmed.ncbi.nlm.nih.gov/19033248/) | 2009 | Case Report | Nephrol Dial Transplant | Successful anakinra treatment of FMF before/after renal transplantation, with preserved graft outcome |
| [21931121](https://pubmed.ncbi.nlm.nih.gov/21931121/) | 2012 | Case Series | Nephrol Dial Transplant | Dramatic clinical improvement with IL-1 inhibitor treatment in FMF complicated by amyloidosis and renal failure |
| [23928237](https://pubmed.ncbi.nlm.nih.gov/23928237/) | 2013 | Case Report | Joint Bone Spine | FMF-associated myositis and spondyloarthritis successfully controlled with anakinra |
| [34550430](https://pubmed.ncbi.nlm.nih.gov/34550430/) | 2022 | Case Series | Rheumatol Int | Canakinumab effective in FMF patients resistant/intolerant to colchicine and/or anakinra (real-world experience) |
| [28585601](https://pubmed.ncbi.nlm.nih.gov/28585601/) | 2017 | Case Series | JPMA | Anakinra used successfully in four children with colchicine-resistant FMF, including sibling cases |
| [31205631](https://pubmed.ncbi.nlm.nih.gov/31205631/) | 2019 | Review | Mediterr J Hematol Infect Dis | Overview of FMF clinical impact and treatment algorithms, incorporating IL-1 blockade for colchicine-resistant cases |
| [26572612](https://pubmed.ncbi.nlm.nih.gov/26572612/) | 2016 | Review | Curr Med Chem | Review of colchicine, biologic agents (including anakinra), and emerging therapies for FMF |
| [23867542](https://pubmed.ncbi.nlm.nih.gov/23867542/) | 2014 | Review | Clin Pharmacol Ther | Progression from colchicine to biologic (IL-1 antagonist) therapies in FMF management |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the underlying evidence pack flags TFDA/label warnings and contraindications as a **Blocking-severity data gap** (DG001) — this must be resolved before any formal safety review can proceed; see Conclusion below.)*

---

## Other Candidate Indications Identified by TxGNN (Same Drug)

Anakinra's evidence pack contains 10 TxGNN-ranked candidates in total. For transparency, the two other candidates with real (non-L5) evidence support are listed here alongside the top-scoring but unsupported prediction:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|------------------|------|
| 1 | Extracutaneous mastocytoma | 99.93% | L5 | Hold | Highest raw TxGNN score, but **zero clinical/literature evidence**; KIT-driven pathology has no clear mechanistic link to IL-1 blockade |
| 3 | Familial Mediterranean Fever | 99.89% | L3 | Proceed with Guardrails | **Primary candidate in this report** — strong mechanistic and real-world clinical support |
| 9 | Pyogenic autoinflammatory syndrome (PAPA/PSTPIP1 spectrum) | 99.83% | L3 | Proceed with Guardrails | Second strongest candidate; PSTPIP1-driven IL-1β overproduction, direct anakinra treatment reports exist |
| 4 | Aggressive systemic mastocytosis | 99.88% | L4 | Hold | Literature retrieved actually describes **Schnitzler syndrome**, not mastocytosis — likely label mismatch, needs manual verification |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Familial Mediterranean Fever has the strongest evidence base among all TxGNN-predicted indications for anakinra — pyrin/IL-1 inflammasome pathophysiology directly matches the drug's mechanism, and multiple case series/reviews confirm real-world use in colchicine-resistant patients. However, evidence is limited to L3 (no RCTs), and anakinra currently holds **zero marketing authorizations in Norway**, so this cannot proceed as an unconditional "Go."

**To proceed, the following is needed:**
- Resolve the **Blocking** safety data gap (DG001): obtain TFDA/official label warnings, contraindications, and DDI data before any S1 safety review
- Obtain structured MOA documentation from DrugBank (DG002) to formally confirm IL-1 receptor antagonist classification
- Clarify Norway/EU regulatory pathway status for anakinra, including any existing off-label use precedent for FMF
- Given the absence of RCTs, consider prospective or registry-based studies to strengthen the evidence level beyond L3
- Manually verify TxGNN disease-label accuracy for lower-confidence candidates (e.g., rank 4's literature mismatch with Schnitzler syndrome) before further screening resources are allocated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

