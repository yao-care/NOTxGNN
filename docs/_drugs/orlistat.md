---
layout: default
title: Orlistat
parent: Kun modellprediksjon (L5)
nav_order: 300
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Orlistat: predikert ny indikasjon Hypervitaminose (evidensnivå L5). Opprinnelig indikasjon: Fedme"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Orlistat: Fra fedme til hypervitaminose
{: .text-alpha }

## Oppsummering i én setning

Orlistat er en hemmer av mage- og bukspyttkjertellipase, opprinnelig brukt til behandling av fedme.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **hypervitaminose**,
men for øyeblikket finnes **0 kliniske studier** og **0 publikasjoner** i de samlede dataene som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Fedme |
| Predikert ny indikasjon | Hypervitaminose |
| TxGNN-prediksjonsscore | 99,42 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (ingen gyldige tillatelser) |
| Antall tillatelser | 2 (begge trukket tilbake) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) fra kildeposten er ikke tilgjengelige. Resonnementet nedenfor bygger derfor på generell farmakologisk kunnskap, ikke på de innsamlede dataene.

Orlistat hemmer mage- og bukspyttkjertellipase og reduserer opptaket av fett fra kosten med omtrent 30 %. Fettløselige vitaminer (A, D, E og K) tas opp sammen med fett i kosten. Teoretisk kan orlistat dermed redusere opptaket av disse vitaminene og kunne hjelpe ved overskudd av fettløselige vitaminer.

Koblingen er plausibel, men spekulativ. Den kjente effekten av orlistat er vitaminmangel, som er en merket bivirkning og krever tilskudd. Det finnes ingen dokumentasjon for at orlistat er en trygg eller effektiv behandling av hypervitaminose. Standardbehandlingen (stans av tilskuddet, støttebehandling og kalsium eller andre midler ved vitamin D-toksisitet) er veletablert, så det udekkede behovet for dette legemidlet er lavt. Den høye TxGNN-scoren (0,994) er kun en modellprediksjon.

---

## Klinisk studiedokumentasjon

For øyeblikket er det ikke registrert noen relevante kliniske studier.

---

## Litteraturdokumentasjon

For øyeblikket finnes det ingen relevant litteratur.

---

## Markedsinformasjon for Norge

Begge tillatelsene er trukket tilbake. Ingen gyldige tillatelser er registrert.

| Tillatelsesnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000854 | Alli (tidligere Orlistat GSK) | – | Fedme |
| EMEA/H/C/000154 | Xenical | – | Fedme |

---

## Sikkerhetshensyn

- **Kontraindikasjoner fra kunnskapsgrafen (TxGNN/PrimeKG, ikke preparatomtale):** leversvikt, primær hyperoksaluri, anorexia nervosa, bulimia nervosa, vitaminmangeltilstander, kolestase, godartet tilbakevendende intrahepatisk kolestase, familiær intrahepatisk kolestase og legemiddelindusert leverskade.
- **Legemiddelinteraksjoner:** 100 interaksjoner ble funnet i søket. Av de 20 som er oppført, er de fleste av moderat alvorlighetsgrad. Eksempler:
  - Moderat: abakavir, lamivudin, emtricitabin, atazanavir (HIV-legemidler); akarbose, albiglutid, alogliptin, kanagliflozin, klorpropamid, metformin (diabetesmidler); amiodaron; asparaginase (E. coli og Erwinia chrysanthemi); kalaspargase pegol; brentuksimab vedotin; klofarabin; kannabidiol.
  - Mindre: kolekalsiferol, kalsifediol, kalsitriol (vitamin D-former).

Opplysninger om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5), uten kliniske studier eller litteratur. Orlistats kjente effekt på fettløselige vitaminer er en bivirkning, og standardbehandlingen av hypervitaminose er godt etablert. Legemidlet har dessuten ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske eller kliniske data som viser at redusert vitaminopptak er terapeutisk nyttig ved hypervitaminose
- Vurdering av regulatorisk status, siden begge tillatelsene i Norge er trukket tilbake
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

