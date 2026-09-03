---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 10
---

# Topotecan
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

# Topotecan: From Ovarian/Cervical/Small Cell Lung Cancer to Breast Carcinoma

## One-Sentence Summary

> Topotecan is a topoisomerase I inhibitor currently approved for ovarian cancer, cervical cancer, and small cell lung cancer.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
> with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Norway; internationally approved for ovarian cancer, cervical cancer, and small cell lung cancer (per evidence pack) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Topotecan is a topoisomerase I inhibitor. It stabilizes the Top1‑DNA cleavage complex, producing single‑strand DNA breaks that convert into lethal double‑strand breaks during S‑phase replication, driving apoptosis in rapidly proliferating cells. This cytotoxic mechanism confers broad antitumor activity that is plausibly applicable to breast cancer cells — particularly the highly proliferative triple‑negative breast cancer (TNBC) subtype, which is supported by preclinical work in the evidence pack (e.g., TFDP1/topotecan target studies).

Breast carcinoma is **not** among topotecan's currently approved indications (approved uses are ovarian cancer, cervical cancer, and small cell lung cancer). The clinical trial and literature record shown here — spanning from 1997 phase II trials to 2025 preclinical mechanistic studies — indicates this is a **long-standing off-label use pattern** rather than a genuinely novel repurposing hypothesis. One high-grade trial (NCT02282020, Phase 3, n=266) was flagged by the evidence pipeline as having a truncated title that requires manual verification, as its summary describes an olaparib-vs-chemotherapy trial in gBRCA-mutated **ovarian** cancer rather than breast cancer specifically.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's choice chemotherapy in platinum-sensitive relapsed gBRCA-mutated ovarian cancer — highest-grade evidence in the pack, but population needs verification (title truncated; likely ovarian, not breast, cancer cohort) |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | TIME regimen (topotecan + ifosfamide/mesna + etoposide) followed by autologous stem cell rescue in metastatic breast cancer |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib (topotecan-containing arm) vs. standard chemo in platinum-resistant recurrent ovarian/peritoneal/fallopian cancer |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with standard chemotherapy/immunotherapy regimens in advanced malignancies; safety-focused, limited direct relevance |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown | 35 | Patient-derived organoid high-throughput drug screening assay for refractory solid tumors; preclinical drug-sensitivity platform, not a treatment efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II Trial | American Journal of Clinical Oncology | CALGB phase II trial of topotecan in advanced breast cancer previously treated with one chemotherapy line |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot/Cohort | Onkologie | Topotecan as primary chemotherapy for breast cancer brain metastases |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Cohort/Clinical Study | British Journal of Cancer | Continuous infusional topotecan in advanced breast cancer and NSCLC; no evidence of increased efficacy vs. standard dosing |
| [21514634](https://pubmed.ncbi.nlm.nih.gov/21514634/) | 2011 | RCT (Phase 2) | Gynecologic Oncology | Lapatinib + topotecan overcomes BCRP/P-gp-mediated resistance in platinum-refractory ovarian/peritoneal carcinoma — mechanistically relevant to breast cancer resistance protein biology |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynäkologisch-geburtshilfliche Rundschau | Review of new cytotoxic agents (including topotecan) in breast carcinoma therapy |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical | International Journal of Biological Macromolecules | TFDP1 identified as a therapeutic target for topotecan in triple-negative breast cancer |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical/Mechanistic | Cancer Research | Topoisomerase I inhibition promotes synthetic lethality in MYC-driven breast cancer via R-loop accumulation |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic topotecan + pazopanib shows potent efficacy in TNBC preclinical models |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical | Pharmacological Research | Daidzein enhances topotecan anticancer effect and reverses BCRP-mediated drug resistance in breast cancer |
| [39657238](https://pubmed.ncbi.nlm.nih.gov/39657238/) | 2024 | Preclinical | ACS Applied Materials & Interfaces | Biomimetic topotecan-gene nanoparticles for combination therapy of metastatic breast cancer |

---

## Norway Market Information

Topotecan currently holds **no marketing authorizations in Norway** (0 licenses on record; market status: not marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Topoisomerase I inhibitor, camptothecin derivative) |
| Myelosuppression Risk | High — dose-limiting neutropenia and thrombocytopenia are consistently reported as the principal toxicities across trials in the evidence pack (e.g., cisplatin-refractory germ cell tumor trial, PMID 8617580) |
| Emetogenicity Classification | Low to Moderate (typical for topoisomerase I inhibitor class) |
| Monitoring Items | CBC with differential (neutrophil/platelet nadir), renal function (renally cleared), liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations (hazardous drug precautions during preparation and administration) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence level is L1 based on trial count, but the highest-grade trial (NCT02282020, Phase 3) has an unverified patient population, and the overall clinical/literature record shows breast carcinoma use is a long-standing off-label pattern rather than a novel, high-confidence hypothesis — warranting cautious progression rather than a full "Go."

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (currently a Blocking data gap; safety evaluation cannot proceed without this)
- Confirmed drug mechanism-of-action documentation from DrugBank (High-severity gap affecting mechanistic-relevance analysis)
- Manual verification of NCT02282020's actual patient population (title suggests ovarian, not breast, cancer)
- Clarification of Norway market/regulatory pathway, since topotecan is currently not marketed there
- Prioritized, disease-specific literature curation to separate breast-cancer-relevant records from the broader topotecan literature set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

