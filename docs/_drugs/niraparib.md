---
layout: default
title: Niraparib
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Niraparib
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

# Niraparib: From Ovarian Cancer to Cystic Neoplasm

## One-Sentence Summary

Niraparib is an oral PARP1/2 inhibitor already used internationally as maintenance therapy for platinum-sensitive ovarian, fallopian tube, and primary peritoneal cancer. Within this evidence pack, the TxGNN model's highest-scored candidate with actual supporting data predicts benefit in **Cystic Neoplasm** — a label that, in the retrieved trials and literature, corresponds almost entirely to high-grade serous ovarian carcinoma and uterine/endometrial serous carcinoma — supported by **3 clinical trials** and **9 publications**. However, none of the identified trials have yet produced mature efficacy results (one withdrawn, one terminated early with only 11 patients, one still recruiting), so this remains an early, unconfirmed signal (Evidence Level L2) rather than a validated new indication.

> **Note on TxGNN ranking:** The single highest-scoring prediction overall in this dataset ("epiglottis neoplasm", score 99.99%) has **zero** supporting clinical trials or literature and is mechanistically implausible for a PARP inhibitor. This report therefore focuses on the highest-scored prediction that is actually supported by evidence. Eight of the ten predicted indications in this pack (epiglottis neoplasm, benign neoplasm of hypopharynx/tongue/floor of mouth, cervical neuroblastoma, tumor of testis and paratestis, inner ear neoplasm, schwannoma of jugular foramen) have no clinical trial or literature support and remain at Evidence Level L5 with a "Hold" status.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian, fallopian tube, and primary peritoneal cancer — maintenance treatment after response to platinum-based chemotherapy (derived from trial/literature descriptions in this pack; no Norway license record exists) |
| Predicted New Indication | Cystic Neoplasm (evidence maps to high-grade serous ovarian carcinoma / uterine serous carcinoma) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a High-severity data gap, DG002). Based on information embedded elsewhere in this evidence pack, niraparib is a PARP1/2 (poly ADP-ribose polymerase) inhibitor that acts through a synthetic lethality mechanism, producing selective cytotoxicity in tumours with homologous recombination deficiency (HRD) — including BRCA1/2-mutated cancers. This mechanism is already the basis of niraparib's established use in ovarian, fallopian tube, and primary peritoneal cancer maintenance therapy.

The predicted new indication "Cystic Neoplasm" is a broad label, but the trials and publications actually retrieved under it are overwhelmingly about **high-grade serous ovarian carcinoma (HGSOC)** and **uterine/endometrial serous carcinoma (ESC/USC)** — diseases that frequently present as cystic adnexal masses. Literature in this pack explicitly notes that ESC "has similar molecular characteristics to high-grade serous ovarian carcinoma... such as similar chromosomal instability, somatic copy number variation profiles and somatic mutations," and that ESC treatment protocols already borrow from HGSOC management. Approximately half of HGSOC cases carry HRD, the population in which niraparib and other PARP inhibitors show the strongest activity.

