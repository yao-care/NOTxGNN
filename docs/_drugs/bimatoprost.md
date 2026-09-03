---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost: From Eyelash Hypotrichosis / Ocular Hypotension to Alopecia (Hair Loss)

## One-Sentence Summary

> Bimatoprost is a prostamide (prostaglandin F2α analog) best known clinically for treating ocular hypertension/glaucoma and for its FDA-approved use in eyelash hypotrichosis (Latisse).
> Among 10 TxGNN-predicted indications in this evidence pack, most (7 of 10) are flagged by the model's own rationale as knowledge-graph noise with no mechanistic or clinical support.
> The one candidate with genuine biological plausibility and substantial clinical-trial backing is **Alopecia**, supported by **11 clinical trials** (4 rated Grade A) and **20 publications**, including a completed Phase 2 program in both male androgenetic alopecia and female pattern hair loss.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Norway/Taiwan license data on file (drug not marketed). Publicly known original indications: ocular hypertension/open-angle glaucoma and eyelash hypotrichosis |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (MOA field marked as Data Gap). Based on known pharmacology, bimatoprost is a synthetic prostamide analog that binds prostamide/prostanoid receptors on the hair follicle and dermal papilla, prolonging the anagen (growth) phase and increasing follicle density. This mechanism is already clinically validated: bimatoprost 0.03% ophthalmic solution is FDA-approved (Latisse) specifically for eyelash hypotrichosis, meaning its hair-growth-promoting effect is not a theoretical extrapolation but an established, approved pharmacological action.

The step from eyelash hypotrichosis to scalp alopecia (androgenetic alopecia, female pattern hair loss) is a logical mechanistic extension — both involve the same follicular growth-cycle biology, differing mainly in follicle type and androgen sensitivity. This is reflected in the underlying rationale data: multiple completed Phase 2 trials directly tested bimatoprost solution against vehicle and active comparators (minoxidil) in men and women with pattern hair loss, and a Phase 4 trial confirmed efficacy/safety in a related eyelash-loss population.

