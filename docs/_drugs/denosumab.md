---
layout: default
title: Denosumab
parent: Kun modellprediksjon (L5)
nav_order: 123
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Denosumab: predikert ny indikasjon Alvorlig ikke-proliferativ diabetisk retinopati (evidensnivå L5). Opprinnelig indikasjon: Tap av benmasse, postmenopausal osteoporose, osteoporose"
monitor_inn: "DENOSUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Denosumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Denosumab: Fra osteoporose og kjempecelletumor i bein til alvorlig ikke-proliferativ diabetisk retinopati

## Sammendrag i én setning

Denosumab er en RANKL-hemmer som opprinnelig brukes mot osteoporose (inkludert postmenopausal osteoporose), tap av benmasse og kjempecelletumor i bein.
TxGNN-modellen forutsier at legemidlet kan ha effekt mot **alvorlig ikke-proliferativ diabetisk retinopati**,
men det finnes **ingen kliniske studier** og **ingen litteratur som direkte undersøker retinopati** for denne indikasjonen. Prediksjonen er foreløpig kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Tap av benmasse, postmenopausal osteoporose, osteoporose |
| Predikert ny indikasjon | Alvorlig ikke-proliferativ diabetisk retinopati |
| TxGNN-prediksjonsscore | 99,63 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede tillatelser |
| Antall tillatelser | 20 (alle opphevet) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i det kompilerte datagrunnlaget. Basert på kjent informasjon er denosumab et monoklonalt antistoff som hemmer RANKL, og effekten ved osteoporose og kjempecelletumor i bein er etablert. Mekanistisk kan det tenkes at det er relevant for diabetisk retinopati.

RANKL/RANK-signalering har blitt foreslått å spille en rolle i betennelse og karbiologi, noe som i teorien kan knyttes til mikrovaskulær sykdom i netthinnen. Dette er spekulativt og ikke validert for retinopati. Likhet mellom opprinnelig og ny indikasjon er ikke vurdert, og mekanismen kunne ikke krysskontrolleres mot kuraterte legemiddeldata.

Det finnes også en nærliggende prediksjon for **diabetisk retinopati** generelt (score 99,23 %). Heller ikke denne har kliniske studier, og de to funnede publikasjonene gir bare indirekte kontekst (se under).

---

## Kliniske studier

Foreløpig er ingen relevante kliniske studier registrert.

---

## Litteraturevidens

For alvorlig ikke-proliferativ diabetisk retinopati finnes ingen relevant litteratur i datagrunnlaget. For den bredere prediksjonen diabetisk retinopati ble to publikasjoner identifisert. Ingen av dem evaluerer retinopati som utfall:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | Observasjonsstudie/oversikt (antatt ut fra tittel) | Diabetes, Obesity & Metabolism | Denosumab ved osteoporose var knyttet til lavere forekomst av type 2-diabetes, lavere risiko for fotsår og lavere dødelighet sammenlignet med bisfosfonater. Analyse av reelle kohortdata med systematisk oversikt og metaanalyse. |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | Observasjonsstudie/kohort (antatt ut fra tittel) | Cureus | Vurdering av bruken av FRAX-verktøyet for risiko for brudd hos voksne med type 2-diabetes. Omhandler ikke denosumab mot retinopati. |

---

## Markedsinformasjon for Norge

Alle 20 tillatelser er opphevet. Det er ingen gyldige tillatelser for tiden. Et utvalg:

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001120 | Prolia | – | Tap av benmasse, postmenopausal osteoporose, osteoporose |
| EMEA/H/C/002173 | Xgeva | – | Kjempecelletumor i bein, bentumorer |
| EMEA/H/C/006378 | Wyost | – | Kjempecelletumor i bein, bentumorer |
| EMEA/H/C/006507 | Rolcya | – | Osteoporose, postmenopausal osteoporose, tap av benmasse |
| EMEA/H/C/006526 | Evfraxy | – | Tap av benmasse, osteoporose, postmenopausal osteoporose |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Totalt 100 interaksjoner er registrert. Alle viste nivå **moderat** blant de 20 som er listet. Hovedgrupper:
  - Kortikosteroider: hydrokortison, triamcinolon (inkl. oftalmisk), deksametason, betametason, budesonid, prednisolon, prednison, metylprednisolon, kortikotropin og tetrakosaktid
  - Radiofarmaka/immunmodulerende kreftmidler: ibritumomab tiuxetan, jobenguan (I-131), tositumomab (med og uten I-131), levamisol
  - Andre: trimetreksat, merkaptopurin, dupilumab, takrolimus

Se preparatomtalen for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten kliniske studier eller direkte litteratur for retinopati. Alle norske tillatelser er dessuten opphevet, og sikkerhetsdata fra preparatomtale mangler.

**For å gå videre kreves:**
- Preparatomtale med advarsler og kontraindikasjoner fra DMP
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske data eller mekanistiske studier på RANKL/RANK i netthinnens mikrokarsykdom
- Retrospektive kohortstudier med retinopati som utfall hos denosumab-behandlede pasienter med diabetes
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

