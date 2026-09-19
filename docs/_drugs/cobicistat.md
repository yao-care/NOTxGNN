---
layout: default
title: Cobicistat
parent: Kun modellprediksjon (L5)
nav_order: 91
evidence_level: L5
indication_count: 3
---

# Cobicistat
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Cobicistat: Fra antiretroviral farmakokkinetisk forsterker til Simian Immunodeficiency Virus-infeksjon

## Sammendrag i en setning

Cobicistat er en CYP3A4-hemmer som brukes klinisk som farmakokkinetisk forsterker i kombinert antiretroviral terapi (f.eks. med elvitegravir, atazanavir, darunavir) snarere enn som direkte antiviralt middel i seg selv. TxGNN-modellen forutsier en mulig sammenheng til **Simian Immunodeficiency Virus-infeksjon**, men denne prediksjonen støttes for øyeblikket av **0 kliniske forsøk** og **0 publikasjoner** — det er et rent modellresultat uten støttende bevis.

---

## Hurtig oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Farmakokkinetisk forsterker (booster) for antiretroviral terapi — ikke en selvstendig sykdomsindikasjon |
| Forutsagt ny indikasjon | Simian Immunodeficiency Virus-infeksjon |
| TxGNN prediksjonspoeng | 99.92% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvente |

---

## Hvorfor er denne prediksjonen fornuftig?

En strukturert, DrugBank-dokumentert oppføring av virkningsmekanisme er for øyeblikket utilgjengelig for cobicistat (flagget som en høyalvorlighetsgrad datakløft, DG002). Basert på den farmakologiske informasjonen innebygd i modellens egen begrunnelse, er cobicistat kjent for å fungere som en CYP3A4-hemmer — den har ingen direkte antivirale aktivitet i seg selv, og dens kliniske rolle er begrenset til å øke plasmakonsentrasjoner av samtidig administrerte antiretroviraler. Den fungerer ikke direkte mot virale replikasjonssystemer.

Simian Immunodeficiency Virus (SIV) er primatanalogen til HIV og brukes vanligvis som en dyremodell for HIV-forskning. TxGNN-modellens høye poengsum for denne assosiasjonen gjenspeiler sannsynligvis nærhet i kunnskapsgrafen mellom cobicistat, HIV-relaterte stoffklasser, og SIV som en HIV-modell sykdomsenhet — snarere enn noe bevis for at cobicistat i seg selv har anti-SIV-aktivitet. I beste fall kunne cobicistat teoretisk tjene som forsterker for andre antivirale stoffer i et SIV-behandlingsregime, analogt til dets humane ARV-bruk; det ville ikke fungere som et frittstående terapeutikum.

To tilleggskandidater ble forutsagt med nesten identiske poengsum: **felint ervervet immunsviktssyndrom (FIV)**, som følger samme booster-kun logikk med økt bekymring om artsspesifikke CYP450-forskjeller mellom katter og mennesker, og en **sjelden neuro-utviklingsmessig lidelse** (ataksisk gang, manglende tale, redusert kortikal hvit substans) som det ikke finnes noen plausibel mekanistisk sammenheng til CYP3A4-hemming for. Denne tredje kandidaten vurderes som en sannsynlig falsk positiv og anbefales ikke for videre etterforskning.

---

## Klinisk forsøksbevis

Ingen relaterte kliniske forsøk er for øyeblikket registrert.

---

## Litteraturbevis

Ingen relatert litteratur er tilgjengelig for øyeblikket.

---

## Sikkerhetshensyn

Se pakkeutsendingen for sikkerhetsinformasjon.

*(Merk: TFDA-advarsler på merkingen og kontraindikasjoner er flagget som en blokkert datakløft (DG001) — påkrevd før denne kandidaten kan gå videre til en formell sikkerhetsvurdering.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvente**

**Begrunnelse:**
Alle tre TxGNN-forutsagte indikasjoner for cobicistat mangler enhver klinisk forsøk eller litteraturstøtte, og den underliggende mekanismen (en farmakokkinetisk forsterker uten iboende antivirale eller nevrologiske aktiviteter) rettferdiggjør ikke på plausibel måte frittstående terapeutisk bruk i noen av de forutsagte tilstandene. Cobicistat er heller ikke for øyeblikket markedsført i Norge, og sentrale regulatoriske og sikkerhetsmessige data mangler.

**For å gå videre, kreves følgende:**
- TFDA-ekvivalent merkingsdata — advarsler, kontraindikasjoner (DG001, blokkert)
- Bekreftet virkningsmekanisme via DrugBank API (DG002)
- Preklinisk eller in vitro-bevis som etablerer noen direkte eller forsterker-medieret relevans til SIV-infeksjon spesifikt
- Fullstendig legemiddel-legemiddel interaksjon (DDI) profil før videre evalueringsstadium

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

