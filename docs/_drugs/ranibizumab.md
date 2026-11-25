---
layout: default
title: Ranibizumab
parent: Kun modellprediksjon (L5)
nav_order: 346
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-25
monitor_inn: "RANIBIZUMAB"
predicted_indications: ["immature cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "tetanic cataract", "craniostenosis cataract", "nuclear senile cataract", "cortical cataract", "senile cataract", "hemorrhagic disease of newborn"]
description: "Ranibizumab: predikert ny indikasjon Immature cataract (evidensnivå L5). Opprinnelig indikasjon: Wet Macular Degeneration"
---

# Ranibizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

## Ranibizumab: Immature cataract
{: .text-alpha }

## Oppsummering i én setning

Ranibizumab er en VEGF-hemmende antistoffragment-behandling som opprinnelig brukes mot øyesykdommer som våt aldersrelatert makuladegenerasjon, makulaødem og koroidal neovaskularisering.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **alvorlig ikke-proliferativ diabetisk retinopati**.
Dette støttes av **19 publikasjoner** (blant annet RCT-baserte analyser fra RIDE/RISE og PAVILION-studien), men **ingen registrerte kliniske studier** i de innsamlede dataene.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Wet Macular Degeneration;Macular Edema;Choroidal Neovascularization;Diabetes Complications; Wet Macular Degeneration;Macular Edema;Diabetic Retinopathy;Diabetes Complications; Wet Macular Degeneration;Macular Edema;Diabetic Retinopathy;Diabetes Complications;Retinal Vein Occlusion;Choroidal Neovascu |
| Predikert ny indikasjon | Immature cataract |
| TxGNN-prediksjonsscore | 0.9999 |
| Evidensnivå | L5 (bør verifiseres mot fullstendige publikasjoner, se under) |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 10 av 10) |
| Antall godkjenninger | 10 (gyldige: 10) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med sikkerhetstiltak) |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Ranibizumab (uoffisiell oversettelse): «Ranibizumabpreparater bindes til reseptorbindingsstedet på aktive former av VEGF-A, inkludert den biologisk aktive, spaltede formen av dette molekylet, VEGF110. VEGF-A har vist seg å forårsake neovaskularisering og lekkasje i modeller for okulær angiogenese og vaskulær okklusjon, og antas å bidra til patofysiologien ved neovaskulær AMD, mCNV, DR, DME og makulaødem etter RVO.» Engelsk originaltekst: "Ranibizumab products bind to the receptor binding site of active forms of VEGF-A, including the biologically active, cleaved form of this molecule, VEGF110. VEGF-A has been shown to cause neovascularization and leakage in models of ocular angiogenesis and vascular occlusion and is thought to contribute to pathophysiology of neovascular AMD, mCNV, DR, DME and macular edema following RVO." ([DailyMed: Nufymco (ranibizumab-leyk) prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=05ed75bc-ae21-480b-9be4-cbc51689dd8a), versjon av 2026-11-05; hentet 2026-11-19). Ranibizumab er likevel kjent som et anti-VEGF-antistoffragment. VEGF driver lekkasje fra retinale blodkar og nydannelse av kar ved diabetisk retinopati, og VEGF-nivåene i glasslegeme og serum er forhøyet hos pasienter med sykdommen (PMID 36580154).

Ved å nøytralisere VEGF reduseres karpermeabiliteten, og alvorlighetsgraden av retinopatien kan gå tilbake. Dette er en direkte mekanisme på samme sykdomsvei som legemidlets opprinnelige indikasjoner, som makulaødem og diabetisk retinopati.

Det er viktig å merke seg at evidensnivå L1 bygger på titler i litteraturen som viser til fase 3-studiene RIDE/RISE, Protocol I og PAVILION. Selve studiedataene var ikke tilgjengelige, så graderingen må bekreftes mot fullstendige publikasjoner.

---

## Evidens fra kliniske studier

