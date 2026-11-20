---
layout: default
title: Doravirine
parent: Kun modellprediksjon (L5)
nav_order: 131
evidence_level: L5
indication_count: 3
monitor_inn: "DORAVIRINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Doravirine: predikert ny indikasjon Felint ervervet immunsviktsyndrom (feline acquired immunodeficiency syndrome) (evidensnivå L5). Opprinnelig indikasjon: HIV Infections"
---

# Doravirine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Doravirin: NNRTI → felint ervervet immunsviktsyndrom (feline acquired immunodeficiency syndrome)
{: .text-alpha }

## Oppsummering

Doravirin er en ikke-nukleosid revers transkriptasehemmer (NNRTI) mot HIV-1. Modellen TxGNN predikerer at legemidlet kan ha effekt mot **felint ervervet immunsviktsyndrom (feline acquired immunodeficiency syndrome)**. Det finnes **ingen kliniske studier og ingen publikasjoner** som direkte undersøker denne sykdommen, så støtten er kun modellbasert.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | HIV Infections |
| Predikert ny indikasjon | Felint ervervet immunsviktsyndrom (feline acquired immunodeficiency syndrome) |
| TxGNN-prediksjonsscore | 0,9993 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittene «Mechanism of Action» og «Microbiology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Doravirine (uoffisiell oversettelse): «Doravirin er et antiretroviralt legemiddel. […] Doravirin er en pyridinon-ikke-nukleosid revers transkriptasehemmer av HIV-1 og hemmer HIV-1-replikasjon ved ikke-kompetitiv hemming av HIV-1 revers transkriptase (RT). Den hemmende konsentrasjonen ved 50 % (IC 50 ) av doravirin for RNA-avhengig DNA-polymerisering av rekombinant villtype HIV-1 RT i en biokjemisk analyse var 12,2±2,0 nM (n=3).» Engelsk originaltekst: "Doravirine is an antiretroviral drug. […] Doravirine is a pyridinone non-nucleoside reverse transcriptase inhibitor of HIV-1 and inhibits HIV-1 replication by non-competitive inhibition of HIV-1 reverse transcriptase (RT). The inhibitory concentration at 50% (IC 50 ) of doravirine for RNA-dependent DNA polymerization of recombinant wild-type HIV-1 RT in a biochemical assay was 12.2±2.0 nM (n=3)." ([DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25), versjon av 2026-07-09; hentet 2026-11-19). Doravirin er kjent som en NNRTI som hemmer revers transkriptase hos HIV-1. Felint immunsviktvirus (FIV) er et lentivirus som er i slekt med HIV, og i prinsippet finnes derfor en mekanistisk begrunnelse.

Det er imidlertid en vesentlig begrensning: NNRTI-er er generelt dårlig virksomme mot FIV, fordi revers transkriptase hos FIV har en annen struktur i NNRTI-bindingslommen. Den høye scoren (0,9993) ser ut til å gjenspeile sykdommens nærhet til HIV i nettverket, ikke validert aktivitet. Ingen doravirinspesifikke data for FIV er tilgjengelige.

## Klinisk evidens

Foreløpig er det ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur for denne prediksjonen.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004747 | Pifeltro | Ikke angitt | HIV-infeksjoner |
| EMEA/H/C/004746 | Delstrigo | Ikke angitt | HIV-infeksjoner |

## Sikkerhetsmomenter

- **Legemiddelinteraksjoner**: Det er registrert 59 interaksjoner i dataene. Blant dem som er oppført, er de viktigste klassifisert som **alvorlige (Major)**:
  - Deksametason
  - Lumacaftor
- Flere interaksjoner av moderat grad er oppført, blant annet glyserolfenylbutyrat, metreleptin, troglitazon, deferasirox, praziquantel og griseofulvin.
- Mange er klassifisert som lette (Minor), blant annet aprepitant, cimetidin, klaritromycin, flukonazol og erytromycin.

For øvrig sikkerhetsinformasjon, se pakningsvedlegget.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore uten kliniske studier eller litteratur (evidensnivå L5). Biologisk støtte er svak, siden FIV er naturlig lite følsomt for NNRTI-er. Indikasjonen er dessuten veterinærmedisinsk og har ingen direkte humanklinisk relevans.

**For å gå videre kreves følgende:**
- Doravirinspesifikke prekliniske data (in vitro-aktivitet mot FIV)
- Data om virkningsmekanisme (MOA)
- Gjennomgang av preparatomtale for advarsler og kontraindikasjoner
- Vurdering av om en veterinærmedisinsk tilnærming er relevant

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

