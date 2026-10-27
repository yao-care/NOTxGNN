---
layout: default
title: Trametinib
parent: Kun modellprediksjon (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Trametinib: predikert ny indikasjon Koroideremi (rangert som nr. 1) (evidensnivå L5). Opprinnelig indikasjon: Melanom"
monitor_inn: "TRAMETINIB"
predicted_indications: ["choroideremia"]
---

# Trametinib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Trametinib: Fra melanom til koroideremi (primær prediksjon) – med ikke-kutan melanom som best underbygde nye retning
{: .text-alpha }

Merk: Den høyest rangerte prediksjonen (koroideremi) har ingen støttende evidens og et mekanistisk svakt grunnlag. Rapporten tar derfor for seg den høyest rangerte prediksjonen, men vurderer også den best dokumenterte retningen, **ikke-kutant melanom** (rangert som nr. 2).

---

## Oppsummering i én setning

Trametinib er en MEK-hemmer som opprinnelig brukes mot melanom.
TxGNN-modellen predikerer høy score for **koroideremi** (99,31 %), men uten kliniske studier eller publikasjoner. Retningen med mest støtte er **ikke-kutant melanom**, med **10 registrerte kliniske studier** (hovedsakelig tidlig fase eller indirekte relevante) og ingen publikasjoner.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Melanom |
| Predikert ny indikasjon | Koroideremi (rangert som nr. 1) |
| TxGNN-prediksjonsscore | 99,31 % |
| Evidensnivå | L5 (kun modellprediksjon) |
| Status i Norge | Kun kansellert |
| Antall godkjenninger | 1 (kansellert) |
| Anbefalt beslutning | Hold |

For sammenligning: ikke-kutant melanom (score 99,30 %) har evidensnivå L2 etter datagrunnlaget, med anbefalingen «forskningsspørsmål».

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget som er samlet for denne rapporten. Trametinib er kjent som en MEK1/MEK2-hemmer (målgener MAP2K1 og MAP2K2) og brukes ved BRAF V600-mutert melanom, ofte sammen med dabrafenib.

**Koroideremi:** Sykdommen er en X-bundet netthinnedegenerasjon forårsaket av tap av funksjon i CHM-genet (REP1). Den er ikke en MAPK-drevet kreftsykdom, og det finnes ikke noe etablert grunnlag for MEK-hemming. Den høye scoren er sannsynligvis en grafbasert artefakt fra nærheten mellom melanom og øyesykdommer i kunnskapsgrafen, og bør ikke tolkes som biologisk støtte.

**Ikke-kutant melanom:** Slike melanomer (slimhinne, uvealt, acral-nære) kan ha endringer i MAPK-signalveien (BRAF, NRAS, NF1, KIT). MEK-hemming er derfor mekanistisk plausibelt, særlig i kombinasjon med BRAF- eller RAF-hemmere. Studiene er imidlertid heterogene, og subtypespesifikk effekt kan ikke bekreftes.

---

## Evidens fra kliniske studier

**Koroideremi:** Det er for tiden ingen relaterte kliniske studier registrert.

**Ikke-kutant melanom (den best dokumenterte alternative retningen):**

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT02296112](https://clinicaltrials.gov/study/NCT02296112) | Fase 2 | Fullført | 9 | Åpen studie av trametinib ved melanom med BRAF non-V600-mutasjoner; direkte legemiddelevidens, men liten og med begrenset styrke |
| [NCT04439292](https://clinicaltrials.gov/study/NCT04439292) | Fase 2 | Aktiv, ikke rekrutterende | 44 | NCI-MATCH delprotokoll H: dabrafenib + trametinib ved BRAF V600-muterte svulster (utenom melanom m.fl.); tumoragnostisk, indirekte relevans |
| [NCT02872259](https://clinicaltrials.gov/study/NCT02872259) | Fase 1/2 | Fullført | 74 | BGB324 i kombinasjon med pembrolizumab eller dabrafenib/trametinib ved avansert melanom; støtter kombinasjonssikkerhet |
| [NCT02974725](https://clinicaltrials.gov/study/NCT02974725) | Fase 1 | Avsluttet | 241 | LXH254-kombinasjoner (inkl. trametinib) ved NRAS-mutert melanom og NSCLC; begrenset evidens |
| [NCT05907304](https://clinicaltrials.gov/study/NCT05907304) | Fase 1 | Aktiv, ikke rekrutterende | 86 | Naporafenib + trametinib ved faste svulster med RAS Q61X-mutasjon; resultater foreligger ikke |
| [NCT02410863](https://clinicaltrials.gov/study/NCT02410863) | Fase 2 | Avsluttet | 10 | Optimalisering av målrettet behandling etter BRAF-hemmer-progresjon |
| [NCT03944356](https://clinicaltrials.gov/study/NCT03944356) | Ikke relevant | Fullført | 232 | Ikke-intervensjonsstudie av adjuvant dabrafenib + trametinib ved kutant melanom; indirekte relevans |
| [NCT03340506](https://clinicaltrials.gov/study/NCT03340506) | Fase 4 | Rekrutterer | 100 | Oppfølgingsstudie for langtidssikkerhet; kun sikkerhetsdata |
| [NCT07440290](https://clinicaltrials.gov/study/NCT07440290) | Fase 2/3 | Rekrutterer | 30 | DETERMINE: dabrafenib + trametinib ved BRAF V600-positive kreftformer hos voksne og barn |
| [NCT05275374](https://clinicaltrials.gov/study/NCT05275374) | Fase 1/2 | Ikke startet rekruttering | 221 | XP-102 med trametinib ved BRAF V600-muterte solide svulster; ingen data ennå |

NCT02416232 (tilgangsprogram, ikke lenger tilgjengelig) er utelatt fordi det ikke gir effektevidens.

---

## Evidens fra litteratur

For koroideremi og ikke-kutant melanom foreligger det for tiden ingen relatert litteratur.

For andre predikerte melanomvarianter finnes følgende (kun oversikter og kasuistikker):

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [40853557](https://pubmed.ncbi.nlm.nih.gov/40853557/) | 2025 | Oversikt | JAMA | Generell oversikt over kutant melanom (forekomst og epidemiologi) |
| [31361915](https://pubmed.ncbi.nlm.nih.gov/31361915/) | 2020 | Kasuistikk/oversikt | Clin Exp Dermatol | To tilfeller av BRAF-mutert konjunktivalt melanom, med litteraturgjennomgang |
| [31747798](https://pubmed.ncbi.nlm.nih.gov/31747798/) | 2019 | Kasuistikk/oversikt | J Investig Med High Impact Case Rep | Melanom i tåresekken hos 15 japanske pasienter |
| [41209431](https://pubmed.ncbi.nlm.nih.gov/41209431/) | 2026 | Kasuistikk | Oncol Lett | Kombinert BRAF/MEK-hemming ved hjernemetastaser av melanom under graviditet |
| [37756677](https://pubmed.ncbi.nlm.nih.gov/37756677/) | 2025 | Kasuistikk | Retinal Cases Brief Rep | Rask tilbakegang av koroidal metastase etter kombinert målrettet behandling |
| [42583475](https://pubmed.ncbi.nlm.nih.gov/42583475/) | 2026 | Kasuistikk | Ann Med Surg | Tidlig metastatisk BRAF V600E-melanom uten kjent primærtumor |
| [41310270](https://pubmed.ncbi.nlm.nih.gov/41310270/) | 2025 | Kasuistikk | Childs Nerv Syst | Amelanotisk melanom i sentralnervesystemet hos barn |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002643 | Mekinist | – | Melanom (status: kansellert) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet behandling (MEK-hemmer) |
| Myelosuppresjonsrisiko | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Håndteringsbeskyttelse | Følg gjeldende regler for håndtering av kreftlegemidler |

---

## Sikkerhetsvurderinger

Advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelige i datagrunnlaget. Se pakningsvedlegget for sikkerhetsinformasjon.

**Legemiddelinteraksjoner:** Det er funnet 17 oppføringer, hvorav 15 er interaksjoner av moderat alvorlighetsgrad (DDInter):
- Fostamatinib, elagolix, apalutamid, brigatinib
- Dabrafenib, enkorafenib, isavukonazonium, lasmiditan
- Midostaurin, sarecyklin, enzalutamid, erdafitinib
- Gilteritinib, idelalisib, tukatinib

De to øvrige oppføringene beskriver farmakologiske mål (MEK1/MAP2K1 og MEK2/MAP2K2), ikke interaksjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold** (for koroideremi)

**Begrunnelse:**
Prediksjonen for koroideremi bygger kun på modellscore, uten studier, litteratur eller biologisk grunnlag; sykdommen er ikke MAPK-drevet. Ikke-kutant melanom er mekanistisk plausibelt og har tidlig-fase-studier, men uten subtypespesifikke resultater, og bør behandles som et forskningsspørsmål.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA)
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner)
- For ikke-kutant melanom: subtypespesifikke resultater fra studier, fortrinnsvis med kartlegging av BRAF/NRAS/NF1/KIT-status
- Avklaring av markedsstatus i Norge, siden den eneste godkjenningen er kansellert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

