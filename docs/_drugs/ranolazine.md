---
layout: default
title: Ranolazine
parent: Kun modellprediksjon (L5)
nav_order: 347
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Ranolazine: predikert ny indikasjon Nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD) (evidensnivå L5). Opprinnelig indikasjon: Angina pectoris"
monitor_inn: "RANOLAZINE"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ranolazine
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

## Ranolazin: Fra angina pectoris til nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)
{: .text-alpha }

## Oppsummering i én setning

Ranolazin er et legemiddel som opprinnelig brukes til behandling av **angina pectoris** (brystsmerter ved hjertesykdom).
TxGNN-modellen forutsier at det kan være effektivt mot **nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD)**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er ren modellberegning.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Angina pectoris |
| Foreslått ny indikasjon | Nefrogent syndrom med uhensiktsmessig antidiurese (NSIAD) |
| TxGNN-prediksjonsscore | 0,9965 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanismen er ikke tilgjengelige i dataene som er samlet inn for denne rapporten. Ranolazin beskrives generelt som en hemmer av sen natriumstrøm (late INa) med tilleggseffekter på andre ionekanaler, men dette er ikke underbygget av de foreliggende dataene.

NSIAD er en ultrasjelden sykdom forårsaket av aktiverende mutasjoner i vasopressin V2-reseptoren (AVPR2), eller i noen tilfeller GNAS-relatert signalering. Dette gir konstant antidiurese uavhengig av vasopressin, med hyponatremi som hovedutfordring.

Det er ikke åpenbart noen sammenheng mellom hemming av sen natriumstrøm og V2-reseptorsignalering. Den høye scoren (0,9965) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Det kreves sterk mekanistisk begrunnelse før en slik kandidat kan vurderes videre.

---

## Evidens fra kliniske studier

Det er for tiden ingen relevante kliniske studier registrert.

---

## Litteraturevidens

Det er for tiden ingen relevant litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000805 | Ranexa (tidligere Latixa) | Ikke oppgitt | Angina pectoris |

Legemidlet er markedsført i Norge, med 1 gyldig markedsføringstillatelse av 1.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter ranolazin til følgende tilstander: langt QT-syndrom, familiært langt QT-syndrom, torsades de pointes, nyresykdom, pyoureter og levercirrhose. Disse bør verifiseres mot preparatomtalen.
- **Legemiddelinteraksjoner:** 100 interaksjoner er funnet totalt. Blant de 20 som er gjennomgått, er følgende klassifisert som **alvorlige (Major)**:
  - Aprepitant
  - Deksametason
  - Klaritromycin
  - Dolasetron
  - Eliglustat

  Flere interaksjoner er klassifisert som moderate (blant annet famotidin, metformin, loperamid, budesonid, kanagliflozin, dapagliflozin, empagliflozin, bisakodyl, pikosulfat, polyetylenglykol og natriumsulfat) og noen som mindre (bupropion, lorkaserin, cimetidin).

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellberegning (evidensnivå L5) uten kliniske studier eller publikasjoner, og det finnes ingen påvist mekanistisk kobling mellom ranolazin og NSIAD. I tillegg er den eneste godkjenningen i Norge kansellert, og kunnskapsgrafen indikerer flere potensielle kontraindikasjoner (blant annet QT-forlengelse og nyresykdom).

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank, og en mekanistisk analyse av en mulig kobling til AVPR2/GNAS-signalering
- Innhenting og gjennomgang av preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel for sikkerhetsscreening
- Prekliniske data (for eksempel cellemodeller med AVPR2-mutasjoner) som kan underbygge hypotesen
- Vurdering av QT-risiko og nyrefunksjon hos en så sjelden og sårbar pasientgruppe
- Avklaring av regulatorisk status og tilgjengelighet i Norge, siden godkjenningen er kansellert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

