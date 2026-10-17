---
layout: default
title: Erdafitinib
parent: Kun modellprediksjon (L5)
nav_order: 158
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
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

# Erdafitinib: Fra urotelial kreft til pulmonal hypertensjon

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
| TxGNN-prediksjonsscore | 99,38 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (kansellert) |
| Antall markedsføringstillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Erdafitinib er likevel kjent som en pan-FGFR-hemmer (FGFR1–4). Effekten ved urologiske neoplasmer er knyttet til hemming av FGFR-signalering i tumorceller.

FGF/FGFR-signalering er koblet til remodellering av lungekar samt proliferasjon av glatt muskulatur og endotel ved pulmonal arteriell hypertensjon. Det finnes dermed en biologisk plausibel kobling. Koblingen bygger imidlertid kun på TxGNN-prediksjonen, uten støttende studier eller litteratur i de innsamlede dataene.

Sikkerhetsaspekter som hyperfosfatemi, øyetoksisitet og væskerelaterte effekter må vurderes nøye i en kardiopulmonal pasientgruppe.

**Øvrige predikerte indikasjoner (alle L5, Hold):**

| Rang | Sykdom | TxGNN-score | Kommentar |
|---|---|---|---|
| 2 | Kyfoskoliotisk hjertesykdom | 99,27 % | Ingen klar mekanistisk kobling; sannsynlig artefakt i kunnskapsgrafen |
| 3 | Amenoré | 99,26 % | FGFR-hemming vil snarere kunne gi enn behandle reproduktiv dysfunksjon |
| 4 | Revmatoid artritt | 99,25 % | Plausibel, men ikke validert; kun en generell oversiktsartikkel |
| 5 | Amyotrofisk lateralsklerose | 99,06 % | Effektretningen er usikker |
| 6 | Brakydaktyli-syndaktyli-syndrom | 99,03 % | Medfødt tilstand; postnatal kinasehemming vil neppe reversere misdannelser |

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

| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/006050 | Balversa | – | Urologiske neoplasmer |

Tillatelsen er kansellert, og det finnes ingen gyldige tillatelser for tiden.

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
Prediksjonen for pulmonal hypertensjon (score 99,38 %) støttes av en biologisk plausibel FGFR-kobling, men har ingen kliniske studier eller litteratur (evidensnivå L5). I tillegg er den norske tillatelsen kansellert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Hente og analysere preparatomtalens advarsler og kontraindikasjoner (blokkerende datamangel)
- Innhente detaljerte data om virkningsmekanisme
- Prekliniske studier av FGFR-hemming i modeller for pulmonal hypertensjon
- Vurdering av sikkerhetsprofilen (hyperfosfatemi, øyetoksisitet, væskeretensjon) i kardiopulmonale pasienter
- Avklaring av markedsstatus og tilgjengelighet i Norge gitt at tillatelsen er kansellert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

