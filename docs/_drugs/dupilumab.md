---
layout: default
title: Dupilumab
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Dupilumab
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

# Dupilumab: From Atopic Dermatitis / Asthma to Bronchitis

## One-Sentence Summary

Dupilumab is a monoclonal antibody with an established role in moderate-to-severe atopic dermatitis and asthma, both driven by Type 2 (Th2) inflammation. The TxGNN model predicts it may also be effective for **Bronchitis**, but this direction is currently supported by only **1 clinical trial** (on a related condition) and **6 publications**, most of which address asthma/COPD rather than bronchitis directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate-to-severe Atopic Dermatitis / Asthma *(inferred from clinical trial and literature descriptions in this evidence pack — no formal TFDA/DrugBank indication text was retrieved; see Data Gaps)* |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 *(indirect — see caveat in rationale below)* |
| Norway Market Status | ✗ Not Marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently a data gap (DG002, High severity). However, the literature evidence collected in this pack independently and consistently describes dupilumab's mechanism: it is a fully human monoclonal antibody (IgG4 isotype) that binds the shared interleukin-4 receptor alpha (IL-4Rα) subunit, blocking signaling of both IL-4 and IL-13 — the two key cytokines driving Type 2/Th2-mediated inflammation (PMID 25006719, PMID 30194992, PMID 29557246).

Dupilumab's established uses (atopic dermatitis, asthma, and related conditions such as chronic rhinosinusitis) share this same Type 2/eosinophilic inflammatory pathway. Bronchitis — particularly its eosinophilic and smoking-associated (asthma-COPD overlap) subtypes — has been linked in the literature to the same Th2/IL-4/IL-13 axis (PMID 30196731 discusses chronic bronchitis within asthma-COPD overlap; PMID 38488768 discusses "novel therapies for eosinophilic pediatric plastic bronchitis"; PMID 39904363 reviews pharmacologic approaches, including biologics, for preventing COPD/bronchitis exacerbations).

This provides a plausible mechanistic rationale for repurposing: if bronchitis in a given patient is driven by eosinophilic/Type 2 airway inflammation, IL-4/IL-13 blockade could plausibly reduce inflammation and exacerbations, similar to its established effect in asthma. That said, the evidence currently available is largely extrapolated from adjacent respiratory conditions (asthma, COPD, CRS) rather than from trials conducted specifically in a bronchitis population — this gap should be weighed carefully in any decision.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Phase 2 | Completed | 33 | Randomized, double-blind, placebo-controlled study of dupilumab in chronic rhinosinusitis without nasal polyps (CRSsNP) — a related upper-airway Type 2-inflammatory condition, not bronchitis itself. Aimed to determine clinical effectiveness across several disease endotypes and inform patient-selection guidance for future applied research. |

*Note: No trial registered to date has enrolled a bronchitis-specific population; the single retrieved trial targets a mechanistically related but distinct diagnosis (CRSsNP).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Systematic Review / Meta-analysis | Journal of Asthma | Meta-analysis of RCTs comparing dupilumab vs. placebo in uncontrolled asthma; established efficacy/safety profile in Type 2 airway disease. |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Open-label Extension Study | Lancet Respiratory Medicine | TRAVERSE study: long-term (>1 year) safety and efficacy of dupilumab in moderate-to-severe asthma. |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Review | Tuberculosis and Respiratory Diseases | Comprehensive review of pharmacologic therapies, including biologics, for preventing COPD exacerbations. |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review / Expert Opinion | Expert Opinion on Pharmacotherapy | Discusses treatment challenges in smoking-induced airway diseases, including chronic bronchitis and asthma-COPD overlap. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Review | Pediatric Pulmonology | Reviews novel therapies, including biologics, for eosinophilic pediatric plastic bronchitis. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Observational Study | Chest | MRI-based evaluation of anti-T2 biologic treatment effects on lung ventilation in prednisone-dependent asthma. |

---

## Norway Market Information

Dupilumab currently holds **no marketing authorization** in Norway according to this evidence pack (market status: 未上市 / Not Marketed; 0 total authorizations; no license records available).

---

## Safety Considerations

Please refer to the package insert for safety information. *(Key warnings, contraindications, and drug-drug interaction data were not retrievable at this time — TFDA package insert extraction is flagged as a Blocking data gap, DG001, which prevents a full S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The TFDA package insert (warnings/contraindications) is a **Blocking** data gap (DG001), which by itself precludes a preliminary safety assessment (S1) for this candidate.
- Efficacy evidence specific to bronchitis is indirect: the single registered trial targets a related but distinct condition (CRSsNP), and the supporting literature is drawn mainly from asthma/COPD populations rather than bronchitis itself.
- Dupilumab is not currently marketed in Norway, so there is no local safety/utilization track record to draw on.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications, precautions) — DG001
- Confirmed DrugBank mechanism-of-action record — DG002
- Confirmation of the drug's formally approved original indication(s) (regulatory license text)
- Ideally, a trial or observational study conducted specifically in a bronchitis (particularly eosinophilic/Type 2) population, rather than extrapolation from asthma/COPD/CRS data
- Norway market registration status confirmation, should commercialization be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

