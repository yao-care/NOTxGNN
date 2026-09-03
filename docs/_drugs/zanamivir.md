---
layout: default
title: Zanamivir
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 2
---

# Zanamivir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Zanamivir: From Influenza to Pyelonephritis

## One-Sentence Summary

> Zanamivir is a neuraminidase inhibitor antiviral, originally developed for the treatment and prophylaxis of influenza.
> The TxGNN model predicts it may be effective for **Pyelonephritis**, but **0 clinical trials** and **0 publications**
> currently support this direction — the prediction currently rests on model association alone, with no biological rationale identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (based on known antiviral mechanism; not confirmed by Norwegian license text — drug is unmarketed, no license data available) |
| Predicted New Indication | Pyelonephritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for zanamivir is not available in this evidence pack (`original_moa: [Data Gap]`). Based on the drug's known pharmacological class, zanamivir is a neuraminidase inhibitor that blocks the influenza viral neuraminidase enzyme, preventing release of new viral particles from infected cells — a mechanism specific to influenza A/B virus replication.

Pyelonephritis is predominantly a bacterial infection of the renal parenchyma (most commonly caused by *E. coli* and other Enterobacteriaceae). There is no known antibacterial activity, renal-targeting pharmacokinetic property, or immunomodulatory mechanism of zanamivir that would plausibly explain efficacy in this condition. The evidence pack's own repurposing rationale explicitly states that this high TxGNN score reflects a graph-neural-network association only, **without supporting biological plausibility, mechanistic literature, or clinical evidence**.

A second candidate indication in this evidence pack — "disorder of tyrosine metabolism" (a genetic metabolic disease) — shows the same pattern: the three literature citations retrieved actually concern oseltamivir resistance mutations and neuraminidase inhibition assays (where "tyrosine" appears as a residue name at the H275Y mutation site), not tyrosine metabolic disease. This is a strong indicator of a keyword-matching artifact rather than a genuine biological signal, and reinforces that neither prediction in this pack should be advanced without independent mechanistic or clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: literature was retrieved for the second, lower-priority candidate indication — "disorder of tyrosine metabolism" — but on review it concerns oseltamivir/neuraminidase resistance research and is not topically relevant to tyrosine metabolism disorders. It is not presented here as supporting evidence.)*

---

## Norway Market Information

Zanamivir is currently not marketed in Norway; no license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available for this compound.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (pyelonephritis) carries an L5 evidence level — model prediction only, with zero clinical trials, zero supportive literature, and no identifiable mechanistic pathway linking a viral neuraminidase inhibitor to a predominantly bacterial renal infection. A second candidate indication in the same pack shows evidence of a literature-retrieval mismatch, further underscoring the need for caution before any further evaluation.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- TFDA/regulatory label warnings and contraindications (currently blocking S1 safety screening per DG001)
- Independent mechanistic or preclinical evidence linking neuraminidase inhibition to any renal/urinary tract pathology
- Re-validation of the literature retrieval pipeline to rule out keyword-mismatch artifacts (as seen with the tyrosine metabolism candidate)
- If no such evidence emerges, this candidate should be deprioritized rather than advanced to further scoring stages
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

