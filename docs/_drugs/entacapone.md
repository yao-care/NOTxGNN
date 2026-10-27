---
layout: default
title: Entacapone
parent: Kun modellprediksjon (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Entacapone: predikert ny indikasjon PLA2G6-assosiert nevrodegenerasjon (evidensnivå L5). Opprinnelig indikasjon: Parkinsons sykdom"
monitor_inn: "ENTACAPONE"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "paralysis agitans, juvenile, of Hunt", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
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

## Entakapon: Fra Parkinsons sykdom til PLA2G6-assosiert nevrodegenerasjon
{: .text-alpha }

## Sammendrag

Entakapon er en COMT-hemmer som brukes sammen med levodopa ved behandling av Parkinsons sykdom.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **PLA2G6-assosiert nevrodegenerasjon**, men
det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne prediksjonen i de innsamlede dataene.
Prediksjonen er derfor kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Parkinsons sykdom |
| Predikert ny indikasjon | PLA2G6-assosiert nevrodegenerasjon |
| TxGNN-prediksjonsscore | 99,76 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun annullerte godkjenninger (ingen gyldige) |
| Antall godkjenninger | 7 (alle annullert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige for dette legemidlet. Entakapon er kjent som en COMT-hemmer som forlenger virkningen av levodopa, og effekten ved Parkinsons sykdom er godkjent.

PLA2G6-assosiert nevrodegenerasjon omfatter infantil nevroaksonal dystrofi og PLA2G6-relatert dystoni-parkinsonisme. Disse tilstandene har felles trekk med Parkinsons sykdom, blant annet dopaminerg og alfa-synuklein-patologi. Det er derfor teoretisk mulig at entakapon som tillegg til levodopa kan lindre parkinsonlignende symptomer.

Dette er imidlertid kun en hypotese. Den høye TxGNN-scoren (0,9976) er en modellprediksjon og ikke klinisk evidens.

### Andre predikerte indikasjoner (kort oversikt)

Data er også samlet for ni andre predikerte indikasjoner. Alle har evidensnivå L4 eller L5:

| Rangering | Predikert indikasjon | Score | Evidensnivå | Vurdering |
|------|------|------|------|------|
| 2 | Rasmussens subakutte encefalitt | 99,73 % | L5 | Ingen plausibel mekanistisk kobling |
| 3 | Myelitt | 99,63 % | L5 | Ingen mekanistisk begrunnelse |
| 4 | Juvenil paralysis agitans (Hunt) | 99,60 % | L5 | Plausibel, men i hovedsak en gjentakelse av opprinnelig indikasjon; ingen data for barn/unge |
| 5 | Transaldolase-mangel | 99,43 % | L5 | Ingen kobling; leversikkerhet tilsier forsiktighet |
| 6 | Letal infantil mitokondriell myopati | 99,28 % | L5 | Spekulativ, kan være skadelig |
| 7 | Lewy body-demens | 99,25 % | L4 | Plausibel mekanisme, kun indirekte prekliniske data |
| 8 | Fruktose-1,6-bisfosfatase-mangel | 99,22 % | L5 | Ingen kobling |
| 9 | Polymikrogyri med cerebellær hypoplasi og artrogrypose | 99,06 % | L5 | Ingen plausibel rolle |
| 10 | Progressiv supranukleær parese–kortikobasalt syndrom | 99,04 % | L4 | Svak begrunnelse; dårlig levodopa-respons begrenser nytte |

---

## Klinisk studieevidens

For den fremste prediksjonen (PLA2G6-assosiert nevrodegenerasjon) er det for tiden ingen relaterte kliniske studier registrert.

For to andre predikerte indikasjoner finnes studier med perifer relevans (ingen evaluerer entakapon som behandling):

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn | Indikasjon |
|---------|------|------|------|---------|------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Fase 1 | Rekrutterer | 40 | [18F]F-DOPA-bildediagnostikk ved autonom svikt; ikke en terapeutisk studie av entakapon | Lewy body-demens |
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | Ikke angitt | Aktiv, ikke rekrutterende | 120 | Ikke-intervensjonell ganganalyse ved nevrologiske sykdommer, særlig parkinsonisme | PSP–kortikobasalt syndrom |

---

## Litteraturevidens

For den fremste prediksjonen foreligger det for tiden ingen relevant litteratur.

For Lewy body-demens (rangering 7) finnes to prekliniske arbeider:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro-studie | Journal of Neuroscience Research | Undersøkte effekten av antiparkinsonmidler på dannelse av β-amyloid- og α-synuklein-oligomerer; indirekte prekliniske holdepunkter |
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preklinisk (iPSC-organoidmodell) | Science Advances | Modellering av Lewy body-sykdom med SNCA-triplikasjon og identifisering av terapeutiske legemidler; tester ikke entakapon direkte |

---

## Markedsinformasjon for Norge

Alle de syv registrerte godkjenningene er annullert. Dosisform er ikke oppgitt i dataene.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002075 | Entacapone Teva | Ikke oppgitt | Parkinsons sykdom |
| EMEA/H/C/002440 | Entacapone Orion | Ikke oppgitt | Parkinsons sykdom |
| EMEA/H/C/000170 | Comtess | Ikke oppgitt | Parkinsons sykdom |
| EMEA/H/C/000171 | Comtan | Ikke oppgitt | Parkinsons sykdom |
| EMEA/H/C/002785 | Corbilta (tidligere Levodopa/Carbidopa/Entacapone Sandoz) | Ikke oppgitt | Parkinsons sykdom |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** TxGNN-kunnskapsgrafen (PrimeKG) knytter entakapon til kontraindikasjoner ved blant annet ortostatisk hypotensjon, multisystematrofi, legemiddelindusert dyskinesi, epilepsi, psykotiske lidelser, lever- og nyresykdom, magesår/ulcus, åpenvinklet og trangvinklet glaukom, diabetes og diabetisk ketoacidose, hjerteinfarkt og hjerteledningsforstyrrelser, plutselig hjertestans, melanom, hemoglobinopati og diaré. Dette er grafbaserte koblinger og ikke etiketttekst.
- **Legemiddelinteraksjoner:** 82 interaksjoner er funnet. Blant de som er vist, er følgende klassifisert som moderate: epinefrin (inkludert oftalmisk og topisk), morfin (inkludert liposomal), dronabinol, opium, nabilon, metoklopramid og jern. Flere andre (bl.a. pantoprazol, omeprazol, lansoprazol, metformin, doksycyklin, atropin, laktulose, prednison, simvastatin og kaliumklorid) har ukjent alvorlighetsgrad.

Se preparatomtalen for fullstendig informasjon om advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den fremste prediksjonen er basert utelukkende på en modellscore uten støtte fra kliniske studier eller litteratur (evidensnivå L5). I tillegg har entakapon ingen gyldige godkjenninger i Norge i dag. Ingen av de ti predikerte indikasjonene har klinisk evidens for entakapon; Lewy body-demens og PSP–kortikobasalt syndrom (L4) er best egnet som forskningsspørsmål.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Sikkerhetsopplysninger fra preparatomtale (advarsler og kontraindikasjoner)
- Prekliniske eller kliniske data for entakapon ved PLA2G6-assosiert nevrodegenerasjon
- Avklaring av regulatorisk situasjon, siden alle norske godkjenninger er annullert
- Vurdering av sikkerhet og effekt hos barn og unge dersom juvenile former skal vurderes
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

