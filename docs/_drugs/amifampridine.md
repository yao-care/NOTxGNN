---
layout: default
title: Amifampridine
parent: Kun modellprediksjon (L5)
nav_order: 27
evidence_level: L5
indication_count: 2
---

# Amifampridine
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

# Amifampridine: Fra Lambert-Eaton myastenisk syndrom til glaukom

## Sammendrag i en setning

Amifampridine (DrugBank DB11640) er en bredspektret Kv1.x spenningskontrollert kaliumkanal-blokkerer hvis etablerte kliniske bruk — referert i den underliggende mekanistiske begrunnelsen — er Lambert-Eaton myastenisk syndrom (LEMS), hvor det øker acetylkolinfreisetting ved nevromuskulær synapse. TxGNN-modellen forutsier at det kan være effektivt for **Glaukom**, men denne prediksjonen er for tiden støttet av **0 kliniske forsøk** og **0 publikasjoner** — det er et rent beregningssignal (TxGNN-score 99.71%) uten legemiddelspesifikk evidens bak det.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Lambert-Eaton myastenisk syndrom (LEMS) — utledet fra den mekanistiske begrunnelsesteksten (kjent nevromuskulær farmakologi); ingen formell norsk lisensrekord bekrefter dette, da legemidlet har 0 registrerte godkjennelser |
| Forutsagt ny indikasjon | Glaukom |
| TxGNN prediksjons-score | 99.71% |
| Evidensnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen fornuftig?

For tiden er en formelt bekreftet mekanisme-for-handling-rekord ikke tilgjengelig (flagget som datahull, DG002). Basert på informasjonen som er fanget opp i den mekanistiske begrunnelsen for omformål, er amifampridine kjent for å fungere som en bredspektret Kv1.x spenningsavhengig kaliumkanal-blokkerer ved nevromuskulær synapse, hvor det øker acetylkolinfreisetting — det farmakologiske grunnlaget for dets bruk ved LEMS.

Den foreslåtte koblingen til glaukom hviler på at kalium- og vannkanal-aktivitet i siliarlegemets epitel påvirker produksjon av øyevæske og regulering av intraokulært trykk, og kaliumkanaler har en teoretisk rolle i denne veien. Imidlertid er dette en **familie-nivå**-slutning (legemidler som blokkerer kaliumkanaler generelt) snarere enn en **legemiddelspesifikk**: det finnes for tiden ingen publisert data, dyremodell, eller humant intraokulær trykkstudi som demonstrerer at amifampridine virker på kaliumkanaler i siliarlegemet.

Evidenspakken selv flagger denne koblingen som lav-tillitsfull, ikke-spesifikk, og muligens et falskt-positivt artefakt av TxGNN-embedningsrommet snarere enn en biologisk grunnlagt hypotese. Den bør behandles som et kun hypotese-genererende signal, ikke som mekanistisk støtte for å fremme kandidaten.

---

## Klinisk forsøks-evidens

For tiden ingen relaterte kliniske forsøk registrert.

---

## Litteratur-evidens

For tiden ingen relatert litteratur tilgjengelig.

---

## Annen TxGNN-forutsagt indikasjon (lavere prioritet)

En annen kandidatindikasjon ble også flagget av modellen: **Akutt intermittent porfyri** (TxGNN-score 99.32%, rangering 6919; Evidensnivå L5; Anbefaling: Avvent). Ingen kliniske forsøk eller litteratur ble funnet for denne koblingen heller. Begrunnelsen noter eksplisitt at amifampridines mekanisme (kaliumkanal-blokkade / nevromuskulær acetylkolinfreisetting) har ingen kjent krysspunkt med hembiosyntese eller ALA/PBG-metabolisme — den eneste plausible koblingen er en symptom-nivå tilfeldighet (perifer neuropati/svakhet sett i både AIP og nevromuskulære lidelser), som evidenspakken selv karakteriserer som et sannsynlig falskt positivt. Denne kandidaten forfølges ikke videre i denne rapporten.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Merknad: et fullstendig pakningsvedlegg med advarsler og kontraindikasjoner fra Norge/TFDA-tilsvarende har ennå ikke blitt innhentet — dette er loggført som et blokkerende datahull (DG001) og forhindrer kandidaten fra å gå inn i S1-sikkerhet-forscreenings-stadiet.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Denne kandidaten befinner seg på Evidensnivå L5 — en modell-kun prediksjon med null støttende kliniske forsøk eller litteratur, ingen bekreftet mekanisme-for-handling-rekord, og ingen markedsnærvær i Norge (0 godkjennelser, ikke markedsført). Et blokkerende datahull i pakningsvedlegget (advarsler/kontraindikasjoner) forhindrer også enhver sikkerhet-forscreening. Den mekanistiske koblingen til glaukom er selv beskrevet som en svak, ikke-spesifikk, familie-nivå-slutning som kan være et falskt positivt, så det finnes for tiden ikke grunnlag for å gå videre enn overvåking.

**For å gå videre er følgende nødvendig:**
- Løs DG001 (Blokkering): innhent det offisielle pakningsvedlegget/merkelappen (advarsler, kontraindikasjoner) for å muliggjøre innledende sikkerhet-screening
- Løs DG002 (Høy): bekreft detaljerte mekanisme-for-handling-data via DrugBank eller primærkilder innen farmakologi
- Preklinisk eller mekanistisk evidens som knytter amifampridine (eller Kv1.x-blokkade spesifikt) til siliarlegemets ionetransport, øyevæske-dynamikk, eller intraokulært trykk
- Enhver legemiddelspesifikk klinisk forsøk, kasusrapport, eller farmakoovervåkingssignal for amifampridine ved glaukom
- Klarlegging av norsk regulatorisk vei, siden legemidlet for tiden ikke er markedsført (0 lisenser) og ville kreve en import/navngitt pasient eller ny-søknadsrute før enhver utforskende bruk

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

