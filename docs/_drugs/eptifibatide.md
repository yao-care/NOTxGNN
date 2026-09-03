---
layout: default
title: Eptifibatide
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# Eptifibatide: From Acute Coronary Syndrome to Rheumatoid Arthritis

## One-Sentence Summary

Eptifibatide is a GPIIb/IIIa platelet aggregation inhibitor established in the treatment of acute coronary syndrome (unstable angina/NSTEMI), as referenced in the supporting literature.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-based signal with no empirical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Coronary Syndrome (unstable angina/NSTEMI) — inferred from literature context; no formal regulatory indication text on file |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known information, eptifibatide is a synthetic cyclic heptapeptide that antagonizes the αIIbβ3 (GPIIb/IIIa) platelet surface receptor, blocking fibrinogen-mediated platelet aggregation — its established efficacy is in acute coronary syndromes.

The core pathology of rheumatoid arthritis (RA) is synovial immune-cell infiltration and cytokine-driven inflammation (TNF-α, IL-6, etc.). While platelets are known to contribute to some inflammatory amplification loops, there is no established mechanistic link between GPIIb/IIIa inhibition and RA's primary autoimmune pathogenesis.

This prediction is explicitly flagged in the evidence pack itself as a **high TxGNN score without any corroborating mechanistic, preclinical, or clinical evidence**. It should be treated as a hypothesis-generation signal only, not as a basis for clinical action.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Eptifibatide is currently **not marketed** in Norway, and no product license records are available in this evidence pack. Market entry status would need to be re-verified with the Norwegian Medicines Agency (Legemiddelverket) or equivalent regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-drug interaction data were available for eptifibatide in this evidence pack; TFDA/product-label data collection is flagged as a blocking data gap that must be resolved before any safety review can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rheumatoid arthritis) carries a high TxGNN similarity score but zero clinical trial or literature support (Evidence Level L5), and the evidence pack itself notes no established mechanistic connection between eptifibatide's antiplatelet action and RA's immune pathogenesis. There is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve the blocking data gap: TFDA/product label warnings and contraindications (DG001)
- Resolve mechanism-of-action data gap via DrugBank API query (DG002)
- If pursuing repurposing for this drug at all, consider prioritizing the **hemoglobinopathy / sickle cell disease** candidates instead (ranks 2–10 in this evidence pack), which — unlike rheumatoid arthritis — are backed by a completed Phase 1/2 RCT (NCT00834899) and four supporting PubMed publications (PMID 17916103, 22156199, 23973010, 29322543) on eptifibatide in sickle cell painful crises
- Obtain Norway market/regulatory status confirmation, since no license data currently exists in this pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

