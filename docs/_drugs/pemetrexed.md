---
layout: default
title: Pemetrexed
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
---

# Pemetrexed
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

# Pemetrexed: From Pleural Mesothelioma to Malignant Peritoneal Mesothelioma

## One-Sentence Summary

Pemetrexed is a multitargeted antifolate chemotherapy already established as first-line standard-of-care treatment for malignant pleural mesothelioma (in combination with cisplatin) and non-small cell lung cancer.
The TxGNN model predicts it may also be effective for **Malignant Peritoneal Mesothelioma**,
with **11 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Norway regulatory license text on file. Based on clinical evidence in this pack, pemetrexed's established indications are Non-Small Cell Lung Cancer and Malignant Pleural Mesothelioma (pemetrexed + cisplatin is confirmed first-line standard of care for pleural mesothelioma per Vogelzang 2003 Phase 3 trial, PMID 12860938) |
| Predicted New Indication | Malignant Peritoneal Mesothelioma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured DrugBank fields (Data Gap DG002). Based on information contained in the linked clinical evidence, pemetrexed is a multitargeted antifolate that inhibits thymidylate synthase (TS), dihydrofolate reductase (DHFR), and glycinamide ribonucleotide formyltransferase (GARFT) — key folate-dependent enzymes required for DNA/nucleotide synthesis. By blocking these pathways, pemetrexed halts replication in rapidly dividing malignant cells.

Malignant pleural mesothelioma and malignant peritoneal mesothelioma both arise from the same mesothelial cell lineage, differing only in the anatomical cavity affected (pleura vs. peritoneum). Because pemetrexed + cisplatin is already the confirmed standard first-line regimen for pleural mesothelioma, extrapolating this antifolate mechanism to peritoneal mesothelioma is mechanistically straightforward — the tumor biology is highly similar even though the primary site differs.

