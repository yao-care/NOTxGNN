---
layout: default
title: Reslizumab
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 2
---

# Reslizumab
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

# Reslizumab: From Eosinophilic Asthma to Immune Thrombocytopenia

## One-Sentence Summary

> Reslizumab is an anti-IL-5 monoclonal antibody originally developed for eosinophilic asthma.
> The TxGNN model predicts it may be effective for **Immune Thrombocytopenia (thrombocytopenia due to immune destruction)**,
> but currently **no clinical trials and no directly relevant literature** support this prediction — the score reflects an indirect knowledge-graph association rather than established pharmacology.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Eosinophilic asthma (per drug mechanism description; not on file in Taiwan licenses — drug is not marketed) |
| Predicted New Indication | Thrombocytopenia due to immune destruction |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA: Data Gap). Based on known information, Reslizumab is an anti-IL-5 monoclonal antibody that inhibits eosinophil production and activation, and its efficacy in eosinophilic asthma is well established.

However, the repurposing rationale for immune thrombocytopenia explicitly notes that **no known mechanism links the IL-5 pathway to megakaryocyte function or immune-mediated platelet destruction**. The high TxGNN score appears to stem from an indirect knowledge-graph connection — likely through general immune-modulation or autoimmune-related nodes — rather than any documented molecular or clinical pathway. There is no direct pharmacological rationale connecting eosinophil suppression to platelet immune destruction at this time.

A secondary, lower-ranked prediction ("primary release disorder of platelets") is supported only by a single review article on mepolizumab (a different anti-IL-5 agent) in hypereosinophilic syndrome, which does not address reslizumab or platelet release mechanisms directly. This further indicates the current evidence base for platelet-related indications is speculative rather than substantive.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Reslizumab is currently **not marketed in Taiwan** (0 authorizations on file). No license or approved-indication records are available for reference.

## Safety Considerations

Please refer to the package insert for safety information. (TFDA warnings/contraindications and drug interaction data are not yet available — see data gap DG001.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5), with no clinical trials, no directly relevant literature, and no established mechanistic link between the IL-5 pathway and immune-mediated platelet destruction. There is insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- Reslizumab MOA detail from DrugBank (data gap DG002)
- TFDA package insert warnings/contraindications (data gap DG001, blocking for S1 safety review)
- Preclinical or mechanistic studies directly linking IL-5/eosinophil biology to platelet immune destruction
- Any case reports or observational data on reslizumab use in patients with concurrent thrombocytopenia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

