---
layout: default
title: Bempedoic Acid
parent: Kun modellprediksjon (L5)
nav_order: 55
evidence_level: L5
indication_count: 9
monitor_inn: "BEMPEDOIC ACID"
predicted_indications: ["hyperthyroidism", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "hyperthyroxinemia", "drug-induced osteoporosis", "multiple endocrine neoplasia", "pregnancy associated osteoporosis"]
last_modified_at: 2026-11-24
description: "Bempedoic Acid: predikert ny indikasjon Hypertyreose (hyperthyroidism) (evidensnivå L5). Opprinnelig indikasjon: Hypercholesterolemia"
---

# Bempedoic Acid
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

## Bempedoinsyre: ACL-hemmer → hypertyreose (hyperthyroidism)
{: .text-alpha }

## Oppsummering i én setning

Bempedoinsyre er en kolesterolsenkende legemiddelsubstans som hemmer enzymet ATP-citratlyase i leveren.
TxGNN-modellen predikerer at den kan ha effekt ved **hypertyreose (hyperthyroidism)**,
men det finnes **ingen kliniske studier** og **ingen publikasjoner** i de samlede dataene som støtter denne retningen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hypercholesterolemia;Dyslipidemias |
| Predikert ny indikasjon | Hypertyreose (hyperthyroidism) |
| TxGNN-prediksjonsscore | 0,9961 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Bempedoic Acid (uoffisiell oversettelse): «Bempedoinsyre er en adenosintrifosfat-citratlyase (ACL)-hemmer som senker LDL-C ved å hemme kolesterolsyntesen i leveren. ACL er et enzym oppstrøms for 3-hydroksy-3-metyl-glutaryl-koenzym A (HMG-CoA)-reduktase i kolesterolets biosyntesevei.» Engelsk originaltekst: "Bempedoic acid is an adenosine triphosphate-citrate lyase (ACL) inhibitor that lowers LDL-C by inhibition of cholesterol synthesis in the liver. ACL is an enzyme upstream of 3-hydroxy-3-methyl-glutaryl-coenzyme A (HMG-CoA) reductase in the cholesterol biosynthesis pathway." ([DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9), versjon av 2026-06-25; hentet 2026-11-19). Bempedoinsyre er kjent som en hemmer av ATP-citratlyase (ACL), som virker på kolesterolsyntesen i leveren. Det finnes ingen data som knytter denne virkningen til overskudd av thyreoideahormon.

Det er derfor ikke etablert noen mekanistisk sammenheng mellom legemidlets virkning og hypertyreose. Den høye scoren er en grafbasert modellprediksjon uten støtte fra kliniske studier eller litteratur, og må tolkes med stor forsiktighet.

## Kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004958 | Nilemdo | bempedoic acid | Hypercholesterolemia; Dyslipidemias | Gyldig |
| EMEA/H/C/004959 | Nustendi | bempedoic acid; ezetimibe | Hypercholesterolemia; Dyslipidemias | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

## Sikkerhetsmomenter

**Legemiddelinteraksjoner:** Det er registrert 23 interaksjoner. Blant de viktigste:
- **Alvorlige (Major):** kortikosteroider (hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednisolon, prednison, metylprednisolon, deflazakort, fludrokortison), levofloksacin og simvastatin.
- **Moderate:** empagliflozin, glyburid, repaglinid, rifaksimin, rosuvastatin, seleksipag, feksofenadin og revefenacin.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for hypertyreose er kun modellbasert (evidensnivå L5), uten kliniske studier, litteratur eller kjent mekanisme som støtter den. Det er ikke grunnlag for å gå videre nå.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og en hypotese som kobler ACL-hemming til thyreoideafunksjon
- Prekliniske eller kliniske data som direkte studerer hypertyreose
- Gjennomgang av preparatomtalens advarsler og kontraindikasjoner, som mangler i de samlede dataene
- Vurdering av interaksjonene, særlig med kortikosteroider og statiner

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Nexletol (bempedoic acid) prescribing information, Esperion Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=88d06d89-a3da-40b4-b273-8f4f7d56c4c9) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

