---
layout: default
title: Vortioxetine
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 5
---

# Vortioxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Vortioxetine: From Major Depressive Disorder to Neurotic Disorder

## One-Sentence Summary

> Vortioxetine is a multimodal serotonergic antidepressant, and literature in this evidence pack describes it as "currently approved for the treatment of major depressive disorder (MDD)."
> The TxGNN model's top-ranked prediction is **Neurotic Disorder**, an older, broad diagnostic term overlapping with the depressive/anxiety spectrum,
> currently supported by only **1 clinical trial** and **1 publication**. A closely related candidate in the same prediction set — **Neurotic Depression** — is essentially synonymous with MDD under older nomenclature and carries far stronger evidence (6 clinical trials, 20 publications, multiple Phase 3 RCTs).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) — per literature within this pack (PMID 29189941, 25016186); `original_moa`/`original_indications` fields are data gaps and not marketed in Norway, so no local license text is available |
| Predicted New Indication | Neurotic Disorder |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 (per pack scoring: single retrospective real-world trial, Grade C relevance + one Review, Tier 3) |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The `drug.original_moa` field is marked as a data gap. However, literature already collected in this evidence pack (Sanchez et al. 2015, PMID 25016186) describes vortioxetine's mechanism: it is a serotonin transporter (SERT) inhibitor with additional 5-HT1A receptor agonism, 5-HT1B partial agonism, and 5-HT3/5-HT7/5-HT1D receptor antagonism, which increases serotonergic, noradrenergic, dopaminergic, cholinergic, histaminergic, and glutamatergic neurotransmission in brain circuits implicated in mood and cognition.

"Neurotic disorder" is a broad, largely obsolete diagnostic umbrella (ICD-9-era terminology, not part of current DSM-5 nomenclature) that spans anxiety- and depression-adjacent presentations. Mechanistically, a multimodal serotonergic agent is plausible for this spectrum, but because the term itself lacks diagnostic specificity, the supporting evidence is thin and largely indirect — this is explicitly acknowledged in the pack's own `repurposing_rationale` for this candidate.

Notably, four of the five predicted indications in this pack (neurotic disorder, neurotic depression, melancholia, dysthymic disorder) all sit within the same depressive/neurotic-spectrum cluster, essentially re-detecting vortioxetine's known antidepressant profile through different historical naming conventions. Among these, **neurotic depression** (rank 2, score 99.09%) has by far the strongest clinical evidence — six trials including multiple completed Phase 3 RCTs, and 20 publications including systematic reviews and network meta-analyses in MDD — and should be treated as the practical anchor for this signal cluster. The fifth candidate, *benign paroxysmal torticollis of infancy*, is a pediatric paroxysmal disorder with no supporting trials or literature and is most plausibly model noise rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A | Completed | 370,212 | Large real-world retrospective claims-database cohort comparing medication utilization patterns and adverse-outcome risk across commonly used antidepressants; not designed specifically around a "neurotic disorder" diagnosis, so relevance is indirect (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Case-based review of "neurotic depression" treatment, noting the advantages of combining antidepressants with cognitive behavioral therapy. |

---

## Norway Market Information

Vortioxetine is currently **not marketed in Norway** (`market_status: 未上市`, `total_licenses: 0`); no authorization records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data are currently unavailable in this evidence pack (`DG001`, marked *Blocking* — TFDA/Norway package insert warnings and contraindications have not yet been retrieved, which prevents entry into the S1 safety pre-assessment stage).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked candidate, "Neurotic Disorder," is an imprecise legacy diagnostic term with only one indirect real-world trial and one case-review article — insufficient evidence to proceed on its own.
- Within the same prediction cluster, "Neurotic Depression" (L1/S3, "Proceed with Guardrails") is a far stronger, better-evidenced signal and is essentially equivalent to vortioxetine's known MDD indication under older nomenclature; it should be the priority target if this repurposing direction is pursued.

**To proceed, the following is needed:**
- Retrieve TFDA/Norway package insert warnings, contraindications, and DDI data (DG001, blocking) before any S1 safety assessment.
- Retrieve confirmed mechanism-of-action data from DrugBank (DG002).
- Clarify diagnostic mapping of legacy terms (neurotic disorder, neurotic depression, melancholia, dysthymic disorder) to current DSM-5/ICD-11 categories to consolidate this into a single, well-defined target indication — likely centered on "Neurotic Depression"/MDD-spectrum use.
- Treat "benign paroxysmal torticollis of infancy" as low-priority/likely noise given zero supporting trials or literature; do not advance without independent mechanistic justification.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

