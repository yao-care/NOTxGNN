---
layout: default
title: Brolucizumab
parent: Kun modellprediksjon (L5)
nav_order: 61
evidence_level: L5
indication_count: 4
---

# Brolucizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Brolucizumab: Fra økulær neovaskularisert sykdom til mitokondrielt oksidativt fosforyleringsforstyrrelse forårsaket av kjerne-DNA-anomalier

## Sammenfattelse i en setning

> Brolucizumab er klinisk kjent som intravetreal anti-VEGF-A-terapi for økulær neovaskularisert sykdom, selv om denne opprinnelige indikasjonen ikke er dokumentert i gjeldende norsk regulatorisk datasett.
> TxGNN-modellens toppprediksjon foreslår mulig effektivitet for **mitokondrielt oksidativt fosforyleringsforstyrrelse forårsaket av kjerne-DNA-anomalier**,
> men **0 kliniske prøver** og **0 publikasjoner** støtter for øyeblikket denne retningen, og legemidlet er ikke markedsført i Norge.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke dokumentert i norsk regulatorisk data. Kjent klinisk bruk (ifølge legemidlets virkningsmekanisme) er intravetreal anti-VEGF-terapi for økulær neovaskularisert sykdom. |
| Predikert ny indikasjon | Mitokondrielt oksidativt fosforyleringsforstyrrelse forårsaket av kjerne-DNA-anomalier |
| TxGNN-prediksjonspoengsum | 99.67% |
| Bevisgrad | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte virkningsmekanismedata ikke tilgjengelige fra DrugBank. Basert på informasjonen som er tilgjengelig i denne bevissamlingen, er brolucizumab et anti-VEGF-A enkelt-kjede antiststoffragment (scFv) administrert ved intravetreal injeksjon, som virker ved å blokkere VEGF-signalering for å redusere patologisk angiogenese i økulær sykdom.

Mitokondrielt oksidativt fosforyleringsforstyrrelse forårsaket av kjerne-DNA-anomalier er en metabolsk/energiproduksjonssykdom forårsaket av elektronenes transportkjededefekter — en patofysiologi uten kjent overlapping med VEGF-mediator angiogenese. Bevissamlingen selv sier eksplisitt at ingen biologisk vei forbinder de to tilstandene, og at denne høye TxGNN-poengsummen reflekterer en grafneural-nettverksrelasjonell slutning snarere enn et mekanistisk begrunnet signal.

Gitt fraværet av enhver støttende klinisk prøve eller litteraturbevis, og den eksplisitte mekanistiske frakobblingen som er notert i begrunnelsen, bør denne prediksjonen behandles som kun utforskende. Det er verdt å merke seg at de gjenværende rangerte prediksjoner for dette legemidlet (spiserørvariser med/uten blødning, eksokrin pankreatisk insuffisiens) viser samme mønster — høye TxGNN-poeng uten mekanistisk eller klinisk støtte, og når det gjelder spiserørvariseblødning, en begrunnelse som flaggmarkerer en *sannsynlig sikkerhetsbetenkeling i motsatt retning* (anti-VEGF-midler er forbundet med nedsatt vaskulær/sårheling og blødningsrisiko, som teoretisk kunne forverre snarere enn hjelpe en blødningsutsatt tilstand).

---

## Bevis fra kliniske prøver

For øyeblikket er det ikke registrert relaterte kliniske prøver

---

## Litteraturbevis

For øyeblikket er det ingen relatert litteratur tilgjengelig

---

## Norsk markedsinformasjon

Brolucizumab har for øyeblikket ingen markedsføringstillatelse i Norge (Ikke markedsført, 0 lisenser registrert). Ingen produkt-/doseringsform-/indikasjonsdata er tilgjengelige for tabulering.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*Merk: Advarsels-/kontraindikasjon-/DDI-data kunne ikke hentes fra de gjeldende datakilder. Dette er flaggmarkert i kildebevissamlingen som en blokkerende datagap (DG001) for sikkerhetsvurdering før gjennomføring.*

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
Topprangert prediksjon er støttet kun av en modellpoengsum (L5, ingen kliniske prøver eller litteratur), og den mekanistiske begrunnelsen i bevissamlingen selv konkluderer med at det ikke finnes noen kjent biologisk vei som forbinder brolucizumabs anti-VEGF-aktivitet til mitokondrielle oksidativt fosforyleringsforstyrrelse. Kombinert med legemidlets umarkedsførte status i Norge og en blokkering av sikkerhetsmerkingdata, er det ingen grunnlag for å fremme denne kandidaten på dette tidspunktet.

**For å fortsette, kreves følgende:**
- TFDA/produsent pakningsvedlegg (advarsler, kontraindikasjoer) — for øyeblikket blokkering (DG001)
- Bekreftet virkningsmekanisme via DrugBank API-spørring (DG002)
- Enhver preklinisk eller mekanistisk litteratur som direkte forbinder VEGF-hemming til kjerne-DNA-relaterte mitokondrielle forstyrrelse
- Ny vurdering av lavere rangerte prediksjoner (spiserørvariser, eksokrin pankreatisk insuffisiens) kun hvis uavhengig klinisk/mekanistisk bevis dukker opp, gitt blødningsrisikobetenkelig allerede notert for kandidaten med variseblødning

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

