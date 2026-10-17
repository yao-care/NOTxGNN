---
layout: default
title: Insulin Lispro
parent: Kun modellprediksjon (L5)
nav_order: 221
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Insulin Lispro: predikert ny indikasjon Autoimmun oophoritt (evidensnivå L5). Opprinnelig indikasjon: Diabetes mellitus"
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Lispro
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

# Insulin lispro: Fra diabetes mellitus til autoimmun oophoritt

## Oppsummering i én setning

Insulin lispro er et hurtigvirkende insulinanalog som opprinnelig brukes til behandling av diabetes mellitus. TxGNN-modellen predikerer at det kan ha effekt ved **autoimmun oophoritt**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne prediksjonen. Prediksjonen er derfor ren modellberegning.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes mellitus |
| Predikert ny indikasjon | Autoimmun oophoritt |
| TxGNN-prediksjonsscore | 99,78 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalte/avregistrerte godkjenninger (ikke markedsført) |
| Antall godkjenninger | 4 (alle avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelig i de innsamlede dataene. Basert på kjent informasjon er insulin lispro et hurtigvirkende insulinanalog, og effekten ved diabetes mellitus er godt dokumentert gjennom metabolsk blodsukkerregulering.

Det finnes imidlertid ingen klar mekanistisk kobling til autoimmun oophoritt. Tilstanden innebærer immunmediert skade på eggstokkene, og insulinets metabolske virkning har ingen kjent sykdomsmodifiserende rolle her. En eventuell sammenheng er indirekte, for eksempel gjennom autoimmune polyglandulære syndromer som også omfatter type 1-diabetes. Den høye scoren bør derfor tolkes som en beregningsmessig prediksjon, ikke som et biologisk signal.

Andre prediksjoner med høy score i analysen er stort sett også av indirekte art:
- **Pankreasagenesi**: Insulinerstatning er standard behandling for den diabetiske fenotypen, men dette er erstatningsterapi og ikke ekte repurposing. Den ene funnede artikkelen (oversikt over insulinbehandling ved type 2-diabetes, 2002) er kun indirekte relevant.
- **Thiaminresponsivt syndrom, klassisk stiff person-syndrom og fokalt stiff limb-syndrom**: Koblingen går via samtidig diabetes eller anti-GAD-autoimmunitet, ikke via insulinets effekt på selve sykdommen.
- **Opsismodysplasi**: INPPL1 (SHIP2) regulerer insulin/PI3K-signalering negativt, noe som gir en mulig koblingsvei, men effektretningen er uklar.
- **Legemiddelindusert lokalisert lipodystrofi, sentrifugal lipodystrofi og trykkindusert lokalisert lipoatrofi**: Insulininjeksjon kan i seg selv forårsake lokal lipodystrofi. Dette er en bivirkning og ikke en terapeutisk mulighet.

---

## Klinisk studiedokumentasjon

For tiden er det ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

For den prioriterte prediksjonen (autoimmun oophoritt) foreligger det for tiden ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000088 | Humalog | – | Diabetes mellitus |
| EMEA/H/C/005037 | Lyumjev (tidligere Liumjev) | – | Diabetes mellitus |
| EMEA/H/C/000393 | Liprolog | – | Diabetes mellitus |
| EMEA/H/C/004303 | Insulin lispro Sanofi | – | Diabetes mellitus |

Alle fire godkjenningene er avregistrert, og det finnes ingen gyldige godkjenninger.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner**: Interaksjonssøket er fullført og viser totalt 100 registrerte interaksjoner. Av disse er 20 oppført i de innsamlede dataene, og de fleste er av moderat alvorlighetsgrad. Eksempler:
- **Moderat**: fenylefrin, acebutolol, acetazolamid, formoterol, pseudoefedrin, doksycyklin, adrenalin, levonorgestrel, hydrokortison, albiglutid, salbutamol, etanol, hydroklortiazid, alogliptin, metformin, østradiol, alpelisib, etinyløstradiol
- **Mindre alvorlig**: topisk hydrokortison, topisk alklometason

Mange av disse påvirker blodsukkeret og kan forsterke eller svekke insulineffekten. Dette bør vurderes ved samtidig bruk.

**Annen sikkerhetsmerknad**: Insulin kan forårsake lokal lipodystrofi (lipohypertrofi/lipoatrofi) på injeksjonssteder. Dette er relevant for tolkningen av flere av prediksjonene over.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen om autoimmun oophoritt bygger kun på modellscore (L5), uten kliniske studier, litteratur eller en klar mekanistisk kobling. Ingen av de øvrige predikerte indikasjonene representerer reell repurposing, da de enten er standard diabetesbehandling eller knyttet til bivirkninger. I tillegg har legemidlet ingen gyldige godkjenninger i Norge.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA)
- Sikkerhetsopplysninger fra preparatomtalen (advarsler og kontraindikasjoner)
- Prekliniske eller kliniske data som viser en faktisk effekt ved autoimmun oophoritt
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

