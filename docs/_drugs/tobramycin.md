---
layout: default
title: Tobramycin
parent: 僅模型預測 (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Tobramycin
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

# Tobramycin: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

> Tobramycin is an aminoglycoside antibiotic originally used to treat bacterial infections, particularly those caused by *Pseudomonas aeruginosa* and other Gram-negative organisms.
> The TxGNN model predicts it may be effective for **Exposure Keratitis**,
> with **2 clinical trials** and **7 publications** currently supporting this direction — though the evidence base is thin and largely indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (aminoglycoside antibiotic; no market-specific approved indication text is available for this jurisdiction) |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed regulatory mechanism-of-action documentation is not available. Based on known pharmacology, tobramycin is an aminoglycoside antibiotic that inhibits bacterial 30S ribosomal protein synthesis, producing bactericidal activity against *Pseudomonas aeruginosa* and other Gram-negative organisms, as well as some Gram-positive species.

Exposure keratitis arises when incomplete eyelid closure leads to corneal drying and epithelial breakdown, which creates a risk of secondary bacterial infection. Since the pathogens that commonly colonize an exposed, damaged corneal surface fall within tobramycin's established antibacterial spectrum, there is a plausible pharmacological rationale for using it in this setting.

However, this rationale is limited: tobramycin does not treat the underlying cause of exposure keratitis (dryness and mechanical epithelial damage from lagophthalmos). Its role would be adjunctive — preventing or treating secondary bacterial infection — rather than addressing the primary pathology, which is an important caveat when interpreting the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | Unknown | 170 | Studies platelet-rich fibrin (PRF) membrane across four ophthalmic conditions (macular hole, pterygium, corneal ulcer, post-trabeculectomy); not tobramycin-specific, only indirectly relevant |
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | Unknown | 40 | Compares treatment modalities for dendritic (herpetic) viral corneal ulcer; not specific to exposure keratitis or tobramycin |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | Case report | Oxford Medical Case Reports | Bacterial keratitis from multidrug-resistant *Shewanella algae* in a patient unable to close eyes voluntarily (lagophthalmos-related exposure) |
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | In vitro | Current Eye Research | Compares corneal epithelial cytotoxicity of tobramycin against neomycin, gentamicin, and amikacin |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | In vitro comparison | Nippon Ganka Gakkai Zasshi | Compares MIC and postantibiotic effect of antibiotic eyedrops, including tobramycin, against infectious keratitis isolates in Japan |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | Case report | Eye & Contact Lens | Bilateral MRSA keratitis following photorefractive keratectomy |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | *Bacillus cereus* keratitis associated with contact lens wear |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | Case series | Polish Journal of Veterinary Sciences | Seroprevalence and treatment outcomes of feline ocular toxoplasmosis; not directly relevant to human exposure keratitis |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | Case report | Yan Ke Xue Bao | Paracentral corneal dellen as a rare sign of Graves ophthalmopathy; unrelated to tobramycin use |

No study directly evaluates tobramycin for exposure keratitis; the literature consists of case reports and in vitro susceptibility data on related infectious keratitis.

---

## Norway Market Information

No authorization records are currently available — tobramycin is not marketed in this jurisdiction (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The two identified clinical trials have unknown status and are not specific to tobramycin or exposure keratitis, and the supporting literature is limited to case reports and in vitro studies. Critically, the mechanistic rationale itself acknowledges that tobramycin does not treat the underlying cause of exposure keratitis (lagophthalmos-related corneal drying/damage) — it can only address secondary bacterial infection, making this an adjunctive rather than primary indication.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently a blocking data gap for safety pre-assessment (DG001)
- Verified mechanism-of-action documentation from DrugBank or equivalent source (DG002)
- Prospective, controlled studies specifically evaluating topical tobramycin for exposure keratitis or its secondary infection prevention/treatment
- Clarification of whether the intended use case is prophylactic (preventing secondary infection) versus therapeutic (treating established infection) in exposure keratitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

