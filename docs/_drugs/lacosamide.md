---
layout: default
title: Lacosamide
parent: Moderat evidens (L3-L4)
nav_order: 196
evidence_level: L3
indication_count: 10
---

# Lacosamide
{: .fs-9 }

Evidensnivå: **L3** | Predikerte indikasjoner: **10** stk.
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

# Lacosamide: Fra epilepsi til manisk bipolar affektiv lidelse

## Sammendrag på én setning

Lacosamide er et anti-epileptisk legemiddel som brukes ved fokal utgangspunkt (fokal) krampeanfall, og virker gjennom selektiv forbedring av langsom inaktivering av spenningsstyrte natriumkanaler. TxGNN-modellens høyest rangerte prediksjon er effektivitet ved **manisk bipolar affektiv lidelse**, men det understøttende bevisgrunnlaget — **1 klinisk prøving** og **14 publikasjoner** — er tynt og omhandler hovedsakelig bipolar *depresjon* snarere enn den maniske fasen som er spesielt predikert. Dette er et mekanistisk plausibelt, men bevis-retnings mismatch-signal som krever ytterligere avklaring før man går videre.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Epilepsi (fokal utgangspunkt/fokal krampeanfall) — utledet fra klassifisering som anti-epileptisk legemiddel i bevisgrunnlagspakken; ingen Norge-godkjent indikasjonstekst tilgjengelig (legemiddel ikke markedsført) |
| Predikert ny indikasjon | Manisk bipolar affektiv lidelse |
| TxGNN prediksjonspoeng | 99.96% (rangering 711) |
| Bevisnivå | L3 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvente |

---

## Hvorfor er denne prediksjonen rimelig?

Det strukturerte `original_moa`-feltet for lacosamide er markert som et datahull. Imidlertid beskriver litteraturen i denne bevisgrunnlagspakken lacosamides mekanisme som selektiv forbedring av *langsom* inaktiveringsstilstand av spenningsstyrte natriumkanaler, noe som produserer forlenget nevronmembranstabilisering (PMID 28845834). Dette er den samme generelle mekanistiske klassen som deles av etablerte humørregulerende midler som lamotrigin og valproat, som begge har godkjent eller godt dokumentert roller ved bipolar lidelse — noe som gir en plausibel farmakologisk begrunnelse for å utforske lacosamide som et humørregulerende middel.

Når det er sagt, er det en bemerkelsesverdig **bevis-retnings mismatch**. Den eneste registrerte prøvingen (NCT07412132) retter seg eksplisitt mot "Alvorlige depressive episoder ved bipolar lidelse," ikke mani, og er begrunnet av tidligere åpen-label data på forbedring av depressive/maniske symptomer snarere enn en manisk-spesifikk hypotese. Den retrospektive og åpen-label litteraturen som er identifisert (PMID 30251375, 33666402) fokuserer likeledes på bipolar *depresjon*. En kasuistikk (PMID 30275630) dokumenterer lacosamide-utløst neutropeni hos en bipolar pasient — et ikke-relatert sikkerhetssignal snarere enn bevis for effektivitet.

Kort sagt: det natriumkanal-medierende humørregulerende rasjonalet er biologisk rimelig ved analogi til andre anti-epileptiske legemidler som brukes ved bipolar lidelse, men ingen identifisert studie evaluerer direkte lacosamide for den *maniske* fasen som er spesifikt flagget av TxGNN. Prediksjonen bør behandles som et hypotesegenererende signal, ikke en validert indikasjon.

---

## Bevis fra kliniske prøvinger

