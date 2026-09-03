---
layout: default
title: Duvelisib
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Duvelisib
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

Using the Evidence Pack you provided (candidate `TW-DB11952-multi`, DUVELISIB), here is the evaluation report. Note upfront: the top-ranked prediction (Hodgkin lymphoma) carries an explicit disease-entity mismatch warning embedded in the evidence pack itself — I've kept the template's `predicted_indications[0]` as the report subject per your spec, but flagged this prominently rather than glossing over it, and pointed to the stronger-evidence alternative (`B-cell neoplasm`, rank 9) in the conclusion.

---

# Duvelisib: From CLL/SLL and Follicular Lymphoma to Hodgkin's Lymphoma

## One-Sentence Summary

Duvelisib is a dual PI3K-δ/γ inhibitor originally approved for relapsed/refractory chronic lymphocytic leukemia (CLL) / small lymphocytic lymphoma (SLL) and follicular lymphoma. The TxGNN model's top prediction points to **Hodgkin's Lymphoma**, but on closer inspection, the **11 clinical trials** and **16 publications** cited as supporting evidence almost all describe **Non-Hodgkin Lymphoma (NHL)** populations (indolent NHL, follicular lymphoma, CLL/SLL, PTCL) rather than classical Hodgkin lymphoma — no trial in this evidence set actually enrolls Hodgkin lymphoma patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory CLL/SLL and relapsed/refractory follicular lymphoma (drawn from cited literature, e.g. PMID 30430368, 38423708 — no Taiwan-specific approved indication text is on file) |
| Predicted New Indication | Hodgkin's Lymphoma ⚠️ (see mismatch caveat below) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap (DG002) in this evidence pack. Based on information available in the cited literature, Duvelisib is a small-molecule, orally administered dual inhibitor of phosphoinositide 3-kinase delta and gamma (PI3K-δ/γ) (PMID 30430368, 38423708). It blocks B-cell receptor (BCR) signaling and disrupts PI3Kγ-mediated tumor microenvironment support, a mechanism central to several B-cell and T-cell lymphoid malignancies. Its efficacy in CLL/SLL and follicular lymphoma is well established (first global approval 2018, per PMID 30430368), and mechanistically this BCR/PI3K-pathway dependency is shared broadly across lymphoid neoplasms.

**However, the repurposing rationale for classical Hodgkin lymphoma specifically is weak.** The evidence pack's own analysis flags this: *"⚠️ Disease entity mismatch: the 11 trials and most literature listed here actually target Non-Hodgkin Lymphoma (indolent NHL, follicular lymphoma, CLL/SLL) rather than classical Hodgkin lymphoma — the two differ fundamentally in pathophysiology and treatment target (cHL is defined by Reed-Sternberg cells and PD-1/PD-L1-driven immune escape, not the atypical B-cell BCR-signaling dependency seen in NHL). No trial in this set directly enrolls Hodgkin lymphoma patients."* This should be treated as a probable data-labeling error (NHL/HL name confusion) rather than a genuine mechanistic signal, and the mechanistic extrapolation to Hodgkin lymphoma remains unsupported by direct evidence.

