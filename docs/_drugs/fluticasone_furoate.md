---
layout: default
title: Fluticasone Furoate
parent: 僅模型預測 (L5)
nav_order: 153
evidence_level: L5
indication_count: 8
---

# Fluticasone Furoate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Fluticasone Furoate: From Corticosteroid Therapy to Atopic Eczema

## One-Sentence Summary

> Fluticasone Furoate is a potent inhaled/intranasal corticosteroid; the evidence pack does not contain a structured original-indication record for this product (unmarketed in Norway), but it is broadly known as an ICS used for asthma and allergic rhinitis.
> The TxGNN model predicts it may be effective for **Atopic Eczema**,
> with **10 clinical trials** and **2 publications** currently supporting this direction — though most trials use the Propionate ester rather than Furoate itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no Norway license records); generically known as an ICS for asthma/allergic rhinitis |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data (`original_moa`) is not available in the evidence pack. Based on the repurposing rationale, Fluticasone Furoate is described as a high-potency glucocorticoid receptor agonist that suppresses pro-inflammatory cytokines (IL-4, IL-13, TNF-α) and keratinocyte inflammatory responses — the standard mechanism by which topical corticosteroids control atopic dermatitis.

The predicted link to atopic eczema is mechanistically plausible: corticosteroid receptor activation to suppress Th2-driven inflammation is a well-established therapeutic principle across allergic/inflammatory skin conditions. However, nearly all supporting clinical trials in this evidence pack use **Fluticasone Propionate**, not Fluticasone Furoate. The two are different ester forms with different systemic bioavailability (Furoate has lower systemic exposure), so mechanistic extrapolation is reasonable but not a direct molecular equivalence — this is an important caveat rather than confirmed cross-ester efficacy.

Note: a related predicted indication in the same evidence pack, **bronchitis/COPD** (rank 2), has direct Furoate-specific RCT evidence (PMID 21977941) and is already a labeled use in combination products (e.g., fluticasone furoate/vilanterol) — that pathway represents label-extension rather than a novel repurposing hypothesis, and carries stronger (L2) evidence than the atopic eczema signal discussed here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00690105](https://clinicaltrials.gov/study/NCT00690105) | Phase 4 | Completed | 577 | Tacrolimus 0.1% vs Fluticasone (Propionate) 0.005% ointment in adults with facial "red face" atopic dermatitis |
| [NCT00689832](https://clinicaltrials.gov/study/NCT00689832) | Phase 4 | Completed | 487 | Tacrolimus 0.03% vs Fluticasone 0.005% ointment in children ≥2y with moderate-severe AD |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | Proactive skin-barrier care + fluticasone propionate cream vs reactive therapy to prevent AD/food allergy progression in infants |
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Intermittent (2x/week) fluticasone propionate 0.05% cream + moisturizer to reduce AD relapse risk in stabilized pediatric patients |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | EpiCeram (non-steroidal) vs mid-strength fluticasone propionate 0.05% in pediatric moderate-severe AD |
| [NCT04706559](https://clinicaltrials.gov/study/NCT04706559) | NA | Completed | 98 | Oral probiotic supplementation efficacy in children with AD (SCORAD index) — adjunctive, not steroid-focused |
| [NCT00119158](https://clinicaltrials.gov/study/NCT00119158) | Phase 4 | Completed | 90 | Concomitant Elidel (pimecrolimus) 1% + Cutivate (fluticasone propionate) 0.05% in severe AD lesions |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label HPA-axis safety evaluation of Cutivate (fluticasone propionate) lotion 0.05% in pediatric AD |
| [NCT01772056](https://clinicaltrials.gov/study/NCT01772056) | Phase 3 | Terminated | 54 | Twice-weekly fluticasone propionate 0.05% maintenance to reduce AD relapse in children — trial terminated early |
| [NCT07537751](https://clinicaltrials.gov/study/NCT07537751) | NA | Completed | 40 | Topical crisaborole 2% vs fluticasone propionate 0.05% in mild-moderate pediatric AD (SCORAD/ISGA outcomes) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews intranasal corticosteroid use across allergic rhinitis, asthma and atopic dermatitis, with focus on HPA-axis suppression risk |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case Report | Indian J Otolaryngol Head Neck Surg | Case study on allergen immunotherapy in autoimmune patients; notes AIT application extends to atopic dermatitis |

---

## Norway Market Information

Currently no Norway market authorizations found for this product (`market_status`: Not Marketed, 0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Fluticasone Furoate specifically in atopic eczema is Level L3 (observational/uncontrolled and cross-ester extrapolation) — nearly all supporting trials use the Propionate ester, and the only Phase 3 RCT (NCT01772056) was terminated early with a small sample (n=54). The mechanism is plausible but not yet confirmed for the Furoate ester in this indication.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings and contraindications (currently a Blocking data gap — required before any S1 safety evaluation)
- Confirmed mechanism of action (MOA) data specific to Fluticasone Furoate (High-severity data gap)
- Direct Furoate-specific trial or pharmacokinetic bridging data for atopic dermatitis (most existing evidence is for Propionate)
- Consider prioritizing the bronchitis/COPD signal (rank 2) instead, which has direct Furoate RCT evidence (PMID 21977941) and L2 evidence supporting "Proceed with Guardrails"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

