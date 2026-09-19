---
layout: default
title: Aflibercept
parent: Kun modellprediksjon (L5)
nav_order: 19
evidence_level: L5
indication_count: 1
---

# Aflibercept
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

# Aflibercept: Fra neovaskulær øyesykdom til esotropi

## Sammendrag i en setning

> Aflibercept er et VEGF-A/VEGF-B/PlGF-falleprotein opprinnelig utviklet for neovaskulære øyesykdommer som vått AMD, DME og RVO.
> TxGNN-modellen forutsier at det kan være effektivt for **esotropi**, men denne prediksjonen støttes for tiden av **0 kliniske forsøk** og **0 publikasjoner**,
> og den foreslåtte mekanistiske forbindelsen mellom anti-VEGF-aktivitet og esotropi (en ekstrakulær muskulatur-/neuromuskulær forstyrrelse) er ikke godt etablert.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke tilgjengelig i regulatoriske lisensdata (legemidlet er ikke markedsført); basert på legemidlets kjente mekanisme beskrives det i denne bevispakken som brukt for neovaskulære øyesykdommer (f.eks. vått AMD, DME, RVO) |
| Forutsagt ny indikasjon | Esotropi |
| TxGNN-forutsigelsesscore | 99.38% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttende forsøk eller litteratur) |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Det formelle `original_moa`-feltet for dette legemidlet er merket som en datakløft, så det finnes for tiden ingen fullstendig dokumentert virkningsmekanisme. Imidlertid beskriver bevispakkens egen begrunnelse for gjenbruk aflibercept som et VEGF-A/VEGF-B/PlGF-falleprotein som blokkerer angiogen signalering, og bemerker at det brukes for neovaskulære øyesykdommer som vått AMD, diabetisk makulært ødem (DME) og retinal venøs okklusjon (RVO). Alle disse er tilstander som skyldes patologisk blodkarvekst i netthinnen/choroidea.

Esotropi er derimot en form for strabismus forårsaket av ubalanse i ekstrakulær muskeltonus, avvik i akkommodativ konvergens, eller dysfunksjon i hjernenerven (typisk CN VI) — et neuromuskulært/okulomotorisk kontrollproblem, ikke vaskulært eller angiogent. Det finnes ingen etablert farmakologisk vei som forbinder VEGF-falleaktivitet med ekstrakulær muskelbalanse eller nervefunksjon.

Basert på begrunnelsen gitt i denne bevispakken, ser de to tilstandene ut til bare å dele en bred "oftalmologisk sykdom"-klassifisering i kunnskapsgrafen. Den høye TxGNN-poengsum (99.38%) gjenspeiler mest sannsynlig et topologisk artefakt i kunnskapsgrafen snarere enn et genuint biologisk forhold, og bør behandles som **falskt positivt med høy risiko**. Denne vurderingen er videre begrenset av den uløste blokkerte datakløften på TFDA pakkeseddel advarsler/kontraindikasjoner og en manglende bekreftet MOA, som begge reduserer tilliten til enhver kausal slutning.

---

## Bevis fra kliniske forsøk

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er det ingen relatert litteratur tilgjengelig.

---

## Informasjon om norsk marked

Dette legemidlet er for tiden ikke markedsført i Norge (markedsstatus: Ikke markedsført), og ingen godkjennelsesregistre er tilgjengelige i denne bevispakken.

---

## Sikkerhetshensyn

Se pakkeseddelen for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Til tross for en høy TxGNN-forutsigelsesscore, har denne kandidaten null støttende kliniske forsøk og null støttende litteratur, og den foreslåtte mekanistiske forbindelsen mellom anti-VEGF-aktivitet og esotropi er ikke farmakologisk godt støttet — det gjenspeiler mest sannsynlig et topologisk artefakt i kunnskapsgrafen snarere enn et genuint biologisk forhold. Kombinert med en uløst blokkert datakløft på TFDA pakkeseddel advarsler/kontraindikasjoner og en manglende bekreftet MOA, oppfyller denne kandidaten ikke for tiden terskelen for å avansere forbi innledende screening.

**For å gå videre er følgende nødvendig:**
- TFDA pakkeseddel (advarsler, kontraindikasjoner) — for tiden en blokkert datakløft (DG001)
- Bekreftet virkningsmekanisme fra DrugBank eller en annen autoritativ kilde — for tiden en datakløft med høy alvorlighetsgrad (DG002)
- En uavhengig vurdering av mekanistisk plausibilitet som spesifikt adresserer VEGF-vei til strabismus-koblingen før videre bevisinnsamling prioriteres
- Eventuell tilgjengelig preklinisk eller saksnivå bevis som forbinder VEGF-signalering med ekstrakulær muskulatur/neuromuskulær funksjon, hvis det eksisterer
- Oppdatert bekreftelse av markeds-/regulatorisk status, siden legemidlet for tiden er umarkedsført i denne juridiksjonen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

