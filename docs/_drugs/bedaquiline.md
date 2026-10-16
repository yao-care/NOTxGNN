---
layout: default
title: Bedaquiline
parent: Kun modellprediksjon (L5)
nav_order: 53
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bedaquiline: predikert ny indikasjon Tuberkulose… (evidensnivå L5). Opprinnelig indikasjon: Multiresistent tuberkulose"
---

# Bedaquiline
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

# Bedaquilin: Fra multiresistent tuberkulose til inaktiv tuberkulose

## Oppsummering i én setning

Bedaquilin er et legemiddel mot tuberkulose som opprinnelig brukes til behandling av **multiresistent tuberkulose**.
TxGNN-modellen forutsier at det også kan være aktuelt for **tuberkulose, bovin** (rangert først). Den best underbygde prediksjonen i dataene er imidlertid **inaktiv tuberkulose**, med **3 kliniske studier** og **18 publikasjoner**, hvor ingen av studiene har publiserte resultater ennå.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Multiresistent tuberkulose |
| Predikert ny indikasjon | Tuberkulose, bovin (rangert først av TxGNN). Best dokumentert: inaktiv tuberkulose |
| TxGNN-prediksjonsscore | 99,96 % (bovin tuberkulose); 99,96 % (inaktiv tuberkulose) |
| Evidensnivå | L5 for bovin tuberkulose er ikke riktig; L4 for bovin tuberkulose (kun in vitro-studie). L2 for inaktiv tuberkulose |
| Markedsstatus i Norge | Kun annullert |
| Antall godkjenninger | 1 (annullert) |
| Anbefalt beslutning | Bovin tuberkulose: Hold. Inaktiv tuberkulose: Proceed with Guardrails |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i det innsamlede grunnlaget. Basert på kjent informasjon hemmer bedaquilin det mykobakterielle enzymet F-ATP-syntase (underenhet AtpE), og dets effekt ved multiresistent tuberkulose er godt etablert. Mekanismen kan dermed være anvendelig for andre sykdommer forårsaket av mykobakterier.

**Bovin tuberkulose (rangert først):** Sykdommen skyldes *Mycobacterium bovis*, som tilhører *M. tuberculosis*-komplekset, så aktivitet er plausibel. Den eneste koblede artikkelen er imidlertid en in vitro-metodestudie på *M. tuberculosis*, som kun er indirekte evidens. Det finnes ingen kliniske data for bovin tuberkulose spesifikt.

**Inaktiv (latent) tuberkulose:** Dette er den best underbygde prediksjonen. Bedaquilin har sterk steriliserende effekt mot *M. tuberculosis*, og er et plausibelt valg som forebyggende behandling blant kontakter av pasienter med multiresistent tuberkulose, der standardregimer basert på isoniazid eller rifamycin svikter. Fase 2/3-studien BREACH-TB tester dette direkte, men rekrutterer fortsatt og har ingen resultater.

**Øvrige prediksjoner:** Tuberkulom har kun kasuistikker og én oversikt, noe som gir forsiktig støtte (BPaL/BPaLM-regimer med radiografisk bedring). Tuberkuløs ascites og kutan tuberkulose er mekanistisk plausible, men de koblede artiklene gjelder legemiddelbivirkninger, ikke effekt. Aviær tuberkulose har kun grafbasert prediksjon. Vulvovaginal candidiasis, fascioliasis, ureasyklusforstyrrelse og øsofageal candidiasis har ingen kjent mekanistisk kobling og fremstår sannsynligvis som nettverksartefakter.

---

## Evidens fra kliniske studier

