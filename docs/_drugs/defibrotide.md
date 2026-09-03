---
layout: default
title: Defibrotide
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 10
---

# Defibrotide
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

# Defibrotide: From Hepatic Veno-Occlusive Disease to Thrombotic Thrombocytopenic Purpura

## One-Sentence Summary

Defibrotide's established clinical use — evident from trial context (NCT02851407, Phase 3) — is prevention of hepatic veno-occlusive disease (VOD) in patients undergoing hematopoietic stem cell transplantation (HSCT). TxGNN's top-ranked prediction (pseudo-von Willebrand disease) has **zero supporting evidence** and is explicitly flagged by the evidence review as a likely knowledge-graph artifact. The most credible predicted new indication is **Thrombotic Thrombocytopenic Purpura (TTP) / transplant-associated thrombotic microangiopathy (TA-TMA)**, supported by **11 publications** spanning 1984–2023, though with **no dedicated clinical trials** and **no market presence in Norway**.

> **Note on candidate selection**: This evidence pack contains 10 TxGNN-predicted indications. Eight of them (ranks 1–3, 5–9) have **no clinical trial or literature evidence at all** and are scored L5/Hold — several rationales explicitly state the mechanistic direction is *opposite* to defibrotide's antithrombotic profile (e.g., Glanzmann thrombasthenia, factor V deficiency, collagen receptor defects are *bleeding* disorders, not thrombotic ones). Only rank 4 (TTP) and rank 10 (thrombocytopenic purpura, near-duplicate evidence set) reach L3/S2. This report focuses on TTP as the scientifically defensible candidate rather than mechanically reporting the highest raw TxGNN score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (0 licenses; unmarketed in Norway). Trial context (NCT02851407) indicates established use in prevention of hepatic veno-occlusive disease (VOD) in HSCT patients |
| Predicted New Indication | Thrombotic Thrombocytopenic Purpura (TTP) |
| TxGNN Prediction Score | 99.71% (rank 3665 overall) |
| Evidence Level | L3 (observational studies / case series, no RCTs) |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (Data Gap). Based on the available trial and literature context, defibrotide is a polydeoxyribonucleotide with antithrombotic, profibrinolytic, and endothelial-protective properties, and its established use is prevention/treatment of hepatic VOD in HSCT patients — a condition driven by sinusoidal endothelial injury and microvascular thrombosis.

TTP and transplant-associated thrombotic microangiopathy (TA-TMA) share substantial pathophysiological overlap with VOD: both occur predominantly in the HSCT setting and are driven by endothelial injury with consumptive microthrombus formation. This overlap is reflected directly in the literature — several papers on defibrotide-and-TTP are framed specifically in transplant patients (e.g., Uderzo 2000, Corti 2002), and reviews of TA-TMA (Ikezoe 2018, Choi 2009, Batts & Lazarus 2007) describe essentially the same endothelial-injury mechanism defibrotide is designed to address in VOD.

However, this mechanistic plausibility is tempered by evidence quality: no RCTs exist, most literature is older case series/case reports (1984–2002), and — importantly — one publication (Perotti 1994) reports TTP occurring **as an adverse event following** defibrotide therapy, rather than as a treatment response. This creates a safety signal that must be resolved before clinical application (see Safety Considerations below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Note: NCT02851407, a completed Phase 3 VOD-prevention trial, appears elsewhere in this evidence pack but was graded "C" / not relevant by the evidence reviewer for platelet-disorder indications — it is not counted as TTP evidence.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11100281](https://pubmed.ncbi.nlm.nih.gov/11100281/) | 2000 | Cohort | Bone Marrow Transplant | TTP incidence and risk factors in 131 pediatric leukemia patients undergoing HSCT |
| [11960280](https://pubmed.ncbi.nlm.nih.gov/11960280/) | 2002 | Case series | Bone Marrow Transplant | Defibrotide described as a promising treatment for TTP in HSCT patients |
| [8317470](https://pubmed.ncbi.nlm.nih.gov/8317470/) | 1993 | Case series | Am J Hematol | Treatment of TTP with defibrotide |
| [6547211](https://pubmed.ncbi.nlm.nih.gov/6547211/) | 1984 | Case series | Nephron | Defibrotide as a new antithrombotic agent in HUS/TTP-related acute renal failure |
| [30305540](https://pubmed.ncbi.nlm.nih.gov/30305540/) | 2018 | Review | Rinsho Ketsueki | Management of transplant-associated thrombotic microangiopathy (TA-TMA) |
| [17603513](https://pubmed.ncbi.nlm.nih.gov/17603513/) | 2007 | Review | Bone Marrow Transplant | Diagnosis and treatment progress in TA-TMA |
| [19228075](https://pubmed.ncbi.nlm.nih.gov/19228075/) | 2009 | Review | Drugs | TMA in HSCT: diagnosis and treatment overview |
| [10775024](https://pubmed.ncbi.nlm.nih.gov/10775024/) | 2000 | Case report | Clin Appl Thromb Hemost | Defibrotide used in recurrent TTP |
| [37001283](https://pubmed.ncbi.nlm.nih.gov/37001283/) | 2023 | In-vitro/mechanistic | Thrombosis Research | Defibrotide mitigates endothelial cell injury from COVID-19/TMA patient plasmas |
| [7896218](https://pubmed.ncbi.nlm.nih.gov/7896218/) | 1994 | Case report (Adverse Event) | Haematologica | **TTP reported as an adverse event after defibrotide therapy** — safety signal, not efficacy evidence |

---

## Norway Market Information

Defibrotide is currently **not marketed in Norway** — 0 marketing authorizations are on record in this evidence pack. No product/dosage-form data is available.

---

## Safety Considerations

- **Data gap flagged as Blocking**: No TFDA/label warnings or contraindications are available in this evidence pack (DG001, severity: Blocking) — this prevents any preliminary safety assessment.
- **Safety signal from literature**: One case report (Perotti et al., 1994, Haematologica) describes TTP occurring *after* defibrotide therapy, i.e., as a possible adverse event rather than a therapeutic benefit. This directly conflicts with the repurposing hypothesis and must be reconciled before proceeding.
- No structured drug-drug interaction data is available (query returned no results).

Please refer to the package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(conditional — see rationale)*

**Rationale:**
Among 10 TxGNN-predicted indications, TTP/TA-TMA is the only one with a mechanistically coherent rationale (shared endothelial-injury pathophysiology with defibrotide's known VOD use) and multi-decade literature support (11 publications, L3 evidence). However, the absence of RCTs, the presence of a conflicting adverse-event report, and a **Blocking-severity safety data gap** mean this cannot advance to formal evaluation (S1) without additional data.

**To proceed, the following is needed:**
- TFDA/manufacturer label warnings and contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Structured mechanism of action data (DG002, High)
- Resolution of the conflicting signal between defibrotide-as-treatment (case series) vs. defibrotide-as-cause (Perotti 1994 AE report) for TTP
- Confirmation of the drug's actual approved original indication(s), since `original_indications` is currently empty in this pack
- If pursued further, a targeted literature/registry search specifically for TA-TMA (rather than idiopathic TTP) given the stronger mechanistic and clinical-context overlap with defibrotide's known VOD indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

