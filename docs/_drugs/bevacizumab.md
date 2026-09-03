---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: From Anti-VEGF Oncology Therapy to Cystic Neoplasm (Ovarian/Peritoneal Cancer)

## One-Sentence Summary

Bevacizumab is an anti-VEGF-A monoclonal antibody used across multiple solid tumours in combination with cytotoxic chemotherapy; this Evidence Pack does not record a specific original indication for Norway. Among 10 TxGNN-predicted new indications, **Cystic Neoplasm** — evidence suggests this maps most closely to **low-grade serous ovarian and primary peritoneal carcinoma** — is the only candidate reaching actionable evidence strength, supported by **8 clinical trials (including one Phase 3 RCT with n=1052)** and **20 publications**, including a dedicated systematic review.

> Note: Bevacizumab returned 10 TxGNN-predicted indications in this pack. The other 9 (epiglottis neoplasm, benign tongue neoplasm, testicular tumour, etc.) are rated L3–L5 with weak or absent evidence and are not the focus of this report; they are summarised briefly at the end.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (`original_indications` empty; no Norway licenses on file) |
| Predicted New Indication | Cystic Neoplasm (rank 7/10 by TxGNN score; supporting evidence points to low-grade serous ovarian/peritoneal carcinoma) |
| TxGNN Prediction Score | 99.89% (rank 1565 overall) |
| Evidence Level | L1 |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this pack's `original_moa` field. However, the evidence pack's own repurposing rationale text consistently describes bevacizumab as an **anti-VEGF-A monoclonal antibody** that blocks tumour angiogenesis — this is corroborated across nearly every one of the 10 predicted-indication entries and is consistent with its established pharmacology.

The original indication cannot be confirmed from this dataset (empty `original_indications`, no Norway licenses), but the supporting clinical trial evidence for the "Cystic Neoplasm" candidate is drawn almost entirely from **ovarian, primary peritoneal, and fallopian tube cancer** studies (e.g., NCT00565851, a Phase 3 RCT of carboplatin/paclitaxel ± bevacizumab in platinum-sensitive recurrent ovarian/peritoneal/fallopian tube cancer, n=1052). This strongly suggests the TxGNN label "Cystic Neoplasm" is an imprecise ontology mapping for a cystic/serous ovarian tumour subtype rather than a novel disease area.

