---
layout: default
title: Paclitaxel
parent: Kun modellprediksjon (L5)
nav_order: 304
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "PACLITAXEL"
predicted_indications: ["parameningeal embryonal rhabdomyosarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina"]
description: "Paclitaxel: predikert ny indikasjon Parameningeal embryonal rhabdomyosarcoma (evidensnivå L5). Opprinnelig indikasjon: Breast Neoplasms"
---

# Paclitaxel
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Paclitaxel: Parameningeal embryonal rhabdomyosarcoma
{: .text-alpha }

## Enkeltsetningssammendrag

Paklitaksel er et cellegiftmiddel (taksan) som opprinnelig brukes mot brystkreft, bukspyttkjertelkreft og ikke-småcellet lungekreft.
Dette er imidlertid en indikasjon som allerede er godkjent, og ikke reell ompropulsering.
Foreløpig støttes retningen av **45 kliniske studier** og **20 publikasjoner** i de innsamlede dataene, men studielisten for denne indikasjonen inneholder bare fase 1- og fase 2-studier som hovedtyngde.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Breast Neoplasms;Pancreatic Neoplasms;Carcinoma, Non-Small-Cell Lung; Breast Neoplasms |
| Predikert ny indikasjon | Parameningeal embryonal rhabdomyosarcoma |
| TxGNN-prediksjonsscore | 0.9973 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 4 av 4) |
| Antall godkjenninger | 4 (gyldige: 4) |
| Antall tillatelser | 4 (alle kansellert) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med sikkerhetstiltak) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er ikke tilgjengelige i de innsamlede dataene. Ut fra kjent kunnskap stabiliserer paklitaksel mikrotubuli, noe som gir mitotisk arrest og apoptose i raskt delende kreftceller. Mekanismen er uavhengig av hormonreseptorstatus.

Brystkreft er allerede en godkjent indikasjon, så dette er bruk innenfor godkjenningen og ikke sann ompropulsering. Prediksjonen bekrefter i hovedsak en kjent bruk. Studielisten som er levert, inneholder hovedsakelig fase 1/2-studier, så evidensnivået L2 gjenspeiler de foreliggende dataene, ikke hele den fase 3-evidensen som finnes for paklitaksel ved brystkreft.

Merk at flere av de øvrige predikerte indikasjonene (for eksempel ER-negativ, ER-positiv og hormonresistent brystkreft) er undergrupper av brystkreft. Ehrlich-tumor er en musemodell, og rabdomyosarkom-prediksjonene bygger kun på modellscore.

---

## Klinisk studieevidens

