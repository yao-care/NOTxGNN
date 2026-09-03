---
layout: default
title: Ziconotide
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 10
---

# Ziconotide
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

# Ziconotide: From Severe Chronic Pain to Migraine Disorder

## One-Sentence Summary

> Ziconotide is an N-type calcium channel blocker administered via intrathecal infusion, originally used for the management of severe chronic pain in patients who cannot tolerate or fail systemic analgesics. The TxGNN model predicts it may also be effective for **Migraine Disorder**, but this direction is currently supported by only **1 case report** and **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe chronic pain (intrathecal therapy) — not specified in the evidence pack; based on general drug knowledge only |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (original_moa: Data Gap). Based on the model's own rationale, ziconotide selectively blocks N-type (Cav2.2) voltage-gated calcium channels, which suppresses release of neurotransmitters — including CGRP and glutamate — from afferent terminals in the spinal dorsal horn and trigeminal system. This is mechanistically plausible for migraine, since CGRP-mediated trigeminal signaling is a well-established driver of migraine pathophysiology.

However, ziconotide's proven efficacy is in chronic, severe, treatment-refractory pain delivered exclusively via implanted intrathecal pump — an invasive delivery route with a narrow therapeutic window (risk of neuropsychiatric and cognitive adverse effects). Migraine is typically managed with oral, subcutaneous, or nasal therapies; extrapolating from intrathecal chronic-pain use to migraine management represents a substantial leap in both mechanism-to-clinic translation and feasible route of administration.

The only direct clinical evidence identified is a single case report describing resolution of chronic migraine with intrathecal ziconotide in a patient already using an intrathecal pump for other indications — this is hypothesis-generating, not confirmatory, evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26392785](https://pubmed.ncbi.nlm.nih.gov/26392785/) | 2015 | Case Report | Journal of Pain Research | Single case of chronic migraine headache resolution following intrathecal ziconotide, in a patient with pre-existing intrathecal pump for chronic pain |

---

## Norway Market Information

Ziconotide currently holds no marketing authorization in Norway (market status: 未上市 / Not marketed). No license records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and DDI data are marked as data gaps in this evidence pack — see DG001 below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence for migraine is a single case report (L4), with no clinical trials, no dedicated MOA data, and no Norwegian regulatory/safety information available. The proposed intrathecal delivery route is also poorly aligned with standard migraine treatment paradigms, further weakening feasibility.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): Official label warnings/contraindications, ideally sourced from TFDA or equivalent regulatory PDF
- Resolve DG002 (High): Confirmed mechanism of action data from DrugBank
- Additional clinical evidence beyond a single case report (e.g., case series, observational study) before advancing past S1
- Assessment of route compatibility — intrathecal pump implantation is not standard practice for migraine and would require separate risk-benefit justification
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

