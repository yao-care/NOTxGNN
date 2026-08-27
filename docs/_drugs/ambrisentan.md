---
layout: default
title: Ambrisentan
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
---

# Ambrisentan
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

# Ambrisentan: From Pulmonary Arterial Hypertension to Multiple PAH-Subtype Indications (Multi-Candidate Evaluation)

## One-Sentence Summary

> Ambrisentan is a selective endothelin receptor antagonist (ERA) established for the treatment of pulmonary arterial hypertension (PAH) — idiopathic, heritable, and connective-tissue-disease-associated forms — per the literature retrieved in this evidence pack.
> The TxGNN model surfaced **10 candidate indications**, but evidence quality diverges sharply from the raw prediction score: the two strongest candidates, **PAH associated with connective tissue disease** and **PAH associated with congenital heart disease**, are each backed by **multiple completed Phase 2–4 trials and meta-analyses (L1)**, while the top-ranked-by-score prediction, **pulmonary arteriovenous malformation**, rests on a single indirect case report (L4).
> Six of the ten candidates have **no clinical trial or literature support at all** and should be treated as knowledge-graph noise rather than repurposing leads.

---

## Quick Overview

### Drug & Regulatory Snapshot

| Item | Content |
|------|------|
| Original Indication | Pulmonary Arterial Hypertension (idiopathic, heritable, and connective-tissue-disease-associated) — per in-pack literature (PMID 28425346) |
| Norway Market Status | Not marketed (未上市) |
| Number of Authorizations | 0 |
| Blocking Data Gap | TFDA package insert (warnings/contraindications) not yet obtained — blocks formal S1 safety review |

### Top-Ranked Prediction (by TxGNN score)

| Item | Content |
|------|------|
| Predicted New Indication | Pulmonary arteriovenous malformation (disease) |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Recommended Decision | Hold |

### Most Clinically Actionable Predictions (ranked by evidence strength, not score)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommended Decision |
|------|----------------------|-------------|-----------------|-----------------|------------------------|
| 6 | PAH associated with connective tissue disease | 99.30% | L1 | S3 | Proceed with Guardrails |
| 2 | PAH associated with congenital heart disease | 99.37% | L1 | S3 | Proceed with Guardrails |
| 4 | PAH associated with HIV infection | 99.30% | L2 | S2 | Research Question |
| 1 | Pulmonary arteriovenous malformation | 99.41% | L4 | S0 | Hold |
| 3 | PAH associated with schistosomiasis | 99.30% | L5 | S0 | Hold |
| 5 | PAH associated with chronic hemolytic anemia | 99.30% | L5 | S0 | Hold |
| 7 | Malformation syndrome with odontal/periodontal component | 99.19% | L5 | S0 | Hold |
| 8 | Hypotrichosis simplex of the scalp | 99.15% | L5 | S0 | Hold |
| 9 | Hypertrichosis | 99.14% | L5 | S0 | Hold |
| 10 | Syndrome with Dandy-Walker malformation | 99.12% | L5 | S0 | Hold |

---

## Why Are These Predictions Reasonable?

Detailed formal MOA data for ambrisentan is not present in this evidence pack (data gap). Based on what can be reconstructed from the retrieved literature, ambrisentan is a **selective endothelin type-A (ETA) receptor antagonist**, part of the endothelin receptor antagonist (ERA) drug class alongside bosentan and macitentan. Its established efficacy is in PAH, where it blocks endothelin-1 (ET-1)-mediated pulmonary vascular smooth-muscle constriction and remodeling (PMID 28425346, 35412560).

**Why the strongest candidates make sense:** PAH associated with congenital heart disease (Eisenmenger physiology) and PAH associated with connective tissue disease (chiefly systemic sclerosis) are not biologically distinct diseases from the approved indication — both are **WHO Group 1 PAH subtypes**. They share the same core pathophysiology (pulmonary arteriolar remodeling driven by shear stress or vascular inflammation, with ET-1 upregulation) that ambrisentan's approved label already addresses. This is reflected in the evidence: the pivotal AMBITION trial's CTD-PAH subgroup analyses (PMID 32161055, 28039187), the ARIES-E CTD-PAH subgroup (PMID 27492539), and the dedicated EDITA RCT in systemic-sclerosis-associated PAH (PMID 31655622) all used ambrisentan directly in these populations. Similarly, pediatric and adult CHD-PAH/Eisenmenger-syndrome data (PMID 21371683, and the completed pediatric extension trial NCT01342952) demonstrate direct on-label-adjacent use.

