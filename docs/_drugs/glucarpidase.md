---
layout: default
title: Glucarpidase
parent: Kun modellprediksjon (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Glucarpidase: predikert ny indikasjon Diabetisk katarakt (evidensnivå L5). Opprinnelig indikasjon: Metabolske bivirkninger av legemidler og stoffer"
monitor_inn: "GLUCARPIDASE"
predicted_indications: ["diabetic cataract", "diabetic retinopathy", "craniostenosis cataract", "tetanic cataract", "diabetes mellitus type 2 associated cataract", "immature cataract", "mature cataract", "nuclear senile cataract", "cortical cataract", "senile cataract"]
---

# Glucarpidase
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

## Glukarpidase: Fra metotreksat-toksisitet til diabetisk katarakt
{: .text-alpha }

## Oppsummering

Glukarpidase er et enzym som opprinnelig brukes for å behandle metabolske bivirkninger av legemidler og stoffer, i praksis toksiske metotreksatnivåer. TxGNN-modellen (deep learning) forutsier at det kan ha effekt mot **diabetisk katarakt**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Den høye prediksjonsscoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Metabolske bivirkninger av legemidler og stoffer |
| Predikert ny indikasjon | Diabetisk katarakt |
| TxGNN-prediksjonsscore | 0,9985 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er (eller er ikke) denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Glucarpidase (uoffisiell oversettelse): «Glukarpidase er et rekombinant bakterielt enzym som hydrolyserer den karboksyterminale glutamatresten fra folsyre og klassiske antifolater som metotreksat. Glukarpidase omdanner metotreksat til de inaktive metabolittene 4-deoksy-4-amino-N 10 -metylpteroinsyre (DAMPA) og glutamat.» Engelsk originaltekst: "Glucarpidase is a recombinant bacterial enzyme that hydrolyzes the carboxyl- terminal glutamate residue from folic acid and classical antifolates such as methotrexate. Glucarpidase converts methotrexate to its inactive metabolites 4-deoxy-4-amino-N 10 - methylpteroic acid (DAMPA) and glutamate." ([DailyMed: Voraxaze (glucarpidase) prescribing information, BTG International Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acaef5a6-b740-40e3-8ffe-74a75c74745c), versjon av 2024-11-27; hentet 2026-11-19). Ut fra kjent farmakologi er glukarpidase et rekombinant karboksypeptidase G2-enzym som bryter ned metotreksat utenfor cellene til inaktive metabolitter (DAMPA og glutamat). Det gis intravenøst ved toksiske metotreksatnivåer.

Det er ikke funnet noen troverdig mekanistisk kobling til diabetisk katarakt. Glukarpidase påvirker ikke polyolveien, aldosereduktase eller glykering av linseproteiner. Som et stort protein (ca. 83 kDa dimer) gitt intravenøst er det lite praktisk å nå linsen. Den høye scoren skyldes trolig grafnærhet til den opprinnelige betegnelsen «metabolske bivirkninger», ikke biologisk plausibilitet.

Andre topprangerte prediksjoner (alle med score fra 0,9982 til 0,9984 og evidensnivå L5) gjelder i hovedsak ulike katarakttyper og diabetisk retinopati:

| Rang | Predikert indikasjon | Score |
|------|------|------|
| 2 | Diabetisk retinopati | 0,9984 |
| 3 | Kraniostenose-katarakt | 0,9983 |
| 4 | Tetanisk katarakt | 0,9983 |
| 5 | Katarakt ved diabetes mellitus type 2 | 0,9983 |
| 6 | Umoden katarakt | 0,9983 |
| 7 | Moden katarakt | 0,9983 |
| 8 | Nukleær senil katarakt | 0,9983 |
| 9 | Kortikal katarakt | 0,9983 |
| 10 | Senil katarakt | 0,9982 |

For ingen av disse er det identifisert en mekanistisk begrunnelse. Scorene kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/005467 | Voraxaze | glucarpidase | Metabolic Side Effects of Drugs and Substances | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Denne godkjenningen er gyldig, og legemidlet er markedsført i Norge (1 gyldig godkjenning av 1).

---

## Sikkerhetsmomenter

**Legemiddelinteraksjoner** (8 registrerte, alle av moderat alvorlighetsgrad):

- Proguanil
- Trimetoprim
- Levoleukovorin
- Pemetreksed
- Pralatreksat
- Pyrimetamin
- Leukovorin
- Trimetreksat

Det er ikke tilgjengelig data om advarsler og kontraindikasjoner. Se preparatomtalen for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5), uten kliniske studier, litteratur eller troverdig mekanistisk kobling. Systemisk enzymbehandling gitt intravenøst er dessuten dårlig egnet for å nå linsen eller netthinnen. Legemidlet er markedsført i Norge (1 gyldig godkjenning av 1).

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen, som er en forutsetning for sikkerhetsscreening
- Prekliniske data som viser en biologisk sammenheng med linse- eller netthinnepatologi ved diabetes
- Vurdering av administrasjonsvei og tilgang til øyevev
- Avklaring av godkjenningsstatus i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Voraxaze (glucarpidase) prescribing information, BTG International Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acaef5a6-b740-40e3-8ffe-74a75c74745c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

