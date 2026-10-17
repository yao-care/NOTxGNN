---
layout: default
title: Dabigatran Etexilate
parent: Kun modellprediksjon (L5)
nav_order: 109
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Dabigatran Etexilate: predikert ny indikasjon Skleroserende kolangitt (evidensnivå L5). Opprinnelig indikasjon: Leddprotesekirurgi (artroplastikk) og venøs tromboembolisme"
monitor_inn: "dabigatran etexilate"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

# Dabigatranetexilat: Fra venøs tromboembolisme til skleroserende kolangitt

## Oppsummering i én setning

Dabigatranetexilat (Pradaxa) er en direkte trombinhemmer som opprinnelig brukes til forebygging og behandling av venøs tromboembolisme, blant annet etter leddprotesekirurgi.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **skleroserende kolangitt**, men dette er en ren modellprediksjon.
Dataene som er samlet inn for denne rapporten, inneholder **ingen kliniske studier** og **én publikasjon** (en oversiktsartikkel om legemiddelinteraksjoner hos et annet legemiddel), som ikke viser effekt ved sykdommen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Leddprotesekirurgi (artroplastikk) og venøs tromboembolisme |
| Predikert ny indikasjon | Skleroserende kolangitt |
| TxGNN-prediksjonsscore | 99,82 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalte/avregistrerte lisenser (ingen gyldige) |
| Antall godkjenninger | 3 (alle kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige. Basert på kjent informasjon er dabigatran en direkte trombinhemmer. Effekten er dokumentert ved venøs tromboembolisme, men mekanistisk er det uklart om den kan brukes ved skleroserende kolangitt.

Det finnes en teoretisk kobling: trombin og PAR-1-signalering er assosiert med fibrose og inflammasjon, og skleroserende kolangitt er en fibroserende, inflammatorisk gallegangssykdom. Denne koblingen er imidlertid ikke støttet av kliniske data for denne sykdommen.

Den høye modellscoren (0,998) er derfor ikke i seg selv et argument for effekt. Prediksjonen bør betraktes som en hypotese som må testes i prekliniske studier først.

### Øvrige prediksjoner (kort oversikt)

| Rangering | Predikert sykdom | Score | Evidensnivå | Vurdering |
|------|------|------|------|------|
| 2 | Foreldet term for familiær kombinert hyperlipidemi | 99,63 % | L5 | Ingen mekanistisk kobling; termen er foreldet og kan være en ontologi-artefakt |
| 3 | Hypoalfalipoproteinemi | 99,57 % | L5 | Ingen plausibel mekanisme; én fase 1-studie som sannsynligvis gjelder et annet stoff |
| 4 | Homozygot familiær hyperkolesterolemi | 99,49 % | L5 | Ingen mekanistisk begrunnelse |
| 5 | Primær frigjøringsforstyrrelse av blodplater | 99,06 % | L5 | Uklar terapeutisk retning; en antikoagulant kan forverre blødningsrisiko |

---

## Evidens fra kliniske studier

For hovedprediksjonen (skleroserende kolangitt) er det foreløpig ingen relaterte kliniske studier registrert.

For en av de øvrige prediksjonene (hypoalfalipoproteinemi) er det funnet én studie, men den er vurdert som svært svakt relevant:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT07629999](https://clinicaltrials.gov/study/NCT07629999) | Fase 1 | Rekrutterer | 136 | Førstegangs-i-menneske-studie av BMS-986533 hos friske, med vurdering av sikkerhet, farmakokinetikk og P-gp/BCRP-mediert interaksjonspotensial. Antas å gjelde et annet legemiddel; ingen påvist kobling til dabigatran. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Oversikt | Clinical Pharmacokinetics | Vurdering av CYP- og transportørmedierte legemiddelinteraksjoner for cilofexor (FXR-agonist under utvikling mot bl.a. primær skleroserende kolangitt). Gjelder ikke dabigatran og gir ikke evidens for effekt. |
| [19875000](https://pubmed.ncbi.nlm.nih.gov/19875000/) | 2009 | Oversikt | Annales françaises d'anesthésie et de réanimation | Oversikt over effekt og sikkerhet for dabigatran ved godkjent tromboembolisk bruk. Ingen data om primær frigjøringsforstyrrelse av blodplater (rangering 5). |

---

## Markedsinformasjon for Norge

Alle tre registrerte godkjenninger er kansellert, og det finnes ingen gyldige lisenser.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000829 | Pradaxa | – | Artroplastikk, venøs tromboembolisme |
| EMEA/H/C/005922 | Dabigatran etexilate Teva (tidligere Dabigatran etexilate Leon Farma) | – | Venøs tromboembolisme, artroplastikk |
| EMEA/H/C/005639 | Dabigatran Etexilate Accord | – | Venøs tromboembolisme, artroplastikk |

---

## Sikkerhetsvurderinger

Pakningsvedlegget er ikke tilgjengelig i dataene som er samlet inn for denne rapporten. Det bør innhentes og gjennomgås før eventuell videre vurdering.

- **Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** TxGNN-kunnskapsgrafen (PrimeKG) inneholder kontraindikasjonskoblinger mellom dabigatran og følgende tilstander: blødningsforstyrrelse (koagulasjonssykdom), anemi, makrocytær anemi og intracerebral blødning. Dette er signaler fra en modell og må verifiseres mot preparatomtalen.
- **Spesifikk bekymring:** For prediksjonen «primær frigjøringsforstyrrelse av blodplater» er det en reell risiko for at en antikoagulant forverrer blødningstendensen.

Ingen legemiddelinteraksjoner ble funnet i spørringen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle prediksjonene er på evidensnivå L5 (kun modellprediksjon) uten kliniske studier eller litteratur som støtter effekt. I tillegg er alle norske/europeiske lisenser kansellert, og sikkerhetsdata fra pakningsvedlegget mangler.

**For å gå videre kreves følgende:**
- Hente og gjennomgå pakningsvedlegget (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Innhente data om virkningsmekanisme (f.eks. via DrugBank)
- Prekliniske studier som undersøker trombin/PAR-1-hemming ved kolestatisk fibrose og skleroserende kolangitt
- Avklare regulatorisk status, siden ingen lisenser er gyldige
- Vurdere blødningsrisiko hos pasienter med leversykdom og gallegangssykdom før eventuelle kliniske studier
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

