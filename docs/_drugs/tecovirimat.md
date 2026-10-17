---
layout: default
title: Tecovirimat
parent: Kun modellprediksjon (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tecovirimat: predikert ny indikasjon Hordeolum (evidensnivå L5). Opprinnelig indikasjon: Poxviridae-infeksjoner, kukopper, apekopper, vaccinia, kopper"
monitor_inn: "TECOVIRIMAT"
predicted_indications: ["hordeolum", "vibrio infectious disease", "Klebsiella infectious disease", "noma", "coinfection", "infective dermatitis associated with HTLV-1", "Arterivirus infectious disease", "arbovirus infection", "escherichia coli infection"]
---

# Tecovirimat
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

# Tecovirimat: Fra kopper og apekopper til vaccinia (nær på-label bruk)

## Sammendrag i én setning

Tecovirimat er et antiviralt middel som opprinnelig brukes mot infeksjoner med ortopoxvirus (kopper, apekopper, kukopper og vaccinia).
TxGNN-modellen rangerer **hordeolum (byller på øyelokket)** øverst, men dette er sannsynligvis en modellartefakt uten støtte i data. Den eneste biologisk plausible prediksjonen er **vaccinia**, som i praksis allerede ligger innenfor den opprinnelige indikasjonen, med **0 kliniske studier** og **19 publikasjoner** (hovedsakelig oversiktsartikler om apekopper) i de samlede dataene.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Poxviridae-infeksjoner, kukopper, apekopper, vaccinia, kopper |
| Predikert ny indikasjon (rangert først) | Hordeolum |
| TxGNN-prediksjonsscore | 99,66 % |
| Evidensnivå | L5 (kun modellprediksjon) |
| Markedsstatus i Norge | Kun avregistrert/trukket tilbake |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

**Merknad om øvrige prediksjoner:** Den eneste prediksjonen med meningsfull støtte er vaccinia (rang 5, evidensnivå L4, anbefaling: forskningsspørsmål). Den er imidlertid i hovedsak en på-label eller nær på-label bruk, ikke ekte repurposing.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de samlede dataene. Ut fra kjent informasjon hemmer tecovirimat orthopoxvirusets envelope-protein p37 (VP37), som er nødvendig for dannelse av omhyllede viruspartikler og spredning av viruset mellom celler.

**Hordeolum (rang 1):** Hordeolum er vanligvis en lokal bakteriell infeksjon (oftest *Staphylococcus aureus*) i en kjertel i øyelokket. Tecovirimat har ingen kjent antibakteriell virkning, og den høye scoren er mest sannsynlig en artefakt fra grafprediksjonen. Det samme gjelder de andre toppredikerte bakterielle tilstandene (vibrio-infeksjon, Klebsiella-infeksjon, noma, *E. coli*-infeksjon), samt HTLV-1-assosiert infektiøs dermatitt, arterivirus- og arbovirusinfeksjoner. Alle disse mangler mekanistisk grunnlag, kliniske studier og relevant litteratur.

**Vaccinia (rang 5):** Her er mekanismen sterk, siden vaccinia er et ortopoxvirus og tecovirimat blokkerer VP37-avhengig dannelse av omhyllede virioner. Dette overlapper med den opprinnelige indikasjonen. Litteraturen i datasettet gjelder hovedsakelig apekopper (mpox) og er dermed indirekte evidens for vaccinia.

**Koinfeksjon (rang 6):** Begrepet er uspesifikt. Litteraturen omhandler mpox sammen med hiv, VZV, syfilis og andre infeksjoner, der tecovirimat kun virker på ortopoxvirus-komponenten.

---

## Klinisk studieevidens

Foreløpig ingen relaterte kliniske studier registrert for noen av de predikerte indikasjonene i de samlede dataene. Kliniske studier på mpox (utenfor dette datasettet) bør verifiseres separat. Én av oversiktsartiklene (PMID 40210872) uttaler at effekten av tecovirimat i nyere kliniske studier er langt fra tilfredsstillende.

---

## Litteraturevidens

Tabellen viser de mest relevante publikasjonene for **vaccinia** (rang 5), prioritert etter studietype.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [39401235](https://pubmed.ncbi.nlm.nih.gov/39401235/) | 2024 | Oversikt | JAMA | Klinisk presentasjon, diagnostikk og behandlingsstrategier ved mpox |
| [36403582](https://pubmed.ncbi.nlm.nih.gov/36403582/) | 2023 | Oversikt | Lancet | Oversikt over apekopper, et ortopoxvirus i samme slekt som variola, vaccinia og kukopper |
| [38069596](https://pubmed.ncbi.nlm.nih.gov/38069596/) | 2024 | Systematisk oversikt | J Chemother | Systematisk gjennomgang av vaksinasjon og behandling av mpox (69 artikler) |
| [37131608](https://pubmed.ncbi.nlm.nih.gov/37131608/) | 2023 | Oversikt | bioRxiv | Antivirale midler mot apekopper; tecovirimat og brincidofovir |
| [36961984](https://pubmed.ncbi.nlm.nih.gov/36961984/) | 2023 | Oversikt | J Med Chem | Oversikt over antivirale midler mot MPXV og andre ortopoxvirus |
| [35763248](https://pubmed.ncbi.nlm.nih.gov/35763248/) | 2022 | Oversikt | Drugs | Forebygging og behandling av apekopper, inkludert vaksiner og lagrede mottiltak |
| [38801586](https://pubmed.ncbi.nlm.nih.gov/38801586/) | 2024 | Oversikt | Adv Exp Med Biol | Behandling og vaksinasjon mot kopper og apekopper |
| [36374026](https://pubmed.ncbi.nlm.nih.gov/36374026/) | 2022 | Oversikt | Antimicrob Agents Chemother | Tecovirimat mot human apekopper; effektdata hovedsakelig fra dyremodeller, ingen alvorlige bivirkninger i sikkerhetsstudier |
| [32882158](https://pubmed.ncbi.nlm.nih.gov/32882158/) | 2021 | Oversikt | Expert Rev Anti Infect Ther | Tecovirimat ved kopper og utvidet anti-ortopoxvirus-bruk; godkjent av FDA i 2018 |
| [41790953](https://pubmed.ncbi.nlm.nih.gov/41790953/) | 2026 | Prekliniske | Emerg Microbes Infect | Laktoferrin blokkerer ortopoxvirus-inntrengning; additiv effekt sammen med tecovirimat eller brincidofovir |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005248 | Tecovirimat SIGA | Ikke oppgitt | Poxviridae-infeksjoner, kukopper, apekopper, vaccinia, kopper |

Denne godkjenningen har status avregistrert/trukket tilbake. Det finnes ingen gyldige godkjenninger i Norge.

---

## Sikkerhetsbetraktninger

Se preparatomtalen for sikkerhetsinformasjon. Data om advarsler og kontraindikasjoner fra preparatomtalen mangler i de samlede dataene, og ingen legemiddelinteraksjoner ble funnet. Én oversiktsartikkel (PMID 36374026) rapporterer at sikkerhetsstudier på mennesker ikke viste alvorlige bivirkninger.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den toppredikerte indikasjonen (hordeolum) og de øvrige bakterielle og ikke-ortopoxvirale prediksjonene mangler både mekanistisk grunnlag og klinisk evidens, og er mest sannsynlig modellartefakter. Vaccinia er biologisk plausibelt, men ligger innenfor den opprinnelige indikasjonen og er derfor ikke reell repurposing. Dessuten har preparatet ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves følgende:**
- Hente og analysere sikkerhetsinformasjon (advarsler, kontraindikasjoner) fra preparatomtalen, som er en blokkerende datamangel
- Supplere data om virkningsmekanisme (MOA) fra DrugBank
- Verifisere kliniske studier på mpox og andre ortopoxvirus utenfor dette datasettet, inkludert nyere studier med tvilsomme effektresultater
- Avklare regulatorisk status i Norge, siden den eneste godkjenningen er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

