---
layout: default
title: Desloratadine
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 6
---

# Desloratadine
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

# Desloratadine: From Antihistamine Use (Original Indication Not Recorded) to Cold Urticaria

## One-Sentence Summary

Desloratadine's original indication data was not provided in this evidence pack (the drug is not currently marketed in Norway, and no license-based indication text is available), but it is documented as a second-generation, long-acting H1-antihistamine. The TxGNN model predicts it may be effective for **Cold Urticaria**, with **3 Phase 4 clinical trials** and **7 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded — no Norway license data or listed original indications in this evidence pack |
| Predicted New Indication | Cold Urticaria |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data from DrugBank is not available for desloratadine (flagged as a High-severity data gap). Based on the evidence provided in this pack, desloratadine is described as a long-acting, selective peripheral H1-receptor antagonist — the active metabolite of loratadine. It inhibits cold-stimulus-triggered mast cell degranulation and histamine release, which is the central pathological mechanism underlying cold urticaria.

Second-generation H1-antihistamines are already recommended as first-line therapy for cold urticaria under international guidelines (e.g., EAACI/GA²LEN/EDF), and desloratadine is one of the agents used in this class. This mechanistic link — rather than a formal comparison between a documented original indication and a new one — is what underlies the TxGNN prediction, since Norway regulatory/licensing data for this compound is not currently available (market status: Not Marketed).

Because the drug is unmarketed in Norway, no independent local indication text exists to compare against; the strength of this prediction therefore rests primarily on the clinical trial and literature evidence summarized below rather than on precedent from an approved original indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Phase 4 | Completed | 30 | Dose-escalation study (5/10/20 mg) assessing the dose of desloratadine sufficient to inhibit cold urticaria symptoms |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Phase 4 | Completed | 33 | Randomized, double-blind, placebo-controlled crossover study comparing 5 mg vs. 20 mg desloratadine on experimentally induced cold urticaria lesions; hypothesis that updosing (20 mg) is more effective than standard dose |
| [NCT01940393](https://clinicaltrials.gov/study/NCT01940393) | Phase 4 | Completed | 150 | Evaluation of the inhibitory effect of 5 antihistamines (including desloratadine) in urticaria, including cold-induced forms |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatolog Treat | 5 mg desloratadine for 4 days significantly inhibited ice-cube-induced cold urticaria reactions in 12 patients |
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | High-dose desloratadine decreased wheal volume and improved cold provocation thresholds vs. standard dose in acquired cold urticaria (randomized, placebo-controlled crossover) |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Randomized controlled trial of H1-antihistamine dose escalation measuring critical temperature threshold in cold urticaria |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Review | Drugs | Review of chronic urticaria aetiology and management, including antihistamine treatment options |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Review | Allergy | Review of second-generation antihistamines (ebastine) in allergic rhinitis and chronic idiopathic urticaria, contextualizing antihistamine efficacy in urticarial disease |
| [29698807](https://pubmed.ncbi.nlm.nih.gov/29698807/) | 2018 | Case Series | J Allergy Clin Immunol Pract | Description of food-dependent cold urticaria as a new physical urticaria variant |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Case Report | Qatar Med J | Case report of cold-induced urticaria following black ant bite-induced anaphylaxis |

---

## Norway Market Information

Desloratadine is currently not marketed in Norway — no license records are available in the regulatory dataset (total authorizations: 0).

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data were not available in this evidence pack; TFDA-equivalent labeling review is flagged as a Blocking data gap.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 4 randomized/controlled trials and consistent supporting literature (including three RCTs) demonstrate a dose-dependent inhibitory effect of desloratadine on cold urticaria symptoms, meeting the L1 evidence threshold. However, the drug is not currently marketed in Norway and lacks basic safety labeling data, so guardrails are needed before proceeding.

**To proceed, the following is needed:**
- TFDA-equivalent package insert data (warnings/contraindications) — currently a Blocking data gap
- Confirmed drug-drug interaction (DDI) profile
- DrugBank-sourced mechanism of action documentation to formally support the mechanistic rationale
- Norway market entry/regulatory filing status, or an alternative reference market's approved indication text, to establish a documented "original indication" baseline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

