---
layout: default
title: Vismodegib
parent: Kun modellprediksjon (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: Fra basalcellekarsinom til medulloblastom med omfattende nodularitet

## Ensetnings oppsummering

> Vismodegib er en Smoothened (SMO)-hemmer hvis faktisk godkjent bruk er for lokalt avansert/metastatisk basalcellekarsinom (BCC) — som reflektert i denne evidenspakkens egen rang-9-kandidat, som har sterkt klinisk prøvestøtte.
> TxGNN-modellens **topprankerte** prediksjon peker imidlertid på **medulloblastom med omfattende nodularitet**, en SHH-vei-drevet hjernetumor.
> Denne spesifikke prediksjonen støttes for øyeblikket av **0 kliniske studier** og **0 publikasjoner** i dette datasettet — den mekanistiske begrunnelsen er sterk, men bevissekvensen må fortsatt bygges opp.

---

## Rask oversikt

| Emne | Innhold |
|------|---------|
| Original indikasjon | Ikke tilgjengelig fra norsk lisensdata (legemiddel ikke markedsført). Basert på kontekst fra evidenspakken (rang-9 begrunnelse), er vismodegib's kjente faktisk godkjente indikasjon lokalt avansert/metastatisk basalcellekarsinom (BCC) |
| Predikert ny indikasjon | Medulloblastom med omfattende nodularitet |
| TxGNN-prediksjonspoeng | 99.93% |
| Evidensnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Vismodegib er en Smoothened (SMO)-antagonist som blokkerer Hedgehog (Hh)-signalveien. Dette offisielle MOA-feltet er markert som en datakløft i denne pakken, men mekanismen er konsekvent beskrevet gjennom pakkens egne begrunnelsestekster og sitert litteratur (f.eks. PMID 22679179, PMID 24756807): vismodegib binder SMO og forhindrer uønsket aktivering av GLI-transkripsjonfaktorer, og undertrycker tumorproliferasjon i Hh-drevne kreftformer.

Den predikerte indikasjonen — SHH-subtype medulloblastom — er mekanistisk godt matchet: denne hjernekreften er direkte avhengig av konstant Hedgehog-signalveien aktivering, den samme veien vismodegib ble designet til å blokkere. Dette er analogt til vismodegib's etablerte og faktisk godkjente bruk i BCC, hvor PTCH1/SMO-vei mutasjoner driver tumorigenese (se rang-9-kandidaten "hudkreft" i denne samme pakken, som viser storskala fase II-prøvestøtte, f.eks. NCT01367665, n=1232).

Bemerkelsesverdig nok noterer begrunnelsen knyttet til denne topprankerte prediksjonen eksplisitt: *"現實世界中 vismodegib 已核准用於成人復發性/轉移性髓母細胞瘤"* (vismodegib er allerede godkjent i den reelle verden for voksen tilbakevendende/metastatisk medulloblastom). Dette tyder på at TxGNN-modellen har korrekt identifisert et mekanistisk og klinisk gyldig signal — fraværet av prøver/litteratur i dette spesifikke datasettet reflekterer sannsynlig en kløft i bevisinnsamling/indeksering for dette eksakte indikasjonsbegrepet, snarere enn et fravær av reell-verdens bevis. Denne kløften bør lukkes med målrettet litteratursøk før framgang.

---

## Klinisk prøvebevis

For øyeblikket ingen relaterte kliniske studier registrert

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig

---

## Norsk markedsinformasjon

Ingen markedsføringsgodkjenningsdata tilgjengelig — vismodegib er ikke for øyeblikket markedsført i Norge (0 godkjennelser på fil).

---

## Cytotoksisitet

Vismodegib er et antineoplastisk agens (Hedgehog-vei hemmer brukt i kreftiindikasjonene), så denne delen gjelder.

| Emne | Innhold |
|------|---------|
| Cytotoksisitetsklassifikasjon | Målrettet terapi (Hedgehog-vei / Smoothened-hemmer) — ikke en konvensjonell cytotoksisk kjemoterapi-agens |
| Myelosuppresjonrisiko | Vennligst se pakningsvedleggets advarsler og forsiktighetsregler |
| Emetogenisitetsklassifikasjon | Vennligst se pakningsvedleggets advarsler og forsiktighetsregler |
| Overvåkingselementer | Vennligst se pakningsvedleggets advarsler og forsiktighetsregler |
| Håndteringsbeskyttelse | Vennligst se pakningsvedleggets advarsler og forsiktighetsregler |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: TFDA/etikett advarsler og kontraindikasjoner er flagget som en **blokkering** datakløft [DG001] i denne evidenspakken — dette må løses før en S1-sikkerhetsevaluering kan finne sted.)*

---

## Konklusjon og neste skritt

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-poengsum for denne indikasjonen er veldig høyt (99.93%), og den mekanistiske begrunnelsen (SHH-vei-avhengighet i medulloblastom) er solid og konsekvent med vismodegib's kjente faktisk godkjente bruk i verden. Imidlertid gir dette datasettet for øyeblikket **null kliniske studier og null litteratursiteringer** for denne spesifikke indikasjonen, noe som plasserer det på evidensnivå L5 — modellprediksjon bare, uten korroborerende studiebevis samlet ennå.

**For å fortsette, trengs følgende:**
- Målrettet litteratur-/studiesøk for "vismodegib + medulloblastom" (selve begrunnelsesteksten indikerer at faktisk godkjenning eksisterer — dette må uthentes og legges til evidenspakken)
- TFDA/produktetikett advarsler og kontraindikasjoner (DG001, blokkering alvorlighetsgrad — forhindrer for øyeblikket S1-sikkerhetsevaluering)
- Formell virkningsmekanisme (MOA) dokumentasjon fra DrugBank (DG002, høy alvorlighetsgrad)
- Vurdering av norsk markedsføringsgodkjenningsprosess, siden legemidlet for øyeblikket ikke er markedsført der

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

