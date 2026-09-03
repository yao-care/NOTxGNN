---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Treatment-Refractory Schizophrenia

## One-Sentence Summary

Paliperidone is an antipsychotic (the active metabolite of risperidone, D2/5-HT2A receptor antagonist) already used for schizophrenia-spectrum disorders. The TxGNN model returned nine higher-scoring predictions (retinal dystrophy, X-linked/syndromic myopia, hydranencephaly, a glycosylation disorder, CMT type 1G, glycine encephalopathy) that the evidence pack itself flags as mechanistically implausible with **zero supporting trials or literature** — these are treated as model noise, not candidates. The only prediction with real support is an extension into **treatment-refractory schizophrenia**, backed by **4 clinical trials** and **2 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the Norway licensing data (0 authorizations); mechanistically established as schizophrenia/schizoaffective disorder per the drug's known antipsychotic class |
| Predicted New Indication | Treatment-Refractory Schizophrenia (selected from rank 10 — see note below on why rank 1 was not used) |
| TxGNN Prediction Score | 99.80% (score 0.99796, rank 2663) |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

> **Note on ranking:** TxGNN's top 9 predictions by score (rank 1 = retinal dystrophy at 99.92%, down through glycine encephalopathy) have **no clinical trials, no literature, and no mechanistic rationale** — the evidence pack's own annotations explicitly state there is "no identifiable pharmacological mechanism link" for each. These are disregarded as spurious graph-noise signals. The lowest-scoring prediction in this set, **treatment-refractory schizophrenia** (rank 10, still >99.7% score), is the only one with real trial and literature backing and a coherent mechanism, so it is used as the featured candidate in this report.

---

## Why is This Prediction Reasonable?

Drug-level mechanism of action data is formally flagged as a gap (**DG002, High severity**) — no structured MOA record was retrievable from DrugBank at this cutoff. However, the evidence pack's own repurposing rationale documents that paliperidone is the active metabolite of risperidone and acts as a **D2/5-HT2A receptor antagonist**, which is the core pharmacological mechanism underlying antipsychotic therapy.

This is not a cross-disease repurposing case in the classic sense — paliperidone's established therapeutic class already targets schizophrenia. The "new indication" here is better understood as an extension of use into a **treatment-resistant subpopulation** of the same disease, supported by real-world naturalistic and comparative-effectiveness trial designs (e.g., paliperidone palmitate case series, aripiprazole-vs-paliperidone multi-omics RCT). This is mechanistically coherent and lower-risk than the other nine model predictions, which involve unrelated congenital, ophthalmologic, neurodevelopmental, and metabolic disorders with no plausible link to central dopamine/serotonin receptor blockade.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series evaluating paliperidone palmitate effectiveness across three schizophrenia patient subgroups |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Combines pharmacotherapy with recovery-oriented programs (RECOVERYTRSGR/RECOVERYTRSBDGR) for treatment-resistant schizophrenia and bipolar disorder |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Compared clozapine vs. non-clozapine antipsychotics on inflammatory markers in treatment-refractory schizophrenia; low relevance, terminated early with minimal enrollment |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown status | 244 | Open-label multicenter RCT (SchizOMICS) comparing aripiprazole vs. paliperidone/risperidone using multi-omics data in first-episode psychosis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Review | Actas Españolas de Psiquiatría | Reviews antipsychotic pharmacotherapy evidence for schizoaffective disorder, noting the lack of disorder-specific treatment guidelines |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Review | Current Opinion in Psychiatry | Evidence-informed pharmacological approach for early-onset schizophrenia spectrum disorders, including dosing and adverse-effect monitoring |

---

## Norway Market Information

No marketing authorizations were found for paliperidone in the Norway regulatory dataset (`taiwan_regulatory.total_licenses = 0`; market status: 未上市 / Not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. A **blocking data gap (DG001)** exists: TFDA-equivalent label warnings and contraindications for paliperidone could not be retrieved at this cutoff, which prevents this candidate from entering the S1 safety pre-assessment stage. No drug-drug interaction records were found in the current query (`ddi.query_status: not_found`).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the treatment-refractory schizophrenia indication has coherent mechanistic rationale and moderate clinical evidence (L2, 4 trials, 2 reviews) that would otherwise support a "Proceed with Guardrails" call, the drug-level safety data gap (DG001, Blocking) means this candidate **cannot yet enter the S1 safety pre-assessment**, and the drug is not currently marketed in Norway (0 authorizations). The nine other TxGNN-flagged indications (retinal dystrophy, myopia subtypes, hydranencephaly, glycosylation disorder, CMT type 1G, glycine encephalopathy) should be excluded from further evaluation — they have no clinical, literature, or mechanistic support and appear to be knowledge-graph artifacts.

**To proceed, the following is needed:**
- Retrieve TFDA-equivalent label warnings/contraindications (DG001) to unblock S1 safety review
- Retrieve structured MOA data from DrugBank (DG002) to formally support the mechanistic rationale
- Confirm Norway marketing/import pathway status, since the drug currently has zero local authorizations
- If DG001/DG002 are resolved favorably, re-score treatment-refractory schizophrenia for "Proceed with Guardrails" and define specific monitoring guardrails (e.g., metabolic/EPS monitoring per antipsychotic class norms)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

