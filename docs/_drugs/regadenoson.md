---
layout: default
title: Regadenoson
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 4
---

# Regadenoson
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the drug-repurposing evaluation report format to produce the requested report.

# Regadenoson: From Pharmacologic Cardiac Stress Agent to Anaphylaxis (Likely Artifact)

## One-Sentence Summary

Regadenoson is an adenosine A2A receptor agonist used internationally as a pharmacologic stress agent for cardiac perfusion imaging; no Taiwan/Norway-approved indication or MOA record is currently on file.
The TxGNN model's top prediction is **Anaphylaxis**, but this signal is most plausibly a reverse-causality artifact — anaphylactoid/hypersensitivity reaction is a known **adverse effect** of regadenoson, not a treatment target.
Evidence support is minimal: **1 clinical trial (graded irrelevant, "C")** and **0 supporting publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (drug not licensed in Taiwan/Norway; internationally used as a pharmacologic cardiac stress-testing agent) |
| Predicted New Indication | Anaphylaxis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 (model prediction only, no supportive real-world evidence) |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap). Based on available evidence, regadenoson is an adenosine A2A receptor agonist. In the one identified clinical trial context, it is used as a pharmacologic stress agent to simulate exercise-induced cardiac blood flow changes during MRI/perfusion imaging — not as a disease-modifying therapeutic.

Critically, the repurposing rationale provided in the evidence pack itself flags that hypersensitivity/anaphylactoid reactions are a **known, labeled adverse effect** of regadenoson. This means the TxGNN prediction linking regadenoson to "anaphylaxis" most likely reflects a *drug-causes-adverse-event* relationship embedded in the knowledge graph, rather than a *drug-treats-disease* relationship. This is a well-recognized failure mode for embedding-based prediction models (reverse causality / polarity confusion) and should not be interpreted as a genuine treatment signal.

The remaining three candidates (food-dependent exercise-induced anaphylaxis, esotropia, pseudoallergy) show no identifiable mechanistic link to A2A receptor pharmacology, and pseudoallergy has the same reverse-causality concern as the top prediction. None of the four candidates are supported by clinical trials or literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | N/A | Recruiting | 1000 | Multicenter stress cardiac MRI perfusion imaging study; regadenoson used as a pharmacologic stress agent to assess coronary blood flow. Not designed to treat anaphylaxis — any anaphylaxis events would be safety monitoring endpoints, not efficacy endpoints. **Relevance grade: C (does not support the predicted indication).** |

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Regadenoson currently has no marketing authorization on file (0 licenses; market status: Not marketed). No product table can be generated.

---

## Safety Considerations

- **Key Warnings**: Not available in structured safety data (Data Gap). Note, however, that the repurposing rationale explicitly identifies hypersensitivity/anaphylactoid reaction as a known labeled risk of regadenoson — this is directly relevant to interpreting the top-ranked prediction and should be treated as a safety signal, not a treatment opportunity.
- **Drug Interactions**: Query returned no results (not found).

Please refer to the package insert for complete safety information once available (see Data Gap DG001, currently marked Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications are Evidence Level L5 (model prediction only), with either irrelevant (Grade C) or no clinical trial support and zero supporting literature. The top-ranked candidate, anaphylaxis, is very likely a reverse-causality artifact reflecting a known adverse drug reaction rather than a genuine therapeutic relationship, and the drug is not currently marketed in Norway or Taiwan.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official label warnings/contraindications from TFDA before any safety pre-screening can begin
- Resolve DG002 (High): confirm mechanism of action via DrugBank to properly evaluate mechanistic plausibility
- Independent verification of TxGNN edge polarity (treats vs. causes) for the anaphylaxis prediction before further investment
- If pursued, seek prospective clinical or case-report evidence specifically evaluating a therapeutic (not adverse) relationship between regadenoson and any of the four candidate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

