---
layout: default
title: Tecovirimat
parent: Høy evidens (L1-L2)
nav_order: 341
evidence_level: L2
indication_count: 10
---

# Tecovirimat
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **10** stk.
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

# Tecovirimat: Fra kopokkver til vaccinia-relaterte komplikasjoner

## Oppsummering i én setning

Tecovirimat (TPOXX) ble opprinnelig utviklet og godkjent for behandling av kopokkver forårsaket av variola-virus, en Orthopoxvirus. Blant de ti TxGNN-predikerte indikasjonene i denne bevisgjennomgangen, er de fleste (hordeolum, vibrio-infeksjon, Klebsiella-infeksjon, noma, HTLV-1-assosiert dermatitt, Arterivirus-infeksjon, arbovirus-infeksjon, E. coli-infeksjon) flagget av modellens egen begrunnelse som mekanistisk usannsynlige falske positive uten noe støttende bevis. Den eneste kandidaten med reelt støtte er **vaccinia** (rangering 5), støttet av **3 kliniske forsøk** (inkludert et aktivt fase 2-forsøk for legemiddel-vaksin-interaksjon og et gjennomført protokoll for utvidet tilgang) og **18 publikasjoner**, noe som gjør det til den eneste indikasjonen i dette settet som rettferdiggjør videre evaluering.

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Kopokkver (variola-virus) — ikke tilstede i det regulatoriske datasettet (Norge: ikke godkjent), men dokumentert i støttende litteratur (FDA-godkjenning, juli 2018) |
| Predikert ny indikasjon | Vaccinia (Orthopoxvirus-infeksjon/-komplikasjoner, inkludert bivirkninger etter vaksinasjon) |
| TxGNN-prediksjonspoengsum | 99.62% |
| Bevisnivå | L2 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Fortsett med forbeholdsregler |

## Hvorfor er denne prediksjonen rimelig?

`original_moa`-feltet i det regulatoriske datasettet er et datahull, men mekanismen kan rekonstrueres fra støttende litteratur: tecovirimat hemmer Orthopoxvirus VP37-konvoluttviklende protein, som blokkerer dannelsen av ekstracellulær omhyllet virus (EEV) og dermed forhindrer virus fra å spres fra celle til celle og systemisk. Denne mekanismen er iboende for Orthopoxvirus-slekten som helhet, ikke spesifikk for variola.

Vaccinia-virus tilhører samme slekt som variola (kopokkver) og deler VP37-avhengig EEV-monteringsvei som tecovirimat målrettes mot. Dette er en nært naboforlengelse snarere enn en mekanistisk fjern gjenbrukskandidat: vaccinia brukes som levende kopokkver-vaksin (f.eks. ACAM2000, JYNNEOS), og tecovirimat er allerede brukt i praksis for å håndtere alvorlig eller progrederende vaccinia-komplikasjoner etter vaksinasjon, sekundær overføring eller yrkesrelatert eksponering — som gjenspeilt i FDA-sanksjonert utvidet tilgangsprotokoll (NCT05380752) og et gjennomført forsøk for legemiddel-vaksin-interaksjon (NCT04957485).

**Merk om andre TxGNN-rangerte kandidater:** Rangeringer 1–4 og 7–10 (hordeolum, vibrio-infeksjon, Klebsiella-infeksjon, noma, HTLV-1-assosiert dermatitt, Arterivirus-infeksjon, arbovirus-infeksjon, E. coli-infeksjon) scoret like høyt (~99.6%), men hver bærer en eksplisitt «ingen biologisk plausibilitet»-vurdering og ingen støttende forsøk eller litteratur (L5/Hold) — disse diskuteres ikke videre. Rangering 6, «koininfeksjon», er et bredere, mindre spesifikt signal (L4/S1, Forskningsspørsmål): det underliggende beviset støtter tecovirimat sin rolle spesifikt mot orthopoxvirus-komponenten av mpox/HIV eller mpox/syfilis-koinfeksjoner hos immunocompromiserte værter, ikke en frittstående approvbar indikasjon.

## Bevis fra kliniske forsøk

