---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 360
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanized anti-IL-6 receptor monoclonal antibody with established use in rheumatoid arthritis and other IL-6-driven inflammatory diseases. The TxGNN model predicts it may be effective for **Ankylosing Spondylitis (AS)**, with **9 clinical trials** and **19 publications** available — but the dedicated Phase 3 program for this exact indication was already run and terminated early for insufficient efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not captured in Norway regulatory license data (drug not marketed in Norway); established in the literature evidence base as Rheumatoid Arthritis and other IL-6-mediated inflammatory diseases (e.g. sJIA/pJIA, giant cell arteritis) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (two dedicated Phase 3 RCTs exist, but both were terminated for lack of efficacy — see caveat below) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data from DrugBank is not available (Data Gap DG002). Based on information present in the linked literature evidence, tocilizumab is a recombinant humanized monoclonal antibody against the interleukin-6 receptor (IL-6R), blocking both membrane-bound and soluble IL-6R signaling. Its efficacy in rheumatoid arthritis, systemic/polyarticular juvenile idiopathic arthritis, and giant cell arteritis is well established, and mechanistically IL-6 is a plausible driver of any chronic inflammatory rheumatic disease — which is why TxGNN's knowledge graph places ankylosing spondylitis close to tocilizumab's known indications.

However, this mechanistic hypothesis has already been tested directly in patients. Two dedicated, purpose-built trials — a Phase 3 study in TNF-inadequate responders (NCT01209689) and a Phase II/III seamless pivotal study in TNF-naïve patients (NCT01209702) — were both **terminated early**, and the pooled results were published as the BUILDER-1/BUILDER-2 program (PMID 23765873), which concluded tocilizumab did not provide clinically meaningful symptomatic benefit in AS. The prevailing explanation in the supporting literature (e.g. PMID 22452603, PMID 21803631) is that axial spondyloarthropathies are predominantly driven by the IL-17/TNF axis rather than IL-6, unlike rheumatoid arthritis. The high TxGNN similarity score therefore likely reflects graph proximity between AS and tocilizumab's approved indications rather than a validated new therapeutic effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | RCT of tocilizumab (4 or 8 mg/kg IV) vs placebo in AS patients with inadequate response to prior TNF antagonists; terminated early |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | Pivotal seamless RCT of tocilizumab vs placebo in TNF-naïve, NSAID-refractory AS patients; terminated early |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Observational cytokine/biomarker profiling across systemic inflammatory diseases, not AS-specific |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean nationwide biologics/tsDMARD safety registry covering RA, AS, and PsA patients |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper and B cell maturation in RA (not AS) |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | Real-world observational registry for Inflectra (infliximab), tocilizumab relevance indirect |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large epidemiological study on risk of a second immune-mediated inflammatory disease in patients already treated for one IMID |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty, not an AS efficacy trial |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | Not yet recruiting | 52 | Secukinumab (not tocilizumab) trial in Takayasu arteritis; only tangentially relevant via shared IL-6/T-cell pathway rationale |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT (pooled report) | Annals of the Rheumatic Diseases | BUILDER-1/BUILDER-2: tocilizumab failed to show meaningful short-term symptomatic efficacy in AS |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review / Network Meta-Analysis | Medicine | Comparative effectiveness of biologic regimens for AS; IL-6 blockade underperforms TNF/IL-17 blockers |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Reviews rationale and limited clinical evidence for IL-6 antagonism specifically in AS |
| [21803631](https://pubmed.ncbi.nlm.nih.gov/21803631/) | 2011 | Review | Joint Bone Spine | Biologic agents for AS beyond TNFα antagonists, including IL-6 pathway agents |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report / Review | Frontiers in Medicine | Two cases of successful tocilizumab treatment of AA amyloidosis complicating AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clinical Rheumatology | Risk of serious infection with biologics (including IL-6 inhibitors) in axial SpA/AS RCTs |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clinical and Experimental Rheumatology | Contrasts biologic efficacy patterns between RA and AS, noting differing pathogenesis |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Seminars in Arthritis and Rheumatism | Second-line biologic therapy optimization across RA, PsA, and AS |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Current Opinion in Rheumatology | Treatment options for AS refractory to TNF inhibition, including alternative cytokine targets |
| [27789989](https://pubmed.ncbi.nlm.nih.gov/27789989/) | 2009 | Review | Open Access Rheumatology | Comprehensive review of biologics available for RA, AS, and PsA |

---

## Norway Market Information

Tocilizumab is currently **not marketed in Norway** under this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Structured warnings, contraindications, and drug interaction data were not available in this evidence pack — Data Gap DG001, flagged as Blocking severity.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN prediction score for ankylosing spondylitis is not supported by clinical outcome data — the two dedicated Phase 3 trials designed specifically to test this hypothesis (NCT01209689, NCT01209702) were terminated early for insufficient efficacy, and the published pooled results (PMID 23765873) confirm no meaningful symptomatic benefit. This indication should not proceed as a repurposing candidate.

**To proceed, the following is needed:**
- TFDA/Norway package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed DrugBank mechanism-of-action record (DG002)
- If repurposing work continues for this drug, consider redirecting evaluation toward **rheumatoid vasculitis** (rank 2 in this pack, evidence level L4, decision stage S1, "Research Question") — a severe extra-articular manifestation of the drug's already-approved parent indication (RA), supported by refractory-case reports and stronger mechanistic plausibility, rather than ankylosing spondylitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

