---
layout: default
title: Elvitegravir
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 3
---

# Elvitegravir
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

Using no additional skill — this is a direct, fully-specified report-generation task; I'll follow the provided template exactly against the given Evidence Pack.

# Elvitegravir: From HIV-1 Infection to Feline Immunodeficiency Virus (FIV) Infection

## One-Sentence Summary

Elvitegravir is known in the evidence pack's own mechanistic notes as an HIV-1 integrase strand transfer inhibitor (INSTI); however, no formal original-indication or MOA record is present in the source data (both are flagged as data gaps).
The TxGNN model's top prediction is **Feline Acquired Immunodeficiency Syndrome (FIV)** — a veterinary, non-human disease — with a score of **99.89%**, but this ranking is supported by **0 clinical trials** and **0 publications**.
A second-ranked candidate, Simian Immunodeficiency Virus (SIV) infection, does have supporting literature (7 papers), but these are HIV-drug-resistance research-tool studies in macaque models, not a human clinical indication. Overall, the evidence supporting this candidate as a genuine human drug-repurposing opportunity is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (`original_indications` empty; mechanistic notes describe elvitegravir as an HIV-1 integrase inhibitor) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome (FIV) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on the mechanistic notes embedded in the evidence pack, elvitegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), a class that blocks retroviral DNA integration into the host genome.

The top-ranked predicted indication — feline immunodeficiency virus (FIV) infection — is biologically linked to elvitegravir's mechanism only through a broad taxonomic argument: FIV and HIV are both lentiviruses, and integrase-targeted inhibition is theoretically cross-species applicable. However, this rationale is explicitly noted in the evidence pack as **theoretical only**, with no in vitro or in vivo FIV-specific data, and FIV is a veterinary (feline) disease rather than a typical human drug-repurposing target.

A secondary candidate, SIV infection (rank 2), has stronger mechanistic support — multiple in vitro and non-human-primate studies confirm elvitegravir's antiviral activity and resistance profile against SIV/SHIV, given the high homology between SIV and HIV integrase sequences. Critically, however, these studies use SIV/SHIV macaque models purely as **research tools to study HIV drug resistance**, not as a treatment target for a monkey disease. Neither predicted indication, therefore, represents a credible human repurposing candidate under standard drug-repurposing criteria.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

*(Note: the top-ranked predicted indication, FIV, has no supporting literature. The rank-2 candidate, SIV infection, has 7 supporting publications — primarily in vitro resistance/mechanism studies in SIV/SHIV models — but these serve as HIV integrase-inhibitor research tools rather than evidence for a distinct human indication, and are therefore not tabulated here per the rank-1 reporting convention.)*

## Norway Market Information

This drug currently has no marketing authorization in Norway (未上市 / Not Marketed); `total_licenses` = 0 and no license records are available in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: data gap DG001 — TFDA/local package insert warnings and contraindications — is flagged as a **Blocking** severity gap, meaning this candidate cannot yet pass initial safety screening (S1).)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (FIV) is a veterinary disease with no clinical trial or literature support (Evidence Level L5, decision stage S0), and is not a credible human repurposing target. The next-best candidate (SIV infection) is backed only by HIV-resistance research-tool studies in animal models, not a genuine disease indication. Combined with a Blocking safety data gap (DG001) and missing MOA documentation (DG002), this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA/regulatory package insert (warnings, contraindications) — required to clear the Blocking data gap (DG001) before any S1 safety review
- Confirmed MOA documentation via DrugBank API (DG002)
- Re-screening of TxGNN outputs to identify whether any higher-quality, human-relevant predicted indications exist beyond the current top 3 (rank 3, a rare neurodevelopmental disorder, is assessed as likely graph noise with no biological plausibility)
- If any interest remains in the SIV-related research angle, clarification of intended human population and clinical translatability, since current evidence is confined to non-human-primate drug-resistance modeling
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

