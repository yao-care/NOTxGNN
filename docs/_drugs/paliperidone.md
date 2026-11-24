---
layout: default
title: Paliperidone
parent: Kun modellprediksjon (L5)
nav_order: 306
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Paliperidone: predikert ny indikasjon Retinal dystrofi med eller uten ekstraokulære anomalier (evidensnivå L5). Opprinnelig indikasjon: Schizofreni"
monitor_inn: "PALIPERIDONE"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "syndromic myopia", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia 26, X-linked, female-limited", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "atypical glycine encephalopathy"]
---

# Paliperidone
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

## Paliperidon: Fra schizofreni til retinal dystrofi med eller uten ekstraokulære avvik
{: .text-alpha }

## Oppsummering i én setning

Paliperidon er et antipsykotikum som opprinnelig brukes mot schizofreni og psykotiske lidelser. TxGNN-modellen rangerer **retinal dystrofi med eller uten ekstraokulære anomalier** øverst (score 0,9992), men denne prediksjonen har verken kliniske studier eller litteratur bak seg. Den eneste prediksjonen med noe evidens er **behandlingsresistent schizofreni** (3 kliniske studier og 2 oversiktsartikler), men det ligger tett opptil den opprinnelige indikasjonen og er ikke egentlig drug repurposing.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Schizofreni; psykotiske lidelser |
| Predikert ny indikasjon (høyest rangert) | Retinal dystrofi med eller uten ekstraokulære anomalier |
| TxGNN-prediksjonsscore | 0.9992 |
| Evidensnivå | L5 (kun modellprediksjon) |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

<!-- review:begin no-lic-20261124b-paliperidone-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Antall markedsføringstillatelser / 1 (kansellert)» Fjernet: raden gjentok antallet godkjenninger med status «kansellert», noe som ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); antall og status står i raden «Antall godkjenninger» og i lisenstabellen. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-paliperidone-1 -->

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Paliperidone (uoffisiell oversettelse): «Paliperidon er den viktigste aktive metabolitten av risperidon. Virkningsmekanismen til paliperidon ved schizofreni er uklar. Den terapeutiske effekten ved schizofreni kan imidlertid medieres gjennom en kombinasjon av antagonisme av sentrale dopamin type 2 (D 2)- og serotonin type 2 (5HT 2A)-reseptorer.» Engelsk originaltekst: "Paliperidone is the major active metabolite of risperidone. The mechanism of action of paliperidone in schizophrenia is unclear. However, the drug's therapeutic effect in schizophrenia could be mediated through a combination of central dopamine Type 2 (D 2 ) and serotonin Type 2 (5HT 2A ) receptor antagonism." ([DailyMed: Invega (paliperidone) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7b8e5b26-b9e4-4704-921b-3c3c0d159916), versjon av 2025-01-31; hentet 2026-11-19). Basert på kjent informasjon er paliperidon (9-hydroksyrisperidon, den aktive metabolitten til risperidon) en D2- og 5-HT2A-antagonist, og effekten ved schizofreni er etablert.

**Toppredikasjonen (retinal dystrofi):** Det finnes ingen troverdig mekanistisk sammenheng. Paliperidon har ingen kjent rolle i signalveier ved arvelig netthinnesykdom. Den høye scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

**Øvrige topprangerte prediksjoner:** Flere av dem gjelder X-bundet og syndromisk nærsynthet, hydranencefali, glykosyleringsdefekter, kortikale misdannelser, Charcot-Marie-Tooth type 1G og atypisk glycinencefalopati. Ingen har studier eller litteratur, og ingen har en plausibel mekanisme:
- Ved nærsynthet er dopaminagonisme, ikke antagonisme, den teoretiske sammenhengen. Retningen er dermed trolig motsatt.
- Strukturelle hjernemisdannelser og metabolske defekter kan ikke korrigeres av reseptorantagonisme.
- Atypisk glycinencefalopati har en løs konseptuell kobling til glycin/NMDA-modulering ved schizofreni, men paliperidon påvirker ikke glycinmetabolismen.

**Behandlingsresistent schizofreni:** Dette er en utvidelse innenfor den eksisterende indikasjonen. Standardbehandlingen er klozapin, og evidensen for paliperidon i denne gruppen er indirekte.

---

## Klinisk studieevidens

