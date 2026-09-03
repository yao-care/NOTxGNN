---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 242
evidence_level: L5
indication_count: 3
---

# Nevirapine
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

# Nevirapine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Nevirapine is a first-generation non-nucleoside reverse transcriptase inhibitor (NNRTI) established for the treatment of human HIV-1 infection as part of combination antiretroviral therapy. The TxGNN model predicts potential activity against **feline acquired immunodeficiency syndrome (FIV infection)**, a veterinary retroviral disease, but this direction is currently supported by only **1 in vitro/structural comparison study** and **no clinical trials**, with the sole available literature suggesting nevirapine may actually **lack** cross-activity against feline reverse transcriptase.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (well-established use as part of combination antiretroviral therapy; no Norway license records available to extract formal indication text — see Data Gap DG001) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV infection) |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DrugBank query returned a data gap for structured MOA). Based on known information, nevirapine belongs to the NNRTI (non-nucleoside reverse transcriptase inhibitor) class, and its efficacy against HIV-1 infection — as part of combination antiretroviral regimens — is well established in humans. Mechanistically, NNRTIs act by binding to an allosteric hydrophobic pocket on the HIV-1 reverse transcriptase (RT) enzyme, which is structurally distinct across different retroviruses.

The predicted new indication, feline immunodeficiency virus (FIV) infection, is caused by a different lentivirus that also relies on a reverse transcriptase enzyme, which is the superficial basis for TxGNN's similarity-based prediction (both are RT-dependent retroviral infections). However, the single available literature source (PMID 38031646) directly cautions against this extrapolation: it reports that feline RT differs structurally from HIV-1 RT and appears to **lack the hydrophobic binding pocket** required for NNRTI binding. In other words, the only evidence identified for this pairing points toward an absence of cross-species activity rather than a therapeutic signal.

Additionally, FIV infection is a veterinary (feline) disease rather than a human indication, so even if in vitro activity were confirmed, the translational pathway to a human drug-repurposing candidate would remain undefined. For these reasons, the mechanistic plausibility of this specific prediction is weak despite the high TxGNN similarity score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro / structural comparison | Journal of Veterinary Science | Biochemical and structural comparison of NNRTIs (nevirapine, efavirenz, rilpivirine) against feline vs. human immunodeficiency virus reverse transcriptase; findings indicate FIV RT lacks the hydrophobic pocket needed for NNRTI binding, suggesting limited cross-species antiviral activity rather than efficacy |

---

## Norway Market Information

No Norway market authorization records are available for nevirapine (market status: **Not Marketed**, 0 authorizations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/package-insert warnings and contraindications data, and drug-drug interaction data, are flagged as data gaps in this evidence pack — see "To proceed" below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only literature identified for this specific prediction (feline AIDS) argues against, rather than for, meaningful cross-reactivity of nevirapine against FIV reverse transcriptase, there are no clinical trials, and the indication itself is non-human (veterinary), leaving no clear translational path. Combined with a Blocking-severity data gap on package-insert warnings/contraindications, this candidate does not currently meet the threshold to advance past initial screening (S0).

**To proceed, the following is needed:**
- TFDA/manufacturer package-insert warnings and contraindications (Data Gap DG001, Blocking — required before any S1 safety evaluation)
- DrugBank mechanism-of-action detail (Data Gap DG002, High)
- If pursuing an FIV-related research direction: in vitro/in vivo confirmation of nevirapine activity against feline RT, since the current single source suggests the opposite
- Clarification of whether a human-relevant repurposing hypothesis (vs. veterinary) is intended before further investment

---

## Other Model-Predicted Indications in This Evidence Pack (Not Analyzed in Detail)

This evidence pack contains two additional TxGNN predictions for nevirapine that were not the primary focus of this report but are worth noting given the "multi-indication" nature of this candidate:

| Rank | Disease | TxGNN Score | Evidence Level | Decision Stage | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------------------|------|
| 2 | Simian immunodeficiency virus (SIV) infection | 99.85% | L3 | S1 | Research Question | 17 literature hits, but wild-type SIV RT is intrinsically NNRTI-resistant; most studies use HIV-1 RT/SIV chimeras (SHIV) as an animal model for HIV research rather than evidence of direct SIV efficacy. Non-human indication. |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.82% | L5 | S0 | Hold | No clinical trials, no literature, and no plausible mechanistic link to nevirapine's known pharmacology (rare genetic neurodevelopmental disorder vs. an antiretroviral RT inhibitor). |

None of the three predicted indications in this evidence pack currently support a "Go" or "Proceed with Guardrails" decision; all require substantially more mechanistic or preclinical evidence before further evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

