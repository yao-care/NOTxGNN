---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Tubular Adenocarcinoma

## One-Sentence Summary

Capecitabine (Xeloda) is an oral fluoropyrimidine prodrug established globally as standard-of-care for colorectal and breast cancer, but currently without marketing authorization in this jurisdiction.
The TxGNN model identifies it as a strong candidate (score 99.94%) for **Gastric Tubular Adenocarcinoma** — the most common histological subtype of gastric cancer and the first predicted indication with actionable clinical evidence.
This direction is supported by **20 publications**, including at least 8 completed Phase 3 RCTs demonstrating that capecitabine-based CAPOX regimens are active and guideline-endorsed in gastric adenocarcinoma internationally.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer; breast cancer (globally approved; no locally registered indication) |
| Predicted New Indication | Gastric Tubular Adenocarcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Capecitabine is an oral prodrug selectively converted to 5-fluorouracil (5-FU) within tumor tissue by thymidine phosphorylase (TP), an enzyme overexpressed in many solid carcinomas. The resulting 5-FU inhibits thymidylate synthase (TS), blocking de novo synthesis of thymidine monophosphate (dTMP) and halting DNA replication in rapidly proliferating cancer cells. This tumor-selective activation mechanism explains both capecitabine's preferential efficacy in TP-rich solid tumors and its characteristic toxicity profile (e.g., hand-foot syndrome).

Gastric tubular adenocarcinoma is the predominant histological subtype of gastric cancer and exhibits high TP expression, making it biologically well-suited for capecitabine activation. In clinical practice, CAPOX (capecitabine + oxaliplatin) has become a standard chemotherapy backbone for gastric cancer internationally. The landmark CLASSIC trial (Lancet 2012) demonstrated that adjuvant CAPOX after D2 gastrectomy significantly improved disease-free survival in Stage II–IIIB gastric cancer, while the GLOW and SPOTLIGHT Phase 3 trials subsequently established CAPOX as the standard backbone against which newer targeted agents are evaluated.

The mechanistic link between colorectal cancer (capecitabine's primary approved indication) and gastric tubular adenocarcinoma is compelling: both are gastrointestinal epithelial tumors sharing similar oncogenic features — Wnt/β-catenin activation, TP53 alterations, EGFR signaling, and equivalent sensitivity to fluoropyrimidine-platinum combination chemotherapy. Multiple recent Phase 3 trials across diverse combination partners (checkpoint inhibitors, anti-CLDN18.2 antibodies) have uniformly validated CAPOX as an effective and reproducible chemotherapy platform in gastric adenocarcinoma, providing strong mechanistic and clinical confidence in this TxGNN prediction.

---

## Clinical Trial Evidence

Currently no clinical trials specifically registered under the histological entity "gastric tubular adenocarcinoma." Evidence is derived from broader gastric adenocarcinoma trials in which tubular adenocarcinoma constitutes the majority of enrolled patients (see Literature Evidence below for supporting Phase 3 RCT data).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | Phase 3 RCT | Lancet | CLASSIC trial: adjuvant CAPOX after D2 gastrectomy significantly improved DFS vs surgery alone in Stage II–IIIB gastric cancer |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | Phase 3 RCT | Lancet Oncology | RESOLVE trial: perioperative SOX shown non-inferior to postoperative CapOx after D2 gastrectomy; CapOx confirmed as standard adjuvant reference |
| [39952264](https://pubmed.ncbi.nlm.nih.gov/39952264/) | 2025 | Phase 3 RCT | Lancet Oncology | RESOLVE final report: mature OS data confirming long-term survival benefit of CapOx adjuvant chemotherapy after D2 gastrectomy |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | Phase 3 RCT | Nature Medicine | GLOW trial: zolbetuximab + CAPOX vs placebo + CAPOX in CLDN18.2+/HER2− advanced gastric/GEJ adenocarcinoma; CAPOX confirmed as active first-line backbone |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | Phase 3 RCT | Lancet | CheckMate 649: nivolumab + CAPOX/FOLFOX vs CAPOX/FOLFOX alone in HER2-negative advanced gastric/GEJ/esophageal adenocarcinoma; significant OS improvement |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | Phase 3 RCT | BMJ | RATIONALE-305: tislelizumab + capecitabine-based chemotherapy vs placebo in advanced gastric/GEJ adenocarcinoma; statistically significant OS improvement |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | Phase 3 RCT | JAMA | ORIENT-16: sintilimab + CAPOX vs CAPOX alone in unresectable gastric/GEJ cancer; significant OS benefit confirmed |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | Phase 3 RCT | Lancet Oncology | KEYNOTE-859: pembrolizumab + CAPOX/FP vs placebo + CAPOX/FP in HER2-negative advanced gastric/GEJ adenocarcinoma; OS benefit confirmed |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | Phase 3 RCT | Lancet | FLOT4: FLOT vs ECF/ECX (capecitabine-containing arm) perioperative for resectable gastric/GEJ adenocarcinoma; ECX confirmed as valid active comparator |
| [33610734](https://pubmed.ncbi.nlm.nih.gov/33610734/) | 2021 | Phase 2 RCT | Annals of Oncology | FAST trial: zolbetuximab + EOX vs EOX alone in CLDN18.2+ advanced gastric/GEJ adenocarcinoma; Phase 2 signal that preceded the confirmatory GLOW Phase 3 |

---

## Norway Market Information

No marketing authorizations are currently registered for capecitabine in this jurisdiction.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Fluoropyrimidine class (oral prodrug of 5-FU) |
| Myelosuppression Risk | Moderate — neutropenia and thrombocytopenia reported; generally less pronounced than intravenous 5-FU continuous infusion |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function tests (ALT/AST/bilirubin), serum creatinine and creatinine clearance, DPD enzyme activity (DPYD genotyping strongly recommended prior to initiation) |
| Handling Protection | Must follow cytotoxic drug handling regulations; oral tablet formulation — avoid direct contact with broken or crushed tablets; caregiver protection measures required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs consistently demonstrate that capecitabine-based CAPOX regimens are effective and internationally guideline-recommended for gastric adenocarcinoma — the category encompassing gastric tubular adenocarcinoma as its predominant histotype — providing strong L1-level clinical evidence with a well-established mechanistic basis (TP-selective activation and TS inhibition in gastric tumor tissue).

**To proceed, the following is needed:**
- Obtain local package insert or SPC for complete warnings and contraindications (Data Gap DG001 — currently blocking formal safety evaluation)
- Establish local market authorization pathway: no current registration in this jurisdiction; off-label use or special import approval will be required
- Implement DPYD genotyping / DPD enzyme activity screening before initiating treatment to identify patients at high risk of severe fluoropyrimidine toxicity
- Define patient selection biomarkers: HER2 status (for trastuzumab addition), CLDN18.2 expression (for zolbetuximab consideration), PD-L1 CPS (for checkpoint inhibitor combination eligibility)
- Confirm baseline renal function: dose adjustment required for CrCl 30–50 mL/min; use is contraindicated if CrCl < 30 mL/min
- Review full drug interaction profile before prescribing, with particular attention to anticoagulants (coumarin class) and antiepileptic agents (phenytoin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

