---
layout: default
title: Givosiran
parent: Høy evidens (L1-L2)
nav_order: 161
evidence_level: L2
indication_count: 10
---

# Givosiran
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **10** stk.
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

# Givosiran: Fra akutt hepatisk porfyri til porfyri på grunn av ALA-dehydratase-mangel (ADP)

## Sammendrag i en setning

> Givosiran er et siRNA-terapeutikum som brukes ved akutt hepatisk porfyri (AHP), en gruppe arvelige forstyrrelser i hemesyntesen.
> Blant TxGNN-modellens prediksjoner viser kun **porfyri på grunn av ALA-dehydratase-mangel (ADP)** — en sjelden AHP-undertype — en genuin mekanistisk sammenheng og støttende kliniske/litteraturbevis;
> de ni andre høyest rangerte prediksjoner (hepatoportal sklerose, portalventrombose, hepatopulmonal syndrom, HBV/HCV-infeksjon, osv.) er flagget i selve evidenspakken som modellArtefakter som deler bare en "lever"-node, med **ingen mekanistisk grunnlag og null støttende studier**.

---

## Hurtig oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Akutt hepatisk porfyri (AHP) — utledet fra litteratur; ingen formell regulatorisk indiksjonstekst tilgjengelig |
| Predikert ny indikasjon | Porfyri på grunn av ALA-dehydratase-mangel (ADP) |
| TxGNN-prediksjonspoeng | 99.91% |
| Evidensnivå | L2 |
| Markedsstatus i Norge | Ikke på markedet |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Fortsett med beskyttelsestiltak |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme fra en formell kilde ikke tilgjengelige. Basert på litteraturbevisene som ble samlet, er givosiran et siRNA-terapeutikum som demper hepatisk **ALAS1** (5-aminolevulinsyre-syntase 1) mRNA, og reduserer hepatisk overproduksjon av de nevrotoksiske mellomproduktene **ALA** og **PBG**. Denne mekanismen er grunnlaget for godkjenningen ved akutt hepatisk porfyri (AHP), en familie av fire genetiske lidelser — inkludert akutt intermittent porfyri, arvelig koproporfi, variabel porfyri og **porfyri på grunn av ALA-dehydratase-mangel (ADP)** — som deler samme nedstrøms patologi av ALAS1-drevet ALA/PBG-akkumulering.

ADP er derfor ikke egentlig en "ny" indikasjon i biologisk forstand, men en ultra-sjelden undertype innenfor AHP-familien som givosarans mekanisme direkte rammer. Dette forklarer hvorfor denne kandidaten — ulikt modellens høyest rangerte resultater — har genuin mekanistisk og klinisk støtte (L2, fase 3 ENVISION-data, en ADP-spesifikk saksrapport).

**Viktig forbehold angående rangering:** de ni andre TxGNN-prediksjoner i denne evidenspakken (rangeringer 1–8 og 10, inkludert hepatoportal sklerose, portalventrombose, hepatopulmonal syndrom, HBV/HCV-infeksjon, fenylalaninmetabolismeforstyrrelser, osv.) ble eksplisitt annotert i kildedataene som å ha **ingen mekanistisk sammenheng** og **null klinisk forsøks- eller litteraturbevis** — de ser ut til å score høyt bare fordi de deler en "lever"-node med givosiran i kunnskapsgrafen. Alle ble vurdert L5/S0/Hold. Denne rapporten fokuserer derfor på den ene prediksjonen (ADP, rangering 9) som passerte en minimal plausibilitetskontroll; de høyere rangerte prediksjoner bør ikke forfølges uten uavhengig mekanistisk begrunnelse.

---

## Klinisk forsøksbevis

