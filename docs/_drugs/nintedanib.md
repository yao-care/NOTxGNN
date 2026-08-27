---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 3
---

# Nintedanib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Nintedanib: From Idiopathic Pulmonary Fibrosis to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

> Nintedanib is a triple angiokinase inhibitor (targeting VEGFR/FGFR/PDGFR) internationally approved for idiopathic pulmonary fibrosis (IPF) and, in combination with docetaxel, for non-small cell lung cancer.
> The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**,
> but currently **0 clinical trials** and only **1 non-drug-specific review article** support this direction — the case rests on mechanistic plausibility rather than direct clinical evidence.

*Note: this evidence pack contains no Norway licensing data for nintedanib (market status: unmarketed, 0 authorizations), so the original indication above reflects the drug's known international approvals rather than a Norway-specific label.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (IPF); NSCLC (in combination with docetaxel) — general international indication; no Norway-specific license text available |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 |
| Norway Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Nintedanib is described in the evidence pack's repurposing rationale as a **triple angiokinase inhibitor**, with activity against PDGFRα/β in addition to VEGFR and FGFR (the drug-level `original_moa` field itself is flagged as a data gap — DG002 — but this mechanistic detail is preserved in the rationale text). This PDGFR-inhibitory activity is the pharmacological basis for the DFSP prediction.

DFSP is a well-characterized soft tissue tumor driven by the **COL1A1-PDGFB fusion gene**, which causes constitutive activation of the PDGFRB receptor — this is an established, textbook oncogenic mechanism, and it is precisely why the current standard-of-care agent for DFSP (imatinib) works by inhibiting PDGFR. Because nintedanib also inhibits PDGFR signaling, there is a plausible theoretical overlap between its pharmacology and DFSP's driver pathway, which is consistent with the model's very high prediction score (0.9915).

However, this remains a **mechanism-level hypothesis, not a demonstrated clinical effect**. No nintedanib-specific clinical trial or case data for DFSP currently exists; the only supporting literature is a general review of PDGFR-inhibitor drug class pharmacology, not a nintedanib/DFSP-specific study.

Two additional candidates were flagged by the model with similar scores — **liposarcoma** (0.9913, rank 8457) and **ovarian myxoid liposarcoma** (0.9911, rank 8580) — but both are evidence level L5 (model prediction only, no supporting trials or literature) and carry weaker or unconfirmed mechanistic rationale (liposarcoma subtypes show only inconsistent PDGFR/FGFR upregulation; myxoid liposarcoma is driven by FUS-DDIT3/EWSR1-DDIT3, a pathway with no established link to nintedanib's targets). Both are recommended **Hold** and are not pursued further in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | Reviews the role of small-molecule PDGFR inhibitors (as a drug class) in treating neoplastic disorders; discusses PDGF/PDGFR biology relevant to tumors like DFSP, but does not report nintedanib-specific or DFSP-specific clinical data |

---

## Norway Market Information

Nintedanib is currently **not marketed in Norway** (0 marketing authorizations on record), so no license/product table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(No structured key warnings, contraindications, or drug-interaction data are currently available in this evidence pack — TFDA/Norway package insert data is flagged as a Blocking data gap, DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The mechanistic rationale (PDGFR inhibition overlapping with DFSP's COL1A1-PDGFB driver pathway) is biologically plausible and mirrors the established mechanism of the current DFSP standard of care (imatinib), which is why TxGNN assigns a very high score. However, there are zero clinical trials and no drug-specific literature confirming this in practice — evidence level L4 means this is currently a research hypothesis, not a validated repurposing candidate.

**To proceed, the following is needed:**
- Norway/TFDA package insert data — key warnings and contraindications (DG001, Blocking)
- Confirmed structured mechanism-of-action documentation from DrugBank (DG002, High)
- Preclinical (in vitro/in vivo) or case-report evidence of nintedanib activity specifically in DFSP
- Clarification of Norway regulatory/market pathway, given the drug currently has no local marketing authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

