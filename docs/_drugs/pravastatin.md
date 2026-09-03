---
layout: default
title: Pravastatin
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 9
---

# Pravastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pravastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Pravastatin is a HMG-CoA reductase inhibitor (statin) established for treating hypercholesterolemia and reducing cardiovascular risk.
> The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
> but the supporting evidence — **1 clinical trial** (not testing pravastatin itself) and **13 publications** (mostly on other statins or general FH context) — is indirect and does not yet establish efficacy of pravastatin alone in this population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this Evidence Pack (`taiwan_regulatory.licenses` is empty); pravastatin is generally indicated for hypercholesterolemia/dyslipidemia |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L3 (indirect/observational evidence only; no direct RCT of pravastatin in HoFH) |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, pravastatin is a HMG-CoA reductase inhibitor that lowers hepatic cholesterol synthesis and is used to manage hypercholesterolemia and reduce cardiovascular risk.

HoFH is characterized by near-complete absence of functional LDL receptors, which is mechanistically the pathway statins primarily rely on to lower LDL-C. This creates an important caveat: as noted in the repurposing rationale, statins have **limited standalone efficacy** in HoFH and are typically used only as background/adjunct therapy alongside PCSK9 inhibitors, ezetimibe, or LDL apheresis — not as monotherapy.

The single clinical trial identified (NCT03510715) actually tests alirocumab, not pravastatin, in pediatric HoFH, and is graded "C" relevance — useful only as disease-background context. The literature base is similarly indirect, consisting largely of reviews/guidelines on other statins (rosuvastatin, atorvastatin), ezetimibe, and general statin-in-FH systematic reviews, rather than pravastatin-specific HoFH data. The prediction is therefore mechanistically plausible as an adjunct but not well supported as a primary therapy signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (not pravastatin) in children/adolescents with HoFH on top of background lipid-lowering therapy; relevant only as HoFH population/background-treatment context, not direct evidence for pravastatin. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic Review | Cochrane Database Syst Rev | Statins (including pravastatin) in children with FH; largely covers heterozygous FH, notes HoFH as the severe end of the spectrum. |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocr Pract | AACE/ACE dyslipidemia management guideline; statins positioned as foundational therapy across FH severity. |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic Review | Cochrane Database Syst Rev | Earlier version of the statins-in-FH-children Cochrane review. |
| [31358055](https://pubmed.ncbi.nlm.nih.gov/31358055/) | 2019 | Preclinical | Stem Cell Res Ther | iPSC-derived LDLR-deficient hepatocyte model for FH; supports disease mechanism, not direct pravastatin efficacy. |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | Rosuvastatin review noting HoFH as a treatment indication for statins as a class. |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin review; reports rosuvastatin outperformed pravastatin on lipid profile in comparative trials. |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Review | Ann Pharmacother | Atorvastatin review (comparator statin, not pravastatin-specific). |
| [14727947](https://pubmed.ncbi.nlm.nih.gov/14727947/) | 2003 | Review | Am J Cardiovasc Drugs | Ezetimibe review; relevant as a common combination partner with statins in severe FH. |

---

## Norway Market Information

No marketing authorizations were found for pravastatin in the Norwegian register — consistent with the reported "Not marketed" status and 0 total licenses in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all marked as gaps in this Evidence Pack; DG001 flags the missing TFDA label as a Blocking gap that prevents a full S1 safety pre-assessment.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence for pravastatin specifically in HoFH is indirect (the only trial tests a different drug, alirocumab) and the mechanistic rationale itself flags limited standalone efficacy in HoFH due to near-absent LDL receptor function. Combined with a Blocking data gap on TFDA label safety information (DG001), the candidate is not ready to advance.

**To proceed, the following is needed:**
- TFDA label PDF (warnings/contraindications) to clear the Blocking gap (DG001) and enable S1 safety review
- DrugBank MOA data to confirm mechanistic rationale (DG002)
- Direct clinical evidence on pravastatin (alone or as background therapy) specifically in confirmed HoFH patients
- Clarification of intended use case: adjunct/background therapy alongside PCSK9i/ezetimibe/apheresis, rather than monotherapy positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

