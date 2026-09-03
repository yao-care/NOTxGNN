---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Data-Gap Original Indication to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane, microtubule-stabilizing chemotherapy agent; this evidence pack does not contain the original approved indication text or a marketing authorization for the reviewed jurisdiction (0 licenses on file). The TxGNN model predicts continued/expanded efficacy for **Female Breast Carcinoma**, with **50 clinical trials** and **20 publications** currently supporting this direction — largely reflecting paclitaxel's already well-established role as a breast cancer chemotherapy backbone rather than a novel mechanistic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file (drug not marketed, 0 licenses) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% (rank 82) |
| Evidence Level | L1 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap). Based on the mechanistic evidence provided alongside the prediction, paclitaxel is a **microtubule-stabilizing agent (taxane class)**: it promotes tubulin polymerization and inhibits depolymerization, blocking mitotic spindle function and inducing G2/M-phase arrest and apoptosis.

Breast cancer cells proliferate rapidly and are characteristically sensitive to microtubule-targeting agents. This is an **established**, not exploratory, mechanistic role — paclitaxel (as Taxol® and generics) is already widely used across breast cancer subtypes in combination regimens (e.g., with trastuzumab, lapatinib, anthracyclines, and more recently checkpoint inhibitors). The TxGNN prediction here largely reconfirms a mechanism-of-action relationship that is heavily supported by real-world oncology practice rather than proposing a novel repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003992](https://clinicaltrials.gov/study/NCT00003992) | Phase 2 | Completed | 200 | Paclitaxel + trastuzumab adjuvant therapy for HER2-overexpressing stage II/IIIA breast cancer; foundational trial for taxane–HER2 combination |
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Phase 3 | Completed | 444 | Lapatinib + paclitaxel vs. placebo + paclitaxel in ErbB2-amplified metastatic breast cancer; direct efficacy comparison |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Completed | 2,005 | Sequential doxorubicin/paclitaxel/cyclophosphamide vs. concurrent AC→paclitaxel at different intervals, node-positive stage II/IIIA breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy ± trastuzumab (with weekly paclitaxel backbone) in node-positive/high-risk HER2-low invasive breast cancer |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | Completed | 478 | Dose-dense G-CSF-supported FE75C→docetaxel vs. paclitaxel as adjuvant chemotherapy, axillary node-positive breast cancer |
| [NCT00016276](https://clinicaltrials.gov/study/NCT00016276) | Phase 3 | Terminated | 396 | AC ± dexrazoxane → weekly paclitaxel ± trastuzumab, HER2+ stage IIIA/IIIB/IV breast cancer |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | Completed | 280 | Neoadjuvant FEC-75→paclitaxel+trastuzumab vs. paclitaxel+trastuzumab→FEC-75+trastuzumab, HER2+ operable breast cancer |
| [NCT01901146](https://clinicaltrials.gov/study/NCT01901146) | Phase 3 | Completed | 725 | ABP 980 (trastuzumab biosimilar) vs. trastuzumab, HER2+ early breast cancer |
| [NCT01848197](https://clinicaltrials.gov/study/NCT01848197) | N/A | Unknown | 1,000 | Paclitaxel every 2 weeks vs. weekly, adjuvant treatment of breast cancer — direct dosing-schedule comparison |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Terminated | 63 | Paclitaxel + trastuzumab + lapatinib vs. paclitaxel + trastuzumab + placebo, ErbB2-overexpressing metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, including resistance mechanisms |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review establishing paclitaxel/docetaxel role in breast and ovarian cancer, including licensing extension to metastatic breast carcinoma |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort (Phase II) | Cancer | Doxorubicin + paclitaxel efficacy/toxicity in advanced breast carcinoma, importance of prior adjuvant anthracycline exposure |
| [15305399](https://pubmed.ncbi.nlm.nih.gov/15305399/) | 2004 | RCT (GONO trial) | Cancer | Concomitant vs. sequential epirubicin + paclitaxel as first-line therapy in metastatic breast carcinoma |
| [11751485](https://pubmed.ncbi.nlm.nih.gov/11751485/) | 2001 | Phase II RCT | Clin Cancer Res | Doxorubicin followed by sequential vs. concurrent paclitaxel + cyclophosphamide, dose-dense adjuvant regimen, 5-year results |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | — | Chem Biol Drug Des | Paclitaxel combination therapeutics against breast carcinoma with in vivo biomarker identification |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | — | J Immunother Cancer | Paclitaxel's role on tumor-associated macrophages enhancing PD-1 blockade in triple-negative breast cancer |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Real-world study | BioMed Res Int | Neoadjuvant epirubicin/cyclophosphamide + weekly paclitaxel/trastuzumab efficacy in HER2+ breast carcinoma |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | — | Nature Communications | TEKT4 germline variations enriched in paclitaxel-resistant breast cancer, biomarker for treatment response |
| [17272681](https://pubmed.ncbi.nlm.nih.gov/17272681/) | 2007 | — | Mol Pharmacol | Stathmin-mediated resistance to paclitaxel/vinblastine in breast carcinoma cells and reversal strategies |

---

## Norway Market Information

No marketing authorizations are currently on file for paclitaxel in this jurisdiction (total_licenses = 0; market status: Not Marketed). No product name, dosage form, or approved indication text is available for extraction.

---

## Cytotoxicity

**This section applies — paclitaxel is a conventional cytotoxic antineoplastic agent (taxane class).**

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a conventional cytotoxic agent, standard cytotoxic drug handling and disposal precautions apply |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are marked as Data Gap / not found in this evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety-related decision.)

---

## Other Predicted Indications (Overview)

This evidence pack ranks 10 predicted indications for paclitaxel; most are breast-cancer subtypes that reinforce the same established mechanism rather than independent hypotheses:

- **Ranks 2–4** (ER-negative, hormone-resistant, ER-positive breast cancer): L1–L2 evidence, "Proceed with Guardrails" — supported by large Phase 3 trials (e.g., IMpassion130, RIGHT Choice) but represent molecular subsets of the same disease rather than a new indication.
- **Rank 5** (Ehrlich tumor carcinoma): L4, **Hold** — this is a mouse xenograft tumor model, not a human disease entity; evidence is preclinical only.
- **Ranks 6–8** (bilateral breast carcinoma, gene-expression-profiled breast carcinoma, nipple carcinoma): L2–L4, mostly **Hold** — rare anatomical subtypes or symptom-management trials, not disease-specific efficacy trials.
- **Ranks 9–10** (parameningeal / botryoid embryonal rhabdomyosarcoma): L5, **Hold** — pure TxGNN model output with zero supporting clinical trials or literature.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction (Female Breast Carcinoma) is backed by L1-level evidence — multiple completed Phase 3 RCTs and a near-maximal TxGNN score (99.995%) — confirming paclitaxel's well-established, mechanistically sound role in breast cancer chemotherapy. However, this evidence pack has two unresolved data gaps that block full safety sign-off, and the drug currently has no market authorization on file in this jurisdiction.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official regulatory package insert / label warnings and contraindications
- Resolve DG002 (High): obtain drug MOA data via DrugBank API to complete mechanistic documentation
- Clarify local marketing/import status — confirm whether "Not Marketed" reflects a genuine regulatory gap or a limitation of the source dataset, given paclitaxel is a globally established oncology agent
- If pursuing lower-ranked, non-breast indications (ranks 5–10), treat separately — these require independent, disease-specific evidence generation before any development decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

