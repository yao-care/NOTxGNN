---
layout: default
title: Safinamide
parent: Kun modellprediksjon (L5)
nav_order: 375
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Safinamide: predikert ny indikasjon Rasmussens subakutte encefalitt (evidensnivå L5). Opprinnelig indikasjon: Parkinsons sykdom"
monitor_inn: "safinamide"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration"]
---

# Safinamide
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Safinamid: Fra Parkinsons sykdom til Rasmussens subakutte encefalitt
{: .text-alpha }

## Oppsummering i én setning

Safinamid er en MAO-B-hemmer som opprinnelig brukes til behandling av Parkinsons sykdom.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **Rasmussens subakutte encefalitt**,
men **ingen kliniske studier** og **ingen publikasjoner** støtter foreløpig denne prediksjonen. Den er kun en modellbasert hypotese.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Parkinsons sykdom |
| Predikert ny indikasjon | Rasmussens subakutte encefalitt |
| TxGNN-prediksjonsscore | 0,9963 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de innsamlede dataene. Ut fra generell kunnskap er safinamid en reversibel MAO-B-hemmer som også blokkerer spenningsstyrte natriumkanaler og hemmer frigjøring av glutamat. Dette er ikke verifisert mot dataene som er kompilert for denne rapporten.

Disse egenskapene kan i teorien dempe nevronal overeksitabilitet og eksitotoksisitet, noe som er relevant for anfallene ved Rasmussens encefalitt. Sykdommen drives imidlertid hovedsakelig av T-celleformidlet autoimmun betennelse, og den påvirkes ikke av safinamid. Prediksjonen kan derfor høyst gi en symptomatisk effekt, ikke en sykdomsmodifiserende.

**Andre predikerte indikasjoner** (alle på evidensnivå L5, anbefaling Hold):

| Rangering | Sykdom | TxGNN-score | Vurdering |
|------|------|------|------|
| 2 | Myelitt | 0,9946 | Rent spekulativ. Nevrobeskyttende effekt er ikke påvist ved inflammatoriske eller demyeliniserende ryggmargstilstander. |
| 3 | PLA2G6-assosiert nevrodegenerasjon | 0,9922 | Biologisk mest sammenhengende. Sykdommen har parkinsonisme og alfa-synuklein-patologi, som gir et symptomatisk argument for en MAO-B-hemmer. Den underliggende defekten påvirkes trolig ikke. |

---

## Klinisk evidens

Det er foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det foreligger foreløpig ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002396 | Xadago | Ikke oppgitt | Parkinsons sykdom |

Denne godkjenningen (Zambon SpA) er **gyldig**. Legemidlet er markedsført i Norge, med 1 gyldig godkjenning av 1.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er registrert 110 interaksjoner i den kompilerte interaksjonsdatabasen (DDInter). Eksempler på de viktigste:
  - **Alvorlig (Major)**: Bupropion
  - **Moderat**: Isomethepten, klorpropamid, dietylpropion, empagliflozin, fentermin, glimepirid, ulike insuliner (aspart, degludek, detemir, glargin, glulisin, humant isofan, humant regulært, inhalert), metoklopramid, nateglinid, repaglinid, rosuvastatin, acetoheksamid

Se preparatomtalen for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene hviler utelukkende på en modellscore uten støtte fra kliniske studier eller litteratur (L5). Den mekanistiske koblingen er svak for Rasmussens encefalitt og myelitt, fordi disse er immunmedierte. Dessuten er den norske godkjenningen kansellert, og viktige sikkerhetsdata mangler.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Verifiserte data om virkningsmekanisme (MOA) fra DrugBank
- Systematisk litteratur- og studiesøk for de tre predikerte indikasjonene, med prioritet på PLA2G6-assosiert nevrodegenerasjon
- Prekliniske data eller modellstudier som viser effekt på anfall eller nevrodegenerasjon
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