Tabellen gjelder inaktiv tuberkulose, som er den eneste prediksjonen med registrerte studier. For bovin tuberkulose (rangert først) finnes for tiden ingen relaterte kliniske studier registrert.

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT06568484](https://clinicaltrials.gov/study/NCT06568484) | Fase 2/3 | Rekrutterer | 2530 | Åpen ikke-underlegenhetsstudie: 4 uker med bedaquilin mot standardregime for å forebygge tuberkulose hos hivpositive og nære kontakter. Ingen resultater ennå |
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Fase 2/3 | Aktiv, rekrutterer ikke | 288 | CRUSH-TB: 17-ukers regimer med bedaquilin, moxifloksacin og pyrazinamid pluss rifabutin eller delamanid mot standard seks måneders behandling ved lungetuberkulose (aktiv sykdom) |
| [NCT07069582](https://clinicaltrials.gov/study/NCT07069582) | Fase 1 | Ikke rekruttert ennå | 60 | Farmakokinetikk og utskillelse i morsmelk hos ammende kvinner etter enkeltdose av bl.a. bedaquilin. Gir ikke effektdata |

---

## Litteraturevidens

Utvalg fra inaktiv tuberkulose og tuberkulom (flest relevante). For bovin tuberkulose finnes kun én in vitro-studie ([27210281](https://pubmed.ncbi.nlm.nih.gov/27210281/), 2016, om MIC-bestemmelse for bedaquilin mot *M. tuberculosis* H37Rv).

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [28625141](https://pubmed.ncbi.nlm.nih.gov/28625141/) | 2018 | Oversikt | Recent Patents on Anti-Infective Drug Discovery | Bedaquilin som håp for kortere og bedre tuberkuloseregimer |
| [39766559](https://pubmed.ncbi.nlm.nih.gov/39766559/) | 2024 | Oversikt | Antibiotics (Basel) | Hemmere av F-ATP-syntase hos *M. tuberculosis*, bedaquilins målstruktur |
| [39301910](https://pubmed.ncbi.nlm.nih.gov/39301910/) | 2025 | Oversikt | Infectious Disorders Drug Targets | Nye leveringssystemer for bedaquilin; kan ramme persisterende/latent tuberkulose |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Oversikt | Zhejiang Da Xue Xue Bao Yi Xue Ban | Diagnostikk og behandling av latent tuberkuloseinfeksjon |
| [39887565](https://pubmed.ncbi.nlm.nih.gov/39887565/) | 2025 | Oversikt | Respirology | Oppdatering for klinikere om tuberkulose som sykdomsspekter |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Oversikt | Clin Pharmacol Ther | Behandling av tuberkulose, latent og aktiv |
| [34876446](https://pubmed.ncbi.nlm.nih.gov/34876446/) | 2021 | Kasuistikk | BMJ Case Reports | Steril tuberkuløs granulom hos pasient med XDR-TB behandlet med bedaquilin, pretomanid og linezolid |
| [42257795](https://pubmed.ncbi.nlm.nih.gov/42257795/) | 2026 | Kasuistikk | Infection | Radiografisk tilbakegang av antatt cerebellært tuberkulom under BPaLM-basert behandling |
| [40817574](https://pubmed.ncbi.nlm.nih.gov/40817574/) | 2025 | Kasuistikk | Am J Case Rep | Vellykket behandling av multiresistent tuberkuløs meningitt (uten bedaquilin i den oppgitte regimebeskrivelsen) |
| [33400226](https://pubmed.ncbi.nlm.nih.gov/33400226/) | 2021 | Oversikt | Acta Neurologica Belgica | Oppdatering om nevrotuberkulose |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002614 | Sirturo (Janssen-Cilag International N.V.) | Ikke oppgitt | Multiresistent tuberkulose (status: annullert) |

---

## Cytotoksisitet

Bedaquilin er et antimykobakterielt middel og ikke et antineoplastisk legemiddel. Denne seksjonen er derfor utelatt.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Blant de første 20 som er listet, er flere av alvorlighetsgrad **Major**: deksametason, klaritromycin, pikosulfat, polyetylenglykol (3350 med elektrolytter), dolasetron, palonosetron og natriumsulfat. Flere er **Moderate**, blant annet acarbose, famotidin, doksycyklin, pioglitazon, loperamid, bupropion, bisakodyl, kenodeoksykolsyre, minocyklin, oksandrolon, oksymetolon, tetracyklin og naltrekson.
- **Forhold som fremheves i evalueringen av inaktiv tuberkulose:** QT-forlengelse, hepatotoksisitet og høy belastning av legemiddelinteraksjoner. Aktiv tuberkulose må utelukkes før forebyggende behandling for å unngå resistensutvikling ved monoterapi. Begrenset penetrasjon til sentralnervesystemet er relevant for tuberkulom.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold for bovin tuberkulose (rangert først); Proceed with Guardrails for inaktiv tuberkulose**

**Begrunnelse:**
- Bovin tuberkulose har kun en indirekte in vitro-studie og ingen kliniske data, og *M. bovis* har dessuten naturlig resistens mot pyrazinamid, så anbefalingen er Hold.
- For inaktiv tuberkulose støtter fase 2/3-studien BREACH-TB (n = 2530) og CRUSH-TB bedaquilins rolle, og mekanismen er plausibel. Ingen av studiene har imidlertid resultater, så beslutningen forutsetter vern mot de nevnte risikoene. Tuberkulom er et forskningsspørsmål basert på kasuistikker. Prediksjonene for aviær tuberkulose, vulvovaginal candidiasis, fascioliasis, ureasyklusforstyrrelse og øsofageal candidiasis er Hold.

**For å gå videre kreves følgende:**
- Resultater fra BREACH-TB og CRUSH-TB
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra legemiddelmyndighetene (kritisk mangel som blokkerer sikkerhetsscreening)
- Overvåkingsplan for QT-forlengelse, leverfunksjon og legemiddelinteraksjoner
- Avklaring av markedsstatus i Norge, siden den eneste registrerte godkjenningen er annullert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

