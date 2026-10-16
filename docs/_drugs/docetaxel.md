---
layout: default
title: Docetaxel
parent: Kun modellprediksjon (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Docetaxel: predikert ny indikasjon Kvinnelig brystkarsinom (evidensnivå L5). Opprinnelig indikasjon: Kreft i hode og hals, ikke-småcellet lungekreft, adenokarsinom…"
monitor_inn: "DOCETAXEL"
predicted_indications: ["female breast carcinoma", "Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "small cell lung carcinoma", "primary pulmonary lymphoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "pulmonary blastoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma"]
---

# Docetaxel
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

# Docetaxel: Fra brystkreft, lungekreft og prostatakreft til kvinnelig brystkarsinom (utvidet bruk)

## Oppsummering

Docetaxel er et taksan-cellegiftmiddel som opprinnelig er godkjent mot kreft i hode og hals, ikke-småcellet lungekreft, adenokarsinom, prostatakreft, magekreft og brystkreft.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **kvinnelig brystkarsinom**, men dette er i realiteten en bruk som allerede er godkjent (on-label), ikke ekte repurposing.
Det foreligger **44 kliniske studier** og **20 publikasjoner** i de samlede dataene for denne indikasjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kreft i hode og hals, ikke-småcellet lungekreft, adenokarsinom, prostatakreft, magekreft, brystkreft |
| Predikert ny indikasjon | Kvinnelig brystkarsinom |
| TxGNN-prediksjonsscore | 99,90 % |
| Evidensnivå | L2 (konservativ vurdering; se merknad nedenfor) |
| Markedsstatus i Norge | Kun kansellerte tillatelser |
| Antall tillatelser | 3 (alle kansellert) |
| Anbefalt beslutning | Proceed with Guardrails |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de innsamlede dataene. Basert på kjent informasjon er docetaxel et taksan som stabiliserer mikrotubuli og blokkerer celledeling (mitose). Dette er den etablerte virkningsmekanismen ved brystkreft.

Brystkreft er allerede blant de godkjente indikasjonene, så prediksjonen bekrefter en kjent bruk fremfor å foreslå en ny. Flere fase 3-studier i de samlede dataene (blant annet NCT00003519, NCT00021255, NCT00003782, NCT00333775 og NCT00887536) omtaler docetaxel i brystkreft. De er likevel ikke vurdert for relevans i datagrunnlaget, og evidensnivået er derfor satt konservativt til L2.

Blant de øvrige predikerte indikasjonene finnes det begrenset støtte for Ewing-sarkom (L2, forskningsspørsmål) og rabdomyosarkom (L2, forskningsspørsmål). Småcellet lungekarsinom har L3-evidens, men støtten gjelder i hovedsak ikke-småcellet lungekreft. Resten (L4–L5) har kun saksrapporter eller ingen evidens, og bør settes på vent.

---

## Kliniske studier

Tabellen viser et utvalg av de mest relevante studiene (av 44 funnet).

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Fase 3 | Fullført | 2778 | Adjuvant doksorubicin/docetaxel versus doksorubicin/cyklofosfamid ved brystkreft med lymfeknutespredning eller høy risiko |
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Fase 3 | Fullført | 3222 | AC-T versus AC-TH versus TCH adjuvant ved HER2-positiv brystkreft |
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Fase 3 | Fullført | 5351 | Sammenligning av AC-T, AT og ATC adjuvant ved brystkreft med positive lymfeknuter |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Fase 3 | Fullført | 736 | Bevacizumab pluss docetaxel versus docetaxel pluss placebo ved HER2-negativ metastatisk brystkreft |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Fase 3 | Fullført | 1613 | TC pluss bevacizumab versus TC alene og versus TAC ved HER2-negativ brystkreft |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Fase 3 | Fullført | 2411 | Preoperativ AC med eller uten docetaxel ved operabel brystkreft |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Fase 2 | Fullført | 148 | Randomisert sammenligning av karboplatin og docetaxel ved metastatisk arvelig brystkreft |
| [NCT00003352](https://clinicaltrials.gov/study/NCT00003352) | Fase 2 | Fullført | 89 | Kombinasjonen doksorubicin, docetaxel og cyklofosfamid ved metastatisk eller lokalavansert brystkreft |
| [NCT00003953](https://clinicaltrials.gov/study/NCT00003953) | Fase 2 | Fullført | 39 | Preoperativ doseintensiv doksorubicin og deretter docetaxel |
| [NCT00025493](https://clinicaltrials.gov/study/NCT00025493) | Fase 2 | Avsluttet | 27 | Docetaxel som monoterapi hos eldre kvinner (≥70 år) med metastatisk brystkreft; avsluttet tidlig |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC-studiene: sammenligning av TC (docetaxel/cyklofosfamid) med taksan-antracyklin-regimer ved tidlig brystkreft |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Oversikt | Lancet | Taksaner er veletablerte komponenter i behandling av avansert bryst-, lunge- og eggstokkreft |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Oversikt | Breast Cancer Res Treat | Docetaxel-antracyklin-kombinasjoner ved metastatisk brystkreft |
| [18624687](https://pubmed.ncbi.nlm.nih.gov/18624687/) | 2008 | Oversikt | Expert Opin Drug Metab Toxicol | Erfaringer fra utviklingen av docetaxel |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Fase 2-studie | Oncology | Ukentlig docetaxel og gemcitabin som førstelinjebehandling ved metastatisk brystkreft |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Doseøkningsstudie | Tumori | Docetaxel og gemcitabin ved metastatisk brystkarsinom |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Fase 2-studie | Cancer | Kapecitabin med docetaxel og epirubicin ved tidligere ubehandlet avansert brystkreft |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospektiv studie | Anti-Cancer Drugs | Sammenheng mellom adjuvant docetaxelbasert kjemoterapi og lymfødem etter brystkreft |

---

## Markedsinformasjon for Norge

Alle tre tillatelsene er kansellert, og ingen er gyldige per i dag.

| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000073 | Taxotere | Ikke oppgitt | Kreft i hode og hals, ikke-småcellet lungekreft, adenokarsinom, prostatakreft, magekreft, brystkreft |
| EMEA/H/C/002539 | Docetaxel Accord | Ikke oppgitt | Kreft i hode og hals, ikke-småcellet lungekreft, adenokarsinom, prostatakreft, brystkreft |
| EMEA/H/C/002325 | Docetaxel Kabi | Ikke oppgitt | Kreft i hode og hals, ikke-småcellet lungekreft, adenokarsinom, prostatakreft, brystkreft |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonelt cytostatikum (taksan, mikrotubulistabiliserende) |
| Risiko for myelosuppresjon | Høy. Kunnskapsgrafen kobler docetaxel til nøytropeni, trombocytopeni, agranulocytose og anemi |
| Emetogenisitet | Lav til moderat (generell klasseinformasjon; ikke hentet fra dataene) |
| Overvåkingspunkter | Fullt blodbilde med differensialtelling, lever- og nyrefunksjon (bilirubin), nevrologisk status (perifer nevropati), væskeretensjon |
| Håndtering og beskyttelse | Må følge gjeldende regler for håndtering av cytostatika |

---

## Sikkerhetsvurderinger

Data om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Kontraindikasjoner fra kunnskapsgrafen** (TxGNN/PrimeKG, ikke hentet fra preparatomtalen): leversykdom, galleblæresykdom, trombocytopeni, nøytropeni, agranulocytose, perifer nevropati og andre nervesykdommer (inkludert nevritt og motorisk nevropati), anemi, hyperbilirubinemi (inkludert arvelig form og Gilberts syndrom), diaré, lungeødem, stomatitt og hjertetamponade.

**Legemiddelinteraksjoner** (100 interaksjoner funnet; utvalg):
- **Alvorlig:** klaritromycin
- **Moderat:** aprepitant, metronidazol, cimetidin, eliglustat, mikonazol, rolapitant, rosuvastatin, simvastatin, tinidazol, troglitazon
- **Mild:** deksametason, levofloksacin, prednisolon, prednison

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails**

**Begrunnelse:**
Docetaxel har en veletablert og godkjent bruk ved brystkreft, støttet av mange kliniske studier, blant annet flere store fase 3-studier. Evidensnivået er satt til L2 fordi fase 3-studiene ikke er vurdert for relevans i datagrunnlaget. Alle norske/europeiske tillatelser er imidlertid kansellert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves:**
- Hente og analysere preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Avklare hvorfor tillatelsene er kansellert og om det finnes gyldige markedsføringstillatelser i Norge
- Supplere data om virkningsmekanisme (MOA) fra DrugBank
- Gjennomgå og relevansvurdere fase 3-studiene for å bekrefte evidensnivå (mulig L1)
- Etablere en overvåkingsplan for myelosuppresjon, nevropati, leverfunksjon og interaksjoner (særlig med CYP3A4-hemmere som klaritromycin)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

