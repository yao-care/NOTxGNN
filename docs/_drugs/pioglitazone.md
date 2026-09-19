---
layout: default
title: Pioglitazone
parent: Kun modellprediksjon (L5)
nav_order: 279
evidence_level: L5
indication_count: 9
---

# Pioglitazone
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

# Pioglitazone: Fra type 2-diabetes mellitus til opsismodysplasi

## Sammenfatting på en setning

Pioglitazone er et insulinfølsomhetsfremmende stoff i tiazolidindion-klassen (TZD) som historisk har blitt brukt ved type 2-diabetes mellitus.
TxGNN-modellens høyest rangerte prediksjon i denne bevissamlingen er **opsismodysplasi**, en sjelden skjelettdysplasi,
men denne kandidaten har **0 kliniske forsøk** og **0 støttende publikasjoner**, og modellens egen begrunnelse flagger det som sannsynlig kunnskapsgrafen-støy snarere enn et genuint signal.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Type 2-diabetes mellitus (basert på kjent farmakologi; ingen norsk lisens/indikasjonsformalisme tilgjengelig i denne bevissamlingen) |
| Predikert ny indikasjon | Opsismodysplasi |
| TxGNN-prediksjonscore | 99,59% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | **Avvent** |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er det ikke tilgjengelig detaljert informasjon om virkningsmekanisme (datakløft DG002, flagget som høy alvorlighetsgrad). Basert på tilgjengelig informasjon er pioglitazone en PPAR-γ-agonist som fungerer som et insulinfølsomhetsfremmende stoff, med etablert effektivitet ved type 2-diabetes gjennom forbedret perifer glukoseopptak og bevaring av bukspyttkjertels betaceller-funksjon.

Opsismodysplasi er imidlertid en genetisk skjelettdysplasi forårsaket av *INPPL1*-mutasjoner som påvirker signalering i vekstplatene i knoklene. Det eksisterer ingen etablert mekanistisk sammenheng mellom PPAR-γ-agonisme og *INPPL1*-mediiert skjelettutviklingen. Bevissamlingens egen omformål-begrunnelse er eksplisitt på dette punktet: den høye TxGNN-scoren reflekterer sannsynligvis sparsomme forbindelser i kunnskapsgrafen rundt denne sjeldensjukdom-noden snarere enn en virkelig farmakologisk sammenheng, og stoffets faktiske rangering (4832) blant alle kandidatsykdommer ligger langt utenfor ethvert område som normalt ville støtte prioritering.

Gitt fraværet av alle kliniske forsøk, observasjons- eller mekanistisk litteratur spesifikk for denne kombinasjonen, bør denne prediksjonen behandles som en artefakt fra hypotesegenerering snarere enn en handlingsorientert omformål-kandidat.

---

## Kliniske forsøk

Ingen relaterte kliniske forsøk er registrert for tiden.

---

## Litteraturbevis

Ingen relatert litteratur er tilgjengelig for tiden.

---

## Markedsinformasjon for Norge

Pioglitazone er ikke for tiden markedsført i Norge i henhold til denne bevissamlingen (`market_status: Ikke markedsført`, `total_licenses: 0`). Ingen autorisasjonsposter er tilgjengelige for gjennomgang.

---

## Andre kandidatindikasjoner som ble vurdert (ikke prioritert)

Bevissamlingen inkluderte 8 ytterligere lavtrangerte kandidater, alle på samme måte vurdert som L5 / Avvent på grunn av svak eller fraværende mekanistisk og klinisk grunnlag:

| Rangering | Sykdom | TxGNN-score | Nøkkelspørsmål |
|-----------|--------|-------------|----------------|
| 2 | Fokal stiv lemme-syndrom | 99,50% | Autoimmun/GABAerg sykdom; ingen mekanistisk eller empirisk sammenheng til PPAR-γ |
| 3 | Klassisk stiv person-syndrom | 99,50% | Det samme som ovenfor |
| 4 | Tiamin-responsiv dysfunksjonssyndrom | 99,48% | Underliggende defekt (SLC19A2) løses ikke av insulinfølsomhetsfremmende behandling |
| 5 | Legemiddelinducert lokalisert lipodystrofi | 99,30% | Mekanistisk motstridende — TZDer er også kjent for å *forårsake* fettomfordeling |
| 6 | Sentrifugal lipodystrofi | 99,26% | Pediatrisk, idiopatisk; ingen støttende bevis |
| 7 | Trykkinducert lokalisert lipoatrofi | 99,24% | Mekanisk/lokal etiologi; svak systemisk PPAR-γ-sammenheng |
| 8 | Idiopatisk lokalisert lipodystrofi | 99,19% | Etiologi ukjent; ingen rettet bevis |
| 9 | Bukspyttkjertels agenesе | 99,18% | 9 hentet publikasjoner er alle generelle T2DM/TZD-oversikter — søkeord-mismatch, ikke sykdomsspesifikk bevis |

Ingen av de 9 kandidatene når ut over L5-bevis, og ingen begrunner for tiden eskalering forbi modellprediksjonstrinnet.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og legemiddelinteraksjondata er ikke tilgjengelig i denne bevissamlingen — DG001 er flagget som en blokkerende datakløft som forhindrer initial vurdering i sikkerhetsstadiet.)

---

## Konklusjon og neste skritt

**Beslutning: Avvent**

**Begrunnelse:**
Alle 9 predikerte indikasjoner er L5 (kun modellprediksjon), uten kliniske forsøk og med enten ingen litteratur eller litteratur som ikke er relevant for den spesifikke sykdommen. Den høyest rangerte kandidaten (opsismodysplasi) har ingen troverdig mekanistisk sammenheng og er eksplisitt flagget av modellens egen begrunnelse som sannsynlig kunnskapsgrafen-støy. Kombinert med en blokkerende sikkerhetsdatakløft (DG001) og fraværende MOA-data (DG002), eksisterer det for tiden intet grunnlag for å fremme noen kandidat forbi S0.

**For å kunne fortsette, er følgende nødvendig:**
- Løse DG001: få TFDA/regulatoriske merkevareadvarsler og kontraindikasjoner for pioglitazone
- Løse DG002: bekrefte detaljert virkningsmekanisme via DrugBank API-spørring
- Dersom man forfølger bukspyttkjertels agenesе-kandidaten (rangering 9), manuelt verifisere hvorvidt noen av de 9 hentet publikasjoner virkelig er sykdomsspesifikk snarere enn generelle T2DM/TZD-oversikter
- Gitt det jevnt svake signalet på tvers av alle 9 kandidater, vurder å kjøre TxGNN på nytt med rangbasert (ikke rå score) terskelbestemmelse før videre bevisinnsamling iverksettes

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

