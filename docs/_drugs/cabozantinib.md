---
layout: default
title: Cabozantinib
parent: Kun modellprediksjon (L5)
nav_order: 76
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
description: "Cabozantinib: predikert ny indikasjon Liposarkom (evidensnivå L5). Opprinnelig indikasjon: Nyrecellekarsinom og hepatocellulært karsinom"
monitor_inn: "CABOZANTINIB"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
---

# Cabozantinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Cabozantinib: Fra nyrecellekarsinom til liposarkom
{: .text-alpha }

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
| TxGNN-prediksjonsscore | 0,9983 |
| Evidensnivå | L5 (kun tidligfase-data for bløtvevssarkom; ingen liposarkomspesifikke resultater) |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Cabozantinib hemmer VEGFR2, MET og AXL. Disse reseptorene driver angiogenese og overlevelsessignalering i svulster, også i bløtvevssarkomer. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Cabozantinib (uoffisiell oversettelse): «Biokjemiske og/eller cellulære analyser in vitro har vist at kabozantinib hemmer tyrosinkinaseaktiviteten til MET, VEGFR-1, -2 og -3, AXL, RET, ROS1, TYRO3, MER, KIT, TRKB, FLT-3 og TIE-2. Disse reseptortyrosinkinasene er involvert både i normal cellefunksjon og i patologiske prosesser som onkogenese, metastasering, tumorangiogenese, legemiddelresistens og opprettholdelse av tumormikromiljøet.» Engelsk originaltekst: "In vitro biochemical and/or cellular assays have shown that cabozantinib inhibits the tyrosine kinase activity of MET, VEGFR-1, -2 and -3, AXL, RET, ROS1, TYRO3, MER, KIT, TRKB, FLT-3, and TIE-2. These receptor tyrosine kinases are involved in both normal cellular function and pathologic processes such as oncogenesis, metastasis, tumor angiogenesis, drug resistance, and maintenance of the tumor microenvironment." ([DailyMed: Cabometyx (cabozantinib) prescribing information, Exelixis, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3850cce2-6137-42e5-a792-d318c4a4b3b5), versjon av 2025-10-19; hentet 2026-11-20).

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
| EMEA/H/C/004163 | Cabometyx | Godkjent | Nyrecellekarsinom, hepatocellulært karsinom |
| EMEA/H/C/002640 | Cometriq | Godkjent | Skjoldbruskkjertelkreft |

Tilgjengelighet og regulatorisk status må derfor verifiseres før en eventuell videre satsing.

<!-- review:begin no-lic-20261106-cabozantinib-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Begge godkjenningene er registrert som avregistrert. Tilgjengelighet og regulatorisk status må derfor verifiseres før en eventuell videre satsing.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Antall godkjenninger i dataene: 2, hvorav gyldige: 2; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-cabozantinib-1 -->

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
Den høye TxGNN-scoren (0,9983) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Den støttes bare av én pågående fase 2-studie og én fase 1-studie. Begge gjelder bløtvevssarkom generelt og kombinasjonsbehandling, ikke liposarkom spesifikt. Legemidlet er markedsført i Norge, og 2 av 2 godkjenninger er gyldige.

**For å gå videre trengs følgende:**
- Resultater fra NCT05836571, med subgruppeanalyse for liposarkom
- Liposarkomspesifikke data, fortrinnsvis en egen fase 2-studie med cabozantinib som monoterapi
- Utfyllende sikkerhetsdata fra pakningsvedlegget (advarsler og kontraindikasjoner)
- Detaljerte mekanismedata (MOA) for å styrke den mekanistiske koblingen
- Avklaring av regulatorisk status og tilgjengelighet i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «Begge godkjenningene er registrert som avregistrert» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-20 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Cabometyx (cabozantinib) prescribing information, Exelixis, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3850cce2-6137-42e5-a792-d318c4a4b3b5) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

