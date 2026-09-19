---
layout: default
title: Atazanavir
parent: Moderat evidens (L3-L4)
nav_order: 37
evidence_level: L4
indication_count: 6
---

# Atazanavir
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **6** stk.
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

# Atazanavir: Fra HIV-1-infeksjon til Simian Immunodeficiency Virus-infeksjon

## Én-linjers sammendrag

> Atazanavir er en HIV-1-proteasehemmer brukt som del av antiretroviral terapi for HIV-1-infeksjon (utledet fra forsøkssammenheng i denne evidenspakken; ingen formell indikasjonsregistrering foreligger fordi legemidlet ikke er markedsført i Norge).
> TxGNN-modellens topprangerte prediksjon er **Simian Immunodeficiency Virus (SIV)-infeksjon**, en lentivirusinfeksjon hos makaker,
> støttet av bare **1 preklinisk publikasjon** og **0 kliniske studier** — bevis som er bare preklinisk/mekanistisk, ikke klinisk handlingsorientert.

> ⚠️ **Viktig forbehold:** Rankinger 2–4 i dette prediksjonssettet (katters AIDS, en sjelden nevrutviklingsforstyrrelse og et foreldet hyperlipidemibegrep) har ingen meningsfull mekanistisk eller bevisforankring og bør ikke forfølges. Ranking 5 ("AIDS related complex") har sterke bevis (2 fullførte fase 3 RCT-er, L1), men dette gjenspeiler legemidlets **allerede etablerte kjerneindikasjonen**, ikke en genuin repurposing-mulighet.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | HIV-1-infeksjon (antiretroviral terapi) — utledet fra klinisk forsøkssammenheng; ikke formelt registrert da det ikke finnes Taiwan/Norge-lisens |
| Predikert ny indikasjon | Simian Immunodeficiency Virus (SIV)-infeksjon |
| TxGNN-prediksjonspoengsum | 99.98% |
| Evidensnivå | L4 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt avgjørelse | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte DrugBank MOA-data var ikke tilgjengelige i denne evidenspakken (flagget som et datakløft med høy alvorlighetsgrad, DG002). Konteksten innebygd i selve beviset (kliniske forsøkstitler og begrunnelsen for ranking 5) indikerer imidlertid at atazanavir er en **HIV-1-proteasehemmer** som blokkerer spalting av Gag-Pol-polyproteinet, noe som forhindrer viral modning — det farmakologiske grunnlaget for dets etablerte bruk ved HIV-1-infeksjon.

SIV og HIV tilhører begge lentivirusslekten og deler strukturell homologi i sine proteasenzymer. Dette gir et teoretisk grunnlag for proteasehemming på tvers av arter, som er grunnlaget for TxGNNs høye likhetsscore. SIV-infeksjon er imidlertid eksklusivt en **ikke-menneskelig sykdomsmodell** brukt i translasjonsforskning på HIV (f.eks. makakstudier av virale CNS-reservoarer). Det er ikke en menneskelig klinisk indikasjon, så denne prediksjonen har kun forskningsverdi — den kan ikke fremmes som en menneskelig legemiddelrepurposing-kandidat uavhengig av mekanistisk plausibilitet.

Derimot er ranking 5 ("AIDS related complex") direkte støttet av to fullførte fase 3 RCT-er (NCT00035932, n=571; NCT01099579, n=82) og gjenspeiler atazanavirs kjernefarmakologi som allerede er godkjent, snarere enn en ny indikasjon. Dette er nyttig kontekst, men utgjør ikke «repurposing» i den betydningen denne rapporten er ment å evaluere.

---

## Bevis fra kliniske studier

For øyeblikket ingen relaterte kliniske studier registrert for Simian Immunodeficiency Virus-infeksjon.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Nøkkelfunn |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | Preklinisk (makakmodell) | The Journal of Infectious Diseases | HAART-behandlede SIV-infiserte makaker viste redusert viral replikering og inflammasjon i CNS, men vedvarende viral DNA i CNS til tross for virusundertrykkelse i plasma — et funn fra dyretranslasjonsforskning, ikke direkte bevis for en menneskelig indikasjon. |

---

## Norsk markedsinformasjon

Atazanavir er **ikke for øyeblikket markedsført i Norge** (markedsstatus: Ikke markedsført / Ikke markedsført). Det finnes ingen legemiddellisensregistreringer (`total_licenses = 0`), så ingen autorisasjonstabell kan produseres.

---

## Sikkerhetsoverveielser

Se pakningsvedlegg for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og legemiddel-legemiddel-interaksjonsdata var ikke tilgjengelige i denne evidenspakken — flagget som et blokkerende datakløft, DG001, som forhindrer inngang til S1-sikkerhetsvurderingsfasen.)

---

## Konklusjon og neste trinn

**Avgjørelse: Avvent**

**Begrunnelse:**
Den topprangerte prediksjonen (SIV-infeksjon) retter seg mot en ikke-menneskelig sykdomsmodell og er støttet kun av en enkelt preklinisk publikasjon uten kliniske studier (L4, S0 avgjørelsesstadie) — utilstrekkelig for repurposing-vurdering. Rankinger 2–4 mangler enhver troverdig mekanistisk eller bevisforankring. Ranking 5, selv om sterkt støttet (L1), representerer legemidlets eksisterende kjerneindikasjonen snarere enn en ny mulighet, så det endrer ikke den overordnede anbefalingen for denne repurposing-kandidaten.

**Følgende er påkrevd for å fortsette:**
- TFDA-ekvivalent (eller norsk) pakningsvedlegg advarsler/kontraindikasjoner (DG001 — Kritisk; påkrevd før noen S1-sikkerhetsvurdering)
- Bekreftet handlingsmekanisme-data fra DrugBank (DG002 — Høy prioritet; nødvendig for korrekt vurdering av mekanistisk plausibilitet)
- Hvis translasjonsforskning skal forfølges, må det etableres en definert vei fra SIV-makakmodellen til en genuin menneskelig indikasjon (f.eks. HIV-assosiert nevrokognitiv lidelse), siden SIV-infeksjon i seg selv ikke er et menneskelig sykdomsmål

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

