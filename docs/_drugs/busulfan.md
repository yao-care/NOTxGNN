---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Busulfan
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

Using no specialized skill here — this is a direct content-generation task with an explicit template already provided in the prompt; I'll follow it directly.

---

# Busulfan: From Alkylating Chemotherapy Agent to Myelodysplastic Syndrome

## One-Sentence Summary

> Busulfan is a bifunctional alkylating agent classically used in chemotherapy and, more recently, as a cornerstone of pre-transplant conditioning regimens; this evidence pack does not contain a formally coded "original indication" field, but the underlying mechanistic data describe it as a standard component of allogeneic hematopoietic stem cell transplantation (HSCT) conditioning.
> The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**,
> with **50 clinical trials** and **20 publications** currently supporting this direction — much of which reflects an already-established standard-of-care use rather than a truly novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (`original_indications` empty; `original_moa` marked as a data gap). Busulfan is a classical alkylating agent historically used for cytoreductive chemotherapy and as HSCT conditioning. |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal MOA data (DrugBank `original_moa`) is not available in this evidence pack. Based on the mechanistic rationale that *is* captured in the pack's `repurposing_rationale`, busulfan is a bifunctional alkylating agent that crosslinks DNA, producing potent, dose-dependent myelotoxicity. This property has historically been exploited for cytoreductive chemotherapy (classically in chronic myeloid leukemia, prior to the tyrosine-kinase-inhibitor era) and — more centrally to the evidence gathered here — as a standard component of myeloablative or reduced-intensity **conditioning regimens** prior to allogeneic HSCT, typically combined with fludarabine or cyclophosphamide.

The relationship between busulfan's established pharmacology and the top predicted indication, MDS, is direct rather than speculative: MDS is a clonal hematopoietic stem cell disorder for which allogeneic HSCT is the only potentially curative option, and busulfan-based conditioning is already the clinical standard used to ablate the diseased hematopoietic clone and permit donor stem cell engraftment. As the evidence pack itself notes for this candidate: *"this is not a genuinely novel indication but rather a consolidation of evidence for an already-established standard clinical use."*

Mechanistically, this cytotoxic/myeloablative action is disease-agnostic with respect to which abnormal hematopoietic clone is being eradicated — which is why the model's next several ranked predictions (refractory cytopenia of childhood, unclassified MDS, 5q- deletion syndrome, aregenerative/severe aplastic anemia) all cluster around the same underlying mechanism: busulfan clearing marrow to enable transplant. A more exploratory signal — busulfan conditioning to enable engraftment of CCR5-modified or gene-edited CD34+ cells in HIV cure strategies (rank 7) — extends the same mechanism to an experimental, non-oncologic context and carries substantially weaker, largely Phase 1 evidence.

---

