---
layout: default
title: Spironolactone
parent: Kun modellprediksjon (L5)
nav_order: 392
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Spironolactone: predikert ny indikasjon Hypotrichosis simplex i hodebunnen (evidensnivå L5). Opprinnelig indikasjon: Ødem"
monitor_inn: "SPIRONOLACTONE"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
---

# Spironolactone
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

## Spironolakton: Fra ødem og hjertesvikt til hypotrichosis simplex i hodebunnen
{: .text-alpha }

## Oppsummering

Spironolakton er en mineralokortikoidreseptorantagonist med antiandrogen effekt. Den er opprinnelig godkjent for ødem, hjertesvikt, levercirrhose, ascites, nefrotisk syndrom, hyperaldosteronisme og essensiell hypertensjon.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **hypotrichosis simplex i hodebunnen**, men for øyeblikket finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ødem; hjertesvikt; levercirrhose; ascites; nefrotisk syndrom; hyperaldosteronisme; essensiell hypertensjon |
| Predikert ny indikasjon | Hypotrichosis simplex i hodebunnen |
| TxGNN-prediksjonsscore | 0,9926 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Spironolactone (uoffisiell oversettelse): «Spironolakton og dets aktive metabolitter er spesifikke farmakologiske antagonister av aldosteron, og virker hovedsakelig gjennom kompetitiv binding av reseptorer på det aldosteronavhengige natrium-kalium-utvekslingsstedet i den distale kronglete nyretubulus. Spironolakton fører til at økte mengder natrium og vann skilles ut, mens kalium holdes tilbake.» Engelsk originaltekst: "Spironolactone and its active metabolites are specific pharmacologic antagonists of aldosterone, acting primarily through competitive binding of receptors at the aldosterone-dependent sodium-potassium exchange site in the distal convoluted renal tubule. Spironolactone causes increased amounts of sodium and water to be excreted, while potassium is retained." ([DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc), versjon av 2025-11-28; hentet 2026-11-19). Ut fra kjent informasjon er spironolakton en mineralokortikoidreseptorantagonist med betydelig antiandrogen aktivitet, det vil si blokkering av androgenreseptoren og redusert androgensyntese.

Denne antiandrogene effekten er plausibel ved hårtap der androgensignalering bidrar til miniaturisering av hårsekkene, og spironolakton brukes utenfor godkjent indikasjon (off-label) ved kvinnelig hårtap av mønstertype. Hypotrichosis simplex i hodebunnen er imidlertid en sjelden arvelig hårtapslidelse, som vanligvis skyldes varianter i gener som CDSN, APCDD1 eller RPL21, og den er ikke primært androgendrevet.

Den høye TxGNN-scoren (0,9926) er dermed kun en beregnet prediksjon. Det er ikke etablert noen direkte mekanistisk kobling til den underliggende genetiske patologien, og manglende MOA-data begrenser den mekanistiske vurderingen ytterligere.

Den rangerte neste prediksjonen, **medfødt hypotrichosis med milia** (score 0,9904), har enda svakere støtte: den bygger på en generell, indirekte antiandrogen begrunnelse og trolig på nettverkslikhet med andre hypotrichosis-fenotyper, uten validert mekanisme. Heller ikke her er det funnet kliniske studier eller litteratur.

---

## Klinisk studiedokumentasjon

For øyeblikket er det ikke registrert noen relaterte kliniske studier.

---

## Litteraturdokumentasjon

For øyeblikket finnes det ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005535 | Qaialdo | – | Ødem; hjertesvikt; levercirrhose; ascites; nefrotisk syndrom; hyperaldosteronisme; essensiell hypertensjon |

Legemidlet er markedsført, og 1 av 1 markedsføringstillatelser er gyldig.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner/sykdommer med kjent risiko (fra kunnskapsgrafen, ikke fra preparatomtale):** nyresykdom, pyoureter, pankreatitt, systemisk lupus erythematosus (inkludert pediatrisk form), kaliummangel, diabetes mellitus, diabetisk ketoacidose, hyperurikemi, hyperparatyreoidisme, osteitis fibrosa, hepatisk koma, hepatisk encefalopati, neonatal ikterus, anuri, urinsyregikt, hyperkalsemi, nefrokalsinose og forstyrrelser i fosformetabolismen.
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Blant de første 20 som er vist, er **loperamid** klassifisert som **alvorlig (Major)**. De fleste øvrige er av moderat alvorlighetsgrad, blant annet hydrokortison, deksametason, betametason, triamcinolon, budesonid, metformin, bupropion, morfin, bisakodyl, rcensorolje (kastorolje), dronabinol, eksenatid og SGLT2-hemmere (kanagliflozin, dapagliflozin, empagliflozin, ertugliflozin). Doksycyklin, acetylsalisylsyre og fidaksomicin er klassifisert som mindre (Minor).

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes kun av en modellscore (evidensnivå L5), uten kliniske studier eller litteratur. Sykdommen er en sjelden genetisk tilstand som ikke primært er androgendrevet, og den eneste godkjenningen i Norge er kansellert.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og en klargjøring av en mulig mekanistisk kobling til de underliggende genene (CDSN, APCDD1, RPL21)
- Advarsler og kontraindikasjoner fra preparatomtalen, som i dag mangler og blokkerer sikkerhetsscreeningen
- Litteratursøk og prekliniske data for hypotrichosis simplex og medfødt hypotrichosis med milia
- Avklaring av administrasjonsvei og formulering (f.eks. topikal vs. oral), siden doseringsform og rutekompatibilitet ikke er vurdert

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

