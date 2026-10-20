---
layout: default
title: Caffeine
parent: Kun modellprediksjon (L5)
nav_order: 77
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Caffeine: predikert ny indikasjon Nesehulesykdom (nasal cavity disease) (evidensnivå L5). Opprinnelig indikasjon: Apné"
monitor_inn: "Caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "acute laryngopharyngitis", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
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

# Koffein: Fra apné til nesehulesykdom

## Enkel oppsummering

Koffein er godkjent for behandling av apné (pustestopp) hos premature spedbarn. TxGNN-modellen forutsier at det kan ha effekt ved **nesehulesykdom** (nasal cavity disease), med en prediksjonsscore på 99,91 %. Evidensen er svært svak: det finnes **ingen kliniske studier** og bare **3 publikasjoner**, hvorav ingen viser behandlingseffekt på nesehulesykdom.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Apné |
| Predikert ny indikasjon | Nesehulesykdom (nasal cavity disease) |
| TxGNN-prediksjonsscore | 99,91 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukne godkjenninger (ingen gyldige) |
| Antall godkjenninger | 2 (begge trukket tilbake) |
| Anbefalt beslutning | Hold |

Merk: Godkjenningsnumrene i dataene er EMA-numre (EMEA/H/C/...), ikke nasjonale norske numre.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelige i datagrunnlaget. Ut fra kjent farmakologi er koffein en adenosinreseptorantagonist (A1, A2A, A2B, A3) og fosfodiesterasehemmer. Det påvirker også kalsiumfrigjøring via IP3R1 og ryanodinreseptorene (RyR1–3).

Koblingen mellom apné og nesehulesykdom er svak. Apné behandles via stimulering av respirasjonssenteret, mens nesehulesykdom er et lokalt slimhinne- eller anatomisk problem. Den eneste mekanistiske tråden er at bitre smaksreseptorer (TAS2R) i luftveisepitelet, inkludert nesehulen, responderer på koffein og kan modulere medfødt forsvar. Dette er en hypotese på prekliniske nivå. Den eneste nesespesifikke studien gjelder nasal levering av koffein for kognisjon (en studie av administrasjonsvei, ikke behandling av nesesykdom).

---

## Evidens fra kliniske studier

Det er for tiden ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Oversiktsartikkel | Pharmacol Ther | Beskriver bitre smaksreseptorer (T2R) i luftveiene, inkludert nesehulen, og deres farmakologi. Hypotesenivå |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Preklinisk formuleringsstudie | Curr Drug Deliv | Termosensitiv nasal in situ-gel med koffein for bedre kognisjon etter søvnmangel. Gjelder administrasjonsvei, ikke nesesykdom |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Dyrestudie | Cancer Res | Svart te og koffein hemmet lungekarsinogenese hos rotter. Ikke relevant for nesehulesykdom |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001014 | Peyona (tidligere Nymusa) | Ikke oppgitt | Apné (trukket) |
| EMEA/H/C/005435 | Gencebok | Ikke oppgitt | Apné (trukket) |

---

## Sikkerhetsvurderinger

**Kontraindikasjoner fra kunnskapsgraf (ikke fra preparatomtale):** TxGNN-kunnskapsgrafen (PrimeKG) knytter koffein til følgende tilstander som mulige kontraindikasjoner. Dette er ikke bekreftet av godkjent produktinformasjon:
- Hjerte- og karsykdommer: hypertensjon, ortostatisk hypotensjon, posturalt ortostatisk takykardisyndrom, multisystematrofi, langt QT-syndrom (også familiært)
- Nevrologiske og psykiske lidelser: epilepsi, søvnløshet, angstlidelse, nevrotisk lidelse, dystymi
- Lunge: kols (inkludert alvorlig tidlig debuterende)
- Mage-tarm, lever og galle: magesår, ulcerøs sykdom i fordøyelseskanalen, betennelsessykdom i tarm, pankreatitt, leversvikt, leversykdom, gallblæresykdom
- Nyre og urinveier: nyresykdom, pyoureter
- Stoffskifte og endokrine: arvelig porfyri, porfyrisykdommer, hypotyreose (inkludert myxødem og medfødt)
- Blod: trombocytopeni

**Legemiddelinteraksjoner:** Det er ikke identifisert klassiske legemiddel-legemiddelinteraksjoner. De registrerte oppføringene (8) gjelder koffeins farmakologiske mål: adenosinreseptorene A1, A2A, A2B og A3, samt IP3R1 og RyR1, RyR2 og RyR3.

Se preparatomtalen for fullstendig sikkerhetsinformasjon, siden omtalen med advarsler og kontraindikasjoner ikke var tilgjengelig i datagrunnlaget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
- Prediksjonen for nesehulesykdom bygger kun på modellscore (L5). Det finnes ingen kliniske studier, og litteraturen viser ingen terapeutisk effekt. Koffein har heller ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves:**
- Hent og gjennomgå preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel for sikkerhetsscreening
- Hent mekanismedata (MOA) fra DrugBank
- Prekliniske studier som undersøker koffein ved nesehulesykdom (f.eks. via TAS2R i nesepitel)
- Avklare hvilken nesehulesykdom som menes, og om lokal (nasal) administrasjon er aktuelt

**Andre prediksjoner med noe sterkere støtte (til informasjon):** Hypnisk hodepine (L4, trinn S1, anbefalt som «Research Question»), nevralgi og trigeminal autonom cefalalgi (begge L4). For hypnisk hodepine beskriver oversiktsartikler koffein som førstelinjebehandling basert på kasuistikker og små serier, uten randomiserte kontrollerte studier. Medikamentoverbrukshodepine er en relevant sikkerhetsrisiko.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

