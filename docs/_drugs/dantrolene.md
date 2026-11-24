---
layout: default
title: Dantrolene
parent: Kun modellprediksjon (L5)
nav_order: 111
evidence_level: L5
indication_count: 7
monitor_inn: "dantrolene"
predicted_indications: ["moderate multiminicore disease with hand involvement", "King-Denborough syndrome", "congenital multicore myopathy with external ophthalmoplegia", "central core myopathy", "hypokalemic periodic paralysis", "thyrotoxic periodic paralysis", "myopathy, centronuclear"]
last_modified_at: 2026-11-24
description: "Dantrolene: predikert ny indikasjon Moderat multiminicore-sykdom med håndaffeksjon (moderate multiminicore disease with hand involvement) (evidensnivå L5). Opprinnelig indikasjon: Malignant Hyperther…"
---

# Dantrolene
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

## Dantrolen: ryanodinreseptor-hemmer og muskelavslappende middel → Moderat multiminicore-sykdom med håndaffeksjon (moderate multiminicore disease with hand involvement)
{: .text-alpha }

## Oppsummering i korte trekk

Dantrolen er et muskelavslappende legemiddel som virker på kalsiumfrigjøring i skjelettmuskulatur. TxGNN-modellen forutsier at det kan ha effekt ved **moderat multiminicore-sykdom med håndaffeksjon (moderate multiminicore disease with hand involvement)**. Det finnes **ingen kliniske studier** og **ingen publikasjoner** om akkurat denne sykdomsvarianten i dataene som er samlet for rapporten. Prediksjonen bygger altså kun på modellen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Malignant Hyperthermia |
| Foreslått ny indikasjon | Moderat multiminicore-sykdom med håndaffeksjon (moderate multiminicore disease with hand involvement) |
| TxGNN-prediksjonsscore | 0,9990 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Dantrolene (uoffisiell oversettelse): «I isolerte nerve-muskel-preparater er det vist at dantrolen gir relaksasjon ved å påvirke muskelens kontraktile respons på et sted utenfor den nevromuskulære overgangen. I skjelettmuskulatur opphever dantrolen eksitasjons-kontraksjonskoblingen, sannsynligvis ved å hemme frisettingen av Ca ++ fra det sarkoplasmatiske retikulum.» Engelsk originaltekst: "In isolated nerve-muscle preparation, dantrolene has been shown to produce relaxation by affecting the contractile response of the muscle at a site beyond the myoneural junction. In skeletal muscle, dantrolene dissociates the excitation-contraction coupling, probably by interfering with the release of Ca ++ from the sarcoplasmic reticulum." ([DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698), versjon av 2024-10-30; hentet 2026-11-19). Dantrolen er likevel kjent som en hemmer av ryanodinreseptoren i skjelettmuskulatur (RYR1), som styrer frigjøring av kalsium fra det sarkoplasmatiske retikulum.

Multiminicore-sykdom er en medfødt muskelsykdom som ofte er knyttet til varianter i genene *RYR1* eller *SEPN1*. Et mekanistisk resonnement finnes bare for den RYR1-relaterte undergruppen, der forstyrret kalsiumregulering er en sentral mekanisme. For SEPN1-relaterte tilfeller er koblingen til dantrolen ikke underbygget.

Modellscoren er svært høy, men det mangler både studier og litteratur for akkurat denne fenotypen (med håndaffeksjon). Likhet med dantrolens opprinnelige bruk er ikke vurdert. Prediksjonen må derfor ses som en hypotese som ikke er testet klinisk.

## Kliniske studier

Det er for tiden ikke registrert noen relevante kliniske studier.

## Litteraturevidens

Det foreligger for tiden ingen relevant litteratur.

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/006009 | Agilus | dantrolene sodium, hemiheptahydrate | Malignant Hyperthermia | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Til sammen er 72 mulige interaksjoner registrert. De viktigste er:

- **Alvorlig (Major):** morfin og liposomalt morfin.
- **Moderat:** dronabinol, metoklopramid, nabilon, naltrekson, opium, sibutramin, etanol og prometazin.
- **Uklart nivå:** flere andre, blant annet pantoprazol, omeprazol, metformin, simvastatin og klaritromycin.

For øvrig sikkerhetsinformasjon, som advarsler og kontraindikasjoner, vises det til preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen har svært høy modellscore, men støttes verken av kliniske studier eller av publikasjoner om denne spesifikke sykdomsvarianten. Evidensnivået er derfor L5, og det finnes bare et begrenset mekanistisk resonnement for den RYR1-relaterte undergruppen.

**For å gå videre trengs følgende:**
- Genetisk avklaring av hvilke pasienter som har RYR1-relatert sykdom, og hvilke som har SEPN1-relatert sykdom.
- Litteratursøk og prekliniske data som direkte undersøker dantrolen ved multiminicore-sykdom.
- Data om virkningsmekanisme (MOA) for dantrolen.
- Gjennomgang av preparatomtalen for advarsler og kontraindikasjoner, spesielt ved lever- og muskelsykdom.
- Vurdering av administrasjonsvei og formulering, som ikke er avklart.

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Ryanodex Dantrolene Sodium (dantrolene sodium) prescribing information, Eagle Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8f7b3ac0-604d-4c78-b545-5e0f8ea3d698) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

