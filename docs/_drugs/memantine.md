---
layout: default
title: Memantine
parent: Kun modellprediksjon (L5)
nav_order: 261
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Memantin: Fra Alzheimers sykdom til migrene

## Oppsummering i én setning

Memantin er et legemiddel som opprinnelig brukes til behandling av Alzheimers sykdom.
TxGNN-modellen forutsier at det kan være effektivt mot **migrene** (rangert som nr. 2 blant de forutsagte indikasjonene, men den med klart sterkest evidens),
og det finnes foreløpig **1 klinisk fase 3-studie** og **18 publikasjoner** som støtter denne retningen. Evidensen er likevel begrenset av at studien er liten (n=33), og oversiktsartiklene beskriver memantin mot migrene som «stort løfte, men lite evidens».

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Alzheimers sykdom |
| Forutsagt ny indikasjon | Migrene (migraine disorder) |
| TxGNN-prediksjonsscore | 99,52 % |
| Evidensnivå | L1 (se merknad under) |
| Status i Norge | Kun avregistrerte godkjenninger |
| Antall godkjenninger | 8 (alle avregistrert) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med forbehold) |

*Merknad om evidensnivå:* Det tildelte nivået L1 er satt i datagrunnlaget. Etter de definerte reglene (L1 krever minst to fullførte fase 3-studier) er det kun én liten fase 3-studie, så evidensen ligger i praksis nærmere L2. Nivået bør vurderes på nytt.

*Merknad om rangering:* Den høyest rangerte prediksjonen fra TxGNN er pulmonal hypertensjon (score 99,54 %, evidensnivå L5, anbefaling Hold). Denne rapporten fokuserer på migrene, som har mest støtte i data.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget som er samlet for denne rapporten. Memantin er imidlertid kjent som en ikke-kompetitiv NMDA-reseptorantagonist, og dens effekt ved Alzheimers sykdom er knyttet til dempning av glutamatmediert eksitotoksisitet.

Glutamat og NMDA-reseptorsignalering antas å bidra til kortikal spredende depresjon, sentral sensitisering og aktivering av det trigeminovaskulære systemet ved migrene. Oversiktsartikler viser at glutamatnivåene er forhøyet hos migrenepasienter, særlig under anfall, og at gener involvert i glutamatsignalering er knyttet til sykdommen. Siden memantin direkte treffer denne signalveien, er det mekanistisk plausibelt at det kan ha forebyggende effekt.

Alzheimers sykdom og migrene er ulike sykdommer, men har felles patofysiologi knyttet til NMDA-reseptoroveraktivitet. En publikasjon peker også på sammenheng mellom primære hodepiner og kognitiv svikt. Samtidig er det viktig å understreke at den kliniske evidensen foreløpig er begrenset.

---

