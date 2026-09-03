---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 6
---

# Certolizumab Pegol
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

# Certolizumab Pegol: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

> Certolizumab pegol is a PEGylated anti-TNF-α Fab fragment established for rheumatoid arthritis, axial spondyloarthritis, psoriatic arthritis, and Crohn's disease.
> The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
> but the supporting evidence is thin and directionally mixed — **3 clinical trials** (none testing this indication directly) and **8 publications**, most of which describe anti-TNF-*induced* vasculitis rather than treatment benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (also established for axial spondyloarthritis, psoriatic arthritis, and Crohn's disease per literature evidence) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information drawn from the supporting literature, certolizumab pegol is a PEGylated, Fc-free Fab fragment of a humanized monoclonal antibody that selectively neutralizes TNF-α; it is an established treatment for rheumatoid arthritis (RA), axial spondyloarthritis, psoriatic arthritis, and Crohn's disease.

Rheumatoid vasculitis is a recognized extra-articular complication of RA, and TNF-α is mechanistically implicated in the vascular inflammation seen in this condition — providing a plausible rationale for TxGNN to link certolizumab to this disease via shared pathway biology.

However, the literature retrieved for this candidate tells a more complicated story: of 8 publications, only **one** (PMID 34786446) reports certolizumab as a successful *treatment* for RA-associated vasculitis (leg ulcers). The remaining seven are adverse-event case reports and case series describing anti-TNF agents — including certolizumab itself — as a *cause* of vasculitis (leukocytoclastic vasculitis, hypocomplementemic urticarial vasculitis, medium-vessel vasculitis, rapidly progressive glomerulonephritis). This "paradoxical vasculitis" phenomenon is a known class effect of TNF inhibitors. The mechanistic direction of this prediction is therefore ambiguous rather than confirmatory.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in RA patients undergoing shoulder arthroplasty; not focused on vasculitis treatment |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional observational study of tocilizumab (not certolizumab) in RA; only indirectly relevant |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Real-world study of biologic-induced immune-mediated inflammatory disease risk; relates to disease-induction risk, not therapeutic benefit |

No trial in this evidence pack directly tests certolizumab pegol for rheumatoid vasculitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34786446](https://pubmed.ncbi.nlm.nih.gov/34786446/) | 2021 | Case report | JAAD Case Reports | Certolizumab pegol used to treat leg ulcers due to rheumatoid vasculitis (only positive treatment case) |
| [36597972](https://pubmed.ncbi.nlm.nih.gov/36597972/) | 2022 | Retrospective cohort | RMD Open | Long-term certolizumab pegol in uveitis due to immune-mediated inflammatory disease, n=80 (related IMID population, not vasculitis-specific) |
| [36418084](https://pubmed.ncbi.nlm.nih.gov/36418084/) | 2022 | Review/Safety analysis | RMD Open | Comparative infection profile of immune-modulatory drugs from SmPC data |
| [31990069](https://pubmed.ncbi.nlm.nih.gov/31990069/) | 2020 | Case report (ADR) | J Clin Pharm Ther | Hypocomplementemic urticarial vasculitis developed during certolizumab treatment for RA |
| [28405087](https://pubmed.ncbi.nlm.nih.gov/28405087/) | 2017 | Case report (ADR) | Proc (Baylor Univ Med Cent) | Leukocytoclastic vasculitis as a drug reaction to certolizumab pegol |
| [41158918](https://pubmed.ncbi.nlm.nih.gov/41158918/) | 2025 | Case report (ADR) | Cureus | Anti-TNF-related medium-vessel vasculitis in a seronegative RA patient switched to certolizumab |
| [32687015](https://pubmed.ncbi.nlm.nih.gov/32687015/) | 2021 | Case report (ADR) | Mod Rheumatol Case Rep | Rapidly progressive glomerulonephritis after introduction of certolizumab pegol |
| [29610119](https://pubmed.ncbi.nlm.nih.gov/29610119/) | 2018 | Case series (ADR) | Clin Med Res | Single-center experience of biologic agent-associated cutaneous adverse events |

**7 of 8 publications describe anti-TNF-induced vasculitis as an adverse drug reaction, not a therapeutic effect.**

---

## Norway Market Information

Certolizumab pegol currently holds **no market authorization in Norway** (market status: Not Marketed, 0 authorizations on record). No product listings are available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (TFDA label warnings, contraindications, and DDI data are flagged as a Blocking-severity data gap in this evidence pack and have not yet been retrieved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L4 with no trial directly testing certolizumab pegol for rheumatoid vasculitis, and the literature signal is predominantly the opposite of what is being proposed — most reports describe TNF inhibitors, including certolizumab, as *inducing* vasculitis rather than treating it. This is consistent with a known paradoxical anti-TNF class effect and does not currently support a repurposing hypothesis.

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (currently a Blocking data gap)
- Confirmed mechanism-of-action documentation from DrugBank
- A prospective or controlled study specifically evaluating certolizumab efficacy in rheumatoid vasculitis (none currently exists)
- A pharmacovigilance review to clarify whether the paradoxical vasculitis signal represents a safety risk rather than a therapeutic opportunity before further investment

**Note:** This same evidence pack contains two higher-confidence, L1-level signals for certolizumab pegol — *inflammatory spondylopathy* and *vertebral disease* — both reflecting its already-established, guideline-supported use in axial spondyloarthritis/ankylosing spondylitis. If not already documented as approved indications, these merit a separate, dedicated evaluation rather than being treated as novel repurposing candidates.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

