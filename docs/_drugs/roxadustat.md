---
layout: default
title: Roxadustat
parent: 僅模型預測 (L5)
nav_order: 316
evidence_level: L5
indication_count: 4
---

# Roxadustat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Roxadustat: From Renal Anemia to Dry Eye Syndrome

## One-Sentence Summary

Roxadustat is a HIF prolyl-hydroxylase inhibitor (HIF-PHI) originally developed to treat renal anemia (anemia associated with chronic kidney disease) by stabilizing HIF-1α/2α and inducing endogenous erythropoietin production. The TxGNN model predicts potential efficacy for **Dry Eye Syndrome**, but currently only **1 clinical trial** (an observational study, not an efficacy trial) and **no supporting literature** back this direction — the evidence base remains preliminary (**L4**).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal anemia (chronic kidney disease-associated anemia) — inferred from mechanistic rationale in the evidence pack; no formal regulatory indication text available, as the drug is not marketed in Norway |
| Predicted New Indication | Dry Eye Syndrome |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in the regulatory data (data gap). Based on the mechanistic rationale captured alongside the TxGNN prediction, roxadustat is a HIF-PHI (HIF prolyl-hydroxylase inhibitor) that stabilizes HIF-1α/2α to induce erythropoietin (EPO) production, and is used to treat renal anemia.

The proposed link to dry eye syndrome is theoretical: HIF signaling is known to regulate the hypoxia response of corneal and conjunctival epithelium, and meibomian gland dysfunction — a key contributor to dry eye — involves inflammatory, hormonal, and microvascular/oxidative-stress pathways that could plausibly intersect with HIF biology. However, this is an indirect mechanistic hypothesis rather than a demonstrated pharmacological effect.

Importantly, the only supporting clinical trial does not test roxadustat's efficacy for dry eye — it is an observational study characterizing meibomian gland structure/function in renal anemia patients who happen to present with dry eye symptoms. The overlap is due to shared patient population (renal anemia patients), not a therapeutic intervention being evaluated. This substantially limits the strength of the current evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06287879](https://clinicaltrials.gov/study/NCT06287879) | NA (Observational) | Unknown | 50 | Characterizes meibomian gland function/morphology in renal anemia patients with dry eye symptoms; does not evaluate roxadustat's therapeutic effect on dry eye. Relevance graded **C** — indirect, population-overlap only. |

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Roxadustat is not currently marketed in Norway. No product authorizations are on record (0 licenses).

---

## Other Candidate Indications (Lower Priority, Not Detailed Above)

The evidence pack also flagged three additional TxGNN candidates, all at evidence level L5 (model prediction only, no clinical or literature support). These are noted for completeness but are not recommended for further evaluation at this time:

| Disease | TxGNN Score | Note |
|------|------|------|
| Bone Paget disease | 99.12% | Purely mechanistic hypothesis (HIF role in osteoclast/vascular coupling); no clinical or preclinical data |
| Dentinogenesis imperfecta | 99.06% | Weak biological plausibility; likely reflects indirect graph connectivity rather than a true mechanistic link |
| Squamous cell carcinoma | 99.02% | **Safety signal, not a treatment opportunity** — HIF-1α/2α activation is generally understood to promote tumor angiogenesis, invasion, and chemoresistance in squamous cell carcinoma. This pairing should be treated as a potential contraindication/risk signal rather than a repurposing candidate. |

---

## Safety Considerations

No structured safety data (warnings, contraindications, or drug interactions) is currently available for roxadustat in this evidence pack — please refer to the package insert for safety information once available.

**Class-level caution (from mechanistic analysis, not formal safety data):** As a HIF-PHI, roxadustat's core mechanism (HIF stabilization) has a theoretical association with tumor-promoting pathways (see squamous cell carcinoma signal above). This should be factored into any future safety assessment, particularly for oncology-adjacent or malignancy-risk populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The dry eye syndrome prediction is currently supported only by an observational trial with indirect (population-overlap) relevance and no efficacy data, no literature, and no regulatory/safety documentation. The drug is also not marketed in Norway. Evidence is insufficient to justify progression at this time.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/local label warnings and contraindications) and DG002 (formal MOA documentation) — both currently blocking or high-severity data gaps
- An interventional trial or preclinical study directly testing roxadustat's effect on dry eye syndrome or meibomian gland function
- Literature review to establish biological plausibility beyond the current single-trial population overlap
- DDI and contraindication data before any S1 safety review can proceed
- A dedicated risk assessment of the HIF-activation/malignancy signal (see squamous cell carcinoma note) before any further repurposing work on this molecule
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

