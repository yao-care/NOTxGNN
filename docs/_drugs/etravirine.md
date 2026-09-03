---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection (NNRTI-Resistant, Treatment-Experienced) to Congenital HIV Infection (Perinatal/Mother-to-Child Transmission Setting)

## One-Sentence Summary

Etravirine is a second-generation NNRTI originally used to treat HIV-1 infection in treatment-experienced adults and children with NNRTI-resistance mutations. Among the TxGNN predictions, the two clinically valid and evidence-backed candidates are **Congenital HIV Infection** (perinatal/mother-to-child transmission setting) and **AIDS-Related Complex**, each supported by **L2-level evidence** (real-world pharmacokinetic studies in pregnant women, plus background trial data). The model's top two raw-ranked predictions (simian and feline immunodeficiency virus infection) are **veterinary/animal-model diseases, not valid human indications**, and are excluded from this evaluation.

> **Methodology note:** TxGNN's raw top-10 ranking includes several outputs that are not clinically actionable: rank 1 (simian immunodeficiency virus), rank 2 (feline AIDS), and rank 3 (a rare congenital neurodevelopmental disorder) are non-human diseases or unsupported noise per the evidence pack's own rationale. Ranks 6–10 (prostate fibroma, Brenner tumor, benign reproductive neoplasms, familial hyperlipidemia) have zero supporting trials or literature and are flagged in the source data as embedding artifacts. This report therefore focuses on **rank 4 (Congenital HIV Infection)** and **rank 5 (AIDS-Related Complex)** — the only candidates with real clinical trial/literature support and coherent mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection in treatment-experienced adults/children with NNRTI-resistance mutations (per repurposing rationale; no formal `original_indications` record in source data) |
| Predicted New Indication | Congenital HIV Infection (perinatal/mother-to-child transmission prevention); AIDS-Related Complex as a secondary, closely related candidate |
| TxGNN Prediction Score | 99.79% (rank 4, congenital HIV) |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (pending blocking safety data) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA field) is not available — this is flagged in the evidence pack as a **High-severity data gap (DG002)**. Based on information embedded in the evidence pack's own rationale, etravirine is a second-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) that inhibits HIV-1 reverse transcriptase and is approved for treatment-experienced HIV-1-infected patients carrying NNRTI-resistance mutations.

Both candidate indications are not really "new" mechanisms but **extensions of the existing approved mechanism into adjacent clinical contexts**:

- **Congenital HIV Infection / perinatal exposure**: Etravirine's antiretroviral activity is already used off-label in highly treatment-experienced pregnant women to construct a suppressive regimen and reduce vertical transmission risk. Pharmacokinetic data in pregnancy (NCT00855335) and case reports (PMID 20587860) already exist, supporting extrapolation to formal use in perinatal/congenital HIV management.
- **AIDS-Related Complex (ARC)**: A historical clinical classification for symptomatic HIV infection not yet meeting full AIDS criteria. Etravirine's approved population (treatment-experienced, NNRTI-resistant HIV-1 patients) directly overlaps with this population, making this less a novel hypothesis and more a labeling/nomenclature extension.

Neither candidate represents a genuinely new pharmacological mechanism; both leverage etravirine's established antiretroviral activity in populations adjacent to its current approved use.

---

## Clinical Trial Evidence (Congenital HIV Infection)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | Completed | 77 | Etravirine-specific PK study (± darunavir/ritonavir, rilpivirine) in HIV-1-infected pregnant women — directly supports perinatal dosing safety |
| [NCT04630002](https://clinicaltrials.gov/study/NCT04630002) | Phase 1 | Completed | 54 | PK interaction study of etravirine (± darunavir/ritonavir) with GSK3640254 in healthy adults |
| [NCT01199731](https://clinicaltrials.gov/study/NCT01199731) | Phase 2b | Terminated | 30 | Etravirine used as active control arm in NNRTI-resistant, treatment-experienced HIV-1 adults |
| [NCT07412977](https://clinicaltrials.gov/study/NCT07412977) | N/A | Not yet recruiting | 5160 | French prospective cohort assessing impact of viral infections (incl. HIV) and antiviral treatment during pregnancy on maternal/child outcomes |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | Phase 4 | Completed | 1578 | IMPAACT P1026s — PK of antiretroviral/TB drugs in pregnant and postpartum women and infants (background ARV-class evidence) |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | Active, not recruiting | 618 | ATLAS: switch to long-acting cabotegravir/rilpivirine in virologically suppressed HIV-1 adults (background, not etravirine-specific) |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Phase 3 | Active, not recruiting | 1049 | ATLAS-2M: long-acting CAB+RPV dosing interval comparison (background) |
| [NCT02938520](https://clinicaltrials.gov/study/NCT02938520) | Phase 3 | Active, not recruiting | 631 | FLAIR: long-acting CAB+RPV switch maintenance (background) |
| [NCT02429791](https://clinicaltrials.gov/study/NCT02429791) | Phase 3 | Completed | 510 | Switch to dolutegravir + rilpivirine in suppressed HIV-1 adults (background) |

**Data quality note:** NCT04273165 ("Etravirine in Friedreich Ataxia") is flagged in the source data as a mapping error under this disease cluster and is excluded from this table; it is unrelated to congenital HIV infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | Cohort/Case series | Antiviral Therapy | Two case reports of darunavir + etravirine (± raltegravir) use in highly treatment-experienced pregnant women, informing perinatal safety/efficacy |

Additional supporting literature exists for the related AIDS-Related Complex candidate (PMID 19290032, cohort study on GI adverse events in HIV treatment; PMID 27067022, NNRTI-resistance mutation analysis), reinforcing the broader NNRTI-resistant HIV population rationale but not specific to congenital transmission.

---

## Norway Market Information

Etravirine currently has **no marketing authorization in Norway** — 0 licenses on record. No product/dosage form data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

**Critical limitation:** TFDA-equivalent label warnings and contraindications are flagged as a **Blocking-severity data gap (DG001)** in this evidence pack — "impact: cannot proceed to S1 safety pre-assessment." No drug-drug interaction data was found (query status: not found). This gap must be resolved before any further clinical development discussion.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The congenital HIV and AIDS-related complex candidates have reasonable mechanistic coherence and L2-level supporting evidence (etravirine is already used off-label in pregnancy with existing PK data). However, this drug is not marketed in Norway (0 authorizations) and lacks essential safety label data (Blocking gap DG001), which by definition prevents entry into the S1 safety pre-assessment stage. A "Proceed with Guardrails" recommendation cannot be responsibly issued until basic safety documentation is available.

**To proceed, the following is needed:**
- Obtain TFDA/manufacturer product label (warnings, contraindications, DDI) — Blocking gap DG001
- Obtain DrugBank/manufacturer MOA documentation — High-priority gap DG002
- Manually verify and correct trial-to-disease mapping (e.g., NCT04273165 misclassified under congenital-HIV/rare neurodevelopmental disorder clusters)
- Clarify Norway regulatory pathway status, since the drug currently holds zero local authorizations
- If pursuing the perinatal/congenital HIV indication, prioritize sourcing additional pregnancy-specific safety and dosing data beyond the single PK trial and case-series literature currently available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