For tiden er det ingen relaterte kliniske forsøk registrert (fase 3-forsøket ENVISION for AHP bredt blir referert bare via post-hoc litteraturanalyse, ikke som en registrert forsøksjournal i denne evidenspakken).

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [36028858](https://pubmed.ncbi.nlm.nih.gov/36028858/) | 2022 | RCT (fase 3, ENVISION) | Orphanet J Rare Dis | Post-hoc-analyse av det placebokontrollerte ENVISION-forsøket som evaluerte sykdomsbyrde hos AHP-pasienter ≥12 år behandlet med givosiran |
| [40312531](https://pubmed.ncbi.nlm.nih.gov/40312531/) | 2025 | Kohorte/klinisk studie | Scientific Reports | Studie med utvidet tilgang hos 10 japanske AHP-pasienter som mottok månedlig SC givosiran 2,5 mg/kg; effektivitets- og sikkerhetdata |
| [35067977](https://pubmed.ncbi.nlm.nih.gov/35067977/) | 2022 | Kohorte (virkelig verden) | J Intern Med | RNAi-terapi med givosiran reduserer angrepshyppigheten betydelig ved akutt intermittent porfyri |
| [37027823](https://pubmed.ncbi.nlm.nih.gov/37027823/) | 2023 | Anmeldelse | Blood | Oversikt over RNA-interferensterapiens virkningsmekanisme (ALAS1-dempning) på tvers av de akutte hepatiske porfirier |
| [39313028](https://pubmed.ncbi.nlm.nih.gov/39313028/) | 2024 | Anmeldelse | Revista Clinica Espanola | Terapeutisk tilnærming til akutte kriser ved hepatiske porfirier, inkludert ALA-dehydratase-mangel undertype |
| [35734365](https://pubmed.ncbi.nlm.nih.gov/35734365/) | 2022 | Anmeldelse | Drug Des Devel Ther | Design, utvikling og terapeutisk plassering av givosiran hos voksen AHP |
| [36883675](https://pubmed.ncbi.nlm.nih.gov/36883675/) | 2023 | PK-PD-modellering | CPT: Pharmacometrics & Systems Pharmacology | PK-PD-modell av reduksjon av urinært ALA etter givosiran-behandling, samlet fase I-III-data |
| [35991568](https://pubmed.ncbi.nlm.nih.gov/35991568/) | 2022 | Saksrapport (ikke-respons) | Frontiers in Genetics | Rapporterer **manglende respons** på givosiran i et bekreftet ALAD-porfyri (ADP)-tilfelle — et viktig sikkerhets-/effektivitets-advarselssignal |

---

## Markedsinformasjon for Norge

Givosiran er for tiden **ikke på markedet i Norge** (0 godkjennelser på arkiv). Ingen produkt-, doseringsform- eller godkjent-indikasjondata er tilgjengelig for dette markedet.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og interaksjondata er for tiden ikke tilgjengelige i evidenspakken — dette er flagget som et **blokkerande** datakløft (DG001) som må løses før noen sikkerhetsgjennomgang kan fortsette.)

---

## Konklusjon og neste trinn

**Beslutning: Fortsett med beskyttelsestiltak**

**Begrunnelse:**
Givosarans kjernesekanisme (hepatisk ALAS1-dempning) er direkte relevant for ADP, og denne sammenhengen er støttet av fase 3 ENVISION sykdomsbyrde-data samt flere anmeldelser av ALAS1/ALA-PBG-banen. Imidlertid er ADP en ultra-sjelden AHP-undertype med praktisk talt ingen ADP-spesifikk forsøksdata, og den ene publiserte ADP-saksrapporten viser **ingen klinisk respons** på givosiran — så den mekanistiske begrunnelsen garanterer ikke effektivitet i denne undergruppen, og beskyttelsestiltak (f.eks. bruk på forsøksbasis med tett overvåking) er berettiget snarere enn en full "Gå".

Separat mangler de ni andre TxGNN-predikerte indikasjonene i denne evidenspakken mekanistisk og bevisbasert støtte og bør holdes (**Hold**) mens man venter på uavhengig validering — de blir ikke behandlet videre i denne rapporten.

**For å fortsette er følgende nødvendig:**
- TFDA/regulatorisk-kilde merkedata (viktige advarsler, kontraindikasjoner, DDI) — blokkerer for tiden (DG001)
- Formell MOA-dokumentasjon fra DrugBank eller tilsvarende primærkilde (DG002)
- ADP-undergruppespecifikk effektivitets-/sikkerhetdata utover saksrapporten med den eneste ikke-respondenten
- Status for markedsinngang i Norge og vurdering av regulatorisk godkjenningsvei, siden stoffet ikke er på markedet der for tiden
- En strukturert sikkerhetsovervåkingsplan dersom off-label eller utvidet tilgang i ADP vurderes

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

