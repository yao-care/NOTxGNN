---
layout: default
title: Delamanid
parent: Kun modellprediksjon (L5)
nav_order: 122
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Delamanid: predikert ny indikasjon Inaktiv tuberkulose (evidensnivå L5). Opprinnelig indikasjon: Multiresistent tuberkulose"
monitor_inn: "DELAMANID"
predicted_indications: ["tuberculosis, bovine", "inactive tuberculosis", "tuberculosis, avian", "tuberculoma", "tuberculous ascites", "allergic urticaria", "cutaneous tuberculosis"]
---

# Delamanid
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

# Delamanid: Fra multiresistent tuberkulose til inaktiv tuberkulose

## Oppsummering

Delamanid er et antimykobakterielt legemiddel som opprinnelig er godkjent for behandling av multiresistent tuberkulose (MDR-TB).
TxGNN-modellen forutsier at det kan være effektivt mot **inaktiv tuberkulose** (rangert som den mest relevante prediksjonen ut fra tilgjengelig dokumentasjon), med **1 klinisk studie** og **20 publikasjoner** som indirekte støtter retningen.
Evidensen er begrenset: studien gjelder aktiv lungetuberkulose, og ingen publikasjoner undersøker delamanid direkte ved den foreslåtte indikasjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Multiresistent tuberkulose |
| Predikert ny indikasjon | Inaktiv tuberkulose (høyest rangerte prediksjon i datagrunnlaget er «tuberculosis, bovine» med score 99,91 %, men evidensen er sterkest for inaktiv tuberkulose) |
| TxGNN-prediksjonsscore | 99,91 % (inaktiv tuberkulose) |
| Evidensnivå | L2 (ifølge datagrunnlaget; merk at studien er pågående og gjelder aktiv TB, så reelt nivå er lavere) |
| Status på det norske markedet | Kun avregistrert |
| Antall godkjenninger | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Delamanid er imidlertid et nitro-dihydro-imidazooksazol-prodrug som aktiveres av det deazaflavin-avhengige nitroreduktaseenzymet Ddn i *Mycobacterium tuberculosis*. Det hemmer syntesen av mykolsyre i celleveggen. Aktiviteten omfatter også ikke-replikerende basiller, noe som konseptuelt er relevant for latent eller inaktiv tuberkulose.

Betegnelsen «inaktiv tuberkulose» er tvetydig: den kan bety latent infeksjon eller en behandlet, inaktiv sykdomstilstand. Den eneste identifiserte studien (NCT05766267) undersøker aktiv lungetuberkulose, så den tester ikke direkte behandling av latent eller inaktiv sykdom. Den høye prediksjonsscoren gjenspeiler i stor grad at legemidlet allerede har en TB-indikasjon.

Andre prediksjoner i datagrunnlaget er svakere:
- **Bovin tuberkulose** (*M. bovis*, score 99,91 %): Aktivitet er plausibel fordi arten tilhører *M. tuberculosis*-komplekset, men det finnes ingen delamanid-spesifikke data. Eneste artikkel gjelder genetisk diversitet og resistens hos *M. bovis*.
- **Tuberkulom** (CNS-manifestasjon): Patogenet er i prinsippet følsomt, men delamanids penetrasjon til sentralnervesystemet er ikke påvist.
- **Tuberkuløs ascites**: Plausibel aktivitet, men kun modellprediksjon og ukjent penetrasjon til bukhulevæske.
- **Kutan tuberkulose**: Mekanistisk plausibel, men de to artiklene gjelder legemiddelbivirkninger og ikke effekt.
- **Aviær tuberkulose**: Aktivitet er usannsynlig fordi *M. avium* mangler Ddn-veien som kreves for aktivering. Scoren skyldes trolig nettverksnærhet til andre TB-entiteter.
- **Allergisk urtikaria**: Ingen plausibel mekanistisk kobling. Prediksjonen er sannsynligvis en artefakt i kunnskapsgrafen.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Fase 2/3 | Aktiv, rekrutterer ikke | 288 | CRUSH-TB: sammenligner 17-ukers kortkurs-regimer (bedakvilin, moksifloksacin, pyrazinamid pluss enten rifabutin eller delamanid) med standard seks måneders behandling av lungetuberkulose. Forventet ferdig 2027. Resultater foreligger ikke. |

