---
layout: default
title: Talimogene Laherparepvec
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 7
---

# Talimogene Laherparepvec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Talimogene Laherparepvec: From Cutaneous Melanoma to Investigational Oncolytic Virotherapy Indications

## One-Sentence Summary

> Talimogene laherparepvec (T-VEC) is an oncolytic HSV-1-based virotherapy whose real-world approved indication is cutaneous malignant melanoma (CMM7) — but this dataset's `drug.original_indications` field is empty, so the model surfaced that known indication as its top "prediction" rather than a genuine repurposing candidate.
> The remaining candidates (leptomeningeal melanoma, uveal melanoma, glottis SCC, occult lung SCC, cloacogenic carcinoma, gallbladder adenosquamous carcinoma) are true novel signals, but **none have any clinical trial or literature evidence captured in this pack**, and several are anatomically incompatible with T-VEC's intratumoural injection route.
> A **Blocking-severity data gap** (missing TFDA label warnings/contraindications) also means this candidate cannot yet enter S1 safety pre-assessment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this dataset (data gap); per the model's own rationale text, T-VEC's real-world approved indication is Cutaneous Malignant Melanoma (marketed as Imlygic) |
| Predicted New Indication | CMM7 (Cutaneous Malignant Melanoma) — **see caveat below: this is not a genuinely novel signal** |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L1 (per dataset; based on external/real-world evidence, not the empty trial/literature arrays in this pack) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** (overridden from the record's "Proceed with Guardrails" — see rationale below) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available from DrugBank for this candidate (`original_moa: [Data Gap]`, DG002). Based on the mechanistic description embedded in the evidence pack's repurposing rationale, T-VEC is an oncolytic herpes simplex virus type-1 (HSV-1) vector that, after intratumoural injection, selectively replicates within and lyses melanoma cells while expressing GM-CSF to prime a systemic anti-tumour immune response. This mechanism is clinically validated and is the basis of T-VEC's approval as Imlygic for melanoma.

**Important data quality caveat:** The rank-1 "predicted" indication, CMM7, is explicitly identified in the record's own rationale text as T-VEC's core, already-approved indication — not a new repurposing opportunity. This happened because `drug.original_indications` was left empty in this dataset, so the pipeline could not distinguish "known indication" from "novel candidate." Its L1 evidence level and empty trial/literature counts should therefore be read as **evidence-collection gaps for an already-established indication**, not as a newly discovered use.

Looking past rank 1, the genuinely novel candidates cluster into two groups by anatomical/mechanistic plausibility:
- **Anatomically incompatible** (Hold, L5): pediatric leptomeningeal melanoma, lung occult SCC, rectal cloacogenic carcinoma, gallbladder adenosquamous carcinoma — these involve CNS, undetectable, or deep-visceral lesions that cannot be reached by T-VEC's approved intratumoural injection route.
- **Mechanistically plausible but evidence-thin** (Research Question, L3–L4): epithelioid uveal melanoma (shares melanocytic lineage and HSV-1 receptor expression, but different molecular drivers and no injectable primary site) and glottis squamous cell carcinoma (head & neck SCC, supported indirectly by T-VEC + pembrolizumab combination trials such as MASTERKEY-232, though no glottis-specific data exists in this pack).

---

## Clinical Trial Evidence

Currently no related clinical trials registered (all `evidence.clinical_trials` arrays are empty across every predicted indication in this pack, including the top-ranked CMM7 entry).

---

## Literature Evidence

Currently no related literature available (all `evidence.literature` arrays are empty across every predicted indication in this pack).

---

## Norway Market Information

Currently no marketing authorization records (`total_licenses: 0`; market status: Not Marketed).

---

## Cytotoxicity

T-VEC is an antineoplastic agent (approved oncolytic virotherapy for cutaneous melanoma), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy — Oncolytic viral therapy (HSV-1 vector engineered to express GM-CSF), not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | As a live, replication-competent oncolytic virus product, handling requires biosafety precautions distinct from standard cytotoxic drug handling regulations (e.g., protection against viral shedding, dedicated waste disposal). Specific TFDA-labelled requirements are unavailable pending resolution of DG001 |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA label warnings, contraindications, and drug interaction data are currently a **Blocking-severity data gap (DG001)** — this candidate cannot proceed to S1 safety pre-assessment until this is resolved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for the top-ranked indication (CMM7/cutaneous melanoma) is strong, but it reflects T-VEC's existing approved use rather than a genuine repurposing opportunity — a data registration gap, not a discovery. All truly novel candidates (ranks 2–7) carry weak evidence (L3–L5) and several are ruled out by route-of-administration incompatibility. Combined with a Blocking safety data gap, no candidate in this pack can currently justify a "Go" or "Proceed with Guardrails" decision.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA label PDF for warnings/contraindications before any S1 safety evaluation
- Resolve DG002 (High): retrieve full MOA data via DrugBank API
- Correct `drug.original_indications` to reflect T-VEC's actual approved indication (cutaneous melanoma) so future TxGNN runs don't re-surface it as a "new" prediction
- For genuinely novel candidates — particularly glottis SCC — source dedicated trial/literature evidence (e.g., MASTERKEY-232 data) before advancing beyond Research Question stage
- Clarify local market status/regulatory pathway, since a marketing authorization application may itself be a prerequisite before any repurposing indication can be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

