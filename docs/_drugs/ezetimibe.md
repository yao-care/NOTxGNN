---
layout: default
title: Ezetimibe
parent: Høy evidens (L1-L2)
nav_order: 170
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-15
description: "Ezetimibe: predikert ny indikasjon Hyperlipoproteinemi (evidensnivå L1). Opprinnelig indikasjon: Hyperkolesterolemi"
---

# Ezetimibe
{: .fs-9 }

Evidensnivå: **L1** | Predikerte indikasjoner: **4** stk.
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

# Ezetimib: Fra hyperkolesterolemi til hyperlipoproteinemi

## Oppsummering i én setning

Ezetimib er et kolesterolsenkende legemiddel som opprinnelig brukes mot hyperkolesterolemi og dyslipidemi.
TxGNN-modellen forutsier at det kan være effektivt ved **hyperlipoproteinemi**, med **ca. 40 kliniske studier** og **ca. 20 publikasjoner** i dataene som er samlet inn for denne rapporten.
Merk at den predikerte indikasjonen i stor grad overlapper med den eksisterende godkjente bruken, så dette er ikke en reell ny anvendelse (repurposing).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hyperkolesterolemi; dyslipidemi |
| Predikert ny indikasjon | Hyperlipoproteinemi |
| TxGNN-prediksjonsscore | 99,63 % |
| Evidensnivå | L1 |
| Markedsstatus i Norge | Kun avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med forbehold) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er ikke tilgjengelige i de innsamlede dataene. Basert på kjent informasjon hemmer ezetimib NPC1L1-mediert opptak av kolesterol i tarmen og senker dermed LDL-kolesterol. Dette retter seg direkte mot den lipidforstyrrelsen som kjennetegner hyperlipoproteinemi.

Den predikerte indikasjonen er i praksis den samme som legemidlets opprinnelige godkjente bruk (hyperkolesterolemi/dyslipidemi). Den høye scoren (0,996) er derfor i tråd med eksisterende klinisk bruk, og ikke et funn av en ny indikasjon.

Modellen foreslo også tre andre sykdommer. Disse er omtalt kort nedenfor:

- **Familiær hyperkolesterolemi (score 99,38 %, L1):** Ezetimib gir additiv LDL-senkning oppå statiner, og flere fase 3-studier har testet det direkte ved heterozygot og homozygot FH. Også dette er etablert bruk. Effekten ved homozygot FH forventes å være mer beskjeden fordi LDL-reseptorfunksjonen er begrenset.
- **Hyperkolesterolemi ved kolesterol-7α-hydroksylase-mangel (score 99,25 %, L4, Hold):** Mekanismen er plausibel, men den eneste publikasjonen er prekliniske musedata om NPC1L1 og gallesyrer. Det finnes ingen kliniske studier, og tilstanden er svært sjelden.
- **Kolesterolester-transferprotein (CETP)-mangel (score 99,09 %, L5, Hold):** Tilstanden gir forhøyet HDL-kolesterol og krever vanligvis ikke LDL-senkende behandling. Koblingen er kun en prediksjon fra kunnskapsgrafen, og den høye scoren gjenspeiler trolig delte nettverkskoblinger i lipidmetabolismen.

---

## Evidens fra kliniske studier

De mest relevante studiene for hyperlipoproteinemi:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Fase 4 | Fullført | 40 | Åpen randomisert sammenligning av ezetimib som tillegg til statin mot statin alene ved hyperkolesterolemi |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Fase 3 | Fullført | 511 | Evolokumab mot ezetimib ved statinintoleranse (muskelrelaterte bivirkninger); ezetimib er komparator |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Fase 4 | Fullført | 127 | Ezetimib/rosuvastatin kombinert med kandesartan/amlodipin ved hypertensjon og hyperlipidemi |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Fase 3 | Avsluttet | 49 | Åpen behandlingsbruksstudie av ezetimib 10 mg/dag ved homozygot FH eller sitosterolemi |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | Ikke relevant (observasjonsstudie) | Fullført | 1794 | 52 ukers japansk legemiddelovervåking av Zetia (ikke randomisert) |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Fase 3 | Fullført | 1220 | Ezetimib/simvastatin sammen med niacin ved hyperlipidemi type IIa/IIb |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Fase 3 | Fullført | 576 | Fenofibrat og ezetimib samtidig ved blandet hyperlipidemi |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Fase 3 | Fullført | 611 | Ezetimib/simvastatin og fenofibrat ved blandet hyperlipidemi |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Fase 3 | Fullført | 720 | ENHANCE: ezetimib + simvastatin mot simvastatin alene ved heterozygot FH, mål på aterosklerose i halsarterien |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | Ikke relevant (observasjonsstudie) | Fullført | 4105 | Overvåking av sikkerhet og effekt av ezetimib hos filippinske pasienter |

