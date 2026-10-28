---
layout: default
title: Durvalumab
parent: Kun modellprediksjon (L5)
nav_order: 136
evidence_level: L5
indication_count: 6
monitor_inn: "DURVALUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-28
description: "Durvalumab: predikert ny indikasjon Adenokarsinom i livmorligamentet (evidensnivå L5). Opprinnelig indikasjon: Ikke-småcellet lungekreft"
---

# Durvalumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

## Durvalumab: Fra ikke-småcellet lungekreft til adenokarsinom i livmorligamentet
{: .text-alpha }

## Oppsummering i én setning

Durvalumab er et PD-L1-hemmende legemiddel som er godkjent for ikke-småcellet lungekreft.
TxGNN-modellen forutsier at det kan ha effekt ved **endocervikalt karsinom** (høyest rangerte kandidat med data; den øverste rangerte kandidaten, livmorbåndets adenokarsinom, har ingen støttende data),
men foreløpig finnes bare **1 klinisk studie** (fase 1, 20 pasienter) og **2 publikasjoner** som ikke direkte viser effekt ved denne sykdommen.

> Merknad: Rapporten er basert på de samlede dataene for denne kandidaten. Den første forutsagte indikasjonen (rang 1) er «uterine ligament adenocarcinoma» uten noen studier eller litteratur. Tabellene under viser derfor først rang 1, og deretter rang 2 som har data.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke-småcellet lungekreft |
| Forutsagt ny indikasjon | Livmorbåndets adenokarsinom (rang 1); endocervikalt karsinom (rang 2, med data) |
| TxGNN-prediksjonsscore | 0,9992 (rang 1); 0,9991 (rang 2) |
| Evidensnivå | L5 (rang 1); L5 for endocervikalt karsinom (se vurdering under) |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold (vent) |

Evidensnivået for rang 2 er satt til L5, fordi ingen av de siterte studiene viser effekt direkte ved endocervikalt karsinom: fase 1-studien gjelder blandet livmorhals-, skjede- og vulvakreft i kombinasjon med stråling og tremelimumab, og publikasjonene gjelder nevroendokrin livmorhalskreft (oversikt) og blandede solide svulster.

## Hvorfor er denne prediksjonen rimelig?

Det finnes foreløpig ingen detaljerte data om virkningsmekanismen i de samlede dataene. Durvalumab er kjent som en PD-L1-hemmer (immunsjekkpunkthemmer), og effekten ved ikke-småcellet lungekreft er etablert. Mekanistisk kan blokkering av PD-1/PD-L1-aksen være aktuell ved livmorhalskreft, der PD-L1-uttrykk og HPV-drevet immunogenisitet er vanlig.

For de øvrige kandidatene (livmorbåndets adenokarsinom, adenoid cystisk karsinom i livmorhalsen, serøst adenokarsinom i livmorbåndet og sjeldne mucinøse adenokarsinomvarianter i livmorhalsen) finnes ingen studier eller litteratur. Høye scorer skyldes trolig nærhet i sykdomsontologien til livmorhalskreft heller enn spesifikke data. Koblingen til PD-L1-hemming er spekulativ.

## Klinisk studiedokumentasjon

For rang 1 (livmorbåndets adenokarsinom): Foreløpig er ingen relaterte kliniske studier registrert.

For rang 2 (endocervikalt karsinom):

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Fase 1 | Fullført | 20 | Hypofraksjonert strålebehandling kombinert med durvalumab og tremelimumab ved tilbakevendende/metastatisk livmorhals-, skjede- eller vulvakreft. Gir sikkerhets- og gjennomførbarhetssignaler, men ingen effektkonklusjoner i tilgjengelige data. |

## Litteraturdokumentasjon

For rang 1: Foreløpig er ingen relatert litteratur tilgjengelig.

For rang 2 (endocervikalt karsinom):

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Oversiktsartikkel | Biomedical Journal | Småcellet nevroendokrint karsinom i livmorhalsen: molekylært grunnlag og behandlingsutvikling. Data begrenset til kasuistikker og serier. |
| [42518016](https://pubmed.ncbi.nlm.nih.gov/42518016/) | 2026 | Ikke-randomisert klinisk studie (fase 1) | Oncology and Therapy | Ceralasertib pluss durvalumab hos kinesiske pasienter med avanserte solide svulster; sikkerhet, farmakokinetikk og antitumoraktivitet. Ikke spesifikk for livmorhalskreft. |

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004771 | Imfinzi | – | Ikke-småcellet lungekreft |

Dataene viser én gyldig godkjenning for enkeltstoffet (produsent: AstraZeneca AB).

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Immunterapi (PD-L1-hemmende monoklonalt antistoff), ikke konvensjonell cytostatika |
| Myelosuppresjonsrisiko | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forsiktighetsregler |

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: 81 interaksjoner er registrert. Blant de viktigste:
  - **Alvorlig (Major)**: adalimumab.
  - **Moderat**: kortikosteroider (hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednisolon, prednison, metylprednisolon, deflazakort), roflumilast, alefacept, alemtuzumab, anakinra, stivkrampetoksoid-vaksine og miltbrannvaksine.
  - **Mindre (Minor)**: sinkpreparater (acetat, glukonat, sulfat, klorid).

For øvrig sikkerhetsinformasjon, se pakningsvedlegget.

## Konklusjon og neste steg

**Beslutning: Hold (vent)**

**Begrunnelse:**
Prediksjonen for rang 1 og de fleste øvrige kandidatene mangler enhver støttende studie eller litteratur (L5). For endocervikalt karsinom finnes bare en liten fase 1-studie uten effektdata, og ingen studie som direkte viser effekt ved sykdommen, så evidensnivået forblir L5. Det er ikke grunnlag for å gå videre til klinisk bruk.

**For å gå videre kreves følgende:**
- Effektdata fra fase 2/3-studier spesifikt ved endocervikalt karsinom (eller den aktuelle histologien)
- Resultater fra fase 1-studien NCT03452332
- Data om virkningsmekanisme (MOA) og analyse av mekanistisk kobling
- Gjennomgang av pakningsvedleggets advarsler og kontraindikasjoner (mangler i de samlede dataene og er et blokkerende datagap)
- Vurdering av administrasjonsvei og sykdomsspesifikk sikkerhetsplan
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

