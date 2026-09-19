---
layout: default
title: Eribulin
parent: Kun modellprediksjon (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Eribulin
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

# Eribulin: Fra liposarkom til fibroblastisk neoplasi (Solitary Fibrous Tumor)

## Oppsummering i én setning

> Eribulin er en mikrotubuli-hemmer kjemoterapi-agent med FDA-godkjenning for bruk ved ikke-resektabelt liposarkom som referert i underliggende bevis.
> TxGNN-modellen genererte 10 kandidatindikasjon for dette legemidlet; blant dem skiller **Fibroblastisk neoplasi (Solitary Fibrous Tumor)** seg ut som den eneste kandidaten støttet av en **gjennomført klinisk utprøving i fase II** og **flere støttepublikasjoner**, mens 7 av de andre 9 kandidatene (inkludert modellens #1-rangerte prediksjon, "familial Mediterranean fever") ikke har noen klinisk eller litteraturstøtte og er flagget av selv bevispacken som sannsynlig modellstøy.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke-resektabelt liposarkom (bløtvevssarkom) — nevnt i bevispackens begrunnelse; ingen formell indikasjonsliste ble returnert for dette legemidlet |
| Predikert ny indikasjon | Fibroblastisk neoplasi (Solitary Fibrous Tumor) |
| TxGNN Prediksjonsscore | 99.36% |
| Bevisnivå | L3 (en gjennomført, enkeltarms fase II-utprøving spesifikk for denne indikasjon + støttende preklinisk litteratur; ennå ikke en randomisert fase 2/3-utprøving, så ikke helt opp til L2) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Fortsett med sikkerhetstiltak |

**Merknad om valg:** Denne rapporten vurderer den *best-bevisede* kandidaten fra de 10 TxGNN-prediksjoner som ble levert, ikke den høyest rangerte. Den #1-rangerte prediksjonen ("autosomalt recessiv familial Mediterranean fever," poeng 99.82%) har ingen klinisk eller litteraturbevis i det hele tatt, og dens egen mekanistiske begrunnelse angir eksplisitt at det er "meget sannsynlig TxGNN modellstøy/falsk positiv." Fibroblastisk neoplasi (modellrangering 8, poeng 99.36%) er den eneste kandidaten med en dedikert gjennomført utprøving.

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte virkningsmekanisme-data for eribulin ikke tilgjengelige i denne bevispacken (flagget som et datakløft med høy alvorlighetsgrad, DG002). Basert på informasjonen som er tilgjengelig, er eribulin en mikrotubuli-dynamikk-hemmer (halichondrin B-analogklasse) brukt som cytotoksisk kjemoterapi, med en etablert, FDA-godkjent rolle ved ikke-resektabelt liposarkom — et bløtvevssarkom.

Fibroblastiske neoplasier, og spesifikt Solitary Fibrous Tumor (SFT), tilhører den samme brede bløtvevssarkom-familien som liposarkom. Flere prekliniske studier i bevispacken demonstrerer eribulin-aktivitet og resistansmekanismer spesifikt i fibrosarkom-cellelinjer (f.eks. HT1080), og en pasientavledet xenograft-studie (PDX) (PMID 28284173) identifiserte eksplisitt eribulin og trabectedin som effektive kandidater mot SFT — et funn som synes å ha direkte motivert den dedikerte ERASING fase II-utprøvingen (NCT03840772).

Dette gir fibroblastisk neoplasi/SFT en sterkere og mer mekanistisk sammenhengende begrunnelse enn de fleste av de andre 9 TxGNN-prediksjoner i denne pakken, hvorav de fleste (mesoteliom-undertyper, pleural adenomatoid tumor, familial Mediterranean fever) ikke har kliniske utprøvinger, ingen litteratur, og mekanistiske begrunnelser som anerkjenner at forbindelsen er spekulativ.

---

## Klinisk utprøvingsbevis

| Utprøvingsnummer | Fase | Status | Rekruttering | Viktige funn |
|---------|------|------|------|---------|
| [NCT03840772](https://clinicaltrials.gov/study/NCT03840772) | Fase 2 | Gjennomført | 16 | ERASING-utprøving (Italian Sarcoma Group): enkeltarms fase II-studie av eribulin ved avansert Solitary Fibrous Tumor |

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [28284173](https://pubmed.ncbi.nlm.nih.gov/28284173/) | 2017 | Preklinisk (PDX) | European Journal of Cancer | Pasientavledede SFT-xenografter viser høy sensitivitet for doxorubicin/dacarbazine; fremhever også eribulin og trabectedin som effektive kandidater — grunnlag for senere klinisk testing |
| [38136399](https://pubmed.ncbi.nlm.nih.gov/38136399/) | 2023 | Oversikt | Cancers | Oversikt over diagnose og behandling av ekstramenigeal Solitary Fibrous Tumor |
| [40295012](https://pubmed.ncbi.nlm.nih.gov/40295012/) | 2025 | Preklinisk (in vivo) | In Vivo | Eribulin-resistente HT1080 fibrosarkom-celler blir mer ondartete; kombinasjon med metioninrestriksjon overvinner resistans i musemodeller |
| [39197933](https://pubmed.ncbi.nlm.nih.gov/39197933/) | 2024 | Preklinisk (in vitro) | Anticancer Research | Rekombinant methioninase øker eribulin-effektivitet 16-fold i eribulin-resistente HT1080 fibrosarkom-celler |
| [38423656](https://pubmed.ncbi.nlm.nih.gov/38423656/) | 2024 | Preklinisk (in vitro) | Anticancer Research | Sterk synergi mellom rekombinant methioninase og eribulin mot fibrosarkom-celler, sparer normale fibroblaster |

---

## Markedsinformasjon for Norge

Ingen markedsføringstillatelsesoppføringer ble funnet for eribulin i Norge (0 godkjenninger; markedsstatus: ikke markedsført).

---

## Cytotoksisitet

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Konvensjonell cytotoksisk (mikrotubuli-hemmer, halichondrin B-analogklasse) |
| Benmargssuppresjonrisiko | Se advarsel og forholdsregler i pakningsvedlegget |
| Emetogenitetsklassifisering | Se advarsel og forholdsregler i pakningsvedlegget |
| Overvåkingselementer | Se advarsel og forholdsregler i pakningsvedlegget |
| Håndteringsbeskyttelse | Standard sikkerhetshåndtering for cytotoksisk legemidler gjelder, i samsvar med andre antineoplastiske kjemoterapiagenter |

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. Merk: innhenting av advarsler og kontraindikasjoner fra TFDA-ekvivalent merking for dette legemidlet er for øyeblikket et **blokkeringsdatakløft (DG001)** — dette må løses før noen klinisk sikkerhetsassessering (S1-fase) kan fortsette.

---

## Konklusjon og neste trinn

**Beslutning: Fortsett med sikkerhetstiltak**

**Begrunnelse:**
Fibroblastisk neoplasi/Solitary Fibrous Tumor er støttet av en gjennomført, dedikert fase II-utprøving (ERASING, n=16) og konsistent preklinisk mekanistisk bevis, noe som gjør det til den eneste troverdige kandidaten blant de 10 TxGNN-prediksjoner som ble levert. Imidlertid er utprøvingen liten og enkeltarms (ikke randomisert), og legemiddeldata på sikkerhet/merking mangler helt, så dette kan ikke ennå støtte en full "Go"-beslutning.

**For å fortsette, er følgende nødvendig:**
- Løse blokkeringsdatakløft DG001: skaffe advarsler, kontraindikasjoner og DDI-data fra pakningsvedlegget
- Løse datakløft DG002: skaffe formelle virkningsmekanisme-data fra DrugBank
- Søke bekreftende eller større kohort-data utover den 16-pasient ERASING-utprøvingen før du vurderer formell omformål
- Deprioritere (Vent) de 7 lav-bevis TxGNN-kandidatene i denne pakken (mesoteliom-undertyper, pleural adenomatoid tumor, familial Mediterranean fever) med mindre nye kliniske eller litteraturbevis oppstår
- Fortsette overvåkingen av dermatofibrosarcoma protuberans og ovarialt myksoid liposarkom som sekundære "Research Question"-ledere (for øyeblikket L4, kun mekanisme-støtte)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

