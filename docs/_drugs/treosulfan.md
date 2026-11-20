---
layout: default
title: Treosulfan
parent: Kun modellprediksjon (L5)
nav_order: 435
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
description: "Treosulfan: predikert ny indikasjon Diabetisk katarakt (evidensnivå L5). Opprinnelig indikasjon: Hematopoetisk stamcelletransplantasjon"
monitor_inn: "TREOSULFAN"
predicted_indications: ["diabetic cataract"]
---

# Treosulfan
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Treosulfan: Fra hematopoetisk stamcelletransplantasjon til diabetisk katarakt
{: .text-alpha }

## Oppsummering i én setning

Treosulfan er et alkylerende middel som opprinnelig brukes som forbehandling (kondisjonering) før hematopoetisk stamcelletransplantasjon.
TxGNN-modellen predikerer at det kan ha effekt mot **diabetisk katarakt**, men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen.
Prediksjonen er ren modellberegning, og det er faktisk holdepunkter som peker mot en mulig skaderisiko for linsen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hematopoetisk stamcelletransplantasjon |
| Predikert ny indikasjon | Diabetisk katarakt |
| TxGNN-prediksjonsscore | 0,9901 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Clinical Pharmacology» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Treosulfan (uoffisiell oversettelse): «Treosulfan er et alkylerende middel. DNA-alkylering antas å være årsaken til de cytotoksiske virkningene av treosulfan. Treosulfan viste aktivitet som tømmer hematopoetiske stamceller, samt immunsuppressiv og antitumoral aktivitet i musemodeller for leukemi.» Engelsk originaltekst: "Treosulfan is an alkylating agent. DNA alkylation is thought to be responsible for the cytotoxic activities of treosulfan. Treosulfan showed hematopoietic stem cell depleting activity as well as immunosuppressive and antitumor activity in mouse models of leukemia." ([DailyMed: Grafapex (treosulfan) prescribing information, Medexus Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d06b03c-17aa-0492-e063-6294a90abd8f), versjon av 2025-01-31; hentet 2026-11-19). Ut fra generell farmakologisk kunnskap er treosulfan et bifunksjonelt alkylerende middel. Det er et prodrug som omdannes til epoksidmellomprodukter som danner kryssbindinger i DNA, og det brukes i kondisjonering før stamcelletransplantasjon.

Diabetisk katarakt skyldes hovedsakelig aktivering av polyolveien (aldosereduktase og opphopning av sorbitol), oksidativt stress og glykering av proteiner i linsen. Det er ingen åpenbar mekanistisk kobling mellom DNA-alkylering og disse prosessene. Den høye TxGNN-scoren (0,9901) er kun en beregnet prediksjon og støttes ikke av noen studie eller litteratur.

Systemiske alkylerende midler og kondisjoneringsregimer er dessuten forbundet med økt risiko for katarakt (for eksempel etter total kroppsbestråling eller busulfanbasert kondisjonering). Dette taler mot nytte og reiser en mulig sikkerhetsbekymring.

---

## Evidens fra kliniske studier

Foreløpig er ingen relevante kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes ingen relevant litteratur.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004751 | Trecondi | Ikke oppgitt | Hematopoetisk stamcelletransplantasjon |

Merk: Legemidlet er markedsført, og 1 av 1 godkjenning er gyldig.

---

## Sikkerhetsvurderinger

- **Katarakt som mulig bekymring**: Alkylerende midler og kondisjoneringsregimer er assosiert med økt kataraktrisiko, noe som er relevant ved en indikasjon som diabetisk katarakt.

Ut over dette bes du se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon. Data om interaksjoner ble ikke funnet i de innsamlede dataene.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (L5) uten støtte fra kliniske studier, litteratur eller en plausibel mekanisme. Et cytotoksisk alkylerende middel er lite egnet for en kronisk, ikke-malign øyesykdom. Preparatet er markedsført i Norge, og 1 av 1 godkjenning er gyldig.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske data (f.eks. linsemodeller) som kan belyse en eventuell mekanistisk kobling
- Vurdering av kataraktrisiko og av om administrasjonsvei er forenlig med en øyeindikasjon

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Grafapex (treosulfan) prescribing information, Medexus Pharma, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d06b03c-17aa-0492-e063-6294a90abd8f) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

