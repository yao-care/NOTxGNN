---
layout: default
title: Andexanet Alfa
parent: Kun modellprediksjon (L5)
nav_order: 34
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-15
description: "Andexanet Alfa: predikert ny indikasjon Glanzmanns trombasteni (evidensnivå L5). Opprinnelig indikasjon: Legemiddelrelaterte bivirkninger og uønskede reaksjoner (reversering…"
monitor_inn: "ANDEXANET ALFA"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemophilia"]
---

# Andexanet Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

## Andexanet alfa: Fra legemiddelrelaterte bivirkninger til Glanzmanns trombasteni
{: .text-alpha }

## Oppsummering i én setning

Andexanet alfa er et motgift-legemiddel som brukes til å reversere effekten av faktor Xa-hemmere (blodfortynnende midler) ved legemiddelrelaterte bivirkninger og blødninger.
TxGNN-modellen forutsier at det kan ha effekt ved **Glanzmanns trombasteni**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne spesifikke indikasjonen.
Prediksjonen kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Legemiddelrelaterte bivirkninger og uønskede reaksjoner (reversering av faktor Xa-hemmere) |
| Predikert ny indikasjon | Glanzmanns trombasteni |
| TxGNN-prediksjonsscore | 0,9977 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er (eller er ikke) denne prediksjonen rimelig?

Andexanet alfa er et rekombinant, katalytisk inaktivt faktor Xa-lokkemiddel («decoy»). Det binder og fjerner direkte FXa-hemmere, og også antitrombin III–LMWH-komplekset. Data om detaljert virkningsmekanisme er ikke tilgjengelig i de innsamlede dataene, men den generelle farmakologien er godt kjent.

Glanzmanns trombasteni er en arvelig defekt i plateleintegrinet αIIbβ3 (GPIIb/IIIa), som hindrer blodplateaggregasjon. Andexanet alfa virker kun på koagulasjonskaskaden og påvirker ikke blodplateaggregasjon eller fibrinogenbinding. Det finnes dermed ingen plausibel mekanistisk sammenheng mellom den opprinnelige og den nye indikasjonen.

Den svært høye scoren (0,9977) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede blødnings- og hemostaserelaterte sykdommer, ikke biologisk rasjonale. I tillegg har legemidlet en risiko for tromboemboliske hendelser (varsel i boks), noe som er bekymringsfullt ved en blødningslidelse som behandles med prohemostatiske midler.

Andre predikerte indikasjoner følger samme mønster:

| Predikert indikasjon | TxGNN-score | Evidensnivå | Vurdering |
|------|------|------|------|
| Primær frigjøringsforstyrrelse i blodplater | 0,9976 | L5 | Ingen mekanistisk støtte, ingen studier |
| Pseudo-von Willebrands sykdom | 0,9965 | L5 | Ingen påvirkning av GPIb–VWF-interaksjon, ingen studier |
| Hemofili | 0,9910 | L5 | Kun indirekte litteratur, ingen studier på effekt |

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert for Glanzmanns trombasteni.

---

## Litteraturevidens

Det foreligger ingen relevant litteratur for Glanzmanns trombasteni.

For den fjerde predikerte indikasjonen, hemofili, ble 9 publikasjoner funnet. De er indirekte og gjelder andexanet alfa ved antikoagulantrelaterte blødninger, ikke effekt ved hemofili:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Kohort (ANNEXA-4 delanalyse) | Circulation | Effekt og sikkerhet av andexanet alfa ved akutt gastrointestinal blødning under FXa-hemmere |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Retningslinje/oversikt | Thromb Haemost | ICSH-anbefalinger for laboratoriemåling av direkte orale antikoagulantia (DOAK) |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Laboratoriestudie | Haemophilia | Andexanet alfa kan nøytralisere rivaroksabans interferens i FVIII/FIX-analyser (diagnostisk relevans) |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Oversikt | Curr Pharm Des | Nye hemostatiske midler og antidoter, perioperative hensyn |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Oversikt | Blood | Reversering av anti-FXa-midler og udekkede behov hos traumepasienter |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Oversikt | Drug Saf | Reverseringsstrategier for NOAK |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Oversikt | Dtsch Med Wochenschr | Koagulasjonsforstyrrelser på intensivavdeling |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Oversikt | EJHaem | Gjennomgang av lokale protokoller for bruk av andexanet alfa i Storbritannia |
| [42033142](https://pubmed.ncbi.nlm.nih.gov/42033142/) | 2026 | Posisjonserklæring | Br J Haematol | Britisk hematologiforenings posisjon om bruk av andexanet alfa |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004108 | Ondexxya | Ikke oppgitt | Legemiddelrelaterte bivirkninger og uønskede reaksjoner (status: godkjent) |

---

## Sikkerhetsvurderinger

- **Tromboemboliske hendelser**: Legemidlet har en risiko for tromboembolisme (varsel i boks). Dette er særlig bekymringsfullt ved blødningslidelser som behandles med prohemostatiske midler.

For øvrig sikkerhetsinformasjon, se preparatomtalen (pakningsvedlegget). Ingen legemiddelinteraksjoner ble funnet i dataene.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen mangler mekanistisk støtte, kliniske studier og direkte litteratur. Den høye TxGNN-scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk rasjonale. Legemidlet er dessuten markedsført i Norge (1 gyldig markedsføringstillatelse av 1) og har tromboembolisk risiko.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel)
- Detaljerte data om virkningsmekanisme (MOA)
- Prekliniske data som viser en eventuell effekt på blodplatefunksjon eller hemostase ved de predikerte lidelsene
- Vurdering av om en nisjesituasjon (hemofilipasienter som også bruker FXa-hemmere) er klinisk relevant
- Avklaring av regulatorisk status, siden den eneste norske godkjenningen er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

