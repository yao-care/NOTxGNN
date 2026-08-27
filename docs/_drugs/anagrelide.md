---
layout: default
title: Anagrelide
parent: 僅模型預測 (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
---

# Anagrelide
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

# Anagrelide: From Essential Thrombocythemia to Reactive Thrombocytosis

## One-Sentence Summary

Anagrelide is a platelet-lowering agent whose established use, as reflected in the supporting literature, is the management of clonal thrombocytosis in myeloproliferative neoplasms such as essential thrombocythemia (ET). The TxGNN model predicts it may also be effective for **Reactive Thrombocytosis**, but this direction is currently supported only by **0 clinical trials** and **10 mechanism/review-level publications**, none of which directly studies anagrelide in a reactive (non-clonal) thrombocytosis population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from local regulatory licenses (drug not marketed locally). Based on the supporting literature, anagrelide's established use is platelet-count reduction in essential thrombocythemia (ET) / clonal thrombocytosis. |
| Predicted New Indication | Reactive Thrombocytosis |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 |
| Norway Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the structured DrugBank field (flagged as data gap DG002, High severity). Based on information reflected in the supporting literature (notably PMID 15270658, *"Anagrelide: an update on its mechanisms of action and therapeutic potential"*), anagrelide is understood as a platelet-lowering agent that suppresses megakaryocyte maturation and thereby reduces platelet production. Its efficacy for reducing elevated platelet counts in essential thrombocythemia and related myeloproliferative disorders is well established in the literature base.

Essential thrombocythemia and reactive thrombocytosis both present clinically as elevated platelet counts, but they differ fundamentally in etiology: ET is a clonal stem cell disorder, whereas reactive thrombocytosis is typically secondary to infection, inflammation, splenectomy, or other transient triggers, and is generally self-limiting. Several of the retrieved publications (e.g., PMID 10494240, 7783354, 17171694) explicitly discuss the differential diagnosis between these two entities, which is consistent with the TxGNN model surfacing anagrelide via shared platelet-count phenotype rather than shared disease biology.

Mechanistically, anagrelide's inhibition of megakaryocyte maturation is not intrinsically restricted to clonal disease, which is the plausible basis for the model's prediction. However, this is a theoretical extrapolation: none of the 10 retrieved publications report anagrelide use, efficacy, or safety data specifically in a reactive thrombocytosis population, and clinical practice generally does not recommend cytoreductive therapy for reactive thrombocytosis, since the condition is usually transient and carries a much lower thrombotic risk than clonal thrombocytosis. This gap between mechanistic plausibility and the absence of population-specific evidence is the central limitation of this prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15270658](https://pubmed.ncbi.nlm.nih.gov/15270658/) | 2004 | Review | Expert Review of Anticancer Therapy | Overview of anagrelide's mechanism of action and therapeutic potential in clonal thrombocytosis; distinguishes clonal from reactive thrombocytosis, the latter not requiring therapy. |
| [16019501](https://pubmed.ncbi.nlm.nih.gov/16019501/) | 2005 | Review | Leukemia & Lymphoma | Critical review of anagrelide therapy in essential thrombocythemia and related disorders; reactive thrombocytosis noted as generally inconsequential and not requiring cytoreduction. |
| [10494240](https://pubmed.ncbi.nlm.nih.gov/10494240/) | 1999 | Review | The Medical Journal of Australia | Diagnosis of essential thrombocythaemia depends on excluding other myeloproliferative disorders and reactive thrombocytosis; outlines platelet-lowering therapy thresholds. |
| [7783354](https://pubmed.ncbi.nlm.nih.gov/7783354/) | 1995 | Review | Rinsho Ketsueki (Jpn J Clin Hematol) | Discusses differential diagnosis of ET from reactive thrombocytosis and reviews megakaryocyte-suppressing agents including anagrelide. |
| [1994734](https://pubmed.ncbi.nlm.nih.gov/1994734/) | 1991 | Review | The American Journal of the Medical Sciences | Reviews the clinical spectrum of thrombocytosis and thrombocythemia and the cytokine regulation of platelet production. |
| [28380402](https://pubmed.ncbi.nlm.nih.gov/28380402/) | 2017 | Review | Leukemia Research | Case-based review of thrombocytapheresis for hyperthrombocytosis in myeloproliferative neoplasms; cytoreductive drug therapy discussed as mainstay management. |
| [17171694](https://pubmed.ncbi.nlm.nih.gov/17171694/) | 2007 | Cohort (Retrospective) | Pediatric Blood & Cancer | Retrospective analysis of 12 pediatric cases comparing essential versus reactive thrombocythemia, highlighting diagnostic and clinical course differences. |
| [27276864](https://pubmed.ncbi.nlm.nih.gov/27276864/) | 2016 | Case Report | Srpski Arhiv za Celokupno Lekarstvo | Case of ET with ankylosing spondylitis (a condition associated with reactive thrombocytosis) treated with anagrelide combined with DMARDs and etanercept. |
| [38455691](https://pubmed.ncbi.nlm.nih.gov/38455691/) | 2024 | Case Report | European Journal of Case Reports in Internal Medicine | Case of acute myocardial infarction in an ET patient treated with anagrelide, illustrating thrombotic risk management context for platelet-lowering therapy. |
| [29851840](https://pubmed.ncbi.nlm.nih.gov/29851840/) | 2018 | Case Report | Medicine | Case report on digital replantation in a patient with thrombocytosis after splenectomy (a reactive thrombocytosis scenario), addressing thrombosis risk management. |

---

## Norway Market Information

Anagrelide is currently **not marketed** in this jurisdiction (market status: 未上市) and has **0 registered authorizations**. No product/license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are currently available in the evidence pack — this is flagged as a **Blocking** data gap, DG001, preventing completion of the S1 safety screening stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction (score 99.83%, TxGNN rank 2305) reaches only evidence level L4 — supported by mechanism/review-level literature and case reports, with no clinical trials or population-specific studies in reactive thrombocytosis, and no direct evidence that anagrelide is effective or safe in this specifically self-limiting, non-clonal population. Current clinical practice does not generally support cytoreductive therapy for reactive thrombocytosis, which weighs against advancing this candidate without further investigation. A blocking data gap on official label safety information (DG001) also prevents completion of the S1 safety pre-screen required to move forward.

**To proceed, the following is needed:**
- TFDA (or local regulator) package insert data — warnings, contraindications, and DDI profile (Blocking, DG001)
- Confirmed mechanism of action from DrugBank API (High priority, DG002)
- Literature or translational studies evaluating anagrelide specifically in reactive (non-clonal) thrombocytosis populations, including risk-benefit versus watchful waiting
- Clarification of regulatory pathway, since the drug is not currently marketed locally (0 authorizations)

**Note on secondary prediction:** A second candidate indication, *inverse Klippel-Trenaunay syndrome* (TxGNN score 99.59%, rank 4816), was also flagged by the model but has no supporting clinical trials or literature, no clear mechanistic link to anagrelide's platelet-lowering action, and is scored L5/S0. It is not recommended for further evaluation at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

