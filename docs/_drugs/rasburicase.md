---
layout: default
title: Rasburicase
parent: Kun modellprediksjon (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Rasburicase: predikert ny indikasjon Renal hypourikemi (evidensnivå L5). Opprinnelig indikasjon: Hyperurikemi"
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "hepatoportal sclerosis", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
---

# Rasburicase
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Rasburikase: Fra hyperurikemi til renal hypourikemi
{: .text-alpha }

## Oppsummering i én setning

Rasburikase er et rekombinant urat-oksidaseenzym som opprinnelig ble brukt mot **hyperurikemi**. TxGNN-modellen predikerer at det kan være effektivt ved **renal hypourikemi**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er sannsynligvis et grafbasert artefakt og ikke et reelt terapeutisk signal.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hyperurikemi |
| Predikert ny indikasjon | Renal hypourikemi |
| TxGNN-prediksjonsscore | 99,99 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Basert på kjent informasjon er rasburikase et urat-oksidaseenzym som omdanner urinsyre til allantoin og dermed senker serumnivået av urinsyre. Effekten ved hyperurikemi, særlig i forbindelse med tumorlysesyndrom, er godt etablert.

Renal hypourikemi er imidlertid allerede en tilstand med lav serumurinsyre, forårsaket av defekt renal reabsorpsjon av urat (for eksempel varianter i SLC22A12/URAT1 eller SLC2A9). Ytterligere nedbryting av urinsyre gir ingen terapeutisk begrunnelse og kan være skadelig. Den høye TxGNN-scoren skyldes trolig assosiasjoner i kunnskapsgrafen via urinsyrestoffskiftet, ikke en reell behandlingseffekt.

Også de øvrige ni predikerte indikasjonene (blant annet delvis HGPRT-mangel, hepatisk porfyri, hepatoportal sklerose, portvenetrombose, hepatopulmonalt syndrom, renal tubulær acidose og forstyrrelser i fenylalaninstoffskiftet) mangler både klinisk evidens og biologisk plausibilitet. Flere av dem har identiske scorer, noe som tyder på et felles artefakt i grafen. Alle er vurdert til evidensnivå L5 og «Hold».

---

## Klinisk studieevidens

Det er foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er foreløpig ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000331 | Fasturtec | – | Hyperurikemi |

Tillatelsen har status avregistrert. Det finnes ingen gyldige tillatelser i dag.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Totalt 13 interaksjoner er identifisert.
  - **Alvorlige (Major)**: prilokain og salpetersyrling (nitrous acid).
  - **Moderate**: tetrakain (oftalmisk og topikal), lidokain (topikal og oftalmisk), benzokain (topikal), kokain (topikal og nasal), proparakain (oftalmisk), oksybuprokain (oftalmisk), cinkokain (topikal) og idelalisib.
- **Andre sikkerhetshensyn knyttet til prediksjonene**: Rasburikase er immunogent og har begrenset bruk ved gjentatt dosering. Det er også risiko for hemolyse og methemoglobinemi, særlig ved G6PD-mangel. Dette er en særlig bekymring ved metabolske og leversykdommer.

Se preparatomtalen for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen om renal hypourikemi mangler både klinisk evidens og mekanistisk støtte, og ytterligere senking av urinsyre er biologisk uhensiktsmessig ved en tilstand som allerede kjennetegnes av lav urinsyre. Produktet er dessuten avregistrert i Norge.

**For å gå videre kreves følgende:**
- Innhenting og analyse av preparatomtale (advarsler og kontraindikasjoner), da dette er en blokkerende datamangel for sikkerhetsscreening
- Data om virkningsmekanisme (MOA) fra DrugBank
- Biologisk eller prekliniske data som kan underbygge en reell sammenheng med noen av de predikerte indikasjonene
- Avklaring av regulatorisk status og tilgjengelighet i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

