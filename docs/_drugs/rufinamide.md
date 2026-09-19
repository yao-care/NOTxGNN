---
layout: default
title: Rufinamide
parent: Kun modellprediksjon (L5)
nav_order: 317
evidence_level: L5
indication_count: 5
---

# Rufinamide
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

# Rufinamid: Fra Lennox-Gastaut-syndrom til febril infeksjonsrelatert epilepsi-syndrom

## Sammendrag på en setning

> Rufinamid er et triazol-derivat antikonvulsivum; innen denne bevissamlingen refereres dets etablerte rolle kun indirekte som basisbehandling for Lennox-Gastaut-syndrom (feltet `original_indications` er tomt).
> TxGNN-modellen forutsier at det kan være effektivt for **febril infeksjonsrelatert epilepsi-syndrom (FIRES)**,
> men dette støttes for øyeblikket av **0 kliniske studier** og **0 publikasjoner** — bare prediksjonsscoren.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke bekreftet i bevissamlingen (`original_indications` er tomt); Lennox-Gastaut-syndrom refereres kun innen rang-5-begrunnelsesteksten, venter TFDA-merketbekreftelse (DG001) |
| Forutsagt ny indikasjon | Febril infeksjonsrelatert epilepsi-syndrom (FIRES) |
| TxGNN-prediksjonspoengsum | 99,57 % |
| Bevisnivå | L5 (modellprediksjon kun — ingen kliniske studier eller litteratur identifisert) |
| Markedsstatus i Norge | Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) for rufinamid er ikke tilgjengelige i denne bevissamlingen — dette er flagget som et datahull med høy alvorlighetsgrad (DG002). Innen pakkets egen tekst siteres rufinamids bruk ved Lennox-Gastaut-syndrom (LGS) — en alvorlig barneepileptisk ensefalopati som ofte involverer epileptiske spasmer og flere krampeanfallstyper — som eksisterende «indikasjonsbasis» (se rang-5-begrunnelse), og legemidlets antatte bredt spektrum natriumkanalmodulasjon brukes ellers i pakken til å argumentere for plausibilitet for relaterte syndromer.

For den topprankede kandidaten, febril infeksjonsrelatert epilepsi-syndrom (FIRES), inneholder pakken ennå ikke en spesifikk mekanistisk begrunnelse (`mechanistic_link`/`similarity_to_original` er merket «venter»). FIRES er en sjelden, alvorlig epileptisk ensefalopati utløst av febril sykdom som ofte progrederer til superrefraktær status epilepticus og behandles ofte med midler som er effektive ved andre refraktære epileptiske ensef alopatier. Gitt rufinamids refererte rolle i LGS og natriumkanalmekanismen som er påberopt for tilstøtende kandidater i denne samme pakken, er utvidelse til FIRES mekanistisk plausibel i prinsippet — men for øyeblikket hviler dette utelukkende på TxGNN-scoren, uten noen bekreftelses-studie, ICTRP- eller litteraturbevis.

## Bevis fra kliniske studier

For øyeblikket er ingen relaterte kliniske studier registrert.

## Litteraturbevis

For øyeblikket er ingen relatert litteratur tilgjengelig.

## Markedsinformasjon for Norge

Rufinamid er for øyeblikket ikke markedsført og har null autorisasjoner på fil (`total_licenses: 0`, `licenses: []`) — ingen markedsføringsautorisasjonstabell kan genereres fra denne bevissamlingen.

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

> **Datahull-notat:** TFDA/produktmerke-advarsler og kontraindikaser er merket som et **blokkerende** datahull (DG001) — i henhold til bevissamlingen, forhindrer dette spesifikt inngang til S1-sikkerhetsinitialbedømmingsstadiet. Ingen viktige advarsler, kontraindikaser eller DDI-poster er for øyeblikket på fil (`ddi.query_status: not_found`).

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Topprankede indikasjon (FIRES) har bevisnivå L5 — en TxGNN-poengsum med null støttende studier eller litteratur — og legemidlet er umarkedsført med et blokkerende datahull på sikkerhetsmerkingen (DG001), som i seg selv forhindrer enhver S1-sikkerhetsbedømmelse.

**For å fortsette, er følgende nødvendig:**
- TFDA produktmerke (advarsler/kontraindikaser) — løser DG001, for øyeblikket blokkert
- Bekreftet virkningsmekanisme via DrugBank API — løser DG002
- Bekreftelse av rufinamids faktiske originale godkjente indikasjon(er), siden `original_indications` er for øyeblikket tomt
- Målrettet litteratur-/klinisk-studie-søk spesifikk for FIRES for å gå utover L5
- Vurdering av regulatorisk vei, gitt null gjeldende markedsautorisasjoner

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

