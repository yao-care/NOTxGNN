---
layout: default
title: Vortioxetine
parent: Kun modellprediksjon (L5)
nav_order: 388
evidence_level: L5
indication_count: 5
---

# Vortioxetine
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

# Vortioxetin: Fra alvorlig depressiv lidelse til nevrotisk lidelse

## Sammendrag på en setning

> Vortioxetin er et multimodalt serotonergt antidepressivum, og litteraturen i denne bevissamlingen beskriver det som «for tiden godkjent for behandling av alvorlig depressiv lidelse (MDD)».
> TxGNN-modellens høyest rangerte prediksjon er **Nevrotisk lidelse**, en eldre, bred diagnostisk betegnelse som overlapper depressivt/angstspekteret,
> for tiden støttet av kun **1 klinisk forsøk** og **1 publikasjon**. En nært beslektet kandidat i samme prediksjonsresultat — **Nevrotisk depresjon** — er i det vesentlige synonymt med MDD under eldre nomenklattur og har langt sterkere bevis (6 kliniske forsøk, 20 publikasjoner, flere fase 3 RCT).

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Alvorlig depressiv lidelse (MDD) — i henhold til litteraturen i denne samlingen (PMID 29189941, 25016186); `original_moa`/`original_indications`-felt er datahull og ikke markedsført i Norge, så ingen lokal lisenstekst er tilgjengelig |
| Predikert ny indikasjon | Nevrotisk lidelse |
| TxGNN prediksjonspoengsum | 99,24% |
| Bevisnivå | L3 (etter pakkepoengsum: enkelt retrospektivt virkelighetsstudium, Grad C-relevans + en oversikt, Nivå 3) |
| Markedsstatus i Norge | ✗ Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

`drug.original_moa`-feltet er merket som et datahull. Imidlertid beskriver litteraturen som allerede er samlet i denne bevissamlingen (Sanchez et al. 2015, PMID 25016186) vortioxetins mekanisme: det er en serotonitransporter (SERT)-hemmer med tilleggs 5-HT1A-reseptor-agonisme, 5-HT1B-delvis agonisme, og 5-HT3/5-HT7/5-HT1D-reseptor-antagonisme, som øker serotonerge, noradrenerge, dopaminerge, kolinnerge, histaminerge og glutamaterge nevrotransmisjon i hjernekretser involvert i humør og kognisjon.

«Nevrotisk lidelse» er en bred, stort sett foreldet diagnostisk samlebetegnelse (ICD-9-era terminologi, ikke del av nåværende DSM-5-nomenklattur) som omfatter angst- og depresjonsnære manifestasjoner. Fra et mekanistisk perspektiv er en multimodal serotonergen agent plausibel for dette spekteret, men fordi betegnelsen selv mangler diagnostisk spesifisitet, er den støttende evidensen begrenset og stort sett indirekte — dette er eksplisitt anerkjent i pakkens egen `repurposing_rationale` for denne kandidaten.

Det er bemerkelsesverdig at fire av fem predikerte indikasjoner i denne pakken (nevrotisk lidelse, nevrotisk depresjon, melankoli, dystymic lidelse) alle ligger innenfor samme depressiv/nevrotisk-spektrum-klynge, og i hovedsak gjenfinner vortioxetins kjente antidepressivprofil gjennom ulike historiske navngivingnormer. Blant disse har **nevrotisk depresjon** (rangering 2, poengsum 99.09%) langt den sterkeste kliniske evidensen — seks forsøk inkludert flere fullførte fase 3 RCT, og 20 publikasjoner inkludert systematiske oversikter og nettverksmetaanalyser i MDD — og bør behandles som det praktiske ankeret for denne signalklyngen. Den femte kandidaten, *benign paroxysmalt tortikollis hos spedbarn*, er en pediatrisk paroxysmalsykdom uten støttende forsøk eller litteratur og er mest plausibelt modellstøy snarere enn et genuint ombruks-signal.

---

## Bevis fra kliniske forsøk

| Forsøksnummer | Fase | Status | Antall deltakere | Viktige funn |
|---------|------|------|------|---------|
| [NCT04446039](https://clinicaltrials.gov/study/NCT04446039) | N/A | Fullført | 370,212 | Stort retrospektivt virkelighetsstudium basert på forsikringskravdata som sammenligner medikamentbruksmønstre og risiko for ugunstige utfall på tvers av hyppig brukte antidepressiva; ikke spesifikt utformet for «nevrotisk lidelse»-diagnose, så relevansen er indirekte (Grad C). |

---

## Bevis fra litteratur

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Oversikt | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | Kasusbasert oversikt over «nevrotisk depresjon»-behandling som bemerker fordelene ved å kombinere antidepressiva med kognitiv atferdsterapi. |

---

## Markedsinformasjon for Norge

Vortioxetin er for tiden **ikke markedsført i Norge** (`market_status: Not marketed`, `total_licenses: 0`); ingen godkjennelsesregistre er tilgjengelige i denne bevissamlingen.

---

## Sikkerhetshensyns

Vennligst se pakningsvedlegget for sikkerhetsopplysninger. Viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjoner er for tiden utilgjengelige i denne bevissamlingen (`DG001`, markert som *Blokkering* — advarsler og kontraindikasjoner i TFDA/Norge-pakningsvedlegget er ennå ikke hentet, noe som forhindrer oppføring i S1 sikkerhetsvurderingsfasen).

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
- Den høyest rangerte kandidaten, «Nevrotisk lidelse», er en upresis arvet diagnostisk betegnelse med kun ett indirekte virkelighetsforsøk og en kasusgjennomgangsartikkel — utilstrekkelig evidens for å gå videre på egenhånd.
- Innenfor samme prediksjonsklynge er «Nevrotisk depresjon» (L1/S3, «Fortsett med sikkerhetstiltak») et langt sterkere, bedre-bevist signal og er i det vesentlige ekvivalent med vortioxetins kjente MDD-indikasjon under eldre nomenklattur; det bør være målet med høyeste prioritet hvis denne ombruksretningen forfølges.

**For å gå videre er følgende nødvendig:**
- Hent TFDA/Norge-pakningsvedleggets advarsler, kontraindikasjoner og DDI-data (DG001, blokkering) før sikkerhetsvurdering på S1-nivå.
- Hent bekreftet virkemekanisme-data fra DrugBank (DG002).
- Avklar diagnostisk kartlegging av arvet terminer (nevrotisk lidelse, nevrotisk depresjon, melankoli, dystymic lidelse) til gjeldende DSM-5/ICD-11-kategorier for å konsolidere dette til en enkel, veldefinert målindikasjon — sannsynlig sentrert på «Nevrotisk depresjon»/MDD-spektrum-bruk.
- Behandle «benign paroxysmalt tortikollis hos spedbarn» som lavprioritet/sannsynlig støy gitt null støttende forsøk eller litteratur; ikke gå videre uten uavhengig mekanistisk begrunnelse.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

