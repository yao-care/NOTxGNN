---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 235
evidence_level: L5
indication_count: 8
---

# Moroctocog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Moroctocog Alfa: From Hemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

> Moroctocog alfa is a recombinant coagulation Factor VIII (FVIII) product, pharmacologically indicated in the class of Hemophilia A / FVIII replacement therapy; however, formal Norway regulatory indication text is unavailable because the product is **not marketed in Norway**.
> The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but currently **0 relevant clinical trials** and **0 publications** support this specific direction — the 7 retrieved trials are all graded "C" (not related to the predicted disease).
> This top-ranked TxGNN prediction appears to be a database co-morbidity artifact rather than a mechanistically grounded signal; a lower-ranked candidate (Acquired Coagulation Factor Deficiency, rank 4) shows substantially stronger and more plausible evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Norway regulatory data (product not marketed); drug class is recombinant FVIII, typically used for Hemophilia A |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, moroctocog alfa is a recombinant human Factor VIII (FVIII) product, functioning by replacing deficient clotting factor activity in the coagulation cascade — its established use is in Hemophilia A.

Primary release disorder of platelets (a platelet storage pool disease) is pathologically distinct from Hemophilia A: the defect lies in platelet granule content/release, not in plasma coagulation factor levels or activity. Supplementing FVIII does not address a platelet secretion defect, so there is no direct mechanistic pathway linking moroctocog alfa's pharmacology to this disease.

Consistent with this, the retrieved clinical trials for this prediction are all graded "C" — they concern unrelated topics (hemophilia A prophylaxis trials, AML hematology monitoring, post-COVID-19 vaccination syndrome, artificial liver support, portal vein hemostasis) rather than platelet storage pool disease itself. This pattern is typical of a TxGNN co-morbidity/graph-proximity artifact rather than a genuine mechanistic signal, and the evidence pack's own rationale explicitly flags this as a likely false positive.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Phase 3 | Completed | 159 | BIVV001 (rFVIIIFc-VWF-XTEN) prophylaxis in severe Hemophilia A — not related to platelet release disorder |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Phase 3 | Completed | 74 | Pediatric BIVV001 safety/efficacy in severe Hemophilia A — not related |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Phase 3 | Completed | 30 | PEGylated rFVIII (BAX 855) in Hemophilia A patients undergoing surgery — not related |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Not yet recruiting | 80 | Coagulation profiling in AML patients — observational, not a treatment trial |
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Recruiting | 200 | Lab evaluation of post-COVID-19-vaccination syndrome — not related |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Recruiting | 25 | Artificial liver support system in acute-on-chronic liver failure — not related |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Recruiting | 45 | Systemic/portal hemostasis during TIPS placement — not related |

**Note:** None of the retrieved trials directly investigate moroctocog alfa (or FVIII therapy) for primary release disorder of platelets. All were graded "C" (not relevant) in the evidence pack's own relevance assessment.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Moroctocog alfa currently holds **no marketing authorization in Norway** (0 licenses on file). No product/dosage-form data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (primary release disorder of platelets) lacks any supporting clinical trial or literature evidence, and the disease's underlying platelet-granule-release pathology has no plausible mechanistic link to FVIII replacement. Combined with the product's non-marketed status in Norway, this candidate does not meet the threshold to advance past model-prediction-only status.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) documentation for moroctocog alfa
- TFDA/Norway-equivalent product labeling (warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- If this indication is still of interest: preclinical/mechanistic studies specifically linking FVIII pharmacology to platelet storage pool disease, since none currently exist

**Additional note for portfolio consideration:**
Within the same evidence pack, **rank 4 — Acquired Coagulation Factor Deficiency** — shows a materially stronger signal (Evidence Level L3, decision stage S2, "Research Question"), including two completed Phase 2/3 trials on structurally analogous B-domain-deleted recombinant FVIII products (NCT01178294, NCT04580407) in acquired Hemophilia A. This candidate is mechanistically coherent with moroctocog alfa's known FVIII activity and may warrant separate evaluation as a more promising repurposing direction than the top-ranked candidate reviewed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