This extrapolation is not purely theoretical: several retrospective and prospective studies directly test pemetrexed-based regimens in peritoneal mesothelioma specifically (e.g., Nagata 2019, PMID 31287877; Fujimoto 2017, PMID 28594258), and two actively recruiting Phase 2 RCTs (NCT06057935, NCT05001880) are evaluating pemetrexed/platinum-based systemic chemotherapy in this population. This combination of mechanistic plausibility and site-specific clinical evidence supports the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06057935](https://clinicaltrials.gov/study/NCT06057935) | Phase 2 | Recruiting | 64 | Randomized trial of intraperitoneal vs. intravenous chemotherapy after cytoreductive surgery + HIPEC for peritoneal mesothelioma |
| [NCT05001880](https://clinicaltrials.gov/study/NCT05001880) | Phase 2 | Recruiting | 66 | Randomized trial of carboplatin/pemetrexed/bevacizumab ± atezolizumab as neoadjuvant/palliative therapy for peritoneal mesothelioma |
| [NCT03875144](https://clinicaltrials.gov/study/NCT03875144) | Phase 2 | Suspended | 66 | PIPAC + systemic chemotherapy (cisplatin+pemetrexed) vs. systemic chemotherapy alone as 1st-line MPM treatment |
| [NCT00402766](https://clinicaltrials.gov/study/NCT00402766) | Phase 1 | Completed | 19 | Cisplatin, pemetrexed, and imatinib mesylate in unresectable/metastatic malignant mesothelioma |
| [NCT06543069](https://clinicaltrials.gov/study/NCT06543069) | Phase 2 | Recruiting | 28 | Sintilimab + bevacizumab combined with pemetrexed and cisplatin for unresectable peritoneal mesothelioma |
| [NCT04462809](https://clinicaltrials.gov/study/NCT04462809) | Phase 2 | Unknown | 40 | Maintenance talazoparib following first-line platinum-based chemotherapy in pleural/peritoneal mesothelioma |
| [NCT02535312](https://clinicaltrials.gov/study/NCT02535312) | Phase 1/2 | Active, not recruiting | 30 | TRC102 + pemetrexed/cisplatin in advanced solid tumors and pemetrexed/cisplatin-refractory mesothelioma |
| [NCT02029690](https://clinicaltrials.gov/study/NCT02029690) | Phase 1 | Terminated | 85 | ADI-PEG 20 with pemetrexed and cisplatin in arginine-requiring tumors, including peritoneal mesothelioma |
| [NCT01353482](https://clinicaltrials.gov/study/NCT01353482) | Phase 1/2 | Withdrawn | 0 | Vorinostat with pemetrexed-cisplatin as first-line therapy for malignant pleural mesothelioma |
| [NCT00061477](https://clinicaltrials.gov/study/NCT00061477) | Phase 2 | Completed | 48 | Pemetrexed plus gemcitabine as front-line chemotherapy for pleural or peritoneal mesothelioma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31417959](https://pubmed.ncbi.nlm.nih.gov/31417959/) | 2019 | Cohort | Pleura and peritoneum | Bidirectional chemotherapy improved resectability, enabling surgery and HIPEC for initially unresectable peritoneal mesothelioma |
| [35407498](https://pubmed.ncbi.nlm.nih.gov/35407498/) | 2022 | Review | Journal of Clinical Medicine | Overview of surgical cytoreduction + HIPEC as preferred treatment; systemic chemotherapy role reviewed |
| [30450291](https://pubmed.ncbi.nlm.nih.gov/30450291/) | 2018 | Review | Translational Lung Cancer Research | Comprehensive review of MPM biology, diagnosis, and treatment approaches |
| [28594258](https://pubmed.ncbi.nlm.nih.gov/28594258/) | 2017 | Retrospective | Expert Review of Anticancer Therapy | Retrospective evaluation of first-line pemetrexed + cisplatin efficacy in peritoneal mesothelioma |
| [31287877](https://pubmed.ncbi.nlm.nih.gov/31287877/) | 2019 | Retrospective | Japanese Journal of Clinical Oncology | Efficacy and safety of pemetrexed + cisplatin as first-line chemotherapy in advanced peritoneal mesothelioma |
| [41133016](https://pubmed.ncbi.nlm.nih.gov/41133016/) | 2025 | Retrospective | Clinical Medicine Insights: Oncology | Comparison of pemetrexed-platinum vs. gemcitabine-platinum first-line regimens in peritoneal mesothelioma |
| [33743636](https://pubmed.ncbi.nlm.nih.gov/33743636/) | 2021 | Retrospective | BMC Cancer | Efficacy of second-line treatment and prognostic factors following pemetrexed-based first-line therapy |
| [38806763](https://pubmed.ncbi.nlm.nih.gov/38806763/) | 2024 | Multi-center study | Annals of Surgical Oncology | Analysis of treatment strategies and outcomes across a multi-center peritoneal mesothelioma cohort |
| [23291819](https://pubmed.ncbi.nlm.nih.gov/23291819/) | 2013 | Case report | BMJ Case Reports | Patient responded to rechallenge with cisplatin and pemetrexed after initial progression |
| [26941986](https://pubmed.ncbi.nlm.nih.gov/26941986/) | 2016 | Review | Journal of Gastrointestinal Oncology | Diagnosis and management overview of peritoneal mesothelioma, including systemic chemotherapy options |

---

## Norway Market Information

Currently no marketing authorizations are on file — pemetrexed is **not marketed** in Norway (0 licenses).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (multitargeted antifolate / antimetabolite class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations applicable to antineoplastic agents |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence Level L2 is supported by two actively recruiting Phase 2 RCTs (NCT06057935, NCT05001880) directly testing pemetrexed-based regimens in peritoneal mesothelioma, plus multiple retrospective cohort studies showing efficacy of first-line pemetrexed + cisplatin. Mechanistic plausibility is high given pemetrexed's already-confirmed role in pleural mesothelioma, a tumor of the same cell lineage.

**To proceed, the following is needed:**
- TFDA/local regulatory warnings and contraindication data (currently a Blocking data gap, DG001)
- Structured DrugBank mechanism-of-action and toxicity profile (High-severity gap, DG002)
- A Norway-specific market entry assessment, since the drug is not currently marketed there
- Mature outcome data from the two ongoing Phase 2 RCTs (NCT06057935, NCT05001880)
- A formal drug-drug interaction review, since the current DDI query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

