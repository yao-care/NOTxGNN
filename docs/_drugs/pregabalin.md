---
layout: default
title: Pregabalin
parent: Kun modellprediksjon (L5)
nav_order: 337
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
monitor_inn: "PREGABALIN"
predicted_indications: ["tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
description: "Pregabalin: predikert ny indikasjon Tendinitis (evidensnivå L5). Opprinnelig indikasjon: Anxiety Disorders"
---

# Pregabalin
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

## Pregabalin: Tendinitis
{: .text-alpha }

## Ettsetningssammendrag

Pregabalin er et legemiddel som opprinnelig brukes mot epilepsi, angstlidelser og nevropatisk smerte (nevralgi).
TxGNN-modellen forutsier at det kan ha effekt ved **migrenelidelse** (høyeste score blant forslagene med noe klinisk støtte), men beviset er begrenset: **1 kliniske studie med fase 3-design (trukket tilbake før oppstart)**, **1 fase 4-studie som ikke tester effekt**, og flere publikasjoner, hovedsakelig små pediatriske randomiserte studier.
Det øverste forslaget på listen, **tendinitt** (score 0,9971), har ingen direkte klinisk støtte og er derfor ikke brukt som hovedkandidat i denne rapporten.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Anxiety Disorders;Epilepsy; Epilepsy;Anxiety Disorders;Neuralgia; Anxiety Disorders;Neuralgia;Epilepsy |
| Predikert ny indikasjon | Tendinitis |
| TxGNN-prediksjonsscore | 0.9971 |
| Evidensnivå | L5 (migrene); tendinitt L4 |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 6 av 6) |
| Antall godkjenninger | 6 (gyldige: 6) |
| Anbefalt beslutning | Hold (migrene: forskningsspørsmål, ikke klar for videre utvikling) |

*Merknad:* Evidensnivået L2 for migrene er den automatiske vurderingen i dataene. Det bygger på små pediatriske randomiserte studier, ikke på en fullført fase 2/3-studie, så det bør tolkes forsiktig.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelige i de innhentede dataene. Basert på kjent informasjon er pregabalin en ligand til alfa-2-delta-underenheten i spenningsstyrte kalsiumkanaler. Den reduserer frisetting av eksitatoriske nevrotransmittere som glutamat og demper sentral sensitisering. Virkningen er godt dokumentert ved epilepsi og nevropatisk smerte.

Migrene deler flere trekk med disse tilstandene: nevronal hyperekscitabilitet og sentral sensitisering. Prekliniske studier viser at pregabalin hever terskelen for kortikal spredt depolarisering (cortical spreading depression), som antas å ligge bak migreneaura, og at det hemmer P/Q-type kalsiumkanaler. Dette gir en plausibel mekanistisk kobling.

Det finnes likevel viktige forbehold. Klinisk støtte kommer i hovedsak fra små pediatriske randomiserte studier (mot valproat og propranolol) og en nettverksmetaanalyse, men ikke fra voksenstudier i fase 3. Andre antiepileptika (topiramat, valproat) er bedre etablert i migreneforebygging.

For tendinitt, den høyest rangerte prediksjonen, er en eventuell nytte trolig begrenset til symptomatisk smertelindring, ikke behandling av selve senebetennelsen eller degenerasjonen. Den høye TxGNN-scoren støttes ikke av direkte klinisk evidens. Prediksjonene for idiopatisk granulomatøs myositt, myositis fibrosa og inklusjonslegememyositt mangler både studier og plausibel mekanisme.

---

## Klinisk studieevidens

