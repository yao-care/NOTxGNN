---
layout: default
title: Risperidone
parent: Kun modellprediksjon (L5)
nav_order: 363
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Risperidone: predikert ny indikasjon Familiær horisontal blikkparese med progressiv skoliose (evidensnivå L5). Opprinnelig indikasjon: Schizofreni"
monitor_inn: "RISPERIDONE"
predicted_indications: ["gaze palsy, familial horizontal, with progressive scoliosis", "amelocerebrohypohidrotic syndrome", "Phelan-McDermid syndrome", "trichotillomania", "major affective disorder"]
---

# Risperidone
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Risperidon: Fra schizofreni til Familiær horisontal blikkparese med progressiv skoliose
{: .text-alpha }

## Kort oppsummering

Risperidon er et antipsykotikum som opprinnelig brukes til behandling av schizofreni. TxGNN-modellen predikerer at det kan være effektivt ved **familiær horisontal blikkparese med progressiv skoliose** (en sjelden genetisk sykdom), men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter dette. Prediksjonen er kun beregningsbasert. Blant de øvrige predikerte indikasjonene har **alvorlig affektiv lidelse** klart sterkest støtte, med **flere fase 3-studier** og **systematiske oversikter** (se avsnittet «Andre predikerte indikasjoner»).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Schizofreni |
| Predikert ny indikasjon | Familiær horisontal blikkparese med progressiv skoliose |
| TxGNN-prediksjonsscore | 0,9976 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall markedsføringstillatelser | 1 |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er for tiden ikke tilgjengelige i dataene som er sammenstilt for denne rapporten. Risperidon er kjent som en antagonist av dopamin D2- og serotonin 5-HT2A-reseptorer, og effekten ved schizofreni er etablert.

For denne indikasjonen er det **ingen identifisert mekanistisk sammenheng**. Sykdommen er en sjelden arvelig lidelse (knyttet til ROBO3) som rammer aksonveiledning i hjernestammen og gir en strukturell nevroutviklingsfeil. D2/5-HT2A-blokade har ingen plausibel rolle i å korrigere dette. TxGNN-scoren er derfor en ren beregningsmessig prediksjon uten støtte i kliniske data.

---

## Dokumentasjon fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

Foreløpig finnes ingen relatert litteratur.

---

## Informasjon om markedet i Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005406 | Okedi | Ikke oppgitt | Schizofreni |

Legemidlet er markedsført, og 1 av 1 tillatelser er gyldig. Innehaver er Laboratorios Farmacéuticos Rovi, S.A.

---

## Sikkerhetsvurderinger

**Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):**
Kunnskapsgrafen (PrimeKG) knytter risperidon til følgende tilstander, som bør vurderes nøye:
- **Hjerte- og karsykdom:** hjerteinfarkt, koronar trombose, hjerneslag/cerebrovaskulær sykdom, hjerneinfarkt, plutselig hjertestans, hjerteledningsforstyrrelser, hjertesykdom generelt
- **Blodtrykk og autonom regulering:** ortostatisk hypotensjon, hypotensjon, multippel systematrofi, posturalt ortostatisk takykardisyndrom (POTS)
- **Stoffskifte:** hyperglykemi, diabetes mellitus, diabetisk ketoacidose, hyperlipidemi (inkl. familiær), fedme (inkl. monogen)
- **Lever og galleveier:** leversvikt, leversykdom, gallblæresykdom
- **Blod:** nøytropeni, agranulocytose, hemoglobinopati
- **Andre:** epilepsi, kvinnelig brystkreft

**Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Alvorlige (Major):
- **Bupropion**
- **Morfin**

Moderate interaksjoner omfatter blant annet metformin, akarbose, kanagliflozin, alogliptin, albiglutid, epinefrin, hydrokortison, amfotericin B, atropin, hyoscyamin, glykopyrronium, klidinium, loperamid, bisakodyl, lorkaserin og famotidin. Ranitidin er klassifisert som mindre (Minor).

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Andre predikerte indikasjoner

| Indikasjon | Score | Evidens | Beslutning |
|------|------|------|------|
| Amelocerebrohypohidrotisk syndrom | 0,9969 | L5 | Hold |
| Phelan-McDermid syndrom | 0,9959 | L4 | Forskningsspørsmål |
| Trikotillomani | 0,9951 | L4 | Forskningsspørsmål |
| **Alvorlig affektiv lidelse** | 0,9911 | **L1** | **Proceed with Guardrails** |

