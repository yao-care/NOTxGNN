---
layout: default
title: Olaparib
parent: Høy evidens (L1-L2)
nav_order: 253
evidence_level: L1
indication_count: 1
---

# Olaparib
{: .fs-9 }

Evidensnivå: **L1** | Predikerte indikasjoner: **1** stk.
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

# Olaparib: Fra BRCA-mutert eggstokkkreftt til brystkreft

## Sammendrag på en setning

> Olaparib er en PARP1/2-hemmer opprinnelig utviklet og godkjent internasjonalt for vedlikeholdsbehandling av BRCA-mutert eggstokkkreftt.
> TxGNN-modellen flagger **Kvinnelig brystkreft** som en relatert indikasjon, med **73 kliniske studier** og **20 publikasjoner** i evidenspakken —
> men dette er svært sannsynlig allerede en etablert indikasjon (olaparib har vært godkjent for gBRCA-mutert HER2-negativ brystkreft siden 2018) snarere enn et genuint nytt gjenbrukssignal. Se merknad nedenfor.

> ⚠️ **Merknad om datakvalitet**: `drug.original_indications` og `taiwan_regulatory.licenses` er begge tomme i denne evidenspakken, og `original_moa` er flagget som datakløft (DG002). Selv gjenbruksbegrunnelsen flaggerer dette som sannsynlig databaseomission, siden olaparib (Lynparza®) er et godt etablert, globalt godkjent onkologilegemiddel. Denne rapporten er skrevet strengt fra den angitte evidenspakken; ekstern verifisering mot det faktiske TFDA/Norge-bladet er påkrevd før enhver beslutning.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Original indikasjon | Ikke tilgjengelig i evidenspakken (0 lisenser registrert); offentlig kjent original godkjenning: BRCA-mutert, platinumsensitiv tilbakefallt eggstokkkreftt (vedlikeholdsbehandling) |
| Forutsagt ny indikasjon | Kvinnelig brystkreft |
| TxGNN-forutsigelsesscore | 99.09% |
| Bevisnivå | L1 |
| Markedsstatus i Norge | ✗ Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Gå videre med sikringstiltak |

---

## Hvorfor er denne forutsigelsen rimelig?

For øyeblikket er ingen strukturert virkningsmåte-felt tilgjengelig for olaparib i denne evidenspakken (DG002, høy alvorlighetsgrad). Imidlertid gir gjenbruksbegrunnelsen det mekanistiske grunnlaget: olaparib er en **PARP1/2-hemmer (poly-ADP-ribose polymerase hemmer)**. I tumorceller med BRCA1/2-mutasjoner eller bredere homolog rekombinasjonsmangel (HRD), blokkerer PARP-hemming enkeltstreng-DNA-skadegreparasjon, noe som forårsaker ansamling av dobbeltstrengbrudd og celledød via **syntetisk lethality**. Denne mekanismen har blitt omfattende validert både biologisk og klinisk i BRCA-muterte tumorer.

BRCA1/2-mutasjoner driver både arvelig eggstokkkrefft og arvelig brystkreft gjennom samme DNA-reparasjonssti. Siden olapariba sin syntetisk-lethality-mekanisme er genetisk-defekt-drevet snarere enn vevsSpesifikk, utvider effektiviteten seg lett fra eggstokkkreftt til brystkreft hos pasienter som deler samme germinal BRCA1/2-mutasjon — dette er ikke en spekulativ gjenbrukshypotese men en mekanistisk forventet og klinisk bekreftet utvidelse.

