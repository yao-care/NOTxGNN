---
layout: default
title: Susoctocog Alfa
parent: Moderat evidens (L3-L4)
nav_order: 334
evidence_level: L3
indication_count: 10
---

# Susoctocog Alfa
{: .fs-9 }

Evidensnivå: **L3** | Predikerte indikasjoner: **10** stk.
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

# Susoctocog alfa: Fra ervervet hemofili A til ervervet koagulasjonsfaktormangel

## Oppsummering i én setning

> Susoctocog alfa (rekombinant grisearts faktor VIII, markedsført andre steder som Obizur/OBIZER) er en etablert behandling for blødningsepisoder ved **ervervet hemofili A (AHA)** — en indikasjon bekreftet av den kliniske studien og litteraturbevisene i denne pakken, selv om den ikke er formelt registrert i de regulatoriske datafeltene her.
> TxGNN-modellen foreslår separat en utvidelse til det bredere sykdomskonseptet **ervervet koagulasjonsfaktormangel**, støttet av **1 klinisk studie** og **10+ relevante publikasjoner** som i stor grad beskriver legemidlets etablerte AHA-bruk.
> Dette legemidlet **er ikke for tiden markedsført i Norge**. Av de 10 sykdommene TxGNN totalt predikerte, har bare denne indikasjonen (og den nært beslektede "hemofili"-noden) reelt støttebevis — de øvrige 8 er flagget nedenfor som lavkonfidensielle, mekanistisk usupporterte prediksjoner.

---

## Hurtig oversikt

| Punkt | Innhold |
|------|--------|
| Originalindikasjon | Ikke registrert i regulatoriske data (datagap); kliniske/litteraturbevis i denne pakken identifiserer konsekvent **ervervet hemofili A** som legemidlets etablerte bruk |
| Predikert ny indikasjon | Ervervet koagulasjonsfaktormangel (bredere utvidelse av AHA-mekanismen) |
| TxGNN prediksjonspoengsum | 99.74% (hemofili-node, rang 4) / 99.64% (ervervet koagulasjonsfaktormangel, rang 5) |
| Bevisnivå | L3 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Fortsett med sikringsmekanismer |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte mekanisme-for-handling-data var ikke tilgjengelig i standardfeltet MOA for denne bevisepakken (datagap). Imidlertid beskriver den kliniske studien og litteraturbevisene konsekvent susoctocog alfa som en **rekombinant, B-domene-deletert grisearts faktor VIII-sekvens (rpFVIII)**. Det virker ved direkte å erstatte koagulasjonsfaktor VIII-aktivitet hos pasienter hvis endogene humane FVIII har blitt nøytralisert av autoantistoff — den definierende patologien ved ervervet hemofili A (AHA).

TxGNN-prediktert node "ervervet koagulasjonsfaktormangel" er mekanistisk koherent med legemidlets kjente virkning: det er i hovedsak samme patofysiologiske kategori som AHA (tap av en koagulasjonsfaktor på grunn av ervervede/autoimmune årsaker i stedet for genetisk mangel), og deler nesten all sin støttende litteratur med AHA/hemofili-noden. Dette forstås best som at TxGNN korrekt gjenvinner og generaliserer legemidlets kjente mekanisme, snarere enn å identifisere en virkelig ny biologisk vei.

I kontrast mangler legemidlets opprinnelige godkjente bruk (AHA) selv fra de strukturerte regulatoriske feltene i denne pakken — dette ser ut til å være et dataregistreringsgap snarere enn et genuint fravær av en godkjent indikasjon, siden den pivotale fase II/III-studien (NCT04580407, referert i PMID 39158833) og flere virkelighets­studier beskriver susoctocog alfa/Obizur som lisensiert spesifikt for blødningsepisoder hos voksne AHA-pasienter.

---

## Bevis fra klinisk studie