For den predikerte indikasjonen (alvorlig ikke-proliferativ diabetisk retinopati) er det for øyeblikket ingen relaterte kliniske studier registrert i de innsamlede dataene.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmol | PAVILION: portleveringssystem med ranibizumab vs. overvåking ved ikke-proliferativ diabetisk retinopati uten makulaødem |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Metaanalyse (post-hoc av fase 3) | Ophthalmol Retina | Sammenheng mellom baseline-alvorlighetsgrad av retinopati og tid til oppløsning av diabetisk makulaødem |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT post-hoc | Clin Ophthalmol | Prediktorer for tidlig regresjon av diabetisk retinopati i RIDE/RISE |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | RCT-forlengelse | BMJ Open Ophthalmol | Endring i DRSS-skår med mindre hyppig ranibizumab i RIDE/RISE |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT sekundæranalyse | JAMA Ophthalmol | Endring i retinopati over 2 år: aflibercept, bevacizumab og ranibizumab |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT-oppfølging | Retina | DRCR.net Protocol I, 5-årsrapport: endring i alvorlighetsgrad av retinopati |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Oversikt | Expert Opin Biol Ther | Ranibizumab ved diabetisk retinopati |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematisk oversikt og økonomisk analyse | Health Technol Assess | Anti-VEGF sammenlignet med laserfotokoagulasjon ved diabetisk retinopati |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Systematisk oversikt og metaanalyse | Health Technol Assess | Anti-VEGF vs. laser ved diabetisk retinopati |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Systematisk oversikt og metaanalyse | Eur J Pharmacol | Vedvarende ranibizumab-portlevering ved diabetisk retinopati og makulaødem |

---

## Markedsinformasjon for Norge

Godkjenningene i dataene er gyldige. Dosjeringsform er ikke oppgitt i dataene.

<!-- review:begin no-lic-20261112-ranibizumab-1 -->

> **Kontrollrettelse (2026-11-25)**: Opprinnelig sto det: «Alle syv godkjenningene er registrert som opphørt.» Rettet: ifølge EMAs data om sentrale EU-godkjenninger er godkjenningene gyldige (2026-11-25; også de nye godkjenningene Susvimo, Rexatilux og Vislyfa). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261112-ranibizumab-1 -->

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000715 | Lucentis | ranibizumab | Wet Macular Degeneration; Macular Edema; Diabetes Complications; Myopia, Degenerative; Choroidal Neovasculari… | Gyldig |
| EMEA/H/C/005019 | Ranivisio | ranibizumab | Wet Macular Degeneration; Macular Edema; Diabetic Retinopathy; Diabetes Complications | Gyldig |
| EMEA/H/C/005545 | Byooviz | ranibizumab | Wet Macular Degeneration; Macular Edema; Diabetic Retinopathy; Myopia, Degenerative | Gyldig |
| EMEA/H/C/005617 | Ximluci | ranibizumab | Wet Macular Degeneration; Macular Edema; Diabetic Retinopathy; Diabetes Complications | Gyldig |
| EMEA/H/C/006055 | Rimmyrah | ranibizumab | Wet Macular Degeneration; Macular Edema; Diabetes Complications; Myopia, Degenerative; Choroidal Neovasculari… | Gyldig |
| EMEA/H/C/006502 | Ranluspec | ranibizumab | Wet Macular Degeneration; Macular Edema; Diabetic Retinopathy; Diabetes Complications; Retinal Vein Occlusion… | Gyldig |
| EMEA/H/C/006527 | Susvimo | ranibizumab | Wet Macular Degeneration | Gyldig |
| EMEA/H/C/006528 | Epruvy (previously Ranibizumab Midas) | ranibizumab | Wet Macular Degeneration; Macular Edema; Choroidal Neovascularization; Diabetes Complications | Gyldig |
| EMEA/H/C/006634 | Rexatilux | ranibizumab | Wet Macular Degeneration | Gyldig |
| EMEA/H/C/006926 | Vislyfa | ranibizumab | Wet Macular Degeneration; Macular Edema; Diabetes Complications; Retinal Vein Occlusion; Choroidal Neovascula… | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (ikke preparatomtale):** Kunnskapsgrafen (PrimeKG) peker på øyeinfeksjoner og konjunktivitt som sykdommer der legemidlet er kontraindisert.
- **Legemiddelinteraksjoner:** Ingen interaksjoner funnet i dataene.