Det er viktig å merke seg at det kliniske beviset i denne pakken (OlympiAD, OlympiA) viser at denne "forutsatte" indikasjonen **allerede er en godkjent, retningslinjestandard bruk** av olaparib i gBRCA-mutert HER2-negativ brystkreft (både metastatisk og høy-risiko tidlig-adjuvant instillinger) i flere jurisdiksjoner siden 2018–2022. TxGNN-signalet her bør tolkes som **bevisbekreftelse av en eksisterende indikasjon**, ikke oppdagelse av en ny.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Viktige funn |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Fase 3 | Fullført | 266 | Olaparib-monoterapi vs. legens valg enkeltagens kjemoterapi ved platinumsensitiv tilbakefallt, gBRCA1/2-mutert eggstokkkreftt |
| [NCT03162627](https://clinicaltrials.gov/study/NCT03162627) | Fase 1 | Aktiv, rekrutterer ikke | 90 | Selumetinib + olaparib ved solide tumorer (inkl. bryst) med Ras-vei-alterasjoner eller PARP-resistens |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Fase 1 | Fullført | 25 | Carboplatin + olaparib → olaparib-monoterapi vs. capecitabine som førstelinjebehandling ved BRCA1/2-mutert HER2-negativ avansert brystkreft |
| [NCT03402841](https://clinicaltrials.gov/study/NCT03402841) | Fase 3b | Fullført | 279 | Enkeltarms olaparib-vedlikehold ved platinumsensitiv tilbakefallt, ikke-germinal BRCA eggstokk-/endometrioidkreft |
| [NCT02503436](https://clinicaltrials.gov/study/NCT02503436) | N/A (observasjonsbasert) | Fullført | 276 | C-PATROL: effektivitet/sikkerhet av olaparib i praksis ved BRCAm+ platinumsensitiv tilbakefallt eggstokkkreftt |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Fase 2 | Fullført | 99 | AZD2281 (olaparib) ved BRCA-mutert/trippel-negativ brystkreft og gjentakende eggstokkkreftt — responsrate og korrelative biomarkører |
| [NCT05564377](https://clinicaltrials.gov/study/NCT05564377) | Fase 2 | Rekrutterer | 2900 | ComboMATCH biomarkør-styrt kombinasjonsterapi-plattformtudie, inkludert brystkreft-kohorter |
| [NCT04421963](https://clinicaltrials.gov/study/NCT04421963) | Fase 3 | Aktiv, rekrutterer ikke | 185 | ROSY-O fortsettelsesstudie som gir fortsatt olaparib-behandling etter avslutning av mortudie |
| [NCT06545942](https://clinicaltrials.gov/study/NCT06545942) | Fase 1 | Aktiv, rekrutterer ikke | 220 | MOMA-313 monoterapi eller kombinert med en PARP-hemmer (olaparib) ved avansert/metastatisk solide tumorer |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Fase 4 | Fullført | 202 | Olaparib ved indiske pasienter med platinumsensitiv tilbakefallt eggstokkkreftt og BRCA1/2-mutert metastatisk brystkreft |

*Merknad: 43 ytterligere studier i evidenspakken er klassifisert som "under vurdering" (ugjennomgått relevans) og er utelatt fra denne tabellen; de fleste er kombinasjons-/kurvstudier på tvers av flere solide tumortyper snarere enn brystkreft-spesifikke.*

---

## Bevis fra litteraturen

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib viser antitumor-aktivitet ved metastatisk brystkreft med germinal BRCA-mutasjon |
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib reduserer gjentakelse ved gBRCA1/2-mutert, HER2-negativ tidlig brystkreft |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD endelig OS og tolerabilitet: olaparib vs. kjemoterapi ved gBRCA-mutert HER2-negativ mBC |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA fase 3 overordnet overlevelsesresultater for adjuvant olaparib ved høy-risiko tidlig brystkreft |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD utvidet oppfølging: vedvarende OS og sikkerhetdata for olaparib ved gBRCAm HER2-negativ mBC |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Fase 2, enkeltarm | J Clin Oncol | TBCRC 048: olaparib-aktivitet ved mBC med somatisk BRCA1/2 eller ikke-BRCA HR-relaterte genmutasjoner |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Fase 2, kombinasjon | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel øker pCR ved høy-risiko HER2-negativ brystkreft |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Oversiktsartikkel | Target Oncol | Oversikt over PARP-hemmere (olaparib, talazoparib) godkjent for BRCA-mutert HER2-negativ brystkreft |
| [35163586](https://pubmed.ncbi.nlm.nih.gov/35163586/) | 2022 | Oversiktsartikkel | Int J Mol Sci | Molekylære mekanismer, biomarkører og kommende terapier for kjemoterapiresistent TNBC |
| [37253112](https://pubmed.ncbi.nlm.nih.gov/37253112/) | 2023 | Translasjonell/Funksjonell | Cancer Res | Funksjonell karakterisering av RAD51C-varianter relevant for HR-mangel og PARP-hemmer-følsomhet |

---

## Markedsinformasjon for Norge

Ingen autorisasjonsregistreringer er tilstede i evidenspakken (`total_licenses: 0`, `licenses: []`). Olaparib har for øyeblikket **ingen registrert markedsføringstillatelse i Norge ifølge denne datakilden**. Dette bør verifiseres uavhengig mot nasjonalt legemiddelregister før man fortsetter, siden olaparib (Lynparza®) er sentralt autorisert i EU/EØS og ville normalt forventes å vises.

---

## Cytotoksisitet

Olaparib er et antineoplastisk middel (PARP-hemmer, onkologiindikasjon) og denne delen gjelder derfor.

| Element | Innhold |
|------|------|
| Cytotoksisitet-klassifisering | Målrettet terapi (PARP-hemmer; syntetisk lethality i HR-defisiente tumorer) |
| Myelosuppresjonrisiko | Vennligst se pakkeblad-advarsler og forholdsregler |
| Emetogenitet-klassifisering | Vennligst se pakkeblad-advarsler og forholdsregler |
| Overvåkingselementer | Vennligst se pakkeblad-advarsler og forholdsregler |
| Håndteringsbeskyttelse | Vennligst se pakkeblad-advarsler og forholdsregler |

*Detaljerte toksisitets-/overvåkingsdata kunne ikke innhentes — dette er blokkert av DG001 (TFDA-pakkeblad advarsler/kontraindikasjoner ikke ennå hentet).*

---

## Sikkerhetshensyn

Vennligst se pakkeblad for sikkerhetsinformasjon. Ingen viktige advarsler, kontraindikasjoner eller legemiddel-legemiddel-interaksjondata er for øyeblikket tilgjengelig i denne evidenspakken (alle felt flagget som datakløfter; DDI-søk returnerte ingen resultater).

---

## Konklusjon og neste trinn

**Beslutning: Gå videre med sikringstiltak**

**Begrunnelse:**
Klinisk bevis er sterkt (5 fase 3 RCT-er, inkludert to sentrale studier — OlympiAD og OlympiA — som direkte etablerer olapariba sin effektivitet ved gBRCA-mutert brystkreft), noe som rettferdiggjør bevisnivå L1. Imidlertid ser dette ut til å representere bekreftelse av en **allerede internasjonalt godkjent indikasjon** snarere enn en ny gjenbrukskandidat, og kritisk sikkerhet og regulatoriske data (TFDA/Norge-pakkeblad, virkningsmåte, markedsføringsautorisasjon) mangler fra denne pakken — derfor sikringstiltak snarere enn ubetinget grønt lys.

**For å fortsette, trengs følgende:**
- Løs DG001 (Blokkering): hent og analysér det faktiske produktbladet for advarsler, kontraindikasjoner og DDI-data
- Løs DG002 (Høy): bekreft strukturert virkningsmåte fra DrugBank API
- Verifiser faktisk markedsføringsautorisasjonsstatus i Norge/EØS for olaparib (Lynparza®), siden 0 lisenser i denne pakken er inkonsistent med dens kjente EU-sentraliserte autorisasjon
- Bekreft hvorvidt "kvinnelig brystkreft" skal omklassifiseres som en eksisterende godkjent indikasjon snarere enn en TxGNN-forutsagt ny indikasjon, for å unngå feilkarakterisering av denne kandidaten i etterfølgende rapportering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

