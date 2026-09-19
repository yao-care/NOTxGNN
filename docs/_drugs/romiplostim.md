---
layout: default
title: Romiplostim
parent: Kun modellprediksjon (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Romiplostim
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

# Romiplostim: Fra immun trombocytopeni (ITP) til primær utskillelsesforstyrrelse av blodplater

## Sammenfattelse i én setning

> Romiplostim er en trombopoetin (TPO)-reseptor-agonist hvis etablerte referanseindikasjoin er immun trombocytopeni (ITP) — dette er ikke formelt dokumentert i det nåværende datasettet, men er konsekvent antydet gjennom det vitenskapelige materiales mekanistiske begrunnelse.
> TxGNN-modellens høyest rangerte prediksjon er **Primær utskillelsesforstyrrelse av blodplater**,
> for tiden støttet av **1 klinisk forsøk** og **2 publikasjoner**, begge indirekte (overlapp mellom sykdompopulasjoner snarere enn direkte behandlingsvitenskapslig bevis).
> En separat, bredere kandidat i det samme vitenskapelige materiale — *blødningsforstyrrelse av platelet-type* — har langt sterkere direkte vitenskapslig bevis (7 forsøk inkludert en gjennomført fase 3 RCT), og er flagget separat nedenfor.

---

## Rask oversikt

| Emne | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke dokumentert i dette datasettet (`original_indications` tomt, `original_moa` = Datagap). Romiplostims kjente referanseindikasjoin — immun trombocytopeni (ITP) — blir referert til gjennom hele det vitenskapelige materiales mekanistiske begrunnelse, men er ikke formelt kildeangivet her. |
| Predikert ny indikasjon | Primær utskillelsesforstyrrelse av blodplater |
| TxGNN-prediksjonspoengsum | 99.9998% |
| Bevisnivå | L3 (observasjonsstudie + review/kohort-litteratur; ingen direkte romiplostim RCT for denne spesifikke diagnosen) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Forskningsspørsmål |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert formell virkningsmekanisme-dokumentasjon er for tiden et datagap (DG002). Det vitenskapelige materiales egen begrunnelse for omformål beskriver konsekvent romiplostim som en **trombopoetin (TPO)-reseptor-agonist** som virker på **MPL-reseptoren** for å fremme megakaryocytt-modning og blodplateutskillelse — dette er det farmakologiske grunnlaget sitert gjennom nesten hver kandidatindikasjoin i dette materiale.

"Primær utskillelsesforstyrrelse av blodplater" beskriver en defekt i blodplateutskillelse fra megakaryocytter inn i blodsirkulasjonen. Mekanistisk er stimulering av MPL-reseptoren for å drive megakaryocytt-modning og blodplateutskillelse en plausibel tilpasning for denne kategorien. Imidlertid er det vitenskapelige beviset som for tiden er tilgjengelig, hentet fra **immun trombocytopeni (ITP)**-forskning — en *sekundær* (immunmediert) utskillelsesforstyrrelse — snarere enn fra primær/iboende utskillelsesdefekt-populasjoner spesifikt. Det eneste koblede kliniske forsøket (NCT03820960) er en observasjonskohortstudie om tromboserisikofaktorer hos ITP-pasienter og tester ikke romiplostim-behandling; det ble koblet av TxGNN på grunn av overlapp mellom sykdompopulasjoner, ikke direkte intervensjonsvitenskapslig bevis.

Kort sagt, er den mekanistiske logikken solid, men det nåværende vitenskapelige grunnlaget har ikke ennå direkte testet romiplostim hos pasienter med en primær (ikke-immunmediert) blodplateutskillelsesdefekt.

---

## Vitenskapslig bevis fra kliniske forsøk

| Forsøksnummer | Fase | Status | Deltakere | Viktigste funn |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A | Gjennomført | 10,039 | Observasjonskohortstudie om tromboserisikofaktorer hos pasienter med immun trombocytopeni (ITP). Tester ikke romiplostim-behandlingseffekt; koblet til denne indikasjon via overlapp mellom sykdompopulasjoner kun (relevansgrad C). |

---

## Litteraturvitenskapslig bevis

| PMID | År | Type | Tidsskrift | Viktigste funn |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Review | British Journal of Haematology | Gjennomgår megakaryocytopoiese og thrombocytopoiese-mekanismer, og identifiserer trombopoetin (TPO) som den primære vekstfaktoren som driver megakaryocytt-modning og blodplateutskillelse. |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Kohort | Haematologica | In vitro-studie som viser at antiblodplate-autoantistoffer hos ITP-pasienter hemmer proplatelett-danningen fra megakaryocytter, og hemmer dermed blodplateproduksjon/-utskillelse. |

---

## Markedsinformasjon for Norge

Ingen markedsautoritetsregistre for Norge (eller Taiwan) er for tiden tilgjengelig for romiplostim i dette datasettet — legemidlet er registrert som ikke markedsført (0 godkjennelser).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjoner er alle for tiden merket som datagap i dette materiale; TFDA-merketikettdatahenting (DG001) er flagget som blokkering for en formell sikkerhetsprevurdering.)*

---

## Konklusjon og neste trinn

**Beslutning: Forskningsspørsmål**

**Begrunnelse:**
Den mekanistiske koblingen mellom TPO-reseptor-agonisme og blodplateutskillelsesforstyrrelse er biologisk plausibel, men det eneste støttende forsøket er en observasjonskohortstudie som ikke tester romiplostim direkte, og ingen intervensjonsvitenskapslig bevis finnes spesifikt hos pasienter med primær (ikke-immunmediert) blodplateutskillelsesdefekt. Dette oppfyller ikke ennå grensen for "Fortsett med sikkerhetstiltak."

**For å fortsette, er følgende nødvendig:**
- TFDA-pakningsvedlegg / merketikettdata (DG001 — for tiden blokkering, nødvendig før noen sikkerhetsprevurdering)
- Formell virkningsmekanisme-dokumentasjon (DG002)
- Et forsøk eller kasuistikkserie som tester romiplostim spesifikt hos pasienter med en primær (iboende, ikke-immunmediert) blodplateutskillelsesdefekt, snarere enn ITP-avledet slutning
- Norge/Taiwan-regulering og markedsautoritetsdata, for tiden helt fraværende

**Merknad om en sterkere alternativ kandidat i det samme prediksjonssettet:**
Innenfor samme prediksjonssett, *"blødningsforstyrrelse av platelet-type"* (rangering 8, poengsum 99.93%) har vesentlig sterkere direkte vitenskapslig bevis — **L1**, med en gjennomført fase 3 RCT (RECITE, kjemoterapiindusert trombocytopeni hos GI/pankreas/kolorektal kreft, n=165) pluss 6 ytterligere direkte relevante forsøk (blodplate-engraftment etter transplantasjon, MDS, biosimilar langtidssikkerhet) — og er allerede trinnvist "Fortsett med sikkerhetstiltak." Hvis målet er å identifisere det mest handlingsdyktige omformål-signal for romiplostim snarere enn strengt tatt det høyest rangerte TxGNN-poengsum, forsvarer denne kandidaten en separat, dedikert vurdering.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

