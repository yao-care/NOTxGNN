---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 9
---

# Enfortumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Enfortumab Vedotin: From Unspecified Original Indication to Leprosy (Low-Confidence Signal)

## One-Sentence Summary

Enfortumab vedotin is an antibody-drug conjugate (ADC) targeting Nectin-4; this evidence pack does not include its original regulatory indication or mechanism-of-action data. TxGNN's top-ranked prediction is **Leprosy** (score 99.53%), but there are **zero clinical trials and zero publications** supporting this signal, and the model's own mechanistic rationale flags it as probable graph noise rather than a genuine biological relationship. All 9 predicted indications in this pack carry a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not provided (no license/regulatory data; drug not marketed) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for enfortumab vedotin in this evidence pack. Based on the literature evidence that is present (a 2025 FAERS pharmacovigilance study on ADCs in bladder cancer), the drug's real-world use context appears to be an anti-Nectin-4 antibody-drug conjugate delivering the cytotoxic payload MMAE (monomethyl auristatin E) in advanced bladder cancer — but this is inferred from a safety-signal paper, not confirmed regulatory or indication data.

For the top-ranked prediction, **leprosy**, no mechanistic link exists between Nectin-4 targeting or a microtubule-disrupting cytotoxin and *Mycobacterium leprae* infection. The rationale accompanying this prediction states explicitly: *"Enfortumab vedotin is an anti-Nectin-4 ADC (MMAE payload); there is no known mechanism explaining efficacy against leprosy infection. The high TxGNN score likely reflects lack of biological grounding and may represent knowledge-graph noise."*

This same pattern repeats across all 9 predictions in this pack: multiple endocrine neoplasia, cerebral infarction, HIV, homozygous familial hypercholesterolemia, and two veterinary/non-human diseases (infectious bovine rhinotracheitis, malignant catarrh) all lack any plausible mechanistic connection to an ADC cytotoxic payload. The one indication with literature support, candidiasis, is contradicted by the direction of the evidence — the cited paper describes ADC-associated immunosuppression as an **adverse-event risk signal**, not a therapeutic rationale. Taken together, this cluster of predictions does not currently support any repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the top-ranked indication (leprosy).

---

## All Predicted Indications (Ranked Summary)

Because this evidence pack evaluates multiple low-confidence signals for the same drug, the full ranked set is summarized below rather than a single indication in isolation.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|----------------------|-------------|-----------------|------|
| 1 | Leprosy | 99.53% | L5 | No mechanistic basis; likely graph noise |
| 2 | Multiple endocrine neoplasia | 99.43% | L5 | No mechanistic basis |
| 3 | Cytomegalovirus infection | 99.36% | L5 | Any ADC-related link would be immunosuppression risk, not therapeutic benefit |
| 4 | Candidiasis | 99.30% | L4 | Sole literature (FAERS study) describes ADC-associated infection risk, not treatment efficacy — evidence direction contradicts prediction |
| 5 | Cerebral infarction | 99.23% | L5 | No mechanistic basis |
| 6 | HIV infectious disease | 99.19% | L5 | No mechanistic basis |
| 7 | Homozygous familial hypercholesterolemia | 99.18% | L5 | No mechanistic basis |
| 8 | Infectious bovine rhinotracheitis | 99.13% | L5 | Non-human (veterinary) disease |
| 9 | Malignant catarrh | 99.13% | L5 | Non-human (veterinary) disease |

---

## Norway Market Information

The drug is not marketed and has no registered authorizations in this dataset (0 licenses).

---

## Cytotoxicity

Based on drug-class inference from the available literature (ADC context in bladder cancer), enfortumab vedotin is treated as an antineoplastic agent for this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (antibody-drug conjugate delivering an MMAE cytotoxic payload) |
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
No clinical trial or literature evidence supports any of the 9 predicted indications above L4, and the highest-scoring prediction (leprosy) has an explicitly stated lack of biological plausibility. The one candidate with supporting literature (candidiasis) is contradicted in direction — the evidence describes a safety risk, not a treatment rationale. Combined with missing original indication and MOA data, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- TFDA/regulatory label (warnings, contraindications) — currently a **Blocking** data gap (DG001); required before any S1 safety screening
- Confirmed mechanism of action data from DrugBank — currently a **High** severity gap (DG002)
- Original indication and regulatory history for the drug
- If any of these 9 signals are to be pursued further, dedicated literature/clinical-trial searches specific to that disease-drug pair, since none currently exist beyond the single (contradictory) candidiasis reference
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

