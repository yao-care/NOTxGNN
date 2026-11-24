---
layout: default
title: Icatibant
parent: Kun modellprediksjon (L5)
nav_order: 204
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "ICATIBANT"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "Glanzmann thrombasthenia"]
description: "Icatibant: predikert ny indikasjon Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) (evidensnivå L5). Opprinnelig indikasjon: Angioedemas, Hereditary"
---

# Icatibant
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

## Icatibant: Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)
{: .text-alpha }

## Oppsummering

Icatibant er et peptidbasert legemiddel som blokkerer bradykininreseptorer, først og fremst B2-reseptoren.
TxGNN-modellen predikerer at det kan ha effekt ved **serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)**.
Det finnes **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen. Prediksjonen er derfor kun modellbasert.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Angioedemas, Hereditary |
| Predikert ny indikasjon | Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) |
| TxGNN-prediksjonsscore | 0.9999 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Icatibant (uoffisiell oversettelse): «Ikatibant er en kompetitiv antagonist som er selektiv for bradykinin B2-reseptoren, med en affinitet tilsvarende bradykinin. Hereditært angioødem skyldes fravær eller dysfunksjon av C1-esterasehemmer, en sentral regulator av den proteolytiske kaskaden faktor XII/kallikrein som fører til produksjon av bradykinin.» Engelsk originaltekst: "Icatibant is a competitive antagonist selective for the bradykinin B2 receptor, with an affinity similar to bradykinin. Hereditary angioedema is caused by an absence or dysfunction of C1-esterase-inhibitor, a key regulator of the Factor XII/kallikrein proteolytic cascade that leads to bradykinin production." ([DailyMed: Firazyr (icatibant acetate) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ed6657ca-ab68-477a-9968-e12dc928b540), versjon av 2025-07-07; hentet 2026-11-19). Farmakologidataene som er samlet inn for rapporten viser likevel at icatibant er en peptidantagonist som virker på bradykininreseptorene B1 (BDKRB1) og B2 (BDKRB2). Legemidlet hemmer dermed bradykininsignalering nedstrøms.

Den høye modellscoren skyldes trolig nettverksnærhet til serpin-relaterte gener i modellens biologiske nettverk. Sykdommen er definert av at feilfoldede serpiner polymeriserer og blir toksiske. Icatibant påvirker verken serpinfolding eller polymerisering, siden det virker på reseptornivå og ikke på selve proteinet.

Det er derfor ikke påvist noen mekanistisk sammenheng. Prediksjonen bør regnes som et beregningsmessig artefakt inntil motsatt er vist.

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

## Markedsinformasjon for Norge

Begge godkjenningene i dataene er gyldige.

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000899 | Firazyr | icatibant | Angioedemas, Hereditary | Gyldig |
| EMEA/H/C/005083 | Icatibant Accord | icatibant acetate | Angioedemas, Hereditary | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner**: 12 interaksjonsposter er registrert. Ti av dem er av moderat alvorlighetsgrad og gjelder ACE-hemmere:
- benazepril
- captopril
- enalapril
- perindopril
- trandolapril
- moexipril
- lisinopril
- quinapril
- ramipril
- fosinopril

De to øvrige postene gjelder farmakologiske målproteiner (B1- og B2-reseptoren), ikke interaksjoner med andre legemidler.

Ut over dette henvises det til preparatomtalen for informasjon om advarsler og kontraindikasjoner.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (0,9999) uten kliniske studier, litteratur eller en plausibel mekanisme. Icatibant virker på bradykininreseptorer, mens sykdommen skyldes feilfoldede og polymeriserende serpiner. Evidensnivået er L5.

**For å gå videre kreves:**
- En plausibel mekanistisk hypotese som kobler bradykinin-B2-blokade til serpinpolymerisering, bekreftet i prekliniske modeller
- Publiserte studier eller registrerte kliniske studier som direkte omhandler denne sykdommen
- Sikkerhetsdata fra preparatomtalen (advarsler og kontraindikasjoner), som mangler i datagrunnlaget
- Data om virkningsmekanisme (MOA) fra legemiddeldatabasen

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Firazyr (icatibant acetate) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ed6657ca-ab68-477a-9968-e12dc928b540) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

