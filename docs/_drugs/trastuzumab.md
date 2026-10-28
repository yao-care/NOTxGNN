---
layout: default
title: Trastuzumab
parent: Kun modellprediksjon (L5)
nav_order: 431
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
description: "Trastuzumab: predikert ny indikasjon Malignant cutaneous granular cell skin tumor (evidensnivå L5). Opprinnelig indikasjon: Stomach Neoplasms"
---

# Trastuzumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Trastuzumab: Malignant cutaneous granular cell skin tumor
{: .text-alpha }

## Én-setnings sammendrag

Trastuzumab er et monoklonalt antistoff mot HER2, opprinnelig brukt til behandling av **brystkreft og magekreft**.
TxGNN-modellen predikerer at det kan ha effekt ved **progesteronreseptor-positiv brystkreft**, men dette ligger innenfor den eksisterende brystkreftindikasjonen og er ikke en reell ny bruk.
Funnet støttes av **12 kliniske studier** og **20 publikasjoner** i de data som er sammenstilt for denne rapporten. Nytten gjelder bare HER2-positiv sykdom.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Stomach Neoplasms;Breast Neoplasms; Breast Neoplasms;Stomach Neoplasms; Breast Neoplasms |
| Predikert ny indikasjon | Malignant cutaneous granular cell skin tumor |
| TxGNN-prediksjonsscore | 0.9948 |
| Evidensnivå | L5 |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 11 av 11) |
| Antall godkjenninger | 11 (gyldige: 11) |
| Antall tillatelser | 11 (alle avregistrert) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med sikkerhetstiltak) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Basert på kjent informasjon binder trastuzumab seg til det ekstracellulære domenet til HER2, blokkerer signalering og medierer antistoffavhengig cellulær cytotoksisitet (ADCC).

Svulster som er både PR-positive og HER2-positive har nytte av trastuzumab. Kombinasjon med endokrin behandling adresserer samspillet mellom HER2- og hormonreseptorveiene. Dette ligger innenfor den allerede godkjente brystkreftindikasjonen, så det er ikke en ekte repurposing.

Nytten er begrenset til HER2-positiv sykdom, og HER2-testing er nødvendig. Prediksjonen bør derfor leses som en bekreftelse av kjent bruk, ikke som en ny terapeutisk mulighet.

---

## Dokumentasjon fra kliniske studier

