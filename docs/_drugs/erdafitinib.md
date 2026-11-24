---
layout: default
title: Erdafitinib
parent: Kun modellprediksjon (L5)
nav_order: 158
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Erdafitinib: predikert ny indikasjon Pulmonal hypertensjon (evidensnivå L5). Opprinnelig indikasjon: Urologiske neoplasmer"
monitor_inn: "ERDAFITINIB"
predicted_indications: ["pulmonary hypertension", "kyphoscoliotic heart disease", "amenorrhea (disease)", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "brachydactyly-syndactyly syndrome"]
---

# Erdafitinib
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

## Erdafitinib: Fra urotelial kreft til pulmonal hypertensjon
{: .text-alpha }

## Oppsummering i én setning

Erdafitinib er en FGFR-hemmer (tyrosinkinasehemmer) som opprinnelig er godkjent for behandling av urologiske neoplasmer.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **pulmonal hypertensjon**.
Prediksjonen støttes foreløpig av **0 kliniske studier** og **0 publikasjoner** som er direkte relevante, så den hviler kun på modellprediksjon.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Urologiske neoplasmer |
| Predikert ny indikasjon | Pulmonal hypertensjon |
| TxGNN-prediksjonsscore | 0,9938 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall markedsføringstillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Erdafitinib (uoffisiell oversettelse): «Erdafitinib er en kinasehemmer som bindes til og hemmer den enzymatiske aktiviteten til FGFR1, FGFR2, FGFR3 og FGFR4, basert på in vitro-data. Erdafitinib hemmet FGFR-fosforylering og -signalering og reduserte cellelevedyktigheten i cellelinjer som uttrykker genetiske FGFR-endringer, inkludert punktmutasjoner, amplifikasjoner og fusjoner.» Engelsk originaltekst: "Erdafitinib is a kinase inhibitor that binds to and inhibits enzymatic activity of FGFR1, FGFR2, FGFR3 and FGFR4 based on in vitro data. Erdafitinib inhibited FGFR phosphorylation and signaling and decreased cell viability in cell lines expressing FGFR genetic alterations, including point mutations, amplifications, and fusions." ([DailyMed: Balversa (erdafitinib) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2a8aa5c0-6c92-4566-8c45-e8f4d1fc20ee), versjon av 2025-10-24; hentet 2026-11-19). Erdafitinib er likevel kjent som en pan-FGFR-hemmer (FGFR1–4). Effekten ved urologiske neoplasmer er knyttet til hemming av FGFR-signalering i tumorceller.

FGF/FGFR-signalering er koblet til remodellering av lungekar samt proliferasjon av glatt muskulatur og endotel ved pulmonal arteriell hypertensjon. Det finnes dermed en biologisk plausibel kobling. Koblingen bygger imidlertid kun på TxGNN-prediksjonen, uten støttende studier eller litteratur i de innsamlede dataene.

Sikkerhetsaspekter som hyperfosfatemi, øyetoksisitet og væskerelaterte effekter må vurderes nøye i en kardiopulmonal pasientgruppe.

**Øvrige predikerte indikasjoner (alle L5, Hold):**

| Rang | Sykdom | TxGNN-score | Kommentar |
|---|---|---|---|
| 2 | Kyfoskoliotisk hjertesykdom | 0,9927 | Ingen klar mekanistisk kobling; scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens |
| 3 | Amenoré | 0,9926 | FGFR-hemming vil snarere kunne gi enn behandle reproduktiv dysfunksjon |
| 4 | Revmatoid artritt | 0,9925 | Plausibel, men ikke validert; kun en generell oversiktsartikkel |
| 5 | Amyotrofisk lateralsklerose | 0,9906 | Effektretningen er usikker |
| 6 | Brakydaktyli-syndaktyli-syndrom | 0,9903 | Medfødt tilstand; postnatal kinasehemming vil neppe reversere misdannelser |

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

For hovedprediksjonen (pulmonal hypertensjon) finnes ingen relatert litteratur. For rang 4 (revmatoid artritt) er én publikasjon koblet til, men den er ikke sykdomsspesifikk:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Oversiktsartikkel | Pharmacological Research | Oppdatering om egenskaper ved FDA-godkjente småmolekylære proteinkinasehemmere (inkl. erdafitinib godkjent i 2019); ingen spesifikk evidens for erdafitinib ved revmatoid artritt |

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/006050 | Balversa | Erdafitinib | Urologic Neoplasms | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Legemidlet er markedsført, og 1 av 1 tillatelse er gyldig.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet behandling (FGFR-tyrosinkinasehemmer) |
| Myelosuppresjonsrisiko | Se preparatomtalen for advarsler og forsiktighetsregler |
| Emetogenisitetsklassifisering | Se preparatomtalen for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Fosfatnivå i serum og øyeundersøkelser (basert på kjente sikkerhetshensyn); ytterligere punkter i preparatomtalen |
| Håndteringsbeskyttelse | Følg lokale retningslinjer for håndtering av antineoplastiske legemidler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Det er registrert 100 interaksjoner i datagrunnlaget. Et utvalg av de viktigste:
  - **Alvorlig (Major):** kolekalsiferol, deksametason, kalsiumfosfat, kalsifediol, kalsitriol, kalsiumacetat, klaritromycin, magnesiumoksid, magnesiumsulfat, magnesiumklorid
  - **Moderat:** metformin, loperamid, saksagliptin, eliglustat, empagliflozin, linagliptin, naldemedin, naloksegol, prukaloprid, rifaximin

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for pulmonal hypertensjon (score 0,9938) støttes av en biologisk plausibel FGFR-kobling, men har ingen kliniske studier eller litteratur (evidensnivå L5). I tillegg mangler sikkerhetsdata fra preparatomtalen.

<!-- review:begin no-lic-20261124b-erdafitinib-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den norske tillatelsen kansellert, og sikkerhetsdata fra preparatomtalen mangler.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-erdafitinib-1 -->

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalens advarsler og kontraindikasjoner (blokkerende datamangel)
- Innhente detaljerte data om virkningsmekanisme
- Prekliniske studier av FGFR-hemming i modeller for pulmonal hypertensjon
- Vurdering av sikkerhetsprofilen (hyperfosfatemi, øyetoksisitet, væskeretensjon) i kardiopulmonale pasienter
- Avklaring av markedsstatus og tilgjengelighet i Norge

<!-- review:begin no-lic-20261124b-erdafitinib-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av markedsstatus og tilgjengelighet i Norge gitt at tillatelsen er kansellert» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-erdafitinib-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Balversa (erdafitinib) prescribing information, Janssen Products LP](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2a8aa5c0-6c92-4566-8c45-e8f4d1fc20ee) |
| 2026-11-24 | Rettet: «I tillegg er den norske tillatelsen kansellert, og sikkerhetsdata fra preparatomtalen mangler.» → «I tillegg mangler sikkerhetsdata fra preparatomtalen.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av markedsstatus og tilgjengelighet i Norge gitt at tillatelsen er kansellert» → «Avklaring av markedsstatus og tilgjengelighet i Norge» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

