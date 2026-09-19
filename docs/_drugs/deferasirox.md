---
layout: default
title: Deferasirox
parent: Kun modellprediksjon (L5)
nav_order: 100
evidence_level: L5
indication_count: 5
---

# Deferasirox
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

# Deferasirox: Fra jernoverbelastningsbehandling til HIV-infeksjon prediksjon

## Enlinjesammendrag

Deferasirox er et oralt trivalent jernskjelator. Denne Evidence Pack gir ikke offisielle godkjente indikasjoner, men basert på eksisterende farmakologisk kunnskap brukes det klinisk til behandling av transfusjonsrelatert jernoverbelastning. TxGNN-modellen peker med sin høyest rangerte predikerte indikasjon mot **HIV-infeksjon**, og støttes for tiden bare av **2 publikasjoner** (mekanistisk in vitro-studie og narkotikanyhetsoversikt), **uten noen registrerte kliniske studier**, og bevisstyrken er svak.

---

## Hurtigoversikt

| Emne | Innhold |
|------|---------|
| Originale indikasjoner | Manglende data (`original_indications` ikke oppgitt, Norge Not marketed ingen autorisasjonsdata tilgjengelig) |
| Forutsagt ny indikasjon | HIV infectious disease |
| TxGNN forutsigelsesskår | 99.40% |
| Bevisnivå | L4 (mekanistisk/preklinisk forskningsnivå) |
| Markedsstatus for Norge | ✗ Not marketed |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor har denne prediksjonen rimelig grunnlag?

For tiden foreligger det ingen detaljert informasjon om virkningsmekanisme (MOA) (`original_moa` er merket som Data Gap). Basert på assosiativanalysen i Evidence Pack er Deferasirox et oralt trivalent jernskjelator hvis primære farmakologiske virkning er å redusere intracellulær fri jernkonsentrasjon, og det brukes klinisk oftest ved jernoverbelastningsrelaterte lidelser; denne mekanismen kan ha utvidet anvendelighet innen jernomsettings- og virusinteraksjonsfeltet.

Den mekanistiske hypotesen som støtter HIV-indikasjonspredikasjonen kommer fra en in vitro-studie: jernionkonsentrasjonen i endolysosomer påvirker graden av oligomerisering av HIV-1 Tat-protein, og dermed regulerer LTR-transkripsjonsaktivasjon (PMID 34550543). Denne hypotesen antyder at jernskjelering muligens indirekte kan hemme viral transkripsjonsaktivasjon, men dette er **en indirekte hypotese om jernomsettings-virusinteraksjon**, ikke en direkte antivirale mekanisme for legemidlet, og det foreligger ingen kliniske studier som bekrefter effektiviteten av denne veien hos mennesker.

Det skal også bemerkes at denne Evidence Pack samtidig viser 4 andre TxGNN-prediksjoner (kronisk HCV, sjelden nevrolig utviklingssykdom, utdatert familial blandet dyslipidemi, dermatofibrosarcoma protuberans), og bevisnivåene er for det meste L5 (ren modellprediksjon, uten litteratur eller klinisk støtte), og anbefalingstilstanden er alle Hold, så denne rapporten fokuserer på HIV-indikasjonssignalet med relativt fullstendigere bevis (rank 1).

---

## Bevis fra kliniske studier

For tiden ingen relevante registrerte kliniske studier

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|-----------|---------------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preklinisk mekanismestudium | Journal of Neurovirology | Jernionkonsentrasjonen i endolysosomer begrenser oligomerisering av HIV-1 Tat-protein og β-catenin-ekspresjon, og hemmer dermed Tat-formidlet HIV-1 LTR-transaktivasjon (in vitro mekanismestudium) |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Oversikt/Narkotikanyheter | Journal of the American Pharmacists Association | Er en narkotikanyhetesoversikt (dekker ramelteon, tipranavir, nepafenac, deferasirox), gir ikke spesifikke effektivitetsdata for deferasirox relatert til HIV |

---

## Markedsinformasjon for Norge

For tiden er Deferasirox markedsstatus i Norge «Not marketed», uten autorisasjonsdata som kan vises.

---

## Sikkerhetsvurderinger

Konsulter pakningsvedlegget for sikkerhetsinformasjon (advarsler, kontraindikasjoner og data om legemiddelinteraksjoner i denne Evidence Pack er alle merket som Data Gap, og DG001 er allerede klassifisert som et Blocking-nivå gap, som venter på offisielle pakningsvedlegg fra DMP-nettstedet).

---

## Konklusjon og videre anbefalinger

**Beslutning: Hold**

**Begrunnelse:**
Dagens bevis som støtter HIV-indikasjonen består bare av en enkelt in vitro mekanismestudium (L4), mangler all klinisk eller human verifikasjonsdata; samtidig er sikkerhetspakningsvedlegg data (advarsler, kontraindikasjoner) et Blocking-nivå gap (DG001). Før disse dataene fylles, kan ikke S1-sikkerhetsinitiell evaluering utføres, og det er ikke tilstrekkelig til å støtte inngang i neste utviklingsfase.

**Hvis du ønsker å gå videre, må du supplere:**
- TFDA-pakningsvedlegg advarsler og kontraindikasjonsdata (DG001, Blocking, må laste ned og analysere offisielt pakningsvedlegg PDF)
- Komplett virkningsmekanismedata (MOA) (DG002, High, kan suppleres gjennom DrugBank API-søk)
- In vivo-verifikasjonsstudier for hypotesen «jernskjelering-HIV Tat-transkripsjonregulering», eller i det minste etablering av preklinisk/tidlig fase klinisk forsøksplanlegging for denne indikasjonen
- Formelle søkeresultater for legemiddelinteraksjoner (DDI), for tiden i not_found-status

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

