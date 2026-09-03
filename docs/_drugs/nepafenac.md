---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Ocular Inflammation (Established Use) to Eye Disease (Broad TxGNN Prediction)

## One-Sentence Summary

> Nepafenac is a topical ophthalmic NSAID with well-documented efficacy in preventing and treating inflammation and pain after cataract surgery, though it is not currently marketed in Norway.
> The TxGNN model's top prediction for this drug is the broad category **Eye Disease**,
> with over **40 clinical trials** and **20 publications** — largely reflecting its already-established ophthalmic anti-inflammatory use rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the regulatory record (no Norway licenses on file); extensively evidenced in clinical trial data as ocular inflammation and pain associated with cataract surgery |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack. Based on the clinical trial and literature evidence collected, nepafenac is a topical ophthalmic NSAID prodrug that, after ocular penetration, is converted to its active metabolite amfenac, which inhibits cyclooxygenase (COX-1/COX-2) and thereby reduces prostaglandin-mediated inflammation in ocular tissue.

Its efficacy in preventing and treating inflammation and pain after cataract surgery is extensively documented — over 40 registered trials and multiple completed Phase 3 RCTs (some with enrollment exceeding 2,000 subjects) consistently support this use, and a 2025 systematic review/meta-analysis (PMID 39936354) confirms its benefit in reducing macular swelling and improving visual outcomes post-cataract surgery.

The TxGNN prediction of "eye disease" is therefore mechanistically unsurprising: it largely reflects the drug's already-known anti-inflammatory activity across ocular conditions (cataract surgery inflammation, diabetic macular edema, laser iridotomy inflammation) rather than identifying a distinct, unmet new indication. Preclinical data further suggest an anti-angiogenic effect on retinal vasculature (PMID 19897019, PMID 17259381), which could extend applicability to diabetic retinopathy-related conditions, but this remains largely at the mechanistic/preclinical level for indications beyond post-surgical inflammation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Safety and efficacy of nepafenac 0.3% for prevention/treatment of ocular inflammation and pain after cataract extraction |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for post-cataract inflammation and pain |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% once-daily superior to vehicle in diabetic subjects post-cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Confirmatory Phase 3 replicate of NCT01853072 in diabetic post-cataract patients |
| [NCT03025945](https://clinicaltrials.gov/study/NCT03025945) | NA | Completed | 662 | Adjunctive nepafenac 0.3% vs placebo for pseudophakic cystoid macular edema prevention |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Bioequivalence of generic nepafenac 0.3% vs Ilevro for post-cataract pain/inflammation |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | Completed | 267 | Nepafenac 0.1% vs Acular LS for treatment of ocular inflammation after cataract surgery |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% vs placebo for prevention/treatment of post-cataract inflammation and pain in Chinese subjects |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | Completed | 227 | European study: nepafenac 0.1% vs ketorolac vs placebo for post-cataract inflammation/pain |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | Terminated | 175 | Nepafenac for macular edema incidence/severity reduction in diabetic retinopathy post-cataract surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review & Meta-analysis | Eur J Ophthalmol | Nepafenac reduces foveal thickness and improves visual outcomes when added to steroid regimen post-cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% comparable to prednisolone acetate for controlling inflammation after laser peripheral iridotomy |
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | Phase 3 RCT | J Cataract Refract Surg | Once-daily nepafenac 0.3% effective for prevention/treatment of post-cataract inflammation and pain |
| [24345317](https://pubmed.ncbi.nlm.nih.gov/24345317/) | 2014 | RCT | Am J Ophthalmol | Nepafenac 0.1% eye drops do not significantly raise intraocular pressure |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | RCT | J Cataract Refract Surg | Prophylactic nepafenac and ketorolac both superior to placebo in preventing post-phacoemulsification macular edema |
| [19040348](https://pubmed.ncbi.nlm.nih.gov/19040348/) | 2008 | RCT | J Ocul Pharmacol Ther | Dosing frequency comparison (QD/BID/TID) for nepafenac in post-cataract pain and inflammation |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | Comparative Clinical Study | Korean J Ophthalmol | Nepafenac 0.1% vs prednisolone acetate 1% for inflammation control after micro-incisional cataract surgery |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | Comparative Clinical Study | Acta Ophthalmol | Nepafenac vs preservative-free diclofenac for prevention of pseudophakic cystoid macular oedema |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Review of nepafenac's role, penetration, and safety profile in cataract surgery |
| [35025078](https://pubmed.ncbi.nlm.nih.gov/35025078/) | 2022 | Review | Drugs | Review of diagnostic and therapeutic agents (including NSAIDs) for non-infectious corneal injury |

---

## Norway Market Information

Nepafenac is currently **not marketed in Norway** (0 authorizations on file). No product license records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. No detailed warnings, contraindications, or drug interaction data are currently available in the evidence pack (flagged as a **Blocking** data gap — TFDA/label warnings — pending retrieval and parsing from the official product insert).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While clinical trial and literature evidence for nepafenac's anti-inflammatory ocular activity is strong (L1, multiple completed Phase 3 RCTs), the TxGNN-predicted indication ("eye disease") is non-specific and largely overlaps with the drug's already-established use rather than representing a novel repurposing opportunity. Combined with the absence of any Norway market presence and a blocking gap in safety/label data, a full go/no-go decision cannot yet be made.

**To proceed, the following is needed:**
- TFDA/product insert warnings and contraindications (Blocking gap, DG001)
- Confirmed mechanism of action documentation (DG002)
- Clarification of the specific eye disease sub-indication targeted by the TxGNN prediction (the current label is too broad for regulatory or clinical decision-making)
- Norway-specific regulatory pathway assessment, since the drug currently holds no local authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

