---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 6
---

# Lenalidomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Lenalidomide: From Myelodysplastic Syndrome (del5q) to Myeloid Leukemia

## One-Sentence Summary

> Lenalidomide is an oral immunomodulatory drug (IMiD) already used for transfusion-dependent anemia due to low-risk myelodysplastic syndrome (MDS) with deletion 5q, and for multiple myeloma in combination with dexamethasone.
> The TxGNN model predicts it may also be effective for **Myeloid Leukemia**,
> with **50+ clinical trials** and **20 publications** currently supporting this direction, though a critical safety-labeling gap remains unresolved.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transfusion-dependent anemia due to low-risk MDS with del(5q); multiple myeloma (in combination with dexamethasone) — per literature evidence (PMID 23316859) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for lenalidomide is currently a data gap in the regulatory extraction (DG002). However, the evidence pack's own literature fills this gap: lenalidomide binds **cereblon (CRBN)**, a substrate receptor of the E3 ubiquitin ligase complex, and recruits transcription factors **IKZF1/IKZF3** for ubiquitination and degradation — the mechanism through which it exerts both its antimyeloma and antileukemic activity (PMID 39881283). This CRBN-dependent pathway is the same mechanism already validated in its approved indication of del(5q) MDS.

Myelodysplastic syndrome and acute myeloid leukemia are biologically continuous diseases: MDS carries an intrinsic risk of transformation to AML, and both share the same clonal hematopoietic stem-cell origin (PMID 24656536, PMID 37288607). This shared pathophysiology is why lenalidomide — already effective in del(5q) MDS and multiple myeloma — has been extensively investigated, largely in combination with hypomethylating agents such as azacitidine, across the MDS-to-AML disease spectrum, including relapsed/refractory AML, post-transplant relapse, and maintenance therapy settings.

The predicted new indication therefore represents a plausible extension along the same disease continuum and mechanistic axis as the drug's established use, rather than an unrelated therapeutic area.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00843882](https://clinicaltrials.gov/study/NCT00843882) | Phase 3 | Active, not recruiting | 247 | Lenalidomide ± epoetin alfa for major erythroid response in low/int-1 risk MDS with symptomatic anemia |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Phase 2/3 | Active, not recruiting | 282 | Randomized: azacitidine + lenalidomide vs. azacitidine alone vs. azacitidine + vorinostat in higher-risk MDS/CMML |
| [NCT01301820](https://clinicaltrials.gov/study/NCT01301820) | Phase 2 | Completed | 120 | Randomized maintenance therapy alternating lenalidomide/azacitidine cycles in elderly high-risk AML in first CR |
| [NCT02921802](https://clinicaltrials.gov/study/NCT02921802) | N/A (surveillance) | Completed | 4,626 | Large real-world all-case surveillance of Revlimid 5mg capsules, safety and efficacy |
| [NCT00065156](https://clinicaltrials.gov/study/NCT00065156) | Phase 2 | Completed | 148 | Pivotal single-arm study establishing efficacy of lenalidomide monotherapy in RBC transfusion-dependent del(5q) MDS |
| [NCT02472691](https://clinicaltrials.gov/study/NCT02472691) | Phase 2 | Completed | 50 | Lenalidomide + azacitidine + donor lymphocyte infusion for MDS/CMML/AML relapse after allo-SCT |
| [NCT00352365](https://clinicaltrials.gov/study/NCT00352365) | Phase 2 | Completed | 41 | Lenalidomide monotherapy in untreated elderly del(5q) AML patients declining induction chemotherapy |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | Completed | 29 | Lenalidomide maintenance in high-risk AML in remission |
| [NCT01016600](https://clinicaltrials.gov/study/NCT01016600) | Phase 1/2 | Completed | 31 | Azacitidine plus lenalidomide toxicity and remission rates in AML |
| [NCT04068597](https://clinicaltrials.gov/study/NCT04068597) | Phase 1/2 | Recruiting | 250 | CCS1477 (inobrodib) monotherapy and combination in AML, high-risk MDS and other hematologic malignancies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35277655](https://pubmed.ncbi.nlm.nih.gov/35277655/) | 2022 | RCT | Leukemia | Randomized phase II: azacitidine ± lenalidomide in higher-risk MDS/AML with del(5q) karyotype |
| [30653424](https://pubmed.ncbi.nlm.nih.gov/30653424/) | 2019 | Clinical Trial | J Clin Oncol | Lenalidomide + azacitidine as novel salvage therapy for AML/MDS relapse after allo-SCT |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Clinical Trial (Azalena-Trial) | Haematologica | Azacitidine + lenalidomide + DLI for MDS/AML/CMML relapse post-transplant |
| [40250191](https://pubmed.ncbi.nlm.nih.gov/40250191/) | 2025 | Phase 1 Trial | Leukemia Research | Lenalidomide + bortezomib for AML/MDS relapsing after allo-SCT |
| [34955443](https://pubmed.ncbi.nlm.nih.gov/34955443/) | 2022 | Phase Ib Trial | J Geriatr Oncol | Lenalidomide as post-remission therapy in older AML adults; safety and geriatric functional assessment |
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Systematic Review/Meta-analysis | Hematology (Amsterdam) | Efficacy and adverse events of azacitidine + lenalidomide across AML, MDS, and CMML |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Comprehensive review of MDS pathophysiology and progression to AML |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making framework for MDS treatment |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opin Investig Drugs | Lenalidomide's approved indications and rationale for investigation in higher-risk MDS/AML |
| [39881283](https://pubmed.ncbi.nlm.nih.gov/39881283/) | 2025 | Mechanistic Study | Cell Mol Biol Lett | KDM5C stabilizes cereblon to enhance AML cell sensitivity to lenalidomide |

---

## Norway Market Information

Lenalidomide is currently **not marketed in Norway** — no local authorizations (0 licenses) are on record in this evidence pack. Norway market access data (e.g., MT status via EMA centralized procedure) would need to be separately confirmed before any regulatory pathway can be planned.

---

## Cytotoxicity

Lenalidomide is included here because its established indications (multiple myeloma, MDS) are hematologic malignancies, though it is **not a conventional cytotoxic chemotherapy agent**.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Immunomodulatory drug (IMiD); acts via cereblon (CRBN)-mediated ubiquitination/degradation of IKZF1/IKZF3, not direct DNA-damaging cytotoxicity |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no quantitative toxicity data available in this evidence pack) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count (CBC) with differential; renal function (multiple trial designs targeted cytopenia and dose-limiting toxicity monitoring) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug–drug interaction data were not available in this evidence pack — flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Clinical and mechanistic evidence for lenalidomide's activity across the MDS-to-AML disease spectrum is substantial (L2 — multiple completed trials including at least one randomized Phase 2 study, plus a supporting meta-analysis). However, a **Blocking** data gap (DG001 — missing TFDA/regulatory safety labeling) explicitly prevents entry into the S1 safety pre-assessment stage, and the drug currently has zero market authorizations in Norway. Evidence strength alone cannot offset this regulatory/safety blind spot.

**To proceed, the following is needed:**
- Official product label (warnings, contraindications, DDI) — e.g., EMA SmPC, since no Norway license exists yet
- Formal MOA documentation from DrugBank/regulatory source (currently DG002)
- Clarification of the "myeloid leukemia" disease mapping to a specific AML/MDS subtype and stage relevant to Norway clinical practice
- Assessment of Norway market-entry pathway (e.g., centralized EU authorization extension) given current unmarketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

