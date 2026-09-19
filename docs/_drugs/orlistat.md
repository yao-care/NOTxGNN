---
layout: default
title: Orlistat
parent: Kun modellprediksjon (L5)
nav_order: 256
evidence_level: L5
indication_count: 1
---

# Orlistat
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

# Orlistat: Fra fedmestyrring til hypervitaminose

## Oppsummering i én setning

Orlistat er en pankreatisk lipasehemmer som generelt brukes til vektkontroll ved fedme (ikke bekreftet via det nåværende Taiwan/Norge-lovgivinsdatasett, da legemidlet ikke er markedsført i denne bevissamlingen). TxGNN-modellen forutsier at det kan være effektivt for **hypervitaminose**, men denne prediksjonen er for øyeblikket støttet av **0 kliniske forsøk** og **0 publikasjoner** — det er en hypotese basert kun på virkningsmekanisme.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Original indikasjon | Ikke tilgjengelig i lovgivinsdatasett (legemidlet er ikke markedsført); vanligvis kjent som et antifedme-/vektkontrollmiddel |
| Forutsagt ny indikasjon | Hypervitaminose |
| TxGNN forutsigelsesscore | 99.42% |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert offisiell dokumentasjon av virkningsmekanisme er ikke tilgjengelig i denne bevissamlingen (`original_moa` = datakløft). Imidlertid, basert på legemidlets kjente farmakologi, er orlistat en pankreatisk/gastrisk lipasehemmer som blokkerer hydrolysen av diettrigliserider i tarmlumen, og derved reduserer absorpsjonen av diettfett.

Absorpsjonen av fettløselige vitaminer (A, D, E, K) avhenger av dannelsen av blandede lipidmicellestrukturer i tarmen — samme prosess som orlistat forstyrrer. Dette er hvorfor mangel på fettløselige vitaminer er en godt anerkjent bivirkning av orlistat-terapi i dens opprinnelige fedmeindikasjon. TxGNN-prediksjonen foreslår i hovedsak den omvendte anvendelsen av denne samme mekanismen: bruk av orlistats fettmalabsorpsjonseffekt for å senke overdrevne sirkulerende nivåer av fettløselige vitaminer ved hypervitaminose.

Dette er en mekanistisk plausibel hypotese, men den har ikke blitt testet i noe registrert klinisk forsøk eller publisert studie. Den høye TxGNN-scoren (99.42%) gjenspeiler sterk strukturell/mekanistisk likhet sluttet av modellen, **ikke** klinisk validering.

---

## Bevis fra kliniske forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon for Norge

Dette legemidlet er ikke for øyeblikket markedsført i dette datasettet (`market_status`: Ikke markedsført), og ingen autorisasjonsregistreringer er tilgjengelige (`total_licenses`: 0).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Prediksjonen bygger utelukkende på mekanistisk resonnement (Evidensnivå L5) uten støtte fra kliniske forsøk eller litteratur, og legemidlet er ikke for øyeblikket markedsført i denne jurisdiksjon. Dette oppfyller ikke bevisgrensen for å gå videre til sikkerhetsgjennomgang eller klinisk evaluering.

**For å gå videre kreves følgende:**
- Bekreftet offisiell dokumentasjon av virkningsmekanisme (DrugBank API-spørring — for øyeblikket blokkert, DG002)
- Regulatoriske merkingsvarsler og kontraindikasjoner fra TFDA (Blokkerende kløft, DG001) før noen sikkerhetskontroll på S1-nivå kan finne sted
- Bekrefting av legemidlets faktiske godkjente opprinnelige indikasjon(er) fra en autoritativ lovgivningskilde
- Minst preklinisk eller kasusistisk bevis som utforsker orlistats effekt på fettløseligt vitamineklirinering ved hypervitaminose før vurdering av videre evaluering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

