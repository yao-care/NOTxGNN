---
layout: default
title: Mannitol
parent: Kun modellprediksjon (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: Fra cystisk fibrose til nefrogent syndrom med uhensiktsmessig antidiurese

## Oppsummering i én setning

Mannitol er et osmotisk middel som opprinnelig ble godkjent (som Bronchitol, inhalasjon) for behandling av cystisk fibrose. TxGNN-modellen predikerer at det kan være effektivt ved **nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)**, men det finnes **ingen kliniske studier** og bare **én generell oversiktsartikkel** som ikke støtter bruken. Prediksjonen er dermed ikke underbygd av klinisk evidens.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cystisk fibrose |
| Predikert ny indikasjon | Nefrogent syndrom med uhensiktsmessig antidiurese |
| TxGNN-prediksjonsscore | 99,97 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall godkjenninger | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelig i de sammenstilte dataene. Basert på kjent informasjon er mannitol et osmotisk diuretikum, og effekten ved cystisk fibrose skyldes at det trekker vann inn i luftveisslimet og bedrer slimtransporten.

Mekanismen gir liten støtte for den predikerte indikasjonen. NSIAD skyldes aktiverende mutasjoner i vasopressin V2-reseptoren, så defekten ligger på reseptornivå og er ikke osmotisk. Mannitol kan i tillegg forverre hyponatremi gjennom osmotiske vannforskyvninger. Den høye TxGNN-scoren er derfor trolig et utslag av assosiasjoner i kunnskapsgrafen og ikke et uttrykk for reell klinisk nytte.

### Andre predikerte indikasjoner (kort oversikt)

| Rang | Predikert indikasjon | Score | Evidensnivå | Vurdering |
|---|---|---|---|---|
| 2 | Akutt pulmonal hjertesykdom | 99,88 % | L4 | Indirekte, historiske rapporter (ARDS, lungeødem); mannitol kan øke intravaskulært volum og belaste høyre hjerte |
| 3 | Anstrengelsesutløst malign hypertermi | 99,86 % | L5 | Ingen mekanistisk kobling, ingen litteratur |
| 4 | Malign hypertermi (disposisjon) | 99,80 % | L4 | Mannitol er hjelpestoff i dantrolen; litteraturen gjelder dantrolen |
| 5 | Familiær periodisk paralyse | 99,75 % | L4 | Kun rolle som bærevæske for kalium |
| 6 | Hypokalemisk periodisk paralyse | 99,72 % | L4 | Støttende rolle som fortynningsmiddel, ikke sykdomsmodifiserende |
| 7 | Medfødt multicore-myopati med ekstern oftalmoplegi | 99,72 % | L5 | Ingen evidens |
| 8 | Moderat multiminicore-sykdom med håndaffeksjon | 99,71 % | L5 | Ingen evidens |
| 9 | Nefrogen diabetes insipidus | 99,70 % | L5 | Osmotisk diurese kan forverre polyuri og dehydrering |
| 10 | Sentral kjerne-myopati (central core) | 99,69 % | L5 | Ingen evidens |

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
| EMEA/H/C/001252 | Bronchitol (Pharmaxis Europe Limited) | Ikke oppgitt | Cystisk fibrose (status: avregistrert) |

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
Den høye TxGNN-scoren (99,97 %) er ikke støttet av kliniske studier eller relevant litteratur, og mekanismen (reseptornivådefekt ved NSIAD, risiko for forverret hyponatremi) taler snarere imot bruk. Produktet har dessuten ingen gyldig markedsføringstillatelse i Norge. Ingen av de ti predikerte indikasjonene har evidens utover L4.

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

