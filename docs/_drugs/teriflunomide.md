---
layout: default
title: Teriflunomide
parent: Høy evidens (L1-L2)
nav_order: 351
evidence_level: L1
indication_count: 1
---

# Teriflunomide
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

# Teriflunomid: Fra etablert bruk til TxGNN-bekreftet Multipel Sklerose med relapser og remisjon

## Sammenfatting i en setning

> Teriflunomid (DrugBank DB08880) er det aktive orale sykdomsmodifiserende legemiddelet som markedsføres internasjonalt som Aubagio®; strukturerte original-indikasjondata er ikke tilgjengelige i det lokale regulatoriske datasettet, men publisert litteratur bekrefter at det har vært lisensiert i EU/USA for Multipel Sklerose med relapser og remisjon (RRMS) siden 2013.
> TxGNN-modellen forutsier uavhengig **RRMS** som sin toppindikasjon med en **99.24%** tillitsscore — dette er et tilfelle der modellen gjenoppretter legemidlets egen etablerte indikasjon i stedet for å avdekke en genuint ny.
> Forutsigelsen er støttet av **30 kliniske forsøk** (inkludert flere fullførte fase 3 pivotal-/sammenlignings-RCT-er) og **20 publikasjoner**, som representerer veldig sterk evidens, selv om legemiddelet for tiden ikke markedsføres lokalt og et kritisk lokalt sikkerhetsetikett-datagap gjenstår uløst.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Originalindikasjon | Ikke dokumentert i lokale regulatoriske data (legemiddelet er ikke markedsført lokalt); offentlig kjent internasjonalt som Multipel Sklerose med relapser og remisjon (Aubagio®, EU-godkjent siden 2013) |
| Forutsagt ny indikasjon | Multipel Sklerose med relapser og remisjon |
| TxGNN-forutsigelsesscore | 99.24% |
| Evidensnivå | L1 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne forutsigelsen rimelig?

Feltet `original_moa` er ikke utfylt, men støttelitteraturen er konsistent og spesifikk: teriflunomid er en oral, selektiv og reversibel hemmer av det mitokondrialt enzym **dihydro-orotat dehydrogenase (DHODH)**. Ved å blokkere de novo-pyrimidinsyntes reduserer det proliferasjon og aktivering av raskt delende lymfocytter (både T- og B-celler), og produserer en anti-inflammatorisk, immunomodulerende effekt (PMID 31098896, PMID 32757523).

Den forutsatte indikasjon — RRMS — er ikke et nytt terapeutisk område for teriflunomid; det er legemidlets egen etablerte, globalt godkjente bruk (markedsført som Aubagio® i EU siden august 2013, per PMID 26758290, og brukt som aktivt sammenligningsstoff i tallrike fase 3-forsøk mot nyere sykdomsmodifiserende terapier). Dette betyr at TxGNN-scoren her bør tolkes som et **valideringssignal** — modellen gjenoppretter korrekt et velljent legemiddel–sykdomsforhold med veldig høy selvtillit — snarere enn som en genuint ny bruksindikasjon.

Fordi det lokale (Taiwan/Norge) regulatoriske datasettet viser null lisenser og ingen registrert originalindikasjon, er denne kandidatens praktiske verdi mindre om vitenskapelig nyhet og mer om å flagge at **teriflunomid for tiden mangler lokal markedsautorisasjon**, til tross for robust global effektivitets- og sikkerhetdata for RRMS.

---

## Klinisk forsøksbevis

