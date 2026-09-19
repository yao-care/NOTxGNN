---
layout: default
title: Ponatinib
parent: Kun modellprediksjon (L5)
nav_order: 284
evidence_level: L5
indication_count: 2
---

# Ponatinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Ponatinib: Fra uavklart opprinnelig indikasjon til Gingival Fibromatose

## Sammendrag i én setning

> Ponatinibs opprinnelige godkjent indikasjon og virkningsmekanisme er ikke tilgjengelige i det nåværende datasettet (begge flagget som datahull).
> TxGNN-modellen predikerer at det kan være effektivt for **Gingival Fibromatose**,
> men denne prediksjonen støttes for tiden av **0 kliniske forsøk** og **0 publikasjoner** — bevisnivå L5 (kun modellpreduksjon).

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig (ingen lisens- eller indikasjonsdata i arkiv) |
| Predikert ny indikasjon | Fibromatose, gingival |
| TxGNN-prediksjonspoengsum | 99.04% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanisme-data for ponatinib ikke registrert (flagget som et høytsvært datahull). Imidlertid identifiserer bevissakens egen repurposing-rasjonale ponatinib som en multi-kinase-hemmer som retter seg mot BCR-ABL, FGFR, PDGFR, VEGFR, KIT og SRC — konsistent med dens kjente klasse som en tyrosin-kinase-hemmer.

Gingival fibromatose er mekanistisk knyttet til SOS1/PDGFR-signalering og fibroblast-overproliferasjon. Siden ponatinib hemmer PDGFR, finnes det et teoretisk grunnlag for å undertrykke fibroblast-proliferasjon. Imidlertid er denne koblingen avledet rent fra TxGNN-poengsum — det finnes ingen støttende mekanistisk litteratur, prekliniske data eller kliniske bevis, og fordi de opprinnelige indikasjonsdata mangler helt, kan det ikke trekkes noen troverdig farmakologisk analogi mellom de opprinnelige og predikerte indikasjonene.

Gitt det svært svake evidentiargrunnlaget (kun-score-preduksjon, TxGNN-rangering 9202 — langt utenfor typiske høykonfidens-områder), bør denne prediksjonen behandles som kun utforskende.

---

## Klinisk forsøksbevis

For tiden ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Ponatinib er for tiden **ikke markedsført** og har **0 godkjennelser**, så ingen lisens-/produkttabell er tilgjengelig.

---

## Cytotoksisitet

Ponatinibs repurposing-rasjonale identifiserer den som en multi-kinase-hemmer (BCR-ABL/FGFR/PDGFR/VEGFR/KIT/SRC), konsistent med en målrettet antineoplastisk terapi-klasse, så denne delen er inkludert for fullstendighet.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (multi-kinase-hemmer: BCR-ABL/FGFR/PDGFR/VEGFR/KIT/SRC) |
| Risiko for myelosuppresjon | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingselementer | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Vennligst se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Regulatory label-advarsler, kontraindikasjoner og DDI-data er for tiden et **blokkerende** datahull — se DG001.)

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Rasjonale:**
Den beste prediksjonen (gingival fibromatose) støttes kun av TxGNN-poengsum, uten kliniske forsøk eller litteratur (L5) og en lav prediksjonsrangering (9202), og både opprinnelig-indikasjon og MOA-data mangler — utilstrekkelig grunnlag for å gå videre. En sekundær kandidat i samme bevissakk, **liposarkom** (poengsum 99.00%, rangering 9484), har en preklinisk kinase-screeningpublikasjon (PMID [29132397](https://pubmed.ncbi.nlm.nih.gov/29132397/), L4) som antyder en teoretisk kinase-veioverlapning, men den tester ikke ponatinib direkte og er også vurdert til Hold.

**For å gå videre, er følgende nødvendig:**
- TFDA/label-advarsler og kontraindikasjoner for ponatinib (DG001, blokkering)
- Bekreftet virkningsmekanisme-data fra DrugBank (DG002)
- Opprinnelig indikasjon og regulatorisk historie for ponatinib
- Mekanistiske eller prekliniske studier som direkte tester ponatinib ved gingival fibromatose eller liposarkom
- Hvis liposarkom-signalet følges opp, målrettet validering av ponatinib (ikke generelle kinase-hemmere) mot liposarkom-cellelinjer

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

