---
layout: default
title: Brolucizumab
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Brolucizumab: From Ophthalmic Neovascular Disease to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies

## One-Sentence Summary

> Brolucizumab is known clinically as an intravitreal anti-VEGF-A therapy for ocular neovascular disease, though this original indication is not documented in the current Norway regulatory dataset.
> The TxGNN model's top prediction suggests possible effectiveness for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
> but **0 clinical trials** and **0 publications** currently support this direction, and the drug is not marketed in Norway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Norway regulatory data. Known clinical use (per drug mechanism description) is intravitreal anti-VEGF therapy for ocular neovascular disease. |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on the information available in this evidence pack, brolucizumab is an anti-VEGF-A single-chain antibody fragment (scFv) administered by intravitreal injection, working by blocking VEGF signaling to reduce pathological angiogenesis in ocular disease.

Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies is a metabolic/energy-production disease driven by electron transport chain defects — a pathophysiology with no known overlap with VEGF-mediated angiogenesis. The evidence pack's own rationale states explicitly that no biological pathway connects the two conditions, and that this high TxGNN score reflects a graph-neural-network relational inference rather than a mechanistically grounded signal.

Given the absence of any supporting clinical trial or literature evidence, and the explicit mechanistic disconnect noted in the rationale, this prediction should be treated as exploratory only. It is worth noting that the remaining ranked predictions for this drug (esophageal varices with/without bleeding, exocrine pancreatic insufficiency) show the same pattern — high TxGNN scores with no mechanistic or clinical support, and in the case of esophageal variceal bleeding, a rationale that flags a *plausible safety concern in the opposite direction* (anti-VEGF agents are associated with impaired vascular/wound healing and bleeding risk, which could theoretically worsen rather than help a bleeding-prone condition).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Brolucizumab currently holds no marketing authorization in Norway (未上市, 0 licenses on record). No product/dosage form/indication data is available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Warning/contraindication/DDI data could not be retrieved from the current data sources. This is flagged in the source evidence pack as a blocking data gap (DG001) for safety pre-assessment.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported only by a model score (L5, no clinical trials or literature), and the mechanistic rationale in the evidence pack itself concludes there is no known biological pathway linking brolucizumab's anti-VEGF activity to mitochondrial oxidative phosphorylation disorders. Combined with the drug's unmarketed status in Norway and a blocking gap in safety labeling data, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action via DrugBank API query (DG002)
- Any preclinical or mechanistic literature directly linking VEGF inhibition to nuclear-DNA-related mitochondrial disorders
- Re-evaluation of lower-ranked predictions (esophageal varices, exocrine pancreatic insufficiency) only if independent clinical/mechanistic evidence emerges, given the bleeding-risk concern already noted for the variceal-bleeding candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

