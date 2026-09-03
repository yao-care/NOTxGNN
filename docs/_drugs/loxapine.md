---
layout: default
title: Loxapine
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Loxapine
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

Using no additional skill here — this is a direct content-generation task per the explicit report template already provided in the prompt.

# Loxapine: From Schizophrenia to Acute Agitation in Bipolar Disorder

## One-Sentence Summary

> Loxapine is a first-generation (typical) antipsychotic of the dibenzoxazepine class, historically used to treat schizophrenia via oral administration for decades.
> The TxGNN model predicts it may be effective for **manic bipolar affective disorder** (specifically, acute agitation associated with bipolar mania),
> with **0 registered clinical trials in the evidence pack's trial registry** but **20 supporting publications**, including completed Phase III RCTs and an existing international regulatory precedent (inhaled formulation approved in the US/EU).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia (per literature; not documented in local market licenses — drug not currently marketed in Norway) |
| Predicted New Indication | Manic bipolar affective disorder (acute agitation) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs identified in supporting literature) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank (data gap). Based on information embedded in the supporting literature, loxapine is a first-generation antipsychotic of the dibenzoxazepine class, originally used for schizophrenia treatment in oral form for over three decades. A reformulated inhaled powder (marketed elsewhere as Adasuve®) using the Staccato® thermal aerosol delivery system was subsequently developed, reaching peak plasma concentrations within a median of ~2 minutes — enabling rapid onset of antipsychotic/calming effect.

Schizophrenia and bipolar mania are both severe psychiatric disorders that share an overlapping clinical presentation: acute psychomotor agitation, excessive motor/verbal activity, and risk of escalation to aggression. Because loxapine's antipsychotic action (dopamine D2 / serotonin 5-HT2A receptor antagonism, typical of this drug class) targets these transdiagnostic symptom domains rather than a disease-specific pathology, its efficacy is not necessarily confined to schizophrenia.

This mechanistic plausibility is directly reflected in the literature itself: inhaled loxapine was studied and approved (US FDA/EU) specifically for "acute treatment of agitation associated with schizophrenia **or** bipolar I disorder" as a single combined indication, and clinical guidelines for bipolar mania (Pacchiarotti et al. 2020) list antipsychotics such as loxapine among recommended pharmacologic options — supporting the TxGNN-predicted association rather than representing a novel or speculative hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (no structured entries present in `clinical_trials` or `ictrp_trials`). Note: several literature items below reference completed Phase III RCTs (e.g., NCT00628589, NCT00721955 per Zeller et al. 2017) that were not captured as structured trial registry entries in this evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29724638](https://pubmed.ncbi.nlm.nih.gov/29724638/) | 2018 | RCT | Eur Neuropsychopharmacol | PLACID study: assessor-blind RCT (23 centres, 4 countries) comparing inhaled loxapine vs IM aripiprazole for acute agitation in schizophrenia/bipolar I disorder |
| [29163985](https://pubmed.ncbi.nlm.nih.gov/29163985/) | 2017 | RCT (post-hoc analysis) | BJPsych Open | Responder analysis of 2 completed Phase III RCTs (NCT00628589, NCT00721955; 344 schizophrenia + 314 bipolar I patients) using PANSS-EC scale |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | RCT (secondary analysis) | Int J Clin Pract | Effect-size analysis from 2 Phase III RCTs of inhaled loxapine in schizophrenia/bipolar disorder agitation |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic Review & Meta-analysis | Hum Psychopharmacol | Systematic review of short-term pharmacologic interventions for agitation in schizophrenia/bipolar disorder |
| [28376877](https://pubmed.ncbi.nlm.nih.gov/28376877/) | 2017 | RCT Protocol | BMC Psychiatry | Design of PLACID RCT comparing inhaled loxapine vs IM aripiprazole in acute agitation |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based treatment options and clinical guidance for bipolar mania, including antipsychotic choice |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Expert Review | Drugs in R&D | Review of inhaled loxapine for acute agitation management in bipolar disorder and schizophrenia |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Review | CNS Drugs | Review of loxapine inhalation powder (Adasuve®) pharmacokinetics and Phase III trial data |
| [28208695](https://pubmed.ncbi.nlm.nih.gov/28208695/) | 2017 | Clinical Review | Int J Mol Sci | Narrative/clinical mini-review of inhaled loxapine efficacy and tolerability in acute agitation |
| [37581475](https://pubmed.ncbi.nlm.nih.gov/37581475/) | 2023 | Review | Expert Opin Pharmacother | Review of pharmacotherapy options for agitation associated with bipolar disorder |

---

## Norway Market Information

Not currently marketed in Norway — no authorization records available (`total_licenses: 0`).

---

## Safety Considerations

Local package insert data (warnings, contraindications, drug-drug interactions) is currently unavailable — this has been flagged as a **Blocking** data gap (DG001), meaning the candidate cannot yet enter formal safety pre-assessment (S1 stage). Please refer to the package insert for safety information once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Literature evidence is strong (L1: ≥2 completed Phase III RCTs, one dedicated head-to-head RCT, and a systematic review/meta-analysis), and the predicted indication is corroborated by an existing international regulatory precedent (inhaled loxapine approved in the US/EU for agitation in schizophrenia *or* bipolar I disorder). However, the candidate cannot proceed past initial safety screening because local warnings/contraindications data is completely unavailable (Blocking gap DG001), and the drug is not currently marketed in Norway.

**To proceed, the following is needed:**
- Retrieve official label/package insert safety data (warnings, contraindications) — source: TFDA-equivalent regulatory filing or EMA/FDA label
- Obtain detailed MOA/pharmacology data from DrugBank (DG002)
- Confirm intended route of administration (oral vs. inhaled Staccato® delivery) and its regulatory pathway in Norway
- Conduct DDI screening (currently `query_status: not_found`)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

