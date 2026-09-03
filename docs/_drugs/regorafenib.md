---
layout: default
title: Regorafenib
parent: 僅模型預測 (L5)
nav_order: 300
evidence_level: L5
indication_count: 8
---

# Regorafenib
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

# Regorafenib: From Metastatic Colorectal Cancer to Liposarcoma

## One-Sentence Summary

Regorafenib is an oral multi-kinase inhibitor originally developed for metastatic colorectal cancer, GIST, and hepatocellular carcinoma.
The TxGNN model predicts it may be effective for **Liposarcoma**, with **2 clinical trials** and **9 publications** currently addressing this specific indication —
however, the completed trials report **negative efficacy results in liposarcoma specifically**, which is an important caveat to the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Metastatic colorectal cancer, GIST, hepatocellular carcinoma (drug not licensed in Norway; indication derived from literature, not from a market authorization record) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank-sourced mechanism-of-action text is not available for this candidate. Based on the repurposing rationale supplied with this evidence pack, regorafenib is a multi-kinase inhibitor acting on VEGFR1–3, PDGFR-β, FGFR1, KIT, RET, and RAF, giving it combined anti-angiogenic and anti-proliferative activity. Liposarcoma, particularly the dedifferentiated subtype, is highly vascular-dependent, and activation of the RAS/RAF/MEK and VEGF signaling pathways is a recognized driver of its pathogenesis — providing a plausible mechanistic overlap with regorafenib's target profile, which is the basis for the TxGNN score.

However, this mechanistic plausibility is **not confirmed by clinical outcomes**. The two identified trials specifically evaluated liposarcoma as a pre-defined cohort within broader soft-tissue-sarcoma studies, and both report **discordant, negative findings for liposarcoma**: the REGOSARC trial found regorafenib effective in leiomyosarcoma, synovial sarcoma, and other non-adipocytic sarcomas, but explicitly **not** in liposarcoma; the SARC024 liposarcoma cohort (a dedicated randomized Phase 2 trial vs. placebo) concluded that results "do not support the routine use of regorafenib in this patient population." This means the high TxGNN score and the mechanistic rationale point in a different direction than the actual completed clinical evidence — a discrepancy that should be weighted heavily in any decision-making.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01900743](https://clinicaltrials.gov/study/NCT01900743) | Phase 2 | Completed | 219 | REGOSARC: randomized, placebo-controlled trial across 5 STS cohorts (including liposarcoma); reported efficacy in non-adipocytic sarcoma subtypes but not in liposarcoma |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024: multi-cohort trial of oral regorafenib in selected sarcoma subtypes, including a dedicated liposarcoma arm |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | Lancet Oncol | REGOSARC primary results: regorafenib improved PFS in doxorubicin-refractory STS |
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarcoma cohort: results do **not** support routine use of regorafenib in refractory liposarcoma |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | Eur J Cancer | REGOSARC updated/cross-over analysis: efficacy confirmed in non-adipocytic sarcoma, **not** in liposarcoma |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Trial Protocol | BMC Cancer | Study protocol for REGOSARC, rationale based on angiogenesis signaling in sarcoma biology |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | RCT (secondary analysis) | Cancer | Q-TWiST analysis of REGOSARC quantifying quality-adjusted clinical benefit |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Review | Targeted Oncology | Review of regorafenib's growing role across STS subtypes including liposarcoma |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Review | Crit Rev Oncol Hematol | Review of maintenance therapy strategies in advanced STS after first-line chemotherapy |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospective study (different drug, anlotinib) | Anti-Cancer Drugs | Indirect reference; notes regorafenib/pazopanib approved for non-adipocytic STS, anlotinib studied in liposarcoma |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Case report (different drug, pazopanib) | Rare Tumors | Indirect reference citing SARC024 rationale for adding sarcoma arms including liposarcoma |

## Norway Market Information

Regorafenib currently has no marketing authorization in Norway (0 licenses on record); no product/dosage-form data is available for this jurisdiction.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (oral multi-kinase inhibitor: VEGFR1-3, PDGFR-β, FGFR1, KIT, RET, RAF) |
| Myelosuppression Risk | Low — dose-limiting toxicities reported in the literature are predominantly non-hematologic (hand-foot skin reaction, hypertension, hepatotoxicity, proteinuria) rather than bone marrow suppression |
| Emetogenicity Classification | Low, consistent with oral TKI class |
| Monitoring Items | Liver function tests, blood pressure, urinalysis (proteinuria), skin/dermatologic exam (hand-foot skin reaction), CBC |
| Handling Protection | Oral targeted agent; standard oral-oncolytic handling precautions apply (avoid crushing/splitting, use gloves when handling); does not require IV-cytotoxic handling protocols, but institutional oral-chemotherapy policy should still be followed |

## Safety Considerations

Please refer to the package insert for safety information. TFDA/Norway-specific warnings, contraindications, and drug-interaction data were not retrievable at this data cutoff (flagged as a Blocking data gap — see Conclusion).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L2 is met on trial-count grounds (two completed Phase 2 RCTs with dedicated liposarcoma cohorts), and the mechanistic rationale (VEGF/PDGFR-driven angiogenesis in liposarcoma) is plausible. However, both trials report that regorafenib specifically **failed to demonstrate efficacy in liposarcoma**, in contrast to its activity in other soft-tissue sarcoma subtypes. This directional conflict between the TxGNN prediction and the actual clinical trial outcomes means "guardrails" should include an explicit efficacy caveat, not just a general safety caveat.

**To proceed, the following is needed:**
- TFDA/Norway product-label warnings and contraindications (currently a Blocking data gap)
- Confirmed drug-interaction profile (DDI query returned no data)
- Formal DrugBank-sourced mechanism-of-action and toxicity data to replace the current rationale-derived summary
- A structured re-assessment of whether "liposarcoma" as a monotherapy target should be downgraded to Hold, given that both completed trials in this exact indication were negative — combination-therapy or biomarker-selected subpopulation approaches would need separate justification before any development decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

