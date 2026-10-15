---
layout: default
title: Pazopanib
parent: Kun modellprediksjon (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: Fra nyrecellekarsinom til uklassifisert nyrecellekarsinom

## Kort oppsummering

Pazopanib er en multitarget tyrosinkinasehemmer (VEGFR/PDGFR/c-Kit) som opprinnelig brukes til behandling av nyrecellekarsinom.
TxGNN-modellen forutsier at legemidlet kan være effektivt ved **uklassifisert nyrecellekarsinom** (høyest rangerte indikasjon med litteraturgrunnlag),
med **6 publikasjoner** (ingen registrerte kliniske studier) som for tiden støtter denne retningen.
Den mest modne dokumentasjonen i de dataene som er sammenstilt for denne rapporten gjelder imidlertid **liposarkom** og **dermatofibrosarcoma protuberans (DFSP)**, og disse omtales også nedenfor.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Nyrecellekarsinom (Carcinoma, Renal Cell) |
| Predikert ny indikasjon | Renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions (rangert nr. 1 av modellen; ingen studier eller litteratur) |
| TxGNN-prediksjonsscore | 99,63 % |
| Evidensnivå | L5 for rangert nr. 1 (kun modellprediksjon). Uklassifisert nyrecellekarsinom: L3. Liposarkom og DFSP: L2 |
| Markedsstatus i Norge | Kun opphevet (cancelled only) |
| Antall godkjenninger | 1 (opphevet) |
| Anbefalt beslutning | Hold for rangert nr. 1. Proceed with Guardrails for liposarkom og DFSP |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte mekanismedata (MOA) er for tiden ikke tilgjengelige i datagrunnlaget. Pazopanib er likevel kjent som en multitarget tyrosinkinasehemmer som blokkerer VEGFR, PDGFR og c-Kit. Effekten ved nyrecellekarsinom er etablert, og mekanismen er antiangiogen og antiproliferativ.

**Xp11.2-translokasjons-RCC (rangert nr. 1):** Dette er en sjelden RCC-undertype med biologi som delvis overlapper med angiogen signalering ved RCC. Prediksjonen er plausibel, men ingen studier eller litteratur er tilgjengelig, så koblingen bygger kun på modellen.

**Uklassifisert nyrecellekarsinom:** VEGFR/PDGFR-hemming er etablert ved klarcellet RCC og kan sannsynligvis utvides til ikke-klarcellet og uklassifisert RCC. Litteraturen består av en enarmet fase 2-studie og flere retrospektive og virkelighetsnære serier. Uklassifisert RCC er heterogen og analyseres vanligvis sammen med andre ikke-klarcellede undertyper, så evidensen er ikke spesifikk.

**Liposarkom:** Pazopanibs antiangiogene og PDGFR-rettede aktivitet er relevant for bløtvevssarkom. Adipocytiske sarkomer ble imidlertid ekskludert fra PALETTE-studien, og liposarkom var et bemerkelsesverdig unntak. Fase 2-data gir direkte, men beskjedne og ikke-randomiserte holdepunkter. Det dedifferensierte subtypen krever særlig forsiktighet.

**DFSP:** Sykdommen drives av COL1A1-PDGFB-fusjonen, som gir konstitutiv PDGFR-beta-aktivering. Pazopanib hemmer PDGFR, noe som gir et sterkt mekanistisk grunnlag, særlig etter imatinibresistens.

**Øvrige prediksjoner** (rangert nr. 2, 5, 6, 7 og 9: nyrecellekarsinom assosiert med nevroblastom, barnenyrecellekarsinom, ovarielt myksoid liposarkom, hjertefibrosarkom og nyrefibrosarkom) har ingen studier eller litteratur. Flere av dem er svært sjeldne og kan være ontologi-artefakter, og høy score gjenspeiler trolig den overordnede RCC-godkjenningen.

---

## Evidens fra kliniske studier

Ingen registrerte kliniske studier for uklassifisert nyrecellekarsinom. Nedenfor vises studier for de to predikerte indikasjonene med sterkest evidens.

### Liposarkom

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) | Fase 2 | Fullført | 42 | Pazopanib som monoterapi ved inoperabelt eller metastatisk liposarkom |
| [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) | Fase 2 | Fullført | 52 | Aktivitet og tolerabilitet ved avansert/metastatisk liposarkom etter residiv (tittelen er avkortet, populasjon bør verifiseres) |
| [NCT01532687](https://clinicaltrials.gov/study/NCT01532687) | Fase 2 | Fullført | 54 | Randomisert, dobbeltblind: gemcitabin med eller uten pazopanib ved refraktært bløtvevssarkom |
| [NCT02357810](https://clinicaltrials.gov/study/NCT02357810) | Fase 2 | Fullført | 178 | Pazopanib pluss oral topotekan ved metastatisk, inoperabelt bløtvevs- og beinsarkom |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Fase 2/3 | Fullført | 140 | Neoadjuvant, randomisert: strålebehandling ± kjemoterapi ± pazopanib ved ikke-rabdomyosarkom bløtvevssarkom |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Fase 1/2 | Rekrutterer | 139 | Risikotilpasset studie med vedlikeholdsbehandling med pazopanib ved ikke-rabdomyosarkom bløtvevssarkom |

### Dermatofibrosarcoma protuberans (DFSP)

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) | Fase 2 | Avsluttet tidlig | 23 | Pazopanib ved inoperabelt, lokalavansert DFSP. Direkte relevant, men begrenset av tidlig avslutning |
| [NCT02601209](https://clinicaltrials.gov/study/NCT02601209) | Fase 1/2 | Avsluttet tidlig | 151 | MLN0128 (sapanisertib) versus pazopanib ved avansert sarkom. Pazopanib er komparator |
| [NCT02180867](https://clinicaltrials.gov/study/NCT02180867) | Fase 2/3 | Fullført | 140 | Bred bløtvevssarkompopulasjon, DFSP-spesifikke data er usikre |
| [NCT06239272](https://clinicaltrials.gov/study/NCT06239272) | Fase 1/2 | Rekrutterer | 139 | Bred bløtvevssarkompopulasjon, ingen resultater ennå |

### Fibroblastisk neoplasme

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) | Fase 2 | Fullført | 96 | Pazopanib som monoterapi ved inoperabel eller metastatisk solitær fibrøs tumor og ekstraskjelettalt myksoid kondrosarkom |

---

## Litteraturevidens

### Uklassifisert nyrecellekarsinom

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/) | 2018 | Enarmet fase 2 | Cancer Res Treat | Effekt og sikkerhet av pazopanib ved metastatisk ikke-klarcellet RCC |
| [28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/) | 2017 | Retrospektiv multisenter | Clin Genitourin Cancer | PANORAMA: førstelinje pazopanib ved ikke-klarcellet RCC i Italia |
| [27568124](https://pubmed.ncbi.nlm.nih.gov/27568124/) | 2017 | Retrospektiv kohort | Clin Genitourin Cancer | Utfall ved metastatisk ikke-klarcellet RCC behandlet med pazopanib |
| [31921344](https://pubmed.ncbi.nlm.nih.gov/31921344/) | 2019 | Virkelighetsnær kohort | Ecancermedicalscience | Sunitinib og pazopanib sammenlignet ved ikke-klarcellet og sarkomatoid RCC |
| [41558869](https://pubmed.ncbi.nlm.nih.gov/41558869/) | 2026 | Retrospektiv kohort | Eur Urol Oncol | Førstelinjebehandlinger ved metastatisk ikke-klarcellet RCC (IMDC) |
| [30268423](https://pubmed.ncbi.nlm.nih.gov/30268423/) | 2019 | Kohort/serie | Clin Genitourin Cancer | Metastatisk karsinom med ukjent primærsted og RCC-trekk, behandlet med målrettet terapi |

### Liposarkom

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | 2019 | Fase 2 | Expert Opin Investig Drugs | Pazopanib ved avansert liposarkom av intermediær/høy grad |
| [28844815](https://pubmed.ncbi.nlm.nih.gov/28844815/) | 2017 | Kommentar | Lancet Oncol | Pazopanib ved avansert liposarkom |
| [34050255](https://pubmed.ncbi.nlm.nih.gov/34050255/) | 2021 | Fase 2 | Br J Cancer | Pazopanib med oral topotekan ved bløtvevs- og beinsarkom |
| [27751846](https://pubmed.ncbi.nlm.nih.gov/27751846/) | 2016 | RCT (fase 2) | Lancet Oncol | REGOSARC: regorafenib (beslektet TKI) ved bløtvevssarkom |
| [30060824](https://pubmed.ncbi.nlm.nih.gov/30060824/) | 2018 | Prekliniske data | Tissue Cell | Pazopanib ga regresjon i PDGFRA-amplifisert pleomorft liposarkom i musemodell |
| [32026050](https://pubmed.ncbi.nlm.nih.gov/32026050/) | 2020 | Oversikt | Curr Treat Options Oncol | Systemiske behandlingsalternativer ved dedifferensiert liposarkom |
| [35609512](https://pubmed.ncbi.nlm.nih.gov/35609512/) | 2022 | Oversikt | Oncol Res Treat | Etablerte og eksperimentelle behandlinger ved avansert liposarkom |

### Dermatofibrosarcoma protuberans (DFSP)

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/) | 2021 | Fase 2 | J Invest Dermatol | Multisenterstudie av pazopanib ved inoperabelt DFSP |
| [34066400](https://pubmed.ncbi.nlm.nih.gov/34066400/) | 2021 | Retrospektiv | Cancers | Langtidsutfall etter neoadjuvant TKI (imatinib eller pazopanib) ved lokalavansert DFSP |
| [27988943](https://pubmed.ncbi.nlm.nih.gov/27988943/) | 2017 | Kasuistikk | J Dermatol | Delvis respons på pazopanib ved metastatisk fibrosarkomatøst DFSP |
| [37592448](https://pubmed.ncbi.nlm.nih.gov/37592448/) | 2023 | Prekliniske data | Cancer Sci | Pazopanib identifisert som mulig hemmer av COL1A1-PDGFB-fusjonen |
| [37610680](https://pubmed.ncbi.nlm.nih.gov/37610680/) | 2023 | Prekliniske data | Hum Cell | Multiomikk- og ex vivo-modell av imatinibresistent DFSP |
| [22510939](https://pubmed.ncbi.nlm.nih.gov/22510939/) | 2012 | Oversikt | Curr Opin Oncol | Behandling av DFSP med PDGFR-hemmere |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001141 | Votrient (Novartis Europharm Limited) | Ikke oppgitt | Nyrecellekarsinom (status: opphevet) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (multitarget tyrosinkinasehemmer), ikke konvensjonelt cytotoksisk |
| Myelosuppresjonsrisiko | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisk klassifisering | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget. Kunnskapsgrafen peker på leverskade, hypertensjon, QT-forlengelse og proteinuri, som det er naturlig å overvåke |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetsmomenter

**Kontraindikasjoner fra kunnskapsgrafen (PrimeKG, ikke preparattekst):** Sykdommer som kunnskapsgrafen knytter til kontraindikasjon, omfatter blant annet:
- Hjerte- og kar: hypertensjon, langt QT-syndrom (inkludert familiær form), torsades de pointes, hjerteinfarkt, koronar trombose
- Lever: leversvikt, legemiddelindusert leverskade, hyperbilirubinemi (inkludert Gilberts syndrom)
- Skjoldbruskkjertel: hypotyreose, myksødem, medfødt hypotyreose
- Elektrolytt/metabolsk: kaliummangel, hyperkalsemi, nefrokalsinose, forstyrrelser i fosformetabolismen
- Øvrige: diarésykdom, aktivt magesår, intrakraniell blødning, pankreatitt, proteinuri, hemoglobinopati

Dette er modellbaserte koblinger og må bekreftes mot godkjent preparatomtale.

**Legemiddelinteraksjoner (100 registrert, de viktigste vist):**
- **Alvorlige (Major):** famotidin, ranitidin, cimetidin, omeprazol, esomeprazol, rabeprazol, deksansoprazol (syrehemmere), klaritromycin, dolasetron
- **Moderate:** pioglitazon, loperamid, aprepitant, deksametason, budesonid, bisakodyl, magnesiumoksid, polyetylenglykol, saksagliptin, eliglustat

Syrehemmende midler er særlig relevante, siden de kan påvirke opptaket av pazopanib.

Detaljerte advarsler og kontraindikasjoner fra preparattekst er ikke tilgjengelige. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold for Xp11.2-translokasjons-RCC og uklassifisert RCC (forskningsspørsmål). Proceed with Guardrails for liposarkom og DFSP.**

**Begrunnelse:**
- Den høyest rangerte indikasjonen (Xp11.2-RCC) har kun modellprediksjon (L5) uten studier eller litteratur. Uklassifisert RCC har kun ikke-randomiserte data (L3) som ikke er spesifikke for undertypen.
- Liposarkom og DFSP har fase 2-data (L2), men studiene er små, enarmede eller avsluttet tidlig, og pazopanib er kun opphevet i Norge (ingen gyldig lisens).

**For å gå videre kreves følgende:**
- Preparattekstens advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening). De bør hentes fra DMP.
- Detaljerte mekanismedata (MOA), for eksempel fra DrugBank
- Undertypespesifikke resultater for uklassifisert RCC, liposarkom (spesielt dedifferensiert) og DFSP, siden flere studietitler er avkortet og populasjonene ikke er verifisert
- Avklaring av regulatorisk status i Norge, siden eneste lisens er opphevet
- Plan for sikkerhetsovervåking (blodtrykk, lever, QT, proteinuri) og vurdering av interaksjoner med syrehemmere
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

