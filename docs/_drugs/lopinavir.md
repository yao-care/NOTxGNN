---
layout: default
title: Lopinavir
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 3
---

# Lopinavir
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

# Lopinavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lopinavir is an HIV-1 protease inhibitor, typically administered in combination with ritonavir for antiretroviral therapy. The TxGNN model predicts a possible signal for **Simian Immunodeficiency Virus (SIV) Infection**, but this is currently supported only by **0 clinical trials** and **3 animal-model publications**, none of which involve human subjects or the predicted indication in a clinical sense.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 Infection (established antiretroviral indication; not itemized in this evidence pack) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Lopinavir is a peptidomimetic HIV-1 protease inhibitor, typically co-formulated with ritonavir to boost its plasma concentration via CYP3A4 inhibition, and its efficacy in HIV-1 infection is well established.

The repurposing rationale for SIV infection rests on structural homology between the HIV-1 protease and the SIV protease, which theoretically permits cross-inhibition by the same class of compound. However, this rationale is drawn from non-human primate (macaque) research-model studies rather than clinical evidence, and SIV infection is not a human disease — it is a veterinary/research model used to study lentiviral pathogenesis and antiretroviral efficacy in macaques.

Two lower-ranked predictions in this evidence pack — feline acquired immunodeficiency syndrome and a rare neurodevelopmental disorder — have no supporting literature or trials at all, and the latter is assessed as a likely knowledge-graph false positive with no plausible mechanistic link to protease inhibition. These should not be pursued.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal model (macaque) | Journal of Virology | Quadruple antiretroviral therapy (including a PI) produced rapid viral decay in SIVmac251-infected cynomolgus macaques |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Animal model (SHIV construction) | Microbes and Infection | Constructed a chimeric SHIV bearing the HIV-1 protease gene as a tool for testing protease inhibitor efficacy in vivo in rhesus macaques |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Animal model (macaque) | Journal of Virological Methods | Oral HAART including lopinavir/ritonavir assessed for impact on CD8+ subset in SHIV(89.6P)-infected rhesus macaques |

## Norway Market Information

Lopinavir currently holds no marketing authorization in Norway (0 licenses on record); the product is not marketed in this jurisdiction.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All evidence supporting the top-ranked prediction derives from non-human primate research models rather than clinical studies, and the drug has no current marketing authorization in Norway. Evidence level (L4) and the complete absence of clinical trial data preclude progression at this time.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action from DrugBank — currently a High-severity data gap (DG002)
- Any human clinical evidence for SIV/lentiviral cross-species protease inhibition relevance (if such a translational pathway exists)
- Re-evaluation of rank 2–3 predictions is not recommended; both lack any supporting evidence and rank 3 is likely a model artifact
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

