---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fenofibrate: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Fenofibrate is a PPARα agonist traditionally used to manage hypertriglyceridemia and mixed hyperlipidemia (dyslipidemia).
> The TxGNN model predicts it may also be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
> but this direction is currently supported by only **1 indirectly relevant clinical trial** (testing a different drug in the same disease population) and **11 publications**, none of which are direct fenofibrate RCTs in HoFH.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyslipidemia (hypertriglyceridemia / mixed hyperlipoproteinemia) — inferred from supporting literature; no formal Norway label text available |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fenofibrate is a fibrate-class **PPARα agonist**, and its efficacy in dyslipidemia (hypertriglyceridemia, mixed hyperlipoproteinemia) has been proven; mechanistically, this profile is being evaluated for potential relevance to homozygous familial hypercholesterolemia.

Dyslipidemia and HoFH both fall under disorders of lipid metabolism, which is likely why the TxGNN model linked them. However, the pathophysiology differs substantially: HoFH results from a near-complete loss of LDL receptor (LDLR) function, whereas fenofibrate's core action — increasing lipoprotein lipase (LPL) activity and lowering ApoC-III — primarily reduces triglycerides and modestly raises HDL, with only limited effect on LDL-C.

Because HoFH patients require LDLR-independent treatment strategies (PCSK9 monoclonal antibodies, lomitapide, LDL apheresis), fenofibrate's mechanism has weak evidence for meaningful LDL-C reduction in this specific population. It may still have a role as adjunctive triglyceride control, but not as a core therapy — which is consistent with the model's own generated rationale for this candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated **alirocumab** (a PCSK9 inhibitor, not fenofibrate) in children/adolescents with HoFH on LDL-C reduction over 12–48 weeks. Only the disease population overlaps; this is not direct evidence for fenofibrate. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Small trial | Pharmacological Research Communications | 22 type II hyperlipoproteinemia patients treated with fenofibrate 300 mg/day; one patient with HoFH showed the greatest fall in total and LDL cholesterol among the cohort. |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Annals of the New York Academy of Sciences | Reviews pharmacologic/surgical treatments for dyslipidemic children, noting fenofibrate among agents with variable success in familial hypercholesterolemia. |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | Review/PK | Pharmacotherapy | PK interaction study of lomitapide (an approved HoFH drug) with commonly co-used lipid-lowering agents including fenofibrate. |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | Reviews liver transplantation for HoFH and notes emerging lipid-lowering drug alternatives to LDL-apheresis. |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | States fenofibrate's most definite monotherapy indication is severe hypertriglyceridemia (>500 mg/dL) to prevent pancreatitis; modest cardiovascular benefit noted. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Review/Guideline | Endocrine Practice | AACE/ACE clinical practice guideline for dyslipidemia management and cardiovascular disease prevention. |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews LDL-C reduction strategies including statins and PCSK9 inhibitors for severe hypercholesterolemia. |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Reviews ezetimibe as a selective cholesterol absorption inhibitor, contextualizing non-statin LDL-lowering options. |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Pharmacology and therapeutic potential of atorvastatin in hyperlipidemia management. |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Reviews dyslipidemia management in pregnancy; not specific to HoFH or fenofibrate. |

---

## Norway Market Information

Fenofibrate is currently **not marketed in Norway** (total authorizations: 0). No license records are available to summarize approved indications, dosage forms, or product names.

---

## Safety Considerations

Please refer to the package insert for safety information. (No key warnings, contraindications, or drug interaction data are currently available in the evidence pack — TFDA/label warning data is flagged as a blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for fenofibrate in HoFH is limited to preclinical/mechanistic-level data (L4) with no direct fenofibrate clinical trials in this population — the only registered trial evaluates a different drug (alirocumab) in the same disease group. Combined with fenofibrate's weak mechanistic fit for LDLR-independent disease and the drug's current non-marketed status in Norway, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TFDA/Norwegian label warnings and contraindications (currently a blocking data gap)
- Detailed mechanism of action (MOA) data from DrugBank
- At least one fenofibrate-specific clinical trial or controlled study in a HoFH population
- Formal Norway licensing/regulatory pathway assessment, since the drug is not yet marketed

**Note:** Within this evidence pack, **rank 2 — hyperlipoproteinemia** — has substantially stronger support (L1 evidence, multiple completed Phase 3 RCTs, recommendation: *Proceed with Guardrails*) and may warrant separate evaluation as a more viable repurposing candidate for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