By contrast, the evidence pack's rank-9 candidate, **B-cell neoplasm**, is supported by a completed Phase 3 pivotal trial (NCT02004522, the DUO trial) and reflects Duvelisib's actual approved indication space — this is a substantially stronger, evidence-backed repurposing signal than the Hodgkin lymphoma prediction (see Conclusion).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04379167](https://clinicaltrials.gov/study/NCT04379167) | Phase 2 | Unknown | 140 | Single-arm study of YY-20394 (a duvelisib analog) in relapsed/refractory follicular NHL. Grade C — status unknown, population not confirmed as classical HL. |
| [NCT05923502](https://clinicaltrials.gov/study/NCT05923502) | N/A | Not Yet Recruiting | 200 | Real-world observational study (CHANT) of Duvelisib capsules in Non-Hodgkin's Lymphoma — explicitly NHL, not HL. |
| [NCT04803201](https://clinicaltrials.gov/study/NCT04803201) | Phase 2 | Suspended | 170 | Randomized study of chemo ± Duvelisib in CD30-negative peripheral T-cell lymphoma; suspended. |
| [NCT01882803](https://clinicaltrials.gov/study/NCT01882803) | Phase 2 | Completed | 129 | Duvelisib monotherapy in refractory indolent NHL. Grade C — title explicitly "Non-Hodgkin Lymphoma," disease entity does not match. |
| [NCT04038359](https://clinicaltrials.gov/study/NCT04038359) | Phase 2 | Completed | 103 | Compared two intermittent dosing schedules of Duvelisib in indolent NHL; dosing-schedule study, not HL-specific. |
| [NCT05044039](https://clinicaltrials.gov/study/NCT05044039) | Phase 1 | Active, Not Recruiting | 42 | Duvelisib following CAR T-cell therapy to improve CAR-T persistence in lymphoma post-CAR-T relapse; not HL-specific. |
| [NCT04836832](https://clinicaltrials.gov/study/NCT04836832) | Phase 1 | Withdrawn | 0 | Duvelisib + acalabrutinib in relapsed/refractory indolent NHL; withdrawn, no data generated. |
| [NCT02640833](https://clinicaltrials.gov/study/NCT02640833) | Phase 1 | Withdrawn | 0 | Duvelisib + venetoclax in relapsed/refractory CLL/SLL/NHL; withdrawn, no data generated. |
| [NCT05065866](https://clinicaltrials.gov/study/NCT05065866) | Phase 1 | Completed | 14 | Duvelisib + BMS-986345 dose-finding study in lymphoid malignancy. |
| [NCT01871675](https://clinicaltrials.gov/study/NCT01871675) | Phase 1 | Completed | 48 | Duvelisib (IPI-145) + rituximab or bendamustine/rituximab in relapsed/refractory lymphoma or CLL. |

*One additional trial (NCT02576275, Phase 3, Withdrawn, 0 enrolled) was excluded from this table as it generated no data.*

**None of the above trials enroll a classical Hodgkin lymphoma population.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36685572](https://pubmed.ncbi.nlm.nih.gov/36685572/) | 2022 | Systematic Review/Meta-analysis | Frontiers in Immunology | Meta-analysis of Duvelisib safety/efficacy across relapsed/refractory lymphoid neoplasm subtypes — covers NHL/CLL populations, not classical HL specifically. |
| [30799261](https://pubmed.ncbi.nlm.nih.gov/30799261/) | 2019 | Review | The Lancet. Oncology | Commentary on Duvelisib in indolent Non-Hodgkin lymphoma. |
| [31580408](https://pubmed.ncbi.nlm.nih.gov/31580408/) | 2019 | Review | Am J Health-Syst Pharm | Summarizes approved targeted therapies for B- and T-cell lymphomas, including Duvelisib. |
| [33616890](https://pubmed.ncbi.nlm.nih.gov/33616890/) | 2021 | Review | Drugs | Novel therapy approaches in follicular lymphoma, including PI3K inhibitors. |
| [32356174](https://pubmed.ncbi.nlm.nih.gov/32356174/) | 2020 | Review | Curr Treat Options Oncol | Reviews PI3K inhibitors (including Duvelisib) as targeted therapy in lymphoma generally; no HL-specific data. |
| [33132100](https://pubmed.ncbi.nlm.nih.gov/33132100/) | 2021 | Review | Clin Lymphoma Myeloma Leuk | Discusses next-generation PI3K inhibitors' potential in B-cell NHL. |
| [29191916](https://pubmed.ncbi.nlm.nih.gov/29191916/) | 2018 | Phase 1 clinical study | Blood | Original Phase 1 dose-escalation study establishing Duvelisib's clinical activity in advanced hematologic malignancies (CLL, NHL subtypes). |
| [36882482](https://pubmed.ncbi.nlm.nih.gov/36882482/) | 2023 | Preclinical/Mechanistic | Scientific Reports | Shows PI3Kγ/δ inhibition disrupts mantle cell lymphoma (an NHL subtype) proliferation and migration. |
| [27872741](https://pubmed.ncbi.nlm.nih.gov/27872741/) | 2016 | Review | Mediterr J Hematol Infect Dis | Reviews novel drugs, including PI3K inhibitors, in follicular lymphoma. |
| [32658557](https://pubmed.ncbi.nlm.nih.gov/32658557/) | 2020 | Review | Future Oncology | Reviews PI3K-class inhibitor use in Non-Hodgkin lymphoma. |

**No publication in this evidence set specifically studies classical Hodgkin lymphoma.**

---

## Taiwan Market Information

Duvelisib currently holds **no marketing authorization in Taiwan** (`market_status`: 未上市 / Not Marketed; `total_licenses`: 0). No license records are available to tabulate.

---

## Cytotoxicity

Duvelisib is an antineoplastic agent (approved for hematologic malignancies — CLL/SLL, follicular lymphoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (small-molecule PI3K-δ/γ dual inhibitor) — not a conventional cytotoxic chemotherapeutic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (no quantified toxicity data in this evidence pack; the literature notes PI3K inhibitors as a class carry a "severe toxicity profile" that has led to restricted use — PMID 35899388, 33275709) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all listed as data gaps in this evidence pack; DG001 — TFDA package insert warnings/contraindications — is flagged as a **Blocking** gap, meaning this candidate cannot proceed to the S1 safety pre-screen until resolved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence cited for the Hodgkin lymphoma prediction is built almost entirely on Non-Hodgkin Lymphoma trials and literature — a probable disease-entity mislabeling rather than genuine mechanistic support — leaving the actual HL-specific evidence base at essentially zero. Combined with a Blocking safety data gap (no TFDA package insert on file) and no Taiwan market presence, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Verify and correct the disease-entity labeling on the NCT/PMID records currently mapped to "Hodgkin's Lymphoma" (likely an NHL/HL confusion) before re-scoring this candidate
- Obtain the TFDA package insert (warnings, contraindications) to close Blocking gap DG001 and enable the S1 safety pre-screen
- Obtain confirmed mechanism-of-action documentation from DrugBank to close High-severity gap DG002
- If genuine interest in Hodgkin lymphoma remains, a dedicated early-phase trial enrolling a confirmed classical HL population would be required — no such trial currently exists
- **Recommend evaluating rank-9 "B-cell neoplasm" as the priority candidate instead** — it is supported by L1 evidence (completed Phase 3 DUO trial, NCT02004522) and aligns with Duvelisib's already-established global approval in CLL/SLL and follicular lymphoma, making it a substantially stronger repurposing case within this same evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

