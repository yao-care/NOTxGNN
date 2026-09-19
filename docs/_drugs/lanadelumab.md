---
layout: default
title: Lanadelumab
parent: Kun modellprediksjon (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
---

# Lanadelumab
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

# Lanadelumab: Fra udokumentert originalindikasjon til C1-inhibitormangel (hereditær angiødem)

## Oppsummering i en setning

> Dokumentasjonspakken registrerer ikke en dokumentert originalindikasjon for lanadelumab (DrugBank-felt er tomt), men støttende litteratur i pakken identifiserer det som en plasmakallkrekinin-inhibitor utviklet for hereditær angiødem (HAE)-profylakse.
> TxGNN-modellen forutsier høy relevans for **C1-inhibitormangel**, som faktisk er sykdomskategorien som ligger til grunn for HAE — noe som betyr at dette signalet i stor grad **bekrefter en allerede etablert indikasjon i stedet for en ny repositioneringsmulighet**.
> Bevis er omfattende: **22 kliniske forsøk** (inkludert ett gjennomført pivot-fase 3-RCT) og **20 publikasjoner** støtter denne indikasjonen, men legemidlet er for øyeblikket **ikke markedsført i Norge** og sikkerhetsdokumentasjon mangler helt.

---

## Rask oversikt

| Punkt | Innhold |
|------|------|
| Originalindikasjon | Ikke dokumentert i DrugBank-post (felt er tomt); litteratur (PMID 30267321) identifiserer HAE-profylakse som legemidlets kjente global indikasjon |
| Forutsatt ny indikasjon | C1-inhibitormangel |
| TxGNN-prediksjonsscore | 99.996% |
| Bevisnivå | L2 (1 gjennomført fase 3-RCT + omfattende støttende fase 3/real-world/systematisk oversikt-bevis) |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte data om virkningsmekanisme ikke tilgjengelige i det strukturerte `original_moa`-feltet (flagget som datakløft DG002). Imidlertid beskriver litteratur i denne dokumentasjonspakken (PMID 30267321) lanadelumab som et fullt humanisert monoklonalt antistoff som hemmer plasmakallkrekinin. Mutasjoner i *SERPING1*-genet forårsaker C1-inhibitor (C1-INH)-mangel eller dysfunksjon, noe som fører til ukontrollert plasmakallkreinin-aktivitet og overproduksjon av bradykinin — vasodilatoren som antas å drive angiødemsymptomer.

Det er viktig å merke seg at "C1-inhibitormangel" (den forutsatte indikasjonen) ikke er et distinkt nytt sykdomsmål i forhold til lanadelumabs mekanisme — det er den underliggende patofysiologiske kategorien av hereditær angiødem, tilstanden som legemidlets egen mekanisme var designet for å behandle. Dette tyder på at TxGNN-prediksjonen her best tolkes som et **valideringssignal** (modellen korrekt gjenoppretter et kjent legemiddel-sykdom-forhold) snarere enn en sann off-label-repositioneringsmulighet. Dette forsterkes av det faktum at lanadelumab (Takhzyro®) allerede er godkjent og markedsført for HAE i USA, EU, Japan, Kina og Sør-Korea, ifølge kliniske forsøks- og litteraturbevis nedenfor — det har rett og slett ikke oppnådd autorisasjon i Norge ennå.

Fordi "originalindikasjon"-feltet i denne dokumentasjonspakken er tomt, anbefaler vi at dette behandles som et **problem med datakomplettheten** i DrugBank-ekstraksjonen i stedet for ekte fravær av en godkjent indikasjon, og flagges for korreksjon før denne kandidaten går videre.

---

## Bevis fra kliniske forsøk

| Forsøksnummer | Fase | Status | Antall deltakere | Nøkkelfunn |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Fase 3 | Avsluttet | 125 | HELP-studie — pivot-randomisert, dobbeltblindet, placebokontrollert forsøk av lanadelumab for langtidsprofylakse mot HAE-anfall (type I/II) |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Fase 3 | Avsluttet | 212 | HELP-studie forlengelse — åpen-label langtidsikkerhet og effektivitetsoppfølging |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Fase 3 | Avsluttet | 21 | SPRING-studie — PK/PD og effektivitet av lanadelumab hos pediatriske HAE-pasienter (2–<12 år) |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Fase 3 | Avsluttet | 12 | Effektivitet og sikkerhet av lanadelumab hos japanske HAE type I/II-pasienter |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Fase 3 | Avsluttet | 20 | Sikkerhet, PK og effektivitet av lanadelumab hos kinesiske HAE-pasienter over 26 uker |
| [NCT04444895](https://clinicaltrials.gov/study/NCT04444895) | Fase 3 | Avsluttet | 73 | Langtidsikkerhet/effektivitet ved ikke-histaminerg angiødem med normal C1-INH |
| [NCT04687137](https://clinicaltrials.gov/study/NCT04687137) | Fase 3 | Avsluttet | 12 | Japan Expanded Access Program før lokal lisensering |
| [NCT01923207](https://clinicaltrials.gov/study/NCT01923207) | Fase 1 | Avsluttet | 32 | Første menneske enkelt stigende dose sikkerhet/tolerabilitet/PK-studie |
| [NCT02093923](https://clinicaltrials.gov/study/NCT02093923) | Fase 1 | Avsluttet | 38 | Studie av flere stigende doser sikkerhet/tolerabilitet/PK hos HAE-fagpersoner |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | Avsluttet | 168 | EMPOWER — observasjonsstudie fra virkeligheten av HAE-anfallsrater før/etter lanadelumab (USA/Canada) |

---

## Litteraturbevis

| PMID | År | Type | Journal | Nøkkelfunn |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab reduserte signifikant HAE-anfallsrate kontra placebo (HELP-studie hovedpublikasjon) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Åpen-label forlengelse | Allergy | Langtidsprevensjon (HELP OLE) av HAE-anfall bekreftet hos pasienter ≥12 år |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Nettverksmeta-analyse | Drugs in R&D | Sammenlignende effektivitet/sikkerhet av lanadelumab vs garadacimab, C1-INH, berotralstat for LTP av HAE |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematisk oversikt | Clin Rev Allergy Immunol | Karakteriserer gjennombruddanfall hos HAE-pasienter på langtidsprofylakse inkludert lanadelumab |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | Observasjonsstudie fra virkeligheten | JACI In Practice | Flerlandsstudie INTEGRATED som bekrefter effektivitet av lanadelumab i praksis |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Oversikt | Drugs | "Første global godkjenning"-oversikt — MOA, utviklingshistorie og regulatorisk status |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Oversikt | BioDrugs | Oversikt over prekliniske og fase 1-studier av lanadelumab |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Oversikt | NEJM | Generell oversikt over hereditær angiødem-patofysiologi og behandling |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Oversikt | J Allergy Clin Immunol | Sykdomsbyrde av C1-INH-mangel HAE i Asia-Stillehavsregionen |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Oversikt | J Investig Allergol Clin Immunol | Oversikt over gjeldende og kommende HAE-behandlinger inkludert lanadelumab |

---

## Norsk markedsinformasjon

Det er for øyeblikket ingen autorisasjoner registrert i Norge. Lanadelumab har **0 lisenser** på fil og er klassifisert som **Ikke markedsført** i dette datasettet, til tross for at det er godkjent og markedsført andre steder (USA, EU, Japan, Kina, Sør-Korea) som **Takhzyro®**.

---

## Sikkerhetshensyn

Vær vennlig å se pakningsvedlegget for sikkerhetsinformasjon.

> **Merk:** Dette er en blokkerende datakløft (DG001) — ingen TFDA/lokale merkingers advarsler, kontraindikasjoner eller legemiddel-legemiddel-interaksjondata er for øyeblikket tilgjengelige for denne kandidaten, og formell S1-sikkerhetevaluering kan ikke fortsette før dette blir løst.

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
Effektivitetsbevis er sterkt — en gjennomført pivot-fase 3-RCT (HELP-studie) pluss omfattende støttende fase 3, real-world og systematisk gjennomgang av bevis på tvers av flere regulatoriske jurisdiksjoner hvor legemidlet allerede er godkjent for HAE. Imidlertid har legemidlet null markedsautorisasjoner i Norge, og en **blokkerende datakløft** hindrer enhver formell sikkerhetsgjennomgang (ingen etikett-advarsler, kontraindikasjoner eller DDI-data tilgjengelige). Den forutsatte indikasjonen er også faktisk identisk med legemidlets egen etablerte bruk, så dette bør reklassifiseres internt som indikasjonbekreftelse i stedet for en repositioneringskandidat før videre handling.

**For å gå videre, er følgende nødvendig:**
- Lokale etikett-/sikkerhetdata (TFDA-ekvivalente advarsler og kontraindikasjoner) — last ned og analysere (DG001, blokkering)
- Strukturerte virkningsmekanisme-data via DrugBank API (DG002)
- Korreksjon av det tomme `original_indications`-feltet i kildemedikamentposten — bekreft og dokumenter lanadelumabs etablerte HAE-indikasjon
- Bekreftelse av status for søknad om markedsautorisasjon i Norge, dersom planlagt

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

