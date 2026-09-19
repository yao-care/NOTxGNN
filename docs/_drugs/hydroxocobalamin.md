---
layout: default
title: Hydroxocobalamin
parent: Kun modellprediksjon (L5)
nav_order: 170
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Hydroxocobalamin: Fra uspesifisert originalindikasjon til øsofagale variser (uten blødning)

## Oppsummering i én setning

Hydroxocobalamins opprinnelig godkjente indikasjon er ikke tilgjengelig i det nåværende datasettet (DrugBank-utdrag viser ingen originale indikasjoner og ingen Taiwan/Norge markedslisens eksisterer).
TxGNN-modellen forutsier potensiell effektivitet for **øsofagale variser uten blødning** (og, med en praktisk talt identisk poengsum, **øsofagale variser med blødning**),
men dette støttes for øyeblikket av **0 kliniske forsøk** og **0 publikasjoner** — dette er et rent modellforutsigelses-signal uten direkte kliniske eller prekliniske bevis.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke tilgjengelig — ingen originale indikasjoner registrert, og medikamentet er ennå ikke godkjent i Norge |
| Forutsagt ny indikasjon | Øsofagale variser uten blødning (rangering 1); øsofagale variser med blødning (rangering 2, samme poengsum) |
| TxGNN-forutsikelses-poengsum | 99.23% |
| Bevisgrad | L5 (modellforutsigelse kun, ingen støttende forsøk eller litteratur) |
| Norges markedsstatus | Not marketed (Not marketed) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne forutsielsen rimelig?

Detaljerte mekanisme-data for hydroxocobalamin er for øyeblikket merket som et datakrav-gap (DG002) og ikke tilgjengelig fra denne bevisspakken. Imidlertid gir modellens egen rasjonaliseringsfeld en mekanistisk hypotese: hydroxocobalamin er kjent for å sekvestre nitrogenmonoksid (NO-sekvestering), som produserer systemisk vasokonstriksjon — en egenskap som allerede utnyttes klinisk for tilstander som vasoplegisk sjokk og refraktær hypotensjon.

Denne samme vasokonstriksjonsmekanismen er det farmakologiske grunnlaget for etablerte øsofagale variser-terapier (f.eks. vasopressin, terlipressin, somatostatin), som reduserer portaltrykk. Dette gir "med blødning"-forutsielsen en plausibel fysiologisk rasjonale. "Uten blødning"-forutsielsen (primær profylakse) utvider denne logikken til langvarig, ikke-akutt bruk, noe som reiser ytterligere bekymringer — kronisk vasokonstriksjonseksponering (hypertensjonrisiko) og hydroxocobalamins kjente interferens med visse kolorimetriske laboratorie-analyser ville trenge separat evaluering.

Viktigst er det at denne mekanistiske forbindelsen er eksplisitt flagget i bevisspakken som inferensiell, ikke evidensbasert: det finnes ingen prekliniske eller kliniske studier som direkte tester hydroxocobalamin i noen av øsofagale variser-indikasjonene. Forbindelsen bør behandles som et hypotesegenererende signal kun.

## Klinisk forsøks-bevis

Ingen relaterte kliniske forsøk registrert for øyeblikket.

## Litteratur-bevis

Ingen relatert litteratur tilgjengelig for øyeblikket.

## Markedsinformasjon for Norge

Hydroxocobalamin er for øyeblikket **ikke markedsført i Norge** (markedsstatus: Not marketed) og har **0 godkjennelser** på rekord — ingen lisens eller godkjente-indikasjon data eksisterer for å oppsummere.

## Sikkerhetshensyn

Vennligst referer til pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner, og legemiddel-interaksjons data er alle for øyeblikket utilgjengelig — legemiddel-interaksjons-spørring returnerte ingen resultater, og TFDA-etikettadvarsler/kontraindikasjoner er merket som et **blokkerende** datakrav-gap, DG001.)

## Konklusjon og neste steg

**Beslutning: Avvent**

**Rasjonale:**
- Begge forutsielsene er L5 (modellforutsigelse kun) med null støttende forsøk eller litteratur, og et blokkerende datakrav-gap (manglende TFDA-etikett/advarsler) forhindrer selv en innledende sikkerhetsvurdering (S1).

**For å fortsette, er følgende nødvendig:**
- Løs DG001 (blokkerende): innhent og parse TFDA/produktetiketten for advarsler, kontraindikasjoner, og forholdsregler.
- Løs DG002: hent bekreftet virkningsmekanisme via DrugBank API.
- Etabler medikamentets faktiske originalindikasjon(er) og eventuelle eksisterende markedslisenser (ingen identifisert for øyeblikket).
- Gjennomfør et målrettet litteratur-/klinisk forsøks-søk spesifikt for hydroxocobalamin og portalt hypertensjon/øsofagale variser for å bevege seg utover modell-kun-bevis (L5 → høyere nivå).
- Hvis bevis dukker opp, evaluer rutekompabilitet (IV-formulering vs. påkrevd rute for øsofagale variser-behandling) og langtids-sikkerhet (hypertensjon, laboratorie-analyseinterferens) før fremgang forbi S0.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

