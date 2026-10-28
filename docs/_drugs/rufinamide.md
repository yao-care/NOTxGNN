---
layout: default
title: Rufinamide
parent: Kun modellprediksjon (L5)
nav_order: 371
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
monitor_inn: "RUFINAMIDE"
predicted_indications: ["perioral myoclonia with absences"]
description: "Rufinamide: predikert ny indikasjon Perioral myoclonia with absences (evidensnivå L5). Opprinnelig indikasjon: Epilepsy"
---

# Rufinamide
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

## Rufinamide: Perioral myoclonia with absences
{: .text-alpha }

## Oppsummering

Rufinamid er et legemiddel som opprinnelig brukes mot **epilepsi**. Etter det som er kjent fra generell farmakologi, er det godkjent for anfall ved Lennox-Gastaut-syndrom.
TxGNN-modellen predikerer at det kan være effektivt mot **febril infeksjonsrelatert epilepsisyndrom (FIRES)**.
Det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen, så prediksjonen er rent modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Epilepsy |
| Predikert ny indikasjon | Perioral myoclonia with absences |
| TxGNN-prediksjonsscore | 0.9951 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelige i det innsamlede materialet. Ut fra generell farmakologi antas rufinamid å forlenge den inaktive tilstanden til spenningsstyrte natriumkanaler, noe som kan dempe anfallsaktivitet. Legemidlet har dokumentert effekt ved epilepsi, og mekanistisk kan det tenkes å være relevant for andre epilepsiformer.

FIRES er en behandlingsresistent epileptisk encefalopati som oppstår etter feber, og har en tydelig nevroinflammatorisk komponent. Natriumkanalmodulering kan derfor trolig gi bare symptomatisk anfallsdemping, ikke behandling av selve inflammasjonen.

Modellen predikerer også fire andre epilepsisyndromer, alle med evidensnivå L5 og ingen studier eller litteratur:

| Rang | Predikert indikasjon | TxGNN-score | Merknad |
|------|------|------|------|
| 2 | Perioral myoklonus med absenser | 0,9951 | Natriumkanalblokkere kan forverre enkelte generaliserte absenser og myoklone anfall |

---

## Klinisk studieevidens

Foreløpig er det ingen registrerte kliniske studier knyttet til denne indikasjonen.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000660 | Inovelon (Eisai GmbH) | Ikke oppgitt | Epilepsi (status: godkjent) |

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke fra preparatomtale):** TxGNN-kunnskapsgrafen (PrimeKG) knytter rufinamid til følgende sykdommer: leversvikt, leversykdom, sykdom i galleblæren, leukopeni, angstlidelse, nevrotisk lidelse og dystymi. Disse bør verifiseres mot preparatomtalen.
- **Legemiddelinteraksjoner:** Det er registrert 100 interaksjoner, og de 20 første som er vist har alle alvorlighetsgrad moderat. Eksempler er:
  - Kortikosteroider: hydrokortison, prednison, triamcinolon, betametason
  - Vitamin D-forbindelser: kolekalsiferol, kalsifediol, kalsitriol
  - Opioider og beslektede: morfin, difenoksin, difenoksylat
  - Cannabinoider: dronabinol, nabilon
  - Kvalmehemmere: ondansetron, metoklopramid, rolapitant
  - Andre: pioglitazon, bupropion, eliglustat, naloksegol, nitisinon

Advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelige i dataene. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore uten støtte fra kliniske studier eller litteratur (evidensnivå L5). I tillegg er den eneste norske tillatelsen avregistrert, og sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre kreves følgende:**
- Hente og analysere advarsler og kontraindikasjoner fra preparatomtalen (blokkerende datamangel)
- Innhente data om virkningsmekanisme fra DrugBank
- Litteratursøk og søk etter kliniske studier om rufinamid ved FIRES og de andre predikerte syndromene
- Avklare rutekompatibilitet og likhet med den opprinnelige indikasjonen
- Avklare mulig markedsstatus i Norge, siden Inovelon er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

