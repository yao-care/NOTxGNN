---
layout: default
title: Cetuximab
parent: Kun modellprediksjon (L5)
nav_order: 95
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cetuximab: predikert ny indikasjon Prekreftale neoplasmer (pre-malignant neoplasm) (evidensnivå L5). Opprinnelig indikasjon: Hode- og halskreft (Head and Neck Neoplasms)"
---

# Cetuximab
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

# Cetuximab: Fra hode- og halskreft og tykktarmskreft til prekreftale neoplasmer

## Oppsummering i én setning

Cetuximab er et monoklonalt antistoff mot EGFR (epidermal vekstfaktorreseptor), opprinnelig brukt mot hode- og halskreft og kolorektal kreft.
TxGNN-modellen predikerer at det kan være effektivt mot **prekreftale neoplasmer** (pre-malignant neoplasm), blant flere andre prediksjoner med svært høye skårer.
For denne indikasjonen finnes det **4 kliniske studier** og **2 publikasjoner**, hvorav én fullført fase II-studie er direkte relevant.

Merk: Rapporten bruker prediksjon nr. 10 («pre-malignant neoplasm») som hovedindikasjon fordi den har sterkest støtte i dataene. Prediksjon nr. 1 («bronchial adenomas/carcinoids childhood») har samme modellskåre, men ingen evidens. De øvrige prediksjonene er omtalt kort nedenfor.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hode- og halskreft (Head and Neck Neoplasms); kolorektal kreft (Colorectal Neoplasms) |
| Predikert ny indikasjon | Prekreftale neoplasmer (pre-malignant neoplasm) |
| TxGNN-prediksjonsskåre | 99,95 % |
| Evidensnivå | L2 (én fullført fase II-studie som er direkte relevant, men uten tilgjengelige resultater; ingen fase 3 for denne sykdommen) |
| Markedsstatus i Norge | Kun trukket tilbake (Cancelled only) |
| Antall autorisasjoner | 1 (trukket tilbake) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er ikke tilgjengelige i datamaterialet. Basert på kjent informasjon er cetuximab et antistoff som binder EGFR (Kd-verdi fra patent US7060808). Det blokkerer reseptoren og hemmer dermed signalveier for vekst og overlevelse hos tumorceller. Cetuximab brukes ved EGFR-uttrykkende metastatisk kolorektal kreft der annen kjemoterapi ikke har gitt respons, og ved plateepitelkarsinom i hode og hals i kombinasjon med strålebehandling.

EGFR er overuttrykt i prekreftale lesjoner i øvre luft- og fordøyelsesveier, med økt proteinuttrykk og økt genkopitall sammenlignet med normal slimhinne. Dette gir en kjemoprevensjonsbegrunnelse: hvis EGFR driver utviklingen fra prekreftal lesjon til hode- og halskreft, kan blokade av EGFR i teorien hindre progresjon. Oversiktsartikkelen fra 2014 (PMID 24412287) beskriver nettopp denne tankegangen.

Det er viktige forbehold. Resultater for effekt og toleranse i kjemoprevensjonsøyemed er ikke tilgjengelige i dataene. Cetuximabs bivirkninger (hudreaksjoner og infusjonsreaksjoner) kan begrense bruk hos personer uten påvist kreft.

---

