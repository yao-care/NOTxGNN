---
layout: default
title: Neratinib
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 4
---

# Neratinib
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

# Neratinib: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

> Neratinib is an irreversible pan-HER (EGFR/HER1, HER2, HER4) tyrosine kinase inhibitor whose established use — per the pivotal ExteNET Phase 3 trial and other trials contained in this evidence pack — is HER2-positive breast cancer; note that the drug's "original indication" field is itself flagged as a data gap in this registry and needs manual verification.
> The TxGNN model predicts it may also be effective for **progesterone-receptor (PR) positive breast cancer**,
> with **5 clinical trials** and **10 publications** currently supporting this direction, though the evidence base remains at an early stage (L2).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this registry (`original_indications` empty, `market_status` = 未上市/Not Marketed) — a flagged data gap; literature in this pack indicates the drug's established use is HER2-positive breast cancer |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Neratinib is an irreversible pan-HER tyrosine kinase inhibitor that blocks signaling through EGFR/HER1, HER2, and HER4. Clinically it is best established in HER2-positive breast cancer, where it has demonstrated benefit both as extended adjuvant therapy after trastuzumab (ExteNET, PMID 26874901) and in combination regimens for metastatic disease. PR status itself is not neratinib's direct molecular target, but PR-positive disease frequently co-occurs with HER2 positivity (the "triple-positive," HR+/HER2+ subgroup), and there is a clear pharmacological rationale for combining neratinib with endocrine therapy (e.g., fulvestrant, aromatase inhibitors) in this population — HER2 pathway activation is a recognized mechanism of endocrine resistance, and blocking it with neratinib is intended to restore endocrine sensitivity.

Several trials in this evidence pack directly test this combination strategy in HR+/HER2+ disease (e.g., NCT04886531: neoadjuvant neratinib + aromatase inhibitor + trastuzumab in ER+/HER2+ cancer), supporting the biological plausibility of the TxGNN prediction.

**Important caveat flagged in the underlying data:** this evidence pack records `original_indications` as empty and Norway `market_status` as "Not Marketed" with 0 authorizations, which is inconsistent with neratinib's known regulatory history (e.g., FDA-approved as Nerlynx for HER2+ breast cancer). This discrepancy is explicitly noted by the analysis pipeline itself and should be manually verified against the source database before this candidate advances further.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04901299](https://clinicaltrials.gov/study/NCT04901299) | Phase 2 | Withdrawn | 0 | Planned to evaluate neratinib + fulvestrant in previously treated HR+/HER2-negative metastatic breast cancer; withdrawn before enrollment, no data generated |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Pre-operative neratinib + aromatase inhibitor + trastuzumab in ER-positive, HER2-positive breast cancer; results pending |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A (retrospective) | Completed | 1,151 | Multicenter retrospective study of HER2-low prevalence, characteristics, and treatment patterns in HER2-negative metastatic breast cancer; not an interventional efficacy study |
| [NCT04460430](https://clinicaltrials.gov/study/NCT04460430) | Phase 2 | Terminated | 12 | Neratinib targeting EGFR/ERBB2 in HR-positive/HER2-negative, HER2-enriched advanced/metastatic breast cancer; terminated early with limited enrollment |
| [NCT05599334](https://clinicaltrials.gov/study/NCT05599334) | N/A (retrospective) | Completed | 111 | Retrospective observational study of neratinib as extended adjuvant therapy in early-stage HER2-positive breast cancer under the European Early Access Program; descriptive data only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncology | ExteNET: Phase 3 RCT showing 12 months of neratinib after trastuzumab-based adjuvant therapy improves outcomes in early-stage HER2-positive breast cancer |
| [27406346](https://pubmed.ncbi.nlm.nih.gov/27406346/) | 2016 | RCT | New England Journal of Medicine | I-SPY 2 adaptive Phase 2 trial evaluating neratinib among other novel agents added to neoadjuvant chemotherapy in high-risk breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2-positive breast cancer |
| [29784737](https://pubmed.ncbi.nlm.nih.gov/29784737/) | 2018 | Review | JNCCN | NCCN guideline update on breast cancer, covering endocrine and HER2-directed treatment algorithms |
| [32139271](https://pubmed.ncbi.nlm.nih.gov/32139271/) | 2020 | Review | Clinical Breast Cancer | Expert roundtable on HER2-positive breast cancer treatment developments, including neratinib and lapatinib |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Review | Future Oncology | Current treatment trends in HR-positive/HER2-positive breast cancer, discussing neratinib-based combinations |
| [24892840](https://pubmed.ncbi.nlm.nih.gov/24892840/) | 2013 | Review | Clin Adv Hematol Oncol | Overview integrating recent metastatic breast cancer data by receptor subtype |
| [39153126](https://pubmed.ncbi.nlm.nih.gov/39153126/) | 2024 | Cohort | Breast Cancer Res Treat | Real-world patterns of adjuvant neratinib use and tolerability in HR+/HER2+ early-stage breast cancer; notes significant GI toxicity driving discontinuation |
| [32782013](https://pubmed.ncbi.nlm.nih.gov/32782013/) | 2020 | Cohort | Breast Cancer Research | In silico analysis of ERBB2 mutation status as a prognostic/targetable marker in ER-positive, ERBB2 non-amplified lobular breast cancer |
| [35251981](https://pubmed.ncbi.nlm.nih.gov/35251981/) | 2022 | Case Series | Frontiers in Oncology | Case report/literature review of durable response with pyrotinib + vinorelbine in HER2-positive breast cancer with leptomeningeal disease (indirect relevance) |

---

## Norway Market Information

Neratinib is not currently marketed in Norway — the evidence pack lists 0 product authorizations, so no license table can be produced.

---

## Cytotoxicity

Neratinib is an antineoplastic agent (targeted small-molecule kinase inhibitor used in breast cancer), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — irreversible pan-HER (EGFR/HER2/HER4) tyrosine kinase inhibitor; not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Not directly reported in this evidence pack; real-world literature (PMID 39153126) indicates the dominant treatment-limiting toxicity is gastrointestinal (diarrhea) rather than myelosuppression — formal hematologic toxicity data should be confirmed via the package insert |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function tests; close monitoring and proactive management of diarrhea/GI toxicity (per literature); CBC as standard oncology monitoring |
| Handling Protection | Please refer to the package insert warnings and precautions; oral formulation — institutional cytotoxic/hazardous drug handling protocols should be confirmed locally |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The PR-positive breast cancer prediction is biologically plausible given neratinib's established mechanism in HER2-driven, hormone receptor-positive disease, and is supported by ongoing/completed Phase 1–2 trials plus a strong precedent from the Phase 3 ExteNET trial in the broader HER2-positive population (L2 evidence). However, two blocking-level data gaps prevent a full go decision at this time.

**To proceed, the following is needed:**
- Resolve the TFDA/local product label safety data gap (warnings, contraindications) — currently blocking any S1 safety evaluation
- Confirm mechanism of action (MOA) directly via DrugBank rather than relying solely on trial-derived rationale
- Manually verify the discrepancy between this dataset's "not marketed / no original indication" status and neratinib's known regulatory history (e.g., FDA approval as Nerlynx) before relying on this evidence pack for downstream decisions
- Obtain results from the ongoing PR+/HR+-specific trial (NCT04886531) once available, since current PR+-specific trial evidence has no completed readouts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