Studiene gjelder predikasjonen «behandlingsresistent schizofreni». Ingen kliniske studier er registrert for toppredikasjonen.

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Fase 4 | Aktiv, rekrutterer ikke | 84 | Farmakoterapi kombinert med recovery-orienterte programmer ved behandlingsresistent schizofreni og bipolar lidelse. Uklart om paliperidon er en studert arm. |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Fase 4 | Ukjent | 244 | Åpen, randomisert studie som sammenligner aripiprazol og paliperidon/risperidon ved første psykoseepisode (SchizOMICS, multi-omics). Paliperidon trolig komparator, så evidensen er indirekte. |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Fase 4 | Avsluttet i utide | 5 | Eksplorerende studie av immun- og inflammasjonsrespons ved klozapin versus ikke-klozapin antipsykotika. Kun 5 deltakere, så i praksis ingen brukbar effektevidens. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Oversiktsartikkel | Actas Españolas de Psiquiatría | Gjennomgang av psykofarmakologi ved schizoaffektiv lidelse. Behandlingen bygger hovedsakelig på antipsykotika, uten spesifikke retningslinjer. |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Oversiktsartikkel | Current Opinion in Psychiatry | Effekt og toleranse av psykososiale og psykofarmakologiske intervensjoner ved tidlig debuterende schizofreni hos ungdom. |

Ingen litteratur er funnet for toppredikasjonene.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000746 | Invega | paliperidone | Schizophrenia; Psychotic Disorders | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Legemidlet er markedsført, og 1 av 1 tillatelser er gyldig.

---

## Sikkerhetsvurderinger

Pakningsvedlegg med advarsler og kontraindikasjoner mangler i dataene, så det må innhentes før sikkerhetsvurdering.

**Kontraindikasjoner/risikotilstander fra kunnskapsgrafen (ikke fra preparatomtale):** Tilstander knyttet til paliperidon i TxGNN-kunnskapsgrafen inkluderer:
- Hjerte og kar: langt QT-syndrom (inkludert familiært), torsades de pointes, ortostatisk hypotensjon, POTS, hypotensive tilstander, hjerteinfarkt og koronar trombose
- Nevrologi: epilepsi, basalgangliesykdom, fokal håndstonia, blefarospasme, multisystematrofi
- Stoffskifte og endokrinologi: hyperglykemi, diabetes mellitus, diabetisk ketoacidose, hyperlipidemi (inkludert familiær), fedme (inkludert monogen), kaliummangel
- Blod: nøytropeni, agranulocytose, hemoglobinopati
- Andre: Crohns sykdom og inflammatorisk tarmsykdom, brystkreft hos kvinner, nedsatt nyrefunksjon

**Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert. De 20 første som er vist i dataene, omfatter:
- **Alvorlige (Major):** bupropion og morfin
- **Moderate:** antidiabetika (acarbose, alogliptin, metformin, pioglitazon, kanagliflozin, klorpropamid, albiglutid), antikolinerge midler (atropin, hyoscyamin, glykopyrronium), famotidin, epinefrin, hydrokortison, amfotericin B, loperamid, lorkaserin og bisakodyl

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
- Toppredikasjonene er rene modellprediksjoner (L5) uten kliniske studier, litteratur eller plausibel mekanisme. Behandlingsresistent schizofreni har noe støtte (L4), men er en utvidelse av den eksisterende indikasjonen med kun indirekte fase 4-evidens, og klozapin er standard behandling.
- Kritiske sikkerhetsdata mangler.

<!-- review:begin no-lic-20261124b-paliperidone-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Den eneste norske tillatelsen er kansellert, og kritiske sikkerhetsdata mangler.» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-paliperidone-2 -->

**For å gå videre kreves følgende:**
- Hente pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel)
- Hente data om virkningsmekanisme fra DrugBank
- For behandlingsresistent schizofreni: avklare om paliperidon er en studert arm i NCT07047651 og NCT06060886, og vurdere direkte komparative studier mot klozapin
- Avklare om preparater med paliperidon er tilgjengelige i Norge
- Vurdere om de høyest rangerte prediksjonene (netthinnesykdom, nærsynthet m.fl.) skal forkastes som grafartefakter, med mindre ny mekanistisk støtte fremkommer

<!-- review:begin no-lic-20261124b-paliperidone-3 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklare hvorfor markedsføringstillatelsen er kansellert og om preparater med paliperidon er tilgjengelige i Norge» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-paliperidone-3 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Invega (paliperidone) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7b8e5b26-b9e4-4704-921b-3c3c0d159916) |
| 2026-11-24 | Fjernet: «&#124; Antall markedsføringstillatelser &#124; 1 (kansellert) &#124;» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Den eneste norske tillatelsen er kansellert, og kritiske sikkerhetsdata mangler.» → «Kritiske sikkerhetsdata mangler.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklare hvorfor markedsføringstillatelsen er kansellert og om preparater med paliperidon er tilgjengelige i Norge» → «Avklare om preparater med paliperidon er tilgjengelige i Norge» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

