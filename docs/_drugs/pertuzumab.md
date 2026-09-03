---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Pertuzumab is a HER2-targeted monoclonal antibody already established (per the source clinical trial literature) as an FDA-approved treatment for HER2-positive breast cancer, typically combined with trastuzumab and a taxane.
> The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**,
> with **10 clinical trials** and **20 publications** currently associated — though notably, several of the top trials actually enrolled **PR/ER-negative** populations, which is the opposite molecular profile of the predicted indication.
> Given this evidence mismatch plus multiple unresolved data gaps (mechanism of action, safety label, Norway market status), this candidate requires manual curation before further action.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (established use, referenced across the trial evidence base; not separately documented in the Evidence Pack's regulatory fields) |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 (evidence exists but is largely indirect/mismatched — see rationale below) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for pertuzumab is not available in this Evidence Pack (flagged as a High-severity data gap). Based on information embedded in the supporting clinical trial records, pertuzumab is a monoclonal antibody that "blocks members of a family of proteins that include Human Epidermal Growth Factor Receptor 2 (HER2)" and is used together with trastuzumab (and typically a taxane such as docetaxel) as standard-of-care therapy for HER2-positive breast cancer, both in the neoadjuvant/adjuvant and metastatic settings.

The predicted new indication — PR-positive breast cancer — is not a distinct disease but a hormone-receptor subclassification that can co-occur with HER2 positivity (i.e., "triple-positive" or HR+/HER2+ breast cancer). Several trials in the evidence set do study this overlap population directly (e.g., NCT02689921 evaluating aromatase inhibitor + pertuzumab/trastuzumab in HR+/HER2+ disease; NCT00999804 comparing lapatinib+trastuzumab ± endocrine therapy in HER2-overexpressing, hormone-receptor-relevant disease), which supports a plausible mechanistic rationale: dual HER2 blockade combined with endocrine therapy in HR+/HER2+ tumors.

However, a substantial portion of the "top" cited trials for this specific prediction (e.g., NCT04629846, NCT03726879) actually enrolled **ER/PR-negative** or hormone-receptor-unselected HER2-positive populations — the opposite or a non-matching biomarker profile relative to the predicted indication. This suggests the evidence retrieval captured general "pertuzumab + HER2-positive breast cancer" literature rather than PR-positive-specific data, and the prediction itself may simply be re-identifying an already-covered biomarker subgroup of the drug's existing approved use rather than a genuinely novel therapeutic direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Pertuzumab biosimilar (QL1209) vs. reference pertuzumab + docetaxel in HER2-positive, **ER/PR-negative** early/locally advanced breast cancer (mismatched biomarker profile) |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | Biosimilar (BCD-178) vs. Perjeta as neoadjuvant therapy in ER/PR-negative HER2-positive breast cancer |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 + pertuzumab preoperative therapy; explores HER2 heterogeneity, not PR-status-specific |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | Neoadjuvant Herceptin/docetaxel/pertuzumab combinations in HER2-positive breast cancer (unselected for PR status) |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective non-interventional study of HER2-low prevalence and treatment patterns; not PR-specific |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Withdrawn | 0 | Neoadjuvant paclitaxel in Nigerian women with breast cancer; withdrawn, no enrollment |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | Neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab (chemo-free) specifically in **HR+ (ER+/PR+) HER2+** localized breast cancer — directly relevant, but very small (n=7) and unknown status |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab vs. placebo with neoadjuvant chemo + trastuzumab/pertuzumab in early HER2-positive breast cancer; not PR-status stratified |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | Neoadjuvant lapatinib + trastuzumab ± endocrine therapy in HER2-overexpressing breast cancer; relevant to HR-pathway crosstalk |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: de-escalated adjuvant chemo in HER2+, **ER-negative**, node-negative early breast cancer — again a mismatched (ER-negative) population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (5-yr follow-up) | Lancet Oncology | NeoSphere trial: neoadjuvant pertuzumab + trastuzumab improved pathological complete response in HER2-positive breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (Phase 2) | Annals of Oncology | WSG-ADAPT HER2+/HR- trial: 12-week neoadjuvant dual HER2 blockade ± paclitaxel, de-escalation strategy |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II: endocrine therapy + trastuzumab/pertuzumab vs. de-escalated chemo in **HR-positive/HER2-positive** early breast cancer — directly relevant to PR-positive population |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (Phase 3 equivalence) | British Journal of Cancer | QL1209 biosimilar vs. reference pertuzumab in HER2-positive, **ER/PR-negative** breast cancer (mismatched population) |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase 2, open-label) | J Clin Oncol | PERTAIN trial: trastuzumab + aromatase inhibitor ± pertuzumab in **HER2-positive and hormone-receptor-positive** metastatic/LABC — directly relevant |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update on systemic therapy for HER2-positive advanced breast cancer |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treatment Reviews | Overview of HR/HER2-positive breast cancer biology and crosstalk between ER and HER2 pathways |
| [33662161](https://pubmed.ncbi.nlm.nih.gov/33662161/) | 2021 | Review | Eur J Clin Invest | CDK4/6 and PI3K inhibitors as emerging combination strategies in HER2-positive breast cancer |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Review | Breast Cancer (Tokyo) | Advances in intrinsic signaling pathway interactions and clinical translation of HR+/HER2+ breast cancer |
| [32905036](https://pubmed.ncbi.nlm.nih.gov/32905036/) | 2020 | Review | Cureus | Therapeutic strategies for HER2-positive metastatic breast cancer, covering receptor subtyping including PR status |

---

## Norway Market Information

Pertuzumab is **not currently marketed in Norway** — no authorization records are on file (`total_licenses = 0`). No original approved-indication text is available from local regulatory sources to verify against the global (FDA/EMA) approved indication referenced in the clinical trial evidence.

---

## Cytotoxicity

Pertuzumab is an antineoplastic biologic (anti-HER2 humanized monoclonal antibody), so this section applies, though it is **not** a conventional cytotoxic chemotherapy agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2-dimerization inhibitor monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Cardiac function (LVEF) monitoring is standard practice for anti-HER2 therapy given known class-related cardiotoxicity risk, particularly in combination regimens |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (All safety fields — key warnings, contraindications, and drug-drug interactions — are currently unavailable in this Evidence Pack; TFDA/label data acquisition is flagged as a **Blocking** data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (missing TFDA label warnings/contraindications) prevents this candidate from entering preliminary safety evaluation (S1), and the mechanism-of-action data needed to assess biological plausibility is also missing. Additionally, the clinical trial evidence most closely associated with this specific prediction shows a notable population mismatch (several key trials enrolled PR/ER-**negative**, not PR-**positive**, patients), and the "new" indication may substantially overlap with pertuzumab's already-established use in HER2-positive breast cancer rather than represent a distinct repurposing opportunity.

**To proceed, the following is needed:**
- TFDA package insert / label data (warnings, contraindications) to complete S1 safety evaluation
- Confirmed mechanism of action from DrugBank or manufacturer labeling
- Manual re-triage of clinical trial and literature relevance flags (majority currently marked "pending") to separate PR-positive-specific evidence from general HER2-positive breast cancer evidence
- Clarification of whether this predicted indication represents a genuinely novel use versus a biomarker subgroup already covered by pertuzumab's existing approved indication
- Norway/EU regulatory status confirmation, since the drug currently has zero local authorizations on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

