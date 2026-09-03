---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Normal Breast-like Subtype of Breast Carcinoma

## One-Sentence Summary

> Trastuzumab is a HER2/ERBB2-targeted monoclonal antibody, historically established for HER2-overexpressing breast cancer (original indication data itself is a documented gap in this evidence pack — see below).
> The TxGNN model's top prediction is that trastuzumab may be effective for the **normal breast-like PAM50 subtype of breast carcinoma**,
> with **12 clinical trials** and **1 publication** currently associated with this prediction — though the evidence itself flags a mechanistic contradiction (see rationale below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the structured regulatory data (data gap). Based on the drug's known mechanism and the repurposing rationale embedded in this evidence pack, trastuzumab's established use is HER2-overexpressing breast cancer. |
| Predicted New Indication | Normal breast-like subtype of breast carcinoma |
| TxGNN Prediction Score | 99.90% (rank 1423 of full candidate list) |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold (Research Question stage) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available at the drug level (**Data Gap DG002**). Based on the mechanistic descriptions embedded throughout this evidence pack's repurposing rationale, trastuzumab is a humanized monoclonal antibody that binds the extracellular domain of HER2 (ERBB2), blocking its downstream proliferative signaling and mediating antibody-dependent cell-mediated cytotoxicity (ADCC). Its efficacy in HER2-overexpressing breast cancer has been extensively demonstrated, and the top TxGNN-predicted new indication — "normal breast-like" — is itself a molecular subtype *of breast cancer*, not a distinct disease category. In that narrow sense, the prediction is not a large mechanistic leap.

However, the evidence pack's own rationale for this specific prediction flags an important **biological contradiction**: the PAM50 "normal-like" subtype is clinically characterized by low proliferative activity and is frequently HER2-low or HER2-negative — the opposite of the population in which trastuzumab has proven benefit. None of the 12 associated clinical trials were designed to specifically enrich for or test this PAM50 subtype; most are general HER2-positive breast cancer trials in which trastuzumab appears as a background or comparator therapy. The single literature citation (PMID 19466513) discusses basal-like, not normal-like, tumor morphology, and is a general review rather than subtype-specific outcome data.

Taken together, this prediction is plausible only insofar as "normal breast-like" falls within the broad breast-cancer indication space trastuzumab already occupies — but the model's confidence score does not resolve the underlying mechanistic mismatch (HER2-targeted therapy applied to a typically HER2-low/negative subtype). This is why the evidence pack itself stages this candidate at **S1 / "Research Question"** rather than a more advanced decision stage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, Not Recruiting | 720 | Weekly paclitaxel ± carboplatin in large operable/locally advanced triple-negative (basal-like) breast cancer; population defined by conventional HER2 status, not PAM50 normal-like stratification (Grade B). |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Phase 2 | Completed | 23 | Paclitaxel + trastuzumab + pertuzumab as pre-operative therapy for inflammatory HER2+ breast cancer; no subtype-specific design (Grade B). |
| [NCT04329065](https://clinicaltrials.gov/study/NCT04329065) | Phase 2 | Recruiting | 25 | WOKVAC vaccine + neoadjuvant chemotherapy + HER2-targeted antibody therapy; trastuzumab is background treatment, not the primary evaluated agent (Grade C). |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Phase 1/2 | Unknown | 120 | Hydroxychloroquine + antibody-drug conjugate vs. ADC alone in advanced breast cancer; status unknown, weak evidentiary value (Grade C). |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Phase 2 | Recruiting | 370 | Trastuzumab deruxtecan (an ADC, not naked trastuzumab) with biology-driven treatment selection for HER2-positive breast cancer; does not directly test trastuzumab in normal-like subtype (Grade C). |
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Phase 2 | Active, Not Recruiting | 55 | ATREZZO study: atezolizumab + trastuzumab + vinorelbine in ER-negative or PAM50 non-luminal HER2-positive advanced/metastatic breast cancer. |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Phase 1/2 | Recruiting | 46 | Drug-screening-guided neoadjuvant therapy using patient-derived tumor-like cell clusters in HER2-positive early breast cancer. |
| [NCT06585969](https://clinicaltrials.gov/study/NCT06585969) | Phase 3 | Withdrawn | 0 | Trastuzumab deruxtecan vs. CDK4/6 inhibitors in non-Luminal A, ER-positive/HER2-low metastatic breast cancer; trial withdrawn before enrollment. |
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | Completed | 56 | Neratinib alone/with fulvestrant in HER2 non-amplified but HER2-mutant metastatic breast cancer. |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Phase 2 | Recruiting | 74 | Efficacy/safety of optimal neoadjuvant-to-adjuvant anti-HER2 therapy in Nigerian women with HER2-positive breast cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Review | Breast Cancer (Tokyo, Japan) | Describes morphological/cytopathological characteristics of the basal-like breast carcinoma subtype within the five-subtype intrinsic classification (luminal A, luminal B, normal-like, HER2-overexpressing, basal-like); does not directly address trastuzumab response in the normal-like subtype. |

---

## Norway Market Information

Trastuzumab is currently **not marketed** in this jurisdiction according to the regulatory data provided (0 authorizations, no license records available). No product/dosage-form table can be generated from this evidence pack.

---

## Cytotoxicity

Trastuzumab is classified as antineoplastic — all TxGNN-predicted indications in this pack are cancers/tumors, and the drug's mechanism (HER2/ERBB2-targeted cytotoxic activity via ADCC) falls under oncology therapeutics.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-targeted humanized monoclonal antibody; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (specific hematologic toxicity data not available in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are marked as data gaps in this evidence pack — **DG001, Blocking severity** — and could not be populated from the TFDA/regulatory label source.)

---

## Conclusion and Next Steps

**Decision: Hold (Research Question)**

**Rationale:**
The top-ranked prediction (normal breast-like PAM50 subtype) is supported only by L3 evidence — a single review article and no subtype-specific completed trials — and the evidence pack's own mechanistic rationale identifies a biological contradiction, since this subtype is typically HER2-low/negative, undermining trastuzumab's core targeted mechanism. This candidate should not advance past the research-question stage without subtype-specific validation. (Note: within this same evidence pack, the PR-positive and PR-negative breast cancer candidates, ranks 2–3, reach a stronger L2 evidence level with completed Phase 3 RCTs and are separately staged "Proceed with Guardrails" — these may warrant prioritization over the rank-1 candidate.)

**To proceed, the following is needed:**
- TFDA/regulatory label data — warnings, contraindications, DDI (DG001, Blocking)
- Confirmed, sourced mechanism-of-action documentation at the drug level (DG002)
- HER2 expression prevalence data specifically within the PAM50 "normal-like" subtype population
- A subtype-specific prospective trial (or retrospective biomarker-stratified analysis) testing trastuzumab response in HER2-low/negative "normal-like" tumors before this candidate can be re-staged
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

