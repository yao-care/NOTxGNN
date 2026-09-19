---
layout: default
title: Idebenone
parent: Kun modellprediksjon (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Idebenone
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Idebenone: Ingen godkjent indikasjon → Predikert ny indikasjon Hepatic Porphyria (hepatisk porfyri)

## Oppsummering i én setning

Idebenone er foreløpig uten godkjente indikasjoner på markedet, og er heller ikke markedsført i Norge. Offentlige data viser at det er et syntetisk CoQ10-lignende stoff som primært virker på elektrontransportkjeden i mitokondriene og har antioksidativ effekt. TxGNN-modellen predikerer at det kan være effektivt for **hepatisk porfyri (Hepatic Porphyria)**, men det finnes foreløpig **0 kliniske prøver** og **0 litteraturreferanser** som støtter denne retningen. Bevisnivået er det laveste: **L5** (ren modellpreduksjon).

---

## Rask oversikt

| Punkt | Innhold |
|------|---------|
| Opprinnelig indikasjon | Ingen godkjent indikasjon registrert (legemiddel Not marketed) |
| Predikert ny indikasjon | Hepatic porphyria (hepatisk porfyri) |
| TxGNN-prediksjonspoengsum | 99.92% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | Not marketed |
| Antall lisenser | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Fordi feltet `original_moa` i DrugBank er merket som en datahull, er denne delen basert på mekanismebeskrivelser levert i modellresonnementteksten: Idebenone er et syntetisk CoQ10 (koenzym Q10)-lignende stoff som hovedsakelig virker antioksidativt og støtter mitokondriens elektrontransportkjede – dets særegne egenskap er at det kan omgå Complex I og transportere elektroner direkte til Complex III. Derfor har det et teoretisk grunnlag i sykdommer der mitokondriens funksjon er svekket.

Imidlertid er patofysiologien ved hepatisk porfyri primært knyttet til enzymatiske defekter i hemebiosynteseveien, som fører til akkumulering av porfyrinprekursorer i lever eller røde blodceller. Det er ingen kjent direkte sammenheng mellom dette og mitokondriens oksidativ fosforylering. Med andre ord er TxGNN-skåren på 99.92% sannsynligvis et uttrykk for indirekte assosiasjoner i kunnskapsgrafen (for eksempel at begge er knyttet til «lever»-noden), snarere enn konkret bevis for farmakologisk mekanisme.

Dessuten inneholder denne Evidence Pack 10 TxGNN-predikerte indikasjoner. Bortsett fra hepatisk porfyri som denne rapporten fokuserer på, har de øvrige 9 (som idiopathic copper-associated cirrhosis, primitive portal vein thrombosis, immune-mediated necrotizing myopathy, osv.) bevisnivå L5. Kun 2 av dem (immune-mediated necrotizing myopathy, antisynthetase syndrome) er merket som S1 «Research Question» fordi de har høyere mekanismelikhet med idebenones kjente mitokondrielle muskelapplikasjon (som Duchenne muskeldystrofi); resten er S0 «Hold».

---

## Bevis fra kliniske prøver

Det finnes ingen relaterte kliniske prøveregistreringer for øyeblikket.

---

## Litteraturbevis

Det finnes ingen relatert litteraturdata for øyeblikket.

---

## Markedsinformasjon for Norge

Idebenone er foreløpig **ikke markedsført i Norge**. Det finnes ingen gyldige lisenser (total_licenses = 0), så det er ingen godkjente produktinformasjoner å oppgi.

---

## Sikkerhetshensyn

Se legemiddelpakningsvedlegget for fullstendig sikkerhetsinformasjon.

> Tilleggsmerknad: Denne Evidence Pack merker TFDA-pakningsvedleggets advarsler/kontraindikasjoner (DG001) som **Blocking**-nivå datahull, noe som betyr at før disse dataene finnes, **kan denne kandidaten ikke gå videre til S1-sikkerhetsvurderingsstadium**. Dette er en nøkkelgrunn til at beslutningen er Hold.

---

## Konklusjon og påfølgende anbefalinger

**Beslutning: Hold**

**Grunn:**
- Første rangeerte predikerte indikasjon (hepatisk porfyri) har bevisnivå L5, uten noen klinisk prøve eller litteraturstøtte. Mekanismekoblingen vurderes også som svak (ren grafassociasjonspreduksjon).
- Sikkerhetsdatahull (DMP-pakningsvedleggets advarsler/kontraindikasjoner) er på Blocking-nivå. I henhold til gjeldende regler kan modellen ikke gå videre til S1-sikkerhetsvurdering.

**For å kunne gå videre, må følgende legges til:**
- TFDA-pakningsvedleggets advarsler og kontraindikasjoner (DG001, Blocking)
- DrugBank fullstendig virkningsmekanisme (MOA) data for å styrke mekanisme-assosiasjonsanalysen (DG002, High)
- Samle inn preklinisk eller pasientdokumentasjon for kandidatindikasjoner med høyere mekanismerimeligket (immune-mediated necrotizing myopathy, antisynthetase syndrome) som utgangspunkt for senere verifisering av forskningshypotese

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

