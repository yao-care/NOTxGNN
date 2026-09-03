---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 231
evidence_level: L5
indication_count: 1
---

# Midazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine established for procedural sedation, anesthesia induction, and status epilepticus. The TxGNN model predicts it may also be effective for **Insomnia**, a signal supported by **32 screened clinical trials** and **11 curated publications**, several of which are decades-old randomized controlled trials that already demonstrated oral midazolam's efficacy as a short-term hypnotic.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Norway license data (drug unmarketed); internationally established for procedural sedation, anesthesia induction, and status epilepticus |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The evidence pack's `original_moa` field is a data gap, but the repurposing rationale supplied with the prediction fills this in: midazolam is a short-acting benzodiazepine that potentiates GABA-A receptor-mediated chloride channel conductance, producing sedative, anxiolytic, and hypnotic effects. This places it in the same pharmacological family as established hypnotics such as flurazepam and zolpidem — the mechanistic link to insomnia is direct and well-characterized, not a novel hypothesis.

Notably, this is less a case of genuine "drug repurposing" and more a re-surfacing of a previously validated use. Oral midazolam was already marketed in several European countries during the 1980s–1990s specifically as a short-term treatment for insomnia, before falling out of favor relative to newer hypnotics. The TxGNN prediction is therefore consistent with historical clinical precedent rather than an unproven mechanistic extrapolation.

Because midazolam's sedative/anesthetic use and its historical hypnotic use share the identical GABA-A mechanism, the biological plausibility for insomnia is high. The main open question is not "does it work" (older RCTs already answered that) but whether it remains a *competitive* option given modern hypnotics with better next-day safety profiles.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Dexmedetomidine vs. midazolam compared for postoperative sleep quality after TURP under spinal anesthesia; directly measures midazolam's effect on sleep outcomes (Grade B). |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Phase 3 | Unknown | 120 | Dexmedetomidine vs. midazolam sedation efficacy in critically ill ventilated children; benzodiazepine-related agitation/delirium as comparator endpoint. |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Phase 4 | Unknown | 285 | Remimazolam (benzodiazepine analog) vs. standard sedation in ICU mechanical ventilation post-maxillofacial surgery. |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | 24-hour polysomnography comparing dexmedetomidine vs. midazolam on sleep quality/quantity and delirium incidence in ICU patients. |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic comparison of α2-agonist vs. GABA-agonist (midazolam-class) sedation on sleep staging and total sleep time. |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Phase 3 | Not yet recruiting | 195 | Oral melatonin vs. oral midazolam as premedication in children undergoing tonsillectomy, framed around sleep-inducing effect. |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Recruiting | 280 | Preoperative oral midazolam evaluated in patients with sleep disturbance/anxiety undergoing colorectal cancer surgery; oral midazolam solution noted as "safe and effective for short-term hypnosis." |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | N/A | Completed | 23 | Dexmedetomidine vs. midazolam for facilitating ICU extubation, comparing benzodiazepine sedation transition. |
| [NCT01343095](https://clinicaltrials.gov/study/NCT01343095) | N/A | Terminated | 8 | ICU noise-reduction trial measuring sedative medication use and sleep quality as secondary endpoints (indirect overlap only). |
| [NCT06498869](https://clinicaltrials.gov/study/NCT06498869) | N/A | Completed | 178 | Ketamine's effect on sleep quality (PSQI) in colonoscopy patients; midazolam used as part of baseline sedation regimen. |

*Note: The majority of the 32 screened trials study midazolam in perioperative/ICU sedation contexts rather than chronic insomnia treatment; only the trials above have direct relevance graded (B/C) or explicit sleep/insomnia framing.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Double-blind trial: midazolam 15mg vs. Vesparax in 30 patients with insomnia secondary to neuromuscular disease; midazolam was an effective hypnotic, better tolerated, no hangover effect. |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | 14-day multicenter RCT comparing flurazepam and midazolam in chronic insomniacs, assessing sleep, performance, and plasma levels. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Executive summary companion to the above multicenter chronic-insomnia RCT of flurazepam vs. midazolam. |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT | Arzneimittel-Forschung | Dose-finding pilot study (10–30mg oral) in 75 hospitalized patients with mild-to-moderate insomnia; established optimal dosing range for midazolam as a hypnotic. |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | RCT | Journal of Clinical Medicine | Notes benzodiazepines (incl. midazolam) traditionally used for insomnia but may increase delirium risk; evaluates lemborexant as an alternative in high-risk sedation patients. |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Review | Orvosi Hetilap | General review of insomnia pathogenesis (primary vs. secondary) and hyperarousal state. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | Review of benzodiazepine hypnotics' clinical use, pharmacokinetic/pharmacodynamic differentiation, and rationale for a variety of agents. |
| [22729271](https://pubmed.ncbi.nlm.nih.gov/22729271/) | 2013 | Other | Psychopharmacology | Preclinical/behavioral study of zolpidem's sedative and memory effects (comparator hypnotic class, not midazolam-specific). |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Preclinical | Pain | Mouse model showing neuropathic pain-associated insomnia linked to altered GABAergic transmission — supports GABA-mechanism relevance to insomnia broadly. |
| [36912148](https://pubmed.ncbi.nlm.nih.gov/36912148/) | 2024 | Cohort | American Journal of Hospice & Palliative Care | Case-based report on symptom management including sedatives at end of life in COVID-19 patients (indirect relevance). |

---

## Norway Market Information

Midazolam is **not currently marketed in Norway** — the evidence pack contains zero authorization records (`total_licenses: 0`). No product name, dosage form, or approved indication text is available from the local regulator.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The evidence pack flags a **Blocking** data gap (DG001) for TFDA-equivalent label warnings/contraindications, which currently prevents this candidate from clearing the S1 safety pre-screen. This must be resolved before formal safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is strong and historically validated — oral midazolam was clinically proven effective for insomnia in multiple RCTs (1981–1990) and was even marketed for this use in Europe. However, most supporting evidence is decades old, small-scale, and the drug is currently unmarketed in Norway with a **blocking data gap** on label safety information (warnings/contraindications), so guardrails are required before advancing.

**To proceed, the following is needed:**
- TFDA/local package insert data (warnings, contraindications) — resolves blocking gap DG001
- Formal drug-drug interaction (DDI) data (currently `not_found`)
- Structured original MOA and original-indication documentation for the regulatory dossier — resolves gap DG002
- A market-entry regulatory pathway assessment, since midazolam holds zero authorizations in Norway
- Contemporary comparative-effectiveness data against modern hypnotics (e.g., zolpidem, lemborexant), given most positive insomnia trials predate current standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