Studier for migrenelidelse:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00447369](https://clinicaltrials.gov/study/NCT00447369) | Fase 3 | Trukket tilbake | 70 (planlagt) | Randomisert, blindet crossover-studie av pregabalin mot natriumvalproat i migreneforebygging. Trukket tilbake, ingen data. |
| [NCT02747940](https://clinicaltrials.gov/study/NCT02747940) | Fase 4 | Fullført | 200 | Studie av hjernesignaturer ved kroniske smertetilstander (kronisk migrene og fibromyalgi). Kartleggingsstudie, tester ikke effekt av pregabalin ved migrene. |

For de andre predikerte indikasjonene (tendinitt, idiopatisk granulomatøs myositt, myositis fibrosa, inklusjonslegememyositt, migrene med hjernestammeaura) er det for tiden ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Utvalg for migrenelidelse:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [37637787](https://pubmed.ncbi.nlm.nih.gov/37637787/) | 2023 | RCT | Iran J Child Neurol | Pregabalin sammenlignet med natriumvalproat i migreneforebygging hos barn |
| [26024701](https://pubmed.ncbi.nlm.nih.gov/26024701/) | 2015 | RCT | Acta Med Iran | Pregabalin sammenlignet med propranolol i migreneforebygging hos barn (99 barn, 3–15 år) |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Nettverksmetaanalyse | JAMA Netw Open | Forebyggende legemidler ved pediatrisk migrene |
| [23797675](https://pubmed.ncbi.nlm.nih.gov/23797675/) | 2013 | Systematisk oversikt | Cochrane Database Syst Rev | Gabapentin eller pregabalin for forebygging av episodisk migrene hos voksne |
| [21479703](https://pubmed.ncbi.nlm.nih.gov/21479703/) | 2011 | Oppfølgingsstudie | J Headache Pain | Effekt og tolerabilitet av pregabalin som forebyggende migrenebehandling over 3 måneder |
| [25669613](https://pubmed.ncbi.nlm.nih.gov/25669613/) | 2015 | Klinisk studie | Int J Clin Pharmacol Ther | Effekt av pregabalin på sentral sensitisering og allodyni ved migrene |
| [30880369](https://pubmed.ncbi.nlm.nih.gov/30880369/) | 2019 | Oversikt | Curr Treat Options Neurol | Status for antiepileptika som forebyggende migrenebehandling |
| [37924146](https://pubmed.ncbi.nlm.nih.gov/37924146/) | 2023 | Preklinisk | Mol Brain | Kronisk pregabalin beskytter mot spredt depolarisering i musemodell for familiær hemiplegisk migrene type 1 |
| [28223480](https://pubmed.ncbi.nlm.nih.gov/28223480/) | 2017 | Preklinisk | PNAS | Pregabalin hemmer kortikal spredt depolarisering (relevant også for migrene med hjernestammeaura) |
| [20464594](https://pubmed.ncbi.nlm.nih.gov/20464594/) | 2010 | Oversikt | Neurol Sci | Behandlingsstrategier ved migrene med komorbide stemnings- og angstlidelser |

Merknad om tendinitt: de hentede artiklene er i hovedsak case-rapporter eller studier av postoperativ smerte etter skulderkirurgi (f.eks. PMID 34052386), ikke studier av tendinitt. De gir ikke direkte støtte.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003880 | Pregabalin Viatris Pharma (tidligere Pregabalin Pfizer) | – | Angstlidelser; epilepsi |
| EMEA/H/C/000546 | Lyrica | – | Epilepsi; angstlidelser; nevralgi |
| EMEA/H/C/004024 | Pregabalin Accord | – | Angstlidelser; epilepsi |
| EMEA/H/C/004010 | Pregabalin Sandoz | – | Angstlidelser; nevralgi; epilepsi |
| EMEA/H/C/004078 | Pregabalin Viatris (tidligere Pregabalin Mylan) | – | Angstlidelser; epilepsi |

(Én ytterligere annullert godkjenning, Pregabalin Zentiva, er ikke vist i tabellen.)

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (TxGNN/PrimeKG, ikke preparatomtale):** angstlidelse, nevrotisk lidelse, dysthymisk lidelse, trombocytopeni, angioødem (inkludert ervervet, hereditært, ikke-histaminisk og ACE-/RAAS-hemmerutløst), myopati, muskelsykdom, skjelettmuskelsykdom, familiær periodisk paralyse, rabdomyolyse, nodulær fasciitt, nedsatt nyrefunksjon og atrioventrikulært blokk. Disse er grafbaserte signaler og må bekreftes mot preparatomtalen.
- **Legemiddelinteraksjoner (100 registrert; utvalg):**
  - **Alvorlig (Major):** morfin, morfin (liposomalt). Risiko for additiv sentralnervøs og respirasjonsdemping.
  - **Moderat:** pioglitazon, rosiglitazon, troglitazon, difenoksin, difenoksylat, dronabinol, nabilon, metoklopramid, opium, sibutramin.
  - **Ukjent nivå:** kalsitriol, vitamin A, fentermin, pantoprazol, glimepirid, sukralfat, palonosetron, nystatin.

Informasjon om advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelig i de innhentede dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den eneste fase 3-studien i migrene (NCT00447369) ble trukket tilbake og har ingen resultater. Støtten består av små pediatriske studier og prekliniske data, og andre antiepileptika er bedre etablert. Den høyest rangerte prediksjonen (tendinitt) og de øvrige muskelsykdommene mangler direkte evidens eller plausibel mekanisme.

**For å gå videre trengs følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel som hindrer sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (MOA) fra DrugBank
- Randomiserte, kontrollerte studier hos voksne med migrene, helst fase 2/3 med placebo eller etablert forebyggende komparator
- Klargjøring av regulatorisk status i Norge, siden alle godkjenninger er annullert
- Sikkerhetsplan som tar hensyn til interaksjon med opioider og kontraindikasjonssignalene fra kunnskapsgrafen (blant annet nedsatt nyrefunksjon, myopati og angioødem)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

