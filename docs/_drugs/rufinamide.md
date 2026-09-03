---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

> Rufinamide is a triazole-derivative anticonvulsant; within this evidence pack, its established role is referenced only indirectly as basis therapy for Lennox-Gastaut syndrome (the formal `original_indications` field is empty).
> The TxGNN model predicts it may be effective for **febrile infection-related epilepsy syndrome (FIRES)**,
> but this is currently supported by **0 clinical trials** and **0 publications** — the prediction score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in evidence pack (`original_indications` is empty); Lennox-Gastaut syndrome is referenced only within the rank-5 rationale text, pending TFDA label confirmation (DG001) |
| Predicted New Indication | Febrile infection-related epilepsy syndrome (FIRES) |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Norway Market Status | 未上市 (Not Marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action (MOA) data for rufinamide is not available in this evidence pack — this is flagged as a High-severity data gap (DG002). Within the pack's own text, rufinamide's use in Lennox-Gastaut syndrome (LGS) — a severe childhood epileptic encephalopathy frequently involving epileptic spasms and multiple seizure types — is cited as existing "indication basis" (see rank-5 rationale), and the drug's presumed broad-spectrum sodium-channel modulation is used elsewhere in the pack to argue plausibility for related syndromes.

For the top-ranked candidate, febrile infection-related epilepsy syndrome (FIRES), the pack does not yet contain a specific mechanistic rationale (`mechanistic_link`/`similarity_to_original` are marked "pending"). FIRES is a rare, severe epileptic encephalopathy triggered by febrile illness that frequently progresses to super-refractory status epilepticus and is often treated with agents effective in other refractory epileptic encephalopathies. Given rufinamide's referenced role in LGS and the sodium-channel mechanism invoked for adjacent candidates in this same pack, extension to FIRES is mechanistically plausible in principle — but currently this rests solely on the TxGNN score, with no confirmatory trial, ICTRP, or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Norway Market Information

Rufinamide is not currently marketed and has zero authorizations on file (`total_licenses: 0`, `licenses: []`) — no marketing-authorization table can be generated from this evidence pack.

## Safety Considerations

Please refer to the package insert for safety information.

> **Data gap note:** TFDA/product-label warnings and contraindications are marked as a **Blocking** data gap (DG001) — per the evidence pack, this specifically prevents entry into the S1 safety initial-assessment stage. No key warnings, contraindications, or DDI records are currently on file (`ddi.query_status: not_found`).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked indication (FIRES) has Evidence Level L5 — a TxGNN score with zero supporting trials or literature — and the drug is unmarketed with a blocking data gap on safety labeling (DG001), which by itself prevents any S1 safety assessment.

**To proceed, the following is needed:**
- TFDA product label (warnings/contraindications) — resolves DG001, currently blocking
- Confirmed mechanism of action via DrugBank API — resolves DG002
- Confirmation of rufinamide's actual original approved indication(s), since `original_indications` is currently empty
- Targeted literature/clinical-trial search specific to FIRES to move beyond L5
- Regulatory pathway assessment, given zero current market authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

