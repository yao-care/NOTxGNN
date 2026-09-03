---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Diabetes Mellitus (Original Indication Not Recorded) to Type 1 Diabetes Mellitus — Data Gap Flagged, Not a Genuine Repurposing Signal

## One-Sentence Summary

Insulin detemir (DrugBank DB01307, marketed globally as Levemir) is a long-acting basal insulin analogue already used to treat type 1 and type 2 diabetes. The TxGNN model's top prediction — **Type 1 Diabetes Mellitus** — is not a new indication at all; it is the drug's own well-established, already-approved use. This candidate exists only because the evidence pack's `original_indications` field is empty and `market_status` incorrectly shows "not marketed," which are data gaps in the source registry rather than a genuine repurposing discovery. **34 clinical trials** and **20 publications** support insulin detemir's efficacy in type 1 diabetes — but as confirmation of known use, not as new-indication evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (registry data gap). Publicly, insulin detemir (Levemir) is indicated for type 1 and type 2 diabetes mellitus. |
| Predicted "New" Indication | Type 1 diabetes mellitus — **identical to the drug's real-world established use** |
| TxGNN Prediction Score | 99.77% (rank 2954) |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) — reflects existing-use evidence, not novel-indication evidence |
| Norway Market Status | 未上市 (Not marketed) — flagged as likely inaccurate given Levemir's known global marketing history |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (pending data verification) |

## Why is This Prediction Reasonable?

Mechanistically, insulin detemir is straightforward: it is a soluble, long-acting human insulin analogue acylated with a 14-carbon fatty acid, which reversibly binds albumin to provide slow, prolonged absorption. This directly replaces the endogenous insulin deficiency that defines type 1 diabetes mellitus (T1DM), which is why it makes pharmacological sense — because it is already the standard basal insulin therapy for T1DM, not because TxGNN uncovered a novel mechanistic link.

This is the central issue with this candidate: the "original indication → new indication" relationship the report template expects does not exist here. The evidence pack itself flags this in `repurposing_rationale`: *"此為藥物之原始核准適應症（非老藥新用候選）"* — this is the drug's original approved indication, not a repurposing candidate. The high TxGNN score and abundant clinical/literature evidence reflect the strength of insulin detemir's established use in T1DM, not the discovery of a new therapeutic avenue.

Two data gaps in the source pack likely caused this false-positive framing: (1) `original_indications` is empty, so the pipeline had no baseline indication to compare against, and (2) `market_status` shows "not marketed" with zero licenses, which is inconsistent with Levemir's known international market presence. Both should be corrected at the source (DrugBank/national regulatory registry) before this drug is evaluated further in any repurposing workflow.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Insulin detemir vs NPH insulin (both + aspart) in pregnant women with T1DM; glycemic control and safety comparison |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | Completed | 347 | Detemir vs NPH insulin in children/adolescents with T1DM, once or twice daily + mealtime aspart |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | Efficacy/safety of detemir (2400 nmol/mL formulation) vs NPH in T1DM basal-bolus regimen |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | Completed | 598 | Detemir + aspart vs NPH + human soluble insulin in T1DM basal-bolus regimen |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Phase 4 | Completed | 520 | Once-daily vs twice-daily detemir + aspart in T1DM: HbA1c, hypoglycemia, weight |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | Completed | 114 | Detemir + aspart vs NPH + aspart in adults with T1DM |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Degludec/aspart vs detemir once/twice daily + aspart in children/adolescents with T1DM |
| [NCT00655200](https://clinicaltrials.gov/study/NCT00655200) | N/A (observational) | Completed | 2286 | Post-marketing safety/tolerability of Levemir (detemir) in Filipino T1DM/T2DM patients |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Phase 3 | Completed | 26 | Dapagliflozin add-on to liraglutide + insulin (incl. detemir as background) in T1DM |
| [NCT00591227](https://clinicaltrials.gov/study/NCT00591227) | Phase 4 | Completed | 176 | ED-initiated basal-bolus insulin (incl. detemir) for hyperglycemia management |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: degludec vs detemir (both + aspart) in pregnant women with T1DM, non-inferiority design |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review/Network Meta-analysis | Value Health | Comparative efficacy/safety of basal insulin regimens (incl. detemir) in adults with T1DM |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane Systematic Review | Cochrane Database Syst Rev | Review of (ultra-)long-acting insulin analogues, including detemir, for T1DM |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic Review/Meta-analysis | Pol Arch Med Wewn | Detemir vs NPH insulin in T1DM: glycemic control outcomes |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review/Meta-analysis | Clin Ther | Degludec vs other long-acting basal analogues (glargine, detemir) in T1D/T2D |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Management of T1DM in pregnancy: lifestyle, pharmacological treatment, technology |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Insulin detemir: review of use in T1DM and T2DM management |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Update on T1DM/T2DM treatment, focus on insulin detemir |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Insulin detemir in the treatment of T1DM and T2DM |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Review | BioDrugs | Spotlight on insulin detemir in T1DM and T2DM |

## Norway Market Information

No marketing authorization records are present in this evidence pack (`total_licenses = 0`, `market_status = 未上市/Not marketed`). This is flagged as a likely **data gap rather than fact**: insulin detemir (Levemir, Novo Nordisk) has a long-standing global marketing history including in European markets. Before any downstream decision is made on this candidate, the Norwegian Medicines Agency (Legemiddelverket) register should be checked directly to confirm actual market status and authorization numbers.

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and DDI data are all unavailable in this evidence pack — DG001 is flagged as a **Blocking** data gap that prevents S1 safety pre-assessment.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is not a genuine repurposing candidate — the "predicted new indication" (T1DM) is insulin detemir's own established, already-approved use. The high TxGNN score and rich evidence base confirm known pharmacology rather than reveal anything new. Proceeding under a "Proceed with Guardrails" label (as the raw scoring engine suggests) would risk misrepresenting a data-pipeline artifact as a discovery. Additionally, DG001 (missing TFDA/regulatory label warnings and contraindications) is a **Blocking** gap that independently prevents any safety pre-assessment (S1) regardless of indication novelty.

**To proceed, the following is needed:**
- Correct the `original_indications` field at the source (DrugBank) so insulin detemir is not re-flagged as a "new" T1DM candidate
- Verify actual Norway/EU market status and authorization numbers directly against Legemiddelverket, since `market_status = 未上市` appears inconsistent with Levemir's known marketing history
- Retrieve TFDA/EMA package insert warnings and contraindications (DG001) before any safety-stage evaluation
- Retrieve DrugBank MOA record (DG002) to support future mechanistic analyses
- For lower-ranked candidates in this batch (autoimmune oophoritis, opsismodysplasia, stiff person syndrome, drug-induced lipodystrophy, etc.), no further action is warranted: these are flagged in the source rationale as comorbidity confounding or reversed-causality artifacts (e.g., lipodystrophy is a known adverse effect of insulin injection, not a treatable indication) rather than credible repurposing signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

