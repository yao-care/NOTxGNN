---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Advanced Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

> Everolimus is an mTOR inhibitor (rapalog) with established use in advanced renal cell carcinoma, based on descriptions found in the supporting literature.
> The TxGNN model predicts it may also be effective for **Liposarcoma**,
> with **1 clinical trial** and **5 publications** currently supporting this direction.
> No official Taiwan/Norway marketing authorization or label safety data are available for this candidate, which limits the strength of this conclusion.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced Renal Cell Carcinoma (post-antiangiogenic therapy) — inferred from literature context (PMID 33867192); no formal license/label data available |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 (1 published Phase 2 trial, formal status still Active/Not Recruiting) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not provided directly in the DrugBank field for this candidate (data gap). However, the supporting literature in this evidence pack consistently and repeatedly describes everolimus as **"an mTOR inhibitor"** (e.g., PMID 33867192, PMID 27601542), consistent with its known classification as a rapalog. Everolimus was originally used in advanced renal cell carcinoma, a setting where the PI3K/Akt/mTOR signaling axis is a well-established driver of tumor growth.

Liposarcoma — specifically the dedifferentiated subtype (DDL) — shares this same pathway biology. PMID 26518767 directly demonstrates **activation of the Akt-mTOR pathway in dedifferentiated liposarcoma specimens**, providing a molecular rationale for mTOR-targeted intervention. Because DDL frequently also harbors CDK4 amplification, combining everolimus with a CDK4/6 inhibitor (ribociclib) — as tested in NCT03114527 and reported in PMID 37967116 — offers a mechanistically synergistic approach: CDK4/6 inhibition addresses the cell-cycle driver while mTOR inhibition addresses the downstream survival pathway. This provides a plausible, biology-driven basis for the TxGNN prediction rather than a purely statistical association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Two-arm study of ribociclib + everolimus in advanced dedifferentiated liposarcoma (Arm A) and leiomyosarcoma (Arm B) after ≥1 prior systemic therapy; evaluates anti-tumor activity of combined CDK4/6 and mTOR inhibition. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 clinical trial report | Clinical Cancer Research | Reports the ribociclib + everolimus (SAR-096) trial; CDK4/mTOR combination shows synergistic growth inhibition in DDL/LMS tumor models, supporting clinical rationale. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX mouse models identify effective combination regimens with CDK inhibitors (e.g., palbociclib) in sarcomas, supporting cell-cycle/mTOR pathway targeting strategy. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/immunohistochemical study | Tumour Biology | Demonstrates activation of the Akt-mTOR and MAPK pathways in dedifferentiated liposarcoma specimens; in vitro data show antitumor effect of an mTOR inhibitor. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical | Anticancer Research | Evaluates eribulin in combination with mechanistically different anticancer agents in liposarcoma models; broad-spectrum combination antitumor activity context. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Mechanistic study | Oncogene | Identifies XPO1 inhibitor (selinexor) disruption of the core transcriptional circuitry driving DDLPS; supports the concept of targeting dysregulated survival/transcriptional pathways in this tumor type. |

---

## Norway Market Information

Currently not marketed in Norway; no license/authorization records are available in the evidence pack.

---

## Cytotoxicity

Everolimus is an oncology-use mTOR-targeted agent and is therefore included here.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalog) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Not available in the evidence pack; please refer to the package insert |
| Emetogenicity Classification | Not available in the evidence pack; please refer to the package insert |
| Monitoring Items | Not available in the evidence pack; please refer to the package insert |
| Handling Protection | Not available in the evidence pack; please refer to the package insert |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
There is a biologically plausible mechanistic link (Akt-mTOR pathway activation in DDL) and an actively reported Phase 2 combination trial (ribociclib + everolimus), which together support cautious further evaluation. However, the trial itself is not yet formally completed, and this candidate carries a **Blocking** data gap (TFDA/local label warnings and contraindications) that must be resolved before any safety-relevant decision can be finalized.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label/package insert warnings and contraindications
- Resolve DG002 (High): confirm mechanism of action via DrugBank API query
- Confirm formal completion and topline results of NCT03114527
- Clarify the original approved indication(s) via an authoritative regulatory source, since `taiwan_regulatory.licenses` is currently empty and the "original indication" in this report was inferred from literature context only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