| Studie-nummer | Fase | Status | Antall deltakere | Viktige funn |
|---------|------|--------|----------|---------|
| [NCT06461533](https://clinicaltrials.gov/study/NCT06461533) | N/A (post-markedsføringsoversikt) | Rekrutterer | 25 | Japansk heldekkende overvåking av Susoctocog Alfa (OBIZER) IV-injeksjon for blødningshendelser ved ervervet hemofili A, overvåker bivirkninger og effektivitet i virkelig bruk |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|--------|---------|
| [27098420](https://pubmed.ncbi.nlm.nih.gov/27098420/) | 2016 | Gjennomgang | Drugs | Omfattende gjennomgang: susoctocog alfa (Obizur) effektiv og generelt godt tolerert for alvorlig blødning ved AHA i en multinasjonalt fase II/III-studie (n=28 evaluerbar) |
| [38066923](https://pubmed.ncbi.nlm.nih.gov/38066923/) | 2023 | Gjennomgang | Hematology Am Soc Hematol Educ Program | Diagnose- og laboratorieovervåkingstilnærming for AHA, inkludert FVIII-hemmer-vurdering |
| [39245591](https://pubmed.ncbi.nlm.nih.gov/39245591/) | 2024 | Gjennomgang | La Revue de médecine interne | 2024-oppdatering på AHA-patofysiologi, diagnose og hemostase-behandlingsalternativer inkludert rpFVIII |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Gjennomgang | Current Pharmaceutical Design | Perioperativ anestesihensyn for nye hemostase-midler, inkludert rekombinant grisearts FVIII |
| [39158833](https://pubmed.ncbi.nlm.nih.gov/39158833/) | 2024 | Fase II/III-kohorte | Int J Hematol | Japansk fase II/III åpen-label-studie (NCT04580407) som evaluerer effektivitet/sikkerhet for rpFVIII ved voksne AHA med alvorlig blødning |
| [32698943](https://pubmed.ncbi.nlm.nih.gov/32698943/) | 2020 | Retrospektiv kohorte | Blood Transfus | Største italienske multisentrale virkelighetsregister for rpFVIII hos 9 eldre AHA-pasienter, beskriver effektivitet og sikkerhet |
| [37584309](https://pubmed.ncbi.nlm.nih.gov/37584309/) | 2023 | Post-autorisasjon sikkerhet kohorte | Haemophilia | Ikke-intervensjons virkelighetsbasert sikkerhets- og effektivitetsstudie for rpFVIII ved AHA |
| [40812597](https://pubmed.ncbi.nlm.nih.gov/40812597/) | 2025 | Kohorte/PK | J Thromb Haemost | Farmakokinetiske strategier for presis FVIII-kontroll med susoctocog alfa-dosering ved AHA |
| [37799011](https://pubmed.ncbi.nlm.nih.gov/37799011/) | 2024 | Kohorte (lab-metoder) | Int J Lab Hematol | Enighet mellom ett-trinns og kromogene tester for overvåking av rpFVIII-aktivitet |
| [36010349](https://pubmed.ncbi.nlm.nih.gov/36010349/) | 2022 | Kohorte (lab-metoder) | Diagnostics | Analytisk ytelsessammenligning av laboratoriumsmetoder for måling av susoctocog-alfa-aktivitet |

---

## Andre TxGNN-predikterte indikasjoner (lav konfidens — avvent)

Utover AHA-relaterte funn ovenfor, har TxGNNs øvrige 8 topprangerte prediksjoner **ingen støttende kliniske studier eller litteratur** og ble eksplisitt flagget i kildebevisene som mekanistisk usupportert — modellen ser ut til å koble disse sykdommene via en generell "blødningstendens"-semantisk likhet snarere enn en spesifikk farmakologisk sammenheng:

| Sykdom | TxGNN-poeng | Hvorfor mekanismen ikke passer |
|--------|--------|---------|
| Primær frigjøringsforstyrrelser av blodplater | 99.94% | Patologi er blodplategranulumsutgift, ikke FVIII-mangel |
| Pseudo-von Willebrand-sykdom | 99.93% | Forårsaket av blodplatereseptor GPIb-abnormitet, ikke FVIII |
| Glanzmanns trombasteni | 99.88% | GPIIb/IIIa blodplattaggregasjonsdefekt, urelatert til FVIII |
| Scotts syndrom | 99.60% | Blodplattemembran scramblase-defekt, ikke FVIII |
| Blødningsdiates (kollagenreseptordefekt) | 99.17% | Blodplatteadhesjon (f.eks. GPVI)-defekt, ikke FVIII |
| Blødningsforstyrrelser (konstitusjonell trombocytopeni) | 99.17% | Blodplateantallmangel; FVIII-erstatning har ingen effekt |
| Medfødt faktor XIII-mangel | 99.15% | Mangel på en annen koagulasjonsfaktor (XIII, ikke VIII) |
| Adenosin deaminasemangel | 99.04% | Immunsvikt (SCID), ingen biologisk sammenheng til koagulasjon |

**Anbefaling for alle 8: Avvent** — ingen klinisk, mekanistisk eller litteraturbasis for å forfølge.

---

## Norsk markedsinformasjon

Susoctocog alfa **er ikke for tiden markedsført i Norge** (0 godkjennelser på record). Ingen lisens- eller doseringsformdata er tilgjengelig i denne pakken.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Viktige advarsler, kontraindikasjoner og legemiddelinteraksjondata var ikke tilgjengelig i denne bevisepakken — dette er flagget som et blokerande datagap, DG001, som krever innhenting av TFDA/regulatorisk produktinformasjon før noen sikkerhetsfase-beslutning.)*

---

## Konklusjon og neste steg

**Beslutning: Fortsett med sikringsmekanismer**

**Begrunnelse:**
Bare AHA/ervervet-koagulasjonsfaktormangel-signalet (ranger 4–5) er støttet av reelle kliniske og observasjonelle bevis (L3), og det er mekanistisk koherent med legemidlets kjente erstatnings­terapi-virkning — dette er i stor grad en bekreftelse/utvidelse av en allerede etablert bruk snarere enn en virkelig ny omformålshypotese. De andre 8 TxGNN top-score-prediksjoner mangler noe som helst støttende bevis og bør avventes.

**For å fortsette, kreves følgende:**
- Innhent offisiell TFDA/EMA/FDA-merking (Obizur/OBIZER) for å fylle det blokerande sikkerhetsdatagapet (DG001) — advarsler, kontraindikasjoner, legemiddelinteraksjoner
- Innhent DrugBank MOA-data (DG002) for formelt å dokumentere mekanisme
- Bekreft og registrer legemidlets faktiske opprinnelige godkjente indikasjon(er), som for tiden mangler fra regulatoriske felt
- Avklar Norges-spesifikk regulatorisk vei, siden produktet ikke er for tiden markedsført der
- Hvis man forfølger den bredere "ervervet koagulasjonsfaktormangel"-utvidelsen, søk etter sykdomsspesifikk sakdata utover AHA for å støtte den generaliseringen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

