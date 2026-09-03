---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 9
---

# Deferiprone
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

# Deferiprone: From Transfusional Iron Overload (Thalassemia) to Hepatic Porphyria

## One-Sentence Summary

> Deferiprone is an oral iron chelator internationally approved (as Ferriprox) for transfusion-dependent iron overload in thalassemia; it is not currently marketed in Norway.
> The TxGNN model's top-ranked new indication is **Hepatic Porphyria**, based on the shared mechanism of iron-catalyzed porphyrin toxicity.
> Currently only **2 preclinical (animal model) publications** support this direction — **no clinical trials** and **no human data** are available.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transfusion-dependent iron overload in thalassemia (internationally approved as Ferriprox; not present in Norway regulatory dataset) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, deferiprone is an oral trivalent-iron (Fe³⁺) chelator, whose efficacy in transfusional iron overload (thalassemia) has been proven and is the basis of its Ferriprox approval.

The pathophysiology of certain hepatic porphyrias (particularly congenital erythropoietic porphyria and porphyria cutanea tarda) involves iron-catalyzed oxidation of porphyrin precursors, which drives hemolysis and skin photosensitivity. Mechanistically, removing catalytic free iron via chelation could plausibly reduce this oxidative injury — this is the rationale TxGNN is drawing on.

However, the two supporting publications are murine model studies of CEP and PCT specifically, not the broader "hepatic porphyria" category used in this prediction, and no human clinical data exist. The mechanistic link is biologically credible but remains unproven in patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Preclinical (murine CEP model) | Blood | Iron chelation rescued hemolytic anemia and skin photosensitivity in a congenital erythropoietic porphyria mouse model |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Preclinical (murine PCT model) | Hepatology | Oral iron chelator (deferiprone/L1) reduced hepatic uroporphyrin accumulation in Hfe⁻/⁻ mice, comparable to iron-deficient diet |

---

## Norway Market Information

Currently not marketed in Norway; no authorization records available (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA-equivalent label warnings/contraindications (DG001, Blocking severity) and detailed MOA data (DG002, High severity) are currently identified data gaps and must be resolved before any S1 safety pre-assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for hepatic porphyria is limited to two preclinical animal studies on CEP/PCT specifically, not the broader "hepatic porphyria" category; no human trials exist, and blocking safety data gaps (label warnings, contraindications) prevent a safety pre-assessment. The drug is also not currently marketed in Norway.

**To proceed, the following is needed:**
- TFDA/Norwegian-equivalent label warnings and contraindications (DG001 — blocking)
- Detailed mechanism of action data (DG002)
- Human clinical evidence specific to hepatic porphyria (ideally CEP/PCT patient cohorts, not just animal models)
- Confirmation of Norway regulatory/marketing pathway, since the drug currently has zero local authorizations

---

**Additional context on other candidates in this evidence pack:**
- **Beta-thalassemia with other manifestations (rank 8, L1, Proceed with Guardrails)** is not a *new* indication — the rationale text confirms this reflects deferiprone's existing Ferriprox on-label use for transfusional iron overload.
- **Ranks 2–6, 9** (idiopathic copper-associated cirrhosis, hepatoportal sclerosis, early-onset familial noncirrhotic portal hypertension, hepatopulmonary syndrome, primitive portal vein thrombosis, hereditary pyropoikilocytosis) are **L5, no supporting literature/trials**, and the rationale text for several explicitly flags them as likely false positives (e.g., copper chelation is mechanistically weak for deferiprone). These should not be pursued without independent evidence.
- **Pyruvate kinase deficiency (rank 7, L4)** has a plausible secondary iron-overload rationale but no literature/trial support in this dataset — same "Research Question" status as the primary candidate above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

