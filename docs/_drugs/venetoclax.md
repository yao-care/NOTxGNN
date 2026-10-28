---
layout: default
title: Venetoclax
parent: Kun modellprediksjon (L5)
nav_order: 447
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "VENETOCLAX"
predicted_indications: ["Hodgkins lymphoma", "chronic myelogenous leukemia, BCR-ABL1 positive", "Ewing sarcoma", "follicular lymphoma", "metastatic neoplasm", "malignant spiradenoma"]
description: "Venetoclax: predikert ny indikasjon Hodgkins lymphoma (evidensnivå L5). Opprinnelig indikasjon: Leukemia, Lymphocytic, Chronic, B-Cell"
---

# Venetoclax
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

## Venetoclax: Hodgkins lymphoma
{: .text-alpha }

## Oppsummering i én setning

Venetoklaks er en BCL-2-hemmer som opprinnelig er godkjent for behandling av kronisk lymfatisk B-celleleukemi (KLL).
TxGNN-modellen predikerer at legemidlet kan være effektivt ved **pregerminalsenter-KLL/småcellet lymfocyttisk lymfom (SLL)**, en molekylær undergruppe (umutert IGHV) av den allerede godkjente indikasjonen.
Foreløpig finnes **0 kliniske studier** og **1 publikasjon** (en oversiktsartikkel om B-cellereseptor-biologi) som støtter denne spesifikke prediksjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Leukemia, Lymphocytic, Chronic, B-Cell |
| Predikert ny indikasjon | Hodgkins lymphoma |
| TxGNN-prediksjonsscore | 0.9951 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget for denne rapporten. Basert på kjent informasjon er venetoklaks en selektiv hemmer av det antiapoptotiske proteinet BCL-2, og effekten ved KLL er godt dokumentert. Mekanistisk kan den derfor være aktuell også for undergrupper av KLL.

Den predikerte indikasjonen er en molekylær undergruppe av KLL/SLL: umutert IGHV, med opphav i pregerminalsenter-B-celler og dårligere prognose. BCL-2-avhengighet er veletablert ved KLL, så aktivitet i denne undergruppen er mekanistisk plausibel.

Det finnes imidlertid ingen undergruppespesifikk studie. Den eneste publikasjonen handler om struktur og funksjon til tumorens B-cellereseptor, ikke om effekt av venetoklaks. Prediksjonen er derfor i praksis en undergruppe av den eksisterende indikasjonen og ikke et ekte tilfelle av drug repurposing.

---

## Kliniske studier

Foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/) | 2022 | Oversikt/biologisk analyse | Cancers | Gjennomgang av tumorens B-cellereseptor ved KLL. Skiller mellom umutert IGHV (pregerminalsenter, dårlig prognose) og mutert IGHV (postgerminalsenter, god prognose). Ingen data om venetoklaks. |

---

## Markedsinformasjon for Norge


---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisk klassifisering | Målrettet behandling (selektiv BCL-2-hemmer) |
| Risiko for myelosuppresjon | Nøytropeni og andre cytopenier er vanlige i litteraturen om venetoklaks ved lymfoide maligniteter. Se pakningsvedlegget for detaljer. |
| Emetogenitetsklassifisering | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Fullstendig blodtelling, nyrefunksjon og elektrolytter (tumorlysesyndrom er en hyppig bekymring) |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Interaksjonsdatabasen viser til sammen 100 registrerte interaksjoner. Blant de oppførte er følgende klassifisert som **alvorlige (Major)**:

- Aprepitant
- Deksametason
- Klaritromycin
- Eliglustat
- Rolapitant
- Fidaksomicin
- Kobicistat
- Deferipron
- Samarium (153Sm) lexidronam

Flere interaksjoner er klassifisert som moderate, blant annet alvimopan, loperamid, cimetidin, mikonazol, klotrimazol og rifaksimin. Naloksegol er klassifisert som mindre alvorlig. Litteraturen beskriver dessuten at sterke CYP3A-hemmere som posakonazol krever dosejustering av venetoklaks.

For øvrig sikkerhetsinformasjon, se pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen gjelder en undergruppe av den allerede godkjente KLL-indikasjonen, og det finnes ingen undergruppespesifikke studier. Støtten er i praksis en modellscore og én biologisk oversiktsartikkel. Samtidig er legemidlet kun avregistrert på det norske markedet, noe som begrenser praktisk relevans.

**For å gå videre trengs følgende:**
- Undergruppeanalyser (IGHV-status) fra eksisterende KLL-studier med venetoklaks, for eksempel MURANO
- Pakningsvedlegg med advarsler og kontraindikasjoner for en fullstendig sikkerhetsvurdering
- Data om virkningsmekanisme
- Avklaring av markedsstatus og tilgjengelighet i Norge
- Vurdering av de andre prediksjonene i datagrunnlaget, som akutt myeloid leukemi (evidensnivå L1) og follikulært lymfom (L2), som har sterkere evidens og er mer reelle repurposing-kandidater
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

