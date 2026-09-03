---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 3
---

# Cobicistat
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

# Cobicistat: From Antiretroviral Pharmacokinetic Enhancer to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Cobicistat is a CYP3A4 inhibitor used clinically as a pharmacokinetic booster in combination antiretroviral therapy (e.g., with elvitegravir, atazanavir, darunavir) rather than as a direct antiviral agent in its own right. The TxGNN model predicts a possible link to **Simian Immunodeficiency Virus Infection**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharmacokinetic enhancer (booster) for antiretroviral therapy — not an independent disease indication |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A structured, DrugBank-sourced mechanism-of-action record is currently unavailable for cobicistat (flagged as a High-severity data gap, DG002). Based on the pharmacological information embedded in the model's own rationale, cobicistat is known to act as a CYP3A4 inhibitor — it has no direct antiviral activity of its own, and its clinical role is limited to raising plasma concentrations of co-administered antiretrovirals. It does not target any viral replication machinery.

Simian Immunodeficiency Virus (SIV) is the primate analog of HIV and is commonly used as an animal model for HIV research. The TxGNN model's high score for this association likely reflects proximity in the knowledge graph between cobicistat, HIV-related drug classes, and SIV as an HIV-model disease entity — rather than any evidence that cobicistat itself has anti-SIV activity. At best, cobicistat could theoretically serve as a booster for other antiviral compounds in an SIV treatment regimen, analogous to its human ARV use; it would not function as a standalone therapeutic.

Two additional candidates were predicted with near-identical scores: **feline acquired immunodeficiency syndrome (FIV)**, which follows the same booster-only logic with added concern about species-specific CYP450 differences between cats and humans, and a **rare neurodevelopmental disorder** (ataxic gait, absent speech, decreased cortical white matter) for which no plausible mechanistic link to CYP3A4 inhibition exists at all. This third candidate is assessed as a likely false positive and is not recommended for further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are marked as a Blocking data gap (DG001) — required before this candidate can advance to a formal safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three TxGNN-predicted indications for cobicistat lack any clinical trial or literature support, and the underlying mechanism (a pharmacokinetic booster with no intrinsic antiviral or neurological activity) does not plausibly justify standalone therapeutic use in any of the predicted conditions. Cobicistat is also not currently marketed in Norway, and core regulatory/safety data are missing.

**To proceed, the following is needed:**
- TFDA-equivalent label data — warnings, contraindications (DG001, blocking)
- Confirmed mechanism of action via DrugBank API (DG002)
- Preclinical or in vitro evidence establishing any direct or booster-mediated relevance to SIV infection specifically
- Complete drug-drug interaction (DDI) profile before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

