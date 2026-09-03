---
layout: default
title: Buprenorphine
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 6
---

# Buprenorphine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Buprenorphine: From Opioid Analgesia to Acute Intermittent Porphyria

## One-Sentence Summary

Buprenorphine is a partial μ-opioid receptor agonist generally used in pain management and opioid dependence treatment.
The TxGNN model predicts it may be relevant to **Acute Intermittent Porphyria (AIP)**,
but currently only **1 case report** supports this direction — and that report discusses safe anesthetic use in an AIP patient, not treatment efficacy for AIP itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in evidence pack (no Norway license records; buprenorphine is generally recognized as an opioid analgesic/opioid dependence treatment) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for buprenorphine in this evidence pack (data gap DG002, High severity). Based on generally known pharmacology, buprenorphine is a partial agonist at the μ-opioid receptor, and — unlike some other analgesics — is not considered a potent inducer of hepatic ALA synthase or CYP450 enzymes, the pathway central to porphyric crisis provocation.

The single supporting publication (PMID 8301837, 1993 case report) describes the anesthetic management of an AIP patient undergoing surgery, in which buprenorphine was selected specifically because it was judged **safe to use** in AIP without triggering a crisis. This is important to clarify: the evidence documents that buprenorphine can be safely administered to AIP patients for an unrelated purpose (surgical analgesia), not that buprenorphine treats or improves AIP itself. AIP is a metabolic disorder driven by heme biosynthesis pathway defects, and there is no established therapeutic mechanism by which opioid receptor agonism would address the underlying enzymatic deficiency.

The high TxGNN score most likely reflects a graph relationship of "safe co-occurrence" rather than a true "therapeutic-for" relationship. This distinction should be treated as a significant caveat when interpreting the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8301837](https://pubmed.ncbi.nlm.nih.gov/8301837/) | 1993 | Case Report | Masui (Japanese J Anesthesiology) | Describes safe anesthetic management of a patient with suspected/confirmed AIP undergoing gynecologic surgery; buprenorphine chosen as an analgesic not expected to provoke a porphyric crisis. Does **not** evaluate buprenorphine as AIP therapy. |

---

## Norway Market Information

Buprenorphine currently has **no marketing authorization records** in this evidence pack (market status: Not Marketed, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/label warnings, contraindications, and drug interaction data are currently unavailable (data gap DG001, **Blocking** severity) — this gap directly prevents completion of the initial safety screening (S1 stage) for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting literature is a single case report addressing anesthetic safety in an AIP patient — not therapeutic efficacy for AIP — and no clinical trials exist for this indication. Combined with a Blocking-severity safety data gap and the drug's unmarketed status in Norway, the evidence does not support progression past initial screening.

**To proceed, the following is needed:**
- TFDA/official label warnings and contraindications (resolves DG001, currently blocking)
- Drug mechanism of action detail from DrugBank (resolves DG002)
- A mechanistic or preclinical rationale connecting opioid receptor pharmacology to heme biosynthesis/porphyrin metabolism, if this indication is to be pursued further
- Clarification/re-labeling of the literature evidence as safety-context rather than efficacy-context, to avoid overstating the current evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