Mechanistically this is plausible: VEGF-driven angiogenesis is well documented in epithelial ovarian cancer, and bevacizumab combined with platinum-based chemotherapy is already an established real-world treatment strategy for this tumour family (reflected in the systematic review PMID 37754507 on low-grade serous ovarian cancer). The main caveat is that the disease label itself needs clarification before this can be treated as a clean "new indication" rather than a restatement of known use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Phase 3 | Active, not recruiting | 1052 | Carboplatin/paclitaxel (or gemcitabine) ± bevacizumab, followed by bevacizumab maintenance and secondary cytoreductive surgery, in platinum-sensitive recurrent ovarian, primary peritoneal, and fallopian tube cancer. Grade A relevance — key pivotal-scale RCT. |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Phase 2 | Active, not recruiting | 133 | Atezolizumab + bevacizumab in rare solid tumours, including rare gynecologic tumours. Grade A relevance. |
| [NCT00381797](https://clinicaltrials.gov/study/NCT00381797) | Phase 2 | Completed | 97 | Bevacizumab + irinotecan in children with recurrent/refractory glioma, medulloblastoma, ependymoma. Grade B — related biology, different population. |
| [NCT00023959](https://clinicaltrials.gov/study/NCT00023959) | Phase 1 | Completed | 39 | General bevacizumab safety in head & neck cancer with 5-FU/hydroxyurea/RT. Grade C — non-specific. |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | Completed | 66 | Erlotinib + cetuximab ± bevacizumab in metastatic renal/colorectal/head & neck/pancreatic/NSCLC. Grade C. |
| [NCT00324987](https://clinicaltrials.gov/study/NCT00324987) | Phase 3 | Terminated | 12 | Imatinib ± bevacizumab in metastatic/unresectable GIST; terminated, small sample. Grade C. |
| [NCT00492089](https://clinicaltrials.gov/study/NCT00492089) | Phase 2 | Completed | 11 | Bevacizumab to control brain radiation damage. Grade C — unrelated endpoint. |
| [NCT01096381](https://clinicaltrials.gov/study/NCT01096381) | N/A | Terminated | 8 | Biomarkers for bevacizumab-induced hypertension; not efficacy-focused, terminated. Grade C. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | Systematic Review | Current Oncology | Systematic review of bevacizumab in low-grade serous ovarian cancer; supports activity in a chemoresistant subtype. |
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | Cohort | Future Oncology | Retrospective cohort (n=51): ORR 54.1%, median PFS ~15 months with bevacizumab + chemotherapy in recurrent low-grade serous ovarian cancer. |
| [24978709](https://pubmed.ncbi.nlm.nih.gov/24978709/) | 2014 | Prospective study | Int J Gynecol Cancer | Bevacizumab shows durable activity in low-grade serous ovarian and primary peritoneal cancer. |
| [18165643](https://pubmed.ncbi.nlm.nih.gov/18165643/) | 2008 | Phase 2 Trial | J Clin Oncol | Bevacizumab + low-dose metronomic cyclophosphamide in recurrent ovarian cancer; multicenter consortium trial. |
| [18796376](https://pubmed.ncbi.nlm.nih.gov/18796376/) | 2008 | Cohort | Clin Transl Oncol | Oral cyclophosphamide + bevacizumab in heavily pre-treated ovarian cancer. |
| [40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/) | 2025 | Ancillary study (Phase 3) | Eur J Cancer | PAOLA-1/ENGOT-ov25 ancillary analysis on bevacizumab/olaparib maintenance in HRD+ HGSOC. |
| [32494876](https://pubmed.ncbi.nlm.nih.gov/32494876/) | 2020 | Review | Curr Oncol Rep | First-line management of advanced high-grade serous ovarian cancer; discusses VEGF-targeted therapy role. |
| [27498762](https://pubmed.ncbi.nlm.nih.gov/27498762/) | 2016 | Mechanistic/Biomarker | Scientific Reports | VEGF-dependent gene signature predicts prognosis in mesenchymal ovarian cancer subtype — supports mechanistic rationale. |
| [31989304](https://pubmed.ncbi.nlm.nih.gov/31989304/) | 2020 | Review | Curr Oncol Rep | Review of treatment progress in low-grade serous tumours. |
| [40644648](https://pubmed.ncbi.nlm.nih.gov/40644648/) | 2025 | Trial (RAMP 201) | J Clin Oncol | Avutometinib ± defactinib in recurrent low-grade serous ovarian cancer; contextualises the treatment landscape bevacizumab competes in. |

---

## Norway Market Information

Bevacizumab is currently **not marketed in Norway** under this dataset — `taiwan_regulatory.licenses` is empty and `total_licenses = 0`. No authorization records, product names, or approved indication text are available to populate a licensing table.

---

## Cytotoxicity

Bevacizumab is an antineoplastic agent (anti-VEGF-A monoclonal antibody used across multiple oncology combination regimens documented throughout the evidence pack), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-angiogenic monoclonal antibody) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low as monotherapy; myelosuppression seen in the supporting trials is primarily attributable to combination cytotoxic partners (carboplatin, paclitaxel, cyclophosphamide) |
| Emetogenicity Classification | Low (monoclonal antibodies are generally minimally emetogenic) |
| Monitoring Items | Blood pressure, urine protein, wound healing status, bleeding/thromboembolic signs; CBC and renal function when co-administered with cytotoxic chemotherapy |
| Handling Protection | Standard biologic infusion precautions; cytotoxic drug handling regulations apply to combination chemotherapy partners, not to bevacizumab itself |

---

## Safety Considerations

Please refer to the package insert for safety information. This Evidence Pack's `key_warnings`, `contraindications`, and DDI fields are all marked as data gaps (DG001, Blocking severity), so no drug-specific warnings can be reported here.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cystic Neoplasm is the only one of 10 TxGNN-predicted indications reaching L1 evidence, anchored by a Phase 3 RCT (n=1052) and a dedicated systematic review, consistent with bevacizumab's established real-world role in ovarian/peritoneal cancer. However, the disease label itself is ambiguous, the drug is not currently marketed in Norway, and core safety/MOA data are missing (blocking data gaps).

**To proceed, the following is needed:**
- Resolve the disease ontology mapping — confirm "Cystic Neoplasm" corresponds to low-grade serous ovarian/primary peritoneal carcinoma before treating this as a distinct new indication
- Close DG001 (package insert warnings/contraindications, Blocking) and DG002 (confirmed MOA/DrugBank categories, High) before any S1 safety review
- Assess a Norway market entry/registration pathway, since no local authorization currently exists
- Obtain DDI data (currently `not_found`)
- The remaining 9 predicted indications (L3–L5, Hold) require additional trial/literature evidence before re-evaluation and are not actionable at this time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

