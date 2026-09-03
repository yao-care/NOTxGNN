---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 5
---

# Golimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Golimumab: From TNF-α-Driven Inflammatory Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab is a fully human anti-TNF-α monoclonal antibody, established for rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis. The TxGNN model predicts it may also be effective for **rheumatoid vasculitis**, but currently only **3 loosely related clinical trials** and **6 publications** (mostly case reports) support this specific direction, and the mechanistic signal is mixed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis (established anti-TNF-α indications; per literature evidence, e.g. PMID 20065639, 28530020) |
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for golimumab is not currently available in the source data. Based on known information from the evidence pack's own literature (e.g. PMID 20065639, 28530020), golimumab is a fully human anti-TNF-α IgG1κ monoclonal antibody, approved for rheumatoid arthritis (RA), psoriatic arthritis, and ankylosing spondylitis.

Rheumatoid vasculitis is a severe extra-articular manifestation of RA, and TNF-α is known to participate in the inflammatory cascade underlying vascular injury in RA. On this basis, a drug that suppresses TNF-α could plausibly reduce vasculitic activity in RA patients — the disease and the predicted new indication share the same underlying autoimmune population.

However, the literature evidence is not one-directional. A case report (PMID 22999907) describes **new-onset Takayasu's arteritis occurring under anti-TNF therapy** — a paradoxical vasculitis phenomenon that has been reported with this drug class. This means the relationship between anti-TNF-α agents and vasculitis is bidirectional and uncertain, not a clean mechanistic match. No trial or study in this pack directly tests golimumab as a treatment for rheumatoid vasculitis; the supporting evidence is indirect and largely inferential.

---

## Clinical Trial Evidence

None of the identified trials directly evaluate golimumab as a treatment for rheumatoid vasculitis; all listed studies are indirectly related (general RA/IMID population or perioperative management).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large database study on risk of new immune-mediated inflammatory disease (including vasculitis-type conditions) in patients on biologics/immunosuppressants; indirect safety signal only, status unknown |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Post-marketing observational study of tocilizumab (not golimumab) in RA patients with inadequate DMARD response; general RA population, not vasculitis-specific |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; unrelated to vasculitis efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network meta-analysis (RCT-based) | Int J Mol Sci | Compares 5 anti-TNF agents (incl. golimumab) on radiographic joint destruction in RA vs. methotrexate; not vasculitis-specific |
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | Overview of biologic therapies for autoimmune/rheumatologic disease, including anti-TNF agents |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Cohort | Semin Arthritis Rheum | Frequency and causes of end-stage renal disease in RA patients; relevant to comorbidity burden, not vasculitis treatment |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case report | Rheumatol Int | Severe sepsis (pyoderma gangrenosum + pyogenic arthritis) in an RA patient on golimumab; notes rheumatoid vasculitis incidence has decreased since anti-TNF introduction, but reports a serious adverse event |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case report | Joint Bone Spine | Two cases of **Takayasu's arteritis occurring under anti-TNF therapy** — a paradoxical vasculitis signal that complicates the mechanistic rationale |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case report | Ocul Immunol Inflamm | Behçet disease-associated uveitis (a different vasculitis entity) successfully treated with golimumab |

---

## Norway Market Information

Golimumab currently holds **no marketing authorization** in this jurisdiction (Market Status: Not Marketed; Total Authorizations: 0). No license records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information. No structured key warnings, contraindications, or drug interaction data are currently available for this drug in the evidence pack (TFDA label data has not yet been retrieved — see Conclusion).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale (TNF-α involvement in vascular inflammation) is plausible but is directly counterbalanced by case reports of anti-TNF-induced vasculitis (paradoxical effect), and no trial in this pack studies golimumab specifically in rheumatoid vasculitis — evidence is limited to case reports and indirect cohort/database studies (Evidence Level L4).

**To proceed, the following is needed:**
- TFDA/official label data on warnings and contraindications (currently a **Blocking** data gap — required before any safety pre-screening, S1)
- Confirmed mechanism-of-action documentation from DrugBank (currently a **High**-severity data gap affecting mechanistic-linkage analysis)
- A dedicated study (RCT or controlled cohort) evaluating golimumab specifically in RA-associated vasculitis, given current evidence is indirect and mechanistically ambiguous

**Note:** This evidence pack also screened four other candidate indications for golimumab. Two — **inflammatory spondylopathy** and **polyarticular juvenile idiopathic arthritis** — are backed by multiple completed Phase 3 RCTs (Evidence Level L1) and carry a "Proceed with Guardrails" recommendation; these represent substantially stronger repurposing opportunities than rheumatoid vasculitis and may warrant separate, prioritized evaluation. The remaining two ("hypermobility of coccyx," "Kummell disease") have no supporting clinical or literature evidence and are assessed as likely model noise.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