Mechanistically, this makes the prediction reasonable: the new candidate indication is not a novel biological hypothesis but largely an extension of niraparib's already-validated HRD-targeting activity into a molecularly similar, cystic-presenting gynecologic tumour type. The main gap is not mechanism but **maturity of clinical evidence** specifically for this label — the trials identified are early-phase, underpowered, or still recruiting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04716686](https://clinicaltrials.gov/study/NCT04716686) | Phase 2 | Recruiting | 83 | Niraparib monotherapy as maintenance/recurrent treatment for endometrial serous carcinoma; rationale based on molecular overlap between ESC and HGSOC. No mature efficacy data yet reported. |
| [NCT04159155](https://clinicaltrials.gov/study/NCT04159155) | Phase 2/3 | Terminated | 11 | Canadian umbrella trial assessing front-line/maintenance treatment (including niraparib-relevant arms) in serous or p53-mutant endometrial cancer; terminated with only 11 of planned participants enrolled — reason for termination (safety vs. operational) not specified in this pack. |
| [NCT05289648](https://clinicaltrials.gov/study/NCT05289648) | Early Phase 1 | Withdrawn | 0 | Preoperative niraparib window-of-opportunity study in high-grade endometrial cancer; withdrawn before enrollment, no data generated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40473279](https://pubmed.ncbi.nlm.nih.gov/40473279/) | 2025 | Phase II protocol / clinical study | BMJ Open | Study protocol for a Phase II trial of maintenance niraparib in stage III/IV or recurrent uterine serous carcinoma, a disease with poor 2–5 year survival where new maintenance options are needed. |
| [31851805](https://pubmed.ncbi.nlm.nih.gov/31851805/) | 2019 | Review | New England Journal of Medicine | Overview of personalized, biomarker-driven primary treatment strategies (including PARP inhibitors) in serous ovarian cancer. |
| [41323499](https://pubmed.ncbi.nlm.nih.gov/41323499/) | 2025 | Review/Guideline | Pathology Oncology Research | Evaluates comprehensive genomic profiling (F1CDx) for HRD detection to guide PARP inhibitor therapy decisions in ovarian cancer. |
| [41520277](https://pubmed.ncbi.nlm.nih.gov/41520277/) | 2026 | Preclinical (organoid/spheroid) | Cancer Biology & Therapy | Evaluates carboplatin + PARP inhibitor combinations in HGSOC organoid/spheroid models; notes niraparib is approved for platinum-sensitive recurrent disease and is being explored front-line and in combination. |
| [40702505](https://pubmed.ncbi.nlm.nih.gov/40702505/) | 2025 | Retrospective/Bioinformatics | Journal of Ovarian Research | Identifies cancer stem cell-based HGSOC subtypes and a prognostic model, with implications for treatment stratification. |
| [41214101](https://pubmed.ncbi.nlm.nih.gov/41214101/) | 2025 | Mechanistic/Basic Science | Scientific Reports | Describes Claudin-4 as a regulator of genomic instability and immune evasion in HGSOC, relevant to PARP-inhibitor-responsive biology. |
| [34321239](https://pubmed.ncbi.nlm.nih.gov/34321239/) | 2021 | Mechanistic/Translational | Cancer Research | Shows acquired RAD51C promoter methylation loss drives PARP inhibitor resistance in HGSOC PDX models — relevant to resistance mechanisms. |
| [41465250](https://pubmed.ncbi.nlm.nih.gov/41465250/) | 2025 | Mechanistic/Proteomic | International Journal of Molecular Sciences | Proteomic profiling of poly-pharmacological effects of PARP inhibitors (olaparib, niraparib, rucaparib) in HGSOC cells, relevant to adverse effect mechanisms. |
| [31466953](https://pubmed.ncbi.nlm.nih.gov/31466953/) | 2019 | Case Report | BMJ Case Reports | Case of niraparib maintenance therapy in an ovarian cancer patient with brain metastases. |

---

## Norway Market Information

Niraparib is **not currently marketed in Norway** — the evidence pack records 0 authorizations, so no product name, dosage form, or approved-indication text is available for extraction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — PARP1/2 inhibitor acting via synthetic lethality in HRD-deficient tumours |
| Myelosuppression Risk | High — PARP inhibitors as a class carry genotoxic potential, with a recognized risk of secondary myeloid neoplasms (treatment-related MDS/AML); no product-specific haematology data is available in this evidence pack |
| Emetogenicity Classification | Low-to-moderate (typical for oral PARP inhibitors) |
| Monitoring Items | Complete blood count with differential (frequent monitoring during early treatment), blood pressure, renal and hepatic function |
| Handling Protection | Oral small-molecule antineoplastic agent; standard cytotoxic/antineoplastic handling precautions are advisable pending confirmation from an official Norway package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all flagged as data gaps in this evidence pack, and this is classified as a Blocking-severity gap that prevents a formal S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Niraparib's core PARP-inhibitor mechanism is well established in HRD-driven serous gynecologic cancers, and the "Cystic Neoplasm" prediction is biologically coherent with its known activity in ovarian and endometrial serous carcinoma. However, none of the three supporting trials has produced completed, mature efficacy data (withdrawn, terminated at n=11, or still recruiting), the drug has no market authorization in Norway, and a Blocking-severity data gap (missing package insert warnings/contraindications) prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- Official package insert / warnings & contraindications data to resolve the Blocking data gap (DG001) and enable an S1 safety pre-assessment
- Confirmed mechanism-of-action documentation via DrugBank API (DG002)
- Maturation of NCT04716686 (Phase 2, recruiting, expected completion December 2026) and clarification of why NCT04159155 was terminated (safety vs. operational reasons)
- A drug-drug interaction profile, currently returned as "not found"
- No further action on the other 9 TxGNN-predicted indications (including the top-scored "epiglottis neoplasm") unless new clinical trial or literature evidence emerges — all currently lack any supporting data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

