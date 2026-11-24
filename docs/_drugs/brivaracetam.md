---
layout: default
title: Brivaracetam
parent: Kun modellprediksjon (L5)
nav_order: 66
evidence_level: L5
indication_count: 1
monitor_inn: "BRIVARACETAM"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-11-24
description: "Brivaracetam: predikert ny indikasjon beta-ketothiolase-mangel (beta-ketothiolase deficiency) (evidensnivå L5). Opprinnelig indikasjon: Epilepsy"
---

# Brivaracetam
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

## Brivaracetam: SV2A-modulator → beta-ketothiolase-mangel (beta-ketothiolase deficiency)
{: .text-alpha }

## Oppsummering i én setning

Brivaracetam er et legemiddel som brukes mot epilepsi.
TxGNN-modellen forutsier at det kan ha effekt ved **beta-ketothiolase-mangel (beta-ketothiolase deficiency)**,
men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen i dataene som er samlet inn for denne rapporten.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Epilepsy |
| Foreslått ny indikasjon | beta-ketothiolase-mangel (beta-ketothiolase deficiency) |
| TxGNN-prediksjonsscore | 0,9914 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (eller ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Brivaracetam (uoffisiell oversettelse): «Den nøyaktige mekanismen som BRIVIACT utøver sin antikonvulsive aktivitet ved, er ikke kjent. Brivaracetam viser høy og selektiv affinitet for synaptisk vesikkelprotein 2A (SV2A) i hjernen, noe som kan bidra til den antikonvulsive effekten.» Engelsk originaltekst: "The precise mechanism by which BRIVIACT exerts its anticonvulsant activity is not known. Brivaracetam displays a high and selective affinity for synaptic vesicle protein 2A (SV2A) in the brain, which may contribute to the anticonvulsant effect." ([DailyMed: Briviact (brivaracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c), versjon av 2026-11-05; hentet 2026-11-19). Brivaracetam er kjent som en modulator av det synaptiske vesikkelproteinet SV2A, og er et antiepileptikum.

Beta-ketothiolase-mangel er en medfødt feil i omsetningen av ketonlegemer og isoleucin. Det er ingen opplagt mekanistisk kobling mellom SV2A-modulering og denne metabolske sykdommen. Den høye modellscoren skyldes trolig en tilfeldig assosiasjon, for eksempel via anfallsrelaterte fenotyper under metabolske kriser. Likheten med den opprinnelige bruken er foreløpig ikke vurdert.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/003898 | Briviact (in Italy: Nubriveo) | Brivaracetam | Epilepsy | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Totalt 69 interaksjoner er registrert. Blant de viktigste:
- **Moderat:** morfin (inkl. liposomal), opium, dronabinol, nabilon, metoklopramid, difenoksin, difenoksylat, etanol, prometazin, sibutramin, klopidogrel
- **Mindre:** protonpumpehemmere (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol), klorpropamid, tolbutamid, cilostazol

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen mangler både kliniske studier og litteratur, og det finnes ingen plausibel mekanistisk kobling mellom brivaracetam og beta-ketothiolase-mangel. Evidensnivået er L5 (kun modellprediksjon).

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen
- Prekliniske eller mekanistiske studier som kan belyse en eventuell kobling til ketonlegeme- og isoleucinmetabolismen
- Vurdering av om prediksjonen skyldes anfallsrelaterte fenotyper snarere enn en reell sykdomsmekanisme

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Briviact (brivaracetam) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

