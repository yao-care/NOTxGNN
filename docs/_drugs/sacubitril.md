---
layout: default
title: Sacubitril
parent: Kun modellprediksjon (L5)
nav_order: 374
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-04
monitor_inn: "SACUBITRIL"
predicted_indications: ["brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "rheumatoid arthritis", "hemoglobinopathy"]
description: "Sacubitril: predikert ny indikasjon Brain small vessel disease 1 with or without ocular anomalies (evidensnivå L5). Sentrale EU-godkjenninger (EMA): 2 (gyldige: 2)"
---

# Sacubitril
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

## Sacubitril: Brain small vessel disease 1 with or without ocular anomalies
{: .text-alpha }

## Kort oppsummering

Sacubitril er en nepriylsinhemmer som brukes sammen med valsartan. TxGNN-modellen forutsier at legemidlet kan ha effekt ved **hjernens småkarsykdom type 1 med eller uten øyeanomalier (brain small vessel disease 1 with or without ocular anomalies)**. Det finnes **ingen kliniske studier** og **ingen publikasjoner** som direkte undersøker sacubitril ved denne sykdommen, så prediksjonen bygger kun på modellen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke registrert i de lokale dataene |
| Predikert ny indikasjon | Brain small vessel disease 1 with or without ocular anomalies |
| TxGNN-prediksjonsscore | 0.9958 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for sacubitril and valsartan (kombinasjonspreparat med Sacubitril) (uoffisiell oversettelse): «Sakubitril og valsartan inneholder en neprilysinhemmer, sakubitril, og en angiotensinreseptorblokker, valsartan. Sakubitril og valsartan hemmer neprilysin (nøytral endopeptidase; NEP) via LBQ657, den aktive metabolitten av prodrugen sakubitril, og blokkerer angiotensin II type 1 (AT 1 )-reseptoren via valsartan.» Engelsk originaltekst: "Sacubitril and valsartan contains a neprilysin inhibitor, sacubitril, and an angiotensin receptor blocker, valsartan. Sacubitril and valsartan inhibits neprilysin (neutral endopeptidase; NEP) via LBQ657, the active metabolite of the prodrug sacubitril, and blocks the angiotensin II type-1 (AT 1 ) receptor via valsartan." ([DailyMed: sacubitril and valsartan prescribing information, Novadoz Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44db8114-622e-41f6-96a1-447d47b0267c), versjon av 2026-10-30; hentet 2026-11-19). Sacubitril er en prodrug som gir nepriylsinhemming, noe som øker nivået av natriuretiske peptider. Det gis i kombinasjon med valsartan, en angiotensinreseptorblokker.

Sykdommen er en monogen, COL4A1-relatert tilstand med defekter i basalmembran og karintegritet. Ut fra de tilgjengelige dataene finnes det ingen påvist biologisk mekanisme som kobler nepriylsinhemming eller angiotensinreseptorblokkade til denne patologien. Den høye modellscoren er derfor ikke støttet av noe mekanistisk grunnlag i de sammenstilte dataene.

## Klinisk studiedokumentasjon

Foreløpig er det ingen relaterte kliniske studier registrert.

## Litteraturdokumentasjon

Den eneste litteraturen som ble funnet i forbindelse med denne prediksjonen, omhandler sacubitril/valsartan ved svikt i systemisk høyre ventrikkel, som er en annen sykdom. Den gir ingen evidens for effekt ved hjernens småkarsykdom type 1, og er derfor ikke listet som støtte.

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004343 | Neparvis | – | Hjertesvikt (opphevet) |
| EMEA/H/C/004062 | Entresto | – | Hjertesvikt (opphevet) |

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (6 registrerte, alle av moderat alvorlighetsgrad):
- Nitisinon
- Rosuvastatin
- Simvastatin
- Kobicistat
- Revefenacin
- Alpelisib

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (evidensnivå L5). Ingen studie har undersøkt sacubitril ved hjernens småkarsykdom type 1, og det er ikke påvist noen plausibel mekanisme for sykdommen.

**For å gå videre trengs følgende:**
- Data om virkningsmekanisme (MOA) og en eventuell biologisk kobling til COL4A1-relatert karpatologi
- Prekliniske studier som direkte undersøker sykdommen
- Gjennomgang av preparatomtale for advarsler og kontraindikasjoner, særlig med tanke på hypotensjon og hyperkalemi

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: sacubitril and valsartan prescribing information, Novadoz Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=44db8114-622e-41f6-96a1-447d47b0267c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

