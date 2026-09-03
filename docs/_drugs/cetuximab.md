---
layout: default
title: Cetuximab
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Cetuximab
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

# Cetuximab: From Anti-EGFR Oncology Therapy to Bronchial Adenomas/Carcinoids, Childhood

## One-Sentence Summary

> Cetuximab is an anti-EGFR chimeric monoclonal antibody; this evidence pack does not contain a Taiwan-approved indication text or formal MOA record (both flagged as data gaps), but the embedded trial/literature background consistently identifies it as an established therapy for EGFR-overexpressing head and neck squamous cell carcinoma (HNSCC) and metastatic colorectal cancer (mCRC).
> The TxGNN model's top-ranked prediction is **Bronchial Adenomas/Carcinoids, Childhood**, but this candidate is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction (L5).
> Two other candidates further down the ranked list (**Cystic Neoplasm** and **Pre-malignant Neoplasm**) have meaningfully stronger evidence (L2, Research Question stage) and are summarized separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in Taiwan regulatory data (no local market license on file). Internationally, cetuximab is an established anti-EGFR therapy for HNSCC and RAS/BRAF wild-type mCRC, as referenced throughout the embedded trial/literature background of this pack. |
| Predicted New Indication | Bronchial Adenomas/Carcinoids, Childhood |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data for cetuximab is not available in this evidence pack (data gap DG002). Based on the background context embedded across the trial and literature evidence in this pack, cetuximab is known to be a chimeric IgG1 monoclonal antibody that blocks the epidermal growth factor receptor (EGFR), and its efficacy has been established in EGFR-overexpressing tumors — chiefly HNSCC and mCRC — through decades of trials referenced throughout this dataset (e.g., NCT00265941, NCT01302834, NCT00056030).

For the top-ranked candidate specifically, the model's own rationale is explicit that the mechanistic link is **weak**: bronchial adenomas/carcinoids of childhood are neuroendocrine tumors, not a typical EGFR-driven malignancy, and the pediatric population lacks any cetuximab safety data. In other words, this is the case where a high TxGNN similarity score does not correspond to a plausible biological mechanism — the prediction should be treated as hypothesis-generating only, not as a candidate for further development at this time.

By contrast, further down the ranked list, two candidates show a much more coherent mechanistic story consistent with cetuximab's known EGFR-blockade action: **adenoid cystic carcinoma** (within the "cystic neoplasm" category) and **chemoprevention of EGFR-overexpressing pre-malignant upper aerodigestive lesions** (within "pre-malignant neoplasm"). These are discussed in the overview section below.

---

## Clinical Trial Evidence (Top-Ranked Candidate: Bronchial Adenomas/Carcinoids, Childhood)

Currently no related clinical trials registered.

---

## Literature Evidence (Top-Ranked Candidate: Bronchial Adenomas/Carcinoids, Childhood)

Currently no related literature available.

---

## Taiwan Market Information

No Taiwan market authorizations are on file for cetuximab in this evidence pack (`total_licenses = 0`, `market_status = 未上市`).

---

## Other Predicted Indications in This Evidence Pack

This evidence pack contains 10 TxGNN-predicted indications for cetuximab, ranging from L5 (no supporting evidence) to L2 (Phase II trial + review-level literature support). For completeness and to avoid burying stronger signals, all 10 are summarized below.

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Trials | Literature |
|------|---------|------|------|------|------|------|------|
| 1 | Bronchial adenomas/carcinoids, childhood | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 2 | Non-seminomatous lesion | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 3 | Ductal or ductular proliferation | 99.95% | L4 | S0 | Hold | 0 | 20 |
| 4 | Chondroid hamartoma | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 5 | Tumor of testis and paratestis | 99.95% | L5 | S0 | Hold | 0 | 0 |
| 6 | Odontogenic cyst | 99.95% | L4 | S0 | Hold | 0 | 2 |
| 7 | Thyroglossal duct cyst | 99.95% | L5 | S0 | Hold | 0 | 0 |
| **8** | **Cystic neoplasm** | 99.95% | **L2** | **S2** | **Research Question** | **5** | **20** |
| 9 | Epiglottis neoplasm | 99.95% | L5 | S1 | Research Question | 0 | 0 |
| **10** | **Pre-malignant neoplasm** | 99.95% | **L2** | **S2** | **Research Question** | **~50** | **2** |

