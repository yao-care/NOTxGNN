---
layout: default
title: Bosentan
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 9
---

# Bosentan
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

> Bosentan is a dual endothelin receptor (ETA/ETB) antagonist historically used for pulmonary arterial hypertension (PAH), though formal original-indication data was not captured in this evidence pack (data gap).
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> with **1 clinical trial** and **15 publications** currently associated with this direction — but the evidence is largely mechanistic/preclinical, and the single registered trial actually targets a different disease (Giant Cell Arteritis).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (0 Taiwan licenses on file). Bosentan is generally known as an endothelin receptor antagonist developed for pulmonary arterial hypertension — not confirmed by the data provided here (see DG001/DG002). |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (preclinical / mechanistic studies only) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known pharmacology, Bosentan is a dual endothelin receptor antagonist (ETA/ETB), and its efficacy in pulmonary arterial hypertension is well established through blockade of endothelin-1 (ET-1)-mediated vasoconstriction.

The mechanistic rationale for rheumatoid arthritis (RA) rests on the observation that ET-1 levels are elevated in RA synovial tissue, and animal models (collagen-induced arthritis, zymosan-induced arthritis) show that ETA/ETB blockade reduces TNF-α, LTB4, and other inflammatory mediators. IL-15 and IL-17-driven nociception in arthritis models has also been shown to be attenuated by dual ET receptor antagonism. These findings suggest a biologically plausible anti-inflammatory role for endothelin blockade in joint disease.

However, this link remains indirect and unproven in humans. The only registered clinical trial associated with this prediction (NCT06957002) is a Phase 2 study of Bosentan in **Giant Cell Arteritis**, not rheumatoid arthritis — a related but distinct rheumatic condition. No RA-specific human trial currently exists, so this prediction should be treated as a research hypothesis rather than a clinically validated indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06957002](https://clinicaltrials.gov/study/NCT06957002) | Phase 2 | Not Yet Recruiting | 40 | Multicenter RCT testing Bosentan + glucocorticoids vs. glucocorticoids alone for failure-free survival at 12 months — **note: enrolled population is Giant Cell Arteritis (GCA), not RA**; relevance graded "C" (mechanistic proxy only) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Preclinical (animal) | Inflammation Research | Bosentan ameliorates collagen-induced arthritis in mice; TNF-α drives induction of endothelin system genes |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Preclinical (animal) | Journal of Leukocyte Biology | ET receptor blockade modulates neutrophil accumulation and edema in zymosan-induced arthritis; ET-1 elevated in RA synovium |
| [19969421](https://pubmed.ncbi.nlm.nih.gov/19969421/) | 2010 | Preclinical (animal) | Pain | IL-17-mediated articular hypernociception in antigen-induced arthritis; ET pathway implicated in RA pain signaling |
| [16766656](https://pubmed.ncbi.nlm.nih.gov/16766656/) | 2006 | Preclinical (animal) | PNAS | IL-15-driven inflammatory hypernociception (relevant to RA) inhibited by dual ETA/ETB receptor antagonism |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheumatic Diseases Clinics of North America | Reviews PAH associated with connective tissue disease, including RA, and current ERA-based treatment options |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | Reviews PAH complicating connective tissue diseases including RA; discusses ET-1 pathophysiology |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case report | Kardiologia Polska | Pediatric case of Eisenmenger syndrome + juvenile RA treated with Bosentan; clinical improvement noted |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Reviews vasculopathy and PAH in autoimmune/rheumatic disease context |

---

## Taiwan Market Information

Bosentan currently has **0 authorizations on file** and is not marketed in Taiwan per this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data were not available in this evidence pack — flagged as Blocking data gap DG001, required before any S1 safety pre-assessment can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rheumatoid Arthritis) is supported only by preclinical/mechanistic evidence (L4) and animal models of arthritis; the sole registered trial targets a different disease (Giant Cell Arteritis, not RA). No completed human RA trial or RCT data exists to justify advancing this indication at this time.

**To proceed, the following is needed:**
- A dedicated RA-specific clinical trial or at minimum a Phase 2 proof-of-concept study
- TFDA/regulatory-grade package insert data (warnings, contraindications, DDI) — currently a Blocking gap (DG001)
- Confirmed mechanism of action documentation (DG002)
- Formal Taiwan regulatory pathway, given the drug is currently unmarketed (0 licenses)

**Note for reviewers:** Within the same evidence pack, **limited systemic sclerosis** (rank 3, TxGNN score 99.65%) shows substantially stronger evidence — a systematic review/meta-analysis, a 300-patient observational study, and multiple mechanistic papers on Bosentan reversing endothelial-to-mesenchymal transition — reaching evidence level **L2** with a "Proceed with Guardrails" recommendation. This candidate may warrant prioritization over the RA hypothesis for near-term development.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