| Forsøksnummer | Fase | Status | Rekruttering | Viktige funn |
|---------|------|------|------|---------|
| [NCT00134563](https://clinicaltrials.gov/study/NCT00134563) | Fase 3 | Fullført | 1088 | Pivotal RCT (TEMSO) — teriflunomid reduserte relappsfrekvens og invaliditetsakumulasjon sammenlignet med placebo i RMS |
| [NCT00883337](https://clinicaltrials.gov/study/NCT00883337) | Fase 3 | Fullført | 324 | TENERE-studie — sammenlignet teriflunomid (to doser) mot interferon beta-1a på tid til manglende effekt og relappsfrekvens |
| [NCT00803049](https://clinicaltrials.gov/study/NCT00803049) | Fase 3 | Fullført | 742 | Langtidsforlengelse som dokumenterer sikkerhet/toleranse av teriflunomid 7 mg og 14 mg over tid |
| [NCT04788615](https://clinicaltrials.gov/study/NCT04788615) | Fase 3 | Fullført | 185 | Ofatumumab mot legevalgt første-linje sykdomsmodifiserende terapi (inkl. teriflunomid) i nydiagnostisert RMS |
| [NCT07189325](https://clinicaltrials.gov/study/NCT07189325) | Fase 3 | Ikke ennå rekruttering | 250 | Anti-CD20-vedlikehold mot nedgradering-strategi i RRMS (teriflunomid-kontekstforsøk) |
| [NCT00228163](https://clinicaltrials.gov/study/NCT00228163) | Fase 2 | Fullført | 147 | Langtidssikkerhet/effektivitetsforlengelse fra tidlig fase 2 teriflunomid-studie |
| [NCT02490982](https://clinicaltrials.gov/study/NCT02490982) | N/A | Fullført | 106 | Observasjonell effektivitetsstudie av teriflunomid i virkelig verden RRMS-praksis |
| [NCT03464448](https://clinicaltrials.gov/study/NCT03464448) | N/A | Fullført | 30 | Mekanistisk fase 4-studie på regulatoriske B-lymfocytter som mediatorer av teriflunomids terapeutiske effekt |
| [NCT04129736](https://clinicaltrials.gov/study/NCT04129736) | Fase 4 | Fullført | 12 | Måling av teriflunomid 14 mg konsentrasjon i serum og cerebrospinalvæske |
| [NCT01881191](https://clinicaltrials.gov/study/NCT01881191) | N/A | Fullført | 50 | 12-måneders MRI-studie av teriflunomids effekt på grå materie-patologi |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [32757523](https://pubmed.ncbi.nlm.nih.gov/32757523/) | 2020 | RCT | NEJM | Ofatumumab mot teriflunomid direkte sammenligningsforsøk; beskriver teriflunomids mekanisme (pyrimidinsyntes-inhibisjon, redusert T/B-celleaktivering) |
| [40202623](https://pubmed.ncbi.nlm.nih.gov/40202623/) | 2025 | RCT | NEJM | Tolebrutinib (BTK-hemmer) mot teriflunomid i MS med relapser |
| [36001711](https://pubmed.ncbi.nlm.nih.gov/36001711/) | 2022 | RCT | NEJM | Ublituximab mot teriflunomid i MS med relapser |
| [33779698](https://pubmed.ncbi.nlm.nih.gov/33779698/) | 2021 | RCT | JAMA Neurology | OPTIMUM-forsøk — ponesimod mot teriflunomid, første fase 3 direkte sammenligningsforsøk av to orale sykdomsmodifiserende terapier |
| [39307151](https://pubmed.ncbi.nlm.nih.gov/39307151/) | 2024 | RCT | Lancet Neurology | Evobrutinib (BTK-hemmer) mot teriflunomid, fase 3 evolutionRMS1/2-forsøk |
| [35266417](https://pubmed.ncbi.nlm.nih.gov/35266417/) | 2022 | RCT | Mult Scler | ASCLEPIOS I/II — ofatumumab mot teriflunomid hos behandlingsnaive MS-pasienter |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Systematisk gjennomgang | Cochrane Database Syst Rev | Nettverks metaanalyse av immunomodulatorer/immunosuppressiva (inkl. teriflunomid) for RRMS |
| [31098896](https://pubmed.ncbi.nlm.nih.gov/31098896/) | 2019 | Oversikt | Drugs | Omfattende oversikt over teriflunomids mekanisme, RCT og reell verden-evidens i RRMS |
| [33620411](https://pubmed.ncbi.nlm.nih.gov/33620411/) | 2021 | Oversikt | JAMA | Generell MS-diagnose og behandlingsoversikt som refererer til teriflunomid som første-linje sykdomsmodifiserende terapi |
| [26758290](https://pubmed.ncbi.nlm.nih.gov/26758290/) | 2016 | Oversikt | CNS Drugs | Oversikt over EU Summary of Product Characteristics for teriflunomid, inkludert sikkerhetsresultater |

---

## Markedsinformasjon Norge

Teriflunomid har for tiden **ingen markedsautorisasjon** i det lokale (Taiwan/Norge) regulatoriske datasettet (0 lisenser registrert). Ingen produkt, dosisform eller godkjent indikasjonestekst er tilgjengelig til oppsummering.

---

## Sikkerhetshensyn

Vær vennlig å referere til pakningsvedlegget for sikkerhetsinformasjon.

*Merk: Et lokalt regulatorisk etikett (TFDA advarsler/kontraindikasjoner) har ikke ennå blitt hentet og er flagget som et kritisk datagap — se Konklusjon nedenfor.*

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
- Global klinisk evidens for teriflunomid i RRMS er omfattende og sterk (L1: flere fullførte fase 3 RCT-er, omfattende sammenligningslitteratur, lange-etablert internasjonal godkjenning), men den forutsatte indikasjon er i hovedsak **legemidlets allerede kjente primære indikasjon** snarere enn et signal om genuint omformål — denne kandidaten bekrefter modellen i stedet for å identifisere ny verdi.
- Mer kritisk, et **kritisk** datagap (DG001: TFDA etikett advarsler/kontraindikasjoner) forhindrer kandidaten fra å gå inn i S1 sikkerhetspre-vurdering-stadiet, og legemiddelet har null lokale markedsautorisasjoner.

**For å fortsette, kreves følgende:**
- Hent og parse det offisielle lokale produktetiketten (advarsler, kontraindikasjoner) — nødvendig for å rydde bort det kritiske gapet (DG001)
- Hent strukturert MOA-bekreftelse fra DrugBank (DG002)
- Avklare om en lokal markedsautorisasjonssøknad er planlagt, gitt teriflunomids etablerte internasjonale godkjenning (Aubagio®) for denne samme indikasjon
- Fordi denne forutsigelsen i stor grad reproduserer en kjent indikasjon, bør du vurdere å kjøre TxGNN på nytt med kjente indikasjononer ekskludert for å identifisere genuint nye bruksindikasjonkandidater for dette legemiddelet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

