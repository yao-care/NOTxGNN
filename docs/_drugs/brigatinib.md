---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Brigatinib
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

# Brigatinib: From ALK-Positive NSCLC to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib is a second-generation ALK/ROS1 tyrosine kinase inhibitor whose established clinical use — evident throughout this evidence pack's own literature — is ALK-positive non-small cell lung cancer (NSCLC); this is not, however, captured in the structured `original_indications` field (data gap). The TxGNN model's **top-ranked** prediction is **Gingival Fibromatosis**, but this specific signal is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic annotation explicitly flags it as likely knowledge-graph embedding noise rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive NSCLC (inferred from literature within this pack; not captured in structured license data — see Data Gaps) |
| Predicted New Indication | Gingival Fibromatosis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the structured `original_moa` field (marked as a data gap). However, the evidence pack's own rationale text repeatedly identifies brigatinib as a **second-generation ALK/ROS1 tyrosine kinase inhibitor**, consistent with its known clinical role in ALK-positive NSCLC.

For the top-ranked prediction, **Gingival Fibromatosis**, no mechanistic link exists: this condition is driven by genes such as *SOS1* and *REST*, or by general fibroblast proliferation, and has no known relationship to ALK/ROS1 signaling. There are zero supporting clinical trials or publications. The evidence pack's own repurposing rationale explicitly concludes this high TxGNN score is likely embedding noise rather than a real signal — a conclusion this report endorses.

**Important context beyond rank 1:** of the 10 predictions in this batch, 7 (ranks 1–4, 6, 7, 9) have no supporting literature and are correctly scored L5/Hold. The remaining 3 (ranks 5, 8, 10) reach L4/"Research Question," but closer reading shows all three suffer from **disease-label mismatch** rather than direct support for the named indication:
- **Rank 5 ("lung benign neoplasm")** — the cited literature (ALTA-1L, NEJM 2018/2021) is actually about ALK+ *malignant* NSCLC, i.e., brigatinib's known approved use, not a new benign-tumor indication.
- **Rank 8 ("lung germ cell tumor")** — the literature concerns brigatinib activity in other rare ALK-fusion-positive tumors (neuroblastoma, pheochromocytoma, LCNEC), not germ cell tumors specifically; this is indirect, pan-tumor "basket" evidence only.
- **Rank 10 ("Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome")** — this is the most notable finding in the dataset. The actual literature (including a 2024 *NEJM* study, PMID 38904277) documents brigatinib activity in **NF2-related schwannomatosis**, an unrelated but real and mechanistically plausible candidate indication that has nothing to do with the syndrome named in this row. This appears to be a genuine repurposing signal mis-attached to the wrong disease label and would merit a dedicated, correctly-labeled evaluation.

None of this, however, supports the rank-1 candidate (Gingival Fibromatosis) that this report is formally evaluating.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

Brigatinib is not currently marketed in Norway. No authorizations are on file (`total_licenses: 0`).

---

## Cytotoxicity (Antineoplastic Drugs Only)

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/DMP label warnings and contraindications are flagged in this evidence pack as a **Blocking** data gap (DG001) — this drug cannot proceed to a S1 safety review until label data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Gingival Fibromatosis) has no clinical, literature, or mechanistic support and is assessed in the source data itself as likely model noise. Combined with the drug's unmarketed status in Norway and a blocking gap in label/safety data, there is no basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA/DMP label (warnings, contraindications) — Blocking gap (DG001)
- Confirmed mechanism-of-action data via DrugBank API — High priority gap (DG002)
- If pursuing further repurposing work on this drug, open a **separate, correctly-labeled evaluation for NF2-related schwannomatosis**, based on the genuine Phase 2 evidence (NEJM 2024) surfaced under the rank-10 entry — this is a materially stronger candidate than any indication currently ranked in this batch
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

