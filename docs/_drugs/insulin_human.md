---
layout: default
title: Insulin Human
parent: Kun modellprediksjon (L5)
nav_order: 220
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Insulin Human: predikert ny indikasjon Autoimmun oofoitt (evidensnivå L5). Opprinnelig indikasjon: Diabetes mellitus"
monitor_inn: "INSULIN HUMAN"
predicted_indications: ["autoimmune oophoritis", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy"]
---

# Insulin Human
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmasøytens vurderingsrapport

</div>

# Humaninsulin: Fra diabetes mellitus til autoimmun oofoitt

## Oppsummering i én setning

Humaninsulin er et hormon som opprinnelig brukes til behandling av diabetes mellitus.
TxGNN-modellen forutsier at det kan ha effekt ved **autoimmun oofoitt** (autoimmune oophoritis),
men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes mellitus |
| Predikert ny indikasjon | Autoimmun oofoitt |
| TxGNN-prediksjonsscore | 99,84 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte (trukket tilbake) |
| Antall godkjenninger | 5 (alle avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data som er samlet inn for denne rapporten inneholder ikke detaljerte opplysninger om virkningsmekanisme. Basert på kjent informasjon er humaninsulin et hormon som aktiverer insulinreseptoren og styrer glukoseopptak og stoffskifte. Effekten ved diabetes mellitus er godt dokumentert.

Det finnes en mulig, men uverifisert kobling: insulinsignalering påvirker granulosaceller i eggstokken og steroidproduksjon. Dette støtter likevel ikke en immunmodulerende rolle ved autoimmun oofoitt. Tilstanden behandles vanligvis med immunsuppresjon eller hormonerstatning, og insulin har ingen etablert plass i behandlingen.

Den høye TxGNN-scoren (0,998) er en beregningsmessig prediksjon og må ikke tolkes som klinisk støtte.

### Andre predikerte indikasjoner (alle L5, Hold)

De ti øverste prediksjonene mangler alle kliniske studier og litteratur. Flere kan forklares av forvekslende sammenhenger:

| Rangering | Predikert indikasjon | Score | Vurdering |
|------|------|------|------|
| 1 | Autoimmun oofoitt | 99,84 % | Ingen etablert rolle for insulin |
| 2 | Klassisk stiff person-syndrom | 99,81 % | Forvekslet: anti-GAD65-autoimmunitet og samtidig type 1-diabetes; insulin behandler diabetesen, ikke den nevrologiske sykdommen |
| 3 | Fokalt stiff limb-syndrom | 99,81 % | Samme forvekslede sammenheng som over |
| 4 | Tiaminresponsivt dysfunksjonssyndrom | 99,80 % | Diabetes er en del av fenotypen; tiamin er sykdomsspesifikk behandling |
| 5 | Opsismodysplasi | 99,79 % | Spekulativ kobling via INPPL1 (SHIP2) i insulin/PI3K-signalveien; effektretning uklar |
| 6 | Legemiddelindusert lokalisert lipodystrofi | 99,72 % | Kjent bivirkning av injisert insulin; bør behandles som sikkerhetssignal |
| 7 | Sentrifugal lipodystrofi | 99,70 % | Fenotypeoverlapp; ingen holdepunkter for nytte |
| 8 | Trykkindusert lokalisert lipoatrofi | 99,70 % | Fenotypeoverlapp med lipoatrofi på injeksjonssteder |
| 9 | Pankreasagenesi | 99,70 % | Insulinerstatning er rasjonell, men er symptomatisk diabetesbehandling innenfor den opprinnelige indikasjonen, ikke ekte repurposing |
| 10 | Idiopatisk lokalisert lipodystrofi | 99,68 % | Fenotypelikhet; ingen støttende mekanisme |

---

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Evidens fra litteratur

Foreløpig finnes det ingen relatert litteratur.

---

## Informasjon om det norske markedet

Alle fem godkjenninger er registrert som avregistrert (cancelled), og ingen er gyldige i dag.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000442 | Protaphane | – | Diabetes mellitus |
| EMEA/H/C/000427 | Actraphane | – | Diabetes mellitus |
| EMEA/H/C/000201 | Insuman | – | Diabetes mellitus |
| EMEA/H/C/000441 | Insulatard | – | Diabetes mellitus |
| EMEA/H/C/000428 | Mixtard | – | Diabetes mellitus |

---

## Sikkerhetsvurderinger

Data om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for sikkerhetsinformasjon.

**Legemiddelinteraksjoner:** Interaksjonssøket er gjennomført og fant 100 registrerte interaksjoner. Blant de første 20 som er vist, er de fleste av moderat alvorlighetsgrad:

- **Moderat:** fenylefrin, acebutolol, acetazolamid, pseudoefedrin, doksycyklin, adrenalin, etinylestradiol, hydrokortison, albiglutid, salbutamol, etanol, hydroklortiazid, alogliptin, metformin, pioglitazon, østradiol, alpelisib, benazepril
- **Mindre:** hydrokortison (topisk), alklometason (topisk)

Mange av disse påvirker blodsukkeret, og hypoglykemi eller svekket glukosekontroll er derfor relevant å overvåke.

**Sikkerhetssignal knyttet til prediksjonene:** Lokal lipodystrofi og lipoatrofi er kjente bivirkninger av injisert insulin. Slike predikerte indikasjoner bør ikke tolkes som terapeutiske muligheter.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for autoimmun oofoitt er kun beregningsbasert (L5) uten kliniske studier eller litteratur, og insulin har ingen kjent immunmodulerende rolle ved tilstanden. Flere av de øvrige prediksjonene gjenspeiler forvekslende sammenhenger (samtidig diabetes) eller bivirkninger. Produktene er dessuten alle avregistrert i Norge.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Prekliniske eller kliniske data som viser nytte ved autoimmun oofoitt
- Avklaring av administrasjonsvei og formuleringer, siden doseringsform mangler og alle norske godkjenninger er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

