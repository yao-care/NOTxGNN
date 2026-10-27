---
layout: default
title: Trabectedin
parent: Kun modellprediksjon (L5)
nav_order: 429
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Trabectedin: predikert ny indikasjon Brystkreft hos kvinner (female breast carcinoma) (evidensnivå L5). Opprinnelig indikasjon: Eggstokkreft og sarkom"
monitor_inn: "TRABECTEDIN"
predicted_indications: ["female breast carcinoma"]
---

# Trabectedin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Trabectedin: Fra sarkom og eggstokkreft til brystkreft hos kvinner
{: .text-alpha }

## Oppsummering i én setning

Trabectedin er et kreftlegemiddel av marin opprinnelse som opprinnelig brukes mot **sarkom og eggstokkreft**. TxGNN-modellen forutsier at det kan ha effekt mot **brystkreft hos kvinner (female breast carcinoma)**. Dette støttes foreløpig av **1 registrert klinisk studie** (med usikker relevans) og **20 publikasjoner**, blant dem flere fase 2-studier i avansert brystkreft.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Eggstokkreft og sarkom |
| Predikert ny indikasjon | Brystkreft hos kvinner (female breast carcinoma) |
| TxGNN-prediksjonsscore | 99,73 % |
| Evidensnivå | L2 (jf. merknad nedenfor) |
| Markedsstatus i Norge | Kun kansellerte godkjenninger |
| Antall godkjenninger | 2 (begge kansellert) |
| Anbefalt beslutning | Hold |

*Merknad om evidensnivå:* L2 er satt i de innsamlede dataene. Den eneste registrerte studien (NCT00786838) er en fase 2-studie som undersøker QT-effekter, ikke effekt mot brystkreft. Publiserte fase 2-studier i brystkreft finnes, men det er ikke dokumentert noen fullførte randomiserte fase 3-studier. Evidensnivået bør derfor tolkes forsiktig.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) var ikke tilgjengelige i de innsamlede dataene. Ut fra generell kunnskap og litteraturen som ligger til grunn, er trabectedin en alkylerende substans som binder seg til DNA-ets lille fure. Dette utløser DNA-skade og cytotoksisitet som avhenger av transkripsjonskoblet nukleotidreparasjon. Legemidlet påvirker også svulstens mikromiljø, blant annet ved å redusere svulstassosierte makrofager.

Aktiviteten antas å være sterkere i svulster med mangelfull homolog rekombinasjon, for eksempel BRCA-mangelfulle svulster. Det gir en biologisk plausibel begrunnelse for bruk i en undergruppe av brystkreft, som BRCA1/2-assosiert og trippelnegativ sykdom. Eggstokkreft og brystkreft deler dessuten biologiske trekk, særlig knyttet til BRCA og DNA-reparasjon.

Den høye TxGNN-scoren (0,997) stemmer med denne mekanistiske nærheten til de godkjente indikasjonene. Scoren er likevel en modellprediksjon og ikke klinisk bevis.

---

## Klinisk studieevidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Fase 2 | Fullført | 76 | Vurderer effekten av en enkeltdose trabectedin på QT-intervallet i EKG hos pasienter med avanserte solide svulster. Ikke en effektstudie i brystkreft, og kan ikke regnes som direkte effektevidens. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Fase 2-studie (randomisert, to doseringsregimer) | Clinical Breast Cancer | Effekt og sikkerhet av trabectedin som monoterapi i avansert brystkreft etter antracyklin og taksan |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Fase 2-studie | Annals of Oncology | Aktivitet hos kvinner med kimbane-BRCA1/2-mutasjon og forbehandlet metastatisk brystkreft |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Fase 2-studie | Clinical Breast Cancer | Trabectedin ved hormonreseptorpositiv, HER2-negativ avansert brystkreft, i forhold til XPG-genuttrykk |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Fase 1-studie | European Journal of Cancer | Trabectedin + doksorubicin ved avansert bløtdelssarkom og brystkreft (hovedsakelig sarkompasienter) |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Oversikt | Expert Opinion on Investigational Drugs | Gjennomgang av trabectedin ved brystkreft, med vekt på virkningsmekanisme og påvirkning av svulstmikromiljøet |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Oversikt | Cancer Treatment Reviews | Trabectedin som kjemoterapialternativ ved BRCA-mangel |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Prekliniske studier | Cancer Immunology Research | Trabectedin forsterker den antitumorale effekten av IL-12 ved trippelnegativ brystkreft |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Prekliniske studier | European Cytokine Network | Antiangiogene effekter på brystkreftceller |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Prekliniske studier | Toxicology Letters | Ulik induksjon av apoptose i MCF-7- og MDA-MB-453-brystkreftceller |
| [18410797](https://pubmed.ncbi.nlm.nih.gov/18410797/) | 2008 | Oversikt | Seminars in Oncology | Nye legemidler ved antracyklin- og taksanrefraktær metastatisk brystkreft |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000773 | Yondelis (Pharma Mar S.A.) | Ikke oppgitt | Eggstokkreft, sarkom (kansellert) |
| EMEA/H/C/006433 | Trabectedin Accord (Accord Healthcare S.L.U.) | Ikke oppgitt | Sarkom, eggstokkreft (kansellert) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonelt cytotoksisk (DNA-alkylerende middel) |
| Risiko for myelosuppresjon | Høy: nøytropeni av grad 3–4 hos ca. 50 % og trombocytopeni hos ca. 20 % av pasientene (ifølge oversiktsartikkel) |
| Emetogenisitet | Se preparatomtalen |
| Overvåkingspunkter | Fullstendig blodstatus med differensialtelling, leverfunksjon (toksisiteten er hovedsakelig hematologisk og hepatisk), nyrefunksjon. QT-intervall kan vurderes. |
| Håndteringsvern | Må følge gjeldende regler for håndtering av cytotoksiske legemidler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Interaksjonssøket ga 100 treff. Blant de som er listet, er det én interaksjon med alvorlighetsgrad **Major** og de øvrige er **Moderate**.

- **Alvorlig (Major):** klaritromycin
- **Moderat (Moderate):** blant annet deksametason, aprepitant, cimetidin, metronidazol, mikonazol, levofloksacin, minocyklin, rosuvastatin, simvastatin, pioglitazon, rosiglitazon, bupropion, naltrekson, akarbose, orlistat, kenodeoksykolsyre, metreleptin, oksandrolon og oksymetolon

Utover dette henvises det til preparatomtalen for informasjon om advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Det finnes biologisk rimelige argumenter og flere fase 2-studier i avansert brystkreft, særlig ved BRCA-mutasjon, men ingen fullførte fase 3-studier. Den eneste registrerte studien handler om QT-effekt, ikke effekt. Sikkerhetsdata fra preparatomtalen mangler, og begge godkjenningene i Norge er kansellert. Samlet sett er dette på forskningsspørsmålsstadiet.

**For å gå videre trengs følgende:**
- Innhenting og gjennomgang av preparatomtalens advarsler og kontraindikasjoner (kritisk datamangel som blokkerer sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Gjennomgang av resultatene fra fase 2-studiene (PMID 25239225, 24692579, 27266804) for effektdata og sikkerhetsprofil
- Avklaring av hvilke undergrupper (BRCA-mutert, trippelnegativ, XPG-uttrykk) som kan ha nytte
- Vurdering av tilgjengelighet i Norge, siden begge godkjenningene er kansellert, og av hvilken administrasjonsvei som kreves
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

