---
layout: default
title: Evolocumab
parent: Kun modellprediksjon (L5)
nav_order: 145
evidence_level: L5
indication_count: 6
---

# Evolocumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Evolocumab: TxGNN-forutsagt sammenheng med symptomatisk hemofili hos kvinnelige bærere (lavt konfidensnivå)

## Sammendrag i én setning

> Denne evidenspakken dokumenterer ikke evolocumabs opprinnelig godkjent indikasjon, og stoffet har for øyeblikket ingen markedslisens i Taiwan.
> TxGNNs høyest rangerte prediksjon antyder en mulig sammenheng med **symptomatisk hemofili hos kvinnelige bærere** (skår 99,82%),
> men dette støttes av **null kliniske studier** og **null publikasjoner** — og pakkens egen mekanistiske analyse viser at sammenhengen sannsynligvis er kunnskapsgraf-nærhetsstøy snarere enn en reell farmakologisk forbindelse.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke på fil (ingen Taiwan-lisenspost; `original_indications` tom i denne evidenspakken) |
| Forutsagt ny indikasjon | Symptomatisk hemofili hos kvinnelige bærere |
| TxGNN-prediksjons skår | 99,82% (rangering 2444) |
| Evidensnivå | L5 (modellprediksjon kun, ingen støttende studier/litteratur) |
| Taiwans markedsstatus | Ikke markedsført (Ikke markedsført) |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

I følge de mekanistiske notatene innebygd i denne evidenspakken, er evolocumab en **PCSK9-monoklonal antistoff**: det hemmer PCSK9-medieret nedbrytning av LDL-reseptorer, og senker derved blod-LDL-C. Dette plasserer stoffets kjente biologi klart innenfor lipidmetabolisme, ikke koagulasjon.

Hemofili hos kvinnelige bærere oppstår fra Factor VIII (F8)-genmangel og innebærer den intrinsic koagulasjonskaskaden — en vei som har **ingen dokumentert mekanistisk overlapping** med PCSK9/LDL-reseptor-biologi. Evidenspakkens egen begrunnelse for denne prediksjonen sier eksplisitt at det ikke finnes noen kjent interaksjon eller delt vei mellom de to, og konkluderer at den høye TxGNN-skåren sannsynligvis gjenspeiler **kunnskapsgraf-nærhetsstøy** snarere enn et genuint farmakologisk signal.

Denne vurderingen forsterkes av mønsteret på tvers av de andre fem rangerte kandidatene i denne pakken (familial ApoC-II-mangel, trombositopenisk purpura, Factor XI-mangel, hemofili A med vaskulær abnormitet, og en ikke-spesifikk ontologi-superklasse «sykdom av katalytisk aktivitet») — alle har samme L5/Avvent-status, ingen studier, ingen litteratur, og begrunnelsestekst som uavhengig argumenterer mot mekanistisk plausibilitet. Dette er ikke typisk for et sterkt omformål-signal.

---

## Evidens fra kliniske studier

For øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturbasert evidens

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Taiwans markedsinformasjon

Evolocumab har for øyeblikket **ingen markedsføringsgodkjenning i Taiwan** (0 lisenser på fil). Ingen doseringsform eller godkjent indiksjonstekst er tilgjengelig for denne jurisdiksjonen.

---

## Sikkerhetsoverveielser

Vær vennlig å referere til pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: viktige advarsler, kontraindikasjoner og stoff-interaksjonsdata er alle flagget som datahuller i denne evidenspakken — inkludert TFDA-merketdata, oppført som Blocking gap (DG001). Dette må løses før noen S1-sikkerhetsgjennomgang kan gjennomføres.)*

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-skåren er høy, men det er null kliniske studier, null publikasjoner, og ingen Taiwan-regulatoriske data som støtter denne prediksjonen. Enda viktigere, pakkens egen mekanistiske begrunnelse konkluderer uavhengig at PCSK9/LDL-stien har ingen kjent forbindelse til hemofilis patofysiologi, noe som antyder at skåren reflekterer en grafartifakt snarere enn et biologisk signal.

**For å gå videre, trengs følgende:**
- TFDA-ekvivalent produktmerking (advarsler/kontraindikasjoner) — for øyeblikket Blocking gap (DG001)
- Verifiserte virkningsmekanisme-data fra DrugBank eller primærlitteratur (DG002)
- Bekreftet opprinnelig indikasjon(er) for evolocumab i dette datasettet
- Et uavhengig litteratur-/klinisk-studie-søk spesifikt for evolocumab i blødningsforstyrrelser, for å bekrefte eller utelukke TxGNN-signalet før videre scoring
- Vurdering av hvorvidt denne kandidaten (og dens søskenprediksjoner i denne pakken) bør deprioriteres til fordel for TxGNN-kandidater med faktisk studie-/litteraturstøtte

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

