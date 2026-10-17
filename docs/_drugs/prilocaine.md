---
layout: default
title: Prilocaine
parent: Kun modellprediksjon (L5)
nav_order: 339
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prilocaine: predikert ny indikasjon Papillær konjunktivitt (evidensnivå L5). Opprinnelig indikasjon: Fysiologisk seksuell dysfunksjon"
monitor_inn: "PRILOCAINE"
predicted_indications: ["papillary conjunctivitis", "manic bipolar affective disorder", "bronchitis", "migraine disorder", "neuralgia", "migraine with brainstem aura", "atopic eczema", "allergic asthma", "rhinitis", "rosacea conjunctivitis"]
---

# Prilocaine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Prilokain: Fra fysiologisk seksuell dysfunksjon til papillær konjunktivitt

## Oppsummering

Prilokain er et amid-lokalbedøvelsesmiddel. Det er registrert for fysiologisk seksuell dysfunksjon (preparatet Fortacin). TxGNN-modellen predikerer at det kan ha effekt ved **papillær konjunktivitt**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne prediksjonen. Anbefalingen er derfor **Hold**.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Fysiologisk seksuell dysfunksjon |
| Predikert ny indikasjon | Papillær konjunktivitt |
| TxGNN-prediksjonsscore | 99,78 % |
| Evidensnivå | L5 (kun modellprediksjon) |
| Markedsstatus i Norge | Kun trukket tilbake (avregistrert) |
| Antall godkjenninger | 1 (0 gyldige, 1 kansellert) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanismen er foreløpig ikke tilgjengelige i datagrunnlaget. Ut fra kjent informasjon er prilokain et amid-lokalbedøvelsesmiddel som blokkerer spenningsstyrte natriumkanaler og dermed demper nerveledning. Effekten ved den opprinnelige indikasjonen skyldes sannsynligvis en lokal, overflatisk nervedempende virkning.

Teoretisk kan en slik virkning gi symptomlindring på øyets overflate, for eksempel mot ubehag og smerte. Det finnes imidlertid ingen studier eller litteratur som viser at prilokain påvirker den underliggende betennelsen eller allergiske prosessen ved papillær konjunktivitt. Prediksjonen bør derfor regnes som en hypotese og ikke som støttet behandling. Likheten mellom den opprinnelige og den nye indikasjonen er ikke vurdert (status: avventer).

## Kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert for papillær konjunktivitt.

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

## Informasjon om markedet i Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002693 | Fortacin (Recordati Ireland Ltd.) | Ikke oppgitt | Fysiologisk seksuell dysfunksjon (status: kansellert) |

## Sikkerhetsvurderinger

Informasjon fra preparatomtale (varsler og kontraindikasjoner) mangler i datagrunnlaget. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Legemiddelinteraksjoner**: Totalt 22 interaksjoner er registrert, og 20 er spesifisert i datagrunnlaget (kilde: DDInter).

- **Alvorlige (Major), 18 stk.**: metoklopramid, sulfasalazin, amylnitritt, rasburikase, salpetersyrling (nitrous acid), klorokin, primakin, kinin, tafenokin, lidokain (systemisk og topikal), benzokain (topikal), nitrogenmonoksid, dapson (systemisk og topikal), cinkokain (topikal), sølvnitrat (topikal) og sølvsulfadiazin (topikal).
- **Moderate**: liposomal morfin.
- **Milde (Minor)**: hyaluronidase.

Mange av de alvorlige interaksjonene gjelder legemidler som kan fremkalle methemoglobinemi eller har additiv effekt. Dette er en kjent risiko for prilokain, og tolkningen bør bekreftes mot preparatomtalen.

**Sykdommer markert som kontraindikasjon i kunnskapsgrafen** (modellbaserte kanter i TxGNN/PrimeKG, ikke tekst fra preparatomtale):
- **Hjerte og kar**: hypertensjon, koronarsykdom, hjerteinfarkt, plutselig hjertestans, hjerteledningsforstyrrelser, atrioventrikulær blokk, hjertesykdom generelt
- **Nevromuskulære**: epilepsi, myasthenia gravis, sykdommer i den nevromuskulære overgangen, butyrylkolinesterasemangel
- **Nyre, lever og galleblære**: nyresykdom, leversykdom, galleblæresykdom
- **Stoffskifte og endokrine**: diabetes mellitus, diabetisk ketoacidose, hypertyreose, Graves sykdom, tyreotoksikose
- **Øvrige**: hemoglobinopati, respirasjonssvikt, trangvinklet glaukom

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
- Prediksjonen for papillær konjunktivitt hviler kun på modellscore (L5), uten kliniske studier eller litteratur. Produktet er dessuten kun avregistrert i markedet, og sikkerhetsdata fra preparatomtalen mangler.

**Andre prediksjoner med mer evidens:**
- **Nevralgi** (rang 5, evidensnivå L3) er den best støttede av de ti predikerte indikasjonene.
  - En liten, åpen fase 2-studie (NCT00916942, n=20) brukte lidokain/prilokain-krem som forbehandling før kapsaicinplaster ved postherpetisk nevralgi.
  - Eldre kliniske studier (PMID 2493878 og 2616182, begge 1989) rapporterer symptomlindring med lidokain/prilokain-krem (EMLA).
  - Prilokains egen bidrag kan ikke skilles fra lidokains, og det finnes ingen fase 3-studier. Dette bør vurderes som et eget forskningsspørsmål.
- For atopisk eksem viser litteraturen primært risiko, som økt systemisk opptak, kramper og methemoglobinemi, og ikke terapeutisk nytte.

**For å gå videre trengs følgende:**
- Preparatomtale med varsler og kontraindikasjoner fra DMP (blokkerende datamangel)
- Data om virkningsmekanisme fra DrugBank
- Vurdering av administrasjonsvei (oftalmisk bruk) og lokal tolerabilitet, samt sikkerhetsvurdering av methemoglobinemi
- Dokumentasjon fra prekliniske eller kliniske studier som viser effekt på underliggende patologi ved papillær konjunktivitt, eller et strategisk skifte til nevralgi som primær kandidat
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

