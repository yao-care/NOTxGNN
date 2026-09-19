---
layout: default
title: Midazolam
parent: Høy evidens (L1-L2)
nav_order: 231
evidence_level: L2
indication_count: 1
---

# Midazolam
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **1** stk.
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

# Midazolam: Fra prosedyresedasjon til søvnløshet

## Sammendrag i én setning

Midazolam er et benzodiazepinderivat med kort virkningstid etablert for prosedyresedasjon, anestesiinduksjon og status epilepticus. TxGNN-modellen forutsier at det også kan være effektivt for **søvnløshet**, et signal som understøttes av **32 gjennomgåtte kliniske forsøk** og **11 kuraterte publikasjoner**, hvorav flere er tiår gamle randomiserte kontrollerte studier som allerede demonstrerte oral midazolams effektivitet som korttids-hypnotikum.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|--------|
| Originalindikasjon | Ikke tilgjengelig fra norske lisensdata (legemiddel ikke markedsført); internasjonalt etablert for prosedyresedasjon, anestesiinduksjon og status epilepticus |
| Forutsagt ny indikasjon | Søvnløshet |
| TxGNN-prediksjonspoeng | 99.74% |
| Bevisnivå | L2 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Fortsett med sikringsmekanismer |

---

## Hvorfor er denne prediksjonen rimelig?

Bevis-pakken har et datahull i feltet `original_moa`, men ombruksgrunnlaget som medfølger prediksjonen fyller dette inn: midazolam er et benzodiazepinderivat med kort virkningstid som forsterker GABA-A reseptor-mediiert kloridkanalkonduktans, og produserer sedative, angstdempende og søvninduktive effekter. Dette plasserer det i samme farmakologiske familie som etablerte hypnotika som flurazepam og zolpidem — den mekanistiske forbindelsen til søvnløshet er direkte og godt karakterisert, ikke en ny hypotese.

Bemerkelsesverdig er at dette mindre er et genuint tilfelle av "legemiddelombru" og mer en gjenopplivelse av en tidligere validert bruk. Oral midazolam ble allerede markedsført i flere europeiske land i løpet av 1980-tallet–1990-tallet spesifikt som korttidsbehandling for søvnløshet, før det falt ut av favør sammenlignet med nyere hypnotika. TxGNN-prediksjonen er derfor konsistent med historisk klinisk presedens snarere enn en ubevist mekanistisk ekstrapolasjon.

Fordi midazolams sedasjon-/anestesibruk og dens historiske søvninduktive bruk deler den identiske GABA-A-mekanismen, er den biologiske sannsynlighet for søvnløshet høy. Hovedspørsmålet er ikke "fungerer det" (eldre RCT-er svarte allerede på det), men om det fortsatt er et *konkurransedyktig* alternativ gitt moderne hypnotika med bedre sikkerhetsprofiler dagen etter.

---

## Klinisk forsøksbevis

