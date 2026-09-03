---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Ustekinumab
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

# Ustekinumab: From Plaque Psoriasis to Dermatitis

## One-Sentence Summary

> Ustekinumab (an IL-12/IL-23 p40 antagonist) was originally developed for moderate-to-severe plaque psoriasis, psoriatic arthritis, Crohn's disease, and ulcerative colitis.
> The TxGNN model predicts it may also be effective for **Dermatitis** (particularly atopic dermatitis),
> with **7 clinical trials** and **20 publications** currently supporting this direction, including two completed Phase 2 RCTs testing this exact indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe plaque psoriasis, psoriatic arthritis, Crohn's disease, ulcerative colitis (per literature evidence, PMID 36208443) |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The DrugBank record for ustekinumab does not provide a structured `original_moa` field, but the literature evidence gathered in this pack consistently describes its mechanism: ustekinumab is a fully human IgG1 monoclonal antibody that binds the shared p40 subunit of IL-12 and IL-23, thereby suppressing Th1, Th17, and Th22 activation (PMID 27304428). This IL-12/23 blockade is the same mechanism that underlies its approved efficacy in plaque psoriasis, an inflammatory Th17-driven skin disease.

Atopic dermatitis — the dermatitis subtype most represented in the evidence below — also involves Th17/Th22 activation alongside the classic Th2 axis, giving a plausible mechanistic bridge from psoriasis to dermatitis. Both are chronic, immune-mediated inflammatory skin diseases, and clinical investigators have directly tested this hypothesis: two completed Phase 2 RCTs (in Japanese and Western populations) evaluated ustekinumab specifically in moderate-to-severe/severe atopic dermatitis, along with a mechanistic study showing down-regulation of Th2/Th22 gene expression after treatment (PMID 27745907). This combination of shared pathway biology and existing dedicated trials makes the TxGNN prediction mechanistically reasonable rather than purely statistical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | Completed | 79 | Randomized, double-blind, placebo-controlled trial of ustekinumab in adult Japanese patients with severe atopic dermatitis |
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | Completed | 32 | Randomized pilot study of ustekinumab in chronic atopic dermatitis patients with sub-optimal response to prior therapy |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | Completed | 676 | Head-to-head RCT of secukinumab vs. ustekinumab (PASI-based efficacy) in moderate-to-severe plaque psoriasis |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | Recruiting | 45 | Suction-blister contact dermatitis model studying how biologic therapies (incl. anti-IL12/23) modulate skin inflammation |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | Completed | 126 | Cardiovascular risk assessment in severe psoriasis patients treated with biologic agents including ustekinumab |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | Completed | 1000 | Retrospective cohort evaluating 10-year drug survival of biologics (including ustekinumab) in cutaneous psoriasis/psoriatic arthritis |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | Not yet recruiting | 10 | Microdevice platform testing multiple FDA-approved atopic dermatitis/psoriasis drugs directly in skin |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT (Phase 2) | Br J Dermatol | Randomized, double-blind, placebo-controlled Phase 2 study showing ustekinumab efficacy/safety in Japanese patients with severe atopic dermatitis |
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT (Phase 2) | Exp Dermatol | Ustekinumab (IL-12/IL-23p40 antagonist) evaluated for efficacy and safety in adults with moderate-to-severe atopic dermatitis |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | Observational (real-world) | J Dermatolog Treat | Real-world evidence analysis on effectiveness of ustekinumab in atopic dermatitis patients |
| [27745907](https://pubmed.ncbi.nlm.nih.gov/27745907/) | 2017 | Clinical study | J Am Acad Dermatol | Ustekinumab treatment in severe atopic dermatitis shown to down-regulate Th2/Th22 gene expression |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | Systematic Review | J Dermatolog Treat | Systematic review of ustekinumab efficacy and safety in the treatment of atopic dermatitis |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Systematic Review/Meta-analysis | Allergy | EAACI evidence review of systemic treatments (including biologics) for moderate-to-severe atopic dermatitis |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | Systematic Review/Meta-analysis | Am J Clin Dermatol | Meta-analysis assessing whether biologics, including ustekinumab, are efficacious in atopic dermatitis |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Review | Dermatol Ther | Review of off-label uses of ustekinumab beyond its approved psoriasis/Crohn's/UC indications |
| [39987634](https://pubmed.ncbi.nlm.nih.gov/39987634/) | 2025 | Observational (FAERS analysis) | Int Immunopharmacol | Real-world adverse-event analysis of ustekinumab safety in psoriasis and psoriatic arthritis |
| [37929636](https://pubmed.ncbi.nlm.nih.gov/37929636/) | 2024 | Case Report | Australas J Dermatol | Case of dual biologic therapy (ustekinumab + dupilumab) in a patient with severe atopic dermatitis and Crohn's disease, no drug interaction observed over 7 months |

---

## Norway Market Information

Ustekinumab is currently **not marketed** in Norway under this evidence pack, and no authorization records (product licenses, dosage forms) are available in the dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-drug interaction data are flagged in the evidence pack as a Blocking data gap — TFDA-equivalent label information has not yet been retrieved and is required before this candidate can proceed to a formal safety evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale and existing evidence base (7 trials, 20 publications, including two completed Phase 2 RCTs directly testing ustekinumab in atopic dermatitis) are encouraging, but a Blocking data gap on official label warnings/contraindications prevents entry into the safety evaluation stage, and the drug is not currently marketed in Norway.

**To proceed, the following is needed:**
- Official package insert / label data (warnings, contraindications) to resolve the Blocking data gap and enable a formal S1 safety review
- Confirmation of detailed mechanism-of-action documentation via DrugBank (to resolve the MOA data gap)
- Assessment of regulatory pathway for market entry in Norway, since no authorizations currently exist
- Additional Phase 3-level trial data specific to the dermatitis indication, as current direct evidence is limited to completed Phase 2 studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

