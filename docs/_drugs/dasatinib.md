---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Chronic Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

> Dasatinib is a multi-target tyrosine kinase inhibitor (BCR-ABL, SRC family, c-KIT, PDGFR-β) with established use in chronic myeloid leukemia (CML) and Ph+ acute lymphoblastic leukemia.
> The TxGNN model's top-ranked *new* candidate indication is **Ewing Sarcoma**,
> currently supported by **3 clinical trials** and **6 relevant publications**, mostly preclinical/mechanistic in nature.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Norway regulatory data (drug currently unmarketed). Per the drug's own literature (PMID 18215092), dasatinib's established indications are **chronic myeloid leukemia (CML)** and **Ph+ acute lymphoblastic leukemia** |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% (rank 1502 in global prediction list) |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

> **Note on candidate list:** This evidence pack scored 10 candidate indications for dasatinib. Rank 2, "myeloid leukemia," is **not** a repurposing candidate — it is dasatinib's already-approved standard indication, and the high TxGNN score there simply reflects a known, strong drug–disease relationship. The genuinely novel repurposing signal is Ewing sarcoma (rank 1), which this report focuses on. A summary of all 10 ranked indications is provided further below.

---

## Why is This Prediction Reasonable?

Dasatinib is a small-molecule, orally bioavailable multi-kinase inhibitor. Based on the literature contained in this evidence pack (PMID 18215092), it inhibits BCR-ABL, SRC family kinases (SFK), c-KIT, ephrin-A receptor, and PDGFR-β at nanomolar concentrations, and is roughly 325-fold more potent than imatinib against BCR-ABL. This broad kinase inhibition profile — beyond BCR-ABL alone — is the pharmacological basis for exploring dasatinib outside leukemia, in tumors driven by SRC, KIT, or PDGFR signaling.

Ewing sarcoma is one such candidate. Multiple in vitro studies in this evidence pack (PMID 17363602, 27566104, 31521948, 18202781) show that Ewing sarcoma cells rely heavily on SFK-driven signaling for migration, invasion, and microenvironmental stress adaptation, and that dasatinib can inhibit these processes and induce apoptosis in bone-sarcoma cell lines dependent on SRC for survival. A review specifically covering FAK-SRC targeting in Ewing sarcoma and related pediatric sarcomas (PMID 35655525) frames dasatinib as a rational SFK-directed agent for this tumor family.

However, the mechanistic story does not yet translate cleanly into clinical benefit. The same review (PMID 35655525) explicitly notes that dasatinib **"failed as a single agent"** in the Phase 2 advanced sarcoma trial for Ewing sarcoma and rhabdomyosarcoma subtypes, and the only Ewing-specific combination trial in this pack (NCT00788125) was terminated early with just 7 patients enrolled. The mechanistic rationale is therefore stronger for **anti-invasive/anti-metastatic activity** than for direct tumor-shrinkage efficacy, and combination strategies (rather than monotherapy) appear necessary for clinical translation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib + ifosfamide/carboplatin/etoposide, the only Ewing-specific combination trial; terminated early, underpowered for efficacy conclusions |
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Broad advanced-sarcoma basket trial assessing response rate and 6-month PFS with dasatinib; Ewing sarcoma likely a sub-cohort, but no disease-stratified results reported |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell therapy trial in relapsed/refractory pediatric solid tumors (including Ewing sarcoma); unrelated to dasatinib, included only due to disease overlap |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | Preclinical (in vitro) | Oncology Reports | Dasatinib shows antiproliferative and antimigratory activity in Ewing sarcoma and neuroblastoma cell lines, consistent with c-KIT/PDGFR/SFK activity |
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | Preclinical (in vitro) | Cancer Research | Dasatinib inhibits migration/invasion across diverse sarcoma cell lines and induces apoptosis in SRC-dependent bone sarcoma cells |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Review/Preclinical | Sarcoma | Reviews FAK-SRC targeting in Ewing sarcoma, DSRCT, and rhabdomyosarcoma; explicitly notes dasatinib **failed as a single agent** in the Phase 2 sarcoma trial for these subtypes |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical (in vitro) | Neoplasia | Micro-environmental stress activates SRC-dependent invadopodia formation and cell migration in Ewing sarcoma, a targetable node for SFK inhibitors |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical (in vitro) | Neoplasia | Tenascin C and SRC cooperate to drive invadopodia formation and metastasis-associated invasion in Ewing sarcoma |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Reviews SRC's role in sarcoma biology (proliferation, apoptosis, invasion, metastasis) and its feasibility as a drug target |