## Klinisk evidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT04698525](https://clinicaltrials.gov/study/NCT04698525) | Fase 3 | Fullført | 33 | Memantin sammenlignet med natriumvalproat som forebyggende behandling av episodisk migrene. Liten studie; resultater og skjevhetsrisiko må verifiseres. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [33961371](https://pubmed.ncbi.nlm.nih.gov/33961371/) | 2021 | Metaanalyse av RCT-er | Clin Neuropharmacol | Vurderer effekten av memantin mot placebo ved migrene; effekten omtales som omstridt. |
| [34352118](https://pubmed.ncbi.nlm.nih.gov/34352118/) | 2021 | Systematisk oversikt | Headache | Vurderer effekt og sikkerhet av memantin som forebyggende behandling av episodisk migrene. |
| [25159002](https://pubmed.ncbi.nlm.nih.gov/25159002/) | 2014 | Systematisk oversikt | Ann Pharmacother | Gjennomgang av data på memantin for forebygging av primære hodepinelidelser. |
| [40978493](https://pubmed.ncbi.nlm.nih.gov/40978493/) | 2025 | Nettverksmetaanalyse | Front Pharmacol | Sammenligner orale forebyggende legemidler mot migrene hos voksne. |
| [26638119](https://pubmed.ncbi.nlm.nih.gov/26638119/) | 2016 | RCT (migrene uten aura, indirekte) | Headache | Randomisert, dobbeltblind, placebokontrollert studie av memantin som forebyggende behandling. |
| [17901918](https://pubmed.ncbi.nlm.nih.gov/17901918/) | 2007 | Retrospektiv studie | J Headache Pain | Retrospektiv gjennomgang av 60 pasienter som fikk memantin som forebyggende behandling. |
| [36869904](https://pubmed.ncbi.nlm.nih.gov/36869904/) | 2023 | Oversikt | Naunyn-Schmiedebergs Arch Pharmacol | Presenterer memantin og ketamin som mulige anti-migrenemidler. |
| [34510445](https://pubmed.ncbi.nlm.nih.gov/34510445/) | 2021 | Kommentar/oversikt | Headache | «Memantine for migraine – big promise but little evidence». |
| [29508147](https://pubmed.ncbi.nlm.nih.gov/29508147/) | 2018 | Oversikt | Neurotherapeutics | Glutamat og dets reseptorer som terapeutiske mål ved migrene. |
| [39467289](https://pubmed.ncbi.nlm.nih.gov/39467289/) | 2024 | Klinisk retningslinje | Ann Intern Med | Retningslinje fra VA/DoD 2023 for behandling og forebygging av migrene og spenningshodepine. |

---

## Markedsinformasjon for Norge

Alle åtte godkjenninger er avregistrert, og ingen er gyldige i dag.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000463 | Ebixa | – | Alzheimers sykdom |
| EMEA/H/C/000378 | Axura | – | Alzheimers sykdom |
| EMEA/H/C/002711 | Memantine Merz | – | Alzheimers sykdom |
| EMEA/H/C/002671 | Memantine ratiopharm | – | Alzheimers sykdom |
| EMEA/H/C/002658 | Marixino (tidligere Maruxa) | – | Alzheimers sykdom |

(Ytterligere tre avregistrerte godkjenninger: Nemdatine, Memantine Mylan og Memantine Accord.)

---

## Sikkerhetshensyn

- **Mulige kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** leversykdom, galleblæresykdom og nedsatt nyrefunksjon.
- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert. Blant de første 20 som er gjennomgått:
  - *Moderat:* antikolinergika, bl.a. hyoscyamin, atropin, glykopyrronium, klidinium, dicyklomin, metskopolamin, propantelin, skopolamin, trospium og mepenzolat.
  - *Mindre:* ranitidin, metformin, cimetidin og kaliumcitrat.
  - *Ukjent nivå:* glimepirid, doksycyklin, lansoprazol, loperamid, famotidin og acetylsalisylsyre.

Preparatomtalens advarsler og kontraindikasjoner er ikke tilgjengelige i dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med forbehold)**

**Begrunnelse:**
Memantin har en plausibel mekanistisk kobling til migrene via NMDA-/glutamatsignalering, og det finnes en fullført fase 3-studie, flere systematiske oversikter og en metaanalyse. Studien er imidlertid liten (n=33), og litteraturen karakteriserer evidensen som begrenset, så anbefalingen bør ikke gå lenger enn forsiktig videre utredning. Tilstedeværelsen i Norge er også svak, siden alle godkjenninger er avregistrert.

**For å gå videre trengs følgende:**
- Gjennomgang av resultater og skjevhetsrisiko i NCT04698525 og metaanalysen (PMID 33961371)
- Større, placebokontrollerte fase 3-studier med migrene som primærindikasjon
- Preparatomtalens advarsler og kontraindikasjoner (dataunderlaget er ufullstendig på dette punktet)
- Detaljerte data om virkningsmekanisme
- Avklaring av regulatorisk vei i Norge, siden alle godkjenninger er avregistrert
- Ny vurdering av evidensnivået (L1 vs. L2)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

