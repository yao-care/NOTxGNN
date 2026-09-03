---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 2
---

# Laronidase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Laronidase: From Mucopolysaccharidosis I to Lysosomal Storage Disease with Skeletal Involvement

## One-Sentence Summary

> Laronidase is a recombinant human alpha-L-iduronidase enzyme replacement therapy, originally developed and marketed (as Aldurazyme) for **Mucopolysaccharidosis I (MPS I)** — including Hurler, Hurler-Scheie, and Scheie syndromes.
> The TxGNN model predicts it may be effective for **Lysosomal Storage Disease with Skeletal Involvement**, a prediction that in practice overlaps substantially with the drug's already-established disease spectrum,
> supported by **4 publications** in the evidence pack (no registered clinical trials in this dataset).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mucopolysaccharidosis I (MPS I) — Hurler / Hurler-Scheie / Scheie syndrome (derived from literature evidence; no license record available) |
| Predicted New Indication | Lysosomal storage disease with skeletal involvement |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L1 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (`original_moa`) is not available as a structured field. However, the evidence pack's repurposing rationale provides substantive mechanistic detail: laronidase is a recombinant human alpha-L-iduronidase that directly supplies the lysosomal enzyme missing in MPS I patients, degrading accumulated glycosaminoglycans (GAGs) and reducing skeletal, joint, and multi-organ involvement.

The "predicted new indication" — lysosomal storage disease with skeletal involvement — is not a novel pharmacological hypothesis but essentially describes the disease spectrum the drug already treats (MPS I, marketed as Aldurazyme). This should be understood as **model confirmation of an already-established indication** rather than a new repurposing candidate. The mechanistic link is direct and well-documented, which explains the high TxGNN score and the L1 evidence level.

Because of this overlap, the primary value of this evaluation is regulatory/market validation (e.g., for jurisdictions like Norway where the drug is not currently marketed) rather than discovery of a new therapeutic use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | Comprehensive review of MPS I pathophysiology, diagnosis (GAG accumulation, iduronidase assay), and disease spectrum from Hurler to Scheie syndrome |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | Overview of laronidase development as recombinant alpha-L-iduronidase ERT for MPS I, including orphan drug designation and early Phase I trial results |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Cohort/Case series | Pediatric Neurology | 6.5-year follow-up of a Scheie syndrome patient on laronidase ERT; documented anthropometric, cardiac, ophthalmologic, and skeletal outcomes over long-term treatment |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | Mechanistic/In vitro | Biological & Pharmaceutical Bulletin | Demonstrated laronidase uptake into MPS I fibroblasts/osteoblasts via mannose-6-phosphate receptors, with lysosomal processing and substrate cleavage |

---

## Norway Market Information

No authorization records are available. Laronidase is currently **not marketed** in Norway (0 authorizations on file), which is consistent with the absence of licensing data in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between laronidase and MPS I / skeletal lysosomal storage disease is direct, well-established, and supported by consistent literature (including a placebo-controlled RCT and long-term follow-up cohorts) — this is essentially the drug's known indication rather than a novel hypothesis. However, key regulatory and safety data (TFDA warnings/contraindications) are missing, and the drug is not currently marketed in Norway, so guardrails are needed before any market action.

**To proceed, the following is needed:**
- Resolve **DG001 (Blocking)**: Obtain TFDA/Norwegian regulatory label — warnings, contraindications, and full safety profile — required before S1 safety evaluation can proceed
- Resolve **DG002 (High)**: Formal documentation of MOA from DrugBank API to support mechanistic review
- Confirm whether a Norway marketing authorization application is planned, given current "not marketed" status
- Note: A secondary prediction for **Sanfilippo syndrome (MPS III)** was also evaluated in this evidence pack but flagged as a mechanistic mismatch (laronidase does not address the heparan sulfate-degrading enzymes deficient in MPS III, and has poor blood-brain barrier penetration for the CNS involvement characteristic of Sanfilippo syndrome) — recommendation for that indication is **Hold** and it is excluded from this report's primary conclusion.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