Vær oppmerksom på at advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med sikkerhetstiltak)**

**Begrunnelse:**
Mekanismen er direkte og biologisk plausibel, og litteraturen omfatter RCT-baserte analyser (RIDE/RISE, Protocol I, PAVILION) som støtter bruk ved diabetisk retinopati. Samtidig er det ingen registrerte studier i dataene, evidensgraderingen bygger på titler.

<!-- review:begin no-lic-20261112-ranibizumab-2 -->

> **Kontrollrettelse (2026-11-12)**: Opprinnelig sto det: «evidensgraderingen bygger på titler, og alle norske godkjenninger er opphørt.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-09). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261112-ranibizumab-2 -->

**For å gå videre kreves:**
- Verifisere L1-graderingen mot fullstendige publikasjoner for RIDE/RISE, Protocol I og PAVILION
- Hente advarsler og kontraindikasjoner fra preparatomtalen (sikkerhetsgjennomgangen kan ikke fullføres uten dette)
- Hente detaljerte data om virkningsmekanisme fra legemiddeldatabasen
- Vurdere administrasjonsvei (intravitreal injeksjon eller portleveringssystem)

<!-- review:begin no-lic-20261112-ranibizumab-3 -->

> **Kontrollrettelse (2026-11-12)**: Opprinnelig sto det: «Hente detaljerte data om virkningsmekanisme fra legemiddeldatabasen / Avklare regulatorisk status i Norge, siden alle godkjenninger er opphørt» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-09). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261112-ranibizumab-3 -->

---

## Andre predikerte indikasjoner (ikke anbefalt)

Alle øvrige prediksjoner har svak eller indirekte evidens og får beslutningen **Hold**:

| Predikert indikasjon | Score | Evidensnivå | Vurdering |
|------|------|------|------|
| Umoden katarakt | 0,9999 | L5 | Kun modellprediksjon, ingen studier eller litteratur |
| Moden katarakt | 0,9999 | L5 | Litteraturen gjelder kombinert kataraktkirurgi og injeksjon, ikke effekt på katarakt |
| Type 2-diabetesassosiert katarakt | 0,9999 | L5 | Litteraturen gjelder diabetisk makulaødem, ikke katarakt |
| Tetanisk katarakt | 0,9999 | L5 | Kun modellprediksjon, årsaken (hypokalsemi) påvirkes ikke av VEGF-hemming |
| Kraniostenose-katarakt | 0,9999 | L5 | Kun modellprediksjon |
| Nukleær senil katarakt | 0,9999 | L5 | Kun modellprediksjon |
| Kortikal katarakt | 0,9999 | L5 | Indirekte litteratur, inkludert en case-rapport om bivirkning (kapselblokk-syndrom) |
| Senil katarakt | 0,9999 | L5 | Biomarkørstudier av netthinnesykdom, ikke effekt på katarakt |
| Hemoragisk sykdom hos nyfødte | 0,9987 | L5 | Skyldes vitamin K-mangel; de to studiene gjelder andre sykdommer (HHT-studien trukket tilbake, 0 inkluderte) |

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-25 | Rettet: «registrert som opphørt» → «gyldige» (uten antall) | Rettet (revidert 2026-11-25; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-12 | Fjernet: «og alle norske godkjenninger er opphørt» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-12 | Fjernet: «Avklare regulatorisk status i Norge, siden alle godkjenninger er opphørt» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Nufymco (ranibizumab-leyk) prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=05ed75bc-ae21-480b-9be4-cbc51689dd8a) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

