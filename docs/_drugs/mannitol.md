---
layout: default
title: Mannitol
parent: Kun modellprediksjon (L5)
nav_order: 257
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Mannitol: predikert ny indikasjon Nefrogent syndrom med uhensiktsmessig antidiurese (evidensnivå L5). Opprinnelig indikasjon: Cystisk fibrose"
monitor_inn: "MANNITOL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
---

# Mannitol
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

## Mannitol: Fra cystisk fibrose til nefrogent syndrom med uhensiktsmessig antidiurese
{: .text-alpha }

## Oppsummering i én setning

Mannitol er et osmotisk middel som opprinnelig ble godkjent (som Bronchitol, inhalasjon) for behandling av cystisk fibrose. TxGNN-modellen predikerer at det kan være effektivt ved **nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)**, men det finnes **ingen kliniske studier** og bare **én generell oversiktsartikkel** som ikke støtter bruken. Prediksjonen er dermed ikke underbygd av klinisk evidens.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cystisk fibrose |
| Predikert ny indikasjon | Nefrogent syndrom med uhensiktsmessig antidiurese |
| TxGNN-prediksjonsscore | 0,9997 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelig i de sammenstilte dataene. Basert på kjent informasjon er mannitol et osmotisk diuretikum, og effekten ved cystisk fibrose skyldes at det trekker vann inn i luftveisslimet og bedrer slimtransporten.

Mekanismen gir liten støtte for den predikerte indikasjonen. NSIAD skyldes aktiverende mutasjoner i vasopressin V2-reseptoren, så defekten ligger på reseptornivå og er ikke osmotisk. Mannitol kan i tillegg forverre hyponatremi gjennom osmotiske vannforskyvninger. Den høye scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

### Andre predikerte indikasjoner (kort oversikt)

| Rang | Predikert indikasjon | Score | Evidensnivå | Vurdering |
|---|---|---|---|---|
| 2 | Akutt pulmonal hjertesykdom | 0,9988 | L5 | Indirekte, historiske rapporter (ARDS, lungeødem); mannitol kan øke intravaskulært volum og belaste høyre hjerte |
| 3 | Anstrengelsesutløst malign hypertermi | 0,9986 | L5 | Ingen mekanistisk kobling, ingen litteratur |
| 5 | Familiær periodisk paralyse | 0,9975 | L4 | Kun rolle som bærevæske for kalium |
| 6 | Hypokalemisk periodisk paralyse | 0,9972 | L4 | Støttende rolle som fortynningsmiddel, ikke sykdomsmodifiserende |
| 7 | Medfødt multicore-myopati med ekstern oftalmoplegi | 0,9972 | L5 | Ingen evidens |
| 8 | Moderat multiminicore-sykdom med håndaffeksjon | 0,9971 | L5 | Ingen evidens |
| 9 | Nefrogen diabetes insipidus | 0,9970 | L5 | Osmotisk diurese kan forverre polyuri og dehydrering |
| 10 | Sentral kjerne-myopati (central core) | 0,9969 | L5 | Ingen evidens |

---

## Klinisk studieevidens

Det er for tiden ikke registrert noen relaterte kliniske studier for nefrogent syndrom med uhensiktsmessig antidiurese.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Oversikt | European Journal of Internal Medicine | Gjennomgang av ti vanlige fallgruver ved utredning av hyponatremi; omtaler ikke mannitol som behandling ved NSIAD |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001252 | Bronchitol (Pharmaxis Europe Limited) | Ikke oppgitt | Cystisk fibrose (status: godkjent) |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner (fra kunnskapsgrafen, ikke preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter mannitol til blant annet leversvikt, leversykdom, hepatisk encefalopati/koma, anuri, nedsatt nyrefunksjon, lungeødem, intrakraniell blødning, trombocytopeni, nøytropeni, agranulocytose, anemi, porfyri, gallblæresykdom, søvnapné, angstlidelse, dysthymi og rusrelaterte lidelser.
- **Legemiddelinteraksjoner:** Til sammen 100 interaksjoner er registrert. Blant de viktigste er:
  - **Alvorlig (Major):** amikacin
  - **Moderat:** litium-/lamivudin-relaterte kombinasjoner (lamivudin), formoterol, salbutamol, arformoterol, amifostin, benazepril, captopril, karbamazepin, cisatrakurium, citalopram, desvenlafaxin, kanagliflozin, dapagliflozin, bisakodyl, pikosulfat, polyetylenglykol med elektrolytter, jotalaminsyre og diatrizoat
  - **Mindre (Minor):** doksysyklin

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den høye TxGNN-scoren (0,9997) er ikke støttet av kliniske studier eller relevant litteratur, og mekanismen (reseptornivådefekt ved NSIAD, risiko for forverret hyponatremi) taler snarere imot bruk. Produktet er markedsført i Norge, med 1 gyldig markedsføringstillatelse av 1. Ingen av de ti predikerte indikasjonene har evidens utover L4.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra DMP for sikkerhetsscreening
- Prekliniske eller kliniske data som direkte undersøker mannitol ved den predikerte indikasjonen
- Avklaring av doseringsform og administrasjonsvei som kan være aktuell for den nye indikasjonen
- Vurdering av om andre predikerte indikasjoner (for eksempel akutt pulmonal hjertesykdom) er mer lovende enn rang 1
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

