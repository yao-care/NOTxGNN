---
layout: default
title: Regorafenib
parent: Kun modellprediksjon (L5)
nav_order: 352
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Regorafenib: predikert ny indikasjon Liposarkom (evidensnivå L5). Opprinnelig indikasjon: Kolorektal kreft (Colorectal Neoplasms)"
---

# Regorafenib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **8** stk.
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

# Regorafenib: Fra tykk- og endetarmskreft til liposarkom

## Oppsummering i én setning

Regorafenib er en oral multikinasehemmer som opprinnelig ble godkjent for behandling av kolorektal kreft.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **liposarkom**,
men evidensen er blandet: det finnes **1 fullført fase 2-studie** og **9 publikasjoner**, og de randomiserte studiene viser at regorafenib **ikke** ga tydelig nytte i liposarkomgruppen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kolorektal kreft (Colorectal Neoplasms) |
| Predikert ny indikasjon | Liposarkom |
| TxGNN-prediksjonsscore | 99,76 % |
| Evidensnivå | L1 (etter datagrunnlagets klassifisering; se merknad under) |
| Status i Norge | Kun tilbakekalt/avregistrert (Cancelled only) |
| Antall markedsføringstillatelser | 1 (0 gyldige, 1 kansellert) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med forbehold) |

*Merknad om evidensnivå: Datagrunnlaget klassifiserer evidensen som L1 fordi det finnes randomiserte, placebokontrollerte fase 2-studier. Disse er imidlertid ikke to fullførte fase 3-studier, og den liposarkom-spesifikke studien var negativ. Evidensen bør derfor tolkes forsiktig.*

---

## Hvorfor er denne prediksjonen rimelig?

Regorafenib er en multikinasehemmer som blokkerer flere signalveier: VEGFR1–3, TIE2 (angiogenese), PDGFR og FGFR (stromale), samt KIT, RET og RAF (onkogene). Disse veiene driver karnydannelse og tumorvekst ved bløtdelssarkomer, inkludert liposarkom.

Kolorektal kreft og sarkom er ulike sykdommer, men legemidlets virkning på angiogenese og vekstsignalering er ikke begrenset til én krefttype. Regorafenib er også etablert ved gastrointestinal stromacelletumor (GIST), og i REGOSARC-studien (randomisert, placebokontrollert fase 2) gav det bedre progresjonsfri overlevelse ved ikke-adipocytære sarkomer.

Det er imidlertid en viktig begrensning: i både REGOSARC og liposarkomkohorten i SARC024 var aktiviteten **begrenset eller fraværende ved liposarkom**. SARC024-forfatterne konkluderer at resultatene «ikke støtter rutinemessig bruk av regorafenib» i denne pasientgruppen. Den høye modellscoren bør derfor ikke tolkes som bekreftet klinisk nytte. Detaljerte mekanismedata fra legemiddeldatabasen var ikke tilgjengelige; beskrivelsen over bygger på publisert litteratur.

---

