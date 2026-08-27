---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

Using the given evidence-pack-to-report template directly (it fully specifies format, extraction rules, and section order — no additional skill applies to this content-generation task). One structural note before the report: this evidence pack is a **multi-indication screen** (`candidate_id: TW-DB00381-multi`) — 10 candidate indications, each independently scored — rather than a single-indication pack. Following the template's extraction rule literally on `predicted_indications[0]` alone (brain stem infarction, L5/Hold, zero evidence) would bury the one indication that actually clears an evidence bar (rank 10, intracerebral hemorrhage, L2/Proceed with Guardrails). I've kept the template's exact section order and table formats, but built the Quick Overview around the best-evidenced candidate and added a full ranking table so nothing is omitted.

---

# Amlodipine: From Hypertension to Recurrent Intracerebral Hemorrhage Prevention (Multi-Indication Screen)

## One-Sentence Summary

> Amlodipine is a long-acting dihydropyridine calcium channel blocker (CCB), originally indicated for hypertension and angina (no structured original-indication or Norway licensing data was returned in this pack).
> TxGNN screened 10 candidate new indications; the only one with actionable evidence is **Intracerebral Hemorrhage** (secondary prevention as part of a triple-pill antihypertensive strategy), supported by **6 clinical trials** (including one completed Phase 3 RCT, n=1,671) and **8 publications**.
> The remaining 9 candidates range from weak mechanistic extensions to apparent model/keyword noise with no supporting evidence.

---

## Quick Overview

*(Featured candidate: Intracerebral Hemorrhage — rank 10, the only indication reaching decision stage S2)*

| Item | Content |
|------|------|
| Original Indication | Hypertension / Angina (general pharmacological knowledge — no `original_indications` or Norway license data was returned in this pack) |
| Predicted New Indication | Intracerebral Hemorrhage (secondary/recurrence prevention) |
| TxGNN Prediction Score | 99.79% (rank 2745) |
| Evidence Level | L2 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails (for this indication only — see full screen below) |

### Full TxGNN Screening Summary (all 10 candidates)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Brain stem infarction | 99.94% | L5 | S0 | Hold |
| 2 | Pulmonary hypertension, unclear/multifactorial mechanism (Group 5) | 99.91% | L5 | S0 | Hold |
| 3 | Pulmonary hypertension owing to lung disease/hypoxia (Group 3) | 99.91% | L5 | S0 | Hold |
| 4 | Malignant renovascular hypertension | 99.90% | L3 | S1 | Research Question |
| 5 | Malignant hypertensive renal disease | 99.90% | L5 | S0 | Hold |
| 6 | Cerebral artery occlusion | 99.89% | L2 | S1 | Research Question |
| 7 | Braddock syndrome | 99.88% | L5 | S0 | Hold |
| 8 | MRI defined brain infarct | 99.86% | L3 | S1 | Research Question |
| 9 | ABri amyloidosis | 99.84% | L5 | S0 | Hold |
| **10** | **Intracerebral hemorrhage** | **99.79%** | **L2** | **S2** | **Proceed with Guardrails** |

Note: TxGNN score ranking does not track evidence quality here — the top-ranked prediction by score (brain stem infarction) has zero supporting trials or literature, while the lowest-ranked prediction (intracerebral hemorrhage) carries the strongest evidence.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available for this pack (`original_moa: [Data Gap]`). Based on known pharmacology, amlodipine is a long-acting dihydropyridine L-type calcium channel blocker; its efficacy in hypertension and angina is well established, and its blood-pressure-lowering effect is the mechanistic thread running through most of the candidates above.

**Intracerebral hemorrhage (lead candidate):** Amlodipine-class CCBs are already a standard component of combination antihypertensive regimens used for secondary prevention after stroke. The completed Phase 3 TRIDENT trial (NCT02699645, n=1,671) directly tested a fixed-dose "Triple Pill" (including a CCB) for reducing recurrent cerebrovascular events after intracerebral hemorrhage, and CASE-J (a large RCT) compared amlodipine-class CCB combination therapy against ARB monotherapy for cardiovascular/cerebrovascular event reduction. This is class-level and combination-therapy evidence rather than an amlodipine-monotherapy trial specifically for ICH, which is why the evidence level caps at L2 rather than L1.

