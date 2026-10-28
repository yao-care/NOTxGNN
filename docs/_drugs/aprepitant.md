---
layout: default
title: Aprepitant
parent: Kun modellprediksjon (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Aprepitant: predikert ny indikasjon Nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD) (evidensnivå L5). Opprinnelig indikasjon: Oppkast"
monitor_inn: "APREPITANT"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

## Aprepitant: Fra oppkast og kvalme til nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)
{: .text-alpha }

## Oppsummering i én setning

Aprepitant er en NK1-reseptorantagonist, opprinnelig brukt mot oppkast, postoperativ kvalme og oppkast og kreftrelatert kvalme.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)**,
men det finnes **ingen kliniske studier og ingen relevant litteratur** som støtter denne retningen. Prediksjonen bygger kun på modellscore.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Oppkast; postoperativ kvalme og oppkast; kreft (kreftrelatert kvalme) |
| Predikert ny indikasjon | Nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD) |
| TxGNN-prediksjonsscore | 0,9997 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Aprepitant er kjent som en NK1-reseptorantagonist, og effekten ved kvalme og oppkast er godt dokumentert. Om den kan overføres til NSIAD, er likevel høyst usikkert.

Prekliniske arbeider antyder at substans P/NK1-signalering kan påvirke regulering av vasopressin og vannbalanse. NSIAD skyldes imidlertid aktiverende mutasjoner i V2-reseptoren (AVPR2), som virker nedstrøms for frisetting av vasopressin. NK1-blokade forventes derfor ikke å påvirke selve grunnfeilen. Koblingen er spekulativ og støttes kun av TxGNN-scoren.

### Andre predikerte indikasjoner

Datagrunnlaget inneholder ni ytterligere prediksjoner. Alle har evidensnivå L5, ingen kliniske studier og anbefalingen Hold:

| Rang | Sykdom | TxGNN-score | Vurdering |
|------|------|------|------|
| 2 | Hypertrikose | 0,9991 | Ingen klar mekanisme; ikke støttet av kliniske data |
| 3 | Pulmonal hypertensjon | 0,9990 | Mekanistisk hypotese er plausibel, men ikke validert |
| 4 | Lepra | 0,9990 | Spekulativ kobling; effektiv behandling finnes allerede |
| 5 | Ambras-type hypertrichosis universalis congenita | 0,9987 | Ingen mekanistisk eller klinisk støtte |
| 6 | Misdannelsessyndrom med tann- og/eller periodontal komponent | 0,9986 | Ingen plausibel mekanisme |
| 7 | Kyfoskoliotisk hjertesykdom | 0,9986 | NK1-mekanisme adresserer ikke den strukturelle årsaken |
| 8 | Syndrom med Dandy-Walker-malformasjon | 0,9986 | Utviklingsmessig misdannelse; ingen støtte |
| 9 | Subaraknoidalblødning | 0,9985 | Mest biologisk plausible; kandidat for prekliniske oppfølgingsstudier |
| 10 | Isolert genetisk hårskaftavvik | 0,9985 | Ingen kjent mekanisme |

Blant alle de predikerte indikasjonene har subaraknoidalblødning den mest biologisk plausible begrunnelsen. Prekliniske studier antyder at substans P/NK1-signalering bidrar til brudd på blod-hjerne-barrieren og hjerneødem etter hjerneskade.

---

## Klinisk studieevidens

Foreløpig er ingen relaterte kliniske studier registrert for den predikerte indikasjonen.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig for den predikerte indikasjonen (NSIAD).

For informasjon: Under rang 3 (pulmonal hypertensjon) ble én publikasjon koblet til prediksjonen, [PMID 28261651](https://pubmed.ncbi.nlm.nih.gov/28261651/) (2016, *Oncology and Therapy*). Dette er en fase I-studie av pazopanib i kombinasjon med cisplatin ved avanserte solide svulster. Den omhandler verken aprepitant eller pulmonal hypertensjon og regnes som en feilaktig kobling uten støttende verdi.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000527 | Emend | Ikke oppgitt | Oppkast; postoperativ kvalme og oppkast; kreft |

Tillatelsen er gyldig. Legemidlet er markedsført i Norge, med 1 gyldig tillatelse av 1.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner (fra kunnskapsgraf):** Kunnskapsgrafen i TxGNN (PrimeKG) viser en kontraindikasjonskobling til **leversvikt**. Dette er ikke hentet fra preparatomtale.
- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er identifisert. Et utvalg:
  - **Alvorlige (Major):** fentanyl, alfentanil, acalabrutinib
  - **Moderate:** paklitaksel, abemaciklib, rabeprazol, nifedipin, ibuprofen, levonorgestrel, hydrokortison, albendazol, fluvoksamin, fosamprenavir, fosfenytoin, fostamatinib, gefitinib, lidokain, dihydrokodein
  - **Mindre (Minor):** dolutegravir

Se preparatomtalen for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for NSIAD har kun modellscore som støtte (evidensnivå L5). Det finnes ingen kliniske studier eller litteratur, og mekanismen er lite sannsynlig siden NSIAD skyldes en V2-reseptordefekt nedstrøms for vasopressin. Legemidlet er markedsført i Norge, med 1 gyldig tillatelse av 1.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel som blokkerer sikkerhetsscreening)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske data som støtter NK1-blokade ved NSIAD, eller alternativt prioritering av subaraknoidalblødning for preklinisk oppfølging
- Avklaring av doseringsformer og administrasjonsveier
- Avklaring av legemidlets regulatoriske status i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

