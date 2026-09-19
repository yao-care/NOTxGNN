---
layout: default
title: Lamivudine
parent: Kun modellprediksjon (L5)
nav_order: 197
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Lamivudine: Fra antiretroviral terapi til felin ervervet immunsviktsyndrom

## Oppsummering i én setning

> Lamivudine (3TC) er en nukleosidrevers transkriptasehemmer kjent offentlig for behandling av HIV-1 og kronisk hepatitt B, selv om denne bevissamlingen ikke dokumenterer den opprinnelige indikasjonen (merket som datamanko).
> TxGNN-modellens topprangerte prediksjon er **felin ervervet immunsviktsyndrom** — en sykdom som kun forekommer hos katter, ikke hos mennesker —
> støttet av **5 kliniske forsøk** (alle faktisk om HIV-1 hos mennesker, ikke felin sykdom) og **5 publikasjoner** (alle in vitro/dyrestudier med katter).
> Dette er ikke en levedyktig kandidat for legemiddelrepurposing hos mennesker; det gjenspeiler en artsmismatch-artefakt i prediksjons-pipelinen.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke dokumentert i denne bevissamlingen (`original_indications` tom, `original_moa` flagget som datamanko DG002). Lamivudine er allmenn kjent som en NRTI antiretroviral for HIV-1/kronisk hepatitt B, men dette er ikke hentet fra samlingen. |
| Predikert ny indikasjon | Felin ervervet immunsviktsyndrom (FIV-infeksjon hos katter) |
| TxGNN-prediksjonspoengsum | 99.93% (rangering 1070) |
| Bevisnivå | L4 (prekliniske/dyrestudier bare; intet klinisk humanbevis for denne indikasjonen eksisterer eller kan eksistere) |
| Status på norsk marked | Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | **Avvent** |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljert handlingsmekanismedata ikke tilgjengelig i denne bevissamlingen (DG002). Basert på offentlig farmakologisk kunnskap hemmer lamivudine retroviral revers transkriptase og brukes hos mennesker mot HIV-1 og hepatitt B-virus.

Den mekanistiske logikken bak denne prediksjonen er reell: Felin immunsviktsvirus (FIV) er et lentivirus nært beslektet med HIV, og lamivudine (ofte kombinert med zidovudin) har blitt studert eksperimentelt hos katter som et veterinært analogon til human antiretroviral terapi. Dette er en vel etablert bruk av HIV/FIV-dyremodellen i retroviroløgi-forskning.

Men **"felin ervervet immunsviktsyndrom" er en sykdom hos husekatter, ikke hos mennesker**, og kan ikke forfølges som en human indikasjon for legemiddelrepurposing gjennom noen regulatorisk vei. Det høye TxGNN-poengsummet skyldes sannsynligvis at legemidlets genuine antiretroviral mekanisme er riktig koblet til en lentiviral sykdom i kunnskapsgrafen, uten et artfilter. Denne kandidaten bør behandles som en forskningsmessig/veterinær-farmakologisk kuriøsitet snarere enn en human indikasjon for repurposing-evaluering.

---

## Klinisk forsøksbevis

⚠ Merk: ingen av forsøkene nedenfor studerer faktisk felin AIDS (umulig i et forsøk hos mennesker). De er lamivudine/HIV-1-forsøk hos mennesker som ble hentet ved legemiddelnavn-søk, ikke sykdomssøk, og utgjør ikke bevis for den predikterte indikasjonen.

| Forsøksnummer | Fase | Status | Deltakelse | Viktige funn |
|---------|------|------|------|---------|
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Fase 3 | Avsluttet | 13 | Dolutegravir + abacavir/lamivudine hos ART-naive HIV-1-voksne; CNS/plasma PK over 96 uker |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Avsluttet | 844 | Dolutegravir + abacavir/lamivudine mot Atripla hos ART-naive HIV-1-voksne, ikke-inferiøriitet over 96 uker |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Avsluttet | 208 | Dosisvalg av dolutegravir med abacavir/lamivudine eller tenofovir/emtricitabin hos ART-naive HIV-1-voksne |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Avsluttet | 145 | Forsterket darunavir + lamivudine mot darunavir + emtricitabin/tenofovir eller lamivudine/tenofovir hos naive HIV-1-pasienter |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Fase 3 | Avsluttet | 828 | Dolutegravir mot raltegravir, begge med dobbel NRTI-rygg (ABC/3TC eller TDF/FTC), hos ART-naive HIV-1-voksne |

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Dyrestudie | Viruses | Evaluerte ZDV, ZDV+IFN-α, ZDV+lamivudine og ZDV+valproinsyre hos naturlig FIV-infiserte katter over 1 år |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Kasuistikk (dyr) | J Feline Med Surg | Langtidsoppfølging med antiretroviral terapi hos FIV-infiserte husekatter |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | In vitro/in vivo | Vet Immunol Immunopathol | AZT/3TC-kombinasjonen viste additiv-til-synergisk anti-FIV-aktivitet i PBMCs |
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | In vitro | Antiviral Res | Kombinert zidovudin/lamivudine/abacavir undertrykket FIV-replikasjon in vitro |
| [11327469](https://pubmed.ncbi.nlm.nih.gov/11327469/) | 2001 | In vitro | Am J Vet Res | Karakteriserte 3TC-resistente FIV-mutanter og replikasjonskinetikk |

---

## Norsk markedsinformasjon

Ikke markedsført — 0 godkjennelser registrert, ingen lisensoppføringer tilgjengelig i bevissamlingen.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (Alle viktige advarsler, kontraindikasjoner og DDI-felt i denne bevissamlingen er flagget som datamanko; TFDA/etikett-data var ikke hentbar — se DG001, klassifisert som **blokkeringsseveritetsdatamanko**.)

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den topprangerte TxGNN-prediksjonen (felin ervervet immunsviktsyndrom) er en veterinær sykdom uten human ekvivalent, så den kan ikke gå videre gjennom en human repurposing-vei uansett prediksjonspoengsum. Klinisk forsøksbevis knyttet til den er uoverensstemmende (human HIV-forsøk, ikke FIV), og litteraturen er begrenset til in vitro/dyrestudier. I tillegg hindrer en blokkeringsseveritetsdatamanko (manglende TFDA-etikett/advarsler) enhver stage 1-sikkerhetsvurdering selv dersom en gyldig human indikasjon ble erstattet.

**For å fortsette trengs følgende:**
- Kjør indikasjonsfiltreringen på nytt for å ekskludere ikke-human/veterinær sykdomsuttrykk fra kandidatlisten
- Løs DG001 (TFDA-etikett/advarsler) og DG002 (MOA) før evaluering av eventuell gjenværende kandidat
- Merk: rangeringene 2–5 i denne samme bevissamlingen (SIV-infeksjon, en ultra-sjelden neurouviklingsforstyrrelse, en foreldet lipidstoffskiftesykdom-betegnelse og sannsynlig HBV/HCV-feilmerking) ble allerede uavhengig vurdert som **Avvent** — dette legemiddelet har for tiden ingen handlingsbar repurposing-kandidat i samlingen.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

