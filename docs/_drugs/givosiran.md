---
layout: default
title: Givosiran
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Givosiran
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

# Givosiran: From Acute Hepatic Porphyria to ALA Dehydratase Deficiency Porphyria (ADP)

## One-Sentence Summary

> Givosiran is an siRNA therapeutic used for acute hepatic porphyria (AHP), a group of inherited heme biosynthesis disorders.
> Among the TxGNN model's predictions, only **ALA dehydratase deficiency porphyria (ADP)** — a rare AHP subtype — shows a genuine mechanistic link and supporting clinical/literature evidence;
> the other nine top-ranked predictions (hepatoportal sclerosis, portal vein thrombosis, hepatopulmonary syndrome, HBV/HCV infection, etc.) are flagged in the evidence pack itself as model artifacts sharing only a "liver" graph node, with **no mechanistic basis and zero supporting studies**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute hepatic porphyria (AHP) — inferred from literature; no formal regulatory indication text available |
| Predicted New Indication | Porphyria due to ALA dehydratase deficiency (ADP) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Norway Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from a formal source is not available. Based on the literature evidence collected, givosiran is an siRNA therapeutic that silences hepatic **ALAS1** (5-aminolevulinic acid synthase 1) mRNA, reducing hepatic overproduction of the neurotoxic intermediates **ALA** and **PBG**. This mechanism is the basis for its approval in acute hepatic porphyria (AHP), a family of four genetic disorders — including acute intermittent porphyria, hereditary coproporphyria, variegate porphyria, and **ALA dehydratase deficiency porphyria (ADP)** — that share the same downstream pathology of ALAS1-driven ALA/PBG accumulation.

ADP is therefore not really a "new" indication in the biological sense, but an ultra-rare subtype within the AHP family that givosiran's mechanism directly targets. This explains why this candidate — unlike the model's top-ranked outputs — carries genuine mechanistic and clinical support (L2, Phase 3 ENVISION data, an ADP-specific case report).

**Important caveat on ranking:** the nine other TxGNN predictions in this evidence pack (ranks 1–8 and 10, including hepatoportal sclerosis, portal vein thrombosis, hepatopulmonary syndrome, HBV/HCV infection, phenylalanine metabolism disorder, etc.) were explicitly annotated in the source data as having **no mechanistic link** and **zero clinical trial or literature evidence** — they appear to score highly only because they share a "liver" node with givosiran in the knowledge graph. All were scored L5/S0/Hold. This report therefore focuses on the one prediction (ADP, rank 9) that passed a minimal plausibility screen; the higher-ranked predictions should not be pursued without independent mechanistic justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (the ENVISION Phase 3 trial for AHP broadly is referenced only via post-hoc literature analysis, not as a registered trial record in this evidence pack).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | RCT (Phase 3, ENVISION) | Orphanet J Rare Dis | Post-hoc analysis of the placebo-controlled ENVISION trial evaluating disease burden in AHP patients ≥12 years treated with givosiran |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Cohort/Clinical Study | Scientific Reports | Expanded access study in 10 Japanese AHP patients receiving monthly SC givosiran 2.5 mg/kg; efficacy and safety data |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | Cohort (real-world) | J Intern Med | RNAi therapy with givosiran significantly reduces attack rates in acute intermittent porphyria |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Review | Blood | Overview of RNA interference therapy mechanism (ALAS1 silencing) across the acute hepatic porphyrias |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Review | Revista Clinica Espanola | Therapeutic approach to acute crises of hepatic porphyrias, including ALA dehydratase deficiency subtype |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Review | Drug Des Devel Ther | Design, development, and therapeutic placement of givosiran in adult AHP |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK-PD Modeling | CPT: Pharmacometrics & Systems Pharmacology | PK-PD model of urinary ALA reduction after givosiran treatment, pooled Phase I-III data |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Case Report (non-response) | Frontiers in Genetics | Reports **lack of response** to givosiran in a confirmed ALAD porphyria (ADP) case — an important safety/efficacy caution signal |

---

## Norway Market Information

Givosiran is currently **not marketed in Norway** (0 authorizations on file). No product, dosage form, or approved-indication data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in the evidence pack — this is flagged as a **Blocking** data gap (DG001) that must be resolved before any safety review can proceed.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Givosiran's core mechanism (hepatic ALAS1 silencing) is directly relevant to ADP, and this link is supported by Phase 3 ENVISION disease-burden data plus multiple reviews of the ALAS1/ALA-PBG pathway. However, ADP is an ultra-rare AHP subtype with essentially no ADP-specific trial data, and the one published ADP case report shows **no clinical response** to givosiran — so the mechanistic rationale does not guarantee efficacy in this subgroup, and guardrails (e.g., trial-basis use with close monitoring) are warranted rather than a full "Go."

Separately, the nine other TxGNN-predicted indications in this evidence pack lack any mechanistic or evidentiary support and should be held (**Hold**) pending independent validation — they are not addressed further in this report.

**To proceed, the following is needed:**
- TFDA/regulatory-source label data (key warnings, contraindications, DDI) — currently blocking (DG001)
- Formal MOA documentation from DrugBank or equivalent primary source (DG002)
- ADP subgroup-specific efficacy/safety data beyond the single non-responder case report
- Norway market entry status and regulatory pathway assessment, since the drug is not currently marketed there
- A structured safety monitoring plan should off-label or expanded-access use in ADP be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

