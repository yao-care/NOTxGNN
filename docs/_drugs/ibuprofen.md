---
layout: default
title: Ibuprofen
parent: Kun modellprediksjon (L5)
nav_order: 171
evidence_level: L5
indication_count: 7
---

# Ibuprofen
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

# Ibuprofen: Fra NSAID-terapi til Acromesomelic Dysplasia, Hunter-Thompson-type

## Sammendrag på én setning

> Ibuprofen er et bredt brukt ikke-steroidalt antiinflammatorisk legemiddel (NSAID), selv om ingen Taiwan-godkjent indikasjonsinformasjon er tilgjengelig i denne bevissamlingen.
> TxGNN-modellens toppprediksjon er **Acromesomelic Dysplasia, Hunter-Thompson-type**, en sjelden medfødt skjelettlidelse,
> men denne kandidaten har for øyeblikket **0 kliniske prøvinger** og **0 publikasjoner** som støtter det, og modellens egen begrunnelse flagger det som et sannsynlig embedding-clustering falskt positivt.

---

## Rask oversikt

| Punkt | Innhold |
|------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig — ingen `original_indications` eller Taiwan-lisensiata i denne bevissamlingen |
| Predikert ny indikasjon | Acromesomelic Dysplasia, Hunter-Thompson-type |
| TxGNN-prediksjonspoengsum | 99.74% |
| Bevisnivå | L5 |
| Taiwan-markedsstatus | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljert virkningsmekanisme-data ikke tilgjengelig (flagget som et alvorlig datgap, DG002). Ibuprofen er generelt kjent som et propionsyre-klasse-NSAID som hemmer COX-1/COX-2 og prostaglandinsyntese, men ingen legemiddel-spesifikk MOA-post ble returnert for denne kandidaten.

Det er viktig at denne prediksjonen **ikke** bør behandles som mekanistisk godt støttet. Modellens egen begrunnelse for den høyest rangerte tilstanden slår fast at Acromesomelic Dysplasia, Hunter-Thompson-type er forårsaket av *GDF5*-genmutasjoner — en medfødt strukturell skjelettlidelse med **ingen kjent patogen overlapping** med COX/prostaglandin-hemningsbanen som ligger til grunn for ibuprofen-farmakologien. Bevissamlingen noterer eksplisitt at denne høye poengsum er mistenkt å være et **graph-embedding klusterings falskt positivt** i stedet for et biologisk forankret signal.

Dette mønsteret gjentar seg på alle sju rangerte kandidater i denne pakken: brachyolmia-amelogenesis imperfecta syndrom, myosclerosis, brachyolmia, brachydactyly-syndactyly syndrom, pseudoachondroplasia og colobomatous microphthalmia-rhizomelic dysplasia syndrom er alle sjeldne medfødte eller utviklingsmessige skjelettlidelser eller bindevevslidelser. Bare pseudoachondroplasias begrunnelse noterer en plausibel (men rent symptomatisk, ikke sykdomsmodifiserende) forbindelse — NSAID-bruk for leddsmerter — mens alle andre kandidater eksplisitt beskrives som manglende en kjent inflammatorisk eller mekanistisk banetilknytning til ibuprofen. Ingen av de sju kandidatene har noen støttende klinisk prøving- eller litteraturbevis.

---

## Bevis fra kliniske prøvinger

For øyeblikket ingen relaterte kliniske prøvinger registrert.

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Taiwan-markedsinformasjon

Ibuprofen har for øyeblikket **ingen markedsføringsautorisasjon i Taiwan** (0 lisenser på posten; markedsstatus: Ikke markedsført). Ingen produktnavn, doseringsform eller godkjent indikasjonsinformasjon er tilgjengelig for denne bevissamlingen.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merknad: TFDA-etikettadvarsler/kontraindikasjoner er registrert som et blokkerings-datgap (DG001) — dette er påkrevd før en S1-sikkerhet forhåndsvurdering kan fortsette.)*

---

## Konklusjon og neste skritt

**Beslutning: Avvent**

**Begrunnelse:**
Alle sju TxGNN-predikerte indikasjoner for ibuprofen er sjeldne medfødte skjelettlidelser/bindevevslidelser med L5-bevis (kun poengsum, ingen kliniske prøvinger eller litteratur), og den høyest rangerte kandidatens egen mekanistiske begrunnelse flagger det som et sannsynlig embedding-clustering falskt positivt med ingen kjent patogen overlapping med NSAID-farmakologi. Kombinert med et blokkerings-datgap på TFDA-etikettdata og et alvorlig-datgap på MOA, kan denne kandidaten ikke avansere forbi S0.

**For å fortsette, kreves følgende:**
- TFDA-etikettadvarsler/kontraindikasjoner (DG001, Blokkering) — påkrevd før en sikkerhet forhåndsvurdering
- DrugBank MOA-data (DG002, Alvorlig) for å ordentlig vurdere mekanistisk plausibilitet
- Uavhengig biologisk/genetisk begrunnelse-gjennomgang for å bekrefte eller utelukke det mistenkte embedding-clustering-artefakt før denne prediksjonen behandles som en levedyktig kandidat
- Hvis videre oppfølging ønskes, kjør TxGNN-rangering på nytt mot ikke-sjelden-sykdom-indikasjonssett for å sjekke om denne kandidatlisten gjenspeiler et systematisk klusteringsproblem spesifikt for ibuprofen-embedningen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

