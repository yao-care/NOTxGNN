---
layout: default
title: Cabozantinib
parent: Kun modellprediksjon (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cabozantinib: predikert ny indikasjon Liposarkom (evidensnivå L5). Opprinnelig indikasjon: Nyrecellekarsinom og hepatocellulært karsinom"
monitor_inn: "CABOZANTINIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
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

# Cabozantinib: Fra nyrecellekarsinom til liposarkom

## Oppsummering

Cabozantinib er en oral multikinasehemmer. Den er opprinnelig godkjent for nyrecellekarsinom, hepatocellulært karsinom og skjoldbruskkjertelkreft.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **liposarkom**.
Støtten er foreløpig begrenset: **1 klinisk studie** (fase 2, pågår) og **1 publikasjon** (fase 1) som gjelder bløtvevssarkom generelt, ikke liposarkom spesifikt.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Nyrecellekarsinom og hepatocellulært karsinom |
| Predikert ny indikasjon | Liposarkom |
| TxGNN-prediksjonsscore | 99,83 % |
| Evidensnivå | L3 (kun tidligfase-data for bløtvevssarkom; ingen liposarkomspesifikke resultater) |
| Markedsstatus i Norge | Kun avregistrerte (opphevede) godkjenninger |
| Antall godkjenninger | 2 (begge avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Cabozantinib hemmer VEGFR2, MET og AXL. Disse reseptorene driver angiogenese og overlevelsessignalering i svulster, også i bløtvevssarkomer. Detaljerte mekanismedata utover dette er ikke tilgjengelige i datagrunnlaget for rapporten.

Legemidlets effekt i nyrecellekarsinom og skjoldbruskkjertelkreft er godt dokumentert. Begge er solide svulster med avhengighet av angiogenese. Det gir et mekanistisk resonnement for at stoffet også kan virke i sarkomer. TxGNN-scoren er svært høy (0,998), men den er modellbasert.

Direkte sarkomevidens er foreløpig begrenset til tidligfasearbeid. Den eneste studien omfatter en blandet gruppe bløtvevssarkomer og kombinerer cabozantinib med immunterapi. Liposarkomspesifikk aktivitet er derfor ikke påvist.

---

## Klinisk studiedokumentasjon

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Fase 2 | Aktiv, rekrutterer ikke | 66 | Randomisert studie som sammenligner ipilimumab og nivolumab alene med samme kombinasjon pluss cabozantinib ved avansert bløtvevssarkom. Ingen resultater er publisert ennå (forventet avslutning mai 2028). |

Studien er relevant for sarkomgruppen, men ikke spesifikk for liposarkom. Fordi den bruker en kombinasjonsbehandling, er det vanskelig å isolere cabozantinibs bidrag.

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Fase 1-studie | American Journal of Clinical Oncology | Vurderte sikkerheten ved samtidig cabozantinib og strålebehandling som neoadjuvant behandling ved bløtvevssarkom i ekstremitetene. Bakgrunnen er at cabozantinib har vist aktivitet i flere sarkomsubtyper, mens bruk sammen med stråling har vært begrenset av frykt for fistel eller perforasjon. |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Status | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004163 | Cabometyx | Avregistrert | Nyrecellekarsinom, hepatocellulært karsinom |
| EMEA/H/C/002640 | Cometriq | Avregistrert | Skjoldbruskkjertelkreft |

Begge godkjenningene er registrert som avregistrert. Tilgjengelighet og regulatorisk status må derfor verifiseres før en eventuell videre satsing.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (multikinasehemmer, tyrosinkinasehemmer) |
| Myelosuppresjonsrisiko | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingsparametere | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndtering og beskyttelse | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Totalt 100 interaksjoner er registrert. De viktigste med alvorlighetsgrad **alvorlig (Major)** er:
  - acetylsalisylsyre
  - cisaprid
  - klaritromycin
  - dolasetron
  - granisetron
  - levofloksacin

  Flere interaksjoner av moderat alvorlighetsgrad er også registrert, blant annet loperamid, aprepitant, deksametason, bisakodyl, laktulose og klotrimazol.
- **Spesifikk bekymring ved sarkom**: Samtidig bruk med strålebehandling er begrenset av risikoen for fistel eller perforasjon (se fase 1-studien over).

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den høye TxGNN-scoren støttes bare av én pågående fase 2-studie og én fase 1-studie. Begge gjelder bløtvevssarkom generelt og kombinasjonsbehandling, ikke liposarkom spesifikt. I tillegg er alle norske godkjenninger avregistrert.

**For å gå videre trengs følgende:**
- Resultater fra NCT05836571, med subgruppeanalyse for liposarkom
- Liposarkomspesifikke data, fortrinnsvis en egen fase 2-studie med cabozantinib som monoterapi
- Utfyllende sikkerhetsdata fra pakningsvedlegget (advarsler og kontraindikasjoner)
- Detaljerte mekanismedata (MOA) for å styrke den mekanistiske koblingen
- Avklaring av regulatorisk status og tilgjengelighet i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

