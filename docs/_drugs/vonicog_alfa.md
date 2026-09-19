---
layout: default
title: Vonicog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Vonicog Alfa
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

# Vonicog alfa: Fra von Willebrand-sykdom til primær frigivelses-forstyrrelse av blodplater

## Oppsummering i en setning

> Vonicog alfa er en rekombinant von Willebrand-faktor (rVWF), etablert for behandling av von Willebrand-sykdom (VWD) — dette er tydelig fra den kliniske forsøks- og litteraturkonteksten i denne bevissamlingen, selv om et strukturert «originalindikasjon»-felt ikke er populert.
> TxGNN-modellen forutsier at det kan være effektivt for **primær frigivelses-forstyrrelse av blodplater**,
> men for tiden **ingen kliniske forsøk** og **ingen publikasjoner** støtter denne spesifikke retningen, og pakketens egen mekanistiske gjennomgang markerer eksplisitt at det biologiske grunnlaget er svakt.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Von Willebrand-sykdom (VWD) — utledet fra stoffets etablerte bruk som rVWF, som gjenspeilt gjennom hele forsøks-/litteraturbeviset i denne pakken; ikke uavhengig bekreftet via norske lisensregistre (ingen på fil) |
| Forutsagt ny indikasjon | Primær frigivelses-forstyrrelse av blodplater |
| TxGNN-prediksjonscore | 99.98% |
| Bevisnivå | L5 (modellprediksjon kun, ingen støttende forsøk eller litteratur) |
| Status på norsk marked | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Utsett |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme for vonicog alfa er ikke tilgjengelig i denne bevissamlingen (merket som datagap med høy alvorlighetsgrad, DG002). Basert på tilgjengelig informasjon er vonicog alfa en rekombinant von Willebrand-faktor (rVWF) som medierer blodplatenes **adhesjon** til steder med vaskulær skade og stabiliserer sirkulerende faktor VIII — dette er mekanismen som ligger til grunn for dens påviste bruk ved von Willebrand-sykdom.

Primær frigivelses-forstyrrelse av blodplater (f.eks. platelet-lagringspol-sykdom) er mekanistisk distinkt: den involverer en defekt i blodplatenes **granulfreisetting**, ikke blodplate-adhesjon. Bevissamlingens egen mekanistiske begrunnelse for denne kandidaten slår tydelig fast at «vWF primært medierer blodplatenes adhesjon snarere enn granulfreisetting-funksjon, og dens mekanistiske relevans til frigivelses-forstyrrelser av blodplater er svak — dette er rent og slett en høyt-scorende TxGNN-prediksjon uten direkte biologisk grunnlag som støtter terapeutisk effekt.»

Med andre ord reflekterer den meget høye TxGNN-scoren (99.98%) en sterk nettverksnivå-assosiasjon i modellen, men er ikke bekreftet av en plausibel årsaksmekanisme, og heller ikke av noen klinisk eller litteraturbevis. Dette er et lærebokeksempel på hvor en høy prediksjonscore alene ikke er tilstrekkelig til å støtte en kandidat som skal fremmes.

---

## Bevis fra kliniske forsøk

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er det ingen relatert litteratur tilgjengelig.

---

## Informasjon om norsk marked

Vonicog alfa har for tiden ingen markedsføringsgodkjenning i Norge (0 lisenser på fil). Ingen produkt-nivå dosisformulering eller godkjent-indikasjon-data er tilgjengelig for dette markedet.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Merknad: viktige advarsler, kontraindikasjoner, og stoff-stoff interaksjonsdata er ikke tilgjengelig i denne bevissamlingen — dette er merket som datagap med blokkerings-alvorlighetsgrad, DG001, siden sikkerhetdata fra TFDA/etikett ennå ikke er hentet. Dette datagap må løses før noen S1 sikkerhetspre-screening kan fortsette for dette legemidlet.)*

---

## Andre forutsagte indikasjoner under evaluering

Denne bevissamlingen evaluerte 10 TxGNN-forutsagte indikasjoner for vonicog alfa. De fleste deler det samme problemet som topprangerte kandidat — meget høye score med svak eller motsigende mekanistisk støtte og ingen klinisk/litteraturbevis. En kandidat skiller seg ut som materielt annerledes:

