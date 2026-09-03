---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 6
---

# Etanercept
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept is a TNF-α receptor fusion protein originally established for the treatment of rheumatoid arthritis and related inflammatory arthritides.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **6 clinical trials** and **20 publications** identified — but the evidence itself points in the opposite direction, repeatedly documenting etanercept-*induced* vasculitis rather than a therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (and related TNF-α-driven arthritides) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap). Based on known information, etanercept is a soluble p75 TNF receptor–Fc fusion protein that binds and neutralizes TNF-α; its efficacy in rheumatoid arthritis has been proven and, mechanistically, TNF-α blockade is theoretically applicable to rheumatoid vasculitis (RV), since TNF-α is understood to participate in the vasculitic inflammatory pathways seen in RA.

However, the evidence collected for this specific candidate does not support that mechanistic logic in practice. The only trial testing etanercept directly in an ANCA-associated vasculitis population — the WGET study ([NCT00001901](https://clinicaltrials.gov/study/NCT00001901), Wegener's granulomatosis) — was **negative**: etanercept failed to demonstrate efficacy and was associated with an increased rate of malignancy. In parallel, a large body of case reports, case series, and cohort studies describes etanercept as a **cause** of cutaneous, renal, and lupus-like vasculitis in RA patients (autoantibody induction, ANA/dsDNA seroconversion), rather than a treatment for it. This is a well-recognized "paradoxical" TNF-inhibitor safety signal, not a typical mechanism-supports-indication scenario.

Because of this direction-of-effect mismatch, the model's high similarity score should be interpreted as reflecting shared disease/pathway proximity (RA ↔ RV) in the knowledge graph rather than genuine predicted efficacy.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 1/2 | Completed | 60 | WGET trial: etanercept in Wegener's granulomatosis (ANCA-associated vasculitis); result was **negative** — no efficacy benefit and increased malignancy risk. Most direct evidence available. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large population-level study on risk of incident immune-mediated inflammatory diseases in patients treated with biologics/immunosuppressants; safety-signal relevant but not vasculitis-specific. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab (not etanercept) in RA; limited relevance. |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world RA treatment pathways with etanercept vs non-biologics; no vasculitis focus. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biologic DMARD treatment patterns in RA; not vasculitis-specific. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Immunosuppressant management around shoulder arthroplasty in rheumatology patients; not mechanistically related to vasculitis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Review | Clinical Rheumatology | Systematic review of biological therapy in rheumatoid vasculitis; summarizes limited and heterogeneous evidence for TNF inhibitors including etanercept. |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Review | The Journal of Rheumatology | Reviews reports of TNF-α blockade being associated with, rather than protective against, vasculitis. |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology Dialysis Transplantation | Discusses rationale and evidence gaps for TNFα blockade in ANCA-associated vasculitis and glomerulonephritis. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA registry: compares risk of lupus-like and vasculitis-like events in TNFi-treated vs non-biologic DMARD-treated RA patients — TNFi use associated with increased risk. |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case series | Scandinavian Journal of Immunology | Describes immunologic mechanisms of cutaneous vasculitis occurring after etanercept and infliximab therapy. |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case report | Arthritis and Rheumatism | Accelerated rheumatoid nodulosis and vasculitis following etanercept therapy for RA. |
| [41327089](https://pubmed.ncbi.nlm.nih.gov/41327089/) | 2025 | Case report | BMC Nephrology | RA patient on biologic therapy who successively developed membranous nephropathy and ANCA-associated vasculitis. |
| [31632872](https://pubmed.ncbi.nlm.nih.gov/31632872/) | 2019 | Case report | Cureus | Etanercept-associated nephropathy, illustrating renal autoimmune adverse effects of TNF inhibition. |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | Cohort | Annals of the Rheumatic Diseases | Single-centre cohort evaluating whether routine ANA testing predicts biologic-DMARD-induced lupus/vasculitis in RA patients. |
| [31668853](https://pubmed.ncbi.nlm.nih.gov/31668853/) | 2019 | RCT | Biologicals | Real-world comparison of originator vs biosimilar (SB4) etanercept efficacy and safety in active RA; background safety data only, not vasculitis-specific. |

## Norway Market Information

Etanercept currently has **no marketing authorization on record in Norway** (market status: not marketed; 0 authorizations). No product-level licensing data is available for this evaluation.

## Safety Considerations

Please refer to the package insert for formal safety information (TFDA/product-label warnings and contraindications are a data gap — see DG001).

**Note on evidence-derived safety signal:** independent of the formal label data gap, the literature gathered for this specific candidate documents a recurring adverse effect pattern — etanercept has been repeatedly reported to **induce or exacerbate** cutaneous and renal vasculitis, ANA/dsDNA seroconversion, and lupus-like syndromes in RA patients. This signal is directly relevant to the rheumatoid vasculitis indication under review and should be weighted heavily in any S1 safety assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only direct interventional trial (WGET, Phase 1/2, ANCA-associated vasculitis) was negative, and the surrounding literature predominantly reports etanercept as a cause of vasculitis rather than a treatment for it. The TxGNN score reflects graph-level similarity between RA and RV, not validated therapeutic direction, so this candidate should not advance past S1 in its current form.

**To proceed, the following is needed:**
- TFDA/product-label warnings and contraindications (DG001, blocking) to complete the S1 safety review
- Formal mechanism-of-action documentation (DG002) to clarify whether any TNF-inhibitor subtype or dosing context could plausibly avoid the paradoxical vasculitis signal
- A structured relevance re-grading of the literature currently marked "pending" to confirm the direction-of-effect conclusion

**Note for portfolio prioritization:** within this same evidence pack, two other etanercept candidates — *inflammatory spondylopathy* (rank 3, L1, Proceed with Guardrails) and *polyarticular juvenile rheumatoid arthritis* (rank 5, L1, Proceed with Guardrails) — have substantially stronger and directionally consistent supporting evidence, and may warrant prioritized review ahead of this candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