For familiær hyperkolesterolemi finnes i tillegg fase 3-studiene [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) (n=50, HoFH, fullført), [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) (n=44, langtidssikkerhet) og [NCT00867165](https://clinicaltrials.gov/study/NCT00867165) (n=138, placebokontrollert hos barn 6–10 år).

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | Oral PCSK9-hemmer (enlicitid) ved heterozygot FH; ezetimib er bakgrunnsbehandling |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | Evolokumab (RUTHERFORD-2) ved heterozygot FH som ikke når målverdier på statin ± ezetimib |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | Inklisiran ved homozygot FH (ORION-5) |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | Kohort | Lancet | Global erfaring med homozygot FH |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Oversikt | Molecular Medicine Reports | Fremskritt innen legemidler mot hyperlipidemi |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Oversikt | J Am Coll Cardiol | Nye og kommende LDL-senkende behandlinger oppå statiner, ezetimib og PCSK9-hemmere |
| [30702994](https://pubmed.ncbi.nlm.nih.gov/30702994/) | 2019 | Oversikt | Circulation Research | Kolesterolsenkende legemidler |
| [25939291](https://pubmed.ncbi.nlm.nih.gov/25939291/) | 2015 | Oversikt | Cardiology Clinics | Familiær hyperkolesterolemi; ezetimib nevnt blant LDL-senkende behandlinger |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Oversikt | Nature Reviews Disease Primers | Familiær hyperkolesterolemi: genetikk, diagnostikk og behandling |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Konsensusuttalelse | European Heart Journal | FH er underdiagnostisert og underbehandlet; veiledning til klinikere |

Mesteparten av litteraturen er oversikter og studier av andre legemidler (PCSK9-hemmere) der ezetimib er bakgrunnsbehandling. Det finnes få publikasjoner som direkte tester ezetimib alene.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004959 | Nustendi | Ikke oppgitt | Hyperkolesterolemi; dyslipidemi |

Tillatelsen er **avregistrert**. Det finnes ingen gyldige tillatelser i de innsamlede dataene, så tilgjengeligheten i Norge må verifiseres.

---

## Sikkerhetsvurderinger

- **Mulige kontraindikasjoner/risikotilstander (fra kunnskapsgrafen, ikke fra preparatomtale):** pankreatitt, leversykdom, galleblæresykdom, myopati, muskelsykdom, skjelettmuskelsykdom, familiær periodisk paralyse, rusmiddelmisbruk/avhengighet, rabdomyolyse og nodulær fasciitt.
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Av de som er klassifisert, er følgende av moderat alvorlighetsgrad:
  - Kenodeoksykolsyre
  - Eluksadolin
  - Rosuvastatin
  - Simvastatin

  Flere andre (f.eks. kalsitriol, pantoprazol, glimepirid, metformin, omeprazol, vankomycin) har ukjent alvorlighetsgrad.

Informasjon om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med forbehold)** for hyperlipoproteinemi og familiær hyperkolesterolemi. **Hold** for kolesterol-7α-hydroksylase-mangel og CETP-mangel.

**Begrunnelse:**
- Evidensen er sterk (L1) fordi flere fullførte fase 3-studier støtter ezetimib ved hyperlipidemi og FH. Men dette er etablert bruk og ikke ny repurposing. De to sjeldne tilstandene mangler klinisk evidens og er kun modellprediksjoner.

**For å gå videre kreves:**
- Verifisere tilgjengelighet og markedsføringstillatelse i Norge, siden den eneste registrerte tillatelsen er avregistrert
- Hente advarsler og kontraindikasjoner fra preparatomtalen (kritisk datamangel)
- Hente detaljerte data om virkningsmekanisme fra DrugBank
- Plan for overvåking av lever- og muskelsikkerhet og av interaksjoner med statiner og fibrater
- Dersom de sjeldne indikasjonene skal følges opp, kreves klinisk eller translasjonell evidens først
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

