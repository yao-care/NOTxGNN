---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 3
---

# Esomeprazole
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

# Esomeprazole: From Acid-Related Disorders to Duodenogastric Reflux

## One-Sentence Summary

> Esomeprazole is a proton pump inhibitor (PPI), originally used for acid-related gastrointestinal disorders such as GERD, erosive esophagitis, and peptic ulcer disease.
> The TxGNN model predicts it may be effective for **Duodenogastric Reflux**,
> with **0 clinical trials** and **1 publication** currently supporting this direction — the evidence base remains preliminary.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acid-related GI disorders (GERD, erosive esophagitis, peptic ulcer disease, H. pylori eradication) — inferred from supporting literature; no Norway licence text available (drug not marketed) |
| Predicted New Indication | Duodenogastric Reflux |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L4 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known information, esomeprazole is the S-isomer of omeprazole and belongs to the proton pump inhibitor (PPI) class, which irreversibly inhibits the H⁺/K⁺-ATPase in gastric parietal cells to suppress acid secretion. Its efficacy in acid-related gastrointestinal disorders is well established.

Duodenogastric reflux (DGR) and the drug's original indications share overlapping anatomy and patient populations — both involve upper GI mucosal injury, and DGR frequently co-occurs with, or follows, conditions like GERD or post-gastric-surgery states where PPIs are already used. However, the mechanistic link is indirect: DGR is primarily driven by bile and pancreatic enzyme reflux, not gastric acid itself. Esomeprazole can only reduce the acidic component's synergistic damage to the mucosa when mixed with refluxate — it does not block the root cause of bile reflux. This makes the rationale plausible but partial, consistent with the L4 (mechanism-only) evidence level and "Hold" recommendation currently assigned.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | General review of PPI clinical use and pharmacokinetics (peptic ulcer, H. pylori, GERD, NSAID-induced GI lesions, Zollinger-Ellison syndrome); does not directly address duodenogastric reflux as a treatment target |

---

## Norway Market Information

Esomeprazole is currently **not marketed in Norway** (0 authorizations on record), so no local product/label information is available for this evaluation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for duodenogastric reflux specifically is limited to a single general PPI review article with no supporting clinical trials, and the mechanistic link is indirect (addresses only the acidic component of a predominantly bile-driven condition). This does not meet the bar to proceed.

**Note:** This evidence pack also scores esomeprazole against two related indications — duodenal obstruction (L5, no supporting data, mechanistically weak) and duodenal ulcer (L1, extensive trial and literature support). The duodenal ulcer signal is strong, but it reflects an already-established PPI/H. pylori-eradication indication rather than a genuinely novel repurposing use, so it does not change the Hold decision for the duodenogastric reflux candidate evaluated here.

**To proceed, the following is needed:**
- TFDA/Norway package insert warnings and contraindications (blocking data gap, DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Dedicated clinical evidence (preclinical or clinical) evaluating esomeprazole specifically for duodenogastric reflux, ideally with bile-reflux–relevant endpoints
- Route of administration compatibility assessment for the new indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

