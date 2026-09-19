---
layout: default
title: Dibotermin Alfa
parent: Kun modellprediksjon (L5)
nav_order: 108
evidence_level: L5
indication_count: 9
---

# Dibotermin Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

# Dibotermin alfa: fra beinregenering til esotropi

## Sammendrag i en setning

> Dibotermin alfa er et rekombinant humant BMP-2 som brukes til å fremme beininduksjon og beinregenering (f.eks. spinalfusjon, reparasjon av tibiafrakstur).
> TxGNN-modellen forutsier at det kan være effektivt for **esotropi**,
> men denne prediksjonen støttes foreløpig av **0 kliniske forsøk** og **0 publikasjoner**, og ingen plausibel mekanistisk vei har blitt identifisert.

---

## Rask oversikt

| Punkt | Innhold |
|------|------|
| Originalindikasjon | Ikke tilgjengelig fra norske regulatoriske data (legemiddel ikke markedsført); ifølge evidenskonteksten, historisk brukt for beininduksjon/beinregenering (spinalfusjon, reparasjon av tibiafrakstur) |
| Predikert ny indikasjon | Esotropi |
| TxGNN-prediksjonspoeng | 99.97% |
| Evidensnivå | L5 (kun modellprediksjon, ingen klinisk eller litteraturstøtte) |
| Markedsstatus i Norge | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Vent |

---

## Hvorfor er denne prediksjonen rimelig?

Foreløpig er detaljerte data om virkningsmekanisme ikke tilgjengelige (`original_moa: [Data Gap]`). Basert på den begrensede informasjonen som er tilgjengelig i evidenspakken, er dibotermin alfa et rekombinant humant benmorfoprotein-2 (BMP-2), og dets kjente kliniske bruk er relatert til beininduksjon og beinregenering — for eksempel spinalfusjon og reparasjon av tibiafrakstur.

Esotropi er en form for strabismus forårsaket av ekstraokular muskel/neuromuskulær ubalanse, en tilstand som mekanistisk ikke er relatert til osteoinduksjon. Evidenspakkens egen begrunnelse slår eksplisitt fast at det **ikke er noen kjent mekanistisk sammenheng** mellom BMP-2-signalisering og esotropi, og ingen eksperimentell eller klinisk evidens støtter denne forbindelsen.

Gitt fraværet av både mekanistisk begrunnelse og empirisk evidens, bør denne prediksjonen behandles som rent modelllartefakt heller enn som en biologisk fundert repurposinghypotese. Den samme merknaden gjelder flere andre TxGNN-rangerte indikasjoner for dette legemiddelet (f.eks. brystkreftsubtypinger), der den underliggende BMP-2 tumorbiologi-litteraturen — der den i det hele tatt finnes — peker mot tumorfremmende heller enn terapeutiske effekter.

---

## Kliniske forsøksbevis

Foreløpig ingen relaterte kliniske forsøk registrert

---

## Litteraturbevis

Foreløpig ingen relatert litteratur tilgjengelig

*Merknad: En lavere rangert kandidat (brysttumortyper luminal A/B, rang 5) ga 19 «samsvarende» PMIDer, men alle ble bekreftet å være databasenøkkelordmismatches (B-celleimmunologi, hepatitt B-vaksinerer, HLA-B-serotypering) som ikke er relatert til verken legemiddelet eller sykdommen, og er ekskludert som støy.*

---

## Markedsinformasjon for Norge

Dibotermin alfa har foreløpig ingen markedsgodkjenning i Norge (0 lisenser); ingen produkttekst eller godkjent indikasjonsinformasjon er tilgjengelig.

---

## Sikkerhetshensyn

Se pakningsinformasjonen for sikkerhetsinformasjon.

*(Merknad: TFDA/Norge pakningsinformasjonsadvarsler og kontraindikasjoner er flagget som en **blokkerende** datagap — nødvendig før noen sikkerhetstrinns-evaluering (S1) kan gjennomføres.)*

---

## Konklusjon og neste trinn

**Beslutning: Vent**

**Begrunnelse:**
TxGNN-poengene er høye, men det er ingen støtte fra kliniske forsøk eller litteratur, ingen sammenhengende mekanistisk forbindelse mellom BMP-2-osteoinduksjon og esotropi (en neuromuskulær tilstand), og legemiddelet er foreløpig ikke markedsført i Norge. Denne kombinasjonen plasserer kandidaten på det laveste evidensnivået (L5) uten grunnlag for å gå videre.

**For å fortsette, trengs følgende:**
- TFDA/Norge pakningsinformasjonsadvarsler og kontraindikasjoner (foreløpig blokkerende datagap, DG001)
- Bekreftet virkningsmekanismedata fra DrugBank eller primærlitteratur (DG002)
- Eventuell preklinisk eller kasusistisk evidens som spesifikt knytter BMP-2-signalisering til ekstraokular muskel/neuromuskulær funksjon
- Fornyet screening av de øvrige TxGNN-rangerte kandidatene (f.eks. brystkreftsubtypinger) for genuin litteraturstøtte, ettersom automatiserte treff viste seg å inkludere falske positiver

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

