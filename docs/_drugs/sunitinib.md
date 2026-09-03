---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

Using the report as a direct drafting task (no coding/debugging skill applies) — writing directly per the specified template and evidence pack below.

# Sunitinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

> Sunitinib is a multi-targeted tyrosine kinase inhibitor already established as first-line therapy for advanced/metastatic renal cell carcinoma (RCC), and is also used in GIST and pancreatic neuroendocrine tumors.
> The TxGNN model predicts it may also be effective for **Liposarcoma**,
> with **3 clinical trials** (2 graded highly relevant) and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (established/approved indication; sunitinib is also a standard therapy for GIST and pancreatic neuroendocrine tumor) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available directly from DrugBank in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic evidence gathered for this prediction, sunitinib is a multi-targeted tyrosine kinase inhibitor (TKI) that inhibits VEGFR1/2/3, PDGFRα/β, KIT, FLT3, and RET. Its established efficacy in renal cell carcinoma, GIST, and pancreatic neuroendocrine tumors is driven by blocking tumor angiogenesis (VEGFR) and receptor-tyrosine-kinase-driven proliferation (KIT/PDGFR).

Liposarcoma — particularly the myxoid/round cell subtype — is a highly vascularized soft tissue sarcoma with partial PDGFR pathway activation, which provides a plausible mechanistic bridge from sunitinib's original renal/GI indications to this new tumor type. This rationale is reinforced by two completed Phase II soft tissue sarcoma trials (NCT00400569, NCT00474994) that specifically enrolled liposarcoma patients, along with a dedicated Phase II study (PMID 21154746) evaluating sunitinib across leiomyosarcoma, liposarcoma, and malignant fibrous histiocytoma histologies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label single-site trial of sunitinib malate in metastatic/unresectable soft tissue sarcoma, including leiomyosarcoma, liposarcoma, fibrosarcoma, and MFH; dosed once daily 28/42-day cycles until progression or toxicity |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing study of sunitinib in non-GIST sarcomas, explicitly covering liposarcoma population |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol primarily testing regorafenib (same TKI class) across sarcoma subtypes; sunitinib referenced only as precedent, not directly tested |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase II trial | Int J Cancer | Phase II study of sunitinib malate in relapsed/refractory soft tissue sarcoma, focused on leiomyosarcoma, liposarcoma, and MFH; evaluated safety and efficacy across these histologies |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | Reviews genetic, epigenetic, and transcriptomic alterations in liposarcoma to guide targeted therapy selection |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | Reviews emerging systemic therapies for adult soft tissue sarcoma by subtype |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Discusses histology-driven medical treatment of soft tissue sarcoma, noting high drug activity in myxoid liposarcoma |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case report | Anticancer Res | Long-lasting clinical benefit of sunitinib malate in a heavily pre-treated metastatic liposarcoma patient |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Discusses histological subtype-based medical treatment strategies for soft tissue sarcomas |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Genomic case series | Oncotarget | NGS profiling of extraskeletal myxoid chondrosarcoma, evaluating predictive factors for sunitinib benefit |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Case series | Am J Surg Pathol | Clinicopathologic analysis of a distinctive myofibroblastic sarcoma subtype; tangential relevance to sarcoma classification landscape |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial protocol | BMC Cancer | REGOSARC trial protocol evaluating regorafenib (same TKI class) in advanced soft tissue sarcoma |

---

## Norway Market Information

Sunitinib is currently **not marketed in Norway** — no authorizations are registered in this evidence pack (0 licenses).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-targeted tyrosine kinase inhibitor; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Based on known TKI-class effects reflected in the broader sunitinib literature (e.g., cardiac function and hypertension studies), monitoring of blood pressure, cardiac function, CBC, liver function, and thyroid function should be considered |
| Handling Protection | Please refer to institutional protocols for oral targeted anticancer agent handling |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase II trials and a dedicated liposarcoma-focused study provide moderate (L2) clinical evidence, and the TxGNN score is very high (99.87%). However, sunitinib is not currently marketed in Norway, and both the TFDA/Norway package insert (Blocking gap) and detailed DrugBank MOA data (High-severity gap) are missing, preventing a full safety (S1) evaluation.

**To proceed, the following is needed:**
- Norway/TFDA-equivalent package insert (warnings, contraindications) — currently a blocking data gap
- Verified DrugBank mechanism-of-action data
- Norway market access assessment, given 0 current authorizations
- Liposarcoma-subtype-specific (myxoid/round cell vs. dedifferentiated) efficacy stratification, as current trials pool multiple sarcoma histologies
- Safety monitoring plan for hypertension and cardiac toxicity, known TKI-class risks noted in the broader sunitinib literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

