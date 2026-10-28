---
layout: default
title: Nilotinib
parent: Kun modellprediksjon (L5)
nav_order: 284
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "NILOTINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
description: "Nilotinib: predikert ny indikasjon Dermatofibrosarcoma protuberans (evidensnivå L5). Opprinnelig indikasjon: Leukemia, Myelogenous, Chronic, BCR-ABL Positive"
---

# Nilotinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Nilotinib: Dermatofibrosarcoma protuberans
{: .text-alpha }

## Sammendrag

Nilotinib er en tyrosinkinasehemmer som opprinnelig brukes til behandling av BCR-ABL-positiv kronisk myelogen leukemi.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **dermatofibrosarcoma protuberans (DFSP)**.
Evidensen er foreløpig svak: **ingen registrerte kliniske studier** og **1 publikasjon** (en oversiktsartikkel) i de innsamlede dataene.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Leukemia, Myelogenous, Chronic, BCR-ABL Positive |
| Predikert ny indikasjon | Dermatofibrosarcoma protuberans |
| TxGNN-prediksjonsscore | 0.9931 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Antall tillatelser | 2 (begge avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

DFSP kjennetegnes av en COL1A1-PDGFB-fusjon som gir vedvarende autokrin aktivering av PDGFRB. Nilotinib hemmer, i tillegg til BCR-ABL, også PDGFR (alfa/beta) og KIT. Dette gir et plausibelt mekanistisk grunnlag for effekt ved DFSP.

Dette er samme mekanistiske klasse som imatinib, som er etablert i behandling av DFSP. Den svært høye prediksjonsscoren er i tråd med denne PDGFR-koblingen, men den er en beregningsbasert prediksjon og ikke klinisk evidens.

Merk: Data om virkningsmekanisme (MOA) er ikke tilgjengelig i de innsamlede dataene. Mekanismebeskrivelsen over bygger derfor på generell farmakologisk kunnskap om nilotinib og ikke på de leverte dataene.

---

## Klinisk studieevidens

Foreløpig ingen relevante kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Oversiktsartikkel | Pharmacological Research | Gjennomgang av rollen til småmolekylære PDGFR-hemmere i behandling av neoplastiske sykdommer; gir bakgrunn for PDGFR som terapeutisk mål |

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000798 | Tasigna (Novartis Europharm Limited) | Ikke oppgitt | Kronisk myelogen leukemi, BCR-ABL-positiv (godkjent) |
| EMEA/H/C/006315 | Nilotinib Accord (Accord Healthcare S.L.U.) | Ikke oppgitt | Kronisk myelogen leukemi, BCR-ABL-positiv (godkjent) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet terapi (tyrosinkinasehemmer) |
| Emetogenisitet | Se preparatomtalen for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Blodstatus (CBC), lever- og nyrefunksjon, elektrolytter (kalium, fosfor, kalsium), blodsukker, EKG/QT-intervall |
| Håndteringsbeskyttelse | Se preparatomtalen for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

Data om advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelig. Se preparatomtalen for sikkerhetsinformasjon.

- **Tilstander markert i kunnskapsgrafen (PrimeKG, ikke preparatomtale):** høyt blodtrykk, langt QT-syndrom (inkl. arvelig form) og torsades de pointes, leversykdom, gallblæresykdom, trombocytopeni, nøytropeni, agranulocytose, anemi, hyperglykemi, diabetes og diabetisk ketoacidose, kaliummangel, hyperkalsemi, nefrokalsinose, forstyrrelser i fosformetabolismen, hypofosfatemi, hyperbilirubinemi (inkl. Gilberts syndrom) og pankreatitt.
- **Legemiddelinteraksjoner:** 100 interaksjoner funnet; de 20 første vises i dataene. Alvorlige (Major) interaksjoner:
  - Deksametason
  - Klaritromycin
  - Pikosulfatsyre
  - Polyetylenglykol (3350 med elektrolytter)
  
  Moderate interaksjoner inkluderer syrehemmere (famotidin, ranitidin, rabeprazol, omeprazol, cimetidin), kortikosteroider (hydrokortison, triamcinolon, betametason, budesonid), pioglitazon, loperamid, bupropion, aprepitant, bisakodyl og saksagliptin.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Det mekanistiske grunnlaget (PDGFR-hemming, analogt med imatinib) er plausibelt, men evidensen består kun av modellprediksjon og én oversiktsartikkel uten kliniske studier. I tillegg er legemidlet markedsført i Norge med 2 gyldige tillatelser av 2, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel)
- Data om virkningsmekanisme fra DrugBank
- Søk etter kliniske studier og case-/fase 2-data for nilotinib ved DFSP, og sammenligning med imatinib
- Avklaring av regulatorisk status og tilgjengelighet i Norge, gitt at begge tillatelsene er avregistrert
- Vurdering av kardiovaskulær sikkerhet (QT-forlengelse) og interaksjonsrisiko før eventuell videre utvikling
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