Utvalg av de mest relevante studiene for progesteronreseptor-positiv brystkreft:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Fase 3 | Fullført | 3270 | Randomisert adjuvant studie: kjemoterapi alene mot kjemoterapi pluss trastuzumab ved brystkreft. Direkte evidens |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Fase 3 | Fullført | 517 | Pertuzumab-biosimilar (QL1209) mot pertuzumab, begge med trastuzumab og docetaxel, ved HER2-positiv, ER/PR-negativ brystkreft |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Fase 2 | Fullført | 92 | Neoadjuvant kjemoterapi med og uten trastuzumab |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Fase 2 | Fullført | 50 | Neoadjuvant kjemoterapiregime inkludert trastuzumab ved HER2-positiv brystkreft |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Fase 1 | Fullført | 37 | Everolimus, letrozol og trastuzumab ved hormonreseptor- og HER2-positiv avansert brystkreft |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Fase 2 | Fullført | 36 | Kabozantinib alene eller med trastuzumab ved hjernemetastaser |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Fase 2 | Ukjent | 34 | Palbociklib, trastuzumab, pyrotinib og fulvestrant ved hjernemetastaser (ER/PR+, HER2+) |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Fase 2 | Fullført | 33 | Letrozol pluss trastuzumab ved ErbB2-positiv, ER/PR-positiv metastatisk brystkreft |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Fase 2 | Rekrutterer | 30 | Preoperativ neratinib og endokrin behandling med trastuzumab ved ER-positiv, HER2-positiv kreft |
| [NCT05868226](https://clinicaltrials.gov/study/NCT05868226) | Fase 1/2 | Rekrutterer | 280 | Plattformstudie for prediksjon av behandlingsrespons; indirekte relevans |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Fase 3 | Trukket tilbake | 0 | Trastuzumab med eller uten tamoxifen; ingen data da studien ikke ble gjennomført |
| [NCT02774681](https://clinicaltrials.gov/study/NCT02774681) | Fase 2 | Avsluttet | 12 | Palbociklib ved HER2-positiv brystkreft med hjernemetastaser; begrensede data |

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [16236738](https://pubmed.ncbi.nlm.nih.gov/16236738/) | 2005 | RCT | N Engl J Med | Adjuvant kjemoterapi med eller uten trastuzumab ved operabel HER2-positiv brystkreft (kun listet under luminal A/B) |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | Lancet Oncol | NeoSphere: 5-årsanalyse av neoadjuvant pertuzumab og trastuzumab ved HER2-positiv brystkreft |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncol | monarcHER: abemaciklib pluss trastuzumab ± fulvestrant ved HR-positiv, HER2-positiv avansert brystkreft |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Ann Oncol | WSG-ADAPT: 12 ukers neoadjuvant dobbel blokade med trastuzumab og pertuzumab ± paklitaxel |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Metaanalyse | Lancet | Effekt av kjemoterapi og hormonbehandling ved tidlig brystkreft på residiv og 15-årsoverlevelse |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Kohort | Theranostics | Molekylære profiler og trastuzumab-respons ved ER+/PR+/HER2+ (trippelpositiv) brystkreft |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Retningslinje | J Clin Oncol | ASCO-retningslinje for systemisk behandling av avansert HER2-positiv brystkreft |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Oversikt | Nat Rev Clin Oncol | HER2- og hormonreseptor-positiv brystkreft: blokkering av riktig mål |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncol | ExteNET: neratinib etter trastuzumab-basert adjuvant behandling |
| [17687157](https://pubmed.ncbi.nlm.nih.gov/17687157/) | 2007 | Annet | J Clin Oncol | Trastuzumab-relatert kardiotoksisitet og spørsmålet om reversibilitet |

---

## Informasjon om det norske markedet

Alle tillatelser i datagrunnlaget er registrert som avregistrert (11 totalt). De fem første:

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000278 | Herceptin | – | Magekreft, brystkreft |
| EMEA/H/C/004916 | Ogivri | – | Magekreft, brystkreft |
| EMEA/H/C/006219 | Dazublys | – | Brystkreft, magekreft |
| EMEA/H/C/004361 | Kanjinti | – | Magekreft, brystkreft |
| EMEA/H/C/004323 | Ontruzant | – | Magekreft, brystkreft |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet behandling (monoklonalt anti-HER2-antistoff), ikke konvensjonelt cytotoksisk |
| Risiko for myelosuppresjon | Lav som monoterapi; kan øke i kombinasjon med kjemoterapi |
| Emetogenisitet | Lav |
| Overvåkingspunkter | Hjertefunksjon (LVEF) før og under behandling, blodstatus ved kombinasjon med kjemoterapi, lever- og nyrefunksjon |
| Håndtering og beskyttelse | Se preparatomtalen for krav til håndtering |

---

## Sikkerhetsvurderinger

- **Kardiotoksisitet**: Litteraturen omtaler trastuzumab-relatert kardiotoksisitet (PMID 17687157), og hjerteovervåking er nødvendig.
- **Legemiddelinteraksjoner**: Totalt 94 interaksjoner er registrert. Viktige eksempler:
  - **Alvorlige (Major)**: deferipron, samarium (153Sm) lexidronam, adalimumab, baricitinib
  - **Moderate**: paklitaksel, warfarin, dikumarol, zidovudin, kloramfenikol, roflumilast, alemtuzumab, azatioprin, anakinra, kanakinumab, palifermin, strontiumklorid Sr-89
- For advarsler og kontraindikasjoner, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails**

**Begrunnelse:**
Det foreligger fullførte randomiserte fase 3-studier og sentrale RCT-publikasjoner for trastuzumab ved HER2-positiv brystkreft, også ved PR-positiv sykdom. Prediksjonen faller innenfor den eksisterende indikasjonen, så evidensen gjelder kjent bruk og ikke ny repurposing.

**For å gå videre kreves følgende:**
- Obligatorisk HER2-testing; kriteriet bør være HER2-status, ikke PR-status
- Plan for hjerteovervåking (LVEF)
- Data om virkningsmekanisme fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen (manglende i datagrunnlaget og blokkerende for sikkerhetsscreening)

**Merknad om øvrige prediksjoner:**
- Den høyest rangerte prediksjonen («normal breast-like subtype») har kun L4-evidens og anbefalingen **Hold**: subtypen er vanligvis HER2-negativ, og den eneste studien gjelder et annet legemiddel (trastuzumab rezetecan) som ikke har startet rekruttering.
- PR-negativ brystkreft og luminal A/B har L1-evidens og anbefalingen Proceed with Guardrails, men bare ved HER2-positiv sykdom.
- Prediksjonene for sjeldne svulster (rangert 5–8) har kun modellstøtte (L5) og anbefalingen Hold.
- Urotelkarsinomene (rangert 9–10) har L5-evidens og er klassifisert som forskningsspørsmål; HER2-immunhistokjemi kreves først.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

