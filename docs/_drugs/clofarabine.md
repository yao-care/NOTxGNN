---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine: From Pediatric Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

> Clofarabine is a purine nucleoside analog originally developed and approved (FDA, 2004) for relapsed/refractory acute lymphoblastic leukemia (ALL) in pediatric patients who failed at least two prior regimens.
> The TxGNN model predicts it may also be effective for **Myeloid Leukemia (AML)**,
> with **44 clinical trials** and **20 publications** currently supporting this direction — though it is not yet marketed in Norway and key safety documentation is still missing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not licensed in Norway (0 authorizations); internationally approved for relapsed/refractory pediatric ALL (ages 1–21, ≥2 prior regimens) |
| Predicted New Indication | Myeloid Leukemia (AML) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently unavailable for clofarabine (data gap), and the drug holds no market authorization in Norway. However, the clinical trial and literature evidence collected consistently describes clofarabine as a second-generation deoxyadenosine (purine) nucleoside analog that inhibits ribonucleotide reductase and DNA polymerase, and disrupts mitochondrial membrane integrity to trigger apoptosis — a mechanism specifically targeting rapidly dividing cells. It was originally approved for relapsed/refractory pediatric ALL after other regimens failed.

ALL and AML both originate from the hematopoietic stem/progenitor compartment and share the defining biological feature that clofarabine is designed to exploit: rapidly proliferating leukemic blasts with high DNA synthesis activity. This mechanistic overlap is the biological rationale for the TxGNN prediction, and it is not merely theoretical — clofarabine has already been extensively studied "off-label" in AML, myelodysplastic syndrome (MDS), and CML blast phase, both as monotherapy and in combination regimens (with cytarabine, idarubicin, busulfan, mitoxantrone, etc.).

The depth of existing investigation reinforces this plausibility: 44 clinical trials and 20 publications specifically address clofarabine in myeloid leukemia populations, including multiple completed Phase 2 studies and a large completed Phase 2/3 programme (NCT00454480, n=2000) in AML/high-risk MDS. This indicates an area of substantial existing clinical practice rather than a purely graph-derived association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2000 | Large treatment-development programme for older AML/high-risk MDS patients, including gemtuzumab ozogamicin and tipifarnib comparator arms |
| [NCT00932412](https://clinicaltrials.gov/study/NCT00932412) | Phase 2 | Completed | 735 | Randomized CLARA (clofarabine/intermediate-dose cytarabine) vs HDAC as consolidation in newly-diagnosed younger AML |
| [NCT02665065](https://clinicaltrials.gov/study/NCT02665065) | Phase 3 | Active, not recruiting | 153 | Iomab-B + RIC transplant vs conventional care in active/relapsed/refractory AML |
| [NCT00373529](https://clinicaltrials.gov/study/NCT00373529) | Phase 2 | Completed | 116 | Single-agent clofarabine in previously untreated older AML unlikely to benefit from intensive chemotherapy |
| [NCT00067028](https://clinicaltrials.gov/study/NCT00067028) | Phase 1/2 | Completed | 116 | Clofarabine/AraC vs Clofarabine/Idarubicin vs triple combo in relapsed AML, high-grade MDS, and CML myeloid blast phase |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | Completed | 86 | Clofarabine salvage therapy in relapsed/refractory AML as bridge to allogeneic HCT |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | Completed | 50 | Clofarabine + high-dose cytarabine + G-CSF priming in newly diagnosed AML/advanced MDS/MPN |
| [NCT02686593](https://clinicaltrials.gov/study/NCT02686593) | Phase 2 | Completed | 50 | CLAM regimen (clofarabine/cytarabine/mitoxantrone) as first salvage for relapsed/refractory AML |
| [NCT00044889](https://clinicaltrials.gov/study/NCT00044889) | Phase 2 | Completed | 40 | Early open-label study of clofarabine in adult refractory/relapsed AML |
| [NCT01090167](https://clinicaltrials.gov/study/NCT01090167) | Phase 1 | Completed | 14 | Safety, tolerability and PK of clofarabine in Japanese AML patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | Phase III RCT | J Clin Oncol | AML08 trial: clofarabine can replace anthracyclines/etoposide in remission induction for childhood AML |
| [18565853](https://pubmed.ncbi.nlm.nih.gov/18565853/) | 2008 | RCT | Blood | Randomized study of clofarabine vs clofarabine+low-dose cytarabine as front-line therapy in older AML/high-risk MDS |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | Cohort | Cancers | Clofarabine-based consolidation (CLARA) improves relapse-free survival in AML with micro-complex karyotype |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Phase 2 | Cancer Medicine | CLAM (clofarabine/cytarabine/mitoxantrone) shows high response rates, effective bridge to allo-HSCT in refractory/relapsed AML |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase IB | Haematologica | Clofarabine + HDAC + liposomal daunorubicin in pediatric relapsed/refractory AML |
| [39078289](https://pubmed.ncbi.nlm.nih.gov/39078289/) | 2024 | Cohort | Clin Cancer Res | Pharmacogenomic (ACS10) score personalizes AML induction regimen selection |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | Comprehensive review of clofarabine's role in adult AML, monotherapy and combination strategies |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leukemia & Lymphoma | Review of clofarabine's role in AML treatment |
| [21182488](https://pubmed.ncbi.nlm.nih.gov/21182488/) | 2011 | Review | Curr Med Chem | Novel and emerging drugs for AML, including clofarabine pharmacology |
| [17852710](https://pubmed.ncbi.nlm.nih.gov/17852710/) | 2007 | Review | Leukemia & Lymphoma | "Clofarabine: past, present, and future" — mechanism and combination rationale |

---

## Norway Market Information

Clofarabine is currently **not marketed in Norway** (0 authorizations on record).

---

## Cytotoxicity

Clofarabine is a conventional cytotoxic antineoplastic agent (purine nucleoside antimetabolite), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine/deoxyadenosine nucleoside analog, antimetabolite class) |
| Myelosuppression Risk | High — as a DNA synthesis inhibitor targeting rapidly dividing cells, bone marrow suppression (neutropenia, thrombocytopenia, anemia) is expected; trial literature reports Grade >3 hematological toxicity as a common event (e.g., PMID 22431002) |
| Emetogenicity Classification | Moderate to High (consistent with intravenous purine analog chemotherapy) |
| Monitoring Items | CBC with differential, liver function tests, renal function/creatinine, fluid balance and blood pressure (capillary leak/hypotension risk reported with nucleoside analogs), signs of infection |
| Handling Protection | Requires standard cytotoxic/hazardous drug handling precautions (PPE, closed-system transfer devices) per antineoplastic handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myeloid leukemia indication is well supported mechanistically and by a substantial body of clinical evidence (44 trials, 20 publications, including a completed Phase III pediatric AML RCT). However, clofarabine has no current market authorization in Norway, and a **Blocking**-severity data gap (missing TFDA-equivalent label warnings/contraindications) prevents entry into the Stage 1 (S1) safety evaluation. Until this is resolved, neither "Go" nor "Proceed with Guardrails" can be responsibly recommended.

**To proceed, the following is needed:**
- Official prescribing information / SmPC with warnings, contraindications, and drug-drug interaction data (resolves the Blocking gap)
- Detailed mechanism-of-action and DrugBank pharmacological classification data (resolves the High-severity gap)
- Confirmation of Norway/EU marketing authorization status or applicable off-label/named-patient access pathways for AML
- Systematic relevance grading of the 44 myeloid leukemia trials and 20 publications (currently unclassified/"pending")
- Route-of-administration and dosing feasibility assessment for the AML population (currently unassessed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

