---
layout: default
title: Guanfacine
parent: Kun modellprediksjon (L5)
nav_order: 199
evidence_level: L5
indication_count: 7
monitor_inn: "Guanfacine"
predicted_indications: ["faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "trichotillomania", "manic bipolar affective disorder", "restless legs syndrome", "Tourette syndrome"]
last_modified_at: 2026-11-20
description: "Guanfacine: predikert ny indikasjon Aarskog-Scott-syndrom (faciodigitogenital syndrome) (evidensnivå L5). Opprinnelig indikasjon: Attention Deficit Disorder with Hyperactivity"
---

# Guanfacine
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

## Guanfacin: alfa-2A-adrenerg agonist → Familiært digitogenitalt ansiktssyndrom (faciodigitogenital syndrome)
{: .text-alpha }

## Oppsummering i én setning

Guanfacin er en selektiv alfa-2A-adrenerg reseptoragonist som brukes ved attention deficit-lidelse med hyperaktivitet (ADHD). TxGNN-modellen predikerer at legemidlet kan ha effekt ved **Aarskog-Scott-syndrom (faciodigitogenital syndrome)**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen i dataene som er samlet inn for denne rapporten. Prediksjonen bygger kun på modellsignalet.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Attention Deficit Disorder with Hyperactivity |
| Predikert ny indikasjon | Aarskog-Scott-syndrom (faciodigitogenital syndrome) |
| TxGNN-prediksjonsscore | 0,9997 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Guanfacine (uoffisiell oversettelse): «Guanfacin er en sentral alfa 2A -adrenerg reseptoragonist. Guanfacin er ikke et sentralstimulerende middel (CNS-stimulerende middel). Virkningsmekanismen til guanfacin ved ADHD er ikke kjent.» Engelsk originaltekst: "Guanfacine is a central alpha 2A -adrenergic receptor agonist. Guanfacine is not a central nervous system (CNS) stimulant. The mechanism of action of guanfacine in ADHD is not known." ([DailyMed: Guanfacine Extended-Release (guanfacine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3ec4fed6-cafc-49a0-9540-8d70ac435769), versjon av 2026-10-15; hentet 2026-11-19). Guanfacin er kjent som en agonist på alfa-2A-adrenoreseptoren (i tillegg til at den binder alfa-2B og alfa-2C), og denne mekanismen forbedrer signaloverføring i prefrontal cortex, noe som er relevant for oppmerksomhet og eksekutive funksjoner.

Aarskog-Scott-syndrom er en X-bundet utviklingsforstyrrelse forårsaket av mutasjoner i FGD1-genet. Det er ikke identifisert noen plausibel mekanistisk kobling mellom alfa-2A-agonisme og denne sykdommen. Enkelte pasienter har ADHD-lignende atferd, men dette er spekulativt og ikke støttet av noen data. Prediksjonen må derfor regnes som et rent modellsignal uten biologisk eller klinisk begrunnelse.

## Klinisk studieevidens

Foreløpig ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig ingen relatert litteratur tilgjengelig.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/006312 | Paxneury | – | – |
| EMEA/H/C/003759 | Intuniv | – | – |

Markedsstatus for guanfacin i Norge er registrert som markedsført.

## Sikkerhetsvurderinger

Pakningsvedlegg med advarsler og kontraindikasjoner er ikke tilgjengelig i dataene som er samlet inn for denne rapporten. Følgende farmakologiske opplysninger foreligger:

- **Legemiddelinteraksjoner:** Datasettet inneholder kun farmakologiske målproteiner, ikke egentlige interaksjoner med andre legemidler. Guanfacin binder alfa-2A-, alfa-2B- og alfa-2C-adrenoreseptorene.

For øvrig sikkerhetsinformasjon, se pakningsvedlegget.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen har svært høy modellscore (0,9997), men mangler helt støtte fra kliniske studier og litteratur, og det finnes ingen plausibel mekanistisk kobling mellom guanfacin og Aarskog-Scott-syndrom. Evidensnivået er derfor L5.

**For å gå videre kreves følgende:**
- En biologisk begrunnelse for hvordan alfa-2A-agonisme kan påvirke FGD1-relaterte symptomer
- Prekliniske eller kliniske data som direkte omhandler denne sykdommen
- Detaljerte data om virkningsmekanisme (MOA)
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner)

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Guanfacine Extended-Release (guanfacine) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3ec4fed6-cafc-49a0-9540-8d70ac435769) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

