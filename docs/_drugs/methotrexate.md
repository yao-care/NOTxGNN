---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

# Methotrexate: From Antifolate Chemotherapy/Immunomodulatory Use to Pulmonary Blastoma

## One-Sentence Summary

> Methotrexate (DrugBank DB00563) is a dihydrofolate reductase (DHFR) inhibitor long used across oncology and autoimmune disease settings, though no formal original-indication or regulatory record is present in this evidence pack. TxGNN's top-ranked prediction is **Pulmonary Blastoma**, but this candidate is currently supported by **0 clinical trials** and **0 publications** — it is a pure model output with no clinical or mechanistic corroboration to date.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record — `taiwan_regulatory.licenses` is empty and `original_indications` is empty (see Data Gaps DG001/DG002) |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack (`original_moa: [Data Gap]`, DG002, severity High). Based on the mechanistic rationale attached to this candidate, methotrexate acts as a DHFR inhibitor, blocking folate-dependent purine and pyrimidine synthesis and thereby exerting cytotoxic pressure on rapidly dividing cells — a mechanism broadly applicable across many malignancies.

Pulmonary blastoma, however, is an extremely rare sarcomatoid lung tumor. The rationale explicitly states that there is currently no mechanistic discussion or clinical data connecting methotrexate to this specific tumor type — the association exists solely as an output of the TxGNN network-similarity model, without any corroborating trial or literature signal.

Given the complete absence of supporting evidence, this specific prediction should be treated as hypothesis-generating only, not as a basis for clinical or research prioritization at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

No marketing authorizations are on record for this product in the current dataset (`total_licenses = 0`, `market_status = 未上市 / Not Marketed`). No license table can be populated.

---

## Cytotoxicity

Methotrexate is a conventional antimetabolite/antifolate cytotoxic agent (criterion: known cytotoxic chemotherapy class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite / Antifolate — DHFR inhibitor) |
| Myelosuppression Risk | High — literature within this evidence pack repeatedly documents dose-limiting hematologic toxicity and nephrotoxicity-related prolonged exposure requiring rescue interventions (e.g., leucovorin rescue, high-flux hemodialysis) in high-dose regimens |
| Emetogenicity Classification | Low to moderate, dose-dependent (higher with high-dose IV regimens) |
| Monitoring Items | CBC with differential, renal function (creatinine/eGFR), hepatic function, serum MTX levels for high-dose regimens, mucositis/oral toxicity |
| Handling Protection | Must follow cytotoxic/hazardous drug handling regulations during preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as data gaps in this evidence pack — DG001, Blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Pulmonary Blastoma) has an L5 evidence level — no clinical trials and no literature support this specific indication. It is purely an algorithmic output and cannot proceed to safety or clinical evaluation without independent substantiation.

**To proceed, the following is needed:**
- TFDA/Norway package-insert data (warnings, contraindications, DDI) — currently Blocking (DG001)
- Confirmed mechanism-of-action documentation from DrugBank (DG002)
- Independent mechanistic or preclinical rationale linking methotrexate to pulmonary blastoma specifically, before any trial or literature search is warranted
- **Note:** within this same evidence pack, other predicted indications for methotrexate carry substantially stronger evidence (e.g., *Hodgkin's lymphoma* and *rhabdomyosarcoma*, both L2/S2 "Proceed with Guardrails"). If the goal is near-term repurposing evaluation, those candidates warrant separate reports and should be prioritized over Pulmonary Blastoma.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

