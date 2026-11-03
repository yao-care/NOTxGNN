---
layout: default
title: Icatibant
parent: Kun modellprediksjon (L5)
nav_order: 204
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-03
monitor_inn: "ICATIBANT"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "Glanzmann thrombasthenia"]
description: "Icatibant: predikert ny indikasjon Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) (evidensnivå L5). Opprinnelig indikasjon: Angioedemas, Hereditary"
---

# Icatibant
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

## Icatibant: Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)
{: .text-alpha }

## Oppsummering

Icatibant er et peptidbasert legemiddel som blokkerer bradykininreseptorer, først og fremst B2-reseptoren.
TxGNN-modellen predikerer at det kan ha effekt ved **serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)**.
Det finnes **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen. Prediksjonen er derfor kun modellbasert.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Angioedemas, Hereditary |
| Predikert ny indikasjon | Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) |
| TxGNN-prediksjonsscore | 0.9999 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige fra legemiddeldatabasen. Farmakologidataene som er samlet inn for rapporten viser likevel at icatibant er en peptidantagonist som virker på bradykininreseptorene B1 (BDKRB1) og B2 (BDKRB2). Legemidlet hemmer dermed bradykininsignalering nedstrøms.

Den høye modellscoren skyldes trolig nettverksnærhet til serpin-relaterte gener i modellens biologiske nettverk. Sykdommen er definert av at feilfoldede serpiner polymeriserer og blir toksiske. Icatibant påvirker verken serpinfolding eller polymerisering, siden det virker på reseptornivå og ikke på selve proteinet.

Det er derfor ikke påvist noen mekanistisk sammenheng. Prediksjonen bør regnes som et beregningsmessig artefakt inntil motsatt er vist.

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

## Markedsinformasjon for Norge

Begge godkjenningene i dataene er gyldige.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000899 | Firazyr (Takeda Pharmaceuticals International AG) | Ikke oppgitt | Arvelig angioødem (opphevet) |
| EMEA/H/C/005083 | Icatibant Accord (Accord Healthcare S.L.U.) | Ikke oppgitt | Arvelig angioødem (opphevet) |

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner**: 12 interaksjonsposter er registrert. Ti av dem er av moderat alvorlighetsgrad og gjelder ACE-hemmere:
- benazepril
- captopril
- enalapril
- perindopril
- trandolapril
- moexipril
- lisinopril
- quinapril
- ramipril
- fosinopril

De to øvrige postene gjelder farmakologiske målproteiner (B1- og B2-reseptoren), ikke interaksjoner med andre legemidler.

Ut over dette henvises det til preparatomtalen for informasjon om advarsler og kontraindikasjoner.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (0,9999) uten kliniske studier, litteratur eller en plausibel mekanisme. Icatibant virker på bradykininreseptorer, mens sykdommen skyldes feilfoldede og polymeriserende serpiner. Evidensnivået er L5.

**For å gå videre kreves:**
- En plausibel mekanistisk hypotese som kobler bradykinin-B2-blokade til serpinpolymerisering, bekreftet i prekliniske modeller
- Publiserte studier eller registrerte kliniske studier som direkte omhandler denne sykdommen
- Sikkerhetsdata fra preparatomtalen (advarsler og kontraindikasjoner), som mangler i datagrunnlaget
- Data om virkningsmekanisme (MOA) fra legemiddeldatabasen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

