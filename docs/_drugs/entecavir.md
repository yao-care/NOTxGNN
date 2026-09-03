---
layout: default
title: Entecavir
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Entecavir
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

# Entecavir: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

Entecavir is a guanosine nucleoside analogue whose established, real-world use is the treatment of chronic hepatitis B virus (HBV) infection — though this original indication is not captured in the source dataset (data gap). The TxGNN model's top-ranked prediction points to **chronic hepatitis C virus infection (HCV)**, but the accompanying evidence — 45 clinical trials and 20 publications — consists almost entirely of HBV-focused studies with no direct anti-HCV efficacy data, and the mechanistic rationale explicitly argues **against** biological plausibility (HCV has no reverse-transcription step for entecavir to target).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis B virus infection (well-established clinical use; not present in the source regulatory/licensing dataset) |
| Predicted New Indication | Chronic Hepatitis C virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for entecavir is not available in this evidence pack (data gap, ID: DG002). Based on established pharmacology, entecavir is a guanosine nucleoside analogue that undergoes intracellular phosphorylation to compete with the natural substrate for incorporation by HBV reverse transcriptase, blocking priming, reverse transcription, and DNA synthesis. This mechanism is specific to reverse-transcribing viruses.

Hepatitis C virus, however, is a positive-strand RNA virus that replicates via an RNA-dependent RNA polymerase and has no reverse-transcription step. The repurposing rationale attached to this candidate is explicit on this point: *"Entecavir 標的為 HBV 反轉錄酶，HCV 為 RNA 病毒依賴 RNA 聚合酶（無反轉錄步驟），機轉上無直接抑制 HCV 複製之理論基礎"* — there is no direct theoretical basis for entecavir inhibiting HCV replication. Nearly all of the clinical trials retrieved for this candidate involve entecavir being used to manage the **HBV component** of HBV/HCV co-infection (e.g., preventing HBV reactivation during HCV DAA therapy), not as an anti-HCV agent itself.

**Caveat:** This dataset lists `original_indications` as empty, which appears to be a data-collection gap rather than a true absence of indication — entecavir's well-documented core indication is chronic HBV infection (this is independently corroborated by rank-2 evidence in the same evidence pack, which carries an L1 evidence level and a "Proceed with Guardrails" recommendation). Readers should treat the HCV prediction below as a **low-confidence, high-score TxGNN artifact** rather than a validated repurposing opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | HCV/HBV co-infection study; entecavir used only to manage HBV reactivation risk during DAA therapy for HCV — not tested as an HCV treatment (relevance grade C) |
| [NCT00065507](https://clinicaltrials.gov/study/NCT00065507) | Phase 3 | Completed | 195 | Entecavir vs. adefovir in HBV with hepatic decompensation; HBV-only trial, no HCV relevance (relevance grade C) |
| [NCT00371150](https://clinicaltrials.gov/study/NCT00371150) | Phase 4 | Completed | 131 | Observational antiviral effect of entecavir in Black/Hispanic patients with chronic HBV (not HCV) |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | Completed | 44 | Viral kinetics of telbivudine vs. entecavir in HBeAg-positive chronic HBV |
| [NCT00096785](https://clinicaltrials.gov/study/NCT00096785) | Phase 3 | Completed | 69 | Entecavir vs. adefovir viral load reduction in nucleoside-naive chronic HBV |
| [NCT01037166](https://clinicaltrials.gov/study/NCT01037166) | Phase 2 | Completed | 84 | Entecavir antiviral activity in Japanese HBV patients with incomplete lamivudine response |
| [NCT01022801](https://clinicaltrials.gov/study/NCT01022801) | Phase 2 | Completed | 120 | Entecavir vs. lamivudine dose-response in Japanese chronic HBV patients |
| [NCT02881008](https://clinicaltrials.gov/study/NCT02881008) | Phase 1/2 | Completed | 48 | Myrcludex B vs. entecavir in HBeAg-negative chronic HBV |

**Note:** None of the retrieved trials directly test entecavir's efficacy against HCV; all involve HBV treatment or HBV management within HBV/HCV co-infected populations.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | Cohort | Viruses | In anti-HCV-antibody-positive chronic HBV patients treated with nucleos(t)ide analogues (including entecavir), HCV RNA levels were tracked but no antiviral effect against HCV was demonstrated |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | Review | Expert Opin Pharmacother | Reviews treatment advances for HBV/HCV co-infection; entecavir discussed only as HBV-directed therapy |
| [32527114](https://pubmed.ncbi.nlm.nih.gov/32527114/) | 2021 | Review | Chin Clin Oncol | Discusses timing of HBV and HCV antiviral therapy in HCC patients; no direct anti-HCV role for entecavir |
| [28230928](https://pubmed.ncbi.nlm.nih.gov/28230928/) | 2017 | Cohort | J Gastroenterol Hepatol | Investigates HBV reactivation risk during DAA therapy for HCV in co-infected patients |
| [22959099](https://pubmed.ncbi.nlm.nih.gov/22959099/) | 2013 | Case report/Review | Clin Res Hepatol Gastroenterol | Describes therapeutic challenges of HBV/HCV dual infection; entecavir used for HBV component |
| [36873880](https://pubmed.ncbi.nlm.nih.gov/36873880/) | 2023 | Case report | Frontiers in Medicine | Reports unusual viral evolution following antiviral therapy in a concurrent HBV/HCV-infected patient |

---

## Norway Market Information

Entecavir is currently **not marketed in Norway** according to the source dataset (0 authorizations, no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information. A drug label / regulatory warning dataset was not available for this evaluation (data gap DG001, marked as Blocking — this currently prevents a formal S1 safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (HCV) lacks a plausible mechanistic basis — entecavir targets HBV reverse transcriptase, while HCV replication does not involve reverse transcription — and no retrieved clinical trial or publication demonstrates direct anti-HCV efficacy; all supporting evidence instead reflects entecavir's established role in managing HBV in HBV/HCV co-infected patients. Combined with a Blocking-severity data gap on regulatory safety labeling, this candidate does not currently meet the bar to proceed.

**To proceed, the following is needed:**
- TFDA/official product label (warnings, contraindications) to clear the Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- If pursued further, a re-evaluation of whether "chronic hepatitis C" is the correct target — consider instead reviewing the co-listed **chronic hepatitis B virus infection** prediction (evidence level L1, "Proceed with Guardrails"), which reflects entecavir's true, well-established indication and is better supported for any repurposing or lifecycle-extension analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

