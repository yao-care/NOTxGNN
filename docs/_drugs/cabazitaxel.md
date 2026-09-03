---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Castration-Resistant Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a third-generation semisynthetic taxane, originally approved (in combination with prednisone) for metastatic castration-resistant prostate cancer after docetaxel failure. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with currently **0 registered clinical trials in the ClinicalTrials.gov feed** but **20 supporting publications**, including one Phase II RCT and one Phase I/II combination trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic Castration-Resistant Prostate Cancer (mCRPC), per literature evidence (no formal regulatory license data available) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (Data Gap DG002). Based on information contained in the supporting literature, cabazitaxel is a taxane-class microtubule inhibitor structurally related to docetaxel, and it was FDA-approved in 2010 for use in combination with prednisone in taxane-refractory metastatic prostate cancer (TROPIC study). Its efficacy in that original indication has been proven, and mechanistically it may be applicable to breast cancer given the class effect of taxanes.

Taxanes (paclitaxel, docetaxel) are already standard-of-care components of breast cancer chemotherapy, and cabazitaxel was specifically engineered to have low affinity for the P-glycoprotein efflux pump, giving it activity against taxane/anthracycline-resistant tumor cell lines — including resistant MCF-7 breast cancer models described in the literature. This resistance-overcoming profile is the key pharmacological rationale connecting the original prostate cancer indication to the predicted breast cancer indication: both are settings where taxane-refractory disease is a major clinical problem.

The supporting evidence base spans a spectrum from an early-phase clinical combination trial and a randomized Phase II neoadjuvant trial in HER2-negative/triple-negative breast cancer, through pharmacology reviews on resistance mechanisms and dosing, to multiple preclinical nanoparticle-delivery studies aimed at improving cabazitaxel's poor solubility for breast tumor targeting — indicating active, ongoing translational interest in this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

*(Note: two literature-indexed clinical studies exist — a Phase II RCT and a Phase I/II dose-escalation trial — see Literature Evidence below, as they were not captured in the structured clinical_trials registry field.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | RCT (Phase II) | European Journal of Cancer | GENEVIEVE trial: neoadjuvant cabazitaxel vs weekly paclitaxel compared, evaluating pathological complete response in operable TNBC/luminal B HER2-negative breast cancer |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II Clinical Trial | European Journal of Cancer | Dose-escalation study of cabazitaxel + capecitabine in metastatic breast cancer after prior anthracycline/taxane; established MTD, safety, PK, and antitumor activity |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | British Journal of Clinical Pharmacology | Overview of taxane pharmacology (incl. cabazitaxel) and role of therapeutic drug monitoring-based dose adjustment |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review | Molecular Cancer Therapeutics | Mechanisms of cabazitaxel resistance in taxane-resistant models, including MCF-7 breast cancer cells; less cross-resistance vs paclitaxel/docetaxel |
| [26651178](https://pubmed.ncbi.nlm.nih.gov/26651178/) | 2016 | Review | Expert Opinion on Therapeutic Patents | Patent perspective on taxane anticancer agents, including cabazitaxel's FDA approval history |
| [30521787](https://pubmed.ncbi.nlm.nih.gov/30521787/) | 2019 | Preclinical | Chemistry and Physics of Lipids | Cabazitaxel + thymoquinone co-loaded lipospheres as a synergistic combination for breast cancer |
| [33360926](https://pubmed.ncbi.nlm.nih.gov/33360926/) | 2021 | Preclinical | Colloids and Surfaces B: Biointerfaces | Cabazitaxel-loaded nanostructured lipid carriers (NLCs) designed and evaluated against breast cancer cell lines |
| [34309357](https://pubmed.ncbi.nlm.nih.gov/34309357/) | 2021 | Preclinical | Bioconjugate Chemistry | Cyclic cell-penetrating peptide-targeted cabazitaxel delivery for prostate and breast cancer therapy |
| [36918084](https://pubmed.ncbi.nlm.nih.gov/36918084/) | 2023 | Preclinical | Journal of Controlled Release | Redox-responsive nanomedicine co-delivering cabazitaxel and dasatinib to modulate tumor-stromal crosstalk in breast cancer |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical | Journal for ImmunoTherapy of Cancer | Cabazitaxel modulates tumor-associated macrophages to enhance CD47-targeted immunotherapy in triple-negative breast cancer |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia is reported as the most common dose-limiting toxicity across taxane class studies, alongside peripheral neuropathy |
| Emetogenicity Classification | Low to moderate (typical of taxane-class agents) |
| Monitoring Items | CBC with differential (neutrophil count especially), liver function, peripheral neuropathy assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations (hazardous drug precautions during preparation and administration) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One Phase II RCT (GENEVIEVE) and one Phase I/II combination trial provide direct clinical signal for cabazitaxel in breast cancer, reinforced by resistance-mechanism and pharmacology reviews plus an active stream of preclinical delivery-optimization research. However, cabazitaxel-specific breast cancer evidence remains limited to early/mid-phase trials (L2), and the drug is not currently marketed in Norway.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) documentation from DrugBank or regulatory source
- TFDA/Norwegian regulatory labeling, warnings, and contraindications (currently Data Gap, Blocking severity)
- Drug-drug interaction data
- Confirmation of whether more recent/later-phase cabazitaxel breast cancer trials exist beyond the identified Phase I/II and Phase II studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

