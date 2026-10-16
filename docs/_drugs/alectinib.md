---
layout: default
title: Alectinib
parent: Kun modellprediksjon (L5)
nav_order: 23
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Alectinib: predikert ny indikasjon Lung benign neoplasm (godartet lungeneoplasme) (evidensnivå L5). Opprinnelig indikasjon: Carcinoma, Non-Small-Cell Lung (ikke-småcellet lungekreft)"
monitor_inn: "Alectinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa"]
---

# Alectinib
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

# Alectinib: Fra ikke-småcellet lungekreft til godartet lungeneoplasme (prediksjon uten reell støtte)

## Oppsummering i én setning

Alectinib er en ALK-hemmer som opprinnelig brukes mot **ikke-småcellet lungekreft (NSCLC)**.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **lung benign neoplasm (godartet lungeneoplasme)**, men de publikasjonene som er funnet gjelder i realiteten den allerede godkjente indikasjonen ALK-positiv NSCLC. **Ingen kliniske studier** og **ingen litteratur om godartede lungesvulster** støtter prediksjonen. Rangering etter TxGNN-score alene gir ingen reell reposisjoneringssignal.

> Merk: Rapporten tar utgangspunkt i prediksjonen med mest litteratur (rang 5, lung benign neoplasm). Prediksjon nr. 1 (gingival fibromatose) har høyest score, men ingen evidens.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Carcinoma, Non-Small-Cell Lung (ikke-småcellet lungekreft) |
| Predikert ny indikasjon | Lung benign neoplasm (godartet lungeneoplasme); høyest rangert er gingival fibromatose |
| TxGNN-prediksjonsscore | 99,95 % (godartet lungeneoplasme); 99,97 % (gingival fibromatose) |
| Evidensnivå | L1 formelt, men gjelder malign NSCLC og overføres ikke; reelt L5 for den predikerte indikasjonen |
| Status i Norge/EØS | Kun kansellert |
| Antall autorisasjoner | 1 (kansellert) |
| Anbefalt beslutning | Hold (vent) |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de innsamlede dataene. Ut fra kjent informasjon er alectinib en selektiv, ATP-konkurrerende hemmer av ALK (anaplastisk lymfomkinase), og farmakologidata viser også binding mot MET. Legemidlet har dokumentert effekt ved ALK-positiv NSCLC, inkludert CNS-aktivitet og effekt mot crizotinib-resistente celler.

Prediksjonen om godartet lungeneoplasme er sannsynligvis en **ontologi-artefakt** i kunnskapsgrafen: sykdomsnavnet ligger nær lungeneoplasmer, som er den godkjente indikasjonen. Godartede lungesvulster har ingen kjent ALK-drevet biologi, og det finnes ingen plausibel begrunnelse for en kinasehemmer. Det samme gjelder de øvrige topprangerte prediksjonene (gingival fibromatose, lungefibrom, hamartom, junksjonell epidermolysis bullosa m.fl.): ingen identifisert mekanistisk kobling.

Den mest nærliggende, men fortsatt svake, indirekte evidensen gjelder lungegermcelletumor (rang 6): kasuistikker viser at ALK-omorganiserte nevroendokrine svulster har respondert på ALK-hemmere, men ingen gjelder kimcelletumorer.

---

## Klinisk studieevidens

For godartet lungeneoplasme: Foreløpig ingen relaterte kliniske studier registrert.

