---
layout: default
title: Romiplostim
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: From Immune Thrombocytopenia (ITP) to Primary Release Disorder of Platelets

## One-Sentence Summary

> Romiplostim is a thrombopoietin (TPO) receptor agonist whose established reference indication is immune thrombocytopenia (ITP) — this is not formally documented in the current dataset, but is consistently implied across the evidence pack's mechanistic rationale.
> The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets**,
> currently supported by **1 clinical trial** and **2 publications**, all indirect (disease-population overlap rather than direct treatment evidence).
> A separate, broader candidate in this same evidence pack — *platelet-type bleeding disorder* — is backed by far stronger direct evidence (7 trials including a completed Phase 3 RCT), and is flagged separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this dataset (`original_indications` empty, `original_moa` = Data Gap). Romiplostim's known reference indication — immune thrombocytopenia (ITP) — is referenced throughout the evidence pack's mechanistic rationale but not formally sourced here. |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L3 (observational study + review/cohort literature; no direct romiplostim RCT for this specific diagnosis) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is currently a data gap (DG002). However, the evidence pack's own repurposing rationale consistently describes romiplostim as a **thrombopoietin (TPO) receptor agonist** that acts on the **MPL receptor** to promote megakaryocyte maturation and platelet release — this is the pharmacological basis cited across nearly every candidate indication in this pack.

"Primary release disorder of platelets" describes a defect in platelet release from megakaryocytes into circulation. Mechanistically, stimulating the MPL receptor to drive megakaryocyte maturation and platelet release is a plausible fit for this category. However, the supporting evidence currently available is drawn from **immune thrombocytopenia (ITP)** research — a *secondary* (immune-mediated) release disorder — rather than from primary/intrinsic release-defect populations specifically. The single linked clinical trial (NCT03820960) is an observational cohort study on thrombosis risk in ITP patients and does not test romiplostim treatment; it was connected by TxGNN due to disease-population overlap, not direct interventional evidence.

In short, the mechanistic logic is sound, but the current evidence base has not yet directly tested romiplostim in patients with a primary (non-immune) platelet release defect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Completed | 10,039 | Observational cohort study on thrombosis risk factors in immune thrombocytopenia (ITP). Does not test romiplostim treatment effect; linked to this indication via disease-population overlap only (relevance grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Reviews megakaryocytopoiesis and thrombopoiesis mechanisms, identifying thrombopoietin (TPO) as the primary growth factor driving megakaryocyte maturation and platelet release. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Cohort | Haematologica | In vitro study showing antiplatelet autoantibodies in ITP patients inhibit proplatelet formation by megakaryocytes, impairing platelet production/release. |

---

## Norway Market Information

No Norway (or Taiwan) market authorization records are currently available for romiplostim in this dataset — the drug is recorded as not marketed (0 authorizations).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are all currently marked as data gaps in this pack; TFDA label retrieval (DG001) is flagged as blocking for a formal safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The mechanistic link between TPO-receptor agonism and platelet release disorders is biologically plausible, but the only supporting trial is an observational ITP cohort study that does not test romiplostim directly, and no interventional evidence exists specifically in primary (non-immune) platelet release-defect patients. This does not yet meet the bar for "Proceed with Guardrails."

**To proceed, the following is needed:**
- TFDA package insert / label data (DG001 — currently blocking, required before any safety pre-assessment)
- Formal mechanism-of-action documentation (DG002)
- A trial or case series testing romiplostim specifically in patients with a primary (intrinsic, non-immune) platelet release defect, rather than ITP-derived inference
- Norway/Taiwan regulatory and market authorization data, currently entirely absent

**Note on a stronger alternative candidate in this same evidence pack:**
Within the same prediction set, *"platelet-type bleeding disorder"* (rank 8, score 99.93%) has substantially stronger direct evidence — **L1**, with a completed Phase 3 RCT (RECITE, chemotherapy-induced thrombocytopenia in GI/pancreatic/colorectal cancer, n=165) plus 6 additional directly relevant trials (post-transplant platelet engraftment, MDS, biosimilar long-term safety) — and is already staged at "Proceed with Guardrails." If the goal is to identify the most actionable repurposing signal for romiplostim rather than strictly the top-ranked TxGNN score, this candidate warrants a separate, dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

