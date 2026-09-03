---
layout: default
title: Idelalisib
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Idelalisib
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

Using no specific coding skill here—this is a direct content-generation task per the detailed template provided in the system prompt, so I'll produce the report directly from the Evidence Pack.

# Idelalisib: From B-Cell Lymphoid Malignancies to Mantle Cell Lymphoma

## One-Sentence Summary

> Idelalisib is an oral PI3Kδ (phosphatidylinositol 3-kinase delta) inhibitor originally developed for relapsed chronic lymphocytic leukemia (CLL), follicular lymphoma (FL), and small lymphocytic lymphoma (SLL) — all B-cell malignancies driven by B-cell receptor (BCR) signalling.
> The TxGNN model predicts it may also be effective for **Mantle Cell Lymphoma (MCL)**, another BCR/PI3Kδ-dependent B-cell neoplasm,
> with **9 clinical trials** and **20 publications** currently supporting this direction — including a completed Phase 1 trial reporting direct clinical activity in MCL.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in the Norway regulatory registry (no license record). Per the literature evidence in this pack (e.g., PMID 25187123, 25637459), idelalisib was originally approved elsewhere for relapsed CLL, relapsed follicular lymphoma, and relapsed SLL |
| Predicted New Indication | Mantle Cell Lymphoma (MCL) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (drug-level MOA field is a data gap). Based on known information drawn from the literature evidence collected here, idelalisib is a first-in-class, selective inhibitor of the delta isoform of phosphatidylinositol 3-kinase (PI3Kδ), a lipid kinase expressed almost exclusively in hematopoietic cells and constitutively active downstream of the B-cell receptor (BCR) in B-cell malignancies (PMID 30069634, 28295729).

Its efficacy in relapsed CLL, follicular lymphoma, and SLL is well established in the literature (PMID 25637459, 25187123), and mechanistically this rationale extends naturally to mantle cell lymphoma. MCL is likewise a mature B-cell neoplasm characterized by the t(11;14) translocation and constitutive BCR/PI3K/AKT pathway activation, which drives survival and proliferation of the malignant clone (PMID 22361516, 24273091). Because idelalisib blocks the same upstream signalling node exploited by MCL cells, it is biologically plausible that the drug retains activity in this related lymphoma subtype.