Et utvalg av de mest relevante studiene (de fleste er kombinasjonsregimer, så paklitaksels egen bidrag er vanskelig å isolere):

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Fase 3 | Fullført | 652 | Taksanbasert kjemoterapi med lapatinib versus trastuzumab ved HER2-positiv metastatisk brystkreft |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Fase 3 | Fullført | 632 | Neoadjuvant nab-paklitaksel versus løsemiddelbasert paklitaksel ved HER2-negativ høyrisiko brystkreft |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Fase 3 | Fullført | 455 | Neo-ALTTO: neoadjuvant lapatinib, trastuzumab og kombinasjon, sammen med paklitaksel |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Fase 3 | Fullført | 280 | Rekkefølge av FEC og paklitaksel + trastuzumab ved HER2-positiv operabel brystkreft |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Fase 3 | Fullført | 580 | Lapatinib + paklitaksel versus paklitaksel alene som førstelinje ved metastatisk brystkreft |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Fase 3 | Fullført | Ikke oppgitt | Gemcitabin + paklitaksel versus paklitaksel ved lokalt tilbakevendende eller metastatisk brystkreft |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Fase 3 | Fullført | 478 | Dosetett FE75C etterfulgt av docetaksel versus paklitaksel som adjuvant behandling |
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Fase 2 | Fullført | 50 | Ukentlig paklitaksel + trastuzumab ved metastatisk brystkreft |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Fase 2 | Ukjent | Ikke oppgitt | Randomisert sammenligning av to regimer med docetaksel eller paklitaksel ved metastatisk brystkreft |
| [NCT00002826](https://clinicaltrials.gov/study/NCT00002826) | Fase 2 | Fullført | 36 | PSC 833 for å modulere multiresistens mot paklitaksel (liten pilotstudie) |

Av disse listene fremgår det at flere fase 3-studier faktisk finnes i de innsamlede dataene, men de tester i hovedsak kombinasjonspartnere eller regimer og ikke paklitaksel isolert. Tilleggsstudier for undergrupper (ER-negativ, ER-positiv) inkluderer blant annet NCT00785291 (fase 3, n=799, ukentlig paklitaksel versus nab-paklitaksel eller ixabepilon med/uten bevacizumab).

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Oversikt | Lancet | Taksaner (paklitaksel, docetaksel) er evidensbaserte komponenter i behandling av avansert bryst-, lunge- og eggstokkreft |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Oversikt | Drug Ther Bull | Paklitaksel og docetaksel ved bryst- og eggstokkreft |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Klinisk studie (fase 2) | Cancer | Doksorubicin og paklitaksel ved avansert brystkarsinom; betydningen av tidligere adjuvant antracyklin |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Oversikt | Cancer | Paklitaksel i multimodal behandling av inflammatorisk brystkarsinom |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | Doseeskaleringsstudie | Ann Oncol | Maksimal tolerert dose av paklitaksel (3-timers infusjon) med cyklofosfamid ved avansert brystkreft |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Translasjonell studie | Nat Commun | TEKT4-varianter og resistens mot paklitaksel ved brystkreft |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Beregningsbasert studie | Chem Biol Drug Des | Paklitaksel-kombinasjoner mot brystkarsinom og identifisering av biomarkører |
| [31515668](https://pubmed.ncbi.nlm.nih.gov/31515668/) | 2019 | Prekliniske data | Cancer Chemother Pharmacol | Nedregulering av SRSF3 sensibiliserer brystkreftceller for paklitaksel |

Flere av publikasjonene er eldre oversikter eller prekliniske studier. Det er ingen nyere randomiserte studier blant publikasjonene som er listet for denne indikasjonen.

---

## Markedsinformasjon for Norge


| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000778 | Abraxane | Ikke oppgitt | Brystkreft, bukspyttkjertelkreft, ikke-småcellet lungekreft |
| EMEA/H/C/005997 | Apexelsin | Ikke oppgitt | Brystkreft, bukspyttkjertelkreft, ikke-småcellet lungekreft |
| EMEA/H/C/006173 | Naveruclif | Ikke oppgitt | Brystkreft, bukspyttkjertelkreft, ikke-småcellet lungekreft |
| EMEA/H/C/004441 | Pazenir | Ikke oppgitt | Brystkreft |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonelt cytotoksisk middel (taksan, mikrotubulistabilisator) |
| Risiko for myelosuppresjon | Høy (nøytropeni er vanlig og dosebegrensende; knoklemargssuppresjon er kjent) |
| Emetogenisitet | Lav til moderat |
| Overvåkingspunkter | Fullstendig blodstatus med differensialtelling, lever- og nyrefunksjon, perifer nevropati |
| Håndteringsbeskyttelse | Må følge regelverk for håndtering av cytotoksiske legemidler |

Merk: Klassifiseringen bygger på alminnelig kjent farmakologi, siden de innsamlede dataene ikke inneholder spesifikke toksisitetsdata. Se også preparatomtalen for detaljer.

---

## Sikkerhetsvurderinger

Advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelige i de innsamlede dataene. Se preparatomtalen for sikkerhetsinformasjon.

- **Kontraindikasjoner fra kunnskapsgraf (ikke fra preparattekst):** TxGNN-kunnskapsgrafen (PrimeKG) knytter paklitaksel til blant annet nøytropeni, agranulocytose, trombocytopeni, anemi, perifer nevropati, lever- og nyresykdom, hjerteinfarkt, plutselig hjertestans, astma, diabetes (inkludert ketoacidose), hypotensive tilstander, hyperbilirubinemi/Gilberts syndrom, psoriasis, angstlidelser og gallblæresykdom. Disse er modellbaserte koblinger og bør verifiseres mot godkjent preparattekst.
- **Legemiddelinteraksjoner:** 100 interaksjoner er funnet totalt; de listede inkluderer hovedsakelig moderate interaksjoner med aprepitant, cimetidin, klaritromycin, klotrimazol, deksametason, eliglustat, metronidazol, mikonazol, rolapitant, rosuvastatin, simvastatin, tinidazol og troglitazon. Mindre interaksjoner gjelder askorbinsyre og levofloksacin. Interaksjonene med glimepirid, doksycyklin, morfin, metformin og omeprazol har ukjent alvorlighetsgrad.
- **Sikkerhetssignaler i litteraturen:** Kasuistikker beskriver blant annet paklitaksel-indusert pneumonitt, uveitt, hornhinnelesjoner og perifer polynevropati.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med sikkerhetstiltak)**

**Begrunnelse:**
Brystkreft er en etablert, godkjent indikasjon for paklitaksel, og flere fase 2- og fase 3-studier i de innsamlede dataene støtter bruken, selv om de fleste er kombinasjonsregimer. Siden alle fire tillatelser i Norge er kansellert og sikkerhetsdata fra preparatomtalen mangler, må bruken ledsages av sikkerhetstiltak.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel for sikkerhetsscreening
- Hente detaljerte data om virkningsmekanisme fra DrugBank
- Avklare hvorfor norske tillatelser er kansellert, og om et alternativt preparat er tilgjengelig
- Plan for overvåking av blodstatus, nevropati og legemiddelinteraksjoner
- Evaluere fase 3-evidens der paklitaksel er den testede komponenten, ikke bare en del av regimet

**Merknad om øvrige predikerte indikasjoner:** ER-negativ og ER-positiv brystkreft støttes av fase 2/3-kombinasjonsstudier (anbefaling: fortsett med sikkerhetstiltak). Hormonresistent brystkarsinom og genekspresjonsdefinert brystkarsinom er kun forskningsspørsmål. Ehrlich-tumor, bilateralt brystkarsinom, brystvortekarsinom og de to rabdomyosarkom-indikasjonene anbefales satt på vent (Hold), siden evidensen er prekliniske data, kasuistikker eller kun modellprediksjon.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

