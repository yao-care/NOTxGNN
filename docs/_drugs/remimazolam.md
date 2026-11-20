---
layout: default
title: Remimazolam
parent: Kun modellprediksjon (L5)
nav_order: 355
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-20
description: "Remimazolam: predikert ny indikasjon Insomni (evidensnivå L5). Opprinnelig indikasjon: Prosedyresedasjon (conscious sedation)"
monitor_inn: "remimazolam"
drugbank_id: DB12404
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Remimazolam
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

## Remimazolam: Fra prosedyresedasjon til insomni
{: .text-alpha }

## Oppsummering i én setning

Remimazolam er et ultrakortvirkende benzodiazepin som opprinnelig brukes til **prosedyresedasjon (conscious sedation)**.
TxGNN-modellen forutsier at det kan være effektivt mot **insomni**, og som nummer to mot **delirium ved alkoholabstinens**.
Foreløpig finnes det **ingen kliniske studier og ingen publikasjoner** i de sammenstilte dataene som støtter disse prediksjonene, så de er kun modellbaserte.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Prosedyresedasjon (conscious sedation) |
| Predikert ny indikasjon | Insomni |
| TxGNN-prediksjonsscore | 0,9991 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen rimelig?

Remimazolam er et benzodiazepin med ultrakort virketid. Det virker som positiv allosterisk modulator av GABA-A-reseptoren. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Remimazolam (uoffisiell oversettelse): «BYFAVO er et benzodiazepin. BYFAVO binder seg til benzodiazepinseter i hjernen (gamma-aminosmørsyre type A [GABA A ]-reseptorer), mens karboksylsyremetabolitten (CNS7054) har 300 ganger lavere affinitet for reseptoren.» Engelsk originaltekst: "BYFAVO is a benzodiazepine. BYFAVO binds to brain benzodiazepine sites (gamma amino butyric acid type A [GABA A ] receptors), while its carboxylic acid metabolite (CNS7054) has a 300 times lower affinity for the receptor." ([DailyMed: Byfavo (remimazolam besylate) prescribing information, Acacia Pharma, Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e1838f2-b999-41a7-a761-d94f09aa531f), versjon av 2025-02-20; hentet 2026-11-19).

Siden virkningen er den samme som hos etablerte benzodiazepiner mot søvnløshet, er en sedativ-hypnotisk effekt biologisk plausibel. Både sedasjon og insomnibehandling handler om å øke hemmende GABA-aktivitet i sentralnervesystemet.

Det er likevel viktige begrensninger. Den svært korte halveringstiden (rask nedbrytning via esteraser) og at legemidlet kun gis intravenøst i prosedyremessige settinger, gjør det dårlig egnet til å opprettholde søvn. Den høye scoren (0,9991) gjenspeiler trolig likhet med andre GABA-A-modulatorer på klassenivå, ikke legemiddelspesifikk evidens.

**Sekundær prediksjon: delirium ved alkoholabstinens (score 0,9930).** Benzodiazepiner er standardbehandling ved alkoholabstinens fordi GABA-A-potensiering motvirker tapet av hemmende tonus. Rask innsettende og avtagende effekt kan gi presis titrering på intensivavdeling, men den korte virketiden kan gi rebound-symptomer uten kontinuerlig infusjon. Dosering ved benzodiazepinresistent delirium tremens er uavklart. Også her er det kun et beregnet signal, ikke klinisk evidens.

---

## Evidens fra kliniske studier

Foreløpig er det ingen registrerte kliniske studier knyttet til disse indikasjonene.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005246 | Byfavo | Ikke oppgitt | Conscious sedation (status: kansellert) |

Legemidlet er markedsført i Norge, med 1 gyldig godkjenning av 1.

---

## Sikkerhetsvurderinger

Pakningsvedlegg med advarsler og kontraindikasjoner er ikke tilgjengelig i de sammenstilte dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Legemiddelinteraksjoner:** Det er registrert 54 interaksjoner. Blant dem som er vist i dataene er de viktigste:

- **Alvorlige (Major):** morfin, liposomal morfin, kodein, hydrokodon. Samtidig bruk av opioider og benzodiazepiner kan gi additiv sentral depresjon, inkludert respirasjonsdepresjon.
- **Moderate:** blant annet etanol, bupropion, dronabinol, nabilon, metoklopramid, opium, sibutramin, diazoksid, fentolamin, prometazin, disulfiram, lidokain, klorfeniramin, cetirizin, azelastin (nasal) og dekstrometorfan.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonene bygger kun på modellscore og klassebasert mekanismelikhet (evidensnivå L5), uten kliniske studier eller litteratur. I tillegg er legemidlets formulering (kun intravenøs) og ultrakorte virketid dårlig tilpasset kronisk søvnbehandling.

**For å gå videre kreves følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel som må løses før sikkerhetsvurdering)
- Detaljerte data om virkningsmekanisme (MOA) fra legemiddeldatabasen
- Systematisk litteratur- og studiesøk for insomni og alkoholabstinens
- Vurdering av administrasjonsvei og farmakokinetikk (infusjon vs. egnet formulering) for de nye indikasjonene
- Avklaring av godkjenningsstatus i Norge, siden eksisterende godkjenning er kansellert

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Byfavo (remimazolam besylate) prescribing information, Acacia Pharma, Ltd.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4e1838f2-b999-41a7-a761-d94f09aa531f) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