| Forsøksnummer | Fase | Status | Deltakere | Viktige funn |
|---------|------|------|------|---------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Fase 4 | Fullført | 111 | Deksmedetomidin vs. midazolam sammenlignet for postoperativ søvnkvalitet etter TURP under ryggmargsanestesi; måler direkte midazolams effekt på søvnutfall (Grade B). |
| [NCT04082767](https://clinicaltrials.gov/study/NCT04082767) | Fase 3 | Ukjent | 120 | Deksmedetomidin vs. midazolam sedasjonseffektivitet hos kritisk syke ventilerte barn; benzodiazepinrelatert agitasjon/delirium som sammenlikningspunkt. |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Fase 4 | Ukjent | 285 | Remimazolam (benzodiazepinanalog) vs. standardsedasjon i ICU mekanisk ventilasjon etter maxillofacial kirurgi. |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | Ikke oppgitt | Avsluttet | 5 | 24-timers polysomnografi som sammenligner deksmedetomidin vs. midazolam på søvnkvalitet/mengde og deliriumforekomst hos ICU-pasienter. |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Fase 1 | Avsluttet | 6 | Polysomnografisk sammenligning av α2-agonist vs. GABA-agonist (midazolam-klasse) sedasjon på søvnstadier og total søvntid. |
| [NCT07336095](https://clinicaltrials.gov/study/NCT07336095) | Fase 3 | Ikke påbegynt | 195 | Oral melatonin vs. oral midazolam som premedikasjoneering hos barn som gjennomgår tonsillektomi, fokusert på søvninduktiv effekt. |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | Ikke oppgitt | Rekrutterer | 280 | Preoperativ oral midazolam evaluert hos pasienter med søvnforstyrrelser/angst som gjennomgår kolorektal kreftkirurgi; oral midazolam-løsning nevnt som "sikker og effektiv for korttids-hypnose." |
| [NCT00744380](https://clinicaltrials.gov/study/NCT00744380) | Ikke oppgitt | Fullført | 23 | Deksmedetomidin vs. midazolam for å lette ICU ekstubering, sammenligning av benzodiazepinsedasjonsovergang. |
| [NCT01343095](https://clinicaltrials.gov/study/NCT01343095) | Ikke oppgitt | Avsluttet | 8 | ICU støyreduksjonsforsøk som måler sedasjonslegemiddelbruk og søvnkvalitet som sekundære endepunkter (indirekte overlapping bare). |
| [NCT06498869](https://clinicaltrials.gov/study/NCT06498869) | Ikke oppgitt | Fullført | 178 | Ketamins effekt på søvnkvalitet (PSQI) hos kolonoskopi-pasienter; midazolam brukt som del av basal sedasjonsregime. |

*Merknad: Flertallet av de 32 gjennomgåtte forsøkene studerer midazolam i perioperativ/ICU sedasjonssammenheng snarere enn kronisk søvnløshetbehandling; bare forsøkene ovenfor har direkte relevans gradert (B/C) eller eksplisitt søvn-/søvnløshetsramme.*

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | British Journal of Clinical Pharmacology | Dobbeltblindet forsøk: midazolam 15mg vs. Vesparax hos 30 pasienter med søvnløshet sekundært til neuromuskulær sykdom; midazolam var et effektivt hypnotikum, bedre tolerert, ingen bakrus-effekt. |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | 14-dagers multisenterstudie som sammenligner flurazepam og midazolam hos kroniske søvnløshetpasienter, evaluering av søvn, ytelse og plasmanivåer. |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Oppsummeringssamarbeider til ovenfor nevnt multisenterstudie med kronisk søvnløshet på flurazepam vs. midazolam. |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | RCT | Arzneimittel-Forschung | Dosebestemmelsespilotforsøk (10–30mg oral) hos 75 inneliggende pasienter med mild til moderat søvnløshet; etablerte optimal doseringsområde for midazolam som hypnotikum. |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | RCT | Journal of Clinical Medicine | Bemerker at benzodiazepiner (inkl. midazolam) tradisjonelt brukt for søvnløshet, men kan øke deliriumrisiko; evaluerer lemborexant som alternativ hos høyrisikopasienter. |
| [17988972](https://pubmed.ncbi.nlm.nih.gov/17988972/) | 2007 | Oversikt | Orvosi Hetilap | Generell oversikt over søvnløshetspatogenese (primær vs. sekundær) og hyperarousal-tilstand. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Oversikt | Acta Psychiatrica Scandinavica Suppl. | Oversikt over benzodiazepinhypnotikuers klinisk bruk, farmakokinetisk/farmakodinamisk differensiering og begrunnelse for et spekter av agenser. |
| [22729271](https://pubmed.ncbi.nlm.nih.gov/22729271/) | 2013 | Annet | Psychopharmacology | Preklinisk/atferdsstudium av zolpidems sedative og hukommelses-effekter (sammenlignbar hypnotika-klasse, ikke midazolam-spesifikk). |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Preklinisk | Pain | Musmodell som viser neuropatisk smerte-assosiert søvnløshet knyttet til endret GABAerg overføring — støtter GABA-mekanismrelevans for søvnløshet bredt. |
| [36912148](https://pubmed.ncbi.nlm.nih.gov/36912148/) | 2024 | Kohort | American Journal of Hospice & Palliative Care | Kasusbasert rapport om symptomstyring inkl. sedasjonsmidler ved livets slutt hos COVID-19-pasienter (indirekte relevans). |

---

## Norsk markedsinformasjon

Midazolam er **ikke for tiden markedsført i Norge** — bevis-pakken inneholder null autorisasjonsposter (`total_licenses: 0`). Ingen produktnavn, doseringsform eller godkjent indikasjonjtekst er tilgjengelig fra den lokale regulatoren.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

> **Merknad:** Bevis-pakken flagget et **blokkerende** datahull (DG001) for TFDA-ekvivalente etikettadvarsler/kontraindikasjoner, som for tiden hindrer denne kandidaten fra å passere S1-sikkerhetsprescreening. Dette må løses før formell sikkerhetsevaluering kan fortsette.

---

## Konklusjon og neste trinn

**Beslutning: Fortsett med sikringsmekanismer**

**Begrunnelse:**
Den mekanistiske forbindelsen er sterk og historisk validert — oral midazolam ble klinisk bevist effektiv for søvnløshet i flere RCT-er (1981–1990) og ble til og med markedsført for denne bruken i Europa. Imidlertid er de fleste støttende bevis tiår gamle, småskala, og legemiddelet er for tiden umarkedsført i Norge med et **blokkerende datahull** på etikettsikkerhetsinformasjon (advarsler/kontraindikasjoner), så sikringsmekanismer er nødvendig før videre fremdrift.

**For å fortsette kreves følgende:**
- TFDA/lokal pakningsvedleggdata (advarsler, kontraindikasjoner) — løser blokkerende gap DG001
- Formell legemiddel-legemiddel interaksjonsdata (DDI) (for tiden `not_found`)
- Strukturert opprinnelig MOA og originalindikasjonsdokumentasjon for det regulatoriske dossieret — løser gap DG002
- Vurdering av regulatorisk inngangssti for marked, siden midazolam har null autorisasjoner i Norge
- Moderne sammenlignende effektivitetsdata mot moderne hypnotika (f.eks. zolpidem, lemborexant), gitt at de fleste positive søvnløshetsforsøk stammer fra før dagens standard for behandling

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

