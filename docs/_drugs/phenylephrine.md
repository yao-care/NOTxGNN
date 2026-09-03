---
layout: default
title: Phenylephrine
parent: 僅模型預測 (L5)
nav_order: 277
evidence_level: L5
indication_count: 3
---

# Phenylephrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Using the report template you provided — this is a straightforward document-generation task, no engineering/debugging skill applies, so I'm producing the deliverable directly.

---

# Phenylephrine: From Nasal Decongestant to Nasal Cavity Disease

## One-Sentence Summary

Phenylephrine is a selective α1-adrenergic receptor agonist most widely used clinically as a topical nasal/ocular decongestant and as a vasopressor. The TxGNN model predicts it may be formally effective for **Nasal Cavity Disease**, with **8 clinical trials** and **8 publications** currently supporting this direction — though the evidence largely documents phenylephrine's *already established* decongestant use rather than a novel therapeutic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Norway regulatory data (no marketed license); pharmacologically established as a nasal/ocular decongestant and vasopressor |
| Predicted New Indication | Nasal Cavity Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, DrugBank's formal mechanism-of-action field for phenylephrine is a data gap in this evidence pack. Based on well-established pharmacology captured in the repurposing rationale, phenylephrine is a **selective α1-adrenergic receptor agonist** that acts on vascular smooth muscle in the nasal mucosa, producing vasoconstriction that reduces mucosal congestion and edema — the classical decongestant mechanism.

This is not so much a novel repurposing hypothesis as a **consolidation of already-documented clinical use**: phenylephrine (alone or in combinations such as Cophenylcaine, Kovanaze, and Polydexa) is routinely used before nasoendoscopy, sinus surgery, and other nasal/ENT procedures to shrink mucosa and improve visualization and comfort. The predicted indication "Nasal Cavity Disease" therefore aligns tightly with existing off-label/adjunct practice rather than requiring mechanistic extrapolation.

