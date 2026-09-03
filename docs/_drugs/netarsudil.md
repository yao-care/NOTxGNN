---
layout: default
title: Netarsudil
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 2
---

# Netarsudil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Netarsudil: From Unspecified Original Indication to Primary Hereditary Glaucoma

## One-Sentence Summary

> Netarsudil's original approved indication is not recorded in the current regulatory dataset (data gap), though supporting evidence in this Evidence Pack indicates it is an already-marketed Rho-kinase (ROCK) inhibitor used for intraocular pressure control.
> The TxGNN model additionally predicts potential efficacy for **Primary Hereditary Glaucoma**,
> but this specific genetic subtype is currently supported by only **1 indirectly related clinical trial** and **0 dedicated publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in current dataset (data gap — `original_indications` is empty and `original_moa` is marked as a data gap; see note below) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

**Note on Original Indication:** The Evidence Pack's own analysis of a related, higher-ranked prediction ("glaucoma", rank 2 in this pack) states that netarsudil's mechanism (ROCK inhibition lowering intraocular pressure) corresponds to its already-established approved use for open-angle glaucoma/ocular hypertension — the empty `original_indications` field is flagged internally as a data gap rather than evidence that no approved use exists. This should be confirmed against a primary regulatory source before use in decision-making.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the `drug.original_moa` field (marked as a data gap). However, the evidence pack's repurposing rationale describes netarsudil as a selective **Rho-kinase (ROCK) inhibitor** that also inhibits the norepinephrine transporter (NET). ROCK inhibition relaxes the cytoskeleton of trabecular meshwork and Schlemm's canal endothelial cells, reducing resistance to aqueous humor outflow and thereby lowering intraocular pressure (IOP) — a mechanism already well validated for glaucoma broadly.

Hereditary forms of glaucoma (e.g., primary congenital glaucoma, juvenile open-angle glaucoma, commonly associated with *MYOC*/*CYP1B1* mutations) share the same downstream pathology: abnormal trabecular meshwork structure/function leading to increased outflow resistance. Because ROCK inhibitors act directly on trabecular meshwork cytoskeleton and extracellular matrix rather than on the specific causative gene product, there is a plausible mechanistic rationale for genotype-independent efficacy in hereditary glaucoma.

That said, the only identified trial (NCT06969586) does **not** actually study primary hereditary glaucoma — it enrolls patients with **Fuchs Endothelial Corneal Dystrophy (FECD)**, a distinct corneal endothelial disease, and evaluates corneal cell protection after cataract surgery rather than IOP control in genetically defined glaucoma. The two conditions only share the common thread of "ROCK inhibitor activity in anterior segment tissue." Direct clinical evidence for this specific predicted indication is therefore essentially absent, and the mechanistic bridge remains a hypothesis rather than a demonstrated effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06969586](https://clinicaltrials.gov/study/NCT06969586) | N/A | Enrolling by Invitation | 50 | Evaluates whether topical ROCK inhibitors reduce corneal endothelial cell loss after cataract surgery in patients with glaucoma and Fuchs Endothelial Corneal Dystrophy (FECD). Relevance graded **C**: the study population is FECD patients, not primary hereditary glaucoma patients — it is an indirect, mechanism-sharing signal rather than direct evidence for this indication. |

---

## Literature Evidence

Currently no related literature available.

---

## Norway Market Information

No marketing authorizations are on record for netarsudil in Norway (`total_licenses`: 0; market status: Not Marketed). No product/dosage-form/indication data can be extracted at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this Evidence Pack. Notably, TFDA-equivalent package-insert warnings/contraindications are flagged internally as a **Blocking** severity data gap, meaning a formal safety pre-screen (S1) cannot currently be completed for this drug.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence specific to primary hereditary glaucoma is limited to a single ongoing trial that actually studies a different corneal condition (FECD), graded only as indirectly relevant (Grade C), placing this indication at Evidence Level L4 / Decision Stage S1 ("Research Question"). Combined with a blocking data gap on safety warnings/contraindications and the drug's undetermined regulatory status in Norway (0 authorizations, not marketed), there is currently insufficient direct evidence or regulatory groundwork to proceed further.

**To proceed, the following is needed:**
- Resolution of the blocking data gap (DG001): TFDA/regulatory package-insert warnings and contraindications, required before any safety pre-screen (S1) can be completed
- Confirmed mechanism-of-action documentation from DrugBank (DG002), to properly assess mechanistic plausibility for genetic glaucoma subtypes
- Clinical trials or literature studying netarsudil specifically in primary hereditary/genetic glaucoma populations (e.g., *MYOC*/*CYP1B1*-associated disease), rather than extrapolating from Fuchs corneal dystrophy studies
- Clarification of netarsudil's true original approved indication and regulatory status, given that a related prediction in this same Evidence Pack (glaucoma, broadly) indicates the drug may already be an approved IOP-lowering agent elsewhere — this should be verified against primary regulatory sources rather than left as an empty field
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

