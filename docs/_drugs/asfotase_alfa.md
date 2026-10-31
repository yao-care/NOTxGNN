---
layout: default
title: Asfotase Alfa
parent: Kun modellprediksjon (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Asfotase Alfa: predikert ny indikasjon Mitokondriell oksidativ fosforyleringssykdom på grunn av kjerne-DNA-avvik (evidensnivå L5). Opprinnelig indikasjon: Hypofosfatasi"
monitor_inn: "ASFOTASE ALFA"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Steel syndrome", "exocrine pancreatic insufficiency", "Scheie syndrome", "Hurler syndrome", "lysosomal storage disease with skeletal involvement", "familial apolipoprotein C-II deficiency", "esophageal varices with bleeding", "esophageal varices without bleeding", "cystinosis"]
---

# Asfotase Alfa
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

## Asfotase alfa: Fra hypofosfatasi til mitokondriell oksidativ fosforyleringssykdom på grunn av kjerne-DNA-avvik
{: .text-alpha }

## Oppsummering i én setning

Asfotase alfa er en rekombinant enzymerstatningsterapi som opprinnelig brukes til behandling av **hypofosfatasi**.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **mitokondriell oksidativ fosforyleringssykdom på grunn av kjerne-DNA-avvik**,
men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hypofosfatasi |
| Predikert ny indikasjon | Mitokondriell oksidativ fosforyleringssykdom på grunn av kjerne-DNA-avvik |
| TxGNN-prediksjonsscore | 0.9995 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (u)rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i de innsamlede dataene. Basert på kjent informasjon er asfotase alfa et rekombinant fusjonsprotein av vevsuspesifikk alkalisk fosfatase (TNSALP). Det spalter ekstracellulære substrater som uorganisk pyrofosfat, pyridoksal-5'-fosfat og fosfoetanolamin. Virkningen er godt dokumentert ved hypofosfatasi.

Mitokondrielle OXPHOS-sykdommer skyldes derimot defekter i den intracellulære energiproduksjonen. Det er usannsynlig at en ekstracellulær enzymerstatning kan korrigere dette. Det finnes ingen etablert mekanistisk kobling mellom TNSALP-veien og mitokondriell oksidativ fosforylering.

Den høye TxGNN-scoren ser ut til å være en grafbasert prediksjon uten biologisk støtte. Den bør derfor tolkes med stor forsiktighet.

### Andre predikerte indikasjoner (alle L5, Hold)

Ingen av de ni andre toppkandidatene har kliniske studier eller litteratur. Vurderingene av mekanismen er oppsummert nedenfor.

| Rang | Sykdom | TxGNN-score | Vurdering |
|---|---|---|---|
| 2 | Steel syndrom | 0,9991 | Kun indirekte kobling via skjelettfenotyper; ingen kjent involvering av TNSALP/pyrofosfat-veien |
| 3 | Eksokrin pankreasinsuffisiens | 0,9989 | Ingen plausibel mekanisme; behandles med oral enzymerstatning |
| 4 | Scheie syndrom | 0,9985 | Mangel på alfa-L-iduronidase; asfotase alfa virker ikke på dette substratet |
| 5 | Hurler syndrom | 0,9975 | Annet enzymmål; etablert behandling er laronidase og stamcelletransplantasjon |
| 6 | Lysosomal lagringssykdom med skjelettinvolvering | 0,9973 | Bred, heterogen kategori; ingen evidens |
| 7 | Familiær apolipoprotein C-II-mangel | 0,9971 | Ingen rolle i lipidmetabolismen |
| 8 | Øsofagusvaricer med blødning | 0,9968 | Skyldes portal hypertensjon; scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens |
| 9 | Øsofagusvaricer uten blødning | 0,9968 | Samme begrunnelse som over |
| 10 | Cystinose | 0,9965 | Defekt cystintransport; svak overlapp via nyrerelatert beinsykdom |

---

## Evidens fra kliniske studier

Foreløpig er det ikke registrert noen relaterte kliniske studier.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003794 | Strensiq | Ikke oppgitt | Hypofosfatasi |

Tillatelsen er registrert som avregistrert (innehaver: Alexion Europe SAS). Det finnes 1 gyldig tillatelse av 1.

---

## Sikkerhetsvurderinger

Det foreligger ingen tilgjengelige data om advarsler eller kontraindikasjoner i de innsamlede dataene. Ingen legemiddelinteraksjoner ble funnet. Se preparatomtalen (SPC) for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er rent modellbasert (L5) uten kliniske studier eller litteratur, og det finnes ingen plausibel biologisk kobling mellom en ekstracellulær TNSALP-erstatning og intracellulære mitokondrielle defekter.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende hull i sikkerhetsscreeningen)
- Prekliniske data eller mekanistiske studier som kan støtte en kobling til mitokondriell OXPHOS-sykdom
- Avklaring av tilgjengelighet og markedsstatus i Norge, siden den eneste tillatelsen er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

