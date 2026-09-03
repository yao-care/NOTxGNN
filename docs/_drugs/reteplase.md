---
layout: default
title: Reteplase
parent: 僅模型預測 (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Reteplase
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

# Reteplase: From Acute Myocardial Infarction to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Reteplase (recombinant plasminogen activator, DB00015) is an established thrombolytic used for acute myocardial infarction, as confirmed by multiple trials in this evidence pack (e.g., GUSTO-V, SPEED/GUSTO-4).
The TxGNN model predicts it may also be effective for the anatomically distinct subtype **Posteroinferior Myocardial Infarction**,
but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction (L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Myocardial Infarction (thrombolytic therapy) — inferred from cited trial/literature context; no Norway license record available |
| Predicted New Indication | Posteroinferior Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on information embedded in the evidence pack, reteplase is a recombinant tissue plasminogen activator (also referenced as BM 06.022), a thrombolytic that dissolves coronary thrombi. Its efficacy in acute myocardial infarction — the general condition — has been demonstrated across several large trials (e.g., NCT00046228, PMID 11079647, PMID 15800019), all involving reteplase for acute MI in various clinical settings.

Posteroinferior myocardial infarction is an anatomical location subtype of acute MI, not a distinct disease with a different pathophysiology. Since reteplase already dissolves the causative coronary thrombus regardless of infarct location, the mechanistic rationale for this "new" indication is strong in principle. However, the very high TxGNN score most likely reflects disease-ontology granularity (a location-specific ICD/ontology term nested under a broader indication already treated by the drug) rather than a genuinely novel therapeutic hypothesis — hence no dedicated trials or literature exist for this specific subtype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Norway Market Information

Reteplase is currently **not marketed** in Norway. No authorization records (0 licenses) are available in the evidence pack, so no dosage form or approved indication text can be extracted.

## Safety Considerations

Please refer to the package insert for safety information.

> Note: TFDA/Norway label warnings and contraindications (DG001) are marked as a **Blocking** data gap in this evidence pack — this prevents formal S1 safety screening for this candidate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (posteroinferior MI) has no supporting clinical trials or literature — it is evidence level L5 (model prediction only). Combined with the blocking gap in TFDA safety/label data, this candidate cannot proceed past S0/S1 review at this time.

**To proceed, the following is needed:**
- TFDA/Norway package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Subtype-specific (posteroinferior MI) trial or registry data, if any exist outside PubMed/ClinicalTrials.gov
- **Consider re-evaluating this candidate profile using a better-evidenced predicted indication from the same pack**: rank 3 "septal myocardial infarction" (L2, one completed Phase 3 RCT — NCT00046228) or rank 5 "coronary stenosis" (L3, six supporting publications including facilitated-PCI cohort data) show substantially stronger evidence bases within this same drug's prediction set.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

