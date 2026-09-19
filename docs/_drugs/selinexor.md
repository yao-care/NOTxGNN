---
layout: default
title: Selinexor
parent: Kun modellprediksjon (L5)
nav_order: 321
evidence_level: L5
indication_count: 1
---

# Selinexor
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Selinexor: Forutsagte indikasjoner under datakløfter — Legemiddel-indusert osteoporose

## Oppsummering i én setning

> Selinexor (DrugBank ID: DB11942) har for øyeblikket **manglende data for både originalindikasjon og virkningsmekanisme (MOA)**, og har ikke fått noen legemiddelgodkjenning i Taiwan (Norges registreringsdatabase).
> TxGNN-modellen forutsier at den kan være effektiv for **Legemiddel-indusert osteoporose**,
> men det finnes for øyeblikket **ingen kliniske forsøk, ingen litteratur** som støtter denne forbindelsen – det er rent en kunnskapsgraf-prediksjon.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ingen data (`original_indications` er tom matrise, `original_moa` merket som [Data Gap]) |
| Forutsagt ny indikasjon | Legemiddel-indusert osteoporose |
| TxGNN-prediksjonspoengsum | 99.22% |
| Bevisnivå | L5 (kun modellprediksjon, ingen faktisk forskning) |
| Norge (Taiwan) markedsstatus | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | **Hold** |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert virkningsmekanismeinformasjon for Selinexor er for øyeblikket ikke tilgjengelig (`original_moa` = [Data Gap]), og det finnes heller ingen registreringer av originalindikasjoner tilgjengelig for sammenligning. Siden data om virkningsmekanisme og originalindikasjon mangler, er det ikke mulig å etablere en farmakologisk forbindelse mellom "originalindikasjon → ny indikasjon".

I henhold til `repurposing_rationale.mechanistic_link` i bevisepakken: TxGNN-poeng på 0.992 er **ren kunnskapsgraf-koblingsprediksjon**, og datasettet selv gir ingen beskrivelse av biologiske mekanismer som støtter denne forbindelsen. Selv om ekstern offentlig informasjon muligens allerede kjenner til Selinexors farmakologiske klassifisering, krever denne rapporten i henhold til reglementene at kun data som er verifisert og sitert innenfor Evidence Pack brukes – ekstern kunnskap som ikke er verifisert av dette datasettet skal ikke substitueres direkte. Derfor vil denne mekanistiske forbindelsen **ikke bli tatt i betraktning**.

Med andre ord har denne prediksjonen for øyeblikket kun referanseverdi når det gjelder statistisk forbindelsesstyrke, og mangler både mekanistisk eller klinisk evidensstøtte.

---

## Bevis fra kliniske forsøk

Det finnes for øyeblikket ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

Det finnes for øyeblikket ingen relatert litteraturdata tilgjengelig.

---

## Norge (Taiwan) markedsinformasjon

Selinexor er for øyeblikket **ikke markedsført** på det lokale markedet (Norge/Taiwan registreringssystem), uten noen legemiddelgodkjennelsesregistreringer (`total_licenses` = 0), derfor finnes det ingen godkjennelsesinformasjon tilgjengelig for opplistning.

---

## Sikkerhetshensyn

Se legemiddelpakningsvedlegget for sikkerhetsinformasjon.

(`key_warnings` og `contraindications` er begge merket som datakløfter, `ddi.query_status` = not_found, ingen legemiddelinteraksjonsregistreringer finnes for presentasjon.)

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
- Denne kandidaten mangler for øyeblikket kliniske forsøk eller litteraturbevis som støtter det (Bevisnivå = L5) – det er kun ren kunnskapsgraf-modellprediksjonspoeng.
- I `data_gaps` er DG001 (DMP-pakningsvedlegg advarsler/kontraindikasjoner) merket som **Blocking**-nivå, som i henhold til reglene ikke tillater fortsettelse til S1-sikkerhetskontroll; DG002 (MOA) er High-nivå datakløft som begrenser mekanistisk-link-analyse.
- Legemidlet er ikke markedsført lokalt, uten faktisk klinisk erfaring med bruk eller sikkerhetserfaringer som kan refereres til.

**Følgende er nødvendig for å fortsette:**
- Supplere TFDA (eller tilsvarende regulatorisk myndighet) pakningsvedlegget med advarsler og kontraindikasjonsinformasjon for å fjerne DG001-blokkeringen
- Supplement virkningsmekanisme (MOA) data gjennom DrugBank API eller andre kilder for å løse DG002-kløften
- Supplement originalindikasjonregistreringer og etabler mekanistisk/klinisk rasjonalitet for legemiddel-indusert osteoporose
- Søk etter eventuelle kliniske forsøk (inkludert ICTRP) eller fagfellevurdert litteratur som kan støtte denne indikasjonsforbindelsen
- Bekreft legemiddelinteraksjon (DDI) data for påfølgende sikkerhetinitialvurdering (S1)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

