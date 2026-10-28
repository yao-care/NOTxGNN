---
layout: default
title: Gefitinib
parent: Kun modellprediksjon (L5)
nav_order: 186
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Gefitinib: predikert ny indikasjon Gingival fibromatose (evidensnivå L5). Opprinnelig indikasjon: Ikke-småcellet lungekreft (Carcinoma, Non-Small-Cell Lung)"
monitor_inn: "GEFITINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "lung benign neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa"]
---

# Gefitinib
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

## Gefitinib: Fra ikke-småcellet lungekreft til gingival fibromatose
{: .text-alpha }

## Oppsummering i én setning

Gefitinib er en EGFR-tyrosinkinasehemmer som opprinnelig brukes mot ikke-småcellet lungekreft.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **gingival fibromatose**, men for denne indikasjonen finnes det **ingen kliniske studier** og **ingen publikasjoner** som støtter prediksjonen. Den er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke-småcellet lungekreft (Carcinoma, Non-Small-Cell Lung) |
| Predikert ny indikasjon | Gingival fibromatose |
| TxGNN-prediksjonsscore | 0.9989 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Gefitinib er kjent som en hemmer av EGFR-tyrosinkinase, og effekten ved EGFR-mutert ikke-småcellet lungekreft er godt dokumentert. Mekanistisk kunne en antiproliferativ effekt på fibroblaster tenkes, men dette er rent spekulativt.

Den høye TxGNN-scoren (0.9989) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Den er ikke støttet av noen kliniske studier eller litteratur for gingival fibromatose. Det finnes ingen direkte, datastøttet kobling mellom den opprinnelige indikasjonen (kreft) og den nye (en fibrøs overvekst i tannkjøttet). Prediksjonen bør derfor sees på som en hypotese og ikke som en terapeutisk begrunnelse.

---

## Kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert for denne indikasjonen.

---

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur for denne indikasjonen.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001016 | Iressa (AstraZeneca AB) | Ikke oppgitt | Ikke-småcellet lungekreft (status: kansellert) |

Legemidlet er markedsført i Norge, og 1 av 1 registrerte godkjenninger er gyldig.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet terapi (EGFR-tyrosinkinasehemmer) |
| Risiko for myelosuppresjon | Se preparatomtalen for advarsler og forsiktighetsregler |
| Emetogenisitet | Se preparatomtalen for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Lever- og nyrefunksjon, lungesymptomer (se sikkerhetsavsnittet) |
| Håndtering og vern | Se preparatomtalen for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (PrimeKG, ikke preparattekst):** leversykdom, gallblæresykdom, interstitiell lungesykdom, lungefibrose og postinflammatorisk lungefibrose. Interstitiell lungesykdom er også beskrevet i litteraturen som en alvorlig bivirkning av gefitinib (inkludert et dødelig tilfelle av akutt pneumonitt).
- **Andre signaler i litteraturen:** hudtoksisitet (akneiform utslett, paronyki), QT-forlengelse og enkelte kardiovaskulære hendelser.
- **Legemiddelinteraksjoner:** 100 interaksjoner er funnet. De vanligste er av moderat alvorlighetsgrad:
  - Syrehemmende midler: famotidin, ranitidin, cimetidin, nizatidin, omeprazol, esomeprazol, pantoprazol, lansoprazol, deksolansoprazol, rabeprazol
  - Klaritromycin, aprepitant, deksametason, naltrekson
  - Soppmidler: mikonazol, klotrimazol
  - Troglitazon
  - I tillegg er kalsitriol og glimepirid registrert med ukjent alvorlighetsgrad.

Opplysninger om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for gingival fibromatose bygger kun på modellscore (evidensnivå L5), uten kliniske studier eller litteratur. Den eneste norske godkjenningen er kansellert, og sikkerhetsprofilen (blant annet interstitiell lungesykdom og hudtoksisitet) taler for forsiktighet.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner fra legemiddelmyndighetenes kilder (blokkerende datamangel)
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Prekliniske data eller mekanistiske studier som viser at EGFR-hemming er relevant for gingival fibromatose
- Vurdering av administrasjonsvei og forholdet mellom nytte og risiko for en ikke-malign tilstand

---

**Merknad om andre prediksjoner:** De øvrige ni toppkandidatene (blant annet lungehilus-karsinom, godartet lungeneoplasme, lungegerminalcelletumor, pulmonal sulcus-neoplasme og junksjonell epidermolysis bullosa) har også anbefalingen Hold. De har enten ingen evidens eller bare indirekte evidens (evidensnivå L4–L5). Lungehilus-karsinom og pulmonal sulcus-neoplasme er anatomisk beslektet med den eksisterende lungekreftindikasjonen, men støttes bare av et enkelt kasuistisk tilfelle og indirekte litteratur.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

