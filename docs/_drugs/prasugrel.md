---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Prasugrel
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

# Prasugrel: From Antiplatelet Therapy to Pulmonary Hypertension

## One-Sentence Summary

> Prasugrel is a thienopyridine P2Y12 receptor inhibitor (antiplatelet agent); detailed original indication and MOA data are not available in the current evidence pack.
> The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but the supporting evidence is limited to **2 clinical trials and 2 publications**, none of which directly address prasugrel or pulmonary hypertension — this is a high-score, low-evidence signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug not marketed in Norway; classified as a thienopyridine P2Y12 inhibitor / antiplatelet agent based on literature evidence) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa: [Data Gap]`). Based on information embedded in the evidence pack's literature notes, prasugrel is a thienopyridine-class P2Y12 receptor inhibitor, in the same pharmacological family as clopidogrel and ticlopidine, and its established role is as an antiplatelet agent (e.g., for stent thrombosis prevention).

For the top-ranked predicted indication, **pulmonary hypertension**, the model's own repurposing rationale is explicit about the weakness of the link: *"No direct mechanistic connection. Antiplatelet drugs may theoretically play an adjunct role in some thrombotic/CTEPH (chronic thromboembolic pulmonary hypertension) pathophysiology, but the trials and literature provided are not focused on pulmonary hypertension — this is a typical TxGNN high-score signal without corresponding evidence (a likely false positive)."*

Both retrieved clinical trials (NOAC use in atrial fibrillation; cancer-associated thrombosis screening) and both retrieved publications (COVID-19 comorbidity therapy; clopidogrel adherence post-PCI) are only tangentially related to antiplatelet therapy in general and do not study prasugrel in pulmonary hypertension. The mechanistic hypothesis (antiplatelet effect in CTEPH) is biologically plausible in theory but currently unsupported by direct data.

**Note on alternative candidates:** Among the other 9 predicted indications in this evidence pack, **migraine disorder** (rank 2, score 99.88%) has comparatively stronger supporting evidence — an open-label pilot study and a retrospective cohort study specifically describing thienopyridine (clopidogrel/prasugrel class) use reducing migraine symptoms in patients with patent foramen ovale (PFO), reaching evidence level **L3 / decision stage S1 (Research Question)**. This may warrant separate evaluation, though it is drug-class-level evidence rather than prasugrel-specific.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational cross-sectional study of NOAC management in elderly Spanish patients with non-valvular atrial fibrillation; no direct relevance to prasugrel or pulmonary hypertension (relevance grade C). |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on trial-eligibility for cancer-associated thrombosis (CARAVAGGIO-type population); does not involve prasugrel or pulmonary hypertension (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Curr Med Res Opin | Factors associated with clopidogrel adherence in ACS patients post-PCI; prasugrel mentioned only as an alternative regimen, not studied in pulmonary hypertension. |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Observational/retrospective | Kardiologiia | ACTIV registry analysis of background cardiovascular therapy and COVID-19 outcomes; no specific data on prasugrel or pulmonary hypertension. |

---

## Norway Market Information

Prasugrel currently holds **no marketing authorization** in Norway (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`). No product listings are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were retrievable for this evaluation (`DDI query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (pulmonary hypertension) has evidence level **L5** — a TxGNN model score with no corresponding disease-specific clinical trials or literature. Combined with the drug's non-marketed status in Norway and a **blocking data gap** on the official package insert (warnings/contraindications), the candidate does not currently meet the threshold to proceed past initial screening (S0).

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings and contraindications) — currently a **blocking** data gap (DG001)
- Confirmed mechanism of action data from DrugBank or equivalent source (DG002)
- Disease-specific (pulmonary hypertension, ideally CTEPH) preclinical or clinical evidence for prasugrel, rather than general antiplatelet-class literature
- If pursuing the migraine/PFO signal (rank 2) instead, a prasugrel-specific trial or case series, since current evidence is at the thienopyridine drug-class level only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

