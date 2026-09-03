---
layout: default
title: Olaparib
parent: 僅模型預測 (L5)
nav_order: 253
evidence_level: L5
indication_count: 1
---

# Olaparib
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

# Olaparib: From BRCA-Mutated Ovarian Cancer to Breast Carcinoma

## One-Sentence Summary

> Olaparib is a PARP1/2 inhibitor originally developed and approved internationally for BRCA-mutated ovarian cancer maintenance therapy.
> The TxGNN model flags **Female Breast Carcinoma** as a related indication, with **73 clinical trials** and **20 publications** in the evidence pack —
> however, this is very likely an already-established indication (olaparib has been approved for gBRCA-mutated HER2-negative breast cancer since 2018) rather than a genuinely novel repurposing signal. See caveat below.

> ⚠️ **Data quality note**: `drug.original_indications` and `taiwan_regulatory.licenses` are both empty in this Evidence Pack, and `original_moa` is flagged as a data gap (DG002). The repurposing rationale itself flags this as a likely database omission, since olaparib (Lynparza®) is a well-established, globally approved oncology drug. This report is written strictly from the supplied Evidence Pack; external verification against the actual TFDA/Norway label is required before any decision.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Evidence Pack (0 licenses recorded); publicly known original approval: BRCA-mutated, platinum-sensitive relapsed ovarian cancer (maintenance therapy) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no structured MOA field is available for olaparib in this Evidence Pack (DG002, High severity). However, the repurposing rationale supplies the mechanistic basis: olaparib is a **PARP1/2 (poly-ADP-ribose polymerase) inhibitor**. In tumor cells with BRCA1/2 mutations or broader homologous recombination deficiency (HRD), PARP inhibition blocks single-strand DNA damage repair, causing accumulation of double-strand breaks and cell death via **synthetic lethality**. This mechanism has been extensively validated both biologically and clinically in BRCA-mutated tumors.

BRCA1/2 mutations drive both hereditary ovarian cancer and hereditary breast cancer through the same DNA-repair pathway. Since olaparib's synthetic-lethality mechanism is gene-defect–driven rather than tissue-specific, its efficacy readily extends from ovarian to breast cancer in patients sharing the same germline BRCA1/2 mutation — this is not a speculative repurposing hypothesis but a mechanistically expected and clinically confirmed extension.