| Rangering | Sykdom | Score | Bevisnivå | Anbefaling | Merknad |
|-----------|--------|-------|-----------|-----------|---------|
| 1 | Primær frigivelses-forstyrrelse av blodplater | 99.98% | L5 | Utsett | Svak mekanisme (adhesjon vs. frigivelse) |
| 2 | Glanzmann-trombasteni | 99.98% | L5 | Utsett | Reseptordefisiens, vWF kan ikke kompensere |
| 3 | Pseudo-von Willebrand-sykdom | 99.97% | L5 | Utsett | Mekanisme går motsatt av terapeutisk hensikt |
| **4** | **Hemofili** | 99.95% | **L3** | **Forskningsspørsmål** | **4 fase 3-forsøk + 1 RCT (Blood, 2022); etikett-/navnmismatch med VWD-forsøk — trenger avklaring** |
| 5 | Scott-syndrom | 99.95% | L5 | Utsett | Ingen mekanistisk overlapp |
| 6 | Ervervet koagulasjonsfaktor-defisiens | 99.94% | L5 | Forskningsspørsmål | Plausibel faktor VIII-stabiliserings-begrunnelse, men ingen bevis |
| 7 | Von Willebrand-sykdom, X-koblet form | 99.92% | L4 | Forskningsspørsmål | Direkte målmatch, men atypisk arvemønster-merking |
| 8 | Blødningsdiates (kollagen-reseptor-defekt) | 99.92% | L5 | Utsett | Ikke-kompensabel reseptor-defekt |
| 9 | Blødningsforstyrelse (konstitusjonell trombocytopeni) | 99.92% | L5 | Utsett | vWF kan ikke korrigere blodpladantall |
| 10 | «Flood factor-defisiens» | 99.90% | L5 | Utsett | Sannsynlig datainntastingsfeil; uklar sykdomsenhet |

Rangering 4 («hemofili») er den eneste kandidaten i denne pakken med meningsfull klinisk forsøks- og litteraturstøtte (L3, S1). Imidlertid rekrutterte de underliggende forsøkene (NCT03879135, NCT02973087, NCT02932618) og nøkkel-RCT (PMID 35439298, *Blood*, 2022) alle faktisk **alvorlig VWD**-pasienter snarere enn klassisk hemofili A/B-populasjoner — dette antyder en etikett/ontologi-overlapp (VWD type 2N som presenterer seg med hemofili-lignende fenotype) snarere enn et genuint ombruksignal til primær hemofili. Denne kandidaten fortjener sin egen fokusert evaluering snarere enn å bli behandlet som ekvivalent med rangering 1-prediksjonen diskutert ovenfor.

---

## Konklusjon og neste trinn

**Beslutning: Utsett**

**Begrunnelse:**
Høyest-rangerte prediksjon (primær frigivelses-forstyrrelse av blodplater) har ingen klinisk forsøks- eller litteraturstøtte, og bevissamlingens egen mekanistiske analyse slår eksplisitt fast at det ikke er noe direkte biologisk grunnlag for effektivitet — den høye TxGNN-scoren alene er ikke tilstrekkelig til å fortsette. I tillegg mangler stoff-nivå sikkerhetdata (TFDA advarsler/kontraindikasjoner) og er merket som blokkerings-gap, så selv en Forskningsspørsmål-nivå kandidat kunne ikke klare S1 sikkerhetspre-screening på dette tidspunktet.

**For å fortsette, trengs følgende:**
- Løs DG001 (Blokkering): hent TFDA/etikettadvarsler og kontraindikasjoner før noen S1 sikkerhetspre-screening
- Løs DG002 (Høy): hent bekreftet MOA-data fra DrugBank for å vurdere mekanistisk plausibilitet ordentlig
- Hvis du forfølger ombruksarbeid på dette legemidlet, omdirigert fokus til **Rangering 4 (hemofili)**, som allerede har L3-bevis, og avklare først om de underliggende forsøkene representerer ekte hemofili A/B eller VWD-hemofili fenotype-overlapp
- Prekliniske eller mekanistiske studier som spesifikt tester vWF rollen i blodplatenes granulfreisettings-mekanismer, hvis frigivelses-forstyrrelse-hypotesen skal forfølges videre

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

