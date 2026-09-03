---
layout: default
title: Febuxostat
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 3
---

# Febuxostat
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

# Febuxostat: From Hyperuricemia (Gout) to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor best known for treating chronic hyperuricemia in gout patients.
The TxGNN model predicts it may also be relevant to **renal hypouricemia** (a condition of *low* serum urate, often complicated by exercise-induced acute kidney injury),
with **1 clinical trial** and **2 publications** currently available as supporting evidence — none of which directly confirms efficacy in this new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the evidence pack (no Norway license records); febuxostat is publicly known as a xanthine oxidase inhibitor indicated for chronic hyperuricemia in gout |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate. Based on generally known pharmacology, febuxostat is a **non-purine selective xanthine oxidase inhibitor**, a drug class whose efficacy in reducing serum urate production has been well established in the treatment of chronic hyperuricemia and gout.

The predicted new indication, renal hypouricemia (RHUC), is mechanistically distinct — it is a condition of *low* urate caused by urate transporter (URAT1) defects, not high urate. The connection is not urate-lowering per se, but rather the antioxidant/renoprotective effect of xanthine oxidase inhibition: reducing reactive oxygen species generated during purine catabolism may help prevent **exercise-induced acute kidney injury (EIAKI)**, a known complication in RHUC patients. This is a mechanism-driven repurposing hypothesis rather than a direct extension of febuxostat's approved urate-lowering effect, and it is supported by only a single published case report at this time.

Because the original indication and MOA fields are both marked as data gaps in this evidence pack, this rationale should be treated as provisional pending confirmation from primary regulatory/DrugBank sources.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study on uric acid control, stone recurrence, and renal function in patients with hyperuricemia-related calculi (Shanghai Xu-hui Central Hospital, Dept. of Urology). Note: this trial concerns *hyperuricemia*, not renal hypouricemia — relevance to the predicted indication is uncertain and marked "pending" review. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Case Report | Internal Medicine (Tokyo) | 16-year-old athlete with familial renal hypouricemia (URAT1 compound heterozygous mutation) and recurrent exercise-induced AKI; febuxostat proposed as prophylaxis via xanthine oxidoreductase inhibition when hydration alone failed. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia etiology and clinical management for rheumatologists; general background, not febuxostat-specific. |

---

## Norway Market Information

Febuxostat currently holds **no marketing authorization in Norway** (0 licenses on record); the evidence pack lists market status as "not marketed." No authorization or product data is available for this section.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data are not currently available in this evidence pack (flagged as a **Blocking** data gap — DG001), so this candidate cannot yet proceed to safety pre-assessment (S1).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic hypothesis is plausible but supported by only a single case report and one clinical trial of uncertain relevance (no completed RCT specific to renal hypouricemia). Combined with a **blocking safety data gap** (no TFDA/Norway label warnings or contraindications available) and the drug's non-marketed status in Norway, the evidence does not yet support advancement.

**To proceed, the following is needed:**
- TFDA/Norway package insert (warnings, contraindications) to clear the blocking safety gap (DG001)
- Confirmed mechanism of action and original approved indication from DrugBank (DG002)
- Additional case series or a dedicated clinical trial evaluating febuxostat specifically for EIAKI prevention in renal hypouricemia patients
- Re-review of NCT04398251 relevance, since its population (hyperuricemia/urolithiasis) does not clearly match the predicted indication (renal hypouricemia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

