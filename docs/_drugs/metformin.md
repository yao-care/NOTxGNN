---
layout: default
title: Metformin
parent: Kun modellprediksjon (L5)
nav_order: 265
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Metformin: predikert ny indikasjon Fokalt stivt lem-syndrom (evidensnivå L5). Opprinnelig indikasjon: Diabetes mellitus, type 2"
monitor_inn: "METFORMIN"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
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

## Metformin: Fra type 2-diabetes til fokalt stivt lem-syndrom
{: .text-alpha }

## Oppsummering i én setning

Metformin er et legemiddel som opprinnelig brukes til behandling av type 2-diabetes. TxGNN-modellen forutsier at det kan ha effekt på **fokalt stivt lem-syndrom** (focal stiff limb syndrome). Det finnes foreløpig **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen, så prediksjonen er rent modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Diabetes mellitus, type 2 |
| Predikert ny indikasjon | Fokalt stivt lem-syndrom |
| TxGNN-prediksjonsscore | 99,45 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte (alle godkjenninger er trukket tilbake) |
| Antall godkjenninger | 19 (0 gyldige, 19 avregistrerte) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Metformin er kjent som et legemiddel mot type 2-diabetes, og er i dette datagrunnlaget registrert både som enkeltstoff og som del av kombinasjonspreparater (for eksempel med DPP-4-hemmere og SGLT2-hemmere). Det finnes imidlertid ingen dokumentert mekanisme som knytter metformin til fokalt stivt lem-syndrom.

Fokalt stivt lem-syndrom er en autoimmun eller nevrologisk stivhetstilstand i det stive menneske-spekteret. Ingen etablert signalvei forbinder metformins kjente effekter (som AMPK-aktivering og hemming av glukoneogenese i lever) med denne sykdommen. Den høye scoren er trolig et resultat av nærhet mellom sykdommer i modellens kunnskapsgraf, ikke av en terapeutisk mekanisme. Samme score (99,45 %) ble gitt for klassisk stiv person-syndrom, noe som tyder på et felles signal i kunnskapsgrafen. Enhver begrunnelse er derfor spekulativ.

---

## Evidens fra kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Markedsinformasjon for Norge

Alle 19 godkjenninger er avregistrert, og ingen er gyldige i dag. Nedenfor vises fem av dem.

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005738 | Vildagliptin / Metformin hydrochloride Accord | – | Diabetes mellitus, type 2 |
| EMEA/H/C/002654 | Vipdomet | – | Diabetes mellitus, type 2 |
| EMEA/H/C/001049 | Zomarist | – | Diabetes mellitus, type 2 |
| EMEA/H/C/004162 | Ebymect | – | Diabetes mellitus, type 2 |
| EMEA/H/C/002672 | Xigduo | – | Diabetes mellitus, type 2 |

---

## Sikkerhetsvurderinger

**Kontraindikasjoner (fra kunnskapsgraf):** Disse er hentet fra relasjoner mellom legemiddel og sykdom i TxGNN-kunnskapsgrafen, ikke fra preparatomtalen. Blant dem er:
- Lever- og nyresvikt, lever- og nyresykdom
- Bukspyttkjertelbetennelse (pankreatitt)
- Gallblæresykdom
- Hjertesvikt (kongestiv)
- Binyrebarksvikt
- Hypofysesvikt og beslektede hypofysehormonmangler (inkl. Sheehans syndrom)
- Hypogonadotrop hypogonadisme (inkl. Kallmanns syndrom)
- Sykdom i thymus

**Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert. Eksempler på de viktigste:
- **Alvorlige (Major):** acetazolamid, etanol (alkohol)
- **Moderate:** blant annet dolutegravir, abemaciklib, fenylefrin, ranitidin, formoterol, pseudoefedrin, ketorolak, nifedipin, adrenalin, ibuprofen, etinyløstradiol, hydrokortison, salbutamol, hydroklortiazid, acetoheksamid
- **Mindre (Minor):** akarbose, topisk hydrokortison, topisk alklometason

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Andre predikerte indikasjoner (til orientering)

Alle har evidensnivå L5, ingen studier eller litteratur, og anbefalingen Hold:

| Rang | Sykdom | Score |
|------|------|------|
| 2 | Klassisk stiv person-syndrom | 99,45 % |
| 3 | Opsismodysplasi | 99,40 % |
| 4 | Tiaminresponsivt dysfunksjonssyndrom | 99,40 % |
| 5 | Legemiddelindusert lokalisert lipodystrofi | 99,06 % |

Blant disse har legemiddelindusert lokalisert lipodystrofi den mest plausible biologiske begrunnelsen (bedret insulinfølsomhet, metformin er studert ved andre lipodystrofier), men uten data for denne konkrete tilstanden. Ved tiaminresponsivt dysfunksjonssyndrom kan metformins samspill med transportproteiner også utgjøre en sikkerhetsbekymring.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore (evidensnivå L5) uten kliniske studier, litteratur eller en støttet mekanistisk kobling. Alle norske godkjenninger er dessuten avregistrert.

**For å gå videre trengs følgende:**
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra legemiddelmyndighetene (blokkerende for sikkerhetsscreening)
- Litteratursøk og søk etter pågående studier for fokalt stivt lem-syndrom
- Prekliniske eller mekanistiske data som kan underbygge en kobling til tilstanden
- Vurdering av administrasjonsvei og legemiddelform
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

