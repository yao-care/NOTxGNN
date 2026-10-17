---
layout: default
title: Givosiran
parent: Kun modellprediksjon (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Givosiran: predikert ny indikasjon Hepatoportal sklerose (evidensnivå L5). Opprinnelig indikasjon: Hepatiske porfyrier"
monitor_inn: "GIVOSIRAN"
predicted_indications: ["hepatoportal sclerosis", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "chronic hepatitis C virus infection", "glycogen storage disease due to hepatic glycogen synthase deficiency", "chronic hepatitis B virus infection", "disorder of phenylalanine metabolism"]
---

# Givosiran
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Givosiran: Fra hepatiske porfyrier til hepatoportal sklerose

## Oppsummering i korte trekk

Givosiran er et siRNA-legemiddel som opprinnelig brukes mot hepatiske (akutte) porfyrier.
TxGNN-modellen forutsier at det kan ha effekt mot **hepatoportal sklerose**, med en svært høy modellscore.
Prediksjonen støttes foreløpig av **0 kliniske studier** og **0 publikasjoner**. Den er kun modellbasert (evidensnivå L5).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hepatiske porfyrier |
| Predikert ny indikasjon | Hepatoportal sklerose |
| TxGNN-prediksjonsscore | 99,999 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte tillatelser |
| Antall godkjenninger | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Givosiran er et siRNA som rettes mot ALAS1 i leverceller (hepatocytter). Det senker produksjonen av de nevrotoksiske heme-forstadiene ALA og PBG. Det er denne mekanismen som gjør legemidlet nyttig ved akutte hepatiske porfyrier. Detaljerte mekanismedata utover dette er ikke tilgjengelige i datagrunnlaget.

Hepatoportal sklerose er en tilstand med ikke-cirrotisk portal hypertensjon. Den kjennetegnes av vaskulære og fibrotiske endringer i leveren. Det er ikke påvist noen plausibel mekanistisk kobling mellom ALAS1-hemming og disse endringene. Den høye scoren skyldes mest sannsynlig at sykdommene ligger nær hverandre i kunnskapsgrafen (felles lever-relaterte naboer). Den bygger ikke på en mekanisme som givosiran faktisk påvirker.

Prediksjonen bør derfor regnes som en hypotese generert av modellen, uten støtte fra kliniske eller litterære data.

---

## Klinisk evidens

Foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig ingen relatert litteratur tilgjengelig for hepatoportal sklerose.

**Merk:** Blant de ti øverste prediksjonene er det bare én som har publisert litteratur, nemlig **porfyri som skyldes ALA-dehydratase-mangel (ADP)**. Dette er en ultrasjelden akutt hepatisk porfyri nær givosirans opprinnelige bruksområde. Evidensen er indirekte og blandet:
- Fase 3-studien ENVISION (hovedsakelig akutt intermittent porfyri) er omtalt i [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) og [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/).
- Et kasuistisk innslag beskriver manglende respons på givosiran ved ADP: [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/).
- En rapport fra 2026 beskriver en pasient som trengte hemming av både hepatisk og erytroid ALA-produksjon: [42443962](https://pubmed.ncbi.nlm.nih.gov/42443962/).

Dette tyder på at ALAS1-hemming i lever alene kan være utilstrekkelig hos enkelte pasienter. Denne indikasjonen er vurdert til L4 og forskningsspørsmål, ikke til selve rapportens hovedindikasjon.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004775 | Givlaari | Ikke oppgitt | Hepatiske porfyrier |

Tillatelsen er registrert som avregistrert, og det finnes ingen gyldige tillatelser i dataene.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Totalt 87 interaksjoner er registrert. Blant de 20 som er gjennomgått, er én klassifisert som **alvorlig (Major)**: **eliglustat**. De øvrige er **moderate**, blant annet:
  - amfotericin B (flere formuleringer)
  - aminoglykosider (kanamycin, neomycin, streptomycin) og vankomycin
  - 5-ASA-preparater (mesalazin, balsalazid, olsalazin, sulfasalazin)
  - alosetron, metoklopramid, naltrekson, eksenatid
  - fenfluramin, deksfenfluramin og koffein

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen (SPC/pakningsvedlegg).

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen for hepatoportal sklerose er rent modellbasert (L5), uten kliniske studier, uten litteratur og uten plausibel mekanistisk kobling til ALAS1-hemming. I tillegg er legemidlet kun registrert med avregistrert tillatelse i Norge.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalen for advarsler og kontraindikasjoner. Dette er en blokkerende datamangel for sikkerhetsscreening.
- Mer detaljerte mekanismedata for givosiran fra DrugBank.
- Prekliniske eller mekanistiske data som kan koble ALAS1-hemming til portal hypertensjon eller levervaskulær sykdom.
- Avklare gjeldende markedsstatus og tilgjengelighet i Norge.
- Vurdere å prioritere ADP-porfyri som et mer forankret forskningsspørsmål, med oppmerksomhet på manglende respons i enkelte tilfeller.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