Det finnes ingen registrerte kliniske studier for de øvrige predikerte indikasjonene.

---

## Evidens fra litteraturen

Ingen av publikasjonene undersøker delamanid direkte ved de predikerte indikasjonene. Utvalget under er det mest relevante.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [29580819](https://pubmed.ncbi.nlm.nih.gov/29580819/) | 2018 | Oversikt | Lancet Infect Dis | Fremskritt innen nye legemidler, kortere behandlingsregimer og vertsrettet terapi ved TB |
| [33837535](https://pubmed.ncbi.nlm.nih.gov/33837535/) | 2021 | Oversikt | Clin Pharmacol Ther | Behandling av TB; skiller mellom latent og aktiv sykdom |
| [38003836](https://pubmed.ncbi.nlm.nih.gov/38003836/) | 2023 | Oversikt | Pathogens | Legemiddelresistent TB hos barn; bedakvilin og delamanid muliggjør tryggere regimer |
| [36982277](https://pubmed.ncbi.nlm.nih.gov/36982277/) | 2023 | Oversikt | Int J Mol Sci | Patogenese, gjeldende regimer og nye legemiddelmål ved TB |
| [33319660](https://pubmed.ncbi.nlm.nih.gov/33319660/) | 2021 | Oversikt | Curr Top Med Chem | Resistensmekanismer, nyere anti-TB-legemidler og vertsrettet terapi |
| [36915977](https://pubmed.ncbi.nlm.nih.gov/36915977/) | 2022 | Oversikt | J Zhejiang Univ Med Sci | Diagnostikk og behandling av latent tuberkuloseinfeksjon |
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Molekylær epidemiologi | BMC Genomics | Genetisk diversitet og legemiddelresistens hos *M. bovis*-isolater (indirekte evidens) |
| [33400226](https://pubmed.ncbi.nlm.nih.gov/33400226/) | 2021 | Oversikt | Acta Neurol Belg | Oppdatering om neurotuberkulose, inkludert tuberkulom (ingen delamanid-data) |
| [41696339](https://pubmed.ncbi.nlm.nih.gov/41696339/) | 2026 | Prekliniske studier | ACS Omega | Nye akirale 4-nitroimidazoler med antitubekulær aktivitet; delamanid nevnt som referanse |
| [24100880](https://pubmed.ncbi.nlm.nih.gov/24100880/) | 2013 | Oversikt | Curr Opin HIV AIDS | Legemiddelpipeline for TB, inkludert regimer for latent TB-infeksjon |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002552 | Deltyba (Otsuka Novel Products GmbH) | Ikke oppgitt | Multiresistent tuberkulose (status: avregistrert) |

---

## Sikkerhetsvurderinger

Ingen sikkerhetsdata er tilgjengelige i datagrunnlaget (advarsler, kontraindikasjoner og legemiddelinteraksjoner mangler). Se preparatomtalen (SPC) for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene har høy modellscore, men mangler direkte støtte: den eneste kliniske studien gjelder aktiv lungetuberkulose, og litteraturen er hovedsakelig generelle oversikter. Produktet er i tillegg avregistrert i Norge, og sikkerhetsdata og virkningsmekanisme mangler i datagrunnlaget.

**For å gå videre kreves:**
- Presisering av hva «inaktiv tuberkulose» betyr (latent infeksjon eller behandlet sykdom), og målrettede studier på denne populasjonen
- Resultater fra CRUSH-TB (NCT05766267)
- Sikkerhetsdata fra preparatomtalen (advarsler, kontraindikasjoner, interaksjoner, blant annet QT-forlengelse bør vurderes i preparatomtalen)
- Data om vevspenetrasjon (CNS, bukhule) dersom tuberkulom eller tuberkuløs ascites skal vurderes
- Avklaring av markedsstatus og tilgjengelighet i Norge etter avregistreringen
- Hentet og verifisert virkningsmekanisme fra DrugBank
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

