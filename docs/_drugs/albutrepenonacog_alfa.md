---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog Alfa: From Hemophilia B (Background Knowledge, Unconfirmed) to Pseudo-von Willebrand Disease

## One-Sentence Summary

Albutrepenonacog alfa is a recombinant coagulation factor product; its original approved indication is not documented in the current source data, though background pharmacological knowledge (also referenced in the model's own rationale) suggests it functions as a **recombinant Factor IX replacement therapy** for Factor IX deficiency (Hemophilia B). The TxGNN model predicts it may be relevant to **Pseudo-von Willebrand Disease**, but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale describes the two conditions as acting at different physiological levels with **no established mechanistic link**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in source data (Data Gap); background knowledge suggests Factor IX replacement therapy for Hemophilia B — unconfirmed |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.94% (raw rank #878 among all candidate diseases) |
| Evidence Level | L5 (model prediction only, no clinical or literature evidence) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity Data Gap in this evidence pack). Based on the limited background information carried in this pack, albutrepenonacog alfa is presumed to be a recombinant Factor IX replacement product, acting on the **secondary hemostasis (coagulation factor) pathway**. This presumption is not confirmed by a formal MOA record and should be treated as unverified until DrugBank/regulatory source data can be reconciled.

The predicted new indication, Pseudo-von Willebrand Disease, is a **primary hemostasis disorder** caused by a gain-of-function abnormality in the platelet GpIb receptor, leading to excessive affinity for von Willebrand factor. This is mechanistically distinct from a coagulation-factor deficiency: one is a platelet-receptor/binding disorder, the other is a clotting-factor deficiency. The evidence pack's own repurposing rationale is explicit on this point, stating that the two conditions "act at different levels" and that there is "no known mechanistic link" between them.

Given this, the prediction should be read as a **statistical association surfaced by the TxGNN knowledge graph model**, not as a mechanistically or clinically validated hypothesis. The high raw prediction score (99.94%) reflects the model's internal ranking confidence, not external validation — no clinical trials, literature, or regulatory precedent currently exist to corroborate it.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Albutrepenonacog alfa currently holds no marketing authorization in Norway (market status: **not marketed**, 0 licenses on record). No product/dosage-form information is available for this evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags the absence of TFDA package-insert warnings/contraindications as a **Blocking** data gap — see Conclusion below. No drug-drug interaction records were found in the queried source.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There is no clinical trial or literature evidence supporting use of albutrepenonacog alfa in Pseudo-von Willebrand Disease (or in any of the other five lower-ranked predicted indications in this pack — primary platelet release disorder, Glanzmann thrombasthenia, Scott syndrome, collagen-receptor bleeding diathesis, and constitutional thrombocytopenia), and the model's own mechanistic rationale for each candidate describes the underlying pathophysiology as distinct from coagulation-factor replacement.
- A **Blocking**-severity data gap exists for TFDA/package-insert safety information (warnings, contraindications), which by this program's own criteria prevents entry into the S1 safety pre-assessment stage. A **High**-severity gap also exists for confirmed mechanism of action.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official package insert to establish key warnings and contraindications before any safety pre-assessment can begin.
- Resolve DG002 (High): confirm mechanism of action via DrugBank or another authoritative source, since the current MOA is presumed rather than verified.
- Confirm the drug's original approved indication(s), which are currently absent from the source regulatory data.
- If this candidate is to be advanced despite the weak mechanistic rationale, obtain independent preclinical or case-level evidence linking Factor IX pathway modulation to platelet-mediated bleeding disorders such as Pseudo-von Willebrand Disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

