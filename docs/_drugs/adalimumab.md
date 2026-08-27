---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 6
---

# Adalimumab
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

Using the drug-repurposing evaluation report format to produce this report from the supplied Evidence Pack. A few notes on how I handled data gaps before the report itself:

- `taiwan_regulatory.licenses` is empty and `original_indications` is empty, so the evidence pack contains **no sourced original-indication text**. Per the prompt's fallback rule for missing MOA data, I've applied the same logic here: Adalimumab's original indication (rheumatoid arthritis) is stated as general/public drug knowledge, clearly distinguished from evidence-pack-sourced regulatory data (which shows 0 Norway licenses / not marketed).
- The report focuses on `predicted_indications[0]` ("rheumatoid vasculitis"), consistent with the template's single-indication structure.
- Adalimumab is an immunomodulator (TNF-α inhibitor), not an antineoplastic/cytotoxic agent → the Cytotoxicity section is omitted per the rules.

---

# Adalimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Adalimumab is a TNF-α inhibitor originally used to treat rheumatoid arthritis and related inflammatory arthropathies.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**,
with **5 clinical trials** and **20 publications** currently retrieved in support of this direction, though most of the trial evidence is indirect (general RA/biologics practice-pattern studies rather than RV-specific interventional trials).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (not present in evidence pack's regulatory data; based on established drug information) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Norway Market Status | Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the evidence pack for this candidate (flagged as a High-severity data gap, DG002). Based on established drug information, adalimumab is a fully human monoclonal antibody that binds tumor necrosis factor-alpha (TNF-α), blocking its pro-inflammatory cytokine effects. Its efficacy in rheumatoid arthritis (RA) is well established, and it is approved across multiple TNF-α-driven inflammatory arthropathies.

Rheumatoid vasculitis (RV) is one of the most severe extra-articular manifestations of RA — a systemic vasculitis affecting small-to-medium vessels that arises from the same underlying autoimmune/inflammatory process as joint disease, with TNF-α implicated in its pathogenesis alongside immune-complex deposition. Because RV occurs almost exclusively in patients with (often long-standing, seropositive) RA, a drug already proven to control RA-driven inflammation is mechanistically plausible for RV as well.

That said, the literature evidence is mixed: alongside a systematic review and case reports of adalimumab controlling RV, there are also case reports of anti-TNF therapy being *associated with* vasculitis-like or lupus-like events, and of RV symptoms recurring after adalimumab dose reduction. This bidirectional signal (TNF-α inhibition as both a plausible treatment and a reported trigger/precipitant of vasculitic events) is an important nuance for interpreting the TxGNN prediction and warrants careful case-by-case clinical judgment rather than a blanket efficacy assumption.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Evaluates perioperative immunosuppressant (incl. biologic) holding strategies in rheumatology patients undergoing shoulder arthroplasty; assesses flare risk, not an RV efficacy trial |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of tocilizumab (not adalimumab) practice patterns in RA patients with inadequate DMARD response |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | Completed | 9,261 | Real-world safety study of brolucizumab in wet AMD — unrelated drug/indication, likely a keyword-matched false positive |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biological DMARD treatment patterns and RA disease characteristics in China |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large-scale study of incident immune-mediated inflammatory disease risk in patients on biologics/immunosuppressants for a single IMID |

**Note:** None of the retrieved trials are interventional studies of adalimumab specifically for rheumatoid vasculitis; they are broader RA/biologics safety and practice-pattern studies (one appears unrelated). No dedicated RV trial for adalimumab is currently registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | Systematic review of biological therapy (including anti-TNF agents) in rheumatoid vasculitis; RV is a severe extra-articular RA manifestation requiring aggressive treatment |
| [18799049](https://pubmed.ncbi.nlm.nih.gov/18799049/) | 2008 | Systematic Review | Clin Exp Rheumatol | Systematic review of 2,707 RA patients (18 vasculitis cases) comparing vasculitis occurrence with vs. without anti-TNF treatment |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-Analysis (36 RCTs) | Int J Mol Sci | Compares 5 TNF inhibitors (incl. adalimumab) vs. methotrexate/placebo on radiographic joint destruction in RA — supports adalimumab's established anti-inflammatory efficacy |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | Case Report | Internal Medicine (Tokyo) | Acute pulmonary hypertension crisis in an RV patient 8 months after adalimumab dose reduction — signals risk of RV flare on de-escalation |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | Case Report | Case Reports in Rheumatology | Digital (RA-associated) vasculitis responded well to adalimumab in a 42-year-old patient |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort Study | RMD Open | BSRBR-RA registry comparison of lupus-like and vasculitis-like event risk between TNFi- and nbDMARD-treated RA patients |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | Review | J Clin Medicine | Update on treatment of RA-associated episcleritis/scleritis, an extra-articular manifestation overlapping with the RV spectrum |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | Case Report | Am J Dermatopathology | Leukocytoclastic vasculitis with perivascular hemophagocytosis reported during adalimumab therapy for RA |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | Case Report | Internal Medicine (Tokyo) | ANCA-associated nephritis emerging during abatacept/adalimumab therapy for RA, later attenuated by tocilizumab |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | Case Report | Nephrologie & Therapeutique | ANCA-associated vasculitis (necrotizing glomerulonephritis) reported in an RA patient on adalimumab |

## Norway Market Information

Adalimumab is currently **not marketed** in Norway according to the available regulatory data (0 authorizations on record). No product/authorization details are available to tabulate.

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields in the evidence pack — key warnings, contraindications, and drug-drug interactions — are currently unavailable. Notably, retrieval of the Norway package insert warnings/contraindications is flagged as a **Blocking** data gap, since it prevents an initial S1 safety assessment.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking data gap exists (Norway package insert warnings/contraindications not retrieved), which by definition prevents even the initial (S1) safety assessment required before this candidate can advance.
- Adalimumab is not currently marketed in Norway, and no adalimumab trial specifically targets rheumatoid vasculitis as an indication — supporting evidence is limited to one systematic review, one earlier systematic review of vasculitis events, an RCT meta-analysis on a different endpoint (joint destruction), and several case reports (some describing adalimumab controlling RV, others describing anti-TNF-associated vasculitic/autoimmune adverse events). This corresponds to Evidence Level L3, not L1/L2.

**To proceed, the following is needed:**
- Retrieve the official Norway package insert (warnings, contraindications) to complete the S1 safety assessment (Blocking gap, DG001)
- Obtain detailed mechanism-of-action reference data from DrugBank to strengthen the mechanistic rationale (High-priority gap, DG002)
- Confirm the drug's original approved indication(s) and regulatory history via authoritative regulatory sources, since this evidence pack contains no sourced original-indication or licensing data
- Given the mixed signal in the case-report literature (both efficacy and RV-flare/vasculitis-inducing reports), any future evaluation should specifically weigh anti-TNF-associated vasculitis risk against RV treatment benefit before considering guardrails for clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

