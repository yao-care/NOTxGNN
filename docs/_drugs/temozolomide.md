---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Temozolomide: From Glioblastoma to Adult Astrocytic Tumour

## One-Sentence Summary

> Temozolomide is an oral alkylating chemotherapy agent whose established clinical use — based on the literature captured in this evidence pack — is the treatment of glioblastoma and other high-grade gliomas.
> The TxGNN model predicts it may be effective for **Adult Astrocytic Tumour**,
> with **2 clinical trials** and **20 publications** currently supporting this direction — though much of this evidence describes temozolomide's *already-established* standard-of-care role rather than a novel repurposing signal (see rationale below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided in structured regulatory data; literature within this evidence pack consistently identifies glioblastoma/malignant glioma as the drug's established use (see [Why is This Prediction Reasonable?](#why-is-this-prediction-reasonable)) |
| Predicted New Indication | Adult astrocytic tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs — e.g. NCT00052455, plus Stupp 2005/2009, Wick 2012, Herrlinger 2019, Stupp 2015) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as data gap DG002, High severity). Based on the literature attached to this candidate, temozolomide is an oral imidazotetrazine alkylating agent that induces DNA methylation-mediated cytotoxicity in tumour cells; it is described repeatedly across the retrieved publications as the backbone of chemoradiotherapy for glioblastoma (the Stupp protocol, NEJM 2005).

Glioblastoma is itself a high-grade **astrocytic tumour**, so the top-ranked TxGNN prediction ("adult astrocytic tumour") largely overlaps with the drug's already-documented use rather than representing a mechanistically distant new indication. The very high TxGNN score (99.36%) and the depth of Phase 3 evidence are therefore consistent with confirming an *existing* therapeutic relationship, not discovering a new one. This should be explicitly noted to decision-makers: the value of this candidate lies in confirming/documenting an established indication rather than in genuine repurposing novelty.

By contrast, the second-ranked prediction in this pack — **cauda equina neoplasm** (spinal myxopapillary ependymoma) — is mechanistically more novel and is supported only by a single case report (PMID 29270703) describing remarkable efficacy in a relapsed, disseminated case. This is a much earlier-stage signal that may warrant separate tracking.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (cabozantinib) combined with temozolomide and radiation in first-line glioblastoma |
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomized comparison of temozolomide vs. PCV regimen in recurrent WHO Grade III/IV astrocytic tumours |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT (Phase 3) | N Engl J Med | Landmark Stupp trial: radiotherapy + concomitant/adjuvant temozolomide vs. radiotherapy alone for newly diagnosed glioblastoma |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT (Phase 3, 5-yr follow-up) | Lancet Oncol | Confirms sustained survival benefit of temozolomide + radiotherapy in glioblastoma (EORTC-NCIC trial) |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT (Phase 3) | Lancet Oncol | NOA-08 trial: temozolomide alone vs. radiotherapy alone in elderly patients with malignant astrocytoma |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT (Phase 3) | N Engl J Med | Bevacizumab added to standard temozolomide/radiotherapy in newly diagnosed glioblastoma |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT (Phase 3) | JAMA | Tumor-Treating Fields + temozolomide vs. temozolomide alone as maintenance therapy in glioblastoma |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT (Phase 3) | Lancet | CeTeG/NOA-09: lomustine-temozolomide combination vs. standard temozolomide in MGMT-methylated glioblastoma |
| [41345097](https://pubmed.ncbi.nlm.nih.gov/41345097/) | 2025 | Trial (Phase Ib/II) | Nat Commun | GEINO 1602: glasdegib + temozolomide/radiotherapy in newly diagnosed glioblastoma |
| [38768767](https://pubmed.ncbi.nlm.nih.gov/38768767/) | 2024 | Trial (Phase 1/2) | Int J Radiat Oncol Biol Phys | Disulfiram/copper combined with radiotherapy and temozolomide in newly diagnosed glioblastoma |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Review of glioblastoma and other primary adult brain malignancies |
| [29075865](https://pubmed.ncbi.nlm.nih.gov/29075865/) | 2017 | Review | Curr Oncol Rep | Review of glioblastoma treatment approaches in older adults |

---

## Norway Market Information

Temozolomide is **not currently marketed** in this jurisdiction (`market_status: 未上市`), and no authorizations are on record (`total_licenses: 0`). No product/license table can be produced from available data.

---

## Cytotoxicity

Temozolomide is an alkylating chemotherapy agent, meeting the antineoplastic classification criteria (cytotoxic drug class; established use in malignant glioma per literature above).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) |
| Myelosuppression Risk | High — alkylating agents in this class are typically associated with dose-limiting thrombocytopenia and neutropenia; drug-specific toxicity grading data is not available in this pack (see DG001) |
| Emetogenicity Classification | Moderate (typical for oral alkylating agents in this class) |
| Monitoring Items | CBC with differential (baseline and periodic during treatment), liver function tests, renal function |
| Handling Protection | Cytotoxic drug handling precautions apply (capsule should not be opened/crushed; standard hazardous drug handling protocols recommended) |

*Note: the above reflects general characteristics of this drug class. Drug-specific toxicity data (package insert) is a blocking data gap (DG001) and should be confirmed before clinical use.*

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are currently unavailable in this evidence pack (flagged as DG001, Blocking severity — this specifically prevents completion of the S1 preliminary safety assessment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for temozolomide in astrocytic tumours is very strong (multiple completed Phase 3 RCTs), but this largely confirms an already-established indication rather than a novel repurposing opportunity. More importantly, a **Blocking** data gap (DG001) prevents completion of the mandatory S1 safety evaluation, and the drug currently has zero market authorizations in this jurisdiction.

**To proceed, the following is needed:**
- TFDA/regulatory package insert with warnings, contraindications, and DDI data (resolves DG001 — required before S1 safety evaluation can proceed)
- DrugBank-sourced mechanism-of-action detail (resolves DG002)
- Clarification of true repurposing novelty for "adult astrocytic tumour," given substantial overlap with temozolomide's established glioblastoma use
- If pursued: confirmation of regulatory pathway/authorization plans, since the drug is not currently marketed
- Secondary signal for future tracking: **cauda equina neoplasm** (spinal myxopapillary ependymoma) is supported only by a single case report (PMID 29270703) and requires substantially more evidence (preclinical or prospective clinical data) before advancing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