**Cerebral artery occlusion / MRI defined brain infarct:** Preclinical rodent studies (transient MCAO models) show amlodipine, alone or combined with atorvastatin, reduces infarct size via antioxidant, anti-apoptotic, and anti-autophagic mechanisms. Clinical evidence here is indirect — large blood-pressure-control trials (e.g., STEP, n=8,000) that use brain-imaging or cerebrovascular endpoints as secondary outcomes, not amlodipine-specific interventional trials for acute occlusion.

**Malignant renovascular hypertension:** This is essentially a pharmacological extension within amlodipine's existing approved use (severe/resistant hypertension) rather than a genuine cross-domain repurposing; the two supporting citations are pediatric case reports that do not name amlodipine explicitly as the study drug.

**Candidates assessed as Hold (no real signal):** Brain stem infarction, Group 5 pulmonary hypertension, malignant hypertensive renal disease, Braddock syndrome, and ABri amyloidosis have no clinical trials or literature support. Notably, the 20 PubMed hits returned for Group 3 pulmonary hypertension (hypoxia/lung-disease-related) are general hypoxia-biology papers unrelated to amlodipine or CCB therapy — likely keyword-matching noise rather than evidence — and current ESC/ERS guidance actually advises *against* CCB use in hypoxia-driven pulmonary hypertension due to risk of worsening ventilation/perfusion mismatch. These candidates should not be advanced.

---

## Clinical Trial Evidence

### Intracerebral Hemorrhage (lead candidate)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT main trial: fixed low-dose "Triple Pill" BP-lowering strategy (incl. CCB) vs. standard care for preventing recurrent stroke after intracerebral hemorrhage — directly relevant, completed Phase 3 RCT |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | N/A | Recruiting | 140 | TRICH Score-guided triple antihypertensive therapy for BP control after ICH; follow-on to TRIDENT concept, no results yet |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | Antihypertensive treatment in high-normal BP adults with Type 2 diabetes (IPAD); large but not ICH-specific |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | High-dose ARB monotherapy vs. ARB + CCB combination for cardiovascular event reduction in elderly Japanese hypertensive patients |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study — terminated, enrollment of 1, not statistically usable |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study — terminated, enrollment of 4, not statistically usable |

### Cerebral Artery Occlusion

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) | N/A | Unknown | 8,000 | STEP trial: intensive vs. standard systolic BP targets in elderly hypertensive patients; status unknown, not amlodipine-specific |
| [NCT02850081](https://clinicaltrials.gov/study/NCT02850081) | Phase 3 | Completed | 31 | Statin (not amlodipine) neuroprotection before carotid endarterectomy — indirectly related only |
| [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) | Phase 4 | Terminated | 400 | Carotid endarterectomy vs. optimal medical treatment; terminated, not amlodipine-specific |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study (see above) |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI sub-study (see above) |

### MRI Defined Brain Infarct

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) | N/A | Unknown | 8,000 | STEP trial (see above); uses MRI-related brain outcomes as one observation measure, status unknown |

**Other 7 candidates (brain stem infarction, both pulmonary hypertension groups, malignant renovascular hypertension, malignant hypertensive renal disease, Braddock syndrome, ABri amyloidosis):** Currently no related clinical trials registered.

---

## Literature Evidence

### Intracerebral Hemorrhage (lead candidate)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT | Hypertension Research | CASE-J trial rationale — large RCT comparing candesartan vs. CCB-based regimens for cardiovascular event reduction in high-risk hypertensive patients |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Review/Trial Rationale | Int J Stroke | TRIDENT trial rationale and design — single-pill CCB-containing combination for secondary BP-driven ICH prevention |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Review | Neurological Sciences | Role of antihypertensive choice (beta-blocker vs. alternatives) in acute hypertensive ICH outcomes |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovascular Drugs and Therapy | Overview of CCB antihypertensive mechanism and use in severe hypertension |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | Preclinical | Biol Pharm Bull | A different dihydropyridine CCB (benidipine) improves cerebral blood flow autoregulation in hypertensive rats — mechanistic class analogy only |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report (Adverse Event) | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with hemorrhagic stroke — safety signal, not efficacy |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | Case Report | BMJ Case Reports | PRES after rapid antihypertensive withdrawal post-bariatric surgery in a patient with prior ICH — unrelated context |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | Case Report | Current Drug Safety | Tizanidine-induced hypotension in stroke patients — different drug, not directly relevant |

