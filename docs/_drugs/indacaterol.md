---
layout: default
title: Indacaterol
parent: Kun modellprediksjon (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: Fra kronisk obstruktiv lungesykdom til nefrogent syndrom for upassende antidurese

## Sammendrag i en setning

Indacaterol er en langvirkende β2-adrenergisk agonist (LABA) brukt ved respiratorisk sykdom (KOLS/astma) basert på kliniske forsøk og mekanistisk bevis i denne pakken; formell original-indikasjon tekst kunne ikke bekreftes fordi legemidlet for tiden er ulisensiert i målmarkedet.
TxGNN-modellens høyest rangerte prediksjon er **Nefrogent syndrom for upassende antidurese (NSIAD)**, men denne kombinasjonen har **0 kliniske forsøk** og **0 publikasjoner** som støtter det, og evidenspakkens egen mekanistiske gjennomgang flagger det som sannsynlig en falskt positiv i kunnskapsgrafen.
Blant alle 10 høyest rangerte TxGNN-prediksjoner for dette legemidlet, har bare en («bronkial sykdom», rang 7) sterkt klinisk bevis (L1) — men det signalet bekrefter ganske enkelt legemidlets kjente LABA-farmakologi i stedet for å representere en ny bruksomlegging.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke bekreftet av lokale lisensdata (0 autorisasjoner på fil); bevis på legemiddelklasse peker på KOLS/astma (LABA) |
| Forutsagt ny indikasjon | Nefrogent syndrom for upassende antidurese |
| TxGNN prediksjonsscore | 99.54% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttende forsøk eller litteratur) |
| Markedsstatus | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelig (DrugBank MOA-felt er et datahull). Basert på mekanistisk bevis som er innebygd gjennom hele denne pakkens innlyselser om kliniske forsøk og begrunnelse, er indacaterol en langvirkende β2-adrenergisk agonist som produserer bronkodilatasjon gjennom direkt virkning på β2-reseptorer på glatt muskulatur i luftveiene — det farmakologiske grunnlaget for dets etablerte bruk ved obstruktiv lungesykdom.

NSIAD er i kontrast en arvelig lidelse forårsaket av gain-of-function-mutasjoner i vasopressin V2-reseptoren, som driver nyre vannretensjon uavhengig av noen β2-adrenergisk vei. Det er ingen kjent farmakologisk, reseptornivå eller fysiologisk overlapping mellom LABA-aktivitet og V2-reseptor-formidlet vannbehandling. Evidenspakkens egen bruksomlegerings begrunnelse for denne kandidaten karakteriserer eksplisitt den som en **kunnskapsgrafs-assosiasjon falskt positiv** i stedet for en genuinn mekanistisk hypotese, og ingen kliniske forsøk eller litteratur finnes for å motsi denne vurderingen.

For kontekst, av de 10 høyest rangerte TxGNN-prediksjoner for indacaterol, er ni (NSIAD, hodepinesykdom, trigeminal autonom cephalgia, paratenonitis, kalsifiserende senebetennelse, hypertrikose, myositt, anafilaksi, hypertrikose av Ambras-type) flagget i kildebegrunnelsen som manglende mekanistisk rimelighet eller som reflekterer bivirkningstegn som blir tatt for terapeutiske. Den tiende («bronkial sykdom») er godt støttet (L1, flere fase 3 RCT-er) men representerer legemidlets **allerede etablerte** LABA-farmakologi, ikke en ny indikasjon. Samlet sett presenterer denne evidenspakken for tiden ikke en troverdig ny bruksomleggeingskandidat for indacaterol.

---

## Bevis fra kliniske forsøk

For tiden ingen registrerte kliniske forsøk relatert.

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon

Ingen autorisasjoner er på fil — dette produktet er for tiden **ikke markedsført** i målmyndigheten, og ingen lisensposter er tilgjengelig for oppsummering.

---

## Sikkerhetshensyn

Vennligst referer til produktresumeet for sikkerhetsinformasjon. Legg merke til at viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjon er alle for tiden utilgjengelige (flagget som et **blokkerende** datahull — DG001: TFDA-ekvivalent produktresume advarsler/kontraindikasjoner ikke ennå hentet), som i seg selv hindrer en fullstendig sikkerhetsvurdering (S1 stadium) for noen indikasjon av dette legemidlet.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den høyest rangerte TxGNN-prediksjonen (NSIAD) har ingen mekanistisk rimelighet, ingen kliniske forsøk og ingen litteraturstøtte, og er eksplisitt vurdert som sannsynlig falskt positiv. Den eneste godt dokumenterte prediksjonen i denne pakken («bronkial sykdom») utgjør ikke en ny indikasjon. Ingen bruksomleggeringstilfelle finnes for tiden som ville rettferdiggjøre avansering forbi det tidligste evalueringsstadiet.

**For å fortsette, er følgende nødvendig:**
- TFDA-ekvivalent produktresume (advarsler/kontraindikasjoner) — for tiden blokkert (DG001)
- Detaljerte mekanisme-of-action-data fra DrugBank — for tiden høy-alvorlighetsgrad hull (DG002)
- En genuinn mekanistisk eller preklinisk begrunnelse som knytter β2-adrenergisk signalisering til V2-reseptor-formidlet antidurese, hvis denne kandidaten skal forfølges videre
- Hvis du forfølger «bronkial sykdom»-signalet i stedet, rammer om det som indikasjoneutvidelse/bekjeftelse av virkningsmekanisme i stedet for bruksomlegging, og innhent formell lokal regulatorisk indikasjonsbeskrivelse

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