Til orientering finnes én studie for en annen prediksjon (lung germ cell tumor, rang 6):

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT04644315](https://clinicaltrials.gov/study/NCT04644315) | Fase 2 | Avsluttet (terminated) | 1 | Enarmet, desentralisert studie av alectinib ved ALK-positive solide svulster utenom lungekreft. Kun 1 deltaker, gir ingen tolkbare effektdata. |

---

## Litteraturevidens

Litteraturen under er knyttet til prediksjonen «lung benign neoplasm», men gjelder malign ALK-positiv NSCLC (den godkjente indikasjonen), ikke godartede svulster.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [38598794](https://pubmed.ncbi.nlm.nih.gov/38598794/) | 2024 | RCT (fase 3, ALINA) | N Engl J Med | Adjuvant alectinib versus kjemoterapi ved reseksjonert ALK-positiv NSCLC |
| [28586279](https://pubmed.ncbi.nlm.nih.gov/28586279/) | 2017 | RCT (fase 3, ALEX) | N Engl J Med | Alectinib versus crizotinib ved ubehandlet avansert ALK-positiv NSCLC, inkl. CNS-sykdom |
| [28501140](https://pubmed.ncbi.nlm.nih.gov/28501140/) | 2017 | RCT (fase 3, J-ALEX) | Lancet | Alectinib versus crizotinib hos japanske pasienter med ALK-positiv NSCLC |
| [32418886](https://pubmed.ncbi.nlm.nih.gov/32418886/) | 2020 | RCT-oppdatering | Ann Oncol | Oppdatert totaloverlevelse og endelig PFS fra ALEX (opptil 5 år) |
| [41110693](https://pubmed.ncbi.nlm.nih.gov/41110693/) | 2026 | RCT (endelig analyse) | Ann Oncol | Endelig totaloverlevelsesanalyse av ALEX, med varighet av respons og langtidssikkerhet |
| [30902613](https://pubmed.ncbi.nlm.nih.gov/30902613/) | 2019 | RCT-oppdatering | J Thorac Oncol | Oppdatert effekt og sikkerhet, og betydning av EML4-ALK-variant i ALEX |
| [39368244](https://pubmed.ncbi.nlm.nih.gov/39368244/) | 2024 | Systematisk oversikt / nettverksmetaanalyse | Lung Cancer | Sammenligning av ALK-hemmere (inkl. lorlatinib) som førstelinjebehandling |
| [40222406](https://pubmed.ncbi.nlm.nih.gov/40222406/) | 2025 | Nettverksmetaanalyse | Value Health | Kostnadseffektivitet av alectinib, brigatinib og lorlatinib i førstelinje |
| [30069772](https://pubmed.ncbi.nlm.nih.gov/30069772/) | 2018 | Legemiddeloversikt | Recent Results Cancer Res | Alectinib som andregenerasjons ALK-hemmer med CNS-aktivitet |
| [31727555](https://pubmed.ncbi.nlm.nih.gov/31727555/) | 2019 | Oversikt | Rev Mal Respir | Behandlingsstrategier ved avansert ALK-positiv NSCLC |

---

## Markedsinformasjon for Norge/EØS

| Autorisasjonsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004164 | Alecensa (Roche Registration GmbH) | Ikke oppgitt | Carcinoma, Non-Small-Cell Lung (status: kansellert) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (tyrosinkinasehemmer mot ALK/MET), ikke konvensjonell cytostatika |
| Myelosuppresjonsrisiko | Se pakningsvedlegget. Litteraturen beskriver anemi (vanligvis mild) og et tilfelle av hemolytisk anemi |
| Emetogenisitet | Se pakningsvedlegget |
| Overvåkingspunkter | Blodstatus, lever- og nyrefunksjon, triglyserider/lipider, vekt og hjerterytme (bradykardi/QTc) bør vurderes |
| Håndteringsbeskyttelse | Se pakningsvedlegget og lokale retningslinjer for håndtering av cytostatika |

---

## Sikkerhetsvurderinger

Offisielle data om advarsler og kontraindikasjoner fra pakningsvedlegget var ikke tilgjengelige i de innsamlede dataene. Se pakningsvedlegget for sikkerhetsinformasjon.

Bivirkninger beskrevet i litteraturen (kasuistikker og farmakovigilans):
- Hypertriglyseridemi-indusert pankreatitt
- Hemolytisk anemi
- Legemiddelreaksjon med eosinofili og systemiske symptomer (DRESS)
- Erythema multiforme
- Betydelig vektøkning (ca. 10 %)

Det er også relevant for kutane sykdommer som junksjonell epidermolysis bullosa at alectinib kan gi hudbivirkninger.

Legemiddelinteraksjoner: Ingen konkrete legemiddel–legemiddel-interaksjoner er oppgitt. Farmakologidata viser kun målene ALK og MET.

---

## Konklusjon og neste steg

**Beslutning: Hold (vent)**

**Begrunnelse:**
Alle prediksjonene er rent modellbaserte uten støtte fra kliniske studier eller litteratur for de predikerte sykdommene. L1-nivået for «lung benign neoplasm» gjelder malign ALK-positiv NSCLC og overføres ikke til godartede svulster. I tillegg er den eneste autorisasjonen i Norge/EØS kansellert.

**For å gå videre kreves følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (MOA)
- Biologisk rasjonale og prekliniske data som kobler ALK/MET-hemming til en av de predikerte sykdommene
- Vurdering av om en ALK-drevet undergruppe finnes (f.eks. ALK-positive nevroendokrine svulster), og eventuelt nye studier der
- Avklaring av årsaken til kansellert status i Norge/EØS
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

