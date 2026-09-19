---
layout: default
title: Regadenoson
parent: Kun modellprediksjon (L5)
nav_order: 299
evidence_level: L5
indication_count: 4
---

# Regadenoson
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Regadenoson: Fra farmakologisk kardial stressagens til anafilaksi (sannsynlig artefakt)

## Enlinjesammendrag

Regadenoson er en adenosin A2A-reseptoragonist som brukes internasjonalt som farmakologisk stressagens for kardial perfusjonsavbilding; ingen godkjent indikasjon i Taiwan/Norge eller MOA-registrering er for øyeblikket arkivert.
TxGNN-modellens beste forutsigelse er **Anafilaksi**, men dette signalet er mest sannsynlig et omvendt-kausalitet-artefakt — anafilaktor/overfølsomhetsreaksjon er en kjent **bivirkning** av regadenoson, ikke et behandlingsmål.
Bevisstøtten er minimal: **1 klinisk forsøk (vurdert irrelevant, "C")** og **0 støttende publikasjoner**.

---

## Hurtigoversikt

| Element | Innhold |
|------|------|
| Originalindikasjon | Ikke tilgjengelig i evidenspakken (legemiddel ikke godkjent i Taiwan/Norge; internasjonalt brukt som farmakologisk kardial stresstest-agens) |
| Forutsagt ny indikasjon | Anafilaksi |
| TxGNN forutsigelsesscore | 99.85% |
| Bevisnivå | L5 (kun modellforutsigelse, ingen støttende virkelighetsbeviser) |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | **Ventilasjon** |

---

## Hvorfor er denne forutsigelsen rimelig?

For øyeblikket er detaljert virkningsmekanisme-data ikke tilgjengelig (Datakløft). Basert på tilgjengelig bevis er regadenoson en adenosin A2A-reseptoragonist. I den identifiserte kliniske forsøkskonteksten brukes det som en farmakologisk stressagens for å simulere øvelsesinindusert kardial blodstrømsendringer under MR/perfusjonsavbilding — ikke som en sykdomsmodifiserende terapeutisk.

Kritisk er at bevispakningen selv eksplisitt identifiserer at overfølsomhet/anafilaktor-reaksjoner er en **kjent, merket bivirkning** av regadenoson. Dette betyr at TxGNN-forutsigelsen som forbinder regadenoson med "anafilaksi" mest sannsynlig gjenspeiler en *legemiddel-forårsaker-bivirkning*-forhold innebygd i kunnskapsgrafen, snarere enn et *legemiddel-behandler-sykdom*-forhold. Dette er en velkjent sviktmodus for embedding-baserte forutsigelsesmodeller (omvendt kausalitet / polaritets-forvirring) og bør ikke tolkes som et genuint behandlingssignal.

De gjenstående tre kandidatene (matavhengig øvelsesinindusert anafilaksi, esotropi, pseudoallergi) viser ingen identifiserbar mekanisk sammenheng med A2A-reseptorfarmakologi, og pseudoallergi har samme omvendt-kausalitet-bekymring som beste forutsigelse. Ingen av de fire kandidatene er støttet av kliniske forsøk eller litteratur.

---

## Klinisk forsøksbevis

| Forsøksnummer | Fase | Status | Inklusjon | Viktige funn |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | N/A | Rekrutterer | 1000 | Flersentersstudie av stresskardialt MR-perfusjonsavbilding; regadenoson brukt som farmakologisk stressagens for vurdering av koronar blodstrøm. Ikke designet for behandling av anafilaksi — eventuelle anafilaksi-hendelser ville være sikkerhetsovervåkings-endepunkter, ikke effektivitets-endepunkter. **Relevansgrad: C (støtter ikke den forutsagte indikasjon).** |

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon Norge

Regadenoson har for øyeblikket ingen markedsføringsgodkjennelse arkivert (0 lisenser; markedsstatus: Ikke markedsført). Ingen produkttabell kan genereres.

---

## Sikkerhetshensyn

- **Viktige advarsler**: Ikke tilgjengelig i strukturert sikkerhetsdata (Datakløft). Merk imidlertid at bevispakningen eksplisitt identifiserer overfølsomhet/anafilaktor-reaksjon som en kjent merket risiko for regadenoson — dette er direkte relevant for tolking av beste-rangerte forutsigelse og bør behandles som et sikkerhetssignal, ikke en behandlingsmulighet.
- **Legemiddelinteraksjoner**: Søket ga ingen resultater (ikke funnet).

Vennligst se pakningsvedlegget for fullstendig sikkerhetsinformasjon når den blir tilgjengelig (se Datakløft DG001, for øyeblikket merket som blokkering).

---

## Konklusjon og neste trinn

**Beslutning: Ventilasjon**

**Begrunnelse:**
Alle fire forutsagte indikasjonene er Bevisnivå L5 (kun modellforutsigelse), med enten irrelevant (Grad C) eller ingen klinisk forsøksstøtte og null støttende litteratur. Den best-rangerte kandidaten, anafilaksi, er meget sannsynlig et omvendt-kausalitet-artefakt som gjenspeiler en kjent legemiddelreaksjon snarere enn et genuint terapeutisk forhold, og legemiddelet er ikke markedsført i Norge eller Taiwan.

**For å fortsette, kreves følgende:**
- Avklare DG001 (Blokkering): innhent offisiell merkeadvarsel/motindikasjoner fra TFDA før noen sikkerhetsvurdering kan igangsettes
- Avklare DG002 (Høy): bekreft virkningsmekanisme via DrugBank for å riktig vurdere mekanistisk plausibilitet
- Uavhengig verifisering av TxGNN edge polaritet (behandler vs. forårsaker) for anafilaksi-forutsigelsen før ytterligere investering
- Hvis forfølgt, søk prospektiv klinisk eller kasuistisk bevis som spesifikt evaluerer et terapeutisk (ikke en bivirkning) forhold mellom regadenoson og noen av de fire kandidat-indikasjonene

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

