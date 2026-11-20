---
layout: default
title: Abaloparatide
parent: Kun modellprediksjon (L5)
nav_order: 12
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Abaloparatide: predikert ny indikasjon Non-syndromisk esofagusmisdannelse (evidensnivå L5). Opprinnelig indikasjon: Postmenopausal osteoporose / osteoporose"
monitor_inn: "ABALOPARATIDE"
drugbank_id: DB05084
predicted_indications: ["non-syndromic esophageal malformation", "esophageal disease", "amenorrhea (disease)", "esophageal ulcer"]
---

# Abaloparatide
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

## Abaloparatid: Fra postmenopausal osteoporose til non-syndromisk esofagusmisdannelse
{: .text-alpha }

## Oppsummering i én setning

Abaloparatid er en analog av parathyroideahormon-relatert protein (PTHrP) som opprinnelig brukes til behandling av postmenopausal osteoporose.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **non-syndromisk esofagusmisdannelse**,
men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen, så prediksjonen bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Postmenopausal osteoporose / osteoporose |
| Predikert ny indikasjon | Non-syndromisk esofagusmisdannelse |
| TxGNN-prediksjonsscore | 0,9984 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Abaloparatide (uoffisiell oversettelse): «Abaloparatid er en PTHrP(1-34)-analog som virker som agonist på PTH1-reseptoren (PTH1R). Dette fører til aktivering av cAMP-signalveien i målceller. Administrering av abaloparatid én gang daglig stimulerer ny bendannelse på trabekulære og kortikale benoverflater ved stimulering av osteoblastaktivitet.» Engelsk originaltekst: "Abaloparatide is a PTHrP(1-34) analog which acts as an agonist at the PTH1 receptor (PTH1R). This results in activation of the cAMP signaling pathway in target cells. Once-daily administration of abaloparatide stimulates new bone formation on trabecular and cortical bone surfaces by stimulation of osteoblastic activity." ([DailyMed: Tymlos (abaloparatide) prescribing information, Radius Health, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=712143d9-e21e-4013-bb3b-3426a21060a8), versjon av 2026-08-11; hentet 2026-11-19). Basert på kjent informasjon er abaloparatid en PTHrP-analog som aktiverer PTH1-reseptoren (PTH1R) og stimulerer beindannelse. Effekten ved postmenopausal osteoporose er dokumentert, blant annet i fase 3-studien NCT01343004, der legemidlet reduserte risikoen for nye brudd sammenlignet med placebo.

Det er ikke funnet noen plausibel farmakologisk sammenheng mellom PTH1R-agonisme og korrigering av medfødte misdannelser i spiserøret, som er utviklingsmessige defekter. Den høye TxGNN-scoren (0,9984) er en ren modellprediksjon uten støtte i studier eller litteratur.

Modellen peker også på tre andre sykdommer, alle uten evidens (evidensnivå L5, anbefaling Hold):

- **Esofagussykdom** (score 0,9975): PTHrP uttrykkes i esofagusepitel og kan ha en rolle i epitelial differensiering, men dette er spekulativt. Benaktive legemidler (f.eks. orale bisfosfonater) er dessuten oftere forbundet med esofagusirritasjon enn nytte.
- **Amenoré** (score 0,9972): Sammenhengen er indirekte. Abaloparatid virker ikke på hypotalamus-hypofyse-ovarie-aksen og kunne i teorien bare påvirke benkomplikasjonen, ikke selve amenoréen. Legemidlet er ikke indisert til premenopausale kvinner.
- **Esofagussår** (score 0,9902): Ingen kjent rolle for den benanabole virkningen i slimhinnetilheling.

---

## Klinisk evidens

Foreløpig er det ingen registrerte kliniske studier knyttet til denne prediksjonen.

---

## Litteraturevidens

Foreløpig finnes ingen relevant litteratur for denne prediksjonen.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005928 | Eladynos | – | Postmenopausal osteoporose / osteoporose |

Merk: Legemidlet er markedsført, og 1 av 1 markedsføringstillatelse er gyldig.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (3 funnet):

- **Kalsitriol (topisk)**: moderat interaksjonsnivå
- **Kalsipotriol (topisk)**: moderat interaksjonsnivå
- **PTH1-reseptor**: farmakologisk målprotein (ikke en egentlig interaksjon); ingen interaksjonsnivå angitt

For advarsler og kontraindikasjoner, se preparatomtalen (pakningsvedlegget).

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten kliniske studier, litteratur eller plausibel mekanistisk forklaring. Sikkerhetsdata fra preparatomtalen mangler.

<!-- review:begin no-lic-20261106-abaloparatide-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «I tillegg er den eneste godkjenningen i Norge avregistrert, og sikkerhetsdata fra preparatomtalen mangler.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-abaloparatide-1 -->

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel)
- Detaljerte data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske eller mekanistiske studier som kan underbygge en kobling mellom PTH1R-signalering og esofagusutvikling eller -tilheling
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «I tillegg er den eneste godkjenningen i Norge avregistrert, og s» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Tymlos (abaloparatide) prescribing information, Radius Health, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=712143d9-e21e-4013-bb3b-3426a21060a8) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

