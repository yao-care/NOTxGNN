---
layout: default
title: Corifollitropin Alfa
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 8
---

# Corifollitropin Alfa
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

Using no additional skill — this is a direct report-generation task following the supplied template; I'll produce the Markdown report from the evidence pack as instructed.

# Corifollitropin Alfa: From Ovulation Induction (IVF) to Gastroduodenitis

## One-Sentence Summary

Corifollitropin alfa is a long-acting FSH receptor agonist used for controlled ovarian stimulation in IVF (per mechanistic notes in this evidence pack; not formally coded in the structured indication fields). The TxGNN model predicts a possible association with **Gastroduodenitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-relatedness score with no biological or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in structured regulatory data; known pharmacological use is ovulation induction/controlled ovarian stimulation (IVF), per rationale notes in this evidence pack |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on the limited information present in this evidence pack, corifollitropin alfa is understood to be a long-acting FSH receptor agonist used for ovulation induction in assisted reproductive technology. According to the evidence pack's own mechanistic assessment, there is **no known biological pathway** connecting FSH receptor agonism to gastroduodenitis, or to any of the seven other candidate indications generated for this drug (migraine, peptic ulcer disease, migraine with brainstem aura, Raynaud disease, pulmonary hypertension, kyphoscoliotic heart disease, and migraine susceptibility).

Notably, the rationale for one lower-ranked candidate (pulmonary hypertension) explicitly flags that corifollitropin's known adverse-effect profile — OHSS-related thrombotic risk from ovarian stimulation — runs *counter* to that indication direction, i.e., it is a safety signal rather than a therapeutic opportunity. For the eighth-ranked candidate (migraine susceptibility), 20 literature records were retrieved, but on review they concern epilepsy genetics and neuroinflammation background biology, not corifollitropin or FSH-pathway pharmacology — they do not constitute repurposing evidence.

In summary, all eight TxGNN-predicted indications for this drug are graph-based relatedness scores (~99.4–99.7%) unaccompanied by mechanistic hypotheses, clinical trials, or relevant literature. This is a low-confidence signal set that should not be interpreted as a validated repurposing opportunity at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

This drug is not currently marketed in Norway (0 authorizations on file). No product license records are available in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/regulatory label warnings and contraindications are flagged as a Blocking data gap in this evidence pack — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or relevant literature support the top-ranked predicted indication (gastroduodenitis), and the evidence pack's own mechanistic analysis finds no biological link across all eight candidate indications. Combined with the absence of MOA data and Norway market presence, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a **Blocking** data gap preventing S1 safety screening
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Preclinical or mechanistic studies establishing a plausible pathway between FSH receptor agonism and any of the predicted GI, vascular, or neurological indications
- Re-evaluation once clinical trial registries (ClinicalTrials.gov/ICTRP) or PubMed return drug-specific (not disease-background) evidence for the target indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