## Klinisk studieevidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00524017](https://clinicaltrials.gov/study/NCT00524017) | Fase 2 | Fullført | 35 | Randomisert studie av cetuximab som monoterapi ved høyrisiko prekreftale lesjoner i øvre luft- og fordøyelsesveier. Direkte relevant; resultater ikke oppgitt i dataene |
| [NCT00482222](https://clinicaltrials.gov/study/NCT00482222) | Fase 3 | Ukjent | 340 | Oksaliplatin/fluoropyrimidin med eller uten cetuximab ved resektable levermetastaser fra kolorektal kreft. Ikke relevant for prekreftale lesjoner |
| [NCT00719199](https://clinicaltrials.gov/study/NCT00719199) | Fase 1 | Avsluttet tidlig | 21 | FOLFIRI + cetuximab + IMO-2055 ved kolorektal kreft. Gjelder etablert kreft |
| [NCT00537823](https://clinicaltrials.gov/study/NCT00537823) | Fase 2 | Avsluttet tidlig | 9 | Kortvarig neoadjuvant FOLFOX-basert behandling og komplikasjoner etter leverreseksjon. Ikke relevant for prekreftale lesjoner |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [24412287](https://pubmed.ncbi.nlm.nih.gov/24412287/) | 2014 | Oversikt | Oral Oncology | EGFR er involvert i karsinogenese ved plateepitelkarsinom i hode og hals, og oralt prekreftale lesjoner har økt EGFR-uttrykk. Gir grunnlag for kjemoprevensjon |
| [33243986](https://pubmed.ncbi.nlm.nih.gov/33243986/) | 2020 | Oversikt | Nature Reviews Disease Primers | Generell oversikt over plateepitelkarsinom i hode og hals (risikofaktorer, HPV-status) |

---

## Andre prediksjoner i datamaterialet

| Predikert indikasjon | Skåre | Evidensnivå | Kommentar |
|------|------|------|------|
| Cystisk neoplasme | 99,95 % | L3 | Fase II-studie ved spyttkjertelkarsinom (PMID 18804410) og fase 1/2-studie ved adenoid cystisk karsinom (NCT01192087, status ukjent). Tidlig og heterogen evidens |
| Odontogen cyste | 99,95 % | L4 | Kun to kasuistikker om primært intraosseøst karsinom; ingen kontrollerte data |
| Duktal eller duktulær proliferasjon | 99,95 % | L5 | Litteraturen gjelder pankreaskreft og er i hovedsak prekliniske studier og oversikter. KRAS-drevet pankreaskreft er generelt resistent mot anti-EGFR-antistoffer |
| Epiglottis-neoplasme | 99,95 % | L5 | Ingen evidens funnet. Sannsynligvis dekket av eksisterende hode- og halsindikasjon (basert på forhåndskunnskap, ikke på dataene) |
| Bronkiale adenomer/karsinoider hos barn, ikke-seminomatøs lesjon, kondroid hamartom, testikkeltumor, tyreoglossal duktuscyste | 99,95 % | L5 | Kun modellprediksjon uten studier eller litteratur. Ingen støttende mekanistisk begrunnelse |

---

## Informasjon om det norske markedet

| Autorisasjonsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000558 | Erbitux | Ikke oppgitt | Hode- og halskreft; kolorektal kreft (status: trukket tilbake) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet behandling (monoklonalt antistoff mot EGFR) |
| Risiko for myelosuppresjon | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegg for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Hudreaksjoner og infusjonsreaksjoner (jf. studiedata); ellers se pakningsvedlegg |
| Håndteringsbeskyttelse | Se pakningsvedlegg for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (20 registrerte; de viktigste er listet):

- **Alvorlig (Major):** aminolevulinsyre, thalidomid
- **Moderat:** protonpumpehemmere (rabeprazol, omeprazol, deksansoprazol, esomeprazol, lansoprazol, pantoprazol), metoksalen, kapecitabin, karboplatin, cisplatin, fluorouracil, oksaliplatin, idelalisib, omacetaksin mepesuccinat, verteporfin, aminolevulinsyre (topikal), metylaminolevulinat (topikal)

**Andre sikkerhetsmomenter fra studiedata:** Cetuximab kan gi alvorlige infusjonsreaksjoner (PMID 39415301) og hudbivirkninger (PMID 30141310). Disse kan være særlig problematiske ved bruk hos personer med prekreftale lesjoner.

Se pakningsvedlegget for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den eneste direkte relevante studien (NCT00524017, fase II, n=35) er fullført, men resultater for effekt og toleranse er ikke tilgjengelige. Fase 3-studien i datamaterialet gjelder kolorektal kreft og støtter ikke denne indikasjonen. Cetuximab er dessuten ikke lenger markedsført i Norge (kun trukket tilbake autorisasjon), og toksisiteten kan veie tungt ved bruk i en ikke-malign populasjon.

**For å gå videre trengs følgende:**
- Publiserte resultater fra NCT00524017 (effekt, progresjon til kreft, sikkerhet)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Pakningsvedlegg med advarsler og kontraindikasjoner (mangler, og blokkerer sikkerhetsscreening)
- Vurdering av nytte-risiko ved kjemoprevensjon sammenlignet med alternativer
- Avklaring av tilgjengelighet og regulatorisk status i Norge, siden autorisasjonen er trukket tilbake
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

