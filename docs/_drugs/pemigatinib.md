---
layout: default
title: Pemigatinib
parent: 僅模型預測 (L5)
nav_order: 274
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From FGFR-Driven Oncology Use to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib is referenced across this evidence pack as an FGFR1-3 kinase inhibitor; its originally approved indication is not recorded in the current data set.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia**,
but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale text flags the mechanistic link as weak and likely an artifact of the knowledge graph.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack |
| Predicted New Indication | Multiple Endocrine Neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for pemigatinib is not available in this evidence pack. Based on information embedded elsewhere in the pack (repurposing rationale text for other candidates), pemigatinib is consistently described as an **FGFR1-3 kinase inhibitor**, used in a context comparable to other FGFR inhibitors such as infigratinib. This is consistent with its known drug class but is not independently confirmed by a structured MOA field here.

The relationship between pemigatinib's (unrecorded) original indication and Multiple Endocrine Neoplasia (MEN) cannot be established from the data provided, since no original indication is listed and no licenses are on file. What the evidence pack does supply is the model's own mechanistic assessment, which is unfavorable: MEN syndromes are driven primarily by **MEN1 and RET** mutations, and have no established connection to the **FGFR1-3** signaling axis that pemigatinib targets.

Because of this mismatch, the pack's own rationale concludes that the high TxGNN score most likely reflects an **indirect knowledge-graph association** — for example, shared proximity to other endocrine-tumor nodes — rather than a genuine pharmacological mechanism. This should be treated as a low-confidence, hypothesis-generating signal only, not a mechanistically grounded repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Pemigatinib is currently **not marketed** in Norway (market status: 未上市) and no authorization records exist in this evidence pack (total licenses: 0). No product table can be generated at this time.

---

## Cytotoxicity

Pemigatinib is referenced in this evidence pack as an FGFR1-3 kinase inhibitor used in oncology contexts (e.g., discussion of FGFR-driven resistance in HER2+ breast carcinoma, and comparison to other FGFR inhibitors explored in FGFR3-driven skeletal disease). On that basis it is treated here as an antineoplastic, targeted small-molecule therapy, though this classification is inferred rather than confirmed via a structured DrugBank category field.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR1-3 kinase inhibitor) |
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
The top-ranked prediction (Multiple Endocrine Neoplasia) has zero supporting clinical trials or literature, and the model's own mechanistic rationale explicitly states the FGFR1-3 pathway has no established link to MEN pathogenesis — this is an L5, hypothesis-only signal with a stated risk of being knowledge-graph noise.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — flagged as a *Blocking* data gap (DG001)
- Confirmed mechanism of action (MOA) from DrugBank or equivalent source — flagged as a *High* severity data gap (DG002)
- Confirmation of pemigatinib's actual original approved indication(s), currently absent from this pack
- Independent mechanistic or preclinical evidence linking FGFR inhibition to MEN before any further evaluation stage is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

