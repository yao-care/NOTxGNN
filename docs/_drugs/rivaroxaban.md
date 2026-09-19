---
layout: default
title: Rivaroxaban
parent: Moderat evidens (L3-L4)
nav_order: 311
evidence_level: L4
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **4** stk.
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

# Rivaroxaban: Fra antikoagulasjon (VTE/AF) til revmatoid artritt

## Sammendrag i én setning

> Rivaroxaban er en faktor Xa-hemmer som brukes til antikoagulasjon (VTE-profylakse/behandling og hjerneslag-forebygging ved atrieflimmer), som referert i studie- og litteraturbevisene i denne pakken (f.eks. EINSTEIN, ACT-forsøk).
> TxGNN-modellen forutsier at det kan være effektivt for **revmatoid artritt**,
> men **0 kliniske forsøk** og bare **4 tangentialt relaterte publikasjoner** støtter for øyeblikket denne retningen, og den mekanistiske begrunnelsen selv flagget dette som sannsynligvis en komorbiditetsartefakt snarere enn et ekte behandlingssignal.

---

## Rask oversikt

| Punkt | Innhold |
|-------|---------|
| Opprinnelig indikasjon | Ikke bekreftet via regulatorisk godkjenning (legemiddel ikke markedsført i Norge); konteksten for bevisepakken indikerer antikoagulasjon for VTE/AF |
| Forutsagt ny indikasjon | Revmatoid artritt |
| TxGNN prediksjonspoeng | 99.57% |
| Evidensnivå | L4 |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt avgjørelse | Utsett |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelig i de strukturerte legemiddeldata (MOA-felt er et datakav). Basert på bevis innenfor denne pakken er rivaroxaban en direkte faktor Xa-hemmer som brukes til antikoagulasjon — det har ingen kjent anti-inflammatorisk eller immunomodulatorisk aktivitet.

Revmatoid artritt (RA) er en kronisk autoimmun inflammatorisk sykdom. RA-pasienter har faktisk en forhøyet risiko for venøs tromboembolisme (VTE) på grunn av kronisk inflammasjon, og i klinisk praksis krever slike pasienter noen ganger antikoagulansterapi — men dette representerer **håndtering av medsykdom**, ikke behandling av RA selv.

Bevisepakkens egen mekanistiske vurdering er eksplisitt på dette punktet: ingen av de fire støttende publikasjonene demonstrerer en antirevmatisk effekt av rivaroxaban. Litteraturen dekker i stedet VTE-diagnose/-håndtering (inkludert hos RA-pasienter som en tilleggsdiagnose), trombingenerasjonsanalyser ved autoimmun sykdom, og DOAC-overholdelsesmønstre. Den høye TxGNN-skåren gjenspeiler mest sannsynlig en lært RA–VTE-medsykdomsassosiasjon i kunnskapsgrafen snarere enn en kausal RA-behandlingsvei. Denne kandidaten bør tolkes med betydelig forsiktighet.

---

## Bevis fra kliniske forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert.

---

## Bevis fra litteraturen

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|---------|----------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Oversikt | JAMA | Generell oversikt over diagnose og behandling av underekstremitets-DVT; ikke RA-spesifikk |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Oversikt | La Revue de médecine interne | Bruk av trombingenerasjonsanalyser ved autoimmun sykdom (inkl. antifosffolipidsyndrom) for screening av hyperkoagulabilitet; ikke en rivaroxaban-RA-effektivitetsstudie |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Kohort | PLoS One | Sammenligninger av overholdelse av rivaroxaban vs. apixaban ved atrieflimmer; ikke relatert til RA |
| [41918541](https://pubmed.ncbi.nlm.nih.gov/41918541/) | 2026 | Kasusrapport | Cureus | Tilfelle av tromboembolisk hjerneslag hos en 88-åring med atrieflimmer som tilfeldig hadde steroid-behandlet RA; RA er en bakgrunnsdetalj, ikke et behandlingsmål |

---

## Norsk markedsinformasjon

For øyeblikket ingen markedsføringsgodkjenning for rivaroxaban i Norge (0 lisenser; markedsstatus: Ikke markedsført).

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: TFDA/etikett-advarsler, kontraindikasjoner og DDI-data er flagget som et blokkerende datakav i denne bevisepakken — se Konklusjon.)*

---

## Konklusjon og neste steg

**Avgjørelse: Utsett**

**Begrunnelse:**
Det er ingen kliniske forsøksbevis og ingen litteratur som direkte demonstrerer en terapeutisk effekt av rivaroxaban på revmatoid artritt; legemidlets kjente faktor Xa-hemmer-mekanisme har ingen plausibel forbindelse til RA-sykdomsaktivitet, og den støttende litteraturen angår VTE-håndtering hos RA-pasienter snarere enn RA-behandling selv. Kombinert med et S0 beslutningstadium og L4 evidensnivå, oppfyller denne kandidaten ikke kravet for å gå videre.

**For å gå videre, er følgende nødvendig:**
- TFDA/regulatorisk etikett-data (advarsler, kontraindikasjoner) — for øyeblikket et **blokkerende** datakav
- Bekreftet virkningsmekanisme (MOA) fra DrugBank — for øyeblikket et datakav med **høy** alvorlighetsgrad
- Enhver preklinisk/mekanistisk studie som direkte knytter faktor Xa-hemming til RA-sykdomsveier, hvis slike bevis finnes
- Dersom denne kandidaten skulle revisiteres, var de andre TxGNN-flaggede indikasjoner for rivaroxaban i denne pakken (gikt, HIV-infeksjon, brachydaktyly-syndaktyly-syndrom) også vurdert og er tilsvarende Utsett — gikt og den sjeldne skjelettlidelsen mangler i det vesentlige støttende bevis, og HIV-relatert evidens angår antikoagulansikkerhet hos HIV-pasienter (legemiddel-legemiddel-interaksjoner med antiretrovirale legemidler) snarere enn antivirale effekt

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

