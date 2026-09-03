---
layout: default
title: Miglustat
parent: 僅模型預測 (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Miglustat
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

# Miglustat: From Gaucher Disease/Niemann-Pick Type C to Tay-Sachs Disease (GM2 Gangliosidosis)

*Note: Among the 10 TxGNN-predicted indications in this evidence pack, the highest-scoring candidate (autosomal ichthyosis syndrome, 99.83%) has no supporting clinical trials or literature and is rated "Hold" with a weak mechanistic link. Tay-Sachs disease (rank 7, score 99.75%) is the only candidate backed by actual clinical trial and publication evidence, and is the only one rated "Proceed with Guardrails." This report focuses on Tay-Sachs disease as the actionable candidate.*

## One-Sentence Summary

Miglustat is a glucosylceramide synthase inhibitor (imino sugar) already approved as substrate reduction therapy for Gaucher disease Type 1 and Niemann-Pick disease Type C. The TxGNN model predicts it may also be effective for **Tay-Sachs disease (GM2 gangliosidosis)**, with **5 clinical trials** and **20 publications** identified, including one completed randomized controlled trial and one 2023 systematic review specifically evaluating miglustat in this population.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally captured in Norway licensing data (drug not marketed); per known drug profile, miglustat is approved for Gaucher disease Type 1 and Niemann-Pick disease Type C |
| Predicted New Indication | Tay-Sachs Disease (GM2 Gangliosidosis) |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L2 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap (DG002) in this evidence pack. Based on the information embedded in the repurposing rationale, miglustat is an inhibitor of glucosylceramide synthase, the enzyme that catalyzes the first committed step of glycosphingolipid biosynthesis. This "substrate reduction therapy" (SRT) approach is already clinically validated in Gaucher disease Type 1 and Niemann-Pick disease Type C, both of which are glycosphingolipid lysosomal storage disorders.

Tay-Sachs disease is caused by hexosaminidase A deficiency, leading to pathological accumulation of GM2 ganglioside — itself a downstream product of the same glycosphingolipid biosynthetic pathway that miglustat inhibits upstream. This makes Tay-Sachs disease the most mechanistically direct extension of miglustat's already-approved substrate reduction indication among all 10 TxGNN candidates in this pack. Several related predictions (Krabbe disease, metachromatic leukodystrophy, prosaposin deficiency) share the same glycosphingolipid-pathway logic but currently have no supporting clinical or literature evidence, whereas Tay-Sachs/GM2 gangliosidosis has been directly studied in humans.

It is worth noting that miglustat has *not* demonstrated a positive efficacy signal in every GM2 gangliosidosis trial — one Phase 3 study (NCT03822013) was terminated in infantile-onset patients, and the mechanistic literature (e.g., PMID 16434676) describes cases where substrate reduction therapy could not arrest neurologic deterioration in infantile-onset disease despite adequate CNS drug exposure. The evidence base is therefore stronger for late-onset/juvenile forms than for the infantile-onset phenotype.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Phase 3 | Completed | 10 | PK/safety/tolerability of miglustat in infantile-onset GM2 gangliosidosis (Tay-Sachs and Sandhoff); miglustat inhibits GM2 ganglioside synthesis and may reduce/delay symptom onset |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Phase 2 | Completed | 5 | Single/multiple-dose PK and tolerability of miglustat in juvenile GM2 gangliosidosis |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Phase 3 | Terminated | 30 | Miglustat's effect on neurological/systemic symptoms in infantile Sandhoff/Tay-Sachs disease; trial terminated, reason not specified in available data |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Phase 4 | Terminated | 16 | Combination of miglustat + ketogenic diet ("Syner-G") hypothesized to improve survival and neurodevelopmental outcomes in infantile/juvenile gangliosidoses; terminated early |
| [NCT07399704](https://clinicaltrials.gov/study/NCT07399704) | Phase 2 | Recruiting | 21 | Long-term safety/PK/efficacy of newer SRT agent nizubaglustat in GM2 gangliosidosis/NPC patients, including those transitioning from prior miglustat therapy |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genetics in Medicine | 12-month randomized controlled trial (with 24-month extension) evaluating safety and efficacy of miglustat in late-onset Tay-Sachs/GM2 gangliosidosis patients |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematic Review | European Journal of Neurology | Systematic review of miglustat efficacy/safety in GM2 gangliosidosis; notes prior inconsistent results across studies |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Cohort (pilot) | J Inherit Metab Dis | Neurocognitive testing pilot study in late-onset Tay-Sachs disease, proposed as an outcome measure for therapeutic trials |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Cohort/Case series | Neurology | Substrate reduction therapy with miglustat in 2 infantile Tay-Sachs patients; could not arrest neurologic deterioration, but achieved measurable CSF drug levels and prevented macrocephaly |
| [33738443](https://pubmed.ncbi.nlm.nih.gov/33738443/) | 2021 | Cohort | Brain Communications | Related lysosomal storage disorder study (acetyl-DL-leucine in NPC1 mouse model); contextual evidence for symptomatic SRT-adjacent approaches |
| [32867370](https://pubmed.ncbi.nlm.nih.gov/32867370/) | 2020 | Review | Int J Mol Sci | Overview of GM2 gangliosidoses clinical features, pathophysiology, and current therapies including substrate reduction |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Review | Frontiers in Physiology | Review of new therapeutic approaches for Tay-Sachs disease |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Review/Drug profile | Curr Opin Investig Drugs | Drug development profile noting miglustat's EU approval for Gaucher disease and ongoing development for Tay-Sachs, Fabry, and Niemann-Pick C |
| [9572057](https://pubmed.ncbi.nlm.nih.gov/9572057/) | 1998 | Review | Molecular Medicine Today | Early review of biology and potential treatment strategies for GM2 gangliosidoses |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Review | Mol Genet Metab | Natural history/timeline of infantile gangliosidoses; notes substrate reduction with miglustat has been tried but limited by GI side effects |

## Norway Market Information

Miglustat currently has no marketing authorization in Norway (`market_status: 未上市`, `total_licenses: 0`). No license records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not available in this evidence pack (flagged as data gap DG001, severity: Blocking — TFDA label warnings/contraindications not yet retrieved).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tay-Sachs disease/GM2 gangliosidosis is the only one of 10 TxGNN-predicted indications supported by an actual completed RCT and a 2023 systematic review, and it has a direct, already-validated mechanistic link to miglustat's approved substrate reduction therapy mechanism. However, results are mixed — one Phase 3 trial and one Phase 4 combination trial were both terminated, and efficacy appears more consistent in late-onset than infantile-onset disease.

**To proceed, the following is needed:**
- Resolve data gap DG001 (Blocking): retrieve TFDA/official label warnings and contraindications before any safety evaluation (S1) can proceed
- Resolve data gap DG002 (High): confirm detailed mechanism of action from DrugBank to strengthen the mechanistic rationale
- Investigate termination reasons for NCT03822013 and NCT02030015, as these are negative signals that need explicit review
- Define target population (late-onset/juvenile vs. infantile-onset) given differential efficacy signals in the literature
- If pursued, prioritize the late-onset/juvenile GM2 gangliosidosis population, consistent with the strongest existing evidence (PMID 19346952)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