This is why the evidence level here (L2) is meaningfully stronger than the other two candidate indications identified for this drug in the same evidence pack — acute laryngopharyngitis (L5, no trials/literature) and trigeminal autonomic cephalalgia (L4, phenylephrine used only as a diagnostic pupillometry reagent, not a treatment). For nasal cavity disease, the mechanism is direct, well-precedented, and supported by an actual Phase 2 RCT.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562120](https://clinicaltrials.gov/study/NCT00562120) | Phase 2 | Completed | 21 | Double-blind, 4-way crossover RCT testing an H3-antagonist vs. nasal decongestant therapy on allergen-induced nasal congestion; most direct comparative evidence for this indication (Grade A) |
| [NCT03380715](https://clinicaltrials.gov/study/NCT03380715) | N/A | Completed | 106 | Co-phenylcaine (contains phenylephrine) nasal spray vs. nebulization for mucosal decongestion/anesthesia before rigid nasoendoscopy |
| [NCT04104789](https://clinicaltrials.gov/study/NCT04104789) | Phase 2 | Withdrawn | 0 | Kovanaze (phenylephrine/tetracaine) nasal mist vs. articaine injection for maxillary pulpal anesthesia; trial withdrawn, no data generated |
| [NCT03962634](https://clinicaltrials.gov/study/NCT03962634) | Phase 2 | Terminated | 3 | Same Kovanaze vs. articaine comparison; terminated early with negligible enrollment |
| [NCT03228914](https://clinicaltrials.gov/study/NCT03228914) | Phase 4 | Completed | 20 | Compares oxymetazoline vs. epinephrine (not phenylephrine) for preoperative sinus surgery decongestion; indirect α-agonist class reference only |
| [NCT02993770](https://clinicaltrials.gov/study/NCT02993770) | N/A | Unknown | 120 | Endoscopic vs. external dacryocystorhinostomy surgical technique comparison; not a direct phenylephrine intervention trial |
| [NCT06457100](https://clinicaltrials.gov/study/NCT06457100) | Phase 1/2 | Active, not recruiting | 60 | Esmolol vs. lidocaine infusion for recovery quality after functional endoscopic sinus surgery; phenylephrine not the studied agent |
| [NCT06443255](https://clinicaltrials.gov/study/NCT06443255) | Phase 3 | Completed | 16 | Compares cocaine, lidocaine/xylometazoline, and saline for intranasal analgesia during awake nasotracheal intubation; phenylephrine arm not included |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15854186](https://pubmed.ncbi.nlm.nih.gov/15854186/) | 2005 | RCT | Int J Clin Pract | Double-blind RCT of cophenylcaine spray (phenylephrine-containing) vs. placebo before flexible nasendoscopy; minimal pain/discomfort in both arms |
| [40899890](https://pubmed.ncbi.nlm.nih.gov/40899890/) | 2025 | RCT/experimental | Vestnik otorinolaringologii | Safety/efficacy evaluation of Polydexa nasal spray with phenylephrine in acute rhinosinusitis |
| [25133491](https://pubmed.ncbi.nlm.nih.gov/25133491/) | 2014 | RCT | PLoS One | Triple-blind RCT on topical tranexamic acid for bleeding/surgical field quality during FESS in chronic rhinosinusitis (adjunct nasal-cavity surgery context) |
| [37184554](https://pubmed.ncbi.nlm.nih.gov/37184554/) | 2023 | Review | Vestnik otorinolaringologii | Endoscopic mucosal assessment after topical antibiotic therapy including Polydexa with phenylephrine for granulomatosis with polyangiitis |
| [37970776](https://pubmed.ncbi.nlm.nih.gov/37970776/) | 2023 | Review | Vestnik otorinolaringologii | Pathogenesis-based treatment approach for inflammatory diseases of nose and paranasal sinuses |
| [9780066](https://pubmed.ncbi.nlm.nih.gov/9780066/) | 1998 | Cohort | Int J Pediatr Otorhinolaryngol | Acoustic rhinometry of nasal cavity/nasopharynx geometry after adenotonsillectomy |
| [7378007](https://pubmed.ncbi.nlm.nih.gov/7378007/) | 1980 | Case report | Arch Ophthalmol | Cocaine and intranasal phenylephrine toxicity during dacryocystorhinostomy; highlights sympathomimetic interaction risk |
| [1375136](https://pubmed.ncbi.nlm.nih.gov/1375136/) | 1992 | In vitro / mechanism | Clin Otolaryngol Allied Sci | Dose-dependent effects of nasal drugs, including phenylephrine, on ciliary beat frequency in vitro |

---

## Norway Market Information

No marketed authorizations were found for phenylephrine in Norway under this evidence pack (`total_licenses = 0`). The drug is currently classified as **未上市 / Not marketed**, so no product-level license table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are all marked as data gaps in this evidence pack — notably flagged as a **Blocking** gap (DG001: TFDA label warnings/contraindications) that prevents completion of the S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis is strong and non-novel — phenylephrine's decongestant effect on nasal mucosa is pharmacologically well-established and already reflected in real-world adjunct use (Cophenylcaine, Kovanaze, Polydexa) — and one Phase 2 crossover RCT (NCT00562120) provides direct comparative evidence, supporting an L2 evidence level. However, the drug is not currently marketed in this jurisdiction and a **blocking** safety data gap (TFDA/label warnings and contraindications) remains unresolved, so full clinical adoption cannot proceed without further data.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the official product label for warnings/contraindications before any S1 safety assessment
- Resolve DG002 (High): confirm formal DrugBank/regulatory MOA documentation
- Clarify route/dosage-form compatibility for the "nasal cavity disease" indication (intranasal spray vs. combination formulations)
- Assess regulatory pathway feasibility given the drug currently has zero marketed licenses in this jurisdiction

**Note on other predicted indications:** Two additional candidates for phenylephrine were assessed in this evidence pack — acute laryngopharyngitis (L5, no supporting trials or literature, **Hold**) and trigeminal autonomic cephalalgia (L4, phenylephrine used only as a diagnostic pupillometry reagent for cluster headache/Horner's differentiation, not as treatment, **Hold**). Neither is recommended for further action at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

