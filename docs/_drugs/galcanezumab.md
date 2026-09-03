---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 3
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab is an anti-CGRP (calcitonin gene-related peptide) monoclonal antibody, known clinically for migraine prevention (original indication data not recorded in this evidence pack).
The TxGNN model predicts it may be effective for **Heparin Cofactor 2 Deficiency**,
but currently **no clinical trials** and **no publications** support this direction — the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in this evidence pack (original_indications is empty); known pharmacology indicates use as an anti-CGRP antibody for migraine prevention |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (MOA field is a data gap). Based on known pharmacology, galcanezumab is an anti-CGRP monoclonal antibody, and its efficacy in migraine prevention is well established through the trigeminovascular pain pathway.

However, the evidence pack's own mechanistic assessment is explicit that **no known biological link exists** between CGRP signaling and heparin cofactor II (a serine protease inhibitor that inhibits thrombin). CGRP acts on neurovascular pain transmission and vasodilation, whereas heparin cofactor II deficiency is a coagulation-related genetic condition — these two systems have no established pharmacological overlap.

This appears to be a case where the TxGNN model assigned a numerically high score without an underlying biological rationale (also reflected in the low prediction rank of 5461 out of the full candidate list). The model score alone is insufficient grounds for prioritizing this candidate; independent mechanistic or preclinical validation would be required before this prediction can be considered credible.

**Note:** Two other candidates were also predicted for this drug with similarly high scores but equally weak mechanistic support — *antithrombin deficiency type 2* (score 99.41%, rank 6213) and *factor 5 excess with spontaneous thrombosis* (score 99.41%, rank 6221). All three fall into the coagulation/hemostasis disease cluster, suggesting the model may be picking up a spurious pattern rather than a true CGRP–coagulation relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Galcanezumab is not marketed in Norway under this evidence pack (0 authorizations recorded); no license data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score, there is no clinical trial or literature evidence, and the mechanistic rationale explicitly identifies no known biological connection between CGRP signaling and heparin cofactor II function. The evidence level (L5) reflects model prediction only, which is insufficient to justify further development effort at this stage.

**To proceed, the following is needed:**
- Confirmed original indication and MOA data for galcanezumab (currently data gaps)
- TFDA/regulatory label warnings and contraindications (currently data gaps, marked Blocking severity)
- Independent mechanistic or preclinical evidence linking CGRP pathways to coagulation/hemostasis disorders
- Re-evaluation if any clinical trials or case reports emerge connecting anti-CGRP therapy to coagulation factor abnormalities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

