---
layout: default
title: Metformin
parent: Kun modellprediksjon (L5)
nav_order: 226
evidence_level: L5
indication_count: 5
---

# Metformin
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

# Metformin: Fra Udokumentert Originalindikasjon til Fokalt Stivt Lemmesynrom

## Sammendrag i Én Setning

> Originalindikasjon for metformin er ikke dokumentert i den nåværende evidenspakken (datahull flagget som Blocking/høy alvorlighetsgrad).
> TxGNN-modellen predikerer at det kan være effektivt for **Fokalt Stivt Lemmesynrom**, en sjelden GAD65-antistoff-mediiert autoimmun nevrologisk lidelse,
> men denne prediksjonen støttes for øyeblikket av **0 kliniske prøver** og **0 publikasjoner** — det er et rent modellstyrt signal (L5), og legemidlets egen repurposing-begrunnelse flagger den mekanistiske forbindelsen som sannsynligvis indirekte snarere enn årsakssammenhengsmessig.

---

## Rask Oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke dokumentert i evidenspakken (datahull) |
| Predikert Ny Indikasjon | Fokalt Stivt Lemmesynrom |
| TxGNN Prediksjonspoeng | 99.45% |
| Bevisnivå | L5 (kun modellprediksjon, ingen klinisk eller litteraturstøtte) |
| Norges Markedsstatus | Ikke markedsført |
| Antall Autorisasjoner | 0 |
| Anbefalt Beslutning | I bero |

---

## Hvorfor Er Denne Prediksjonen Fornuftig?

For øyeblikket er detaljerte virkningsmekanisme-data ikke tilgjengelige for metformin i denne evidenspakken (flagget som et høy-alvorlighetsgrad datahull). Metformins kjente farmakologi — AMPK-aktivering, undertrykking av hepatisk glukoneogenese, og forbedret insulinfølsomhet — er veletablert innen metabolisk sykdomsbehandling, men det finnes ingen verifisert MOA-post i dette datasettet til å formelt knytte det til den predikerte indikasjon.

Det er bemerkelsesverdig at evidenspakkens egen mekanistiske begrunnelse for denne prediksjonen er advarende snarere enn støttende: Fokalt Stivt Lemmesynrom er drevet av GAD65-antistoff-mediiert tap av GABAergisk inhibitorisk signalering i ryggmargen/hjernestammen — en vei uten etablert forbindelse til metformins kjente metabolske mekanismer. Den høye TxGNN-poengsummen gjenspeiler sannsynligvis en indirekte kunnskapsgraf-assosiasjon (f.eks. metabolsk komorbiditet eller legemiddel-bivirkning-kanter i grafen) snarere enn et ekte mekanisme-drevet signal.

Gitt det fullstendige fraværet av kliniske prøver, litteratur, eller en plausibel mekanistisk bro, bør denne prediksjonen behandles som en lav-tillit, utforskende hypotese snarere enn en repurposing-kandidat klar for evaluering.

---

## Evidens fra Kliniske Prøver

For øyeblikket ingen relaterte kliniske prøver registrert

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig

---

## Norges Markedsinformasjon

Metformin har for øyeblikket ingen markedsføringstillatelse registrert i Norge (0 lisenser på fil); ingen produkt-/dosisform-data er tilgjengelig i denne evidenspakken.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: TFDA-ekvivalente advarsler/kontraindikasjoner og legemiddel-interaksjonsdata er flagget som et Blocking-datahull — dette hindrer noen Fase 1-sikkerhetsevaluering for denne kandidaten.)*

---

## Konklusjon og Neste Trinn

**Beslutning: I bero**

**Begrunnelse:**
Prediksjonen støttes kun av en TxGNN-modellpoeng (L5, ingen kliniske prøver eller litteratur), og den medfølgende mekanistiske begrunnelsen noterer eksplisitt at den biologiske forbindelsen til GABAergisk autoimmun patologi er indirekte og ikke mekanisme-drevet. Kombinert med legemidlets «ikke markedsført»-status i Norge og manglende sikkerhetdata, finnes det for øyeblikket ingen grunnlag for å fremme denne kandidaten utover utforskende overvåking.

**For å gå videre, er følgende nødvendig:**
- TFDA-ekvivalente pakningsvedleggs-data (advarsler, kontraindikasjoner) — for øyeblikket et Blocking-hull
- Verifisert metformin-virkningsmekanisme (MOA)-post fra DrugBank eller tilsvarende kilde
- Bekreftelse av metformins faktiske originalindikasjon(er), for øyeblikket udokumentert i denne evidenspakken
- Eventuell preklinisk eller kasus-nivå-evidens som kobler AMPK/metabolske veier til GABAergisk/autoimmun nevrologisk sykdom, for å rettferdiggjøre overgang fra L5 til L4

---

**Merknad om relaterte kandidater:** Denne evidenspakken (`TW-DB00331-multi`) inneholder 4 ytterligere predikerte indikasjoner for metformin med lignende høye TxGNN-poeng (klassisk stivt person-syndrom, opsismodysplasia, tiamin-responsiv dysfunksjonssyndrom, og legemiddel-indusert lokalisert lipodystrofi) — alle vurdert som L5/I bero uten klinisk eller litteraturstøtte. En kandidat (tiamin-responsiv dysfunksjonssyndrom) har en flagget **sikkerhetsbekymring** snarere enn terapeutisk mulighet, siden metformins kjente mitokondriell Complex I-hemming kan være mekanistisk kontraproduktiv i denne tilstanden. Ingen av disse fem kandidatene oppfyller for øyeblikket terskelen for videre evaluering.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

