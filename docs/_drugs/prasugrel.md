---
layout: default
title: Prasugrel
parent: Kun modellprediksjon (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Prasugrel: predikert ny indikasjon Pulmonal hypertensjon (evidensnivå L5). Opprinnelig indikasjon: Akutt koronarsyndrom, ustabil angina, hjerteinfarkt"
monitor_inn: "PRASUGREL"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "migraine with or without aura, susceptibility to", "brachydactyly-syndactyly syndrome", "leprosy"]
---

# Prasugrel
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Prasugrel: Fra akutt koronarsyndrom til pulmonal hypertensjon

## Oppsummering

Prasugrel er en blodplatehemmer (P2Y12-hemmer) som opprinnelig brukes ved akutt koronarsyndrom, ustabil angina og hjerteinfarkt.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **pulmonal hypertensjon**, men det finnes **ingen kliniske studier** og **ingen direkte litteratur** som støtter denne retningen.
Det mest underbygde alternativet blant de predikerte indikasjonene er **migrene (assosiert med åpen foramen ovale, PFO)**, med 2 kliniske studier og 2 publikasjoner som gir indirekte støtte.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Akutt koronarsyndrom, ustabil angina, hjerteinfarkt |
| Predikert ny indikasjon | Pulmonal hypertensjon |
| TxGNN-prediksjonsscore | 99,88 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 (trukket tilbake) |
| Anbefalt beslutning | Hold (vent) |

Merk: Den eneste registrerte tillatelsen (Efient, EMEA/H/C/000984) er en sentral europeisk tillatelse og er markert som trukket tilbake.

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelig i de innsamlede dataene. Basert på kjent informasjon er prasugrel en tienopyridin som hemmer P2Y12-reseptoren på blodplater og dermed reduserer blodplateaktivering og aggregasjon. Effekten er godt dokumentert ved akutt koronarsyndrom.

Ved pulmonal hypertensjon kan blodplateaktivering og mikrotrombose bidra til remodellering av lungekarene, så P2Y12-hemming er biologisk plausibelt. Det finnes imidlertid ingen direkte klinisk dokumentasjon for prasugrel ved denne tilstanden, og TxGNN-scoren er kun en modellprediksjon.

De to publikasjonene knyttet til denne prediksjonen (en kohortstudie om klopidogrel-bruk etter PCI og en COVID-19-registerstudie) omhandler ikke pulmonal hypertensjon og gir ikke relevant støtte.

### Andre predikerte indikasjoner

| Predikert indikasjon | Score | Evidensnivå | Kommentar |
|------|------|------|------|
| Migrene | 99,88 % | L3 | Indirekte støtte fra PFO-relatert litteratur; hypotesegenererende |
| Migrene med hjernestammeaura | 99,83 % | L4 | Kun indirekte evidens |
| Migrene med eller uten aura (mottakelighet) | 99,67 % | L4 | Indirekte klinisk støtte og en preklinisk musestudie (epilepsimodell) |
| Kyfoskoliotisk hjertesykdom, revmatoid artritt, homozygot familiær hyperkolesterolemi, hypoalfalipoproteinemi, brakydaktyli-syndaktyli-syndrom, lepra | 99,46–99,81 % | L5 | Ingen klinisk eller litteraturbasert evidens |

---

## Klinisk studieevidens

For den primære prediksjonen (pulmonal hypertensjon): For tiden er ingen relaterte kliniske studier registrert.

For den nest rangerte prediksjonen (migrene) finnes følgende studier. Ingen av dem tester prasugrel som hovedintervensjon, og de gir kun kontekst:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Fase 3 | Rekrutterer | 32 | PFO-rettet behandling for å stoppe migrene; nevner prasugrel som en medikamentell tilnærming, men legemidlet er ikke tydelig studiens intervensjon |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Ikke aktuelt | Avsluttet (terminert) | 7 | Transkateter-lukking av PFO med septalokkluder mot migrene; en enhetsstudie uten prasugrel |

---

## Litteraturevidens

For pulmonal hypertensjon er ingen direkte relevant litteratur funnet. De to publikasjonene som er knyttet til prediksjonen, er listet nedenfor for åpenhet, men gir ikke støtte:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Kohort | Current Medical Research and Opinion | Faktorer knyttet til bruk av og etterlevelse til klopidogrel hos pasienter med akutt koronarsyndrom etter PCI |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Kohort | Kardiologiia | Betydningen av bakgrunnsbehandling for komorbiditet for dødelig utfall ved COVID-19 (ACTIVE-registeret) |

**Litteratur for migrene (indirekte støtte):**

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospektiv kohort | Neurology | Retrospektiv gjennomgang av off-label tienopyridinbehandling (klopidogrel og prasugrel) ved migrene og PFO |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Åpen pilotstudie | Neurology | Tikagrelor ved refraktær migrene/PFO; tienopyridiner reduserte migrenesymptomer hos noen pasienter |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | Preklinisk (dyrestudie) | European Journal of Pharmacology | Prasugrel viste nevrobeskyttende effekt i en musemodell for epilepsi (PTZ-kindling); ikke en migrenemodell |

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000984 | Efient (Substipharm) | Ikke oppgitt | Akutt koronarsyndrom, ustabil angina, hjerteinfarkt (status: trukket tilbake) |

---

## Sikkerhetsvurderinger

Data fra pakningsvedlegget (advarsler og kontraindikasjoner) er ikke tilgjengelig. Se pakningsvedlegget for sikkerhetsinformasjon.

**Kontraindikasjoner fra kunnskapsgraf (ikke fra preparatomtale):**
Kunnskapsgrafen (PrimeKG) knytter prasugrel til følgende tilstander: leversvikt, hypotensive tilstander, blodkoagulasjonssykdom, hjerneslag, cerebrovaskulær sykdom, hjerneinfarkt, skade, trombocytopenisk purpura, intrakraniell blødning, transitorisk iskemisk anfall og vertebrobasilær insuffisiens. Dette er modellbaserte koblinger og må verifiseres mot offisiell produktinformasjon.

**Legemiddelinteraksjoner (100 registrerte; utvalg):**
- **Alvorlig (Major):** deferasirox, ibritumomab tiuxetan
- **Moderat:** acetylsalisylsyre, morfin, opium, fenfluramin, deksfenfluramin, sibutramin
- **Mindre:** blant annet protonpumpehemmere (omeprazol, pantoprazol, esomeprazol m.fl.), H2-blokkere (famotidin, ranitidin, cimetidin, nizatidin) og bupropion

Prasugrel har en blødningsrisiko som er særlig relevant ved samtidig bruk av andre legemidler som påvirker hemostasen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
For pulmonal hypertensjon er prediksjonen utelukkende modellbasert (L5), uten kliniske studier eller direkte litteratur. I tillegg har prasugrel ingen gyldig tillatelse i Norge, og viktige sikkerhetsdata mangler. Migrene (PFO-assosiert) er den mest lovende sekundære retningen (L3), men evidensen er hypotesegenererende og de registrerte studiene tester ikke prasugrel.

**For å gå videre kreves følgende:**
- Innhenting og gjennomgang av pakningsvedlegg (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (MOA) fra DrugBank
- Prekliniske eller eksplorative kliniske data for prasugrel ved pulmonal hypertensjon
- For migrene: en randomisert, kontrollert studie som faktisk tester prasugrel (eller P2Y12-hemmere) hos pasienter med PFO-assosiert migrene
- Vurdering av blødningsrisiko og en overvåkingsplan for aktuelle pasientgrupper
- Avklaring av regulatorisk status, siden den eneste tillatelsen er trukket tilbake
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