This is not purely theoretical: a dedicated Phase 1 clinical trial (PMID 24615778, published in *Blood*) directly tested idelalisib in relapsed/refractory MCL and reported measurable clinical activity, later summarized in a companion report titled "Idelalisib has activity in mantle cell lymphoma" (PMID 24795031). However, subsequent mechanistic work also identified intrinsic and acquired resistance pathways in MCL (e.g., CBX5 loss, PMID 40466505; p300/CBP-mediated resistance, PMID 33850273), indicating that while the mechanistic rationale is sound, clinical benefit in MCL is not uniform and combination strategies may be needed.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01838434](https://clinicaltrials.gov/study/NCT01838434) | Phase 1 | Completed | 106 | Idelalisib + lenalidomide in relapsed/refractory MCL |
| [NCT01088048](https://clinicaltrials.gov/study/NCT01088048) | Phase 1 | Completed | 241 | Idelalisib combined with chemo/immunomodulatory/anti-CD20 agents in relapsed/refractory iNHL, MCL, or CLL |
| [NCT02603445](https://clinicaltrials.gov/study/NCT02603445) | Phase 1 | Completed | 20 | BCL201 + idelalisib combination in follicular lymphoma and MCL |
| [NCT03740529](https://clinicaltrials.gov/study/NCT03740529) | Phase 1/2 | Completed | 803 | Pirtobrutinib in CLL/SLL/NHL patients who failed standard of care (idelalisib-experienced population) |
| [NCT02824159](https://clinicaltrials.gov/study/NCT02824159) | N/A | Completed | 121 | Real-world pharmacokinetic/side-effect correlation study of ibrutinib and idelalisib; notes EMA approval of idelalisib specifically for MCL |
| [NCT01796470](https://clinicaltrials.gov/study/NCT01796470) | Phase 2 | Terminated | 66 | Entospletinib + idelalisib in relapsed/refractory hematologic malignancies including MCL, CLL, DLBCL, iNHL |
| [NCT02457598](https://clinicaltrials.gov/study/NCT02457598) | Phase 1 | Terminated | 203 | Tirabrutinib combined with targeted anti-cancer therapies in B-cell malignancies |
| [NCT03151057](https://clinicaltrials.gov/study/NCT03151057) | Phase 1 | Terminated | 16 | Idelalisib as post-allogeneic HSCT maintenance in B-cell malignancies |
| [NCT04985214](https://clinicaltrials.gov/study/NCT04985214) | N/A | Unknown | 464 | Quality-of-life assessment in lymphoma patients (incl. MCL) treated with oral therapies including idelalisib |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24615778](https://pubmed.ncbi.nlm.nih.gov/24615778/) | 2014 | Phase 1 Trial | Blood | Phase 1 study of PI3Kδ inhibitor idelalisib in 40 patients with relapsed/refractory MCL; safety, PK, and response data |
| [24795031](https://pubmed.ncbi.nlm.nih.gov/24795031/) | 2014 | Clinical Report | Cancer Discovery | Idelalisib effective in heavily pretreated MCL patients |
| [27342398](https://pubmed.ncbi.nlm.nih.gov/27342398/) | 2017 | Mechanistic/Clinical | Clinical Cancer Research | Idelalisib impacts MCL cell growth via translation-regulatory mechanism disruption |
| [33850273](https://pubmed.ncbi.nlm.nih.gov/33850273/) | 2022 | Preclinical | Acta Pharmacologica Sinica | p300/CBP inhibitor A-485 overcomes intrinsic idelalisib resistance in MCL (in vitro/in vivo) |
| [40466505](https://pubmed.ncbi.nlm.nih.gov/40466505/) | 2025 | Preclinical | Phytomedicine | CBX5 loss drives PI3Kδ inhibitor resistance in MCL; propolis restores sensitivity via ferroptosis |
| [38815797](https://pubmed.ncbi.nlm.nih.gov/38815797/) | 2024 | Preclinical | Cancer Letters | Idelalisib enhances anti-tumor effect of palbociclib via PLK1 in B-cell lymphoma (incl. MCL) |
| [24974852](https://pubmed.ncbi.nlm.nih.gov/24974852/) | 2014 | Review | British Journal of Haematology | Overview of current regimens and novel agents for MCL |
| [26360791](https://pubmed.ncbi.nlm.nih.gov/26360791/) | 2015 | Review | Expert Opinion on Pharmacotherapy | Treatment options for MCL, including PI3K-pathway agents |
| [23512567](https://pubmed.ncbi.nlm.nih.gov/23512567/) | 2013 | Review | Current Treatment Options in Oncology | Current and emerging therapies in MCL by patient fitness/age |
| [28775119](https://pubmed.ncbi.nlm.nih.gov/28775119/) | 2017 | Review | Haematologica | Practical approach to incidence and management of ibrutinib/idelalisib toxicity |

---

## Norway Market Information

Idelalisib is currently **not marketed in Norway** (`未上市`) and holds **0 authorizations** on file — no license records are available to summarize.

---

## Cytotoxicity

*This section applies because idelalisib is an antineoplastic agent (targeted small-molecule kinase inhibitor used across B-cell hematologic malignancies).*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PI3Kδ inhibitor, oral small-molecule kinase inhibitor; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Low to moderate — neutropenia has been reported in idelalisib trials, but the dominant safety signals described in the literature are non-hematologic (hepatotoxicity, colitis, pneumonitis) (PMID 28775119, 30069634) |
| Emetogenicity Classification | Low — oral targeted kinase inhibitor, not among conventionally high-emetogenic agents |
| Monitoring Items | Liver function tests (baseline and frequent early monitoring), CBC with differential, respiratory symptom/imaging surveillance (pneumonitis risk), GI symptom monitoring (colitis/diarrhea), infection surveillance |
| Handling Protection | Standard oral hazardous-drug handling precautions per institutional policy for targeted oncology agents; not classified under conventional cytotoxic reconstitution/handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug-interaction data are currently on file in this Evidence Pack — see Data Gap DG001, blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While mechanistic rationale is sound and a completed Phase 1 trial plus multiple early-phase combination studies show clinical activity of idelalisib in MCL, there is no confirmatory Phase 2/3 RCT specific to this indication, and the drug is not currently marketed in Norway. Critically, official label safety data (warnings/contraindications) is a **Blocking** data gap (DG001), which prevents this candidate from entering the S1 safety pre-assessment stage.

**To proceed, the following is needed:**
- Official package insert / TFDA-equivalent label with warnings and contraindications (resolves DG001, Blocking)
- Confirmed mechanism-of-action documentation from DrugBank (resolves DG002)
- Regulatory pathway assessment for Norway market entry, given current "Not Marketed" status
- If development continues, a confirmatory Phase 2 (ideally randomized) trial specifically in MCL patients to move beyond the existing Phase 1 activity signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

