---
layout: default
title: Natalizumab
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 5
---

# Natalizumab
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

Using the evidence pack as provided (no external assumptions about natalizumab's known clinical history, since `original_indications`, `licenses`, and `original_moa` are empty/gap in this dataset).

# Natalizumab: From Undocumented Original Indication to Bronchitis

## One-Sentence Summary

Natalizumab (DrugBank ID DB00108) is described in the underlying repurposing rationale as an anti-α4-integrin (VLA-4) monoclonal antibody, but its original approved indication and formal mechanism-of-action record are not documented in the current evidence pack. The TxGNN model's top-ranked prediction is **Bronchitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it reflects knowledge-graph topological similarity only, with no mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (see Data Gaps) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for natalizumab is not available as a structured field in this evidence pack. However, the model's own rationale characterizes natalizumab as an anti-α4-integrin (VLA-4) monoclonal antibody that blocks leukocyte migration across VCAM-1-expressing endothelium into inflamed tissue. This is a mechanism associated with autoimmune/neuroinflammatory conditions, not with acute or chronic airway infection/inflammation (bronchitis).

The evidence pack explicitly states that there is **no direct mechanistic argument** linking VLA-4/VCAM-1 blockade to bronchitis pathophysiology. The high TxGNN score (99.46%) appears to be driven purely by graph-embedding proximity in the knowledge graph, not by any retrieved clinical trial or literature signal — there are zero supporting records of either type for this indication pair.

Given the complete absence of corroborating evidence and the lack of a coherent mechanistic hypothesis, this prediction should be treated as exploratory only, not as a basis for further clinical development at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Natalizumab has **0 authorizations** on record and a market status of "Not Marketed" in this evidence pack — no license entries are available to tabulate.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are not currently available in this evidence pack; the TFDA/product label lookup is flagged as a **Blocking** data gap — see Conclusion.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Bronchitis) has Evidence Level L5 — a model score with zero clinical trials and zero literature support, and the pack's own mechanistic analysis finds no direct rationale connecting the drug's proposed mechanism to this disease. Separately, a **Blocking**-severity data gap (missing TFDA label/warnings) means the candidate cannot even pass an initial safety screen (S1), regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA/regulatory label (warnings, contraindications) — required to clear the S1 safety gate (currently Blocking gap, DG001)
- Verified mechanism-of-action record from DrugBank or primary literature (currently High-severity gap, DG002)
- Confirmed original approved indication(s) for the drug, to establish a baseline for mechanistic comparison
- At minimum, preclinical or observational evidence directly linking α4-integrin/VLA-4 blockade to bronchitis pathophysiology before advancing beyond model-prediction stage

*Note: within this same prediction batch, several other candidate indications for natalizumab (psoriasis, parapsoriasis, acute lichenoid pityriasis) are supported only by case reports describing these conditions as **adverse effects induced or aggravated by natalizumab treatment**, not as therapeutic benefits. These should not be misread as efficacy signals during triage.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