**Why the weaker candidates are questionable:** In contrast, HIV-associated PAH shares the WHO Group 1 mechanistic classification but currently lacks an ambrisentan-specific trial (the one identified Phase 3 trial, NCT00709956, actually tested iloprost in a mixed population that merely included some ambrisentan-background patients) — hence a "Research Question" rather than "Proceed" stage. Pulmonary arteriovenous malformation (PAVM), by contrast, is a **structural arteriovenous shunt disorder**, mechanistically unrelated to ET-1-driven vasoconstriction/remodeling; its single supporting reference is a case report of a patient with hereditary hemorrhagic telangiectasia who happened to also have PAH — evidence for treating co-morbid PAH, not PAVM itself. The remaining six candidates (schistosomiasis-PAH, hemolytic-anemia-PAH, periodontal malformation syndrome, hypotrichosis, hypertrichosis, Dandy-Walker malformation) have **zero clinical trial or literature support** and, for the non-PAH entries, no plausible mechanistic link to ET-1 antagonism at all — these are best interpreted as knowledge-graph embedding artifacts rather than genuine repurposing signals.

---

## Clinical Trial & Literature Evidence by Indication

### 1. PAH Associated with Connective Tissue Disease (Rank 6 — L1, Proceed with Guardrails)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01042158](https://clinicaltrials.gov/study/NCT01042158) | Phase 4 | Completed | 25 | Ambrisentan + tadalafil combination therapy in systemic-sclerosis-spectrum PAH (PAH-SSD); assessed 6MWD, NYHA class, hemodynamics |
| [NCT02290613](https://clinicaltrials.gov/study/NCT02290613) | Phase 2 | Completed | 38 | EDITA study — early ambrisentan treatment of borderline mPAP in systemic sclerosis, RCT proof-of-concept |
| [NCT02885012](https://clinicaltrials.gov/study/NCT02885012) | Phase 4 | Terminated | 3 | Switch from bosentan/macitentan to ambrisentan in CTD-PAH; terminated with very small n, limits interpretability |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32161055](https://pubmed.ncbi.nlm.nih.gov/32161055/) | 2020 | RCT post-hoc (AMBITION) | Annals of the Rheumatic Diseases | Initial ambrisentan+tadalafil combination outperforms monotherapy in CTD-PAH subpopulation |
| [23906950](https://pubmed.ncbi.nlm.nih.gov/23906950/) | 2013 | Meta-analysis | BMJ Open | Meta-analysis of clinical trials for CTD-PAH treatment |
| [26360334](https://pubmed.ncbi.nlm.nih.gov/26360334/) | 2015 | Cohort (RCT-derived) | Am J Respir Crit Care Med | Up-front ambrisentan+tadalafil combination therapy in scleroderma-associated PAH |
| [31655622](https://pubmed.ncbi.nlm.nih.gov/31655622/) | 2019 | RCT | Arthritis Research & Therapy | EDITA study: ambrisentan reduces mPAP in mildly elevated PH associated with systemic sclerosis |
| [27492539](https://pubmed.ncbi.nlm.nih.gov/27492539/) | 2016 | Subgroup analysis (ARIES-E) | Respiratory Medicine | 3-year efficacy/safety of ambrisentan specifically in CTD-PAH |
| [28039187](https://pubmed.ncbi.nlm.nih.gov/28039187/) | 2017 | Subgroup analysis (AMBITION) | Annals of the Rheumatic Diseases | Initial ambrisentan+tadalafil combination in CTD-PAH subgroup |
| [38378970](https://pubmed.ncbi.nlm.nih.gov/38378970/) | 2024 | Systematic review/meta-analysis | Internal and Emergency Medicine | Treatment outcomes for CTD-PAH across RCT subgroup/post-hoc data |
| [37765060](https://pubmed.ncbi.nlm.nih.gov/37765060/) | 2023 | Review | Pharmaceuticals (Basel) | Recent advances in CTD-PAH treatment |
| [21119190](https://pubmed.ncbi.nlm.nih.gov/21119190/) | 2010 | Review/Cohort | European Respiratory Review | Early intervention in SSc-associated PAH as disease-management essential |
| [29282676](https://pubmed.ncbi.nlm.nih.gov/29282676/) | 2018 | Post-marketing surveillance | Clinical Drug Investigation | Real-world safety/efficacy of ambrisentan (Volibris) in 702 PAH patients |

*(10 additional lower-priority general-PAH review/registry references were retrieved but omitted here for relevance.)*

### 2. PAH Associated with Congenital Heart Disease (Rank 2 — L1, Proceed with Guardrails)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01884675](https://clinicaltrials.gov/study/NCT01884675) | Phase 3 | Terminated | 33 | Ambrisentan vs. placebo in inoperable CTEPH; terminated — reason (enrollment vs. safety) requires verification |
| [NCT01808313](https://clinicaltrials.gov/study/NCT01808313) | Phase 3 | Completed | 134 | Open-label study of ambrisentan on exercise capacity (6MWT) in Chinese PAH patients |
| [NCT01342952](https://clinicaltrials.gov/study/NCT01342952) | Phase 2 | Completed | 38 | Long-term open-label extension of ambrisentan in pediatric PAH (largely CHD-driven population) |
| [NCT01894022](https://clinicaltrials.gov/study/NCT01894022) | Phase 3 | Terminated | 19 | Open-label long-term safety extension of ambrisentan in inoperable CTEPH |
| [NCT01332331](https://clinicaltrials.gov/study/NCT01332331) | Phase 2 | Terminated | 41 | High- vs. low-dose ambrisentan (weight-adjusted) in pediatric PAH |
| [NCT02688387](https://clinicaltrials.gov/study/NCT02688387) | Phase 1 | Completed | 112 | Relative bioavailability of fixed-dose ambrisentan+tadalafil combinations |
| [NCT04095286](https://clinicaltrials.gov/study/NCT04095286) | Phase 1 | Completed | 29 | PK/bioavailability of a lower-dose pediatric ambrisentan formulation |
| [NCT00593905](https://clinicaltrials.gov/study/NCT00593905) | N/A | Withdrawn | 0 | Pharmacogenomics of ERA response in PAH; withdrawn, no data generated |
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | Unknown | 42 | Iloprost (not ambrisentan) effects in PAH-CHD/Eisenmenger — population-relevant only, not direct drug evidence |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21371683](https://pubmed.ncbi.nlm.nih.gov/21371683/) | 2011 | Cohort | American Journal of Cardiology | Direct ambrisentan use in Eisenmenger syndrome cohort; improved rest/exercise hemodynamics |
| [18333354](https://pubmed.ncbi.nlm.nih.gov/18333354/) | 2007 | Review | Rom J Intern Med | Management of PAH associated with congenital heart disease |
| [31096477](https://pubmed.ncbi.nlm.nih.gov/31096477/) | 2019 | Systematic review/meta-analysis | Medicine | PAH-specific drug therapy positioning in Eisenmenger syndrome |
| [34921523](https://pubmed.ncbi.nlm.nih.gov/34921523/) | 2022 | Cohort | Pediatric Pulmonology | Real-world safety/tolerability of ambrisentan+tadalafil combination in pediatric PH |
| [35412560](https://pubmed.ncbi.nlm.nih.gov/35412560/) | 2022 | Review | JAMA | General PAH diagnosis and treatment overview |
| [21852894](https://pubmed.ncbi.nlm.nih.gov/21852894/) | 2009 | Cohort | Progress in Pediatric Cardiology | Non-CHD pediatric PAH etiologies (contrast reference) |
| [22104452](https://pubmed.ncbi.nlm.nih.gov/22104452/) | 2011 | Registry/Cohort | Postgraduate Medicine | Adult congenital heart disease PAH program experience (Texas) |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | PAH treatment overview across APAH etiologies including CHD |
| [26223872](https://pubmed.ncbi.nlm.nih.gov/26223872/) | 2015 | Review | Indian Journal of Pediatrics | Management concepts for pediatric pulmonary hypertension |
| [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) | 2014 | Cohort | Ther Adv Respir Dis | Ambrisentan clinical use/tolerability in a broad PH referral centre |

*(8 additional references, including one on a different drug (sotatercept) and several general registries, were omitted for relevance.)*

### 3. PAH Associated with HIV Infection (Rank 4 — L2, Research Question)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Phase 3 | Completed | 64 | Crossover study of add-on iloprost in PAH (idiopathic/familial/HIV/drug-related); patients on background bosentan, ambrisentan, or sildenafil — not an ambrisentan-specific HIV-PAH trial |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26897508](https://pubmed.ncbi.nlm.nih.gov/26897508/) | 2016 | Cohort | Medicina Clinica | Clinical/molecular characteristics of 4 HIV-associated PAH cases |
| [24787237](https://pubmed.ncbi.nlm.nih.gov/24787237/) | 2014 | Cohort | Ther Adv Respir Dis | Ambrisentan clinical use/tolerability in a broad PH referral centre |
| [25560124](https://pubmed.ncbi.nlm.nih.gov/25560124/) | 2015 | Case report | Obstetrics and Gynecology | HIV-associated PAH diagnosed postpartum |
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Registry | Terapevticheskii Arkhiv | National PAH registry (Russia), general prevalence/therapy data |

### 4. Pulmonary Arteriovenous Malformation (Rank 1 — L4, Hold)

Currently no related clinical trials registered.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case report | World Journal of Clinical Cases | HHT patient with co-morbid PAH treated per PAH protocol; not evidence of efficacy for PAVM itself |

### 5. Remaining Candidates (Ranks 3, 5, 7–10 — L5, Hold)

- **PAH associated with schistosomiasis** (Rank 3) and **PAH associated with chronic hemolytic anemia** (Rank 5): Currently no related clinical trials registered and no related literature available. Mechanistically plausible (both are WHO Group 1/5 PAH), but purely model-predicted with zero supporting data; hemolytic-disease populations (e.g., sickle cell disease) also carry a theoretical thrombosis-risk concern with ERAs that would need dedicated safety review.
- **Malformation syndrome with odontal/periodontal component** (Rank 7): 20 periodontology publications were retrieved, but none reference ambrisentan or the endothelin pathway — this pairing is assessed as knowledge-graph noise, not a genuine signal.
- **Hypotrichosis simplex of the scalp** (Rank 8), **Hypertrichosis** (Rank 9), **Dandy-Walker malformation syndrome** (Rank 10): Currently no related clinical trials registered and no related literature available. No plausible mechanistic link to ET-1 receptor antagonism.

---

## Norway Market Information

Ambrisentan is **not currently marketed in Norway** — 0 authorizations are on file, and no license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug warnings, contraindications, or interaction data were retrievable in this evidence pack; obtaining the TFDA package insert is flagged as a **blocking data gap** (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for PAH associated with congenital heart disease and PAH associated with connective tissue disease only) / **Hold** (for all other 8 candidates)

**Rationale:**
- PAH-CHD and PAH-CTD are mechanistically indistinguishable from ambrisentan's core approved PAH indication (both WHO Group 1 subtypes) and are backed by L1 evidence — multiple completed Phase 2–4 trials, an EDITA RCT, and AMBITION/ARIES-E subgroup analyses.
- HIV-PAH remains a Research Question (L2) — plausible mechanism, but the only identified Phase 3 trial tested a different drug (iloprost) in a mixed background-therapy population, not ambrisentan specifically.
- The remaining seven candidates (PAVM, schistosomiasis-PAH, hemolytic-anemia-PAH, periodontal malformation syndrome, hypotrichosis, hypertrichosis, Dandy-Walker malformation) lack any clinical trial or literature support, and several lack any credible mechanistic rationale; these should not advance further at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a **blocking** gap that prevents entry into the S1 safety initial assessment (DG001)
- DrugBank-sourced mechanism-of-action detail to strengthen the mechanistic rationale writeup (DG002)
- Verification of termination reasons for the terminated CHD-PAH trials (NCT01884675, NCT01894022, NCT01332331) — to distinguish enrollment-driven terminations from efficacy/safety-driven ones
- Route/dosage-form compatibility check against Norway's regulatory requirements (currently marked "pending" for all candidate indications)
- Confirmation of whether NCT00709956 and NCT01383083 (both testing non-ambrisentan drugs, iloprost) should be reclassified as population-context evidence rather than direct drug evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

