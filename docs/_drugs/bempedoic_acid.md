---
layout: default
title: Bempedoic Acid
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Bempedoic Acid
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

# Bempedoic Acid: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Bempedoic acid is an ATP-citrate lyase (ACL) inhibitor used to lower LDL-cholesterol in patients with hypercholesterolemia/atherosclerotic cardiovascular disease who need additional LDL-C reduction beyond statins.
> Among the TxGNN-predicted indications, the top-ranked candidate (**hyperthyroidism**, score 99.61%) was reviewed and found to have **no credible mechanistic or literature support** — it is flagged as likely model noise.
> The strongest evidence-backed candidate is **Homozygous Familial Hypercholesterolemia (HoFH)**, supported by **1 real-world cohort study and 17 supporting publications**, reaching Evidence Level **L3**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in the regulatory dataset (drug not marketed locally); literature confirms established use as an LDL-C–lowering agent for hypercholesterolemia / ASCVD risk reduction, used alongside statins, ezetimibe, and PCSK9 inhibitors |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.48% (rank #6 among predictions; rank #1 "hyperthyroidism" excluded — see note below) |
| Evidence Level | L3 |
| Market Status | Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on TxGNN ranking:** The single highest TxGNN score (hyperthyroidism, 99.61%) was cross-checked against its supporting literature and found to reference an unrelated drug (tiratricol) with no mechanistic connection to bempedoic acid. Ranks #2–5, #7–10 (thyroid hormone resistance, malignant catarrh, bovine rhinotracheitis, CMV infection, hyperthyroxinemia, drug-induced osteoporosis, MEN, pregnancy-associated osteoporosis) similarly have zero supporting evidence and no plausible mechanism. This report therefore focuses on the one candidate with real evidentiary support: HoFH.

---

## Why is This Prediction Reasonable?

Bempedoic acid inhibits ATP-citrate lyase (ACL), an enzyme upstream of HMG-CoA reductase in the hepatic cholesterol biosynthesis pathway. It is a prodrug activated by ACSVL1, an enzyme expressed almost exclusively in the liver and absent in skeletal muscle — this liver-restricted activation is why bempedoic acid does not carry the same myopathy risk as statins. ACL inhibition upregulates hepatic LDL receptor (LDLR) expression and lowers LDL-C independently of, and additively to, statin therapy.

HoFH is a rare genetic disorder in which LDLR function is severely or completely deficient, producing extremely elevated LDL-C and early-onset atherosclerotic cardiovascular disease. Because LDLR function is so impaired, HoFH management typically requires combination therapy (statins, ezetimibe, PCSK9 inhibitors, evinacumab, lomitapide) to achieve any meaningful LDL-C reduction. Bempedoic acid's LDLR-upregulating, largely LDLR-independent mechanism makes it mechanistically plausible as an *add-on* agent in this population, and a 2026 real-world cohort study (PMID 41274797) already reports its use specifically in HoFH patients.

This is best understood not as a novel disease-area repurposing, but as an **indication extension within the same lipid-disorder therapeutic space** the drug already occupies — which is a much lower-risk, higher-plausibility form of repurposing than the noise-driven candidates elsewhere in the TxGNN output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for HoFH.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41274797](https://pubmed.ncbi.nlm.nih.gov/41274797/) | 2026 | Cohort (real-world) | J Clin Lipidol | Direct real-world evaluation of bempedoic acid efficacy/tolerability specifically in HoFH patients |
| [41741298](https://pubmed.ncbi.nlm.nih.gov/41741298/) | 2026 | Expert consensus | J Clin Lipidol | National Lipid Association update on FH management, incorporating current LDL-C-lowering options |
| [41694628](https://pubmed.ncbi.nlm.nih.gov/41694628/) | 2026 | Case report + review | Clin Case Rep | Illustrates consequences of interrupted HoFH follow-up; reviews aggressive LDL-C-lowering strategies |
| [41106315](https://pubmed.ncbi.nlm.nih.gov/41106315/) | 2025 | Review | Exp Mol Pathol | Reviews innovative HoFH therapies including non-statin LDL-C-lowering agents |
| [35466160](https://pubmed.ncbi.nlm.nih.gov/35466160/) | 2022 | Review | J Atheroscler Thromb | Reviews advancements in HoFH treatment, positioning bempedoic acid among newer options |
| [37071085](https://pubmed.ncbi.nlm.nih.gov/37071085/) | 2024 | Review | Cardiol Rev | Discusses evinacumab and other add-on therapies (incl. bempedoic acid) for HoFH |
| [29449335](https://pubmed.ncbi.nlm.nih.gov/29449335/) | 2018 | Preclinical (animal model) | Arterioscler Thromb Vasc Biol | Bempedoic acid lowers LDL-C and attenuates atherosclerosis in LDLR-deficient miniature pigs — direct mechanistic support for LDLR-independent benefit |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | Reviews emerging LDL-C/ApoB-lowering therapies including bempedoic acid alongside PCSK9i and inclisiran |
| [38576462](https://pubmed.ncbi.nlm.nih.gov/38576462/) | 2024 | Review | Am J Prev Cardiol | Emphasizes cumulative LDL-C exposure as ASCVD driver, supporting rationale for maximal LDL-C reduction in high-risk groups like HoFH |
| [32243228](https://pubmed.ncbi.nlm.nih.gov/32243228/) | 2020 | Review | Postgrad Med | Reviews emerging LDL-C-lowering agents including bempedoic acid's mechanism and clinical positioning |

---

## Norway Market Information

This drug is **not currently marketed** in the evaluated jurisdiction (0 authorizations on file); no license records are available to summarize approved indications or dosage forms.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A mechanistically plausible, LDLR-independent LDL-C-lowering effect is supported by preclinical data in an LDLR-deficient animal model and a real-world clinical cohort specifically in HoFH patients, but no dedicated randomized controlled trial in HoFH exists yet — evidence is promising but not conclusive (L3).

**To proceed, the following is needed:**
- Official mechanism of action (MOA) documentation from the regulatory label/DrugBank (currently flagged as Data Gap, DG002)
- Local regulatory label warnings, contraindications, and DDI data (currently flagged as Blocking Data Gap, DG001) — required before any safety-based decision can be finalized
- A dedicated prospective or randomized trial evaluating bempedoic acid as add-on therapy in HoFH
- Local market authorization pathway assessment, since the drug is not currently marketed in this jurisdiction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

