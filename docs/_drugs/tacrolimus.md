---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tacrolimus: From Atopic Dermatitis (Topical) to Seborrheic Dermatitis

## One-Sentence Summary

> Tacrolimus is a calcineurin inhibitor whose topical ointment form (Protopic) is an established treatment for atopic dermatitis.
> The TxGNN model predicts it may also be effective for **Seborrheic Dermatitis**,
> with **2 clinical trials** (both directly on tacrolimus in facial seborrheic dermatitis) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded as a structured field in this evidence pack (no Norway license text available); per the evidence pack's own repurposing rationale, tacrolimus ointment is already an established topical treatment for atopic dermatitis |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data (`original_moa`) is not available in this evidence pack. Based on the information that is available, tacrolimus is a **calcineurin inhibitor** — a topical immunomodulator class already approved for inflammatory skin disease (atopic dermatitis). Its mechanism works by blocking calcineurin-mediated T-cell activation, which down-regulates the inflammatory cytokine cascade.

Seborrheic dermatitis shares key pathophysiological features with atopic dermatitis: it is a chronic inflammatory skin condition with a T-cell-mediated inflammatory component, and it also involves an aberrant immune response to *Malassezia* yeast colonization. Since tacrolimus's anti-inflammatory action is not specific to any one antigen trigger, its efficacy in atopic dermatitis provides a mechanistically plausible rationale for extension to seborrheic dermatitis.

This is further reinforced by the fact that two other TxGNN-predicted indications in this evidence pack — **generalized dermatitis** (rank 3, also L1 evidence) and **parapsoriasis/pityriasis lichenoides** (rank 2, L4 evidence) — cluster around the same T-cell-mediated inflammatory mechanism, suggesting the model is consistently capturing tacrolimus's calcineurin-inhibitory anti-inflammatory action across a family of related dermatoses rather than flagging an isolated, mechanistically unrelated signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic) as maintenance treatment for severe facial seborrheic dermatitis, aiming to reduce relapse frequency and prolong remission versus topical steroids |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Assessed proactive once/twice-weekly application of 0.1% tacrolimus ointment to maintain remission and reduce exacerbation in adult facial seborrheic dermatitis |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | RCT | Annals of Dermatology | Maintenance therapy with 0.1% tacrolimus ointment reduces relapse in facial seborrheic dermatitis, extending the intermittent low-dose TCI strategy proven in atopic dermatitis |
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT | J Am Acad Dermatol | Multicenter, double-blind RCT comparing tacrolimus 0.1% vs ciclopirox olamine 1% for long-term maintenance therapy in severe facial seborrheic dermatitis |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | RCT | J Am Acad Dermatol | Single-blind RCT comparing hydrocortisone 1% vs tacrolimus 0.1% ointment in adults with facial seborrheic dermatitis; supports tacrolimus's anti-inflammatory and fungicidal properties |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | RCT | Annals of Parasitology | Compared sertaconazole 2% cream vs tacrolimus 0.03% cream efficacy in 60 seborrheic dermatitis patients |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | RCT | Indian J Dermatol Venereol Leprol | Compared oral itraconazole (2 days) plus topical tacrolimus vs topical tacrolimus alone for maintenance treatment of seborrheic dermatitis in Vietnam |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical antifungal, keratolytic, and corticosteroid/TCI therapies for facial seborrheic dermatitis |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Cochrane SR/NMA | Clin Exp Allergy | Network meta-analysis of topical anti-inflammatory treatments (including calcineurin inhibitors) for eczema and related inflammatory dermatoses |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Reviews pathophysiology, safety, and efficacy of topical calcineurin inhibitors (tacrolimus/pimecrolimus) specifically in seborrheic dermatitis |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open-label Pilot Study | J Am Acad Dermatol | Pilot study of 18 seborrheic dermatitis patients treated with 0.1% tacrolimus for 28 days; 61% achieved complete clearance |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Reviews current status and therapeutic horizons of facial seborrheic dermatitis treatment |

---

## Norway Market Information

Currently no marketing authorizations recorded for tacrolimus in Norway (`total_licenses = 0`, market status: 未上市/Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were queried but not found in this evidence pack — `DG001` flags this as a blocking gap that must be resolved before a full safety evaluation.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3/4 trials directly test tacrolimus ointment in facial seborrheic dermatitis, supported by an RCT-rich literature base (including a head-to-head RCT vs. ciclopirox olamine and vs. hydrocortisone), justifying the L1 evidence level and warranting guarded advancement. However, the drug is not currently marketed in Norway under this data set, and core safety documentation (warnings/contraindications/DDI) is missing.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings and contraindications (`DG001`, blocking)
- Official DrugBank mechanism-of-action data (`DG002`)
- Verification of Norway/global marketing status discrepancy (tacrolimus ointment is marketed internationally as Protopic; confirm whether "未上市" reflects this specific product/indication or a data gap)
- Drug-drug interaction profile for topical tacrolimus in the seborrheic dermatitis population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