Importantly, the clinical evidence in this pack (OlympiAD, OlympiA) shows this "predicted" indication is **already an approved, guideline-standard use** of olaparib in gBRCA-mutated HER2-negative breast cancer (both metastatic and high-risk early-stage adjuvant settings) in multiple jurisdictions since 2018–2022. The TxGNN signal here should be interpreted as **evidence confirmation of an existing indication**, not discovery of a novel one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib monotherapy vs. physician's choice single-agent chemotherapy in platinum-sensitive relapsed, gBRCA1/2-mutated ovarian cancer |
| [NCT03162627](https://clinicaltrials.gov/study/NCT03162627) | Phase 1 | Active, not recruiting | 90 | Selumetinib + olaparib in solid tumors (incl. breast) with Ras pathway alterations or PARP resistance |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin + olaparib → olaparib monotherapy vs. capecitabine as first-line therapy in BRCA1/2-mutated HER2-negative advanced breast cancer |
| [NCT03402841](https://clinicaltrials.gov/study/NCT03402841) | Phase 3b | Completed | 279 | Single-arm olaparib maintenance in platinum-sensitive relapsed non-germline BRCA ovarian/endometrioid cancer |
| [NCT02503436](https://clinicaltrials.gov/study/NCT02503436) | N/A (observational) | Completed | 276 | C-PATROL: real-world effectiveness/safety of olaparib in BRCAm+ platinum-sensitive relapsed ovarian cancer |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | AZD2281 (olaparib) in BRCA-mutated/triple-negative breast cancer and recurrent ovarian cancer — response rate and correlative biomarkers |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Phase 2 | Recruiting | 2900 | ComboMATCH biomarker-directed combination therapy platform trial, includes breast cancer cohorts |
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Phase 3 | Active, not recruiting | 185 | ROSY-O rollover study providing continued olaparib treatment post parent-study completion |
| [NCT06545942](https://clinicaltrials.gov/study/NCT06545942) | Phase 1 | Active, not recruiting | 220 | MOMA-313 monotherapy or combined with a PARP inhibitor (olaparib) in advanced/metastatic solid tumors |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Olaparib in Indian patients with platinum-sensitive relapsed ovarian cancer and BRCA1/2-mutated metastatic breast cancer |

*Note: 43 additional trials in the evidence pack are graded "pending" (unreviewed relevance) and are omitted from this table; most are combination/basket trials across multiple solid tumor types rather than breast-cancer-specific.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib shows antitumor activity in metastatic breast cancer with germline BRCA mutation |
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib reduces recurrence in gBRCA1/2-mutated, HER2-negative early breast cancer |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final OS and tolerability: olaparib vs. chemotherapy in gBRCA-mutated HER2-negative mBC |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA phase 3 overall survival results for adjuvant olaparib in high-risk early breast cancer |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD extended follow-up: sustained OS and safety data for olaparib in gBRCAm HER2-negative mBC |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 single-arm | J Clin Oncol | TBCRC 048: olaparib activity in mBC with somatic BRCA1/2 or non-BRCA HR-related gene mutations |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 combination | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel increases pCR in high-risk HER2-negative breast cancer |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Target Oncol | Overview of PARP inhibitors (olaparib, talazoparib) approved for BRCA-mutated HER2-negative breast cancer |
| [35163586](https://pubmed.ncbi.nlm.nih.gov/35163586/) | 2022 | Review | Int J Mol Sci | Molecular mechanisms, biomarkers and emerging therapies for chemotherapy-resistant TNBC |
| [37253112](https://pubmed.ncbi.nlm.nih.gov/37253112/) | 2023 | Translational/Functional | Cancer Res | Functional characterization of RAD51C variants relevant to HR-deficiency and PARP inhibitor sensitivity |

---

## Norway Market Information

No authorization records are present in the Evidence Pack (`total_licenses: 0`, `licenses: []`). Olaparib currently has **no registered marketing authorization in Norway per this data source**. This should be independently verified against the national medicines register before proceeding, since olaparib (Lynparza®) is centrally authorized in the EU/EEA and would ordinarily be expected to appear.

---

## Cytotoxicity

Olaparib is an antineoplastic agent (PARP inhibitor, oncology indication) and this section therefore applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor; synthetic lethality in HR-deficient tumors) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

*Detailed toxicity/monitoring data could not be sourced — this is blocked by DG001 (TFDA label warnings/contraindications not yet retrieved).*

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data are currently available in this Evidence Pack (all fields flagged as data gaps; DDI query returned no results).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clinical evidence is strong (5 Phase 3 RCTs, including two pivotal trials — OlympiAD and OlympiA — directly establishing olaparib's efficacy in gBRCA-mutated breast cancer), justifying Evidence Level L1. However, this appears to represent confirmation of an **already internationally approved indication** rather than a novel repurposing candidate, and critical safety and regulatory data (TFDA/Norway label, MOA, market authorization) are missing from this pack — hence guardrails rather than an unconditional Go.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the actual product label for warnings, contraindications, and DDI data
- Resolve DG002 (High): confirm structured MOA from DrugBank API
- Verify actual Norway/EEA marketing authorization status for olaparib (Lynparza®), since 0 licenses in this pack is inconsistent with its known EU centralized authorization
- Confirm whether "female breast carcinoma" should be reclassified as an existing approved indication rather than a TxGNN-predicted new indication, to avoid mischaracterizing this candidate in downstream reporting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

