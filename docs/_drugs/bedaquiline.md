---
layout: default
title: Bedaquiline
parent: Kun modellprediksjon (L5)
nav_order: 53
evidence_level: L5
indication_count: 4
monitor_inn: "Bedaquiline"
predicted_indications: ["vulvovaginal candidiasis", "fascioliasis", "urea cycle disorder", "esophageal candidiasis"]
last_modified_at: 2026-10-28
description: "Bedaquiline: predikert ny indikasjon vulvovaginal candidiasis (evidensnivå L5). Opprinnelig indikasjon: Tuberculosis, Multidrug-Resistant"
---

# Bedaquiline
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

## Bedaquiline: antimykobakteriell ATP-syntasehemmer → vulvovaginal candidiasis (vulvovaginal candidiasis)
{: .text-alpha }

## Oppsummering i én setning

Bedaquilin er et legemiddel mot tuberkulose. Den første prediksjonen fra TxGNN-modellen er **vulvovaginal candidiasis (vulvovaginal candidiasis)**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen i dataene som er sammenstilt for denne rapporten.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Tuberculosis, Multidrug-Resistant |
| Predikert ny indikasjon | vulvovaginal candidiasis (vulvovaginal candidiasis) |
| TxGNN-prediksjonsscore | 0,9988 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Bedaquiline (uoffisiell oversettelse): «Bedakilin er et antimykobakterielt legemiddel av typen diarylkinolin. […] SIRTURO er et antimykobakterielt legemiddel av typen diarylkinolin som hemmer mykobakteriell ATP (adenosin-5'-trifosfat)-syntase ved å binde seg til subenhet c av enzymet, som er essensiell for energiproduksjonen i M. tuberculosis.» Engelsk originaltekst: "Bedaquiline is a diarylquinoline antimycobacterial drug. […] SIRTURO is a diarylquinoline antimycobacterial drug that inhibits mycobacterial ATP (adenosine 5'- triphosphate) synthase, by binding to subunit c of the enzyme that is essential for the generation of energy in M. tuberculosis." ([DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e), versjon av 2025-10-17; hentet 2026-11-19). Ut fra generell kunnskap virker bedaquilin på ATP-syntasens c-underenhet hos mykobakterier. Dette er ikke en etablert antifungal mekanisme.

Det er ingen tydelig mekanistisk sammenheng mellom mykobakteriell ATP-syntase og soppinfeksjon med *Candida*. Den høye prediksjonsscoren ser ut til å være en modellartefakt, og verken kliniske studier eller litteratur underbygger den. Likhet med den opprinnelige indikasjonen er ikke vurdert.

## Kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

## Informasjon om markedet i Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002614 | Sirturo | Ikke oppgitt | Se lokale lisensdata |

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (100 interaksjoner funnet; et utvalg vises):

- **Alvorlige (Major):** deksametason, klaritromycin, pikosulfat, polyetylenglykol (3350 med elektrolytter), dolasetron, palonosetron, natriumsulfat.
- **Moderate:** blant annet acarbose, famotidin, doksycyklin, pioglitazon, loperamid, bupropion, bisakodyl, kenodeoksykolsyre, minocyklin, oksandrolon, oksymetolon, tetracyklin og naltrekson.

For advarsler og kontraindikasjoner, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5). Det finnes ingen kliniske studier eller litteratur, og ingen plausibel mekanisme for aktivitet mot *Candida*.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og en mekanistisk begrunnelse for antifungal effekt
- Prekliniske data (in vitro-aktivitet mot *Candida*)
- Preparatomtale med advarsler og kontraindikasjoner for sikkerhetsscreening
- Vurdering av administrasjonsvei og egnethet for vulvovaginal bruk

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Sirturo (bedaquiline fumarate) prescribing information, Janssen Products, LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1534c9ae-4948-4cf4-9f66-222a99db6d0e) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

