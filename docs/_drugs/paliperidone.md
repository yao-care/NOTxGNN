---
layout: default
title: Paliperidone
parent: Høy evidens (L1-L2)
nav_order: 261
evidence_level: L2
indication_count: 10
---

# Paliperidone
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **10** stk.
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

# Paliperidone: Fra schizofreni til behandlingsresistent schizofreni

## Sammendrag på en setning

Paliperidone er et antipsykotikum (det aktive metabolitten av risperidon, D2/5-HT2A-reseptorantagonist) som allerede brukes til schizofreni-spektrum-lidelser. TxGNN-modellen returnerte ni høyere-scorede prediksjoner (retinal dystrofi, X-koblet/syndromisk myopi, hydranensefall, en glykosyleringsforstyrrelse, CMT type 1G, glysinencefalopati) som bevisberetningen selv flaggerer som mekanistisk implausible med **null støttende studier eller litteratur** — disse behandles som modellstøy, ikke kandidater. Den eneste prediksjonen med reell støtte er en utvidelse til **behandlingsresistent schizofreni**, støttet av **4 kliniske studier** og **2 publikasjoner**.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke dokumentert i Norges licensieringsdata (0 godkjennelser); mekanistisk etablert som schizofreni/schizoaffektiv lidelse i henhold til medikamentets kjente antipsykotikum-klasse |
| Forutsagt ny indikasjon | Behandlingsresistent schizofreni (valgt fra rangering 10 — se merknad nedenfor om hvorfor rangering 1 ikke ble brukt) |
| TxGNN-prediksjonspoengsum | 99,80% (poengsum 0,99796, rangering 2663) |
| Bevisnivå | L2 |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt avgjørelse | Avvent |

> **Merknad om rangering:** TxGNNs ni øverste prediksjoner etter poengsum (rangering 1 = retinal dystrofi ved 99,92%, nedover til glysinencefalopati) har **ingen kliniske studier, ingen litteratur, og ingen mekanistisk begrunnelse** — bevisberetningens egne merknader sier eksplisitt at det er "ingen identifiserbar farmakologisk mekanismekobling" for hver. Disse blir avvist som falske grafstøysignaler. Det lavest-scorede prediksjonen i dette settet, **behandlingsresistent schizofreni** (rangering 10, fremdeles >99,7% poengsum), er den eneste med reell studie- og litteraturstøtte og en sammenhengende mekanisme, så det brukes som den fremtredende kandidaten i denne rapporten.

---

## Hvorfor er denne prediksjonen rimelig?

Medikamentnivå-virkningsmekanisme-data er formelt flagget som et gap (**DG002, Høy alvorlighetsgrad**) — ingen strukturert MOA-journal kunne hentes fra DrugBank ved denne avslutningen. Imidlertid dokumenterer bevisberetningens egen rasjonale for omformål at paliperidone er det aktive metabolitten av risperidon og fungerer som en **D2/5-HT2A-reseptorantagonist**, som er den kjernefarmakologiske mekanismen bak antipsykotikum-terapi.

Dette er ikke et klassisk krysssykdom-omformålingstilfelle — paliperidones etablerte terapeutiske klasse målretter allerede schizofreni. Den "nye indikasjonen" her bør bedre forstås som en utvidelse av bruk til en **behandlingsresistent subpopulasjon** av samme sykdom, støttet av virkelighetens naturalistiske og komparativ-effektivitets-forsøksdesign (f.eks. paliperidone palmitat case-serier, aripiprazol-vs-paliperidone multi-omics RCT). Dette er mekanistisk sammenhengende og lavere-risiko enn de ni andre modellprediksjoner, som involverer urelaterte medfødt, oftalmologisk, nevro-utviklings-, og metaboliske lidelser uten plausibel kobling til sentral dopamin/serotonin-reseptor-blokkering.

---

## Bevis fra kliniske forsøk

