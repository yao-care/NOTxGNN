---
layout: default
title: Peginterferon Alfa-2A
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Peginterferon Alfa-2A
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

# Peginterferon Alfa-2a: From Chronic Hepatitis C to Hepatitis B Virus Infection

## One-Sentence Summary

> Peginterferon alfa-2a is the pegylated interferon best known as Pegasys, with chronic hepatitis C as its foundational, globally established use.
> The TxGNN model's top prediction for this drug is **Hepatitis B Virus Infection**, an indication supported by **50 clinical trials** and **20 publications** — though as detailed below, this is best understood as a confirmation of an already-approved use rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C (established international indication; not currently licensed in this jurisdiction) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from the standard drug reference (DG002, data gap). However, the evidence pack's own repurposing rationale supplies the key mechanistic detail: peginterferon alfa-2a is an already-approved treatment for chronic hepatitis B (marketed as Pegasys), working by inducing interferon-stimulated gene expression and enhancing host immune clearance of HBV. This is the same broad antiviral/immunomodulatory mechanism that underlies its long-standing role as standard-of-care therapy for chronic hepatitis C, as reflected throughout the clinical trial evidence below (e.g., "the current standard of care in HCV patients consists of a combination of peg-IFN alpha and ribavirin").

Because both chronic hepatitis B and chronic hepatitis C are viral, hepatotropic infections responsive to type-I interferon signaling, the mechanistic bridge between the two is well established rather than speculative. Importantly, the evidence pack itself flags that this particular signal — HBV infection — is **not a novel indication but an existing, on-label use** ("MOA明確且非新適應症，屬既有標籤內用途"). In other words, TxGNN has correctly recovered a known therapeutic relationship rather than surfaced a new hypothesis. This should be read as a validation of the model's reliability on this drug, and it also means the extensive trial base below reflects decades of confirmatory research rather than early-stage exploratory signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01937728](https://clinicaltrials.gov/study/NCT01937728) | Phase 4 | Completed | 542 | Tailored (individualized) duration regimens with peginterferon alfa-2a plus ribavirin, guided by viral kinetics |
| [NCT00436163](https://clinicaltrials.gov/study/NCT00436163) | Phase 4 | Completed | 39 | Baltic post-marketing study: efficacy/safety of peginterferon alfa-2a 180 mcg weekly in HBeAg-positive CHB, treatment-naive |
| [NCT01706575](https://clinicaltrials.gov/study/NCT01706575) | Phase 2 | Completed | 76 | Adding Pegasys to nucleos(t)ide analogue therapy in HBeAg-negative genotype D CHB with stable HBV DNA suppression |
| [NCT00435825](https://clinicaltrials.gov/study/NCT00435825) | Phase 4 | Completed | 551 | 4-arm RCT comparing 24 vs 48 weeks and 90 vs 180 mcg PEGASYS doses for HBeAg seroconversion and safety |
| [NCT01011738](https://clinicaltrials.gov/study/NCT01011738) | N/A | Completed | 1842 | Large multicenter observational cohort evaluating on-treatment predictors of response to Pegasys in HBeAg+/- CHB |
| [NCT02604823](https://clinicaltrials.gov/study/NCT02604823) | Phase 4 | Completed | 307 | Efficacy and safety of Pegasys in naive, interferon- or lamivudine-pretreated HBeAg-positive CHB patients |
| [NCT01730508](https://clinicaltrials.gov/study/NCT01730508) | N/A | Completed | 978 | Multicenter observational cohort in Chinese HBeAg-negative CHB patients receiving Pegasys per local label |
| [NCT00940485](https://clinicaltrials.gov/study/NCT00940485) | Phase 4 | Completed | 200 | Combination/sequential peginterferon alfa-2a plus entecavir for optimizing HBeAg seroconversion |
| [NCT01086085](https://clinicaltrials.gov/study/NCT01086085) | Phase 4 | Completed | 265 | Response-guided treatment (RGT) optimization of PEGASYS in HBeAg-positive CHB |
| [NCT03210506](https://clinicaltrials.gov/study/NCT03210506) | N/A | Unknown | 120 | Mechanistic study of cytokine changes during peginterferon alfa-2a and nucleoside analogue therapy, supporting immune-regulatory MOA |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15987917](https://pubmed.ncbi.nlm.nih.gov/15987917/) | 2005 | RCT | N Engl J Med | Pivotal registration trial: peginterferon alfa-2a ± lamivudine for HBeAg-positive chronic hepatitis B |
| [30318613](https://pubmed.ncbi.nlm.nih.gov/30318613/) | 2019 | RCT | Hepatology | Entecavir/peginterferon alfa-2a combination in HBeAg-positive immune-tolerant children with CHB |
| [30549279](https://pubmed.ncbi.nlm.nih.gov/30549279/) | 2019 | RCT | Hepatology | Entecavir and peginterferon alfa-2a in adults with immune-tolerant chronic HBV infection |
| [30865588](https://pubmed.ncbi.nlm.nih.gov/30865588/) | 2019 | Systematic Review/Meta-analysis | Antiviral Therapy | Individual participant data meta-analysis establishing peginterferon alfa-2a treatment stopping rules in CHB |
| [29715359](https://pubmed.ncbi.nlm.nih.gov/29715359/) | 2018 | Review | JAMA | Comprehensive review of chronic hepatitis B infection and treatment landscape |
| [21423260](https://pubmed.ncbi.nlm.nih.gov/21423260/) | 2011 | Review | Nat Rev Gastroenterol Hepatol | Overview of hepatitis B therapy, including interferon-based approaches |
| [18220290](https://pubmed.ncbi.nlm.nih.gov/18220290/) | 2008 | RCT (Phase 3 registration data) | Hepatology | HBeAg and HBV DNA as outcome predictors during peginterferon alfa-2a therapy (n=271, large multinational trial) |
| [33720089](https://pubmed.ncbi.nlm.nih.gov/33720089/) | 2021 | RCT | J Pediatr Gastroenterol Nutr | Peginterferon alfa-2a plus lamivudine or entecavir in children with immune-tolerant CHB |
| [26700861](https://pubmed.ncbi.nlm.nih.gov/26700861/) | 2015 | RCT | Virology Journal | Double-blind randomized trial of long-term peginterferon alfa-2a effects in Japanese CHB patients |
| [33339708](https://pubmed.ncbi.nlm.nih.gov/33339708/) | 2021 | Cohort | J Formos Med Assoc | Virological/immunological predictors of long-term outcomes of peginterferon alfa-2a in HBeAg-negative CHB |

---

## Norway Market Information

No authorizations are currently registered for this drug in this jurisdiction (market status: **Not Marketed**, total licenses: 0). All clinical and literature evidence above reflects use of the product (marketed internationally as Pegasys) in other jurisdictions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for peginterferon alfa-2a in hepatitis B virus infection is exceptionally strong (L1 — multiple completed Phase 3/4 RCTs plus a systematic review/meta-analysis), but this reflects an already-established, on-label indication rather than a novel repurposing discovery, and the drug currently has no local market authorization.

**To proceed, the following is needed:**
- Confirm local (TFDA-equivalent) label status and obtain the official package insert for warnings/contraindications (DG001)
- Obtain formal MOA documentation from DrugBank or manufacturer labeling (DG002)
- Clarify regulatory pathway for market authorization given current "Not Marketed" status
- Given that this signal is a known indication rather than a new discovery, consider redirecting repurposing-focused review effort toward lower-ranked, evidence-poor candidates in this pack (e.g., hepatitis E virus infection, L3) where genuine novelty assessment is more relevant
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

