---
layout: default
title: Bevacizumab
parent: Kun modellprediksjon (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bevacizumab: predikert ny indikasjon Epiglottis-neoplasme (score 99,90 %, evidensnivå L5) (evidensnivå L5). Opprinnelig indikasjon: Kolorektal neoplasme, brystkreft, eggstokkreft, kreft i eggleder…"
monitor_inn: "BEVACIZUMAB"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
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

# Bevacizumab: Fra kolorektal kreft m.fl. til cystisk neoplasme

## Oppsummering i én setning

Bevacizumab er et monoklonalt antistoff mot VEGF-A som opprinnelig brukes til behandling av flere kreftformer (blant annet tykktarms- og endetarmskreft, brystkreft, eggstokkreft, lungekreft og nyrekreft) og til våt aldersrelatert makuladegenerasjon.
TxGNN-modellen rangerer **epiglottis-neoplasme** øverst, men det beste evidensgrunnlaget finnes for **cystisk neoplasme** (i praksis hovedsakelig eggstokksvulster), med **5 kliniske studier** og **20 publikasjoner** i datagrunnlaget. Evidensen er i stor grad ekstrapolert fra godkjente indikasjoner og er ikke direkte spesifikk for denne diagnosegruppen.

*Merk: Den øverste rangerte prediksjonen (epiglottis-neoplasme) har ingen studier eller litteratur. Rapporten fremhever derfor også prediksjonen med sterkest evidens.*

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kolorektal neoplasme, brystkreft, eggstokkreft, kreft i eggleder, peritoneal kreft, ikke-småcellet lungekreft, nyrecellekarsinom, livmorhalskreft (første lisens). Våt makuladegenerasjon (Lytenava) |
| Predikert ny indikasjon (rangert først) | Epiglottis-neoplasme (score 99,90 %, evidensnivå L5) |
| Predikert indikasjon med sterkest evidens | Cystisk neoplasme (score 99,89 %, evidensnivå L2) |
| Evidensnivå | L5 for rangert nr. 1; L2 for cystisk neoplasme |
| Status i Norge | Kun avregistrerte (cancelled) |
| Antall godkjenninger | 10 (alle avregistrert; ingen gyldige) |
| Anbefalt beslutning | Hold (rangert nr. 1); cystisk neoplasme: forskningsspørsmål, Proceed with Guardrails ved videre utredning |

---

## Hvorfor er denne prediksjonen rimelig?

Bevacizumab nøytraliserer VEGF-A og hemmer dermed tumorangiogenese. Detaljerte mekanismedata (MOA) er ikke tilgjengelige i datagrunnlaget, men virkningsmekanismen er velkjent: svulster som er avhengige av nydannelse av blodkar, kan i prinsippet respondere på VEGF-blokade.

For **epiglottis-neoplasme** er mekanismen plausibel fordi hode- og halssvulster ofte er VEGF-avhengige, men det finnes verken studier eller litteratur. Prediksjonen bygger kun på modellen.

For **cystisk neoplasme** er litteraturen konsentrert om cystiske/epiteliale eggstokksvulster, særlig lavgradig serøs eggstokkkreft (LGSOC) og høygradig serøs kreft. Bevacizumab er allerede godkjent for eggstokkkreft, og en VEGF-avhengig gensignatur er beskrevet i mesenkymal eggstokkkreft. En systematisk oversikt tar for seg bevacizumab ved LGSOC. «Cystisk neoplasme» er imidlertid en heterogen kategori, og evidensen er hovedsakelig ekstrapolert fra eggstokkkreft og sjeldne svulster.

---

## Klinisk studieevidens (cystisk neoplasme)

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Fase 3 | Aktiv, ikke rekrutterende | 1052 | Karboplatin/paklitaksel (eller gemcitabin) med eller uten bevacizumab ved tilbakevendende platinasensitiv eggstokk-, peritoneal- og eggledercancer. Relevant for eggstokkdelen, men gjelder allerede godkjent indikasjon |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Fase 2 | Aktiv, ikke rekrutterende | 133 | Enarmet studie av atezolizumab + bevacizumab ved sjeldne solide svulster; tegn på aktivitet, men uten randomisert kontroll |
| [NCT00023959](https://clinicaltrials.gov/study/NCT00023959) | Fase 1 | Fullført | 39 | Sikkerhetsstudie av bevacizumab + fluorouracil/hydroksyurea + strålebehandling ved hode- og halskreft; indirekte |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Fase 1/2 | Fullført | 66 | Erlotinib + cetuximab + bevacizumab ved flere solide svulster; indirekte |
| [NCT00492089](https://clinicaltrials.gov/study/NCT00492089) | Fase 2 | Fullført | 11 | Bevacizumab mot strålingsskade i hjernen; annen tilstand |

For epiglottis-neoplasme finnes for øyeblikket ingen relevante kliniske studier registrert.

---

## Litteraturevidens (cystisk neoplasme)

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | Systematisk oversikt | Current Oncology | Bevacizumab har vist noe aktivitet ved lavgradig serøs eggstokkkreft, som mangler sykdomsspesifikke behandlingsregimer |
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | Retrospektiv studie | Future Oncology | 51 pasienter med tilbakevendende LGSOC: objektiv responsrate 54,1 % (komplett 10,4 %, delvis 43,7 %) |
| [40644648](https://pubmed.ncbi.nlm.nih.gov/40644648/) | 2025 | Klinisk studie | J Clin Oncol | Avutometinib ± defaktinib ved tilbakevendende LGSOC (ikke bevacizumab-spesifikk) |
| [40700681](https://pubmed.ncbi.nlm.nih.gov/40700681/) | 2025 | Klinisk studie | J Clin Oncol | Alpelisib + olaparib mot kjemoterapi ved platinaresistent høygradig serøs eggstokkkreft |
| [32494876](https://pubmed.ncbi.nlm.nih.gov/32494876/) | 2020 | Oversikt | Curr Oncol Rep | Førstelinjebehandling av avansert høygradig serøs eggstokkkreft, inkludert VEGF-hemming |
| [40513287](https://pubmed.ncbi.nlm.nih.gov/40513287/) | 2025 | Tilleggsstudie til RCT | Eur J Cancer | Prediktiv verdi av BRCA1/RAD51C-metylering i PAOLA-1 (bevacizumab/olaparib-vedlikehold) |
| [27498762](https://pubmed.ncbi.nlm.nih.gov/27498762/) | 2016 | Translasjonell/kohort | Scientific Reports | VEGF-avhengig gensignatur i mesenkymal eggstokkkreft som predikerer prognose |
| [37657955](https://pubmed.ncbi.nlm.nih.gov/37657955/) | 2023 | Klinisk studie | Clin Colorectal Cancer | Mitomycin-C, metronomisk kapecitabin og bevacizumab ved pseudomyxoma peritonei |
| [18796376](https://pubmed.ncbi.nlm.nih.gov/18796376/) | 2008 | Erfaringsserie | Clin Transl Oncol | Oral syklofosfamid + bevacizumab ved sterkt forbehandlet eggstokkreft |
| [23767831](https://pubmed.ncbi.nlm.nih.gov/23767831/) | 2013 | Oversikt | Gynecol Endocrinol | Antiangiogene midler ved avansert endometriekreft; bevacizumab viste lovende aktivitet i fase II |

For de øvrige prediksjonene er litteraturen svært begrenset. For benign neoplasme i tunge og munnbunn finnes kun indirekte og prekliniske arbeider (blant annet PMID 39927612, 18691881, 18577994). Ingen av dem viser effekt ved den aktuelle benigne diagnosen.

---

## Markedsinformasjon for Norge

Alle 10 godkjenninger er avregistrert (cancelled). Ingen er gyldige i dag.

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000582 | Avastin | – | Ikke-småcellet lungekreft, brystkreft, eggstokkkreft, kolorektal kreft, nyrecellekarsinom, kreft i eggleder, peritoneal kreft, livmorhalskreft |
| EMEA/H/C/004728 | Mvasi | – | Nyrecellekarsinom, peritoneal kreft, eggstokkkreft, brystkreft, ikke-småcellet lungekreft, kreft i eggleder |
| EMEA/H/C/004697 | Zirabev | – | Kolorektal kreft, brystkreft, ikke-småcellet lungekreft, nyrecellekarsinom, livmorhalskreft |
| EMEA/H/C/005534 | Vegzelma | – | Kolorektal kreft, brystkreft, eggstokkkreft, kreft i eggleder, peritoneal kreft, ikke-småcellet lungekreft, nyrecellekarsinom, livmorhalskreft |
| EMEA/H/C/005723 | Lytenava | – | Våt makuladegenerasjon |

Ytterligere godkjenninger: Alymsys, Avzivi, Abevmy, Oyavas og Aybintio (alle biotilsvarende, avregistrert).

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet behandling (monoklonalt antistoff mot VEGF-A, antiangiogen); ikke et konvensjonelt cytotoksisk middel |
| Myelosuppresjonsrisiko | Lav som monoterapi; økt risiko for nøytropeni i kombinasjon med cytotoksisk kjemoterapi |
| Emetogenisitet | Lav |
| Overvåkingspunkter | Blodtrykk, urinprotein, blodbilde, tegn på blødning, sårtilheling og tromboemboliske hendelser |
| Håndteringsbeskyttelse | Se preparatomtalen for krav til tilberedning og håndtering |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (22 interaksjoner funnet, hvorav 20 er listet i datagrunnlaget):

- **Alvorlige (Major):** deferipron, samarium (153Sm) lexidronam, panitumumab, sunitinib, talidomid
- **Moderate:** blant annet bisfosfonater (alendronsyre, risedronsyre, etidronsyre, ibandronat, pamidronsyre, tiludronsyre), filgrastim, pegfilgrastim, sargramostim, palifermin, strontium-89, radium-223, romosozumab, idelalisib og natriumfosfat (P32)

**Andre sikkerhetssignaler fra litteraturen:** Oral slimhinnetoksisitet (blant annet geografisk tunge) er beskrevet ved bevacizumab (PMID 39927612).

Advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelige i datagrunnlaget. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (for rangert nr. 1, epiglottis-neoplasme). Cystisk neoplasme: forskningsspørsmål som kan gå videre med forbehold (Proceed with Guardrails).**

**Begrunnelse:**
- Den høyest rangerte prediksjonen har bare modellstøtte (L5), uten studier eller litteratur, og kan ikke anbefales videre nå.
- For cystisk neoplasme (L2) støtter en fase 3-studie, fase 2-data og en systematisk oversikt bruk ved eggstokksvulster, men dette overlapper i stor grad med allerede godkjent indikasjon, og kategorien er heterogen. Ingen studier viser direkte effekt på «cystisk neoplasme» som egen diagnose. Alle norske godkjenninger er dessuten avregistrert.

**For å gå videre kreves følgende:**
- Preparatomtalens advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Detaljerte mekanismedata (MOA), for eksempel fra DrugBank
- Presisering av hvilke undertyper av cystisk neoplasme som er aktuelle, og hvordan de skiller seg fra godkjent eggstokkindikasjon
- Avklaring av markedsstatus i Norge, siden alle godkjenninger er avregistrert
- Vurdering av administrasjonsvei og likhet med opprinnelige indikasjoner
- Direkte kliniske data (helst randomiserte studier) for den valgte undergruppen
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

