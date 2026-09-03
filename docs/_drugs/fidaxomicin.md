---
layout: default
title: Fidaxomicin
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 9
---

# Fidaxomicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Fidaxomicin: From Unspecified Original Indication to Staphylococcal Scalded Skin Syndrome

## One-Sentence Summary

> The evidence pack for Fidaxomicin (DrugBank ID: DB08874) does not contain data on its original approved indication or mechanism of action, and the drug currently holds no marketing authorization in Norway.
> The TxGNN model's top prediction is **Staphylococcal Scalded Skin Syndrome (SSSS)**, but this is supported by **0 clinical trials** and **0 publications**,
> and the rationale accompanying the prediction itself flags the mechanistic link as weak, most likely a model artifact rather than a genuine repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/indication data in evidence pack |
| Predicted New Indication | Staphylococcal Scalded Skin Syndrome |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Fidaxomicin in this evidence pack, and no original indication is on record either. What can be reconstructed from general pharmacology (as noted in the model's own rationale) is that fidaxomicin is a narrow-spectrum macrolide with in vitro activity against some Gram-positive organisms, including *S. aureus*. However, it is administered orally and has negligible systemic bioavailability (<0.5%), acting almost exclusively within the gut lumen.

Staphylococcal Scalded Skin Syndrome is a toxin-mediated, systemic skin disease that requires an antibiotic capable of reaching therapeutic concentrations systemically to clear the toxin-producing staphylococcal focus. Given fidaxomicin's pharmacokinetic profile, it cannot achieve meaningful systemic exposure, so the mechanistic basis for this prediction is weak.

The model's own repurposing rationale explicitly characterizes this as a likely case of TxGNN embedding overgeneralization — the model appears to be picking up on "anti-staphylococcal activity" as a shared feature without accounting for the route-of-administration and pharmacokinetic mismatch. This same caveat (no systemic exposure, no topical/parenteral formulation) recurs across nearly all of the top 9 predicted indications for this drug (bullous impetigo, impetigo, hordeolum, S. aureus pneumonia), and two predictions (inhalational and toxin-mediated botulism) are mechanistically unrelated altogether (neurotoxin-mediated disease vs. an antibacterial agent), and one (vulvovaginal candidiasis) involves a fungal pathogen against which fidaxomicin, an antibacterial RNA polymerase inhibitor, has no known activity.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Fidaxomicin currently holds **no marketing authorization in Norway** (market status: Not Marketed, 0 licenses on record). No product, dosage form, or approved-indication data is available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are marked as a blocking data gap (DG001) in this evidence pack — TFDA/regulatory label data has not yet been retrieved and parsed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (SSSS) carries a high TxGNN similarity score but is entirely unsupported by clinical trials or literature (Evidence Level L5), and the model's own mechanistic rationale flags fidaxomicin's negligible systemic absorption as a fundamental barrier to efficacy in a systemic, toxin-mediated skin disease. This pattern repeats across essentially all top-ranked predictions for this drug — several are mechanistically implausible (fungal or neurotoxin-mediated diseases against a narrow-spectrum antibacterial), and none have an available route of administration (topical/ophthalmic/parenteral) matching the proposed indication. Combined with a blocking safety data gap (DG001), there is no basis to advance any of these candidates past initial screening.

**To proceed, the following is needed:**
- Resolve DG001: retrieve and parse TFDA (or equivalent) label warnings/contraindications before any S1 safety screening can occur
- Obtain confirmed mechanism of action (DG002) and original approved indication for fidaxomicin to properly anchor similarity-to-original analysis
- If SSSS or impetigo-type indications are to be pursued further, first establish whether a topical/dermatologic formulation of fidaxomicin is technically feasible, since the oral formulation's PK profile does not support these use cases
- Independent literature/mechanism review to distinguish genuine repurposing signal from TxGNN embedding overgeneralization before committing further evaluation resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

