---
layout: default
title: Glecaprevir
parent: Moderat evidens (L3-L4)
nav_order: 162
evidence_level: L4
indication_count: 10
---

# Glecaprevir
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **10** stk.
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

# Glecaprevir: Fra hepatitt C-virusinfeksjon til HIV-infeksjonssykdom

## Sammendrag i en setning

> Glecaprevir er en NS3/4A-proteaseinhibitor som opprinnelig ble utviklet (som glecaprevir/pibrentasvir-kombinasjonen, f.eks. Mavyret/Maviret) for kronisk hepatitt C-virusinfeksjon (HCV).
> TxGNN-modellen rangerer **HIV-infeksjonssykdom** som sin #1 foreslåtte nye indikasjon med en **99,87 % score**,
> men den støttende evidensen — **15 kliniske forsøk** og **19 publikasjoner** — beskriver nesten utelukkende HCV-behandling i HIV/HCV-koinfiserte populasjoner, ikke direkte antiretroviral aktivitet, og stoffets egen ombruksgrunnlag flagger dette som en sannsynlig falsk positiv.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Kronisk hepatitt C-virusinfeksjon *(utledet fra klinisk forsøkskopus i denne bevispappen — DrugBank `original_indications` og `original_moa` felt var tomme/Datagap)* |
| Foreslått ny indikasjon | HIV-infeksjonssykdom |
| TxGNN prediksjons-score | 99,87 % (rangering 1845) |
| Bevisnivå | L4 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | **Avvent** |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme for glecaprevir er ikke tilgjengelig i det oppgitte DrugBank-registeret (Datagap). Basert på klinisk forsøksevidents i denne pakken, er glecaprevir godt etablert som en **NS3/4A serinproteasehibitor**, sam-formulert med NS5A-inhibitoren pibrentasvir, for pan-genotypisk kronisk HCV-infeksjon. Det er ingen dokumentert affinitet for HIV-protease eller noen annen HIV-replikasjonsmål.

Mekanistisk sett tilhører HCV (Flaviviridae) og HIV (Retroviridae) urelaterte virusfamilier med strukturelt distinkte proteasenzymer; det er ingen kjent kryssreaktivitet. Den høye TxGNN-scoren reflekterer mest sannsynlig en **komorbiditetskonfunder** snarere enn et genuint farmakologisk signal: nesten alle forsøk hentet for denne kandidaten inkluderte HIV/HCV-koinfiserte pasienter der glecaprevir/pibrentasvir ble brukt til å kurere *HCV*-komponenten, mens HIV ble behandlet separat med antiretroviral terapi. Ett hentet forsøk (NCT02634008) involverer ikke engang glecaprevir — det testet et annet regime (paritaprevir/ritonavir/ombitasvir/dasabuvir).

Dette mønsteret er konsistent over hele top-10 prediksjonslisten: ved siden av HIV, rangerer TxGNN også kattAIDS, apeimmunsviktvirus-infeksjon, hepatitt A/B/E og to sjeldne Flaviviridae-blødingsfebere — ingen av disse har direkte støttende bevis for glecaprevirs antivirale aktivitet. Dette antyder at modellen plukker opp et "virusinfeksjon" / "koinfisert populasjon"-mønster i kunnskapsgrafen snarere enn et spesifikt, mekanistisk begrunnet ombruksignal for HIV.

---

## Klinisk forsøksevidents

