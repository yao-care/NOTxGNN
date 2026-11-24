---
layout: default
title: Amifampridine
parent: Kun modellprediksjon (L5)
nav_order: 29
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Amifampridine: predikert ny indikasjon Glaukom (evidensnivå L5). Opprinnelig indikasjon: Lambert-Eaton myasteniske syndrom"
monitor_inn: "AMIFAMPRIDINE"
predicted_indications: ["glaucoma", "acute intermittent porphyria"]
---

# Amifampridine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Amifampridin: Fra Lambert-Eaton myasteniske syndrom til glaukom
{: .text-alpha }

## Oppsummering i én setning

Amifampridin (3,4-diaminopyridin) brukes opprinnelig til behandling av Lambert-Eaton myasteniske syndrom (LEMS). TxGNN-modellen predikerer at legemidlet kan ha effekt ved **glaukom**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Lambert-Eaton myasteniske syndrom |
| Predikert ny indikasjon | Glaukom |
| TxGNN-prediksjonsscore | 0,9971 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Antall tillatelser | 2 (begge trukket) |
| Anbefalt beslutning | Hold |

---

## Hvorfor kan denne prediksjonen være rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Amifampridine (uoffisiell oversettelse): «Mekanismen som amifampridin utøver sin terapeutiske effekt gjennom hos pasienter med LEMS, er ikke fullstendig klarlagt. Amifampridin er en bredspektret kaliumkanalblokker.» Engelsk originaltekst: "The mechanism by which amifampridine exerts its therapeutic effect in LEMS patients has not been fully elucidated. Amifampridine is a broad-spectrum potassium channel blocker." ([DailyMed: Firdapse (amifampridine phosphate) prescribing information, Catalyst Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f015fe60-3128-4a43-8c31-19fc6b5def3f), versjon av 2026-04-16; hentet 2026-11-19). Ut fra generell kunnskap er amifampridin en blokker av spenningsstyrte kaliumkanaler. Ved å forlenge depolariseringen i presynaptiske nerveender øker den kalsiuminnstrømningen og frigjøringen av acetylkolin i den nevromuskulære overgangen. Dette forklarer effekten ved LEMS.

Det er ikke påvist noen direkte mekanistisk kobling til glaukom (forhøyet intraokulært trykk, degenerasjon av retinale ganglieceller). En spekulativ kobling kan være modulering av kaliumkanaler i nerveceller i netthinnen eller synsnerven, men dette er ikke underbygget av de foreliggende dataene. Den høye scoren er en ren modellprediksjon og støttes ikke av kliniske data eller litteratur.

Et annet predikert alternativ er **akutt intermitterende porfyri** (score 0,9932). Koblingen her er svak: amifampridin påvirker ikke den underliggende metabolske defekten (mangel på hydroksymetylbilansyntase). I tillegg senker amifampridin krampeterskelen, og kramper kan forekomme ved akutte porfyriangrep, noe som er et sikkerhetsproblem. Også dette alternativet har evidensnivå L5 og anbefalingen Hold.

---

## Klinisk studieevidens

Foreløpig er det ikke registrert noen relevante kliniske studier.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/001032 | Firdapse (previously Zenas) | amifampridine | Lambert-Eaton Myasthenic Syndrome | Gyldig |
| EMEA/H/C/005839 | Amifampridine SERB | amifampridine phosphate | Lambert-Eaton Myasthenic Syndrome; Paraneoplastic Syndromes, Nervous System; Nervous System Neoplasms; Parane… | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Begge tillatelsene er gyldige (2 av 2), og legemidlet er markedsført i Norge.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Totalt 68 kjente interaksjoner er registrert. Blant de som er hentet ut, er den eneste med alvorlighetsgrad **Major**:
  - Bupropion (Major)

  Flere interaksjoner med alvorlighetsgrad Moderate er registrert, blant annet:
  - Kortikosteroider: hydrokortison, betametason, deksametason, prednisolon, prednison
  - Sentralstimulerende og appetittdempende midler: dexfenfluramin, dietylpropion, efedrin, fenfluramin, mazindol, fentermin, sibutramin
  - Opioider: morfin, morfin (liposomal), opium
  - Andre: dronabinol, levofloksacin, metoklopramid, polyetylenglykol (3350 med elektrolytter)
- **Krampeterskel**: Amifampridin senker krampeterskelen, noe som er særlig relevant ved akutt intermitterende porfyri.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for glaukom bygger kun på modellscore (L5), uten kliniske studier, litteratur eller en påvist mekanistisk kobling. I tillegg mangler sikkerhetsdata fra preparatomtalen.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtale (advarsler og kontraindikasjoner) for sikkerhetsscreening
- Fullstendige data om virkningsmekanisme
- Prekliniske data eller litteratur som kan koble kaliumkanalblokkade til patofysiologien ved glaukom
- Avklaring av administrasjonsvei og formulering som kreves for øyesykdom
- Vurdering av markedsstatus og eventuell ny tillatelse i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Firdapse (amifampridine phosphate) prescribing information, Catalyst Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f015fe60-3128-4a43-8c31-19fc6b5def3f) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

