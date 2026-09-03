---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart is a rapid-acting human insulin analogue already used to control blood glucose in people with diabetes mellitus.
The TxGNN model's top prediction is **Type 1 Diabetes Mellitus**, supported by **69 clinical trials** and **20 publications**.
However, this is the drug's already-established core indication rather than a novel repurposing signal — see the caveat below.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (Type 1 and Type 2) — per literature evidence (e.g. PMID [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/)); no Norway license record exists to confirm the formal indication text |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs, e.g. NCT02546401, NCT00474045, NCT00312156, NCT00046150) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information, insulin aspart is a rapid-acting human insulin analogue (a single amino-acid substitution at position B28 of human insulin), and its efficacy in lowering postprandial glucose in diabetes mellitus is already well established and extensively documented in the literature and clinical trial record provided in this evidence pack.

**Important caveat:** Unlike a typical repurposing candidate, TxGNN's top-ranked prediction here — "Type 1 Diabetes Mellitus" — is not a *new* indication. It is the drug's original, already-approved therapeutic use. This pattern is common when a drug-disease edge is already strongly represented in the knowledge graph used to train TxGNN: the model essentially reproduces a known association rather than surfacing a genuine repurposing hypothesis. The large volume of Phase 3 RCTs and reviews confirms the *known* indication, but it should not be read as evidence for a novel use.

Genuinely novel candidates on this list — such as rank 2 "autoimmune oophoritis," rank 3 "opsismodysplasia," rank 6/7 stiff person syndrome variants — currently have **no clinical trial or literature support at all**, so they cannot yet be evaluated. Rank 8 "pancreatic agenesis" and rank 5 "permanent neonatal diabetes mellitus" are mechanistically closer to a true rare-disease repurposing story (insulin is already used off-label in neonatal diabetes syndromes) but only have 1–2 supporting publications each, insufficient for a formal evidence tier above L4.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02546401](https://clinicaltrials.gov/study/NCT02546401) | Phase 3 | Completed | 22 | Pre- vs post-meal bolus timing of insulin aspart in T1D patients on insulin pump |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Insulin detemir vs NPH insulin, both combined with insulin aspart bolus, in pregnant women with T1D |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Insulin detemir vs NPH insulin with mealtime insulin aspart in children/adolescents with T1D |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Completed | 59 | HMR1964 vs insulin aspart safety in CSII pumps for T1D |
| [NCT00992537](https://clinicaltrials.gov/study/NCT00992537) | Phase 1 | Completed | 27 | PK/PD comparison of IDegAsp vs IDeg vs insulin aspart in T1D |
| [NCT01464099](https://clinicaltrials.gov/study/NCT01464099) | Phase 1 | Completed | 24 | Bioequivalence of NovoLog 100 U/mL vs 200 U/mL formulations in T1D |
| [NCT03436498](https://clinicaltrials.gov/study/NCT03436498) | Phase 1 | Completed | 45 | Safety of SAR341402 vs NovoLog in CSII pumps in adults with T1D |
| [NCT00607087](https://clinicaltrials.gov/study/NCT00607087) | Phase 4 | Completed | 289 | Insulin glulisine vs aspart vs lispro via CSII pump parameters in T1D |
| [NCT02568280](https://clinicaltrials.gov/study/NCT02568280) | Phase 1 | Completed | 42 | Postprandial glucose metabolism with faster-acting insulin aspart in T1D |
| [NCT00095446](https://clinicaltrials.gov/study/NCT00095446) | Phase 4 | Completed | 513 | External CSII with insulin aspart vs insulin lispro in T1D and insulin-requiring T2D |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT (Phase 3a) | Lancet | ONWARDS 6: once-weekly insulin icodec vs once-daily degludec, both with insulin aspart bolus, in T1D |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: insulin degludec vs detemir, both with insulin aspart, in pregnant women with T1D |
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast: faster-acting insulin aspart vs insulin aspart in T1D/T2D pregnancy and post-delivery |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systematic Review | Diabetes Metab | Efficacy/safety of insulin aspart vs regular human insulin in T1D and T2D |
| [35746893](https://pubmed.ncbi.nlm.nih.gov/35746893/) | 2023 | Meta-Analysis | Diabetes Metab J | Faster-acting aspart vs aspart via insulin pump in T1D |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | General review of Type 1 Diabetes pathophysiology and management |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Management of T1D in pregnancy: lifestyle, pharmacotherapy, technology |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treat Endocrinol | Spotlight review of insulin aspart in T1D and T2D |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | Comprehensive review of insulin aspart's role in T1D and T2D management |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vasc Health Risk Manag | Insulin degludec/aspart combination for T1D and T2D |

## Norway Market Information

Currently no marketing authorization on record — insulin aspart is not marketed in Norway per the available regulatory data (`market_status: 未上市`, `total_licenses: 0`).

## Safety Considerations

Please refer to the package insert for safety information. **Note:** data gap DG001 (TFDA/label warnings and contraindications) is flagged as *Blocking* in the evidence pack — this prevents a formal S1 safety pre-assessment and must be resolved before any decision beyond Hold.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction ("Type 1 Diabetes Mellitus") duplicates insulin aspart's already-established core indication rather than representing a novel repurposing opportunity, so it delivers limited incremental value. In addition, a blocking data gap (missing product label/safety warnings, DG001) and missing MOA data (DG002) prevent a proper safety pre-assessment, and the drug currently has no marketing authorization in Norway.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse official product label warnings/contraindications
- Resolve DG002: confirm mechanism of action via DrugBank API
- Re-scope the repurposing question toward lower-ranked, genuinely novel candidates (e.g. permanent neonatal diabetes mellitus, pancreatic agenesis) and gather dedicated clinical/literature evidence for those, since they currently have only 1–2 supporting publications each
- Clarify Norway market/licensing pathway, since the drug is not currently marketed there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

