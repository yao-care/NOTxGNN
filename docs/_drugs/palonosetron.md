---
layout: default
title: Palonosetron
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 5
---

# Palonosetron
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using no specific skill — this is a direct report-drafting task per the fixed template in the prompt, not a coding/debugging workflow.

# Palonosetron: From Chemotherapy-Induced Nausea and Vomiting to Migraine Disorder

## One-Sentence Summary

Palonosetron is a 5-HT3 receptor antagonist used to prevent chemotherapy-induced nausea and vomiting (CINV). The TxGNN model predicts it may be effective for **Migraine Disorder**, but the only supporting literature (a single case report) actually describes palonosetron **inducing** migraine-type headache as an adverse effect — not treating it. No clinical trials support this or any of the other four predicted indications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV) prevention — general pharmacological knowledge; not confirmed via Norway regulatory data (drug not marketed in Norway) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 (model prediction only; sole literature hit is contradictory) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (DG002). Based on general pharmacological knowledge, palonosetron is a highly selective 5-HT3 receptor antagonist, and its efficacy in preventing CINV is well established. It acts on peripheral and central 5-HT3 receptors involved in the emetic reflex.

Migraine pathophysiology, however, is primarily mediated by 5-HT1B/1D and 5-HT1F receptors (the targets of triptans and ditans), not 5-HT3 receptors. There is no established pharmacological rationale linking 5-HT3 antagonism to migraine prevention or treatment.

More importantly, the only literature evidence retrieved for this indication (PMID 21132477, "Palonosetron-induced migraine-type headache") documents the **opposite** relationship: a case report of palonosetron **causing** a migraine-type headache as an adverse drug reaction, not resolving one. This is a contradictory signal that actively argues against the TxGNN prediction rather than supporting it. Given the lack of mechanistic plausibility and the directionally opposite evidence, this candidate should not advance without independent confirmatory data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21132477](https://pubmed.ncbi.nlm.nih.gov/21132477/) | 2011 | Case Report (Adverse Event) | Canadian Journal of Anaesthesia | Reports palonosetron **inducing** migraine-type headache — an adverse event, not evidence of therapeutic benefit for migraine |

---

## Norway Market Information

Palonosetron is not currently marketed in Norway (0 authorizations). No product/license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. TFDA/manufacturer label warnings and contraindications for palonosetron are not yet available in this dataset (DG001 — Blocking gap).

---

## Other Predicted Indications (Screened Out)

Four additional TxGNN-predicted indications were reviewed and are not recommended for further evaluation due to absence of any supporting evidence:

| Rank | Disease | TxGNN Score | Evidence | Assessment |
|------|---------|-------------|----------|------------|
| 2 | Migraine with brainstem aura | 99.67% | None | No mechanistic link (5-HT3 vs. 5-HT1/2 pathways) |
| 3 | Migraine susceptibility | 99.44% | 20 papers, all on epilepsy/migraine genetic comorbidity | None mention palonosetron; genetic susceptibility literature, not drug evidence |
| 4 | Atrophoderma vermiculata | 99.13% | None | Rare keratinizing skin disorder; no biological plausibility |
| 5 | Ulerythema ophryogenesis | 99.07% | None | Same disease spectrum as #4; no biological plausibility |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (migraine disorder) is supported only by a case report describing the drug **causing** migraine-type headache, which contradicts rather than supports repurposing. All other predicted indications have zero clinical trial or literature support, and no coherent mechanistic rationale connects a 5-HT3 antagonist to these conditions.

**To proceed, the following is needed:**
- TFDA/manufacturer package insert data (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action from DrugBank (DG002)
- Independent literature or preclinical evidence showing a *therapeutic* (not adverse) effect of palonosetron on migraine before any further evaluation stage is initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

