---
layout: default
title: Nitisinone
parent: 僅模型預測 (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
---

# Nitisinone
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

# Nitisinone: From Hereditary Tyrosinemia Type 1 to Renal Tubular Acidosis

## One-Sentence Summary

Nitisinone (NTBC) was originally developed to treat **hereditary tyrosinemia type 1 (HT-1)**, a rare inherited metabolic disorder, by blocking the enzyme that generates toxic tyrosine-degradation byproducts. The TxGNN model predicts it may also be effective for **Renal Tubular Acidosis**, a known renal complication of untreated HT-1, with **0 clinical trials** but **2 supporting publications** (a cohort study and a case series) currently available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary Tyrosinemia Type 1 (HT-1) *(inferred from repurposing rationale text; no formal license record exists — drug is not marketed in Norway)* |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The formal mechanism-of-action field for nitisinone is currently a data gap in this evidence pack. However, the repurposing rationale attached to this prediction indicates that nitisinone (NTBC) acts by inhibiting **4-hydroxyphenylpyruvate dioxygenase (HPPD)**, an enzyme upstream in the tyrosine degradation pathway. By blocking this enzyme, nitisinone prevents the formation of toxic downstream metabolites — most notably succinylacetone — which are responsible for the liver and kidney damage seen in HT-1.

Renal tubular acidosis and broader proximal renal tubular dysfunction are well-recognized complications of **untreated or inadequately treated HT-1**, arising directly from succinylacetone-mediated toxicity to the proximal tubule. Because nitisinone's original approved use already targets the root metabolic defect that causes this renal damage, the predicted new indication is not a novel mechanistic extrapolation — it represents treatment of a **downstream complication of the drug's own original indication**.

This gives the prediction a comparatively high degree of mechanistic plausibility relative to other TxGNN outputs for this drug: the pathway linking cause (toxic metabolite accumulation) and effect (tubular injury) is already established in the HT-1 literature, and nitisinone's core pharmacology (HPPD inhibition) directly addresses that cause.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25172236](https://pubmed.ncbi.nlm.nih.gov/25172236/) | 2014 | Cohort | Molecular Genetics and Metabolism | Describes the early effect of NTBC on renal tubular dysfunction in patients with hereditary tyrosinemia type 1, finding that NTBC therapy is associated with improvement in tubular function markers. |
| [27109516](https://pubmed.ncbi.nlm.nih.gov/27109516/) | 2016 | Case Series | Indian Journal of Gastroenterology | Case series of four children with tyrosinemia type 1 treated with NTBC; three of four showed sustained normal liver function and undetectable urine succinylacetone over ~3 years of therapy, consistent with reduced tubular toxin burden. |

---

## Norway Market Information

Nitisinone currently holds **no marketing authorization in Norway** (market status: not marketed; 0 authorizations on record), so no product/authorization table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data are currently marked as data gaps in this evidence pack — notably, TFDA package insert retrieval (DG001) is flagged as a **Blocking** severity gap that must be resolved before any formal safety assessment (S1 stage) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between nitisinone's established pharmacology (HPPD inhibition, blocking toxic tyrosine-pathway metabolites) and renal tubular acidosis as a downstream HT-1 complication is biologically coherent and supported by two independent publications (a cohort study and a case series) showing renal tubular improvement with NTBC treatment. However, no dedicated clinical trials have directly tested nitisinone for this indication, and evidence remains observational (L3).

**To proceed, the following is needed:**
- TFDA/package insert data on warnings and contraindications (currently a **Blocking** data gap — DG001) to complete the S1 safety pre-assessment
- Formal mechanism-of-action documentation from DrugBank (data gap — DG002) to confirm and strengthen the mechanistic rationale
- Prospective or controlled studies specifically evaluating renal tubular function as a primary outcome in NTBC-treated HT-1 patients
- Norway-specific regulatory pathway assessment, given the drug currently holds no marketing authorization there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

