---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Pregnancy and Lactation-Associated Osteoporosis

## One-Sentence Summary

> Teriparatide (recombinant human PTH 1-34) is an anabolic bone agent originally developed for osteoporosis treatment (marketed as Forteo).
> Among 10 TxGNN-predicted indications, the top-ranked candidate (duodenal ulcer) lacks any mechanistic or clinical support, so this report focuses on the most clinically defensible candidate — **Pregnancy and Lactation-Associated Osteoporosis (PLO)** —
> supported by **2 clinical trials** (mechanistic evidence) and **19 publications**, including case series and systematic reviews of off-label teriparatide use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis (inferred from drug identity; not populated in `original_indications`, see data gap below) |
| Predicted New Indication | Pregnancy and Lactation-Associated Osteoporosis (PLO) |
| TxGNN Prediction Score | 99.55% (rank #8 among 10 candidates by score, but strongest by evidence) |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on ranking:** The model's #1-ranked prediction (duodenal ulcer, score 99.86%) and most other top-10 candidates (esophageal malformation, duodenal obstruction, Worth syndrome, SCOT deficiency, etc.) have **no clinical trials, no literature, and the evidence pack's own rationale explicitly states there is no known mechanistic link**. This report evaluates PLO instead because it is the only candidate with substantive supporting evidence.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (DG002). Based on known pharmacology and supporting trial data (NCT00277706 confirms teriparatide's approved anabolic bone-building action), teriparatide is a PTH(1-34) analog that stimulates osteoblast activity and promotes new bone formation — distinguishing it from antiresorptive agents (bisphosphonates, denosumab) that only slow bone loss.

PLO is a rare condition of rapid bone loss occurring in late pregnancy or the postpartum/lactation period, presenting with vertebral fragility fractures. Its underlying pathophysiology — an imbalance favoring bone resorption over formation — overlaps with the pathophysiology of postmenopausal osteoporosis, teriparatide's proven original indication.

Because teriparatide directly stimulates bone formation, it is mechanistically well-suited to reverse the rapid bone loss seen in PLO. This is reflected in the literature: multiple retrospective cohorts and case series (e.g., PMID 34132853, 35903718) report improved bone mineral density with teriparatide in PLO patients, and reviews (e.g., PMID 28084543) identify teriparatide as one of the preferred off-label treatment options. However, no randomized controlled trial has been conducted in this population, and safety in the peripartum/lactation context requires careful evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02440581](https://clinicaltrials.gov/study/NCT02440581) | N/A | Completed | 141 | Studied renal osteodystrophy (CKD-related bone loss), not PLO directly; relevance graded C — indirect support for teriparatide's role in metabolic bone disease. |
| [NCT00277706](https://clinicaltrials.gov/study/NCT00277706) | Phase 1 | Completed | 40 | Confirmed PTH(1-34)'s osteogenic effect on oral bone regeneration; relevance graded C — mechanistic support only, not PLO population. |

*Note: No trials have been conducted specifically in the PLO population; both listed trials provide indirect mechanistic support only.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40205203](https://pubmed.ncbi.nlm.nih.gov/40205203/) | 2025 | Systematic Review/Meta-analysis | Osteoporosis International | 35 studies, 943 patients with pregnancy-associated osteoporosis; treatment response analysis inconclusive due to limited data. |
| [37708365](https://pubmed.ncbi.nlm.nih.gov/37708365/) | 2024 | Systematic Review/Meta-analysis | J Clin Endocrinol Metab | Compared therapeutic interventions for PLO; optimal management still undefined. |
| [34132853](https://pubmed.ncbi.nlm.nih.gov/34132853/) | 2021 | Retrospective Cohort/Case Series | Calcified Tissue International | 19 PLO patients treated with teriparatide vs. conventional management; assessed BMD and trabecular bone score outcomes. |
| [35903718](https://pubmed.ncbi.nlm.nih.gov/35903718/) | 2022 | Case Series | Geburtshilfe und Frauenheilkunde | 47 women with PLO and vertebral fractures treated with teriparatide; assessed effect on subsequent fracture and BMD. |
| [34037833](https://pubmed.ncbi.nlm.nih.gov/34037833/) | 2021 | Retrospective Cohort | Calcified Tissue International | Evaluated BMD after teriparatide discontinuation with/without sequential antiresorptive therapy in PLO. |
| [39008200](https://pubmed.ncbi.nlm.nih.gov/39008200/) | 2024 | Review | Endocrine | Reviews effective strategies for PLO with specific focus on teriparatide use. |
| [36764958](https://pubmed.ncbi.nlm.nih.gov/36764958/) | 2023 | Case Report | Calcified Tissue International | Bone microarchitecture/strength changes during combined teriparatide and zoledronic acid treatment in severe PLO. |
| [33620518](https://pubmed.ncbi.nlm.nih.gov/33620518/) | 2022 | Review | Calcified Tissue International | Overview of PLO pathophysiology, diagnosis, and treatment landscape. |
| [28084543](https://pubmed.ncbi.nlm.nih.gov/28084543/) | 2017 | Review | Zeitschrift für Rheumatologie | Identifies teriparatide and bisphosphonates as the best treatment options for PLO based on ~100 published cases. |
| [39156353](https://pubmed.ncbi.nlm.nih.gov/39156353/) | 2024 | Case Report | Cureus | Successful subsequent pregnancy after teriparatide treatment for PLO. |

---

## Norway Market Information

Teriparatide is currently **not marketed in Norway** (0 authorizations on record). No license data is available to summarize product names, dosage forms, or approved indications.

---

## Safety Considerations

Please refer to the package insert for safety information (`key_warnings`, `contraindications`, and DDI data are all marked as data gaps — DG001, Blocking severity).

**Additional signal from literature (not part of formal safety dataset):** Two case reports (PMID 26992073) describe worsening of calcinosis cutis in osteoporosis patients with autoimmune disease (dermatomyositis, CREST syndrome) following teriparatide treatment — a signal worth flagging for pharmacist review, though not yet reflected in formal labeling data available to this evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the PLO indication specifically)

**Rationale:**
Teriparatide's anabolic mechanism is well-matched to PLO's rapid bone-loss pathophysiology, and multiple cohort studies, case series, and reviews support its off-label use with favorable BMD/fracture outcomes — but no RCT exists in this population, and the drug is not currently marketed in Norway. All other top-scoring TxGNN predictions (duodenal ulcer, esophageal malformation, Worth syndrome, etc.) should remain on **Hold**, as the evidence pack itself confirms no plausible mechanistic link or supporting evidence.

**To proceed, the following is needed:**
- TFDA/Norwegian label warnings and contraindications (Blocking data gap, DG001)
- Detailed MOA data from DrugBank (High-priority data gap, DG002)
- Regulatory pathway assessment given current unmarketed status in Norway
- Formal safety review of teriparatide use during pregnancy/lactation (including known class-level osteosarcoma boxed warning and the calcinosis cutis signal above)
- Prospective or registry-based studies in the PLO population to close the RCT evidence gap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

