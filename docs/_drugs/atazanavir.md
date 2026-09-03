---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 6
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

Using the drug-repurposing report template to synthesize this Evidence Pack.

# Atazanavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Atazanavir is an HIV-1 protease inhibitor used as part of antiretroviral therapy for HIV-1 infection (inferred from trial context in this evidence pack; no formal indication record exists because the drug is not marketed in Norway).
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**, a lentivirus infection of macaques,
> supported by only **1 preclinical publication** and **0 clinical trials** — evidence that is preclinical/mechanistic only, not clinically actionable.

> ⚠️ **Important caveat:** Ranks 2–4 in this prediction set (feline AIDS, a rare neurodevelopmental disorder, and an obsolete hyperlipidemia term) have no meaningful mechanistic or evidentiary support and should not be pursued. Rank 5 ("AIDS related complex") does have strong evidence (2 completed Phase 3 RCTs, L1), but this reflects the drug's **already-established core HIV/AIDS indication**, not a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy) — inferred from clinical trial context; not formally on file as no Taiwan/Norway license exists |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed DrugBank MOA data was not available in this evidence pack (flagged as a High-severity data gap, DG002). However, context embedded in the evidence itself (clinical trial titles and the rationale for rank 5) indicates atazanavir is an **HIV-1 protease inhibitor** that blocks cleavage of the Gag-Pol polyprotein, preventing viral maturation — the pharmacological basis for its established use in HIV-1 infection.

SIV and HIV both belong to the lentivirus genus and share structural homology in their protease enzymes. This gives a theoretical rationale for cross-species protease inhibition, which is the basis of TxGNN's high similarity score. However, SIV infection is exclusively a **non-human primate disease model** used in translational HIV research (e.g., macaque studies of CNS viral reservoirs). It is not a human clinical indication, so this prediction has research value only — it cannot be advanced as a human drug repurposing candidate regardless of mechanistic plausibility.

By contrast, rank 5 ("AIDS related complex") is directly supported by two completed Phase 3 RCTs (NCT00035932, n=571; NCT01099579, n=82) and reflects atazanavir's core, already-approved pharmacology rather than a new indication. This is useful context but does not constitute "repurposing" in the sense this report is meant to evaluate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Simian Immunodeficiency Virus Infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Preclinical (macaque model) | The Journal of Infectious Diseases | HAART-treated SIV-infected macaques showed reduced CNS viral replication and inflammation, but persistent viral DNA in the CNS despite plasma viral suppression — an animal translational model finding, not direct evidence for a human indication. |

---

## Norway Market Information

Atazanavir is **not currently marketed in Norway** (market status: 未上市 / Not marketed). There are no drug license records (`total_licenses = 0`), so no authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack — flagged as a Blocking-severity data gap, DG001, that prevents entry into the S1 safety pre-assessment stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (SIV infection) targets a non-human disease model and is supported only by a single preclinical publication with no clinical trials (L4, S0 decision stage) — insufficient for repurposing consideration. Ranks 2–4 lack any credible mechanistic or evidentiary basis. Rank 5, while strongly supported (L1), represents the drug's existing core indication rather than a new opportunity, so it does not change the overall recommendation for this repurposing candidate.

**To proceed, the following is needed:**
- TFDA-equivalent (or Norwegian) package insert warnings/contraindications (DG001 — Blocking; required before any S1 safety pre-assessment)
- Confirmed mechanism-of-action data from DrugBank (DG002 — High priority; needed to properly assess mechanistic plausibility)
- If pursuing translational research value, a defined path from the SIV macaque model to a genuine human indication (e.g., HIV-associated neurocognitive disorder), since SIV infection itself is not a human disease target
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

