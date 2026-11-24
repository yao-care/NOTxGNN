---
layout: default
title: Zonisamide
parent: Kun modellprediksjon (L5)
nav_order: 461
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Zonisamide: predikert ny indikasjon Tourettes syndrom (evidensnivå L5). Opprinnelig indikasjon: Partiell epilepsi (fokale anfall)"
monitor_inn: "ZONISAMIDE"
predicted_indications: ["Tourette syndrome", "trichotillomania", "methemoglobinemia, alpha type", "methemoglobinemia", "Prinzmetal angina", "methemoglobin reductase deficiency", "manic bipolar affective disorder", "fibromyalgia", "conjunctivitis"]
---

# Zonisamide
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

## Zonisamid: Fra epilepsi til Tourettes syndrom
{: .text-alpha }

## Oppsummering

Zonisamid er et legemiddel mot epilepsi som er godkjent for partielle (fokale) anfall.
TxGNN-modellen forutsier at det kan ha effekt ved **Tourettes syndrom**, men prediksjonen bygger kun på modellen: **0 kliniske studier** og **0 publikasjoner** støtter den foreløpig.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Partiell epilepsi (fokale anfall) |
| Predikert ny indikasjon | Tourettes syndrom |
| TxGNN-prediksjonsscore | 0.9985 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

---

## Hvorfor kan prediksjonen være rimelig?

Det finnes ingen detaljerte data om virkningsmekanismen i datagrunnlaget som er samlet for denne rapporten. Zonisamid er et antiepileptikum med effekt ved epilepsi. Det er generelt beskrevet å blokkere natriumkanaler og T-type kalsiumkanaler, og kan påvirke dopaminerg og serotonerg signaloverføring. Tourettes syndrom er en nevroutviklingsforstyrrelse med tics, der dopaminerge kretser spiller en sentral rolle. En overlapp i nevrotransmittersystemer kan derfor tenkes. Dette er imidlertid spekulativt og ikke underbygget av data i denne rapporten.

Det er også et sikkerhetsmessig forbehold. En pragmatisk oversiktsartikkel (PMID 36005856, 2022) rapporterer at antiepileptika kan indusere tics og tvangslidelse. Dette kan tale mot bruk ved tic-lidelser og må vurderes nøye før eventuell videre utredning.

Høy modellscore alene er ikke bevis for klinisk effekt. Scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

---

## Kliniske studier

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det foreligger for øyeblikket ingen relatert litteratur.

---

## Markedsinformasjon for Norge

Begge godkjenningene er sentrale europeiske (EMA) godkjenninger. Legemidlet er markedsført, og 2 av 2 godkjenninger er gyldige.

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000577 | Zonegran | zonisamide | Epilepsies, Partial | Gyldig |
| EMEA/H/C/004127 | Zonisamide Viatris (previously Zonisamide Mylan) | zonisamide | Epilepsy | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: 100 interaksjoner er registrert. De viktigste av de 20 første som er vist i datagrunnlaget:
  - **Alvorlig (Major)**: metformin og antikolinerge midler (atropin, hyoscyamin, skopolamin, metskopolamin, glykopyrronium, klidinium, dicyklomin, trospium, mepenzolat, propantelin).
  - **Moderat**: aprepitant, morfin, deksametason, cimetidin, klaritromycin, dronabinol, nabilon, metoklopramid og mikonazol.
- **Kontraindikasjoner fra kunnskapsgrafen**: Kunnskapsgrafen (PrimeKG) knytter zonisamid til en rekke tilstander som kontraindikasjoner. Dette er ikke preparatomtale, men grafbaserte koblinger. Eksempler:
  - psykiske lidelser (angst, psykoser, schizoaffektiv lidelse)
  - nyresykdom og nyrestein
  - leversykdom og gallblæresykdom
  - metabolsk acidose
  - nøytropeni og agranulocytose
- **Psykiatriske bivirkninger**: Litteratur hentet under andre indikasjoner beskriver zonisamid-indusert mani (PMID 2109869) og antiepileptika-indusert tic-lidelse og tvangslidelse (PMID 36005856). Begge er relevante for en tic-lidelse som Tourettes syndrom.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (evidensnivå L5), uten kliniske studier eller litteratur for Tourettes syndrom. Zonisamid har i tillegg en mulig sikkerhetsrisiko for tics, og legemidlet er markedsført i Norge med 2 gyldige godkjenninger av 2.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank.
- Preparatomtale med varsler og kontraindikasjoner, som ikke er tilgjengelig i dagens datagrunnlag.
- Systematisk litteratursøk på zonisamid og tic-lidelser, inkludert rapporter om tics som bivirkning.
- Prekliniske data eller en liten pilotstudie som kan støtte effekt ved Tourettes syndrom.
- Avklaring av regulatorisk vei.

<!-- review:begin no-lic-20261124b-zonisamide-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av regulatorisk vei, siden begge godkjenningene er kansellert.» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-zonisamide-1 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-24 | Rettet: «Avklaring av regulatorisk vei, siden begge godkjenningene er kansellert.» → «Avklaring av regulatorisk vei.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

