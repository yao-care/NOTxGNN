---
layout: default
title: Pretomanid
parent: Kun modellprediksjon (L5)
nav_order: 338
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Pretomanid: predikert ny indikasjon Candidiasis (evidensnivå L5). Opprinnelig indikasjon: Multiresistent tuberkulose"
monitor_inn: "PRETOMANID"
predicted_indications: ["candidiasis", "leprosy", "coronary artery disease", "myocardial ischemia", "anomalous left coronary artery from the pulmonary artery"]
---

# Pretomanid
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Pretomanid: Fra multiresistent tuberkulose til candidiasis
{: .text-alpha }

## Oppsummering i én setning

Pretomanid er et antibakterielt legemiddel mot mykobakterier, opprinnelig brukt til behandling av **multiresistent tuberkulose**.
TxGNN-modellen forutsier at det kan ha effekt mot **candidiasis**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen; prediksjonen er kun beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Multiresistent tuberkulose |
| Predikert ny indikasjon | Candidiasis |
| TxGNN-prediksjonsscore | 0,9969 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden foreligger det ikke detaljerte data om virkningsmekanismen i dataene som er samlet inn for denne rapporten. Basert på kjent informasjon er pretomanid et nitroimidazooksazin-prodrug som aktiveres av nitroreduktasen Ddn i *Mycobacterium tuberculosis*. Det hemmer syntesen av mykolsyre og frigjør nitrogenoksid under anaerobe forhold.

Sopp som *Candida* mangler både Ddn-veien og mykolsyrer. Det finnes derfor ingen mekanistisk kobling mellom den opprinnelige indikasjonen og candidiasis. Den svært høye TxGNN-scoren (0,9969) må tolkes som en ren beregningsmessig prediksjon uten biologisk eller klinisk validering.

For oversiktens skyld: blant de fem predikerte indikasjonene har **lepra** det mest plausible biologiske grunnlaget. *Mycobacterium leprae* er i slekt med *M. tuberculosis*, men det er ikke vist at M. leprae har et Ddn-lignende aktiverende enzym. Alle åtte publikasjoner som ble funnet under lepra-prediksjonen handler om legemiddelresistent tuberkulose og gir kun indirekte kontekst. De øvrige prediksjonene (koronarsykdom, hjerteiskemi og anomal venstre koronararterie fra lungearterien) har ingen rimelig mekanistisk begrunnelse.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Evidens fra litteratur

Foreløpig er det ingen relevant litteratur for candidiasis.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005167 | Dovprela (tidligere Pretomanid FGK) | Ikke oppgitt | Multiresistent tuberkulose |

Merk: Legemidlet er markedsført, og 1 av 1 tillatelser er gyldig.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er registrert 14 interaksjoner i databasen (DDInter).

- **Alvorlige (Major), 7 stk.:** deksametason, lumakaftor, apalutamid, dabrafenib, mitotan, lorlatinib, enzalutamid
- **Moderate, 7 stk.:** empagliflozin, sitagliptin, somatropin, somatrem, baricitinib, klofarabin, metotreksat

Mange av de alvorlige interaksjonene gjelder legemidler som påvirker metabolismeenzymer, og kombinasjoner bør vurderes nøye.

**Øvrig:** Pretomanid-regimer er forbundet med bekymring for QT-forlengelse ved kombinasjon med bedakilin/moksifloksacin. Dette er relevant dersom bruk ved hjertesykdom skulle vurderes.

Se preparatomtalen for fullstendig sikkerhetsinformasjon om advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for candidiasis har kun modellbasert støtte (evidensnivå L5), uten kliniske studier, litteratur eller en plausibel virkningsmekanisme. I tillegg er den norske tillatelsen avregistrert.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra legemiddelmyndighetene (blokkerende datamangel for sikkerhetsscreening)
- Laboratoriedata (in vitro) som viser eventuell aktivitet mot *Candida*
- Vurdering av lepra som en mer biologisk plausibel alternativ hypotese, med studier av Ddn-lignende enzymer i *M. leprae* og in vivo-følsomhet
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

