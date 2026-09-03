---
layout: default
title: Enzalutamide
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 7
---

# Enzalutamide
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

# Enzalutamide: From Castration-Resistant Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is a second-generation androgen receptor (AR) antagonist whose established use is castration-resistant prostate cancer (CRPC); this specific role is described in the evidence pack's mechanistic rationale even though formal license/MOA fields are marked as data gaps.
The TxGNN model's top-ranked prediction for this drug is **prostate cancer/brain cancer susceptibility**, a genetic-susceptibility label rather than a defined disease entity.
Currently **0 clinical trials** and **0 publications** support this specific prediction, and the model itself flags the score as likely a knowledge-graph co-occurrence artifact rather than a genuine mechanistic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Castration-resistant prostate cancer (CRPC) — no Norway license text available; drug is a globally approved AR antagonist for this indication (per mechanistic rationale in evidence pack) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

The evidence pack's `original_moa` field is marked as a data gap, but the mechanistic rationale attached to other candidates in the same pack confirms enzalutamide's known pharmacology: it is a second-generation AR antagonist that blocks testosterone/DHT binding to the androgen receptor and inhibits AR nuclear translocation and DNA binding — the mechanism underlying its established use in CRPC.

The top-ranked new label, "prostate cancer/brain cancer susceptibility," is not a distinct disease with a plausible AR-driven pathophysiology. It appears to be a genetic-predisposition tag that combines two loosely related conditions. The evidence pack's own rationale explicitly states this: the high TxGNN score likely stems from the knowledge graph's "prostate cancer" node co-occurring with the "brain cancer" node, rather than reflecting any real biological link to enzalutamide's AR-blocking mechanism.

Because there is no independent AR-pathway evidence for brain cancer susceptibility, and no clinical or literature data support this pairing, the mechanistic case for repurposing toward this label is weak. It should be treated as model noise pending further validation, not as a genuine repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Norway Market Information

Enzalutamide is currently **not marketed** in Norway (0 authorizations); no license, dosage form, or approved-indication data are available for this market.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (androgen receptor signaling inhibitor) — not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/manufacturer warning and contraindication data are currently missing — flagged as a Blocking data gap that must be resolved before any safety pre-assessment can proceed.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction ("prostate cancer/brain cancer susceptibility") has no supporting clinical trials or literature (Evidence Level L5), and its own mechanistic rationale identifies the score as a likely knowledge-graph artifact rather than a real AR-pathway-driven signal.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a Blocking data gap
- Formal MOA documentation from DrugBank — currently a High-severity data gap
- Independent preclinical or clinical evidence linking AR antagonism to brain cancer susceptibility, if this candidate is to be pursued further
- Consider re-scoping evaluation toward better-evidenced candidates already present in this dataset, e.g. "benign reproductive system neoplasm" (L4, Research Question) or the drug's own core CRPC indication (L1, though not a novel repurposing case)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

