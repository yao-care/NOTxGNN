---
layout: default
title: Moroctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 276
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Moroctocog Alfa: predikert ny indikasjon Primær frigjøringsforstyrrelse i blodplater (evidensnivå L5). Opprinnelig indikasjon: Hemofili A"
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
---

# Moroctocog Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **8** stk.
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

## Moroktokog alfa: Fra hemofili A til primær frigjøringsforstyrrelse i blodplater
{: .text-alpha }

## Oppsummering i én setning

Moroktokog alfa er et rekombinant faktor VIII-preparat (B-domene-delert) som opprinnelig brukes til behandling av **hemofili A**.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **primær frigjøringsforstyrrelse i blodplater**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hemofili A |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse i blodplater |
| TxGNN-prediksjonsscore | 0.9997 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Det foreligger for øyeblikket ingen detaljerte data om virkningsmekanisme. Basert på kjent informasjon er moroktokog alfa et rekombinant faktor VIII-erstatningspreparat. Effekten ved hemofili A er godt kjent, men mekanistisk er det lite som tyder på at det virker ved den predikerte indikasjonen.

Primære frigjøringsforstyrrelser i blodplater skyldes iboende defekter i blodplatenes granula- og sekresjonsfunksjon, ikke mangel på faktor VIII. Tilførsel av faktor VIII vil derfor ikke korrigere den underliggende defekten. Den høye scoren (0.9997) kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

### Andre predikerte indikasjoner (alle evidensnivå L5, anbefaling Hold)

| Rang | Sykdom | Score | Mekanistisk vurdering |
|---|------|------|------|
| 2 | Pseudo-von Willebrands sykdom | 0,9997 | Løs kobling via VWF–FVIII-aksen, men primærdefekten sitter i blodplatene (GPIbα) |
| 3 | Glanzmanns trombasteni | 0,9996 | Defekt i integrin αIIbβ3; FVIII adresserer ikke aggregasjonsdefekten |
| 4 | Ervervet koagulasjonsfaktormangel | 0,9988 | Mekanistisk mest plausibel, men gruppen er heterogen (f.eks. ervervet hemofili A med hemmere der FVIII er lite egnet) |
| 5 | Scotts syndrom | 0,9986 | Defekt i fosfatidylserin-eksponering (TMEM16F), ikke FVIII-mengde |
| 6 | Blødningsdiatese ved kollagenreseptordefekt | 0,9973 | Defekte kollagenreseptorer (GPVI/α2β1); ingen støtte |
| 7 | Hemoragisk lidelse ved konstitusjonell trombocytopeni | 0,9972 | Blødning skyldes blodplatemangel, ikke FVIII-mangel |
| 8 | «Flood factor deficiency» | 0,9911 | Uklart sykdomsnavn, trolig navneartefakt; må avklares |

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000232 | ReFacto AF (Pfizer Europe MA EEIG) | Ikke oppgitt | Hemofili A (status: godkjent) |

---

## Sikkerhetsvurderinger

Data om sikkerhet er ikke tilgjengelige i det kompilerte datagrunnlaget. Se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon. Det er heller ikke funnet registrerte legemiddelinteraksjoner eller kontraindikasjoner fra kunnskapsgrafen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle predikerte indikasjoner er kun modellbaserte (L5) uten kliniske studier eller litteratur. For de fleste kandidatene er den mekanistiske koblingen svak fordi defektene ligger i blodplatene og ikke i faktor VIII. Preparatet er dessuten kun registrert som avregistrert i Norge.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Dersom man vil utforske videre: fokusere på «ervervet koagulasjonsfaktormangel» med en presis sykdomsdefinisjon og en målrettet litteratur- og studiesøk
- Avklaring av sykdomsentiteten «flood factor deficiency»
- Vurdering av preparatets tilgjengelighet i Norge, siden tillatelsen er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