| Prøvingnummer | Fase | Status | Antall deltakere | Viktige funn |
|---------|------|------|------|---------|
| [NCT07412132](https://clinicaltrials.gov/study/NCT07412132) | Fase 3 | Rekrutterer | 40 | Evaluerer lacosamide som augmenteringsterapi for **alvorlige depressive episoder** ved bipolar I/II lidelse (ikke maniske episoder); begrunnelse basert på tidligere åpen-label observasjoner av forbedret depressiv/manisk symptom ved epilepsi og BD-populasjoner |

---

## Bevis fra litteraturen

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [30251375](https://pubmed.ncbi.nlm.nih.gov/30251375/) | 2018 | Retrospektiv kohortstudie | Psychiatry Clin Neurosci | 30-dagers sammenligning av lacosamide vs. andre anti-epileptiske legemidler hos bipolære pasienter uten epilepsi — første direkte lacosamide-in-BD data |
| [33666402](https://pubmed.ncbi.nlm.nih.gov/33666402/) | 2021 | Åpen-label pilotprøving | J Clin Psychopharmacol | 12-ukers pilotprøving av lacosamide spesifikt for bipolar **depresjon** |
| [28845834](https://pubmed.ncbi.nlm.nih.gov/28845834/) | 2017 | Kasuistikk | Acta Biomed | Klinisk humørregulering med lacosamide hos en pasient med komorbid PTSD og frontotemporal epilepsi; beskriver mekanismen for langsom Na+-kanal inaktivering |
| [30275630](https://pubmed.ncbi.nlm.nih.gov/30275630/) | 2018 | Kasuistikk (bivirkningshendelse) | Indian J Psychol Med | Lacosamide-utløst neutropeni hos bipolar pasient med komorbid epilepsi — sikkerhetssignal |
| [38304661](https://pubmed.ncbi.nlm.nih.gov/38304661/) | 2024 | Kasuistikk | Cureus | Kompleks tilfelle av bipolar I lidelse med flere komorbiditeter inkludert krampelignende aktivitet |
| [40777679](https://pubmed.ncbi.nlm.nih.gov/40777679/) | 2025 | Kasuistikk | Cureus | Xylazin-abstinenssyndrom hos pasient med komorbid bipolar lidelse; stort sett perifert til effektivitet |
| [32693579](https://pubmed.ncbi.nlm.nih.gov/32693579/) | 2020 | Mekanistisk gjennomgang | ACS Chem Neurosci | Gjennomgang av CRMP2 som legemiddelmål — relevant for lacosamides sekundær (ikke-Nav) mekanisme |
| [37782796](https://pubmed.ncbi.nlm.nih.gov/37782796/) | 2023 | Strukturell/mekanistisk | PNAS | Cryo-EM strukturell basis for Nav-kanalhemming av anti-epileptiske legemidler (lamotrigin), som understøtter klassemekanisme relevant for lacosamide |
| [29957667](https://pubmed.ncbi.nlm.nih.gov/29957667/) | 2018 | Gjennomgang | Ther Drug Monit | TDM oppdatering av anti-epileptiske legemidler, merknader om utvidet bruk utover epilepsi inkludert bipolar lidelse |
| [22210279](https://pubmed.ncbi.nlm.nih.gov/22210279/) | 2012 | Gjennomgang | Adv Drug Deliv Rev | Kjemiske/farmakokinetiske egenskaper for nyere anti-epileptiske legemidler inkludert lacosamide — kun bakgrunnsfarmakologi |

---

## Markedsinformasjon for Norge

Lacosamide har for øyeblikket **ingen markedsgodkjenning i Norge** (markedsstatus: Ikke markedsført; 0 godkjenninger på fil per datokutoff 2026-09-03). Ingen produktnivå-lisensiering eller godkjent indikasjonstekst er tilgjengelig for ekstraksjon.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: Strukturerte advarsler, kontraindikasjoner og DDI-data var ikke hentet for denne bevisgrunnlagspakken — flagget som en Blocking-gap (DG001) som krever TFDA/Norge-etikett-sourcing før noen sikkerhetsvurdering kan finne sted.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvente**

**Begrunnelse:**
Det mekanistiske rasjonalet (natriumkanal-mediert humørregulering, parallelt med lamotrigin/valproat) er plausibelt, men det eneste fullførte/pågående beviset omhandler bipolar **depresjon**, ikke den maniske fasen som spesifikt er predikert av TxGNN. Med kun L3-bevis, en enkelt liten (n=40), fortsatt-rekrutterende, ikke-manisk-spesifikk prøving, og ingen formell sikkerhetsetikett tilgjengelig, støtter beviset ikke videre framskriting.

**For å fortsette, er følgende nødvendig:**
- Direkte klinisk bevis (prøving eller retrospektiv analyse) som evaluerer lacosamide spesifikt i manisk/hypomanisk episoder, ikke kun bipolar depresjon
- Løsning av Blocking-gap DG001 (TFDA/Norge advarsler og kontraindikasjoner) før noen S1 sikkerhetsvurdering kan finne sted
- Formell MOA-dokumentasjon fra DrugBank (høyt prioritert gap DG002)
- Bekreftelse av Norges marked/import-vei, gitt at legemiddelet for øyeblikket har ingen lokal godkjenning

**Ytterligere merknad:** Blant de 10 TxGNN-predikerte indikasjonene som ble evaluert for lacosamide i denne bevisgrunnlagspakken, viser **migrenelidelse** (rangering 5) vesentlig sterkere bevis — Bevisnivå L1, inkludert en fullført head-to-head fase 3 RCT vs. propranolol (n=600) og mekanistisk CGRP-senking data — og har en "Fortsett med sikkerhetstiltak" anbefaling. Denne kandidaten kan være verdt en separat, dedikert evalueringsrapport.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

