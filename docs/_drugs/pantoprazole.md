---
layout: default
title: Pantoprazole
parent: 僅模型預測 (L5)
nav_order: 265
evidence_level: L5
indication_count: 6
---

# Pantoprazole
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

# Pantoprazole: From Gastroesophageal Reflux Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Pantoprazole is a proton pump inhibitor (PPI) originally used to treat gastroesophageal reflux disease (GERD) and erosive esophagitis.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
with **3 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastroesophageal reflux disease (GERD) / Erosive esophagitis *(from general PPI-class knowledge; no regulatory license text available for this market)* |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L1 |
| Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data (DrugBank MOA field) is flagged as a data gap. Based on the surrounding literature evidence, however, pantoprazole is a substituted benzimidazole proton pump inhibitor that **irreversibly and specifically binds to the H+/K+-ATPase** in gastric parietal cells, blocking the final step of gastric acid secretion. This mechanism is well documented across the retrieved publications (e.g. PMID 19938880, 9017763) and underlies its established efficacy in GERD and erosive esophagitis.

Gastric acid is the central pathogenic driver of peptic ulcer formation and impaired mucosal healing, so acid suppression by pantoprazole is directly applicable to active peptic ulcer disease. It is worth noting explicitly, per the repurposing rationale in the evidence pack, that this is **not a typical "new use" discovery** — peptic ulcer disease (together with H. pylori eradication co-therapy) is already a core, long-established indication for PPIs including pantoprazole. The TxGNN prediction here largely reconfirms a known pharmacological relationship rather than surfacing a genuinely novel indication, which should be kept in mind when interpreting the "repurposing" framing.

Nonetheless, the depth of trial and literature support (including head-to-head Phase 3 trials against other PPIs, and multiple H. pylori eradication triple-therapy RCTs) makes this the strongest-evidenced prediction among the candidates reviewed, and validates the model's ability to recover clinically true relationships.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02084420](https://clinicaltrials.gov/study/NCT02084420) | Phase 3 | Completed | 323 | Multicenter, randomized, double-blind, active-controlled trial comparing ilaprazole vs. pantoprazole triple therapy for H. pylori eradication in gastric/duodenal ulcer patients |
| [NCT02197039](https://clinicaltrials.gov/study/NCT02197039) | N/A | Completed | 316 | Identified risk factors predicting poor fading of stigmata of recent hemorrhage or early rebleeding after endoscopic hemostasis and high-dose PPI infusion in peptic ulcer bleeding |
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated influence of PPIs (including pantoprazole) and statins on clopidogrel antiplatelet effect in PCI patients on dual antiplatelet therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15244210](https://pubmed.ncbi.nlm.nih.gov/15244210/) | 2003 | RCT | Hepato-gastroenterology | Compared efficacy of lansoprazole vs. pantoprazole in active duodenal ulcer treatment and H. pylori eradication |
| [18824852](https://pubmed.ncbi.nlm.nih.gov/18824852/) | 2008 | RCT | Digestion | Prospective randomized study comparing intermittent vs. continuous pantoprazole infusion for peptic ulcer bleeding/rebleeding |
| [12752349](https://pubmed.ncbi.nlm.nih.gov/12752349/) | 2003 | RCT | Aliment Pharmacol Ther | Compared three pantoprazole-based triple therapies for H. pylori eradication and gastric ulcer healing |
| [16677158](https://pubmed.ncbi.nlm.nih.gov/16677158/) | 2006 | RCT | J Gastroenterol Hepatol | Prospective RCT of pantoprazole infusion as adjuvant therapy to endoscopic treatment in peptic ulcer bleeding |
| [19938880](https://pubmed.ncbi.nlm.nih.gov/19938880/) | 2009 | Review | Clinical Drug Investigation | Overview of pantoprazole pharmacology — irreversible H+/K+-ATPase binding, long duration of action, favorable interaction profile |
| [38652367](https://pubmed.ncbi.nlm.nih.gov/38652367/) | 2024 | Preclinical (animal) | Inflammopharmacology | Combined pantoprazole + mesenchymal stem cell treatment accelerated gastric ulcer healing in rats via reduced oxidative stress/inflammation/apoptosis |
| [10632647](https://pubmed.ncbi.nlm.nih.gov/10632647/) | 2000 | Clinical Study | Aliment Pharmacol Ther | Pantoprazole + amoxicillin + azithromycin/clarithromycin for H. pylori eradication in duodenal ulcer |
| [22919877](https://pubmed.ncbi.nlm.nih.gov/22919877/) | 2012 | Clinical Study | Med Arch (Sarajevo) | Efficacy of PPI after endoscopic hemostasis in bleeding peptic ulcer, and role of H. pylori |
| [9678814](https://pubmed.ncbi.nlm.nih.gov/9678814/) | 1998 | Clinical Study | Aliment Pharmacol Ther | Two-week pantoprazole + 1-week amoxicillin/clarithromycin effective for H. pylori eradication and duodenal ulcer healing |
| [11802510](https://pubmed.ncbi.nlm.nih.gov/11802510/) | 2001 | RCT | Wien Klin Wochenschr | RCT of amoxycillin + clarithromycin with sucralfate vs. pantoprazole for H. pylori eradication in duodenal ulcer |

---

## Market Information

Pantoprazole is currently **not marketed** in this jurisdiction (market status: 未上市), and no marketing authorization records are available in the regulatory dataset (`total_licenses = 0`).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level L1 (multiple completed Phase 3/4 trials plus RCTs directly evaluating pantoprazole in peptic ulcer disease and H. pylori eradication) strongly supports the efficacy signal. However, since this indication overlaps with pantoprazole's already-established core use rather than representing a genuinely novel repurposing target, and since key drug-level safety and regulatory data are missing, guardrails are needed before any formal indication expansion or market entry decision.

**To proceed, the following is needed:**
- Official product label warnings/contraindications (TFDA/local regulator equivalent) — currently a Blocking data gap (DG001)
- Formal DrugBank/manufacturer MOA documentation — currently a High-severity data gap (DG002)
- Local drug-drug interaction (DDI) data, since the current query returned no results
- Confirmation of local marketing authorization status and dosage forms before any market-entry planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

