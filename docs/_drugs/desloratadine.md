---
layout: default
title: Desloratadine
parent: Kun modellprediksjon (L5)
nav_order: 124
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Desloratadine: predikert ny indikasjon Kuldeurticaria (evidensnivå L5). Opprinnelig indikasjon: Allergisk rinitt (helårs og sesongbetinget) og urticaria"
monitor_inn: "DESLORATADINE"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
---

# Desloratadine
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

# Desloratadin: Fra allergisk rinitt og urticaria til kuldeurticaria

## Oppsummering i én setning

Desloratadin er et antihistamin (H1-blokker) som opprinnelig er godkjent for behandling av allergisk rinitt (sesongbetinget og helårs) og urticaria.
TxGNN-modellen predikerer at legemidlet også kan være effektivt mot **kuldeurticaria**, og dette støttes foreløpig av **2 kliniske studier** og **6 publikasjoner**, hvorav 3 er randomiserte kontrollerte studier.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Allergisk rinitt (helårs og sesongbetinget) og urticaria |
| Predikert ny indikasjon | Kuldeurticaria |
| TxGNN-prediksjonsscore | 99,94 % |
| Evidensnivå | L1 (se merknad under) |
| Markedsstatus i Norge | Kun opphevede/trukne tillatelser |
| Antall tillatelser | 8 (alle opphevet) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med forbehold) |

*Merknad om evidensnivå:* Den automatiske vurderingen gir L1. Studiene som er funnet er imidlertid små fase 4-studier (30 og 33 pasienter), ikke fase 3-studier. Evidensen er derfor i praksis noe svakere enn et streng L1-nivå, men støttes av flere randomiserte, kontrollerte publikasjoner.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget for denne rapporten. Basert på kjent informasjon er desloratadin en selektiv perifer H1-reseptor invers agonist.

Kuldeurticaria er en mastcelle-mediert fysisk urticaria der histaminfrigjøring gir kvadler og rødme. H1-blokade rammer dermed sykdommens patofysiologi direkte. Økt dosering (opptil fire ganger standarddose) er en retningslinjeanbefalt strategi ved urticaria som ikke responderer på standarddose.

