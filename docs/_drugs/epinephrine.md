---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 135
evidence_level: L5
indication_count: 4
---

# Epinephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Epinephrine: From Anaphylaxis/Cardiac Arrest to Obstructive Lung Disease

## One-Sentence Summary

> Epinephrine is a non-selective adrenergic receptor agonist classically used as an emergency drug for anaphylaxis and cardiac arrest.
> The TxGNN model's top-ranked prediction identifies **Obstructive Lung Disease** (asthma/COPD/bronchiolitis) as an additional indication,
> supported by **2 Cochrane systematic reviews**, **1 completed Phase 3 RCT (n=373)**, and multiple bronchiolitis trials — though it should be noted this largely reaffirms epinephrine's long-standing historical use as a bronchodilator (e.g., OTC Primatene Mist) rather than representing a truly novel mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in dataset (epinephrine is classically indicated for anaphylaxis, cardiac arrest, and acute severe asthma/bronchospasm) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Based on known pharmacology, epinephrine is a non-selective adrenergic receptor agonist acting on α1, β1, and β2 receptors. Its efficacy in anaphylaxis and cardiac arrest resuscitation is well established, and mechanistically this same receptor profile is directly applicable to obstructive lung disease: β2-receptor activation produces bronchial smooth muscle relaxation (bronchodilation), while α1-receptor activation constricts mucosal blood vessels and reduces airway edema.

Epinephrine is in fact one of the earliest bronchodilators ever used clinically, historically available over-the-counter as Primatene Mist for asthma. The TxGNN prediction therefore largely reconfirms an already-validated pharmacological relationship rather than proposing a novel mechanism — the evidence base (Phase 3 asthma trials, decades of bronchiolitis studies) reflects this established use.

It is important to flag that the two Cochrane systematic reviews in the evidence set (2004, 2011) both open with the caveat that epinephrine/bronchodilators are used in bronchiolitis "despite uncertain effectiveness," indicating the clinical benefit — particularly for inpatient bronchiolitis — remains debated even though the mechanistic rationale is sound and short-term symptomatic benefit has been observed in several trials.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01357642](https://clinicaltrials.gov/study/NCT01357642) | Phase 3 | Completed | 373 | 12-week efficacy/safety of Epinephrine HFA Inhalation Aerosol vs placebo-HFA and marketed Primatene Mist CFC inhaler in adolescents/adults with asthma |
| [NCT01300325](https://clinicaltrials.gov/study/NCT01300325) | Phase 4 | Completed | 136 | Nebulized hypertonic saline + epinephrine in hospitalized infants with RSV bronchiolitis; graded A relevance |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Nebulized adrenaline + oral betamethasone vs standard care in pediatric ED bronchiolitis |
| [NCT04207840](https://clinicaltrials.gov/study/NCT04207840) | Phase 4 | Completed | 28 | Systemic exposure comparison: Primatene Mist inhalation vs epinephrine IM injection vs ProAir HFA in healthy adults |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | NA | Unknown | 600 | RCT of epinephrine vs albuterol in bronchiolitis (largest bronchiolitis cohort in this evidence set) |
| [NCT00817466](https://clinicaltrials.gov/study/NCT00817466) | Phase 4 | Unknown | 500 | Optimal nebulized inhalation treatment for infants 0–12 months with acute bronchiolitis (SE-Norway multicenter) |
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | NA | Completed | 60 | Nebulized hypertonic saline (3%) vs nebulized adrenaline for bronchiolitis |
| [NCT05363670](https://clinicaltrials.gov/study/NCT05363670) | Phase 2 | Completed | 18 | Intranasal epinephrine (ARS-1) vs albuterol in persistent asthma, needleless delivery route |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Pharmacokinetic profile of epinephrine HFA-MDI inhalation aerosol in healthy volunteers |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Phase 4 | Unknown | 135 | Home oxygen therapy ± nebulized 0.1% epinephrine for ambulatory bronchiolitis management |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane Review (Tier 1) | Cochrane Database Syst Rev | Systematic review of epinephrine for bronchiolitis; notes bronchodilators used despite uncertain effectiveness |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane Review (Tier 1) | Cochrane Database Syst Rev | Earlier Cochrane review; modest short-term benefit of bronchodilators in mild/moderate bronchiolitis |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Review (Tier 2) | BMJ Clinical Evidence | Overview of bronchiolitis epidemiology and treatment including epinephrine |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Review (Tier 2) | BMJ Clinical Evidence | Bronchiolitis clinical evidence review, seasonal LRTI in infants |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review (Tier 2) | Expert Rev Respir Med | Role of racemic epinephrine, corticosteroids, hypertonic saline, HFOT in pediatric bronchiolitis (2009–2018 literature) |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Cohort (Tier 2) | Scand J Clin Lab Invest | Elevated plasma noradrenaline in COPD correlated with hemodynamics/blood gases |
| [6417212](https://pubmed.ncbi.nlm.nih.gov/6417212/) | 1983 | Review (Tier 3) | J Allergy Clin Immunol | Pathophysiology of childhood asthma as obstructive airway disease |
| [6107058](https://pubmed.ncbi.nlm.nih.gov/6107058/) | 1980 | Review (Tier 3) | Anaesth Intensive Care | Pharmacology of sympathomimetic amines including epinephrine |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Commentary (Tier 3) | Medical Letter Drugs Ther | Return of OTC Primatene Mist (epinephrine inhaler) to market |
| [5434663](https://pubmed.ncbi.nlm.nih.gov/5434663/) | 1970 | Review (Tier 3) | British Medical Journal | General review of bronchodilator classes |

---

## Norway Market Information

Epinephrine currently holds **no marketing authorization records** in the dataset for this market (market status: Not Marketed; total licenses: 0). No product/dosage-form data is available to populate an authorization table.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between epinephrine's adrenergic activity and bronchodilation is well established and supported by a completed Phase 3 RCT and two Cochrane systematic reviews, but the reviews themselves flag uncertain/mixed clinical effectiveness (particularly for inpatient bronchiolitis), and a Blocking-severity data gap (missing official label warnings/contraindications) prevents a full S1 safety screen.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently Blocking (DG001)
- Formal mechanism of action documentation from DrugBank — currently High priority gap (DG002)
- Resolution of the conflicting efficacy signal in bronchiolitis (Cochrane reviews indicate uncertain benefit vs. positive trial-level findings in asthma)
- Route/formulation feasibility assessment for the Norway market, given the drug is currently not marketed there
- Drug interaction and contraindication data (DDI query currently returns no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