**Kort om de tre første:**
- **Asperger-susceptibilitet og amelocerebrohypohidrotisk syndrom:** ingen studier eller litteratur. Risperidon er godkjent for irritabilitet ved autismespekterforstyrrelse, men det gjelder det kliniske syndromet og ikke denne genetiske oppføringen. Det andre er et ultrasjeldent genetisk syndrom (ROGDI-relatert) uten kjent mekanistisk rolle for risperidon.
- **Phelan-McDermid syndrom:** kun en oversikt over klinisk håndtering og en zebrafiskstudie (preklinisk, indirekte). Plausibelt omfang er symptomatisk atferdsbehandling, ikke sykdomsmodifikasjon.
- **Trikotillomani:** kun kasuistikker og små kasusserier (f.eks. risperidon som tillegg ved SSRI-resistente tilfeller) samt oversikter. Ingen kontrollerte studier, og det er sannsynlig publikasjonsskjevhet. Metabolsk og ekstrapyramidal risiko må veies mot en ikke-alvorlig tilstand.

### Alvorlig affektiv lidelse (best dokumentert)

Risperidons 5-HT2A- og D2-antagonisme støtter bruk som tillegg til antidepressiva ved behandlingsresistent depresjon og som antimanisk behandling ved bipolar lidelse.

**Utvalgte kliniske studier:**

| Studienummer | Fase | Status | Antall | Hovedinnhold |
|---------|------|------|------|---------|
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Fase 3 | Fullført | 630 | Risperidon som tillegg vs. placebo ved alvorlig depresjon med utilstrekkelig respons på antidepressiva |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Fase 3 | Fullført | 258 | Risperidon som tillegg til SSRI ved behandlingsresistent depresjon, inkl. vedlikeholdseffekt |
| [NCT00277654](https://clinicaltrials.gov/study/NCT00277654) | Fase 3 | Fullført | 111 | Placebokontrollert risperidon-monoterapi ved bipolar lidelse med angst |
| [NCT00167479](https://clinicaltrials.gov/study/NCT00167479) | Fase 4 | Fullført | 60 | Randomisert, dobbeltblind risperidon-monoterapi ved bipolar lidelse med komorbid angst |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Fase 4 | Avsluttet | 45 | ECT + risperidon vs. ECT alene; tidlig avslutning begrenser tolkningen |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Fase 1/2 | Fullført | 42 | Pilot: risperidon vs. olanzapin som tillegg ved behandlingsresistent depresjon |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Fase 3 | Ukjent | 84 | Risperidon-tillegg ved manglende respons på antidepressiva |

**Utvalgt litteratur:**

| PMID | År | Type | Tidsskrift | Hovedinnhold |
|------|-----|------|------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematisk oversikt/nettverksmetaanalyse | J Affect Disord | Augmenteringsstrategier ved behandlingsresistent depresjon |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematisk oversikt/metaanalyse | J Psychopharmacol | Augmentering og kombinasjonsbehandling ved tidlig behandlingsresistent depresjon |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Systematisk oversikt/metaanalyse | J Psychopharmacol | Antidepressiva + andregenerasjons antipsykotika vs. esketamin vs. litium |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Cochrane-oversikt | Cochrane Database Syst Rev | Andregenerasjons antipsykotika ved alvorlig depresjon og dystymi |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Oversikt | Ann Pharmacother | Effekt og sikkerhet av risperidon som augmentering ved alvorlig depresjon |

**Forbehold:** Evidensen for augmentering ved alvorlig depresjon er sterkere enn for monoterapi ved bipolar depresjon, der dataene er mer blandede. Resultater fra studiene er ikke tilgjengelige i dataene, så effektstørrelser må verifiseres mot primærpublikasjonene.

---

## Konklusjon og neste steg

**Beslutning: Hold** (for den primære predikerte indikasjonen, familiær horisontal blikkparese med progressiv skoliose)

**Begrunnelse:**
- Det finnes ingen kliniske studier, ingen litteratur og ingen plausibel mekanistisk sammenheng. Prediksjonen er kun beregningsbasert (L5).
- Blant de øvrige kandidatene er alvorlig affektiv lidelse (L1) den eneste som kan gå videre, med beslutningen **Proceed with Guardrails**.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner, som mangler i de sammenstilte dataene
- Detaljerte data om virkningsmekanisme (MOA)
- For alvorlig affektiv lidelse: verifisering av effektstørrelser i primærpublikasjonene, en plan for overvåking av metabolske, prolaktinrelaterte og ekstrapyramidale risikoer, samt en sjekk av markedsstatus og godkjente indikasjoner mot gjeldende regional merking, siden den eneste registrerte tillatelsen er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

