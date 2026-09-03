---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia (G-CSF Supportive Care) to Primary Platelet Release Disorder

## One-Sentence Summary

> Filgrastim is a recombinant human G-CSF, clinically used to stimulate neutrophil recovery and mobilize hematopoietic stem cells in the supportive-care setting (e.g., around chemotherapy and stem cell transplantation).
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
> but the supporting evidence is weak — the **13 clinical trials** identified all use Filgrastim only as a supportive agent for stem cell mobilization/neutrophil recovery in unrelated transplant protocols, and only **1 publication** loosely touches on the topic, with no evidence directly evaluating Filgrastim for this indication.

> ⚠️ **Note on original indication**: The evidence pack does not contain a confirmed regulatory-approved indication text for Filgrastim (`original_indications` is empty, `original_moa` is a data gap). The "Neutropenia" framing above is inferred from repeated context in the trial relevance annotations (G-CSF used for "幹細胞動員/嗜中性球恢復") and should be confirmed against an authoritative label before use in any external-facing document.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in evidence pack (regulatory data gap) — G-CSF is contextually referenced as supporting neutrophil recovery/stem cell mobilization |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.99% (rank 48 among all predictions) |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a **High-severity data gap** in the evidence pack). Based on the contextual information available, Filgrastim is a recombinant granulocyte colony-stimulating factor (G-CSF) whose known pharmacology is to stimulate proliferation and differentiation of granulocyte precursor cells and to mobilize hematopoietic stem cells — a mechanism used clinically to support neutrophil recovery after myelosuppressive therapy and to mobilize stem cells before transplantation.

Primary release disorder of platelets, by contrast, is a defect in platelet granule secretion machinery (pathways such as ADP/TXA2 signaling and granule exocytosis). The evidence pack's own mechanistic analysis states explicitly that there is **no direct biological link** between G-CSF signaling and platelet granule release pathways. The high TxGNN score most likely reflects an indirect association learned from the knowledge graph — both concepts cluster under broad "hematologic disease/hematopoiesis" nodes — rather than a genuine shared mechanism.

Consistent with this, all 13 clinical trials retrieved for this indication are studies of allogeneic/autologous hematopoietic stem cell transplantation for unrelated conditions (leukemia, lymphoma, sarcoma, MS, SLE, COVID-19), in which Filgrastim/G-CSF appears only as a supportive-care agent for stem cell mobilization or post-transplant neutrophil recovery — not as an investigational treatment for platelet release disorders. Several trials were explicitly graded "C" (low relevance) during triage. This prediction should be treated as **hypothesis-generating only**, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Phase 2 | Terminated | 200 | Unrelated donor HSCT for hematologic malignancies; G-CSF used for stem cell mobilization/neutrophil recovery, not for platelet disorders (graded low relevance) |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic HSCT for pediatric sarcomas; G-CSF as supportive agent only (graded low relevance) |
| [NCT00354172](https://clinicaltrials.gov/study/NCT00354172) | Phase 2 | Terminated | 16 | Umbilical cord blood transplant + NK cells for myeloid leukemia not in remission |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT for patients with GATA2 mutations |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs. unselected autologous HSCT in MCL/DLBCL; G-CSF used for stem cell collection (graded low relevance) |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Post-transplant cyclophosphamide + sirolimus/MMF for GVHD prophylaxis after PBSCT |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved HLA-mismatched unrelated donor bone marrow transplant with PTCy |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Autologous HSCT for severe systemic lupus erythematosus |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile (NLRP3 inhibitor) for moderate COVID-19/cytokine release syndrome (unrelated to Filgrastim mechanism) |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Post-transplant cyclophosphamide-based GVHD prophylaxis in mismatched unrelated donor PBSCT |

**None of the above trials directly evaluate Filgrastim as a treatment for platelet release disorders; all identified uses are supportive-care/stem cell mobilization in unrelated transplant contexts.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohort study | Frontiers in Immunology | G-CSF mobilization in healthy stem cell donors preferentially mobilizes lymphocyte subsets; does not address platelet granule release function |

---

## Norway Market Information

Filgrastim is currently **not marketed in Norway** (0 authorizations on record). No product license or approved indication text is available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important flag**: The evidence pack marks TFDA/product-label warnings and contraindications as a **Blocking-severity data gap** — this must be resolved (via TFDA label retrieval and parsing) before any safety assessment (S1 stage) can proceed. Drug interaction data was also queried with no results found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the evidence pack's own mechanistic and clinical-trial review finds no direct biological or clinical link between Filgrastim's known G-CSF activity and platelet granule release disorders — all retrieved trials use Filgrastim only as a supportive agent in unrelated transplant protocols, and only one loosely related observational study exists. Combined with a Blocking-severity gap in safety/label data, this candidate does not meet the bar to advance beyond signal detection (S0).

**To proceed, the following is needed:**
- Retrieve and parse the official TFDA/product label for warnings, contraindications, and DDI (Blocking gap, DG001)
- Obtain confirmed mechanism-of-action and approved-indication data from DrugBank (High-severity gap, DG002)
- Seek preclinical or mechanistic evidence directly linking G-CSF/granulocyte signaling to platelet granule secretion pathways, if such a hypothesis is to be pursued further
- Re-triage the "pending" relevance-graded trials to confirm none provide direct evidence before any re-evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

