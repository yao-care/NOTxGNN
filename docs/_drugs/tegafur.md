---
layout: default
title: Tegafur
parent: 僅模型預測 (L5)
nav_order: 342
evidence_level: L5
indication_count: 10
---

# Tegafur
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

# Tegafur: From Established Fluoropyrimidine Chemotherapy to Colonic Neoplasm

## One-Sentence Summary

Tegafur is an oral prodrug of 5-fluorouracil, most widely known as a component of combination regimens such as UFT (tegafur/uracil) and S-1 (tegafur/gimeracil/oteracil), used broadly in gastrointestinal and other solid tumors. The TxGNN model predicts high relevance for **Colonic Neoplasm**, and this is strongly supported by **31 clinical trials** (multiple completed Phase 3 RCTs) and **20 publications** — though the evidence indicates this is an *already-established* clinical use rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in the regulatory dataset (no approved license on file). Based on known pharmacology, tegafur is a 5-FU prodrug used clinically as a component of UFT/S-1 combinations across gastric, colorectal, breast, and lung cancers |
| Predicted New Indication | Colonic Neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action documentation was not retrievable from DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). Based on the available evidence-pack rationale, tegafur is metabolized in the liver via CYP2A6 to its active moiety, 5-fluorouracil, which inhibits thymidylate synthase and disrupts DNA synthesis — a cytotoxic mechanism broadly effective against highly proliferative malignancies, including colorectal cancer.

Importantly, the evidence pack itself flags a critical caveat: **tegafur (as UFT or S-1) already carries an established, guideline-recognized role in colon and colorectal cancer treatment** — most visibly as adjuvant therapy after curative resection and in metastatic settings. The very large body of completed Phase 3 RCTs below reflects decades of confirmed clinical use rather than a newly-discovered signal. In other words, the TxGNN model's high score for "colonic neoplasm" is best interpreted as **validation of known pharmacology**, not as a novel drug-repurposing opportunity. This distinction should inform how much strategic weight is placed on this candidate versus genuinely new signals.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1,608 | UFT+leucovorin vs 5-FU+leucovorin, head-to-head in resected stage II/III colon cancer |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | UFT postoperative adjuvant chemotherapy vs surgery alone (Dukes C colorectal cancer, NSAS-CC) |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2,025 | UFT adjuvant chemotherapy vs observation in curatively resected stage II colon cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1,535 | UFT+leucovorin vs S-1 as adjuvant treatment for stage III colon cancer |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | Unknown | 340 | Multi-arm comparison of UFT+LV / UFT+LV+PSK regimens for stage III colorectal cancer |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial: S-1 (tegafur-based) vs capecitabine as first-line therapy in metastatic colorectal cancer |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1,191 | S-1+oxaliplatin (SOX) vs capecitabine+oxaliplatin (XELOX) adjuvant therapy for stage III colorectal cancer |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | Completed | 47 | UFT + cetuximab + irinotecan + oxaliplatin in first-line metastatic colorectal cancer |
| [NCT00002801](https://clinicaltrials.gov/study/NCT00002801) | Phase 1 | Completed | 30 | UFT + leucovorin + radiotherapy postoperatively for rectal cancer |
| [NCT05266300](https://clinicaltrials.gov/study/NCT05266300) | N/A | Completed | 722 | Clinical implementation of DPYD genotyping in patients treated with fluoropyrimidines (incl. tegafur), safety/pharmacogenomics focus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clinical Colorectal Cancer | ACTS-CC 02 Phase III trial: S-1+oxaliplatin vs UFT/LV as postoperative adjuvant therapy in high-risk stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | Updated 5-year survival analysis of ACTS-CC 02; SOX not superior to UFT/LV on disease-free survival |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT | Medicine | Nationwide cohort study and meta-analysis: UFT vs 5-FU as postoperative adjuvant chemotherapy in stage II/III colon cancer |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | Adjuvant immunochemotherapy trial combining OK-432 with UFT and HCFU in colorectal cancer |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06: oral UFT+leucovorin vs IV 5-FU+leucovorin in stage II/III colon carcinoma |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT | Annals of Oncology | JFMC33-0502 Phase III trial on treatment duration of UFT/LV adjuvant therapy for stage IIB/III colon cancer |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clinical Colorectal Cancer | Asian consensus guideline adaptation for metastatic colorectal cancer management |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | Review of UFT clinical evidence, mechanism of action, and future directions in adjuvant chemotherapy for solid tumors |
| [6402917](https://pubmed.ncbi.nlm.nih.gov/6402917/) | 1983 | Cohort | Am J Clin Oncol | Comparative study of oral tegafur vs IV 5-fluorouracil in metastatic colorectal cancer |
| [7990476](https://pubmed.ncbi.nlm.nih.gov/7990476/) | 1994 | Cohort | J Surg Oncol | Effects of preoperative UFT chemotherapy on DNA ploidy, cell cycle, and histology in gastric/colonic cancer |

---

## Norway Market Information

Tegafur is currently **not marketed** in Norway, and no drug authorization records are available in this evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class; 5-FU prodrug) |
| Myelosuppression Risk | Medium — fluoropyrimidines are associated with neutropenia and leukopenia; DPYD-deficient patients are at markedly elevated risk (see NCT05266300 genotyping study) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; DPYD genotype/phenotype status where available to reduce severe toxicity risk |
| Handling Protection | Must follow institutional cytotoxic/hazardous drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack; the absence of Norwegian product-label warnings/contraindications is flagged as a **Blocking** data gap (DG001) that must be resolved before final safety sign-off.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The colonic neoplasm signal is backed by an unusually large and mature evidence base — multiple completed Phase 3 RCTs (some with >1,500 patients) and consistent literature support (L1) — but this reflects **confirmation of an already-established use** of tegafur/UFT/S-1 in colorectal cancer, not a new discovery. The other nine predicted indications in this pack (villous adenoma, NET G1, lipoma, leiomyoma, lymphangioma, hemangioma, etc.) have negligible-to-weak evidence (L4–L5) and are mechanistically implausible for a cytotoxic agent, and should remain on **Hold**.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain formal product-label warnings/contraindications before any S1 safety review
- Resolve DG002 (High): confirm mechanism-of-action documentation via DrugBank API
- Clarify regulatory pathway: since tegafur holds zero authorizations in Norway, determine whether market entry (rather than "repurposing") is the actual strategic question
- Reassess portfolio priority: given this candidate largely reconfirms known clinical practice, consider whether resources are better directed toward genuinely novel signals elsewhere in the prediction set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

