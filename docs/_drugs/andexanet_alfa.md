---
layout: default
title: Andexanet Alfa
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 4
---

# Andexanet Alfa
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

Using the provided Evidence Pack directly (no external lookups needed) to produce the report below.

---

# Andexanet Alfa: From Factor Xa Inhibitor Reversal to Glanzmann Thrombasthenia

## One-Sentence Summary

> Andexanet alfa is a modified recombinant factor Xa decoy protein used to reverse anticoagulation caused by factor Xa inhibitors (apixaban/rivaroxaban) in life-threatening bleeding.
> The TxGNN model predicts it may be effective for **Glanzmann thrombasthenia**,
> but **no clinical trials and no supporting literature** currently back this direction — the score appears to be driven by embedding proximity ("bleeding disorder" semantic clustering) rather than biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Reversal of anticoagulant effect of factor Xa inhibitors (apixaban/rivaroxaban) in patients with life-threatening or uncontrolled bleeding *(inferred from mechanistic description; not yet locally licensed)* |
| Predicted New Indication | Glanzmann Thrombasthenia |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Market Status (Taiwan) | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) record is not available (flagged as a High-severity data gap, DG002). However, the repurposing rationale attached to each prediction consistently describes andexanet alfa as a **modified recombinant factor Xa decoy protein**: it binds and neutralizes direct factor Xa inhibitors (apixaban, rivaroxaban) and also inhibits tissue factor pathway inhibitor (TFPI), restoring thrombin generation to promote hemostasis.

Glanzmann thrombasthenia, by contrast, is caused by a defect in the **GPIIb/IIIa receptor**, which impairs platelet aggregation at the receptor level — a mechanism entirely upstream of and unrelated to the factor Xa/TFPI pathway that andexanet alfa acts on. The evidence pack's own mechanistic assessment explicitly states there is **no biological pathway** by which restoring thrombin generation would correct a platelet aggregation receptor defect, and concludes the high TxGNN score most likely reflects graph-embedding proximity between "bleeding disorders" as a semantic class, rather than a genuine pharmacological relationship.

This pattern repeats across the other top-ranked candidates in this pack (primary platelet release disorder, pseudo-von Willebrand disease, and hemophilia) — each involves platelet-level or clotting-factor-deficiency mechanisms distinct from the factor Xa/TFPI axis that andexanet alfa targets, and none have supporting mechanistic rationale for a therapeutic (rather than incidental/interfering) role.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*(Note: for the 4th-ranked candidate, hemophilia, 11 publications exist — but on review these predominantly concern (a) andexanet's known interference with factor VIII/IX laboratory assays, and (b) general reviews of DOAC reversal strategies. None describe andexanet alfa as a therapeutic agent for hemophilia itself, so this literature does not constitute supporting evidence for repurposing.)*

---

## Taiwan Market Information

No marketing authorization records currently exist for andexanet alfa in Taiwan (未上市, 0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ Note: TFDA labeling / warnings and contraindications data are marked as a **Blocking** data gap (DG001) — this must be resolved before any Stage 1 (S1) safety pre-assessment can proceed for any indication involving this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (Glanzmann thrombasthenia) has no clinical trials, no literature support, and no plausible mechanistic pathway — the evidence pack's own rationale concludes the score reflects embedding-space artifact rather than pharmacological relevance. Combined with the absence of TFDA safety labeling data (blocking gap), this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA-equivalent label warnings/contraindications before any safety pre-assessment (S1) can begin
- Resolve DG002: obtain a structured MOA record from DrugBank to formally document the factor Xa/TFPI mechanism
- Seek preclinical or case-level evidence specifically testing andexanet alfa (or factor Xa/TFPI-directed agents) in platelet-receptor-defect bleeding disorders, if this indication is to be pursued further
- If no such mechanistic or empirical evidence emerges, this candidate should be deprioritized in favor of higher-scoring, evidence-backed predictions from this drug's full prediction list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

