---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

Using the report template above (matching the Evidence Pack schema exactly) — here is the report:

---

# Dexamethasone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

> Dexamethasone is a potent, long-acting synthetic corticosteroid with broadly established anti-inflammatory and immunosuppressive uses.
> The TxGNN model predicts it may be effective for **Alopecia Areata**,
> and unlike most co-occurrence-driven predictions, this one is backed by **genuine literature evidence** — including RCTs and systematic reviews on dexamethasone oral mini-pulse (OMP) therapy — even though no clinical trial in the evidence pack was designed specifically for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (dexamethasone is a synthetic corticosteroid with broad, well-established anti-inflammatory/immunosuppressive uses; `original_moa` and `original_indications` are data gaps in this pack) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% (rank 168) |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the formal MOA field (data gap). However, the evidence pack's repurposing rationale provides a clear mechanistic account: dexamethasone is a potent, long-acting glucocorticoid that produces systemic immunosuppression, blocking the T-cell-mediated peribulbar inflammatory infiltrate that drives the autoimmune attack on hair follicles in alopecia areata (AA).

Importantly, this is **not a novel mechanistic hypothesis** — dexamethasone mini-pulse (oral or IV) therapy is already an established off-label treatment option in dermatology practice for moderate-to-severe AA, particularly in patients who are ineligible for or cannot access JAK inhibitors. The TxGNN prediction therefore recovers a real, clinically-practiced use rather than proposing an untested mechanistic leap.

It is worth noting that none of the clinical trials automatically linked to this prediction in the evidence pack are actually AA trials — they are oncology trials (multiple myeloma, mesothelioma, NSCLC, etc.) where dexamethasone was used as supportive/combination therapy, and the database link is a drug co-occurrence false positive. The genuine supporting evidence for this indication comes entirely from the **literature** (PubMed), not from registered clinical trials.

---

## Clinical Trial Evidence

Currently no clinical trials specifically evaluating dexamethasone for alopecia areata are registered. The clinical trials returned during evidence collection (e.g., NCT02004275, NCT02685826, NCT05408026 — all multiple myeloma trials using dexamethasone as a combination-therapy backbone) were flagged in the evidence pack as **database co-occurrence false positives**, unrelated to alopecia areata, and are therefore excluded from this table.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Randomized comparison of low-dose dexamethasone oral mini-pulse vs. DPCP contact sensitization in severe pediatric AA |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | RCT (multicentric) | Dermatologic Therapy | Multicentric study of oral dexamethasone mini-pulse therapy for moderate-to-severe AA; positioned as an accessible alternative to JAK inhibitors |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic review / Network meta-analysis | Archives of Dermatological Research | Compares systemic steroids, oral JAK inhibitors, and contact immunotherapy for severe AA; no single treatment shown clearly superior |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Reviews pulse-dose corticosteroid dosing regimens and associated side effects for AA in children |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective cohort | Journal of Clinical Medicine | Real-world evidence on dexamethasone mini-pulse therapy efficacy/safety and predictors of response in AA |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Prospective cohort | Dermatologic Therapy | Compares 1-day vs 3-day IV dexamethasone pulse regimens plus topical clobetasol in 73 children with severe AA |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Cohort, long-term follow-up | Dermatologic Therapy | Long-term (median 96-month) follow-up of combined oral dexamethasone pulse + topical corticosteroid in 65 children with severe AA |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative study | Dermatology (Basel) | Compares efficacy, relapse rate, and side effects across three systemic corticosteroid regimens for AA |
| [17656876](https://pubmed.ncbi.nlm.nih.gov/17656876/) | 2002 | Clinical commentary/review | Indian J Dermatol Venereol Leprol | Discusses risk-benefit of dexamethasone pulse therapy for extensive AA |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Case series | The Journal of Dermatology | Twice-weekly 5 mg dexamethasone oral pulse in 30 patients with extensive AA; reports terminal hair regrowth outcomes |

---

## Norway Market Information

No marketing authorizations are currently registered in Norway (`total_licenses = 0`, `licenses = []`).

---

## Safety Considerations

Please refer to the package insert for safety information. `key_warnings`, `contraindications`, and DDI data are not available in this evidence pack (query status: not found).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The literature evidence — including two RCTs, a systematic review/network meta-analysis, and multiple cohort studies — supports dexamethasone oral/IV mini-pulse therapy as an already-practiced off-label option for moderate-to-severe alopecia areata (Evidence Level L2). However, this evidence pack has a **Blocking** data gap on formal Norway/regulatory label safety data (warnings, contraindications), which prevents the candidate from formally entering the S1 safety review stage.

**To proceed, the following is needed:**
- Retrieve TFDA/Norway-equivalent product label warnings and contraindications (Blocking gap, DG001)
- Retrieve formal mechanism of action (MOA) documentation from DrugBank or equivalent source (High priority gap, DG002)
- Formal DDI review, given dexamethasone's well-known interaction profile (CYP3A4 inducers/substrates, live vaccines, NSAIDs)
- Dosing/regimen standardization review — literature uses varied mini-pulse protocols (e.g., 5 mg twice weekly vs. monthly IV pulses); no consensus regimen has been established
- Confirm route/formulation compatibility (oral tablet vs. IV pulse) against locally available dosage forms, since no Norway licenses currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