## Clinical Trial Evidence
*(for top-ranked predicted indication: Myelodysplastic Syndrome)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06477549](https://clinicaltrials.gov/study/NCT06477549) | Phase 2 | Recruiting | 220 | RCT comparing bendamustine vs. ruxolitinib added to fludarabine/busulfan conditioning in haploidentical HSCT; graded A relevance — large, directly on-mechanism. |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | Active, not recruiting | 116 | Randomized study of venetoclax with timed-sequential busulfan/cladribine/fludarabine conditioning in AML and MDS; graded A relevance. |
| [NCT00416598](https://clinicaltrials.gov/study/NCT00416598) | Phase 2 | Completed | 546 | Large trial of decitabine maintenance after busulfan-containing induction/intensification in AML; graded B (busulfan as background agent). |
| [NCT00454480](https://clinicaltrials.gov/study/NCT00454480) | Phase 2/3 | Completed | 2000 | Large treatment-development program for older AML and high-risk MDS patients incorporating busulfan-based regimens. |
| [NCT00226512](https://clinicaltrials.gov/study/NCT00226512) | Phase 3 | Withdrawn | 203 | Multi-institutional RCT of non-myeloablative fludarabine/busulfan conditioning ± anti-lymphocyte antibodies for AML/MDS allo-HSCT. |
| [NCT00002989](https://clinicaltrials.gov/study/NCT00002989) | Phase 3 | Unknown | 207 | Randomized trial assessing intensification of the conditioning regimen for allo-HSCT in leukemia/MDS with high relapse risk. |
| [NCT00301834](https://clinicaltrials.gov/study/NCT00301834) | Phase 2 | Completed | 35 | Fludarabine/busulfan/alemtuzumab as reduced-toxicity ablative conditioning for children with marrow failure syndromes or MDS/leukemia. |
| [NCT01177371](https://clinicaltrials.gov/study/NCT01177371) | Phase 2 | Completed | 13 | High-dose busulfan + cyclophosphamide followed by allogeneic BMT for leukemia, MDS, myeloma, and lymphoma. |
| [NCT00186342](https://clinicaltrials.gov/study/NCT00186342) | N/A | Completed | 120 | Busulfan/etoposide/cyclophosphamide conditioning; tolerability/efficacy in acute leukemia and MDS/MPD patients aged 51–60. |
| [NCT02861417](https://clinicaltrials.gov/study/NCT02861417) | Phase 2 | Active, not recruiting | 204 | Timed-sequential busulfan plus post-transplant cyclophosphamide for allogeneic transplantation in blood cancers. |

*40 additional trials in the evidence pack were not included above for brevity; most are general hematologic-malignancy/HSCT-conditioning trials in which busulfan is a background regimen component rather than the primary study intervention.*

---

## Literature Evidence
*(for top-ranked predicted indication: Myelodysplastic Syndrome)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT | American Journal of Hematology | Final analysis of a Phase III RCT: treosulfan-based conditioning shows non-inferior/superior event-free survival vs. reduced-intensity busulfan in older AML/MDS patients. |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | RCT | The Lancet Haematology | Randomized, non-inferiority Phase 3 trial: treosulfan vs. busulfan+fludarabine conditioning before allo-HSCT in older AML/MDS patients. |
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | RCT (Phase 3) | The Lancet Haematology | Open-label, multicentre RCT: G-CSF+decitabine+busulfan-cyclophosphamide vs. busulfan-cyclophosphamide conditioning to reduce relapse in MDS/secondary AML. |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | RCT (Phase 3) | Journal of Clinical Oncology | Randomized comparison of myeloablative vs. reduced-intensity conditioning (busulfan-containing) for AML/MDS allo-HSCT. |
| [34692485](https://pubmed.ncbi.nlm.nih.gov/34692485/) | 2021 | Meta-analysis of RCTs | Frontiers in Oncology | Reduced-intensity conditioning shows comparable outcomes to myeloablative conditioning for AML/MDS allo-HSCT. |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Systematic Review/Meta-analysis | Frontiers in Oncology | Long-term outcomes of treosulfan- vs. busulfan-based conditioning for MDS and AML before HSCT. |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Review | American Journal of Hematology | Contemporary review of allogeneic HSCT for myelofibrosis and MDS, including conditioning regimen selection. |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Cohort (registry, propensity-matched) | Bone Marrow Transplantation | Nationwide Japanese registry: fludarabine/busulfan vs. busulfan/cyclophosphamide myeloablative conditioning for MDS. |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Cohort | Cancer | Fractionated IV busulfan myeloablative conditioning improves survival in older AML/MDS patients. |
| [37856098](https://pubmed.ncbi.nlm.nih.gov/37856098/) | 2024 | Evidence-based risk review | Pediatric Blood & Cancer | Evidence-based assessment of busulfan exposure and subsequent malignancy risk, relevant to non-malignant/gene-therapy conditioning use. |

*10 additional publications in the evidence pack (largely retrospective cohorts and case reports on treosulfan/busulfan comparisons and long-term toxicity) were not included above for brevity.*

---

## Norway Market Information

Busulfan currently holds **no marketing authorizations** in the regulatory registry captured by this evidence pack (`market_status`: not marketed; `total_licenses`: 0). No product name, dosage form, or approved-indication text is available for extraction from `taiwan_regulatory.licenses`.

---

## Cytotoxicity

Busulfan meets the antineoplastic/cytotoxic criteria: it is a classical alkylating agent, and the evidence pack's own mechanistic rationale explicitly describes it as inducing "DNA crosslinking leading to myeloablative cytotoxicity."

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, alkyl sulfonate class) |
| Myelosuppression Risk | High — busulfan is used specifically for its potent, myeloablative bone-marrow-clearing effect in conditioning regimens; profound and prolonged cytopenias are expected and intended in this context. |
| Emetogenicity Classification | Moderate to High (typical for IV alkylating agents at myeloablative/conditioning doses; confirm exact category against the package insert) |
| Monitoring Items | CBC with differential, hepatic function (veno-occlusive disease/SOS risk is a known busulfan-class concern), pulmonary function, and — where used at myeloablative doses — seizure prophylaxis and plasma-level (PK-guided) monitoring |
| Handling Protection | Yes — standard cytotoxic/hazardous drug handling precautions required for preparation and administration |

---

## Safety Considerations

Please refer to the package insert for safety information. (`key_warnings`, `contraindications`, and drug-interaction data are all marked as data gaps in this evidence pack; no DDI records were found.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top predicted indication (MDS) is supported by strong, largely Phase 2–3 evidence (L2), including multiple randomized trials directly comparing busulfan-based conditioning regimens in this population — this is less a "new" repurposing hypothesis and more a data-driven confirmation of busulfan's already-standard role in HSCT conditioning for MDS. Lower-ranked predictions in this pack range from moderately supported (refractory cytopenia of childhood, severe aplastic anemia — L2/L3) to essentially unsupported model artifacts (5q- deletion syndrome, seborrheic keratosis, feline AIDS — L5, no trials or literature), and should not be advanced without dedicated evidence.

**To proceed, the following is needed:**
- Official Taiwan/Norway package insert (PI) warnings and contraindications — currently a **blocking data gap (DG001)**; without this, the candidate cannot formally clear the S1 safety pre-screen despite the strength of efficacy evidence.
- Confirmed DrugBank MOA record (DG001/DG002) to replace the inferred mechanistic summary used in this report.
- Formal `original_indications` and licensing data, since none were present in this evidence pack.
- Given busulfan already lacks Norway marketing authorization, a market-access/registration pathway assessment before any further clinical positioning work.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

