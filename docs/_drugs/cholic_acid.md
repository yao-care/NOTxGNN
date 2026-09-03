---
layout: default
title: Cholic Acid
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 10
---

# Cholic Acid
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

Using the report as specified — this is a direct content-generation task per the detailed template, no additional skill applies. Note upfront: the rank-1 prediction (HIV infectious disease) has evidence that is largely tangential or **contradictory** to the predicted direction — I've written the report to reflect that honestly rather than oversell it.

---

# Cholic Acid: From No Registered Indication to HIV Infectious Disease

## One-Sentence Summary

> Cholic acid (DrugBank DB02659) has no registered indication or MOA data available in this Evidence Pack, and it is not currently marketed in Norway.
> The TxGNN model's top-ranked prediction is **HIV infectious disease** (score 99.79%),
> but the **9 supporting publications** are mostly unrelated (spermicide/contraceptive, blood-product sterilization, biomarker studies) or actively **contradict** the predicted direction — one study shows cholic acid derivatives *inducing* HIV-1 replication rather than inhibiting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no indication registered, drug not marketed |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is registered for cholic acid in this dataset. Based on the evidence pack alone, no reliable pharmacological rationale connecting cholic acid to HIV treatment can be established.

Separately from the top-ranked HIV prediction, the evidence pack does contain material (attached to a lower-ranked candidate, "vitamin deficiency disorder") indicating cholic acid is used clinically as bile acid replacement therapy (e.g., Cholbam®) in rare bile acid synthesis disorders — this is the drug's known real-world use context, though it is not the "original indication" formally recorded here.

For the HIV prediction specifically, the mechanistic rationale is weak to contradictory. The supporting literature largely concerns cholic acid's **topical spermicidal/surfactant properties** in vaginal contraceptive sponges (with incidental *in vitro* anti-HIV activity in that local context) — not systemic antiretroviral activity. More critically, one study (PMID 16610808) reports that amino-functionalized cholic acid derivatives **enhance** HIV-1 replication and syncytia formation in T cells — the opposite of a therapeutic effect. This is consistent with the pipeline's own assessment (Evidence Level L5, decision stage S0) that this prediction lacks credible mechanistic or clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro (negative direction) | J Med Chem | Amino-functionalized cholic acid derivatives **induced** HIV-1 replication and syncytia formation in T cells — contradicts the predicted therapeutic direction |
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | Clinical (spermicide/contraceptive) | Hum Reprod | Cholic acid (sodium cholate), as part of the Protectaid vaginal sponge, showed dose-dependent *in vitro* inhibition of HIV-1 reverse transcriptase — topical/local effect, not systemic antiretroviral evidence |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Cohort (biomarker/PK) | Pharmacotherapy | Evaluated plasma bile acid concentrations in HIV patients on protease inhibitor therapy as a possible hepatotoxicity marker — not a treatment study |
| [2870224](https://pubmed.ncbi.nlm.nih.gov/2870224/) | 1986 | Not classified | Lancet | Sodium cholate + tri(n-butyl)phosphate used to sterilize hepatitis/HTLV-III viruses in blood products — an ex vivo decontamination method, not a clinical HIV treatment |
| [9238301](https://pubmed.ncbi.nlm.nih.gov/9238301/) | 1997 | Not classified | Ann NY Acad Sci | Title concerns anti-STD vaginal contraceptive sponges; no abstract available |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Not classified | Aust NZ J Obstet Gynaecol | General review on future contraceptives in the context of HIV/STD protection; not specific to cholic acid |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Not classified | Ann Acad Med Singapore | Review of barrier contraception methods (mainly condoms) and STD/HIV protection; not specific to cholic acid |
| [32052857](https://pubmed.ncbi.nlm.nih.gov/32052857/) | 2020 | Not classified | Hepatology | Review on new NASH drugs in HIV patients, discussing drug-drug interaction concerns with antiretrovirals; not related to cholic acid efficacy |
| [28745428](https://pubmed.ncbi.nlm.nih.gov/28745428/) | 2017 | Not classified | ChemMedChem | Methodological paper on how the detergent Triton X-100 can distort HIV-1 protease inhibitor assay results; unrelated to cholic acid |

**Note:** None of the above literature demonstrates systemic antiretroviral efficacy of cholic acid. The most directly relevant finding (PMID 16610808) points in the opposite therapeutic direction.

---

## Norway Market Information

Cholic acid is currently **not marketed** in Norway (market status: 未上市 / Not Marketed), and no authorization records are available in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data are not currently available (flagged as Blocking data gap DG001 — TFDA-equivalent label warnings/contraindications not yet obtained).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (HIV infectious disease) is supported only by tangential or contradictory literature — no study demonstrates systemic antiretroviral efficacy of cholic acid, and one *in vitro* study shows the opposite effect (enhanced HIV-1 replication). Combined with the absence of MOA data, original indication data, and Norway market registration, this candidate does not meet the threshold to advance beyond S0.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain TFDA/label-equivalent warnings and contraindications before any S1 safety evaluation
- Resolve data gap DG002: confirm mechanism of action via DrugBank or primary literature
- Identify any dedicated pharmacological or clinical study directly testing cholic acid (or a specific derivative) for antiretroviral activity, ideally resolving the contradictory *in vitro* signal from PMID 16610808
- Clarify cholic acid's actual regulatory status and approved indication(s) in Norway/comparable markets, since none are currently recorded
- Given the weak and partly negative evidence, this candidate is not recommended for further investment unless new supporting data emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

