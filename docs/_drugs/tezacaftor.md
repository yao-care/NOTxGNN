---
layout: default
title: Tezacaftor
parent: 僅模型預測 (L5)
nav_order: 353
evidence_level: L5
indication_count: 3
---

# Tezacaftor
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

# Tezacaftor: From Cystic Fibrosis to HIV Infectious Disease

## One-Sentence Summary

> Tezacaftor is a CFTR corrector originally developed for the treatment of cystic fibrosis, correcting misfolded CFTR protein and promoting its trafficking to the cell membrane.
> The TxGNN model predicts it may be effective for **HIV Infectious Disease**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, making it a model-inference-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cystic Fibrosis |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for tezacaftor is not available (flagged as a High-severity data gap). Based on the information available, tezacaftor is a CFTR corrector used in combination regimens for cystic fibrosis, where it corrects CFTR protein misfolding and restores its trafficking to the cell membrane.

There is no known mechanistic overlap between CFTR protein folding/trafficking pathways and HIV viral replication or host immune response pathways. The repurposing rationale explicitly notes that this high TxGNN score most likely reflects knowledge-graph embedding similarity rather than a validated biological mechanism.

The two other top-ranked predictions (leprosy, multiple endocrine neoplasia) show the same pattern: no mechanistic connection to CFTR biology and no supporting clinical or literature evidence. Given the absence of a plausible biological rationale and the complete lack of trial/literature support across all three candidates, this prediction set should be treated as exploratory only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or literature evidence exist for HIV infectious disease (or the other two ranked predictions), and the repurposing rationale itself identifies no plausible mechanistic link to CFTR biology. The high TxGNN score alone (L5, model-prediction-only) is insufficient to advance this candidate.

**To proceed, the following is needed:**
- TFDA/regulatory package insert warnings and contraindications (currently Blocking data gap, DG001)
- Confirmed original mechanism of action data via DrugBank (currently High-severity data gap, DG002)
- Independent literature or preclinical evidence establishing a biological link between CFTR modulation and HIV pathophysiology
- Confirmation of Taiwan/Norway market and licensing status, currently listed as unmarketed with zero authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

