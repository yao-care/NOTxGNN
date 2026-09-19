---
layout: default
title: Avelumab
parent: Kun modellprediksjon (L5)
nav_order: 41
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: Fra merkelcellekarsinom til menneskelig herpesvirus 8-relatert tumor

## Oppsummering i én setning

Avelumab er et anti-PD-L1 monoklonalt antistoff som er internasjonalt godkjent for merkelcellekarsinom og urotelielt karsinom (det finnes ingen informasjon om norsk godkjenning i dette bevisepakken). Topprangert prediksjon fra TxGNN-modellen er **Menneskelig herpesvirus 8-relatert tumor** (f.eks. HHV-8-assosiert Kaposi sarkom / primær effusjonlymfom), men denne prediksjonen er for øyeblikket støttet av **0 kliniske studier** og **0 publikasjoner** — det er rent modelloutput uten bekrefende bevis.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke godkjent i Norge (0 godkjennelser); internasjonalt godkjent for merkelcellekarsinom og urotelielt karsinom |
| Forutsagt ny indikasjon | Menneskelig herpesvirus 8-relatert tumor |
| TxGNN prediksjonsresultat | 99.97% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte data om virkningsmekanisme ikke tilgjengelige (flagget som en blokkerende datakløft, DG002). Basert på informasjonen som ligger i dette bevisepakken, er avelumab et anti-PD-L1 monoklonalt antistoff, og dets effektivitet er etablert for merkelcellekarsinom og urotelielt karsinom — begge tilstander der PD-L1-formidlet immunflukt driver tumorprogresjon.

Den mekanistiske begrunnelsen for HHV-8-relaterte tumorer er at virusassosierte ondartede sykdommer (f.eks. Kaposi sarkom, primær effusjonlymfom) også ofte utnytter checkpoint-formidlet immunflukt, og blokkering av PD-L1 kunne teoretisk gjenopprette T-celle-gjenkjenning av virale tumorantigener. Imidlertid presenterer denne populasjonen seg vanligvis med samtidig HIV-infeksjon eller annen immunsuppresjon, som vesentlig kompliserer risiko-fordel-profilen for checkpoint-blokkering og som ikke behandles noe sted i dette datasettet.

Dette forblir en ekstrapolasjon basert kun på mekanisme: det er ingen PD-L1-uttrykkdata, ingen preklinisk modell, og ingen klinisk eller litteraturbevis spesifikt for HHV-8-relaterte tumorer som støtter prediksjonen.

---

## Bevis fra kliniske studier

For øyeblikket er det ingen relaterte kliniske studier registrert.

---

## Litteraturbevis

For øyeblikket er det ingen relatert litteratur tilgjengelig.

---

## Cytotoksisitet

Avelumab er et antineoplastisk legemiddel (checkpoint-hemmer-klasse), så denne delen er inkludert.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Immunterapi (anti-PD-L1 monoklonalt antistoff; ikke konvensjonell cytotoksisk kjemoterapi) |
| Myelosuppresjonsrisiko | Lav — checkpoint-hemmere er vanligvis ikke myelosuppressive; toksisitet er primært immun-relatert (irAEs) snarere enn hematologisk |
| Emetogenitetsklassifisering | Lav |
| Overvåkingselementer | Thyroidea-, lever- og nyrfunksjon; overvåking av infusjonsrelaterte reaksjoner; overvåking av immun-relaterte bivirkninger (kolitt, pneumonitt, endokrinopatier) |
| Håndteringsbeskyttelse | Ingen spesiell håndteringsprotokoll for cytotoksiske legemidler nødvendig; standard biologisk infusjonsforholdsregler gjelder |

Merknad: Ingen medikamentspesifikk toksisitetsdatasett var tilgjengelig (DrugBank-toksisitetsfelt tomme); det ovennevnte reflekterer generelle klassekjennetegn for PD-L1-hemmere og bør bekreftes mot det offisielle pakningsvedlegget når det blir tilgjengelig.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (Hovedadvarsler, kontraindikasjoner og DDI-data er alle flagget som datakløfter eller «ikke funnet» i dette bevisepakken — DG001 er en blokkerende kløft.)

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Topprangert prediksjon (Menneskelig herpesvirus 8-relatert tumor) har et L5 bevisnivå — ingen kliniske studier, ingen litteratur, og en plausibel men ubekreftet mekanistisk begrunnelse komplisert av hyppig HIV/immunsuppresjon komorbiditet i denne populasjonen. Dette oppfyller ikke terskelen for å avansere til sikkerhetsprøving (S1).

**For å fortsette er følgende nødvendig:**
- Offisielle etikettdata (advarsler/kontraindikasjoner) fra TFDA eller tilsvarende regulatorisk kilde — blokkerer for øyeblikket (DG001)
- Formell MOA-dokumentasjon fra DrugBank eller produktetikett (DG002)
- Preklinisk eller biomerkebevis for PD-L1-uttrykk i HHV-8-assosierte tumorer
- Sikkerhetsvurdering spesifikk for samtidsforekommende HIV/immunsupprimerte populasjoner før noen klinisk utforskning

**Merknad:** Blant de 10 kandidatene i dette bevisepakken viser rangene 9–10 (urotelielt karsinom i prostatisk urethra; sarkomatiod transisjonscellekarsinom i nyrebasseng) sammenlignbar sterkere mekanistisk grunnlag — begge er histologiske/anatomiske utvidelser av avelumabs allerede godkjente urotelielt karsinom-indikasjon, og rang 10 har én fullført real-world observasjonsstudie (NCT05431777, L3). Disse kan berettige prioritering over topprangert HHV-8-prediksjon for videre evaluering.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