*Three additional literature entries returned by the search (PMID 35190971 on chondrosarcoma, 29776413 on plerixafor/CXCR4, and 32999666 on a CML chromosomal abnormality case report) were excluded as not directly relevant to dasatinib in Ewing sarcoma — likely knowledge-graph co-occurrence noise.*

---

## Norway Market Information

Dasatinib currently holds **no marketing authorizations in Norway** (`market_status: 未上市 / Not marketed`, `total_licenses: 0`). No product-level licensing data is available for this evidence pack.

---

## Other Predicted Indications (Full Ranked List, for Context)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Ewing sarcoma | 99.90% | L3 | Research Question | Covered above |
| 2 | Myeloid leukemia | 99.68% | L1 | Proceed with Guardrails | **Already an approved indication**, not a new repurposing target |
| 3 | Liposarcoma | 99.67% | L4 | Research Question | SRC/FAK pathway rationale in myxoid liposarcoma (FUS-CHOP); no disease-specific trial data |
| 4 | Fibromatosis, gingival | 99.65% | L5 | Hold | No trials/literature; no known mechanistic link to dasatinib targets |
| 5 | Dermatofibrosarcoma protuberans | 99.65% | L4 | Research Question | COL1A1-PDGFB driven; class-level PDGFR rationale only, no dasatinib-specific data |
| 6 | Ovarian myxoid liposarcoma | 99.59% | L5 | Hold | No evidence; likely disease-ontology labeling noise |
| 7 | Ganglioneuroblastoma | 99.59% | L5 | Hold | No evidence found |
| 8 | Vertebral anomalies w/ endocrine and T-cell dysfunction | 99.59% | L5 | Hold | No evidence; likely knowledge-graph noise |
| 9 | Inclusion body myopathy w/ Paget disease ± FTD | 99.58% | L5 | Hold | 20 literature hits are generic FTD reviews, none mention dasatinib — disease co-occurrence noise |
| 10 | Hamartoma of lung | 99.56% | L5 | Hold | No evidence; benign tumor with no mechanistic link |

---

## Cytotoxicity

Dasatinib is an approved antineoplastic agent (kinase inhibitor class), so this section applies at the drug level.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — small-molecule multi-kinase inhibitor (BCR-ABL, SRC family kinases, c-KIT, PDGFR-β, ephrin-A receptor) |
| Myelosuppression Risk | Moderate–High. Not directly captured in this pack's structured safety fields, but supported by pack literature and trials at the leukemia indication level, e.g., a dedicated trial studying IL-11 for thrombocytopenia associated with imatinib/dasatinib/other TKIs (NCT00493181), and case reports of dasatinib-associated pleural effusion, chylothorax (PMID 36448074), and interstitial pneumonitis (PMID 36346055) |
| Emetogenicity Classification | Low (typical for oral TKIs as a class; not explicitly reported in this pack) |
| Monitoring Items | CBC with differential, liver and renal function, pleural effusion/pulmonary symptoms, cardiac (QT) monitoring per class effect |
| Handling Protection | Standard oral oncolytic handling precautions; please confirm against official cytotoxic/hazardous drug handling regulations, as this pack contains no facility-specific handling data |

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI query all returned no data in this evidence pack — DDI query status: `not_found`.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Ewing sarcoma signal is mechanistically plausible (SFK-dependent invasion/apoptosis in vitro) but clinically unproven — the only disease-specific combination trial was terminated at n=7, the larger sarcoma basket trial reported no Ewing-specific results, and existing review literature explicitly states dasatinib failed as monotherapy in this tumor type. Combined with a **Blocking** data gap on TFDA/Norway package-insert warnings and contraindications (DG001), this indication is not ready to proceed past the research-question stage.

**To proceed, the following is needed:**
- Resolve DG001 (Norway/TFDA package insert warnings & contraindications) — blocking for any S1 safety pre-assessment
- Resolve DG002 (confirmed mechanism of action from DrugBank API) to strengthen the mechanistic rationale documentation
- New or completed trials testing dasatinib **in combination regimens** for Ewing sarcoma specifically, since single-agent activity has already been shown to fail
- Clarify Norway registration/import pathway, since dasatinib currently has zero marketing authorizations there
- If pursuing rank 3 (liposarcoma) or rank 5 (DFSP) in parallel, generate disease-specific (not basket-trial) efficacy data before advancing past L4
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

