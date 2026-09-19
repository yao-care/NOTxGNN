---
layout: default
title: Avibactam
parent: Kun modellprediksjon (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
---

# Avibactam
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Avibactam: Fra ingen godkjent indikasjon til streptokokk-pneumoni

## Sammendrag på en setning

Avibactam har ingen godkjent opprinnelig indikasjon eller regulatorisk markedstilstedeværelse registrert i denne evidenspakken — det er en ikke-β-laktam β-laktamase-hemmer som må administreres sammen med et β-laktam-antibiotikum (f.eks. ceftazidim) i stedet for å brukes alene. TxGNN-modellen predikerer et mulig signal for **streptokokk-pneumoni**, men dette er støttet av **0 kliniske studier** og **0 publikasjoner**, og modellens egen mekanistiske begrunnelse flagger eksplisitt denne forbindelsen som biologisk svak.

---

## Rask oversikt

| Emne | Innhold |
|------|--------|
| Opprinnelig indikasjon | Ingen godkjent indikasjon registrert (legemiddel ikke markedsført; opprinnelige indikasjondata utilgjengelige) |
| Predikert ny indikasjon | Streptokokk-pneumoni |
| TxGNN-prediksjonspoengsum | 99.70% |
| Bevisnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvente |

---

## Hvorfor er denne prediksjon rimelig?

Detaljerte data om virkningsmekanisme er for øyeblikket ikke tilgjengelige i den strukturerte legemiddelposten. Basert på mekanistiske notater knyttet til selve prediksjonen er avibactam kjent for ikke å ha noen iboende antibakteriell aktivitet — det fungerer som en ikke-β-laktam β-laktamase-hemmer og er kun klinisk nyttig i kombinasjon med et β-laktam-antibiotikum som ceftazidim, primært mot Ambler klasse A/C/D β-laktamase-produserende gram-negative organismer.

Denne bakgrunnen gir viktig kontekst for vurdering av toppprediksjon, *streptokokk-pneumoni*: modellens egen begrunnelse angir at pneumokkal-resistens hovedsakelig oppstår fra endringer i penicillin-bindende protein (PBP) i stedet for β-laktamase-produksjon, noe som betyr at avibactams kjernemekanisme ikke direkte adresserer denne patogenens resistansvei. Den mekanistiske forbindelsen blir derfor vurdert som svak.

De fem gjenværende predikerte indikasjonene (influensafølsomhet, uretetuberkulose, urinær schistosomiasis, hyperamylasemi, polyklonalt hyperviskositets-syndrom) spenner over virale, mykobakterielle, parasittiske, metabolske og immunologiske sykdomskategorier uten noen plausibel forbindelse til β-laktamase-hemming, og er eksplisitt annotert i evidenspakken som sannsynlige grafordbaserte falske positiver. Ingen av de seks prediksjoner er støttet av noen klinisk studie eller litteraturbevis.

---

## Bevis fra kliniske studier

For øyeblikket ingen relaterte kliniske studier registrert

---

## Litteraturbevis

For øyeblikket ingen relevant litteratur tilgjengelig

---

## Informasjon om norsk marked

Avibactam har ingen markedsføringstillatelse i Norge (0 lisenser registrert); ingen produkt- eller godkjent-indikasjon-data er tilgjengelige for dette legemidlet i det gjeldende datasettet.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvente**

**Begrunnelse:**
Topprangert prediksjon (streptokokk-pneumoni) har null støttende kliniske studier eller litteratur og er svekket av modellens egen mekanistiske analyse, som bemerker at avibactams β-laktamase-hemming ikke adresserer den PBP-medierte resistensen som er typisk for *S. pneumoniae*. Alle seks predikerte indikasjonene er på bevisnivå L5 (kun modellprediksjon), og de fem gjenværende kandidatene (influensa, uretetuberkulose, urinær schistosomiasis, hyperamylasemi, polyklonalt hyperviskositets-syndrom) viser ingen biologisk plausibilitet og er flagget som sannsynlige falske positiver — ingen av dem begrunner videre vurdering på dette tidspunktet.

**For å fortsette kreves følgende:**
- TFDA/regulatoriske merkedata (advarsler, kontraindikasjoner) — for øyeblikket et blokeringsdatakløft (DG001)
- Bekreftet virkningsmekanisme fra DrugBank eller primærlitteratur — for øyeblikket et høyalvorlighets-datakløft (DG002)
- Opprinnelig godkjent indikasjon og markedsføringstillatelsesregistreringer, siden ingen eksisterer i dette datasettet
- Ethvert preklinisk eller in vitro-bevis som spesifikt tester avibactam (alene eller i kombinasjon) mot *S. pneumoniae* før dette signalet kan eskaleres utover S0/Avvente

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

