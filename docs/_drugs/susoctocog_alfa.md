---
layout: default
title: Susoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 334
evidence_level: L5
indication_count: 10
---

# Susoctocog Alfa
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

# Susoctocog Alfa: From Acquired Hemophilia A to Acquired Coagulation Factor Deficiency

## One-Sentence Summary

> Susoctocog alfa (recombinant porcine Factor VIII, marketed elsewhere as Obizur/OBIZER) is an established treatment for bleeding episodes in **Acquired Hemophilia A (AHA)** — an indication confirmed by the clinical trial and literature evidence in this pack, even though it is not formally recorded in the regulatory data fields here.
> The TxGNN model separately proposes an extension to the broader disease concept of **Acquired Coagulation Factor Deficiency**, supported by **1 clinical trial** and **10+ relevant publications** that largely describe the drug's established AHA use.
> This drug is **not currently marketed in Norway**. Of the 10 diseases TxGNN predicted overall, only this indication (and the closely related "hemophilia" node) has real supporting evidence — the other 8 are flagged below as low-confidence, mechanistically unsupported predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in regulatory data (data gap); clinical/literature evidence in this pack consistently identifies **Acquired Hemophilia A** as the drug's established use |
| Predicted New Indication | Acquired Coagulation Factor Deficiency (broader extension of the AHA mechanism) |
| TxGNN Prediction Score | 99.74% (hemophilia node, rank 4) / 99.64% (acquired coagulation factor deficiency, rank 5) |
| Evidence Level | L3 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the standard MOA field for this evidence pack (data gap). However, the clinical trial and literature evidence consistently describe susoctocog alfa as a **recombinant, B-domain-deleted porcine sequence Factor VIII (rpFVIII)**. It works by directly replacing coagulation Factor VIII activity in patients whose endogenous human FVIII has been neutralized by autoantibodies — the defining pathology of Acquired Hemophilia A (AHA).

The TxGNN-predicted node "acquired coagulation factor deficiency" is mechanistically coherent with the drug's known action: it is essentially the same pathophysiological category as AHA (loss of a clotting factor due to acquired/autoimmune causes rather than genetic deficiency), and shares nearly all of its supporting literature with the AHA/hemophilia node. This is best understood as TxGNN correctly recovering and generalizing the drug's known mechanism, rather than identifying a truly novel biological pathway.

By contrast, the drug's original approved use (AHA) itself is missing from the structured regulatory fields in this pack — this appears to be a data capture gap rather than a genuine absence of an approved indication, since the pivotal Phase II/III trial (NCT04580407, referenced in PMID 39158833) and multiple real-world studies describe susoctocog alfa/Obizur as licensed specifically for bleeding episodes in adult AHA patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A (post-marketing surveillance) | Recruiting | 25 | Japanese all-case surveillance of Susoctocog Alfa (OBIZER) IV injection for bleeding events in Acquired Hemophilia A, monitoring side effects and effectiveness in real-world use |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Review | Drugs | Comprehensive review: susoctocog alfa (Obizur) effective and generally well tolerated for serious bleeding in AHA in a multinational Phase II/III trial (n=28 evaluable) |
| [38066923](https://pubmed.ncbi.nlm.nih.gov/38066923/) | 2023 | Review | Hematology Am Soc Hematol Educ Program | Diagnosis and laboratory monitoring approach for AHA, including FVIII inhibitor assessment |
| [39245591](https://pubmed.ncbi.nlm.nih.gov/39245591/) | 2024 | Review | La Revue de médecine interne | 2024 update on AHA pathophysiology, diagnosis, and hemostatic treatment options including rpFVIII |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Review | Current Pharmaceutical Design | Perioperative anesthetic considerations for new hemostatic agents, including recombinant porcine FVIII |
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Phase II/III cohort | Int J Hematol | Japanese Phase II/III open-label study (NCT04580407) evaluating efficacy/safety of rpFVIII in adult AHA with severe bleeding |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Retrospective cohort | Blood Transfus | Largest Italian multicentre real-world registry of rpFVIII in 9 elderly AHA patients, describing efficacy and safety |
| [37584309](https://pubmed.ncbi.nlm.nih.gov/37584309/) | 2023 | Post-authorization safety cohort | Haemophilia | Non-interventional real-world safety and effectiveness study of rpFVIII in AHA |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | Cohort/PK | J Thromb Haemost | Pharmacokinetic strategies for precise FVIII control with susoctocog alfa dosing in AHA |
| [37799011](https://pubmed.ncbi.nlm.nih.gov/37799011/) | 2024 | Cohort (lab methods) | Int J Lab Hematol | Agreement between one-stage and chromogenic assays for monitoring rpFVIII activity |
| [36010349](https://pubmed.ncbi.nlm.nih.gov/36010349/) | 2022 | Cohort (lab methods) | Diagnostics | Analytical performance comparison of laboratory methods for measuring susoctocog-alfa activity |

---

## Other TxGNN-Predicted Indications (Low Confidence — Hold)

Beyond the AHA-related findings above, TxGNN's 8 remaining top-ranked predictions have **no supporting clinical trials or literature** and were explicitly flagged in the source evidence as mechanistically unsupported — the model appears to be linking these diseases via a general "bleeding tendency" semantic similarity rather than a specific pharmacological match:

| Disease | TxGNN Score | Why Mechanism Doesn't Fit |
|---------|------|------|
| Primary release disorder of platelets | 99.94% | Pathology is platelet granule release, not FVIII deficiency |
| Pseudo-von Willebrand disease | 99.93% | Caused by platelet GPIb abnormality, not FVIII |
| Glanzmann thrombasthenia | 99.88% | GPIIb/IIIa platelet aggregation defect, unrelated to FVIII |
| Scott syndrome | 99.60% | Platelet membrane scramblase defect, not FVIII |
| Bleeding diathesis (collagen receptor defect) | 99.17% | Platelet adhesion (e.g., GPVI) defect, not FVIII |
| Hemorrhagic disorder (constitutional thrombocytopenia) | 99.17% | Platelet count deficiency; FVIII replacement has no effect |
| Congenital Factor XIII deficiency | 99.15% | Deficiency in a different clotting factor (XIII, not VIII) |
| Adenosine deaminase deficiency | 99.04% | Immunodeficiency (SCID), no biological link to coagulation |

**Recommendation for all 8: Hold** — no clinical, mechanistic, or literature basis to pursue.

---

## Norway Market Information

Susoctocog alfa is **not currently marketed in Norway** (0 authorizations on record). No license or dosage form data is available in this pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data were not available in this evidence pack — this is flagged as a Blocking data gap, DG001, requiring TFDA/regulatory label retrieval before any safety-stage decision.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Only the AHA/acquired-coagulation-factor-deficiency signal (ranks 4–5) is backed by real clinical and observational evidence (L3), and it is mechanistically coherent with the drug's known replacement-therapy action — this largely represents confirmation/extension of an already-established use rather than a novel repurposing hypothesis. The other 8 TxGNN top-score predictions lack any supporting evidence and should be held.

**To proceed, the following is needed:**
- Retrieve official TFDA/EMA/FDA label (Obizur/OBIZER) to fill the Blocking safety data gap (DG001) — warnings, contraindications, DDI
- Retrieve DrugBank MOA data (DG002) to formally document mechanism
- Confirm and record the drug's actual original approved indication(s), currently missing from regulatory fields
- Clarify Norway-specific regulatory pathway, since the product is not currently marketed there
- If pursuing the broader "acquired coagulation factor deficiency" extension, seek disease-specific case data beyond AHA to support that generalization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

