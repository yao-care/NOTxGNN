---
layout: default
title: Lonafarnib
parent: Kun modellprediksjon (L5)
nav_order: 249
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Lonafarnib: predikert ny indikasjon Lepra (evidensnivå L5). Opprinnelig indikasjon: Progeri"
monitor_inn: "LONAFARNIB"
predicted_indications: ["leprosy"]
---

# Lonafarnib
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

## Lonafarnib: Fra progeri og laminopatier til lepra
{: .text-alpha }

## Oppsummering i én setning

Lonafarnib er en farnesyltransferasehemmer som opprinnelig er godkjent for behandling av progeri og laminopatier.
TxGNN-modellen forutsier at legemidlet kan ha effekt mot **lepra**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Progeri; laminopatier |
| Predikert ny indikasjon | Lepra |
| TxGNN-prediksjonsscore | 0,9914 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Lonafarnib hemmer farnesyltransferase, et enzym som fester en farnesylgruppe til proteiner. Ved progeri og progeroide laminopatier reduserer dette opphopningen av det giftige, farnesylerte proteinet progerin. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Lonafarnib (uoffisiell oversettelse): «Lonafarnib hemmer farnesyltransferase for å hindre farnesylering og påfølgende opphopning av progerin og progerinlignende proteiner i den indre kjernemembranen.» Engelsk originaltekst: "Lonafarnib inhibits farnesyltransferase to prevent farnesylation and subsequent accumulation of progerin and progerin-like proteins in the inner nuclear membrane." ([DailyMed: Zokinvy (lonafarnib) prescribing information, Sentynl Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=97391d0c-943e-4c5a-8423-68e163aa7f50), versjon av 2025-07-02; hentet 2026-11-19).

Det finnes ingen dokumentert mekanistisk kobling mellom farnesyltransferasehemming og infeksjon med *Mycobacterium leprae* eller verts-responsen ved lepra (for eksempel infeksjon av Schwann-celler, immunmodulering i makrofager eller reaksjoner som ENL). Teoretisk kan prenyleringsavhengig signalering (Ras/Rho-GTPaser) påvirke samspillet mellom vert og patogen eller betennelse, men dette er spekulativt og ikke støttet av dataene. Den høye modellscoren (0,9914) alene er ikke tilstrekkelig til å vurdere prediksjonen som biologisk plausibel.

---

## Evidens fra kliniske studier

Foreløpig er det ikke registrert noen relaterte kliniske studier.

---

## Evidens fra litteraturen

Foreløpig finnes det ingen relatert litteratur.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/005271 | Zokinvy | Lonafarnib | Progeria; Laminopathies | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Godkjenningen (innehaver: TMC Pharma (EU) Limited) er gyldig. Legemidlet er markedsført, med 1 gyldig godkjenning av 1.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (100 interaksjoner funnet i interaksjonsdatabasen; et utvalg vises nedenfor):

- **Alvorlig (Major):** loperamid, aprepitant, triamcinolon, deksametason, budesonid, cimetidin, klaritromycin, eliglustat, naloksegol
- **Moderat (Moderate):** hydrokortison, omeprazol, betametason, klorpropamid, saksagliptin, empagliflozin, oksandrolon, naldemedin

Mange av disse er sannsynligvis knyttet til metabolisme via CYP3A4. Dette er en tolkning og er ikke bekreftet i dataene. Samtidig bruk av kortikosteroider, makrolider og CYP3A-påvirkende legemidler bør vurderes nøye.

Informasjon om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for lepra bygger utelukkende på modellscore (evidensnivå L5), uten kliniske studier, litteratur eller støttet mekanistisk kobling. Sikkerhetsdata fra preparatomtalen mangler.

<!-- review:begin no-lic-20261106-lonafarnib-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «I tillegg er den eneste norske/europeiske godkjenningen avregistrert, og sikkerhetsdata fra preparatomtalen mangler.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-lonafarnib-1 -->

**For å gå videre kreves følgende:**
- Hente og analysere advarsler og kontraindikasjoner fra preparatomtalen (blokkerende datamangel for sikkerhetsscreening)
- Fullstendige data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Prekliniske eller mekanistiske studier som viser en sammenheng mellom farnesyltransferasehemming og *M. leprae*-infeksjon eller lepra-immunrespons
- Litteratur- og studiesøk for å bekrefte at det ikke finnes relevant evidens
- Avklaring av legemidlets reguleringsstatus og tilgjengelighet i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «I tillegg er den eneste norske/europeiske godkjenningen avregistrert, og s» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Zokinvy (lonafarnib) prescribing information, Sentynl Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=97391d0c-943e-4c5a-8423-68e163aa7f50) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

