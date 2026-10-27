---
layout: default
title: Galcanezumab
parent: Kun modellprediksjon (L5)
nav_order: 184
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Galcanezumab: predikert ny indikasjon Heparinkofaktor 2-mangel (evidensnivå L5). Opprinnelig indikasjon: Migrene (Migraine Disorders)"
monitor_inn: "GALCANEZUMAB"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Galcanezumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Galcanezumab: Fra migrene til heparinkofaktor 2-mangel
{: .text-alpha }

## Sammendrag i én setning

Galcanezumab er et monoklonalt antistoff som opprinnelig brukes til å behandle migrene.
TxGNN-modellen forutsier at det kan være effektivt mot **heparinkofaktor 2-mangel**,
men de data som er sammenstilt for denne rapporten inneholder **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Migrene (Migraine Disorders) |
| Predikert ny indikasjon | Heparinkofaktor 2-mangel |
| TxGNN-prediksjonsscore | 99,50 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (kansellert) |
| Antall markedsføringstillatelser | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i de sammenstilte dataene. Galcanezumab er imidlertid kjent som et monoklonalt antistoff som nøytraliserer liganden CGRP (calcitonin gene-related peptide), og effekten ved migrene er knyttet til blokkering av denne signalveien.

Heparinkofaktor 2-mangel skyldes en defekt i et serinproteasehemmende protein (SERPIND1) i koagulasjonssystemet. Det er ikke identifisert noen plausibel biologisk kobling mellom CGRP-blokkade og denne tilstanden. Den høye TxGNN-scoren er en ren kunnskapsgraf-prediksjon uten støtte i mekanistiske, kliniske eller litteraturbaserte data.

**Andre predikerte indikasjoner med tilsvarende svak støtte** (alle L5, anbefaling Hold, ingen studier eller publikasjoner):

| Rangering | Predikert indikasjon | TxGNN-score | Kommentar |
|------|------|------|------|
| 2 | Antitrombinmangel type 2 | 99,41 % | Ingen mekanistisk sammenheng mellom CGRP-blokkade og SERPINC1-defekter. Å behandle en trombofil tilstand med et legemiddel uten kjent antikoagulerende effekt vekker sikkerhetsbekymringer. |
| 3 | Faktor 5-overskudd med spontan trombose | 99,41 % | Ingen kjent kobling. CGRP er en vasodilatator, så vaskulære effekter av CGRP-hemming må vurderes før et slikt forslag kan gå videre. |

---

## Klinisk studieevidens

Det finnes for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det finnes for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004648 | Emgality | – | Migrene (Migraine Disorders) |

Tillatelsen har status kansellert. Det finnes ingen gyldige tillatelser i dataene.

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

Merk likevel følgende fra den mekanistiske vurderingen: de predikerte indikasjonene gjelder trombotiske eller koagulasjonsrelaterte tilstander, og kardiovaskulær og trombotisk risiko ved CGRP-hemming (CGRP er en vasodilatator) er ikke adressert i dataene.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene bygger utelukkende på en kunnskapsgrafscore (evidensnivå L5) uten kliniske studier, litteratur eller plausibel mekanistisk kobling. I tillegg er den eneste markedsføringstillatelsen i Norge kansellert, og relevante sikkerhetsdata mangler.

**For å gå videre kreves følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (hindrer for øyeblikket sikkerhetsscreening)
- Detaljerte data om virkningsmekanisme (MOA) fra DrugBank
- Mekanistisk eller prekliniske data som kan knytte CGRP-blokkade til koagulasjonsveiene
- Sikkerhetsvurdering av vaskulære og trombotiske effekter ved CGRP-hemming i pasientgrupper med trombofili
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

