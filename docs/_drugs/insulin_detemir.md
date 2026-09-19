---
layout: default
title: Insulin Detemir
parent: Kun modellprediksjon (L5)
nav_order: 184
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin detemir: Fra diabetes mellitus (original indikasjon ikke registrert) til type 1 diabetes mellitus — Datakløft flagget, ikke et ekte signal for ny bruk

## Oppsummering i én setning

Insulin detemir (DrugBank DB01307, markedsført globalt som Levemir) er et langtidsvirkende basalt insulinanalog som allerede brukes til behandling av type 1 og type 2 diabetes. TxGNN-modellens toppprognose — **Type 1 Diabetes Mellitus** — er slett ikke en ny indikasjon i det hele tatt; det er legemidlets egen veletablert, allerede godkjent bruk. Denne kandidaten finnes kun fordi `original_indications`-feltet i bevissamlingen er tomt og `market_status` viser feil som "ikke markedsført," som er datakløfter i kilderegisteret snarere enn en ekte oppdagelse av ny bruk. **34 kliniske forsøk** og **20 publikasjoner** støtter insulin detemirseffektivitet i type 1 diabetes — men som bekrefelse av kjent bruk, ikke som bevis for ny indikasjon.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke registrert i denne bevissamlingen (datakløft i registerdata). Offentlig er insulin detemir (Levemir) indisert for type 1 og type 2 diabetes mellitus. |
| Forutsagt "ny" indikasjon | Type 1 diabetes mellitus — **identisk med legemidlets faktiske etablerte bruk** |
| TxGNN-prognose score | 99.77% (rangering 2954) |
| Bevisnivå | L1 (≥2 fullførte fase 3-RCT) — gjenspeiler eksisterende-bruk-bevis, ikke bevis for ny indikasjon |
| Markedsstatus Norge | Ikke markedsført (Ikke markedsført) — flagget som sannsynlig unøyaktig gitt Levemirs kjente globale markeringshistorie |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | **Avvent** (avventer dataverifikasjon) |

## Hvorfor er denne prognosen rimelig?

Mekanistisk sett er insulin detemir rett fram: det er et løselig, langtidsvirkende humant insulinanalog asetylert med en 14-karbons fettsyre, som reversibelt binder albumin for å gi langsom, forlenget absorpsjon. Dette erstatter direkte den endogene insulinmangelen som definerer type 1 diabetes mellitus (T1DM), som er grunnen til at det gir farmakologisk mening — fordi det allerede er standard basal insulinterapi for T1DM, ikke fordi TxGNN avdekket en ny mekanistisk kobling.

Dette er det sentrale problemet med denne kandidaten: forholdet mellom "original indikasjon → ny indikasjon" som rapportmalen forventer finnes ikke her. Bevissamlingen selv flagger dette i `repurposing_rationale`: *"此為藥物之原始核准適應症（非老藥新用候選）"* — dette er legemidlets opprinnelige godkjente indikasjon, ikke en ny bruk-kandidat. Den høye TxGNN-score og rike kliniske/litteraturbevis gjenspeiler styrken i insulin detemirets etablerte bruk i T1DM, ikke oppdagelsen av en ny terapeutisk vei.

To datakløfter i kildesamlingen forårsaket sannsynligvis denne falske positive rammen: (1) `original_indications` er tomt, så pipeline hadde ingen baseline-indikasjon å sammenligne med, og (2) `market_status` viser "ikke markedsført" med null lisensar, som er inkonsistent med Levemirs kjente internasjonale markedstilstedeværelse. Begge bør korrigeres ved kilden (DrugBank/nasjonalt regulatorisk register) før dette legemidlet vurderes videre i noen ny bruk-arbeidsflyt.

## Klinisk forsøksbevis

