---
layout: default
title: Linaclotide
parent: Kun modellprediksjon (L5)
nav_order: 210
evidence_level: L5
indication_count: 3
---

# Linaclotide
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Linaclotid: Fra ikke spesifisert til Cauda Equina Syndrome

## Sammendrag på en setning

> Linaclotids opprinnelig godkjente indikasjon er ikke dokumentert i gjeldende evidenspakke (data om virkningsmekanisme og indikasjon er ikke tilgjengelige).
> TxGNN-modellen forutsier at det kan være effektivt for **Cauda Equina Syndrome**,
> men denne prediksjonen er for øyeblikket støttet av **0 kliniske forsøk** og **0 publikasjoner**, og legemidlet er ikke markedsført i Norge.

---

## Rask oversikt

| Element | Innhold |
|---------|--------|
| Opprinnelig indikasjon | Ikke tilgjengelig i gjeldende data |
| Predikert ny indikasjon | Cauda Equina Syndrome |
| TxGNN-prediksjonspoengsum | 99.96% |
| Evidensnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte data om virkningsmekanisme ikke tilgjengelige for linaclotid i denne evidenspakken. Basert på legemidlets kjente farmakologiske klasse, er linaclotid en guanylat cyclase-C (GC-C) agonist som virker lokalt på intestinale epitelreseptorer, med neglisjerbar systemisk absorpsjon og ingen sentral eller perifer nevral virkningsmekanisme.

Cauda equina syndrome er en kirurgisk nødsituasjon forårsaket av mekanisk kompresjon av lumbsakrale nerverøtter, som krever hastelig dekompresjon. Det er ingen etablert fysiologisk forbindelse mellom GI-sekretorisk modulering (linaclotids kjente virkemåte) og nerverotkompresjonpatologi.

Gitt fraværet av noen støttende kliniske forsøk eller litteratur, reflekterer denne prediksjonen mest sannsynlig en kunnskapsgrafartefakt — muligens oppstått fra delte komorbiditetsknuter som forstoppelse eller nevrogen blæreproblematikk som ofte forekommer sammen med cauda equina syndrome — snarere enn et genuint farmakologisk signal.

---

## Evidens fra kliniske forsøk

For øyeblikket er det ingen registrerte relaterte kliniske forsøk.

---

## Litteraturbevis

For øyeblikket er ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon Norge

Linaclotid er for øyeblikket ikke markedsført i Norge, og ingen autorisasjonsregistreringer er tilgjengelige i denne evidenspakken.

---

## Sikkerhetsoverveielser

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Ytterligere evaluerte prediksjoner

To andre TxGNN-predikerte indikasjoner ble gjennomgått i denne evidenspakken, begge tilsvarende ustøttet:

| Rangering | Predikert indikasjon | TxGNN-poengsum | Bevis | Anbefaling |
|-----------|----------------------|----------------|-------|-----------|
| 2 | Obsolete Neurogenic Bladder (disease) | 99.89% | Ingen | Hold |
| 3 | Insomnia | 99.51% | Ingen | Hold |

Rangering 2 er flagget som en foreldet/avskrevet sykdomsontologinode, som indikerer et datakvalitetsproblem snarere enn en gyldig hypotese. Rangering 3 mangler mekanistisk plausibilitet, ettersom linaclotid har oral biodisponibilitet <0,1% og krysser ikke blod-hjerne-barrieren, noe som utelukker enhver sentral virkning på søvnregulerende mekanismer.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle tre predikerte indikasjoner har L5-evidens (kun modellpredikasjon), med null støttende kliniske forsøk eller litteratur, og den topprangerte kandidaten (cauda equina syndrome) mangler enhver plausibel mekanistisk grunnlag gitt linaclotids lokale, ikke-systemiske virkemåte. I tillegg kan denne kandidaten ikke fortsette til sikkerhetskontroll (S1) på grunn av en blokkerande datakløft for TFDA-advarsler/kontraindikasjoner.

**For å fortsette trengs følgende:**
- TFDA-pakningsvedlegg (advarsler, kontraindikasjoner) — for øyeblikket en blokkerande datakløft (DG001)
- Bekreftet virkningsmekanismedata fra DrugBank — for øyeblikket en alvorlig datakløft (DG002)
- Opprinnelig godkjente indikasjon(er) for linaclotid, for å etablere en grunnlinje for mekanistisk sammenligning
- Noen virkelighetsnære eller prekliniske bevis direkte knyttet til GC-C-agonisme til de predikerte indikasjonene før videre evaluering er berettiget

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

