---
layout: default
title: Rilpivirine
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 5
---

# Rilpivirine
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

# Rilpivirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

> Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally developed for HIV-1 infection in humans.
> The TxGNN model's top-ranked prediction is **feline acquired immunodeficiency syndrome** — a veterinary disease caused by feline immunodeficiency virus (FIV), not a human indication —
> and this is currently supported by only **1 in vitro structural study** and **no clinical trials**.

⚠️ **Note on this candidate**: The #1-ranked TxGNN prediction in this evidence pack targets a **veterinary disease (cats)**, not a human condition. This is flagged as a likely low-value or off-target model output and is scored `Hold` in the evidence pack itself. Human-relevant candidates with much stronger evidence exist further down the same prediction list (see Conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (NNRTI; inferred from evidence pack literature/rationale — no formal Norway label text available) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome (FIV infection in cats) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Norway Market Status | ✗ Not marketed (未上市) |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (`original_moa: [Data Gap]`). Based on information available in the supporting literature, rilpivirine is a diarylpyrimidine-class NNRTI that binds the HIV-1 reverse transcriptase (RT) enzyme, non-competitively blocking viral replication. Its efficacy in HIV-1 infection is well established, including in long-acting injectable combination form with cabotegravir.

The predicted new indication — feline immunodeficiency virus (FIV)-related syndrome — is mechanistically adjacent only in the broadest sense: FIV is also a lentivirus with a reverse transcriptase enzyme, so an NNRTI could in theory interfere with viral replication. However, FIV RT and HIV-1 RT are structurally distinct, and the single available study is a **biochemical/structural comparison**, not a functional antiviral efficacy study.

Per the evidence pack's own rationale: *"僅有單一生化/結構比較研究，分析 NNRTI 對貓免疫缺陷病毒(FIV) RT 之結合特性；FIV RT 與 HIV-1 RT 結構差異顯著，交叉活性未經功能性驗證，屬獸醫學範疇而非人類藥物再利用標的。"* In short, cross-species binding was studied structurally but never confirmed functionally, and the target species is not human — this is why the evidence pack itself assigns `Evidence Level L4` and `Decision Stage S0 / Hold`.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro structural study | Journal of Veterinary Science | Compared biochemical/structural binding of NNRTIs (nevirapine, efavirenz, rilpivirine) against feline vs. human immunodeficiency virus reverse transcriptase, exploring theoretical potential of NNRTIs for FIV treatment in cats; no in vivo or clinical efficacy data reported. |

---

## Norway Market Information

No authorization records found — rilpivirine is not currently marketed in Norway (`total_licenses: 0`, `licenses: []`).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack; DDI query returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction targets a veterinary condition (feline AIDS/FIV) rather than a human disease, is supported by only one preclinical structural-comparison paper with no functional or clinical validation, and is already self-scored `L4 / Hold` in the evidence pack. This candidate does not meet the bar for human drug repurposing evaluation.

**To proceed, the following is needed:**
- If pursuing this candidate specifically: functional antiviral efficacy data of rilpivirine against live FIV (in vitro or in vivo), and confirmation of veterinary regulatory pathway relevance (likely out of scope for a human repurposing program).
- **Recommended alternative**: re-scope this evaluation to rank 4 (`AIDS related complex`, L2, Proceed with Guardrails) or rank 5 (`congenital HIV` — actually reflects CAB/RPV LA use in pregnant women with HIV, L2, Research Question), both of which have multiple Phase 3 trials and are within rilpivirine's actual human disease area.
- Resolve blocking data gaps: **DG001** (TFDA/Norway label warnings & contraindications — Blocking, required before any S1 safety review) and **DG002** (formal MOA from DrugBank — High priority).
- Manually re-verify TxGNN disease-label mapping for rank 5 ("congenital human immunodeficiency virus"), as the underlying trial/literature evidence actually concerns maternal-fetal pharmacokinetics rather than a distinct congenital-HIV indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

