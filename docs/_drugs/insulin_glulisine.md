---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus (General) to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Insulin glulisine (Apidra) is a rapid-acting human insulin analogue whose established clinical role is glycemic control in diabetes mellitus.
> The TxGNN model predicts it is effective for **Type 1 Diabetes Mellitus**, supported by **~70 clinical trials** and **20 publications**.
> **Important caveat:** this is not a novel repurposing signal — T1DM is already the drug's core, licensed use; the model has essentially re-identified its known indication rather than surfaced a new one.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not extractable from license data (data gap — no Norway licenses on file); by known pharmacology, insulin glulisine is used for glycemic control in diabetes mellitus |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails — but see caveat: this confirms established use, it is not a repurposing opportunity |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known pharmacology, insulin glulisine is a recombinant rapid-acting human insulin analogue (modified at B3/B29) that binds the insulin receptor to promote peripheral glucose uptake and suppress hepatic glucose output, mimicking physiological mealtime (bolus) insulin secretion.

Type 1 diabetes mellitus is characterized by absolute insulin deficiency due to autoimmune β-cell destruction; exogenous insulin replacement — including rapid-acting analogues like glulisine — is the foundational, guideline-standard treatment, not an emerging or repurposed use. The evidence pack's own repurposing rationale explicitly flags this: *"Insulin glulisine directly replaces the deficient insulin secretion in Type 1 diabetes patients; this is a core pharmacological action, not a drug repurposing scenario."*

Practically, this means the very large body of clinical trial and literature evidence below should be read as **validation of an already-established indication**, not discovery of a new one. The high TxGNN score and L1 evidence level reflect the strength of the drug-disease association in the underlying knowledge graph, which is expected and appropriate for a drug's primary indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00607087](https://clinicaltrials.gov/study/NCT00607087) | Phase 4 | Completed | 289 | Glulisine superior to aspart/lispro via CSII pump in reducing unexplained hyperglycemia and infusion-set occlusion in T1DM |
| [NCT00965549](https://clinicaltrials.gov/study/NCT00965549) | Phase 4 | Completed | 463 | Basal-plus-one glulisine regimen non-inferior to biphasic insulin for HbA1c control |
| [NCT00115570](https://clinicaltrials.gov/study/NCT00115570) | Phase 3 | Completed | 572 | Glulisine as safe/effective as lispro in children and adolescents with T1DM over 26 weeks |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | Glulisine non-inferior to lispro on HbA1c change in T1DM, 28-week study |
| [NCT00135096](https://clinicaltrials.gov/study/NCT00135096) | Phase 3 | Completed | 345 | Pre-meal vs post-meal glulisine dosing with glargine basal insulin, weight change outcomes |
| [NCT01204593](https://clinicaltrials.gov/study/NCT01204593) | Phase 4 | Completed | 206 | Glargine + glulisine basal-bolus therapy in previously uncontrolled T1DM patients |
| [NCT00545337](https://clinicaltrials.gov/study/NCT00545337) | Phase 3 | Completed | 60 | Efficacy/safety of glulisine with glargine basal insulin in T1DM (HbA1c, AE, labs) |
| [NCT00397553](https://clinicaltrials.gov/study/NCT00397553) | Phase 3 | Completed | 104 | Local efficacy/safety data for glulisine + glargine in T1DM |
| [NCT00539448](https://clinicaltrials.gov/study/NCT00539448) | Phase 4 | Completed | 98 | Open-label evaluation of glargine + glulisine dosing and safety in T1DM |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Phase 3 | Completed | 26 | Glulisine used as background insulin therapy while testing dapagliflozin add-on in T1DM |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Multicenter RCT comparing glulisine to lispro in adults with T1DM (n=672); comparable efficacy and safety |
| [41366610](https://pubmed.ncbi.nlm.nih.gov/41366610/) | 2026 | Phase III RCT | Diabetes Obes Metab | Biosimilar glulisine shows comparable immunogenicity, efficacy, and safety to originator in T1DM |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | Randomized crossover: glulisine vs aspart vs lispro via CSII in T1DM |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technol Ther | 26-week trial: glulisine comparable efficacy/safety to lispro in pediatric basal-bolus regimen |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | RCT | Diabetes Obes Metab | Glulisine vs lispro with glargine basal insulin in Japanese T1DM patients |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Comprehensive review of glulisine's role in diabetes management |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | PK/PD Study | Clin Pharmacokinet | Clinical PK/PD profile of glulisine vs regular human insulin |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK/PD Study | Diabetes Care | PK, postprandial glucose control, and safety of glulisine in pediatric T1DM |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Cohort | Pediatr Int | 1-year CSII use of glulisine improves post-meal glucose in pediatric T1DM |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Comparative Study | Acta Diabetol | Real-world comparison of glulisine, lispro, aspart via CSII pump in T1DM |

---

## Norway Market Information

No marketed authorizations are currently on file — **0 licenses**, market status **Not Marketed**. No product name, dosage form, or approved indication text is available in the evidence pack for Norway.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are currently available for this evidence pack; TFDA/Norway label data is flagged as a **blocking data gap**.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base is strong (L1 — multiple completed Phase 3 RCTs plus extensive Phase 4 and observational data) and unambiguously supports insulin glulisine's efficacy in Type 1 Diabetes Mellitus. However, this is **not a repurposing candidate** in the traditional sense — T1DM is the drug's established primary indication, and the TxGNN prediction essentially reconfirms known pharmacology rather than identifying a new therapeutic opportunity. The relevant "guardrail" here is regulatory, not clinical: the drug is not currently marketed in Norway.

**To proceed, the following is needed:**
- Obtain TFDA/Norway product label (warnings, contraindications, DDI) — currently a blocking data gap (DG001)
- Obtain formal MOA documentation from DrugBank (DG002)
- If commercial launch in Norway is the actual goal, this should be pursued as a standard **marketing authorization application** using the existing global T1DM evidence base, not as a repurposing workflow
- Lower-confidence signals (ranks 2–10: e.g. thiamine-responsive dysfunction syndrome, pancreatic agenesis) remain at L5/Research-Question or Hold status and would require dedicated literature/trial searches before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

