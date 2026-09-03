---
layout: default
title: Ivosidenib
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 3
---

# Ivosidenib
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

# Ivosidenib: From IDH1-Mutated Acute Myeloid Leukemia to Bulbar Polio

## One-Sentence Summary

Ivosidenib is an IDH1 mutant enzyme inhibitor, inferred from available data to be approved for IDH1-mutated acute myeloid leukemia (AML) — formal original-indication documentation is currently a data gap.
The TxGNN model's top-ranked prediction for this drug is **Bulbar Polio**, but **0 clinical trials** and **0 publications** currently support this specific link, and the model's own rationale notes no known mechanistic connection.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | IDH1-mutated AML (inferred from repurposing rationale text; not confirmed by formal license/label data — see Data Gap DG001/DG002) |
| Predicted New Indication | Bulbar Polio |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on the repurposing rationale accompanying this evidence pack, ivosidenib is understood to inhibit the mutant IDH1 enzyme, blocking accumulation of the oncometabolite 2-hydroxyglutarate (2-HG) in IDH1-mutated cancers such as AML.

Bulbar polio is a poliovirus-induced motor neuron disease. There is no known biological relationship between IDH1/2-HG metabolism and poliovirus-mediated neuronal injury. The model's own generated rationale explicitly states that this high score likely reflects a **sparse or noisy edge in the underlying knowledge graph**, rather than a genuine mechanistic relationship, and that no mechanistic hypothesis currently supports this pairing.

No clinical trials, literature, or biological plausibility currently exist to support ivosidenib as a candidate treatment for bulbar polio. This prediction should be treated as a model artifact requiring no immediate action, rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Norway Market Information

Ivosidenib is not currently marketed in Norway. No authorization records are available in this evidence pack (0 licenses on file).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mutant IDH1 enzyme inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no clinical trial evidence, no published literature, and no plausible mechanistic rationale linking ivosidenib to bulbar polio. This pairing most likely reflects noise in the knowledge graph rather than a true repurposing opportunity.

**To proceed, the following is needed:**
- Formal MOA and original-indication documentation (resolve DG001, DG002) before any further scoring
- TFDA/EMA package insert warnings and contraindications for baseline safety review
- If this candidate is revisited, an independent mechanistic hypothesis beyond the current graph signal is required before advancing past S0

---

### Additional Predicted Indications in This Evidence Pack

This evidence pack contains two other candidate indications for ivosidenib that are mechanistically more plausible and warrant separate tracking rather than dismissal:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Rationale Summary |
|------|---------|-------------|-----------------|-----------------|--------------------|
| 2 | AML/MDS related to alkylating agents | 99.26% | L4 | Research Question | Ivosidenib is used in IDH1-mutated AML broadly (including some therapy-related subtypes per AGILE trial); extrapolation to alkylating-agent-related AML/MDS is mechanistically reasonable if IDH1 mutation is present, but subtype-specific mutation prevalence and added toxicity from prior chemotherapy exposure are unconfirmed. |
| 3 | AML/MDS related to radiation | 99.26% | L4 | Research Question | Same extrapolation logic as above for radiation-induced therapy-related myeloid neoplasms; no subtype-specific trial or literature evidence currently exists in this pack. |

These two candidates should be prioritized over the Bulbar Polio prediction for any future research question follow-up, as they build on an established (though not formally documented in this pack) approved use of ivosidenib in IDH1-mutated AML.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

