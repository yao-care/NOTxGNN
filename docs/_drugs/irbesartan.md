---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB); the detailed approved indication text is not available in this dataset. The TxGNN model predicts potential efficacy for **Malignant Renovascular Hypertension**, but this prediction is currently supported by **no clinical trials and no literature** — it rests solely on mechanistic plausibility (RAAS pathway blockade).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in dataset (no drug license or indication text available; Irbesartan is a known ARB commonly used for hypertension) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 (mechanism-based, no clinical/literature support) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this candidate is not available in the dataset (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, Irbesartan belongs to the angiotensin II receptor blocker (ARB) class, which blocks the AT1 receptor to suppress RAAS-driven vasoconstriction — a pathway central to the pathophysiology of renovascular hypertension (renal artery stenosis → increased renin release → systemic hypertension).

Mechanistically, this explains why TxGNN assigns a high prediction score: ARB pharmacology is conceptually aligned with the pathophysiology of malignant renovascular hypertension. However, this is an important caution rather than pure support — ARBs and ACE inhibitors carry a well-established risk of inducing acute kidney injury in patients with bilateral renal artery stenosis or stenosis of a solitary functioning kidney, which is precisely the population this indication targets. The prediction should therefore be treated as a mechanistic hypothesis requiring careful safety evaluation, not as validated efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

*(Note: the evidence pack does contain 20 literature entries under a lower-ranked, lower-confidence candidate indication — "pulmonary hypertension owing to lung disease and/or hypoxia" — but none of those articles mention Irbesartan or ARBs; they are general hypoxia/oncology biology papers and do not constitute supporting evidence for that indication either.)*

## Norway Market Information

Irbesartan is currently **not marketed** in Norway per this dataset — no drug licenses were found (`total_licenses: 0`).

## Safety Considerations

Detailed safety data (key warnings, contraindications, drug interactions) is not available in this dataset. This is flagged as a **Blocking**-severity data gap (DG001 — TFDA/regulatory package insert warnings and contraindications), meaning this candidate cannot proceed to formal safety evaluation (S1) until the official prescribing information is retrieved.

Please refer to the official package insert for complete safety information once available. Given the known class-effect risk of ARBs in renal artery stenosis (potential acute kidney injury), renal function and safety data should be prioritized before any further evaluation of this specific indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 — the prediction is supported only by class-level mechanistic reasoning, with zero clinical trials or literature directly addressing Irbesartan in malignant renovascular hypertension. The drug is not currently marketed in Norway, and a Blocking safety data gap (missing package insert warnings/contraindications) prevents progression to formal safety review. There is also a known class-risk (AKI in renal artery stenosis) that directly conflicts with the target population, warranting caution rather than advancement.

**To proceed, the following is needed:**
- Official prescribing information (TFDA or equivalent) for warnings and contraindications (resolves blocking gap DG001)
- Detailed mechanism of action data from DrugBank (resolves DG002)
- Targeted literature/trial search specifically for ARB use in renovascular or malignant hypertension (current literature set is unrelated)
- Renal function monitoring protocol given the known AKI risk of ARBs in bilateral/solitary-kidney renal artery stenosis
- Reassessment of Norway market entry status before considering repurposing pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