| Forsøksnummer | Fase | Status | Antall deltakere | Sentrale funn |
|---------|------|------|------|---------|
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Fase 3 | Fullført | 470 | Insulin detemir mot NPH-insulin (begge + aspart) hos gravide kvinner med T1DM; sammenligning av glykmisk kontroll og sikkerhet |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Fase 3 | Fullført | 347 | Detemir mot NPH-insulin hos barn/ungdommer med T1DM, en eller to ganger daglig + måltid aspart |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Fase 3 | Fullført | 752 | Effektivitet/sikkerhet av detemir (2400 nmol/mL-formulering) mot NPH i T1DM basal-bolus-regime |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Fase 3 | Fullført | 598 | Detemir + aspart mot NPH + humant løselig insulin i T1DM basal-bolus-regime |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Fase 4 | Fullført | 520 | En gang daglig mot to ganger daglig detemir + aspart i T1DM: HbA1c, hypoglykemi, vekt |
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Fase 3 | Fullført | 114 | Detemir + aspart mot NPH + aspart hos voksne med T1DM |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Fase 3 | Fullført | 362 | Degludec/aspart mot detemir en/to ganger daglig + aspart hos barn/ungdommer med T1DM |
| [NCT00655200](https://clinicaltrials.gov/study/NCT00655200) | N/A (observasjonell) | Fullført | 2286 | Post-markedssikkerhet/tolerabilitet av Levemir (detemir) hos filippinsk T1DM/T2DM-pasienter |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Fase 3 | Fullført | 26 | Dapagliflozin som tillegg til liraglutid + insulin (inkl. detemir som bakgrunn) i T1DM |
| [NCT00591227](https://clinicaltrials.gov/study/NCT00591227) | Fase 4 | Fullført | 176 | ED-initialisert basal-bolus-insulin (inkl. detemir) for hyperglykemi-behandling |

## Litteraturbevis

| PMID | År | Type | Journal | Sentrale funn |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT-forsøk: degludec mot detemir (begge + aspart) hos gravide kvinner med T1DM, ikke-underlegenhet-design |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematisk oversikt/Nettverks-metaanalyse | Value Health | Sammenlignende effektivitet/sikkerhet av basale insulinregimer (inkl. detemir) hos voksne med T1DM |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | Cochrane-systematisk oversikt | Cochrane Database Syst Rev | Oversikt over (ultra-)langvirkende insulinanaloguer, inkludert detemir, for T1DM |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematisk oversikt/Metaanalyse | Pol Arch Med Wewn | Detemir mot NPH-insulin i T1DM: glykmisk kontroll-resultater |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematisk oversikt/Metaanalyse | Clin Ther | Degludec mot andre langvirkende basale analoguer (glargine, detemir) i T1D/T2D |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Oversikt | Lancet Diabetes Endocrinol | Behandling av T1DM under graviditet: livsstil, farmakologisk behandling, teknologi |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Oversikt | Drugs | Insulin detemir: oversikt over bruk i T1DM- og T2DM-behandling |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Oversikt | Vasc Health Risk Manag | Oppdatering på T1DM/T2DM-behandling, fokus på insulin detemir |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Oversikt | Vasc Health Risk Manag | Insulin detemir i behandlingen av T1DM og T2DM |
| [15691219](https://pubmed.ncbi.nlm.nih.gov/15691219/) | 2005 | Oversikt | BioDrugs | Fokus på insulin detemir i T1DM og T2DM |

## Informasjon om det norske marked

Ingen markedsføringsautorisasjonsregistreringer er tilstede i denne bevissamlingen (`total_licenses = 0`, `market_status = Not marketed/Not marketed`). Dette flagges som en sannsynlig **datakløft snarere enn faktum**: insulin detemir (Levemir, Novo Nordisk) har en langvarig global markeringshistorie inkludert i europeiske markeder. Før noen nedstrøms beslutning tas på denne kandidaten, bør det norske Legemiddelverk sjekkes direkte for å bekrefte faktisk markedsstatus og antall autorisasjoner.

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (`key_warnings`, `contraindications` og DDI-data er alle utilgjengelige i denne bevissamlingen — DG001 flagges som en **blokkerande** datakløft som hindrer sikkerhetspre-vurdering (S1).)

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Dette er ikke en ekte ny bruk-kandidat — den "forutspåtte nye indikasjon" (T1DM) er insulin detemirets egen etablerte, allerede godkjente bruk. Den høye TxGNN-score og rike bevisbase bekrefter kjent farmakologi snarere enn å avsløre noe nytt. Å fortsette under en "Proceed with Guardrails" etikett (som den rå scoringsmotoren foreslår) ville risikere å feillokalisere en datapipeline-artefakt som en oppdagelse. I tillegg er DG001 (manglende TFDA/regulatorisk merkevaringsadvarsler og kontraindikasjoner) en **blokkerande** kløft som uavhengig hindrer sikkerhetspre-vurdering (S1) uavhengig av indikasjonsnyelhet.

**For å fortsette, er følgende nødvendig:**
- Korriger `original_indications`-feltet ved kilden (DrugBank) slik at insulin detemir ikke re-flagges som en "ny" T1DM-kandidat
- Verifiser faktisk markedsstatus for Norge/EU og autorisasjonsnummere direkte mot Legemiddelverk, siden `market_status = Not marketed` synes inkonsistent med Levemirs kjente markeringshistorie
- Hent TFDA/EMA-pakningsvedlegg advarsler og kontraindikasjoner (DG001) før sikkerhetsfase-vurdering
- Hent DrugBank MOA-record (DG002) for å støtte fremtidige mekanistiske analyser
- For lavere-rangerte kandidater i denne batchen (autoimmun oofritt, opsismodysplasi, stiv person-syndrom, medikament-indusert lipodystrofi, etc.), er ingen ytterligere handling anbefalt: disse flagges i kilderationale som komorbiditets-konfundering eller omvendt-kausalitet-artefakter (f.eks. lipodystrofi er en kjent bivirkning av insulininjeksjon, ikke en behandlbar indikasjon) snarere enn troverdige signaler for ny bruk

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

