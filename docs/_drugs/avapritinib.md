---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Avapritinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Avapritinib: From Unclear Original Indication to Axial Spondylometaphyseal Dysplasia

## One-Sentence Summary

> Avapritinib's original approved indication and full mechanism-of-action data are currently unavailable in this evidence pack, though it is referenced elsewhere as a selective KIT/PDGFRA inhibitor.
> The TxGNN model predicts it may be effective for **Axial Spondylometaphyseal Dysplasia**, a rare skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — no approved indication text on file) |
| Predicted New Indication | Axial spondylometaphyseal dysplasia |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack. Based on the mechanistic notes accompanying the model output, avapritinib is described as a **selective KIT/PDGFRA tyrosine kinase inhibitor**. PDGFRA signaling plays a role in cartilage and bone development, which is the theoretical basis offered for a link to this ultra-rare skeletal dysplasia syndrome.

However, the model's own rationale text is explicit that this link is speculative: it states there is "no concrete evidence of pathogenic mechanism overlap with avapritinib's targets" for this disease, and that the prediction is "purely a high-scoring TxGNN output with no clinical or literature support." The same caveat applies across all ten ranked predictions in this pack — several cluster around ALS and motor neuron disease (rationale invokes an indirect PDGFRα role in oligodendrocyte precursor cells and blood-brain-barrier integrity), while others (rare skeletal/neurodevelopmental syndromes) have **no known mechanistic connection at all** to the KIT/PDGFRA pathway.

Because the original indication and MOA fields are both data gaps, and because none of the ten predicted indications have any corroborating clinical trial or literature evidence, this candidate should be treated as an early-stage hypothesis-generation output only, not a repurposing candidate ready for evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Avapritinib is not currently marketed in Norway (0 authorizations on file); no license records are available for this evidence pack.

---

## Cytotoxicity

Based on the mechanistic description available (selective KIT/PDGFRA tyrosine kinase inhibitor), avapritinib falls into the targeted anticancer therapy class rather than conventional cytotoxic chemotherapy. No structured toxicity data is included in this evidence pack.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (KIT/PDGFRA tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications carry evidence level L5 (model prediction only) with zero supporting clinical trials or literature. Combined with the drug's unmarketed status in Norway and a blocking data gap on TFDA label warnings/contraindications, there is no basis to advance any of these candidates beyond hypothesis stage.

**To proceed, the following is needed:**
- Confirmed original indication(s) and approved label text
- Detailed mechanism of action (MOA) data, ideally sourced from DrugBank
- TFDA-equivalent label warnings and contraindications (currently a Blocking gap, DG001)
- At minimum, preclinical or case-level evidence connecting avapritinib to any of the ranked predicted indications before S1 safety screening can begin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

