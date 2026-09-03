---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 1
---

# Eltrombopag
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

# Eltrombopag: From Immune Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

> Eltrombopag is a thrombopoietin receptor (TPO-R) agonist, historically used to treat immune thrombocytopenia (ITP) and thrombocytopenia associated with chronic liver disease and hepatitis C.
> The TxGNN model predicts it may be effective for **HIV infectious disease**,
> with **5 clinical trials** and **9 publications** currently identified — though nearly all evidence relates to managing *HIV-associated thrombocytopenia* rather than HIV infection itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Immune thrombocytopenia (ITP) / thrombocytopenia in chronic liver disease — inferred from mechanism and literature context (Norway license data not available) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 (preclinical / mechanism-level evidence) |
| Norway Market Status | ✗ Not Marketed |
| Number of Authorizations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, eltrombopag is a thrombopoietin receptor (TPO-R) agonist that stimulates megakaryocyte proliferation and platelet production. Its efficacy in ITP is well established, and it has been used off-label for thrombocytopenia secondary to chronic infections (HCV, HIV, *H. pylori*).

The connection to HIV, however, is largely **indirect**: the bulk of clinical trial and literature evidence supports using eltrombopag to manage **thrombocytopenia that occurs as a complication of HIV infection** (including HIV-associated ITP and immune reconstitution inflammatory syndrome-related thrombocytopenia) — this is supportive/symptomatic management of a comorbidity, not antiviral treatment of HIV itself. One in vitro screening study (PMID 32977702) suggests eltrombopag may modulate HIV-1 proviral transcription, but this finding is preliminary, derived from an FDA-approved drug library screen, and has not been validated in cell culture models beyond the initial screen, animal models, or clinical trials.

The high TxGNN score (99.26%) likely reflects a strong "drug–thrombocytopenia–HIV comorbidity" path in the knowledge graph rather than a genuine antiviral mechanism. The predicted indication label "HIV infectious disease" may therefore be **imprecise** — the more accurate and evidence-supported indication would be "HIV-associated thrombocytopenia."

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Eltrombopag to reduce need for platelet transfusion in chronic liver disease patients with thrombocytopenia undergoing invasive procedures; not HIV-specific |
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Open-label rollover study assessing safety of eltrombopag to maintain platelet counts enabling HCV antiviral therapy initiation; not HIV-specific |
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | SB-497115-GR (eltrombopag) raising platelet counts in HCV-related thrombocytopenia with compensated cirrhosis; not HIV-specific |
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | Eltrombopag vs placebo maintaining platelet counts to enable HCV antiviral therapy (Peg-IFN α-2b + ribavirin); SVR as endpoint; not HIV-specific |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | Eltrombopag vs placebo maintaining platelet counts to enable HCV antiviral therapy (Peg-IFN α-2a + ribavirin); SVR as endpoint; not HIV-specific |

**Note:** All five trials were graded "C" relevance by evidentiary review — none directly enrolled or targeted HIV-infected populations or antiviral endpoints; they primarily address ITP/HCV-related thrombocytopenia, which is eltrombopag's established use.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Review | Hematology/Oncology Clinics of North America | Chronic infections (HCV, HIV, *H. pylori*) as causes of secondary/chronic ITP; treating the underlying infection often improves thrombocytopenia |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Review | Seminars in Hematology | Therapeutic strategies for infection-related immune thrombocytopenia, including HCV and HIV |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Review | Internal Medicine Journal | TPO-receptor agonists in ITP of less than 6 months' duration |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Cohort | Platelets | Danish real-world experience with TPO-receptor agonists in refractory ITP, including secondary ITP cases |
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case series | J Int Assoc Provid AIDS Care | TPO-receptor agonists (eltrombopag, romiplostim) as salvage therapy in refractory HIV-associated ITP after HAART optimization |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case report | J Coll Physicians Surg Pak | Hepatitis B leading to megaloblastic anemia and severe thrombocytopenia (not HIV; adjacent infectious-thrombocytopenia context) |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case report | AIDS | Successful use of eltrombopag without splenectomy in refractory HIV-related immune reconstitution thrombocytopenia |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case report | AIDS | Eltrombopag successfully treated aplastic anaemia associated with HIV infection; noted possible immunomodulatory role (↓Th1/Th17, ↑Treg/Th ratio) |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case report | Farmacia Hospitalaria | Two case reports of eltrombopag for thrombocytopenia in chronic hepatitis C |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In vitro screening | Viruses | Screen of FDA-approved drug library identifies potential modulators of HIV-1 proviral transcription; preliminary, mechanism unconfirmed |

---

## Norway Market Information

Eltrombopag is currently **not marketed in Norway**, and no product authorizations were found in the available data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence overwhelmingly supports eltrombopag's established use in managing thrombocytopenia that arises as a complication of HIV infection, rather than treating HIV infection directly. The single mechanistic lead for a direct antiviral effect (in vitro HIV-1 transcription screen) is unvalidated. The predicted indication label likely overstates the actual evidentiary link, and the drug is not currently marketed in Norway.

**To proceed, the following is needed:**
- TFDA/Norwegian package insert data (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Clarification/re-labeling of the predicted indication to "HIV-associated thrombocytopenia" to align with existing evidence, or dedicated preclinical/clinical validation of the direct antiviral (proviral transcription) mechanism before considering this a genuine HIV-treatment repurposing candidate
- Assessment of Norway market entry pathway, given current unmarketed status and zero existing authorizations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

