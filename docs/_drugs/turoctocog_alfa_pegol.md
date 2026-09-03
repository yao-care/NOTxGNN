---
layout: default
title: Turoctocog Alfa Pegol
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog Alfa Pegol: From Hemophilia A to Acquired Coagulation Factor Deficiency

## One-Sentence Summary

Turoctocog alfa pegol is a PEGylated recombinant Factor VIII (FVIII) replacement therapy, originally developed for FVIII deficiency in **Hemophilia A** (inferred from the drug's mechanistic description; formal original-indication data is not yet documented in this evidence pack). The TxGNN model's top-ranked prediction (platelet release disorder) does not hold up mechanistically, so the report instead highlights **Acquired Coagulation Factor Deficiency** as the most pharmacologically plausible candidate among the 10 predictions. **No clinical trials or literature currently support any of the 10 predicted indications** — this is a pure model-prediction (L5) case with an unresolved MOA data gap.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in regulatory data (drug is not yet marketed in Norway); inferred to be Hemophilia A / FVIII deficiency based on drug class |
| Predicted New Indication | Acquired Coagulation Factor Deficiency (selected as the mechanistically strongest of 10 candidates; TxGNN's #1-ranked prediction, platelet release disorder, was assessed as not pharmacologically plausible — see rationale below) |
| TxGNN Prediction Score | 99.97% (rank 525 of all disease predictions) |
| Evidence Level | L5 (model prediction only — no clinical trials or literature for any of the 10 candidates) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action data is currently a documented gap (DG002, High severity — DrugBank API lookup pending). Based on contextual information available in this evidence pack, turoctocog alfa pegol is a **PEGylated recombinant Factor VIII replacement therapy**, used to correct FVIII deficiency in Hemophilia A.

Among the 10 TxGNN-predicted indications, most (platelet release disorder, pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects, constitutional thrombocytopenia, FNAIT, and two ambiguous/likely-mislabeled entries) involve **platelet-level dysfunction or unrelated genetic syndromes**, not coagulation-factor deficiency. FVIII replacement cannot correct platelet granule secretion defects, receptor abnormalities, or membrane phospholipid scrambling — these predictions likely reflect TxGNN's knowledge graph clustering diseases through a shared "bleeding tendency" node rather than genuine pharmacological relevance.

**Acquired Coagulation Factor Deficiency** stands out as the exception: this category includes acquired Hemophilia A (e.g., anti-FVIII autoantibody-mediated FVIII deficiency), for which standard/long-acting FVIII replacement products are already used as supportive therapy in current practice. This is the only one of the 10 predictions where the disease mechanism (FVIII insufficiency) directly matches the drug's mechanism (FVIII replacement) — which is why the evidence pack advances it to decision-stage S1 ("Research Question") while the other 9 remain at S0 (Hold).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Turoctocog alfa pegol is **not marketed in Norway** — no product authorizations are currently registered (0 licenses on file), so no dosage-form or approved-indication table can be produced at this time.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/label warnings and contraindications are flagged as a **Blocking data gap** (DG001) in this evidence pack — they must be resolved before any safety pre-assessment (S1) can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for turoctocog alfa pegol currently have zero supporting clinical trials or literature (L5, prediction-only), the drug is not marketed in Norway, and both the formal MOA data and TFDA/label safety data are documented gaps. Even the mechanistically most plausible candidate (acquired coagulation factor deficiency) has no direct evidence yet — it only qualifies for further inquiry (S1), not advancement.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/Norway label warnings and contraindications before any S1 safety pre-assessment
- Resolve DG002 (High): confirm formal MOA via DrugBank API to validate the FVIII-replacement mechanistic rationale
- Search specifically for literature/case series on FVIII product use in acquired Hemophilia A / acquired coagulation factor deficiency
- Re-evaluate the remaining 9 predictions' plausibility before allocating further review resources to them
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

