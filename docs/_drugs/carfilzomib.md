---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Carfilzomib: From Multiple Myeloma to Melanoma

## One-Sentence Summary

Carfilzomib is an irreversible 26S proteasome inhibitor used internationally to treat relapsed/refractory multiple myeloma (not currently marketed in Norway per this Evidence Pack).
The TxGNN model predicts activity in **Melanoma**, supported by **0 clinical trials** and **5 preclinical/in-silico publications** — no clinical evidence exists yet.
TxGNN also scored four narrower melanoma-subtype terms (CMM7, pediatric leptomeningeal melanoma, epithelioid uveal melanoma, vulvar melanoma) even higher, but these carry **zero supporting evidence** and are flagged "Hold" — they are noted for transparency but not used as the headline indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Myeloma (relapsed/refractory) — based on internationally known drug class; not documented in Norway regulatory data (drug not marketed) |
| Predicted New Indication | Melanoma |
| TxGNN Prediction Score | 99.03% (rank 9297) |
| Evidence Level | L4 (preclinical/mechanistic studies only) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Other TxGNN-ranked melanoma-related terms (no supporting evidence, all Hold/L5):**

| Disease | TxGNN Score | Note |
|---------|-------------|------|
| CMM7 | 99.37% | Disease definition unclear (possible melanoma molecular subtype); no evidence |
| Pediatric leptomeningeal melanoma | 99.30% | Ultra-rare pediatric CNS subtype; blood-brain barrier penetration unknown; no evidence |
| Epithelioid cell uveal melanoma | 99.23% | Distinct GNAQ/GNA11-driven biology from cutaneous melanoma; no evidence |
| Vulvar melanoma | 99.19% | Rare mucosal subtype with distinct molecular profile; no evidence |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (DG002). Based on known pharmacology, carfilzomib is an irreversible 26S proteasome inhibitor: it blocks proteasomal degradation of ubiquitinated proteins, causing intracellular accumulation of misfolded proteins, inhibition of the NF-κB pathway, ER stress, and downstream apoptosis. It is established (internationally) for multiple myeloma, a hematologic malignancy that is highly dependent on proteasome function for survival.

Melanoma is biologically distinct from multiple myeloma (solid tumor vs. hematologic), so the mechanistic bridge relies on a shared vulnerability to proteasome stress rather than tissue-specific overlap. A single in vitro study (B16-F1 mouse melanoma cells) showed apoptosis induction with carfilzomib combined with bortezomib, evidenced by caspase 3/8/9/12 activation. The remaining literature is either indirect (kinase-target docking screens, NF-κB/heparanase mechanism studies in myeloma models, PROTAC degrader studies) rather than melanoma-specific efficacy data.

Overall, the biological rationale is plausible but thin: it rests on one preclinical cell-line study, with no in vivo, clinical, or human translational data. The four higher-scoring subtype predictions (CMM7, pediatric leptomeningeal, uveal, vulvar melanoma) currently have no literature or trial support at all and should be treated as algorithmic signals only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (across all five predicted melanoma-related indications).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Preclinical (in vitro) | Biology | Carfilzomib + bortezomib induced apoptosis in B16-F1 melanoma cells via caspase 3/8/9/12 activation |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In silico (docking/simulation) | J Biomol Struct Dyn | Molecular docking/dynamics screen across 10 cancer types (incl. melanoma) against 18 kinase targets for drug repurposing |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical (mechanism) | Matrix Biology | Bortezomib/carfilzomib activate NF-κB and upregulate heparanase, associated with aggressive tumor phenotype (myeloma model) |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical (gene regulation) | Mol Cancer Res | AIRAP/ZFAND2A gene regulates melanoma cell survival via E3-ligase cIAP2; proteasome-stress pathway relevance |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preclinical (PROTAC/BET degrader) | Leukemia | BET-degrading PROTACs active in myeloma preclinical models; proteasome-dependent mechanism context |

No RCTs, reviews, or case reports are available; all evidence is preclinical or in silico.

---

## Norway Market Information

Carfilzomib is not marketed in Norway (0 authorizations on file). No license or approved-indication text is available in this Evidence Pack.

---

## Cytotoxicity

Carfilzomib is an antineoplastic agent (proteasome inhibitor class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Standard antineoplastic drug handling precautions apply per institutional protocol; formal TFDA/label guidance not yet available (see DG001) |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or DDI data are currently available in this Evidence Pack (DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for melanoma is limited to a single in vitro cell-line study with no in vivo, clinical, or human data (L4/S1), and the four higher-scoring melanoma-subtype signals have no supporting evidence at all. Combined with the absence of Norway market authorization and a Blocking data gap on TFDA label safety information, the candidate cannot proceed past initial screening.

**To proceed, the following is needed:**
- TFDA label / package insert data (warnings, contraindications) — required to clear the Blocking gap before any S1 safety review (DG001)
- Confirmed original MOA and indication documentation from DrugBank or equivalent source (DG002)
- In vivo preclinical or early clinical evidence specifically supporting melanoma before advancing beyond S1
- Clarification of disease-term definitions for CMM7 and the other subtype predictions, as these appear to be data-quality artifacts rather than actionable signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

