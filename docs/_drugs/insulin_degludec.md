---
layout: default
title: Insulin Degludec
parent: Kun modellprediksjon (L5)
nav_order: 216
evidence_level: L5
indication_count: 5
monitor_inn: "INSULIN DEGLUDEC"
predicted_indications: ["autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome"]
last_modified_at: 2026-11-20
description: "Insulin Degludec: predikert ny indikasjon Autoimmun ooforitt (autoimmune oophoritis) (evidensnivå L5). Opprinnelig indikasjon: Diabetes Mellitus"
---

# Insulin Degludec
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Insulin degludec: insulinreseptoragonist → autoimmun ooforitt (autoimmune oophoritis)
{: .text-alpha }

## Sammendrag

Insulin degludec er en langtidsvirkende insulinanalog som brukes til behandling av diabetes. TxGNN-modellen predikerer at den kan ha effekt ved **autoimmun ooforitt (autoimmune oophoritis)**. Det finnes imidlertid **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen i de innsamlede dataene.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes Mellitus; Diabetes Mellitus, Type 2 |
| Predikert ny indikasjon | Autoimmun ooforitt (autoimmune oophoritis) |
| TxGNN-prediksjonsscore | 0,9923 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Insulin Degludec (uoffisiell oversettelse): «Den primære aktiviteten til insulin, inkludert TRESIBA, er regulering av glukosemetabolismen. Insulin og dets analoger senker blodglukose ved å stimulere perifert glukoseopptak, særlig i skjelettmuskulatur og fettvev, og ved å hemme glukoseproduksjonen i leveren.» Engelsk originaltekst: "The primary activity of insulin, including TRESIBA, is regulation of glucose metabolism. Insulin and its analogs lower blood glucose by stimulating peripheral glucose uptake, especially by skeletal muscle and fat, and by inhibiting hepatic glucose production." ([DailyMed: Tresiba (insulin degludec) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8ccd2f4-6ba9-4839-87f8-4742dc9b1c17), versjon av 2024-02-22; hentet 2026-11-19). Insulin degludec er en insulinanalog som virker via insulinreseptoren, og det er ingen kjent mekanistisk kobling mellom dette og autoimmun ooforitt.

Den høye scoren (0,9923) kan trolig skyldes nettverksassosiasjoner med autoimmun endokrin sykdom, for eksempel polyglandulær autoimmunitet som opptrer sammen med type 1-diabetes. Uten støtte fra studier bør prediksjonen regnes som et modellartefakt inntil det motsatte er vist. Likhet med den opprinnelige indikasjonen er ikke vurdert.

## Klinisk evidens

Foreløpig er det ikke registrert noen relaterte kliniske studier.

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

## Informasjon om det norske markedet

Dataene som er samlet inn for denne rapporten, viser tre lisenser for produkter som inneholder insulin degludec. Markedsstatus er registrert som markedsført.

| Lisensnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002498 | Tresiba | – | Diabetes mellitus |
| EMEA/H/C/002499 | Ryzodeg | – | Diabetes mellitus |
| EMEA/H/C/002647 | Xultophy | – | Diabetes mellitus, type 2 |

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er registrert 100 interaksjoner i dataene. De fleste som er listet, er av moderat alvorlighetsgrad. Blant dem er:
  - Fenylefrin, acebutolol, formoterol, pseudoefedrin, adrenalin, salbutamol (kan svekke blodsukkerkontroll eller maskere hypoglykemi)
  - Hydrokortison, østradiol, levonorgestrel, noretisteron
  - Andre antidiabetika: albiglutid, alogliptin, metformin, pioglitazon
  - Doksycyklin, etanol, hydroklortiazid, alpelisib
  - Mindre alvorlige: topikal hydrokortison og topikal alklometason

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en høy modellscore uten kliniske studier, publikasjoner eller en klar mekanistisk kobling. Den mest sannsynlige forklaringen er assosiasjoner i nettverksdata knyttet til autoimmun endokrin sykdom.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA)
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner)
- Prekliniske eller mekanistiske studier som direkte belyser autoimmun ooforitt
- Vurdering av likhet med den opprinnelige indikasjonen og av administrasjonsvei

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Tresiba (insulin degludec) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8ccd2f4-6ba9-4839-87f8-4742dc9b1c17) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