| Forsøksnummer | Fase | Status | Inkludering | Viktige funn |
|---------|------|------|------|---------|
| [NCT02634008](https://clinicaltrials.gov/study/NCT02634008) | Fase 3 | Avsluttet | 83 | Pilotstudie i fersk HCV-infeksjon ± HIV-koinfeksjon; **bruker et annet regime (paritaprevir/ritonavir/ombitasvir/dasabuvir)**, ikke glecaprevir — gradert lav relevans |
| [NCT05108935](https://clinicaltrials.gov/study/NCT05108935) | N/A | Avsluttet | 17 | Telemedisinsk levering av MOUD, HIV PrEP og HCV-behandling ved nåleutvekslingssteder; ikke et glecaprevir-effektivitetsforsøk for HIV |
| [NCT04577482](https://clinicaltrials.gov/study/NCT04577482) | N/A | Avsluttet | 42 | Virkelighetsresultater for SVR med glecaprevir/pibrentasvir hos DAA-erfarne kroniske HCV-pasienter (Russland); HIV-status var ikke endepunktet |
| [NCT07040319](https://clinicaltrials.gov/study/NCT07040319) | Fase 1/2 | Ikke rekrutterer ennå | 30 | PK/sikkerhet for glecaprevir/pibrentasvir initialisert ved graviditet for HCV, med/uten HIV-koinfeksjon; sikkerhet, ikke HIV-effektivitet |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Fase 4 | Avsluttet | 87 | Kardiovaskulær risiko etter HCV-utryddelse hos HIV-monoinfiserte vs. HCV/HIV-koinfiserte pasienter — observasjonell, ikke et HIV-legemiddeleffektivitetsforsøk |
| [NCT02738138](https://clinicaltrials.gov/study/NCT02738138) (EXPEDITION-2) | Fase 3 | Avsluttet | 153 | Effektivitet/sikkerhet for glecaprevir/pibrentasvir for HCV hos HIV-1-koinfiserte voksne; primært endepunkt er HCV SVR12, ikke HIV virale load |
| [NCT02939989](https://clinicaltrials.gov/study/NCT02939989) (MAGELLAN-3) | Fase 3 | Avsluttet | 33 | Glecaprevir/pibrentasvir + sofosbuvir/ribavirin hos HCV-pasienter med virologisk svikt; kun HCV-endepunkt |
| [NCT03222583](https://clinicaltrials.gov/study/NCT03222583) | Fase 3 | Avsluttet | 546 | Stor asiatisk RCT for glecaprevir/pibrentasvir for HCV genotyper 1–6, med/uten HIV-koinfeksjon; HIV er en baseline-kovariant, ikke den behandlede tilstanden |
| [NCT04352309](https://clinicaltrials.gov/study/NCT04352309) (EASY) | N/A | Avsluttet | 99 | Virkelighetseffektivitet av åtte ukers glecaprevir/pibrentasvir ved HCV + sirrose (Russland); ingen HIV-effektivitetsdata |
| [NCT03868163](https://clinicaltrials.gov/study/NCT03868163) | N/A | Avsluttet | 161 | Virkelighetseffektivitet av glecaprevir/pibrentasvir ved kronisk HCV genotyper 1–6 (Russland); ingen HIV-effektivitetsdata |

**Ingen av de hentede forsøkene evaluerer glecaprevir som en behandling for HIV selv.** Alle behandler enten HCV-komponenten av HIV/HCV-koinfeksjon eller er urelaterte sikkerhet-/logistikkstudier.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [31504702](https://pubmed.ncbi.nlm.nih.gov/31504702/) | 2020 | DDI-studie | J Infect Dis | Karakteriserer legemiddelinteraksjoner mellom glecaprevir/pibrentasvir og HIV-antiretroviraler — relevant for **sam-administreringssikkerhet**, ikke anti-HIV-effektivitet |
| [37671831](https://pubmed.ncbi.nlm.nih.gov/37671831/) | 2023 | Kohort | J Antimicrob Chemother | Virkelighets-SVR til glecaprevir/pibrentasvir hos HIV/HCV-koinfiserte pasienter; HIV er lavere med SVR til HCV, ikke behandlet av legemidlet |
| [34664197](https://pubmed.ncbi.nlm.nih.gov/34664197/) | 2021 | Kasuistikk | Clin J Gastroenterol | Vellykket HCV-genotype 4a-klaring med glecaprevir/pibrentasvir hos en HIV/HCV-koinfisert hemofili-pasient |
| [36415300](https://pubmed.ncbi.nlm.nih.gov/36415300/) | 2022 | Kasuistikk | J Prev Med Hyg | Hyperbiluribinemi/gulhet under glecaprevir/pibrentasvir + ART hos en HIV-infisert pasient — sikkerhetssignal, ikke effektivitet |
| [39697370](https://pubmed.ncbi.nlm.nih.gov/39697370/) | 2024 | N/A | Clin Exp Hepatol | Effektivitet av glecaprevir/pibrentasvir for HCV hos HIV/HCV-koinfiserte pasienter på bictegravir/FTC/TAF |
| [29595065](https://pubmed.ncbi.nlm.nih.gov/29595065/) | 2018 | Oversikt | Expert Opin Pharmacother | Oversikt over proteasehibitor-terapi for HCV, inkludert HIV/HCV-koinfeksjonssammenheng |
| [30671330](https://pubmed.ncbi.nlm.nih.gov/30671330/) | 2017 | Oversikt | GMS Infect Dis | Proteasehibitorer for HCV-behandling, inkludert HIV-koinfiserte populasjoner |
| [30499343](https://pubmed.ncbi.nlm.nih.gov/30499343/) | 2019 | Oversikt | Future Microbiol | Glecaprevir/pibrentasvir for kronisk HCV-infeksjon |
| [29845496](https://pubmed.ncbi.nlm.nih.gov/29845496/) | 2018 | Oversikt | Hepatol Int | Glecaprevir/pibrentasvir ekspanderer tilgangen til HCV-terapi |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | Konferanserapport | AIDS Reviews | Rapport fra virushepatittkonferanse; HBV/HCV-byrde og DAA-landskap |

**Ingen publikasjon rapporterer direkte antiretroviral (anti-HIV) aktivitet for glecaprevir.** Den sterkeste direkte relevansen er DDI-papiret (PMID 31504702), som er en sikkerhet/sam-administreringsreferanse for behandling av HCV ved siden av HIV-terapi — ikke bevis for en HIV-indikasjon.

---

## Markedsinformasjon for Norge

Glecaprevir er for øyeblikket **ikke markedsført i Norge** — ingen markedsføringsautoriseringer ble funnet (`total_licenses: 0`, `licenses: []`).

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. *(Nøkkelvarsler, kontraindikasjoner og DDI-data var alle flagget som Datagap / ikke funnet i denne evidensenpakken. Merk separat: metadatagap-loggen lister TFDA/etikett-varsler-gapet (DG001) som **Blokkering** for S1-sikkerhetsgjennomgang, og MOA-gapet (DG002) som **Høy** påvirkning.)*

---

## Konklusjon og neste skritt

**Beslutning: Avvent**

**Begrunnelse:**
Til tross for en høy TxGNN-score, er det mekanistiske grunnlaget for glecaprevir som behandler HIV fraværende (HCV NS3/4A vs. HIV-protease deler ingen målhomologi), og hver hentet studie/publikasjon behandler HCV-behandling hos HIV-koinfiserte pasienter snarere enn anti-HIV-aktivitet. Det interne ombruksgrunnlaget identifiserer eksplisitt dette som en sannsynlig komorbiditet-drevet falsk positiv, forsterket av tilstedeværelsen av biologisk implausible sam-rangerte prediksjoner (kattAIDS, SIV, sjeldne blødingsfebere) i samme top-10-liste.

**For å gå videre, er følgende nødvendig:**
- Direkte *in vitro*-anti-HIV-aktivitetsdata for glecaprevir (for øyeblikket fraværende) før denne kandidaten kan gå forbi S0
- Løsning av Datagap DG002 (MOA) via DrugBank API-spørring
- Løsning av Datagap DG001 (TFDA/etikett-varsler og kontraindikasjoner) — for øyeblikket blokkering for S1-sikkerhetsevaluering
- Hvis det ikke blir funnet direkte antivirale bevis mot HIV, bør denne kandidaten lukkes som et nettverksartefakt falsk positiv snarere enn å drives videre

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

