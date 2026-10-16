---
layout: default
title: Lipegfilgrastim
parent: Kun modellprediksjon (L5)
nav_order: 247
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Lipegfilgrastim: predikert ny indikasjon Primær frigjøringsforstyrrelse i blodplater (evidensnivå L5). Opprinnelig indikasjon: Ikke tilgjengelig i dataene"
monitor_inn: "LIPEGFILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "severe nonproliferative diabetic retinopathy", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "diabetic retinopathy"]
---

# Lipegfilgrastim
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Lipegfilgrastim: Fra et ikke-angitt opprinnelig bruksområde til primær frigjøringsforstyrrelse i blodplater

## Oppsummering i én setning

Lipegfilgrastim er en pegylert G-CSF-analog (vekstfaktor for hvite blodceller). Data som er samlet inn for denne rapporten oppgir ikke noe opprinnelig godkjent bruksområde.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **primær frigjøringsforstyrrelse i blodplater**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter prediksjonen. Den er kun en modellbasert beregning.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke tilgjengelig i dataene |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse i blodplater |
| TxGNN-prediksjonsscore | 99,93 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige. Lipegfilgrastim er en pegylert G-CSF-analog som virker på nøytrofil-linjen via G-CSF-reseptoren.

Primær frigjøringsforstyrrelse i blodplater er en kvalitativ funksjonsdefekt i blodplatene. Det er ikke påvist noen etablert mekanistisk sammenheng mellom G-CSF-signalering og denne tilstanden. Den høye TxGNN-scoren (0,999) er en prediksjon fra kunnskapsgrafen, uten støtte fra studier eller litteratur. Prediksjonen bør derfor tolkes med stor forsiktighet.

### Andre predikerte indikasjoner (alle L5, Hold)

| Rang | Predikert indikasjon | TxGNN-score | Vurdering |
|------|------|------|------|
| 2 | Alvorlig ikke-proliferativ diabetisk retinopati | 99,91 % | Ingen etablert kobling. Mulig spekulativ sammenheng via stamcellebiologi (endotelprogenitorceller), men G-CSF-indusert inflammasjon eller nydannelse av kar kan potensielt være skadelig i netthinnen. |
| 3 | Pseudo-von Willebrands sykdom | 99,91 % | Skyldes en «gain-of-function»-defekt i platereseptoren GPIbα. Ingen plausibel mekanisme fra G-CSF-reseptoragonisme. Høy score gjenspeiler trolig nærhet i nettverket mellom blødnings- og blodplatesykdommer. |
| 4 | Glanzmanns trombasteni | 99,91 % | Skyldes mangel på eller dysfunksjon av integrin αIIbβ3. Lipegfilgrastim har ingen kjent effekt på dette integrinet eller på blodplateaggregasjon. Relevans kan høyst være indirekte (støttebehandling ved stamcelletransplantasjon). |
| 5 | Diabetisk retinopati | 99,75 % | Samme resonnement som for alvorlig ikke-proliferativ diabetisk retinopati. Kun spekulativ kobling og mulige sikkerhetsproblemer i netthinnen. |

---

## Klinisk evidens

Foreløpig er det ikke registrert relaterte kliniske studier.

---

## Litteraturevidens

Foreløpig finnes det ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002556 | Lonquex (Teva B.V.) | Ikke angitt | Ikke angitt (status: avregistrert) |

---

## Sikkerhetsvurderinger

Se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon. Dataene som er samlet inn for denne rapporten inneholder ingen opplysninger om advarsler, kontraindikasjoner eller legemiddelinteraksjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger utelukkende på en modellscore (evidensnivå L5), uten kliniske studier, litteratur eller en plausibel mekanistisk forklaring. I tillegg er den eneste kjente tillatelsen avregistrert, og sikkerhetsdata mangler.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Opplysninger om opprinnelig godkjent indikasjon og doseringsform
- Prekliniske eller mekanistiske studier som kan underbygge en kobling mellom G-CSF-signalering og blodplatefunksjon
- Vurdering av administrasjonsvei og tilgjengelighet i Norge, siden det ikke finnes noen gyldig tillatelse
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