## Klinisk studieevidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Fullført | 131 | SARC024: paraplyprotokoll for oral regorafenib ved utvalgte sarkomtyper, inkludert liposarkomkohorter |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [32701199](https://pubmed.ncbi.nlm.nih.gov/32701199/) | 2020 | RCT | The Oncologist | SARC024 liposarkomkohort: placebokontrollert fase 2; resultatene støtter ikke rutinemessig bruk av regorafenib |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT | The Lancet Oncology | REGOSARC: placebokontrollert fase 2 ved avansert bløtdelssarkom etter antracyklin |
| [29902612](https://pubmed.ncbi.nlm.nih.gov/29902612/) | 2018 | RCT | European Journal of Cancer | Oppdatert REGOSARC-analyse: effekt ved leiomyosarkom og synovialt sarkom, men ikke ved liposarkom |
| [29931504](https://pubmed.ncbi.nlm.nih.gov/29931504/) | 2018 | Oversikt | Targeted Oncology | Regorafenibs voksende rolle ved sarkom |
| [40975452](https://pubmed.ncbi.nlm.nih.gov/40975452/) | 2025 | Oversikt | Crit Rev Oncol Hematol | Vedlikeholdsbehandling etter førstelinje ved avansert bløtdelssarkom |
| [28295221](https://pubmed.ncbi.nlm.nih.gov/28295221/) | 2017 | Sekundæranalyse | Cancer | REGOSARC: analyse av kvalitetsjustert tid uten symptomer/toksisitet (Q-TWiST) |
| [33290314](https://pubmed.ncbi.nlm.nih.gov/33290314/) | 2021 | Retrospektiv studie | Anti-Cancer Drugs | Anlotinib (annen TKI) ved udifferensiert/dedifferensiert liposarkom |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Studieprotokoll | BMC Cancer | Protokoll for REGOSARC-studien |
| [26266019](https://pubmed.ncbi.nlm.nih.gov/26266019/) | 2015 | Kasuistikk | Rare Tumors | Pazopanib ved ekstraossøs Ewing-sarkom; begrunnelse for Ewing-arm i SARC024 |

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002573 | Stivarga (Bayer Pharma AG) | Ikke oppgitt | Kolorektal kreft (status: kansellert) |

Det finnes ingen gyldig markedsføringstillatelse for regorafenib i dataene som er innhentet for Norge.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet behandling (multikinasehemmer), ikke konvensjonelt cytostatikum |
| Myelosuppresjonsrisiko | Se preparatomtale for advarsler og forsiktighetsregler |
| Emetogenisitet | Se preparatomtale for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Blodstatus, lever- og nyrefunksjon (jf. litteratur om leverpåvirkning, proteinuri og hånd-fot-hudreaksjon ved antiangiogene TKI-er) |
| Håndteringsbeskyttelse | Følg lokale retningslinjer for håndtering av kreftlegemidler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (100 registrert i alt; utvalg av de viktigste):

- **Alvorlig (Major):** acetylsalisylsyre, deferasirox, ibritumomab tiuxetan, tositumomab (inkl. I-131), abciksimab, alteplase, antitrombin III, apiksaban
- **Moderat:** deksametason, klaritromycin, naltrekson, rosuvastatin, kobicistat, fenfluramin, deksfenfluramin, sibutramin
- **Mindre:** dapagliflozin, naloksegol, prukaloprid

Mange av de alvorlige interaksjonene gjelder legemidler som påvirker blødning og koagulasjon, noe som er relevant for et antiangiogent legemiddel.

Litteraturen peker også på klassetypiske bivirkninger ved antiangiogene TKI-er: hånd-fot-hudreaksjon, hypertensjon, diaré, leverskade og proteinuri.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails**

**Begrunnelse:**
Det finnes randomiserte fase 2-data for regorafenib ved bløtdelssarkom, men den liposarkom-spesifikke studien (SARC024) var negativ, og REGOSARC viste nytte kun i ikke-adipocytære undertyper. Prediksjonen har dermed biologisk rimelighet, men svak klinisk støtte for liposarkom spesielt. Dette bør kun forfølges med strenge forbehold, for eksempel i definerte undertyper eller kombinasjonsstudier.

**For å gå videre kreves:**
- Vurdering av om spesifikke liposarkomundertyper eller kombinasjonsregimer kan gi nytte, siden monoterapi ikke støttes av dagens data
- Preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel som må løses før sikkerhetsvurdering)
- Detaljerte mekanismedata fra legemiddeldatabasen
- Avklaring av regulatorisk situasjon i Norge, siden eneste tillatelse er kansellert

---

### Merknad om andre prediksjoner

Blant de øvrige predikerte indikasjonene har **klarcellet nyrecellekarsinom** størst støtte (evidensnivå L2, TxGNN-score 99,47 %). Her finnes en fase 2-studie hos tidligere ubehandlede pasienter med metastatisk sykdom (Lancet Oncology 2012), en fase 1/2-studie av regorafenib med avelumab (NCT03475953, ukjent status, 747 deltakere) og en prekliniske reposisjoneringsstudie som peker mot DDR2-assosiert følsomhet. Etablerte legemidler som sunitinib, axitinib og kabozantinib setter imidlertid en høy standard. Anbefalingen er et forskningsspørsmål. De øvrige prediksjonene (ovarielt myksoid liposarkom, andre nyrecellekarsinom-undertyper, barnenyrekreft og vulvasarkom) har kun modellstøtte uten studier eller litteratur (L5) og anbefales satt på vent (Hold).
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