| Prøvenummer | Fase | Status | Rekruttering | Viktige funn |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Fase 4 | Gjennomført | 30 | Prospektiv naturalistisk case-serie evaluerer paliperidone palmitat-effektivitet på tvers av tre schizofreni-pasientundergrupper |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Fase 4 | Rekrutterer | 40 | Kombinerer farmakoterapie med gjenopprettings-orienterte programmer (RECOVERYTRSGR/RECOVERYTRSBDGR) for behandlingsresistent schizofreni og bipolar lidelse |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Fase 4 | Avsluttet | 5 | Sammenlignet klozapin vs. ikke-klozapin-antipsykotika på inflammatoriske markører ved behandlingsresistent schizofreni; lav relevans, avsluttet tidlig med minimal rekruttering |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Fase 4 | Ukjent status | 244 | Åpen-label multisenter RCT (SchizOMICS) som sammenligner aripiprazol vs. paliperidone/risperidon ved hjelp av multi-omics data ved første-episode psykose |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Gjennomgang | Actas Españolas de Psiquiatría | Gjennomgår bevis for antipsykotikum-farmakoterapie ved schizoaffektiv lidelse, og merker mangelen på lidelsesspecifikk behandlingsveiledning |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Gjennomgang | Current Opinion in Psychiatry | Bevisbasert farmakologisk tilnærming til tidlig-oppstart schizofreni-spektrum-lidelser, inkludert dosering og bivirkningsovervåking |

---

## Norges markedsinformasjon

Ingen markedsføringstillatelser ble funnet for paliperidone i Norges regulatorisk datasett (`taiwan_regulatory.total_licenses = 0`; markedsstatus: Ikke markedsført / Ikke markedsført).

---

## Sikkerhetshensyn

Vær vennlig å se pakkevedlegget for sikkerhetsinformasjon. En **blokkeringsdatakløft (DG001)** eksisterer: TFDA-ekvivalente etikettadvarsler og kontraindikasjoner for paliperidone kunne ikke hentes ved denne avslutningen, noe som forhindrer denne kandidaten fra å gå inn i S1-sikkerhet-før-vurderingsfasen. Ingen legemiddel-legemiddel-interaksjonsdata ble funnet i gjeldende spørring (`ddi.query_status: not_found`).

---

## Konklusjon og neste trinn

**Avgjørelse: Avvent**

**Begrunnelse:**
Selv om behandlingsresistent schizofreni-indikasjonen har sammenhengende mekanistisk begrunnelse og moderat klinisk bevis (L2, 4 studier, 2 gjennomganger) som ellers ville støtte en "Fortsett med sikkerhetstiltak"-oppfordring, forhindrer medikamentnivå-sikkerhetsdatakløften (DG001, Blokkering) denne kandidaten fra ennå å kunne gå inn i S1-sikkerhet-før-vurderingen, og medikamentet er ikke for tiden markedsført i Norge (0 godkjennelser). De ni andre TxGNN-flaggede indikasjoner (retinal dystrofi, myopi-undertyper, hydranensefall, glykosyleringsforstyrrelse, CMT type 1G, glysinencefalopati) bør utelukkes fra videre evaluering — de har ingen klinisk, litteratur- eller mekanistisk støtte og ser ut til å være kunnskapsgraf-artefakter.

**For å fortsette er følgende nødvendig:**
- Hent TFDA-ekvivalente etikettadvarsler/kontraindikasjoner (DG001) for å oppheve S1-sikkerhetskjønn
- Hent strukturert MOA-data fra DrugBank (DG002) for å formelt støtte den mekanistiske begrunnelsen
- Bekreft Norges markedsføring/importvei-status, siden medikamentet for tiden har null lokale godkjennelser
- Hvis DG001/DG002 blir løst gunstig, re-score behandlingsresistent schizofreni for "Fortsett med sikkerhetstiltak" og definer spesifikke overvåkingssikkerhetstiltak (f.eks. metabolisk/EPS-overvåking i henhold til antipsykotikum-klasse-normer)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