### Notable candidate — Cystic Neoplasm (Rank 8)

The strongest single piece of evidence in this pack is a directly matched Phase I/II trial for adenoid cystic carcinoma (a "cystic neoplasm" subtype):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Phase 1/2 | Unknown | 49 | ACCEPT trial: cetuximab + IMRT + carbon-ion boost for adenoid cystic carcinoma; graded "A" relevance in the source evidence pack |

Supporting literature (RCT/prospective evidence prioritized):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Phase II prospective trial | Oral Oncology | Cetuximab monotherapy in recurrent/metastatic salivary gland carcinomas (23 adenoid cystic carcinoma patients); clinical benefit rate reported |
| [18366287](https://pubmed.ncbi.nlm.nih.gov/18366287/) | 2008 | Review | Expert Rev Anticancer Ther | Systemic therapy options, including anti-EGFR agents, for recurrent/metastatic salivary gland cancers |
| [22144378](https://pubmed.ncbi.nlm.nih.gov/22144378/) | 2013 | Case report | Head & Neck | Metastatic adenoid cystic carcinoma responding to cetuximab + weekly paclitaxel after paclitaxel-alone failure |

### Notable candidate — Pre-malignant Neoplasm (Rank 10)

A dedicated single-agent Phase II trial exists in high-risk pre-malignant upper aerodigestive lesions, plus a review directly addressing EGFR-targeted chemoprevention:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Phase 2 | Completed | 35 | Single-agent cetuximab in high-risk pre-malignant upper aerodigestive lesions |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Review | Oral Oncology | EGFR is overexpressed in oral pre-malignant lesions; discusses EGFR-targeted chemoprevention rationale for HNSCC |

**Important caveat:** as the source rationale notes, the majority of the ~50 trials tagged to this candidate (e.g., NCT00956007, NCT05959356, NCT00056030) actually enrolled patients with **already-diagnosed** HNSCC/CRC rather than true pre-malignant lesions. Only NCT00524017 is a genuine chemoprevention trial. This distinction matters because treatment-population risk/benefit does not transfer directly to a chemoprevention setting.

---

## Cytotoxicity

Cetuximab is an antineoplastic agent (anti-EGFR monoclonal antibody used in HNSCC/mCRC per the embedded trial background), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR chimeric IgG1 monoclonal antibody) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Not quantified in this evidence pack; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not quantified in this evidence pack; please refer to the package insert warnings and precautions |
| Monitoring Items | Infusion-related reactions/hypersensitivity (referenced in NCT00896896 "Immunoreactivity to Cetuximab in Cancer Patients," n=538, and PMID 39415301 severe infusion reaction case report); skin toxicity (referenced in PMID 30141310, skin disorders as a prognostic factor in mCRC) |
| Handling Protection | Not specified in this evidence pack (TFDA label data is a blocking data gap, DG001); please refer to the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack (DG001, blocking severity), and no DDI records were found (`query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (bronchial adenomas/carcinoids, childhood) has zero supporting clinical trials or literature and is explicitly flagged by the model's own rationale as mechanistically implausible (non-EGFR-driven neuroendocrine tumor, no pediatric safety data). This candidate does not meet the bar for further evaluation at this time.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain TFDA label warnings/contraindications before any S1 safety screening can occur
- Resolve DG002 (high): obtain formal DrugBank MOA record to properly evaluate mechanistic plausibility across all 10 candidates
- If pursuing repurposing work on this drug, redirect attention to the two evidence-backed candidates identified in this pack — **Cystic Neoplasm** (adenoid cystic carcinoma, L2/Research Question, Phase I/II trial + Phase II prospective literature) and **Pre-malignant Neoplasm** (EGFR chemoprevention, L2/Research Question, dedicated Phase II trial) — rather than the top-ranked but evidence-free candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