Legemidlet er allerede godkjent for urticaria, så dette er en utvidelse til en fysisk urticaria-undertype og ikke en helt ny mekanisme.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT01444196](https://clinicaltrials.gov/study/NCT01444196) | Fase 4 | Fullført | 30 | Dobbeltblind dose-eskaleringsstudie (5, 10 og 20 mg) for å finne dosen som hemmer symptomer ved ervervet kuldeurticaria |
| [NCT00600847](https://clinicaltrials.gov/study/NCT00600847) | Fase 4 | Fullført | 33 | Randomisert, dobbeltblind, placebokontrollert crossover-studie av 5 mg vs. 20 mg desloratadin på eksperimentelt fremkalte urticarialesjoner |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [19201016](https://pubmed.ncbi.nlm.nih.gov/19201016/) | 2009 | RCT | J Allergy Clin Immunol | Høydose desloratadin ga mindre kvadelvolum og bedre kuldeprovokasjonsterskel enn standarddose ved ervervet kuldeurticaria (randomisert, placebokontrollert crossover) |
| [22242678](https://pubmed.ncbi.nlm.nih.gov/22242678/) | 2012 | RCT | Br J Dermatol | Dose-eskalering av H1-antihistamin og måling av kritisk temperaturterskel ved kuldeurticaria |
| [14754651](https://pubmed.ncbi.nlm.nih.gov/14754651/) | 2004 | RCT | J Dermatol Treat | 5 mg desloratadin i 4 dager hemmet kuldeurticaria hos 12 pasienter, testet med isbiter |
| [15516152](https://pubmed.ncbi.nlm.nih.gov/15516152/) | 2004 | Oversikt | Drugs | Oversikt over årsaker, behandling og fremtidige alternativer ved kronisk urticaria |
| [19032340](https://pubmed.ncbi.nlm.nih.gov/19032340/) | 2008 | Oversikt | Allergy | Ebastin ved allergisk rinitt og kronisk idiopatisk urticaria (annet legemiddel, indirekte relevans) |
| [38025339](https://pubmed.ncbi.nlm.nih.gov/38025339/) | 2023 | Kasuistikk | Qatar Med J | Kuldeindusert urticaria etter anafylaksi ved maurbitt |

---

## Markedsinformasjon for Norge

Alle åtte tillatelser er registrert som opphevet. Per i dag finnes ingen gyldige tillatelser.

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002310 | Dasselta | – | Allergisk rinitt (helårs og sesongbetinget), urticaria |
| EMEA/H/C/000314 | Neoclarityn | – | Allergisk rinitt (helårs og sesongbetinget), urticaria |
| EMEA/H/C/002435 | Desloratadine Actavis | – | Allergisk rinitt (helårs og sesongbetinget), urticaria |
| EMEA/H/C/002404 | Desloratadine ratiopharm | – | Allergisk rinitt (helårs og sesongbetinget), urticaria |
| EMEA/H/C/002419 | Desloratadine Teva | – | Allergisk rinitt (helårs og sesongbetinget) |

---

## Sikkerhetsvurderinger

- **Mulige kontraindikasjoner (fra kunnskapsgraf, ikke preparatomtale):** Kunnskapsgrafen knytter desloratadin til følgende tilstander: hypertensjon, nyresykdom, leversykdom, galleblæresykdom, diabetes mellitus, diabetisk ketoacidose, benign prostatahyperplasi, koronarsykdom, aterosklerose, trangvinklet glaukom, hyperthyreose (Graves sykdom, tyreotoksikose) og pyoureter. Dette er ikke bekreftet av preparatomtalen og bør verifiseres.
- **Legemiddelinteraksjoner:** Totalt 100 mulige interaksjoner er registrert, men alvorlighetsgrad er ukjent for dem alle. Eksempler: kalsitriol, fentermin, pantoprazol, doksycyklin, klotrimazol, morfin, metformin, omeprazol, rosiglitazon, lansoprazol, cimetidin, vankomycin, simvastatin, epinefrin, hydrokortison og kaliumklorid.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Andre predikerte indikasjoner (kort)

| Predikert indikasjon | Score | Evidensnivå | Beslutning |
|------|------|------|------|
| Sykdom i nesehulen | 99,87 % | L4 | Hold. Overlapper trolig med eksisterende indikasjon; kun dyrestudier. |
| Akutt laryngofaryngitt | 99,85 % | L5 | Hold. Ingen mekanistisk begrunnelse eller evidens. |
| Refraktær atopisk dermatitt | 99,75 % | L5 | Hold. Biologisk plausibelt, men begrenset nytte av H1-blokkere. |
| Atopisk IgE-respons | 99,64 % | L5 | Hold. Et fenotypetrekk, ikke en behandlingsbar sykdom. |
| Rosacea-konjunktivitt | 99,40 % | L5 | Hold. Begrenset mekanistisk relevans. |

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med forbehold)**

**Begrunnelse:**
Kuldeurticaria har en klar mekanistisk begrunnelse, to fullførte randomiserte fase 4-studier og flere RCT-er som viser effekt av desloratadin, særlig ved økt dose. Studiene er imidlertid små, og legemidlet har ingen gyldig tillatelse i Norge i dag.

**For å gå videre kreves følgende:**
- Gjennomgang av preparatomtale (advarsler og kontraindikasjoner), som mangler i datagrunnlaget
- Detaljerte data om virkningsmekanisme
- Avklaring av regulatorisk status, siden alle norske tillatelser er opphevet
- Sikkerhetsvurdering av høydosebruk (opptil fire ganger standarddose), særlig hos pasienter med tilstandene nevnt over
- Større studier eller en systematisk oversikt for å bekrefte effekt og optimal dosering
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