It is worth noting that of the 10 TxGNN-ranked candidates in this pack, most (e.g., periodontal malformation syndromes, Dandy-Walker malformation, pulmonary arteriovenous malformation, Ambras hypertrichosis) show mechanistic directions that are absent, unrelated, or even contradictory to bimatoprost's known pharmacology, and carry no supporting trials or literature — these are assessed as Hold/model noise. Alopecia is the only candidate that combines high TxGNN score, coherent mechanism, and a substantial, largely completed clinical trial base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01325350](https://clinicaltrials.gov/study/NCT01325350) | Phase 2 | Completed | 306 | Bimatoprost solution vs. vehicle and OTC minoxidil 2% in women with female pattern hair loss |
| [NCT01023841](https://clinicaltrials.gov/study/NCT01023841) | Phase 4 | Completed | 71 | Bimatoprost 0.03% vs. vehicle for eyelash loss/hypotrichosis in children |
| [NCT01904721](https://clinicaltrials.gov/study/NCT01904721) | Phase 2 | Completed | 244 | Safety and efficacy of bimatoprost in men with androgenic alopecia (AGA) |
| [NCT01325337](https://clinicaltrials.gov/study/NCT01325337) | Phase 2 | Completed | 307 | Bimatoprost solution vs. vehicle and OTC minoxidil 5% in men with androgenic alopecia |
| [NCT01189279](https://clinicaltrials.gov/study/NCT01189279) | Phase 1 | Completed | 42 | Safety, tolerability, and PK of a new bimatoprost formulation in alopecia patients |
| [NCT02170662](https://clinicaltrials.gov/study/NCT02170662) | Phase 2 | Completed | 33 | Effect of topical bimatoprost solution on androgen-dependent scalp hair follicles |
| [NCT02848300](https://clinicaltrials.gov/study/NCT02848300) | Phase 1 | Completed | 11 | Local skin pharmacokinetics and tolerability of bimatoprost applied to scalp in AGA |
| [NCT05600673](https://clinicaltrials.gov/study/NCT05600673) | Phase 1/2 | Completed | 30 | Combined CO2 fractional laser plus bimatoprost 0.03% for alopecia areata |
| [NCT00187577](https://clinicaltrials.gov/study/NCT00187577) | NA | Completed | 14 | Latanoprost vs. bimatoprost ophthalmic solutions for eyelash regrowth in alopecia areata |
| [NCT02676310](https://clinicaltrials.gov/study/NCT02676310) | Phase 1 | Terminated | 53 | Dose-escalation safety, tolerability, and PK study of bimatoprost in men with AGA |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40252129](https://pubmed.ncbi.nlm.nih.gov/40252129/) | 2025 | RCT | Archives of Dermatological Research | CO2 fractional laser combined with bimatoprost enhances hair regrowth in alopecia areata |
| [29863806](https://pubmed.ncbi.nlm.nih.gov/29863806/) | 2018 | Guideline | The Journal of Dermatology | Japanese clinical guideline for male- and female-pattern hair loss diagnosis and treatment |
| [28264599](https://pubmed.ncbi.nlm.nih.gov/28264599/) | 2017 | Review | Expert Opinion on Investigational Drugs | Overview of bimatoprost for eyelash, eyebrow, and scalp alopecia |
| [37185388](https://pubmed.ncbi.nlm.nih.gov/37185388/) | 2023 | Review | Current Oncology | Prevention and treatment options for chemotherapy-induced alopecia |
| [32250713](https://pubmed.ncbi.nlm.nih.gov/32250713/) | 2022 | Review/Network Meta-analysis | The Journal of Dermatological Treatment | Comparative efficacy of non-surgical AGA treatments |
| [32642317](https://pubmed.ncbi.nlm.nih.gov/32642317/) | 2020 | Review | Dermatology Practical & Conceptual | Prevention and treatment of chemotherapy-induced alopecia |
| [35278027](https://pubmed.ncbi.nlm.nih.gov/35278027/) | 2022 | Cohort (open-label) | Dermatologic Therapy | Topical bimatoprost for eyelash loss in alopecia totalis/universalis |
| [35040730](https://pubmed.ncbi.nlm.nih.gov/35040730/) | 2022 | Preclinical | Drug Delivery | Enhanced-penetration topical bimatoprost formulation with in vivo hair regrowth efficacy in AGA |
| [34304865](https://pubmed.ncbi.nlm.nih.gov/34304865/) | 2021 | Review | Bulletin du Cancer | Alopecia and cancer: pathophysiology and clinical management |
| [38577618](https://pubmed.ncbi.nlm.nih.gov/38577618/) | 2024 | Preclinical | International Journal of Pharmaceutics: X | Spanlastic nanogel delivery of bimatoprost for AGA, improved cutaneous deposition |

---

## Norway Market Information

Bimatoprost currently has no marketing authorization on file for this evaluation (`market_status`: Not Marketed, `total_licenses`: 0). No license records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alopecia is supported by an L2 evidence level — multiple completed Phase 2 trials (n=244–307) directly comparing bimatoprost to vehicle/minoxidil in androgenetic and female pattern hair loss, plus an already-approved related indication (eyelash hypotrichosis) sharing the same growth-cycle mechanism. This is far stronger than the other 9 TxGNN candidates in this pack, most of which lack any supporting evidence and were assessed as Hold due to implausible or contradictory mechanisms.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings and contraindications (currently blocking safety pre-screening, DG001)
- Confirmed mechanism-of-action data from DrugBank or primary literature (DG002)
- A formal Norway/local market authorization pathway assessment, since the product is not currently marketed
- If pursuing broader alopecia subtypes, separate evaluation of lower-evidence related candidates (diffuse alopecia areata, genetic alopecia, hypotrichosis simplex of the scalp — all L4, flagged as Research Question) as exploratory extensions rather than primary indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

