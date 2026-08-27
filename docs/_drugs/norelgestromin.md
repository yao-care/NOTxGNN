---
layout: default
title: Norelgestromin
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 1
---

# Norelgestromin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Norelgestromin: From Contraception to Amenorrhea

## One-Sentence Summary

> Norelgestromin is the active metabolite of norgestimate and is used as a progestin component in combined hormonal contraceptive products (e.g., transdermal patch); no confirmed original indication or mechanism-of-action record is available in this dataset.
> The TxGNN model predicts it may be effective for **Amenorrhea**, based purely on a computational prediction score, with **no supporting clinical trials or literature** currently identified.
> Given the absence of any real-world evidence and outstanding safety data gaps, this candidate is at the earliest and weakest stage of evaluation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from regulatory data (drug not marketed in Norway; no license records). Based on general pharmacological knowledge, norelgestromin is used for contraception as part of combined hormonal contraceptive patches. |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% (rank 5435) |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset (`original_moa`: [Data Gap]), and no original indication records exist either. Based on general pharmacological knowledge, norelgestromin is the active metabolite of norgestimate and belongs to the progestin class, most commonly known as a component of combined hormonal contraceptive transdermal patches.

Progestin-class drugs are pharmacologically known to suppress ovulation and thin the endometrial lining — mechanisms that, as a class effect, can lead to amenorrhea or menstrual suppression. This is a well-established pharmacological property of progestins in general, not a finding specific to norelgestromin.

However, because this dataset provides no confirmed original indication and no verified MOA source, the mechanistic link between norelgestromin and amenorrhea described above should be treated strictly as a **theoretical, class-level inference**. It cannot be used as supporting evidence for the evidence-level determination, which is why this candidate remains at L5 (model prediction only).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Norway Market Information

Norelgestromin is not currently marketed in Norway, and no marketing authorizations are on record (`total_licenses`: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported only by the TxGNN model score (L5, no clinical trials, no literature), and a **Blocking**-severity data gap (TFDA/package-insert warnings and contraindications, DG001) means this candidate cannot yet pass the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- Confirmed original indication and mechanism-of-action (MOA) data for norelgestromin (currently marked High-severity data gap, DG002)
- Official package insert / label warnings and contraindications (Blocking data gap, DG001) to enable S1 safety evaluation
- Drug-drug interaction (DDI) data (currently not found)
- Generation or identification of preclinical/mechanistic or clinical evidence specific to amenorrhea before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