| Forsøksnummer | Fase | Status | Rekruttering | Nøkkelfunn |
|---------|------|------|------|---------|
| [NCT04957485](https://clinicaltrials.gov/study/NCT04957485) | Fase 2 | Aktiv, ikke rekruttering | 100 | RCT som evaluerer hvorvidt samtidig oral tecovirimat (TPOXX, to ganger daglig × 28 dager) interfererer med JYNNEOS-vaksin-immunogenisitet versus placebo |
| [NCT05380752](https://clinicaltrials.gov/study/NCT05380752) | N/A (Utvidet tilgang) | Ikke lenger tilgjengelig | N/A | Ga IV tecovirimat til pasienter med bekreftet/mistenkt orthopoxvirus-infeksjon eller alvorlig vaccinia-bivirkning som ikke kunne tåle oral formulering |
| [NCT05976100](https://clinicaltrials.gov/study/NCT05976100) | Fase 1 | Fullført | 90 | Sikkerhet, tolerabilitet og PK-studie av NIOCH-14, et sammenlignbart anti-orthopoxvirus middel; støttende for legemiddelklassens rationale snarere enn tecovirimat selv |

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Nøkkelfunn |
|------|-----|------|------|---------|
| [32882158](https://pubmed.ncbi.nlm.nih.gov/32882158/) | 2021 | Oversikt | Expert Rev Anti Infect Ther | Oversikt over tecovirimat sin godkjenning for kopokkver og dens utvidede anti-orthopoxvirus (inkludert vaccinia) bruksomrader |
| [22904336](https://pubmed.ncbi.nlm.nih.gov/22904336/) | 2012 | Caserapport | J Infect Dis | Progrederende vaccinia hos en immunocompromisert kopokkver-vaksinert person som ble vellykket behandlet med VIG pluss ST-246 (tecovirimat) og CMX001 |
| [31677948](https://pubmed.ncbi.nlm.nih.gov/31677948/) | 2020 | Preklinisk | Vaccine | Samtidig administrasjon av tecovirimat med ACAM2000-vaksin hos ikkje-humane primater; vurderte effekt på vaksin-immunogenisitet og effektivitet mot dødelig milepokke-utfordring |
| [36374026](https://pubmed.ncbi.nlm.nih.gov/36374026/) | 2022 | Oversikt | Antimicrob Agents Chemother | Mekanisme og klinisk rolle for tecovirimat mot orthopoxvirus inkludert vaccinia og menneske-milepokke-virus |
| [36961984](https://pubmed.ncbi.nlm.nih.gov/36961984/) | 2023 | Oversikt | J Med Chem | Oversikt over antivirale midler, inkludert tecovirimat, aktiv mot milepokke-virus og andre orthopoxvirus |
| [35763248](https://pubmed.ncbi.nlm.nih.gov/35763248/) | 2022 | Oversikt | Drugs | Forebygging og behandlingsstrategier for milepokke, inkludert tecovirimat sin rolle for orthopoxvirus-motforanstaltninger |
| [36403582](https://pubmed.ncbi.nlm.nih.gov/36403582/) | 2023 | Oversikt | Lancet | Omfattende oversikt over milepokke som Orthopoxvirus-sykdom, kontekstualisering av tecovirimat sin bruk |
| [39401235](https://pubmed.ncbi.nlm.nih.gov/39401235/) | 2024 | Oversikt | JAMA | Mpox klinisk presentasjon, diagnose og behandlingsstrategier, inkludert antiviral terapi |
| [36130588](https://pubmed.ncbi.nlm.nih.gov/36130588/) | 2022 | Oversikt | J Pharm Pharm Sci | Milepokke-virologi, patofysiologi og behandlingslandskap |
| [37131608](https://pubmed.ncbi.nlm.nih.gov/37131608/) | 2023 | Oversikt | bioRxiv | Oversikt over antivirale midler (tecovirimat, brincidofovir) mot milepokke og relaterte orthopoxvirus-infeksjoner |

## Norsk markedsinformasjon

Tecovirimat er for øyeblikket **ikke markedsført** i Norge (markedsstatus: Ikke markedsført), og ingen markedsføringsautorisasjonsregistre er tilgjengelige i bevisgjennomgangen.

## Sikkerhetsvurderinger

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og neste trinn

**Beslutning: Fortsett med forbeholdsregler**

**Begrunnelse:**
Tecovirimat sin mekanisme (VP37/EEV-hemming) er direkte relevant for vaccinia gitt dens delte Orthopoxvirus-slekt med variola, og denne utvidelsen er allerede støttet av regulatorisk presedens i praksis (FDA utvidet tilgang) og et aktivt fase 2-interaksjonsforsøk — men bevisgrunnlaget er fortsatt begrenset til ett pågående RCT, ett lukket program for utvidet tilgang og ingen fullført effektivitetsforsøk spesifikt for vaccinia.

**For å fortsette, er følgende nødvendig:**
- Offisiell TFDA/EMA-pakningsvedlegg (advarsler, kontraindikasjoner) — for øyeblikket et kritisk datahull (DG001), påkrevd før enhver S1-sikkerhetskontroll
- Strukturert DrugBank-post for virkningsmekanisme — for øyeblikket et alvorlig datahull (DG002), nødvendig for å formelt dokumentere den mekanistiske begrunnelsen utover litteraturslutninger
- Resultat fra NCT04957485 (estimert fullføring 2027) for å bekrefte ingen immunologisk interferens med JYNNEOS og for å karakterisere sikkerhet i målpopulasjonen
- Hvis gjenbruk forfølges, klargjøring av en regulatorisk vei for et for øyeblikket uautorisert produkt i Norge
- Hvis «koininfeksjon» (rangering 6) undersøkes videre, bør indikasjonen innsnevres til «orthopoxvirus-infeksjon hos immunocompromiserte værter (f.eks. HIV+)» snarere enn den generiske etiketten, for å forbli klinisk og regulatorisk meningsfull
- Ingen ytterligere handling nødvendig for rangeringer 1–4 og 7–10 (hordeolum, vibrio-infeksjon, Klebsiella-infeksjon, noma, HTLV-1-assosiert dermatitt, Arterivirus-infeksjon, arbovirus-infeksjon, E. coli-infeksjon) — korrekt scoret Hold på grunn av fravær av mekanistisk plausibilitet eller bevis

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