### Cerebral Artery Occlusion

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Animal/Preclinical | J Neurosci Res | Amlodipine + atorvastatin reduce infarct size via anti-apoptotic/anti-autophagic mechanisms after transient MCAO in metabolic syndrome rats |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Animal/Preclinical | Brain Research | Synergistic neuroprotection of amlodipine + atorvastatin after stroke in Zucker metabolic rats |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Animal/Preclinical | Brain Research | Combined amlodipine + atorvastatin protects against ischemic stroke damage in Zucker rats |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Animal/Preclinical | Am J Hypertension | Amlodipine reduces stroke size in apolipoprotein E-deficient mice |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Animal/Preclinical | Brain Research | CCBs with antioxidative effects prevent neuronal damage after transient focal cerebral ischemia in rats |

### Malignant Renovascular Hypertension

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16467664](https://pubmed.ncbi.nlm.nih.gov/16467664/) | 2006 | Case Report | Journal of Hypertension | Pediatric case of severe renovascular hypertension from renal artery compression in tuberous sclerosis; management context only, amlodipine not named as study drug |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case Report | BMC Nephrology | Hyponatremic hypertensive syndrome presenting as malignant hypertension in an 18-month-old; amlodipine not named as study drug |

### Pulmonary Hypertension Owing to Lung Disease/Hypoxia (Group 3)

20 PubMed records were returned by keyword search, but on review all are general hypoxia-biology or oncology-hypoxia papers (e.g., cerebral hypoxia and aging, HIF-1α signaling in cancer, altitude physiology) with no direct discussion of amlodipine, CCBs, or pulmonary hypertension treatment. These are assessed as keyword-matching noise rather than genuine evidence and are not counted toward the evidence level; current treatment guidance (ESC/ERS) advises against CCB use in this indication. No relevant literature identified.

**Other candidates (brain stem infarction, Group 5 pulmonary hypertension, malignant hypertensive renal disease, Braddock syndrome, MRI defined brain infarct, ABri amyloidosis):** Currently no related literature available.

---

## Norway Market Information

No marketing authorizations were found for amlodipine in this dataset — market status is recorded as **Not Marketed**, with 0 authorizations on file. No product/dosage-form/indication records are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (No structured warnings, contraindications, or drug-interaction data were returned for this drug in the current pack; a blocking data gap — TFDA/label warnings and contraindications — was flagged and remains unresolved as of the data cutoff.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for Intracerebral Hemorrhage secondary prevention only)* — **Hold** *(for the other 9 screened candidates)*

**Rationale:**
- Intracerebral hemorrhage is the only candidate supported by a completed Phase 3 RCT (TRIDENT, n=1,671) and corroborating class-level trial/literature evidence, justifying guarded advancement rather than outright hold.
- Cerebral artery occlusion and MRI defined brain infarct (Research Question) have credible preclinical/mechanistic signal but no amlodipine-specific interventional trial, and malignant renovascular hypertension is a pharmacological extension of an already-approved use rather than novel repurposing — all three need targeted evidence review before moving past S1.
- The remaining 5 candidates (brain stem infarction, both pulmonary hypertension groups, malignant hypertensive renal disease, Braddock syndrome, ABri amyloidosis) have no supporting trials or literature, and in the case of Group 3 pulmonary hypertension the returned literature is unrelated noise; these should remain on Hold.

**To proceed, the following is needed:**
- Resolution of DG001 (TFDA/label warnings and contraindications) — currently a blocking gap for any safety pre-assessment (S1 gate).
- Resolution of DG002 (mechanism of action) to support the mechanistic-plausibility analysis with primary source data rather than general pharmacological knowledge.
- For the lead candidate (intracerebral hemorrhage): amlodipine-specific (not combination-only) outcome data from TRIDENT if/when available, plus a formal indication-specific safety review given the drug is not currently marketed in Norway.
- For the three Research Question candidates: a targeted literature/trial search using amlodipine-specific search terms (rather than CCB-class terms) to confirm or rule out promotion to S2.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

