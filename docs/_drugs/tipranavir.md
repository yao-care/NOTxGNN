---
layout: default
title: Tipranavir
parent: Kun modellprediksjon (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: Fra HIV-1-infeksjon til felint ervervet immunsviktssyndrom

## Sammendraging i en setning

> Tipranavir (DB00932) er offentlig kjent som en ikke-peptidisk HIV-1-proteasehemmer, selv om evidenspakningen inneholder datahull for både den opprinnelige indikasjonen og virkningsmekanismen.
> TxGNN-modellens topprangerte prediksjon er **felint ervervet immunsviktssyndrom (FIV)**, en veterinærsykdom — dette er **ikke en levedyktig menneskelig indikasjon** og reflekterer en artsspecifikk artefakt i kunnskapsgrafen snarere enn et genuint ombruksignal.
> Ingen kliniske forsøk eller litteratur støtter direkte denne toppprediksjonen; de eneste materielt dokumenterte kandidatene (rangert #5–#6) er bare repetitioner av tipranavirens allerede kjente HIV/AIDS-indikasjon, ikke nye indikasjoner.

---

## Hurtig oversikt

| Punkt | Innhold |
|-------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig i datasett (datahull — ingen `approved_indication_text` på fil; tipranavir er offentlig kjent som en HIV-1-proteasehemmer for behandlingserfarne pasienter) |
| Forutsagt ny indikasjon | Felint ervervet immunsviktssyndrom (veterinærsykdom; ikke aktuelt for mennesker) |
| TxGNN-prediksjonspoengsum | 99.99% |
| Bevisnivå | L5 |
| Status for norsk marked | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt handling | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert virkningsmekanismedata er ikke tilgjengelig i denne evidenspakningen (markert som blokeringskritisk datahull, DG001/DG002). Basert på offentlig kjent farmakologi som refereres konsistent gjennom evidenspakingens egen begrunnelsestekst, er tipranavir en ikke-peptidisk HIV-1-proteasehemmer som blokkerer spalting av virusets Gag-Pol polyprotein, historisk angitt for behandlingserfarne HIV-1-infiserte voksne.

Topprangerte prediksjon, felint ervervet immunsviktssyndrom (FIV), scorer ekstremt høyt i TxGNN, men er en **veterinærsykdom som er artsspecifikk**. Likheten som driver denne scoren er en strukturell homologi mellom HIV-1 og lentiviral (FIV) proteasene — en kjent embedding-artefakt der modellen blander kryssarts-proteasehomologi med terapeutisk relevans. Denne veien har ingen menneskelig klinisk utviklingsrute og bør ikke tolkes som en genuint ombruksmulighet. Det samme mønsteret forklarer ranger #2–#4 og #7–#10 (SIV-infeksjon, en sjelden nevroutviklingsforstyrrelse, en foreldet hyperlipidemiediagnose, og flere urelaterte godartede svulster): ingen av disse har en plausibel mekanistisk sammenheng med proteasehemmning, og flere (f.eks. hyperlipidemi) er mekanistisk *motsagt* av tipranavirens kjente lipidrelaterte bivirkningsprofil.

De eneste kandidatene med noen vesentlig evidensbase er rangert #5 ("AIDS-relatert kompleks") og #6 ("medfødt menneskelig immunsviktsvirus"), begge scoret L4/S1 ("Forskningsspørsmål"). Imidlertid er disse ikke nye indikasjoner — de er historiske/pediatriske klassifiseringer innenfor HIV/AIDS, sykdomsområdet som tipranavir allerede er kjent for å behandle. Rank #6s støttende forsøk er nesten helt for *andre* antiretrovirale midler (cabotegravir, dolutegravir, rilpivirine) og gir bare klassenivåstøtte, ikke legemiddelspesifikk støtte.

---

## Klinisk forsøksbevis

Det er for øyeblikket ingen relaterte kliniske forsøk registrert.

*(Merk: topprangerte prediksjon, FIV, har ingen klinisk forsøksbevis, som forventet for en ikke-menneskelig sykdom. Den mer mekanistisk sammenhengene, men ikke-nye kandidaten "medfødt menneskelig immunsviktsvirus" har 9 tilknyttede forsøk, ingen spesifikk for tipranavir — se begrunnelse ovenfor.)*

---

## Litteraturbevis

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Norsk markedsinformasjon

Tipranavir er ikke for øyeblikket markedsført i Norge (`market_status: Not marketed`) og har 0 registrerte godkjennelser. Ingen lisensdata er tilgjengelige for denne evidenspakningen.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Topprangerte TxGNN-prediksjon (FIV) er en veterinærsykdom uten noen plausibel menneskelig utviklingsbane, og ingen av de øvrige topp-10-prediksjoner utgjør en troverdig, bevisbasert *ny* menneskelig indikasjon — de eneste vitenskapelig konsistente kandidatene (AIDS-relatert kompleks, medfødt HIV) gjentar rett og slett tipranavirens kjente HIV/AIDS-indikasjon i stedet for å avdekke ny terapeutisk potensial. Kombinert med det kritiske fraværet av TFDA/officiell merkedata, kvalifiserer ikke denne kandidaten til å avansere forbi S1-screening.

**For å gå videre kreves følgende:**
- Offisiell merke-/monografidata (TFDA eller tilsvarende) for å løse DG001 (advarsler/kontraindikasjoner) og DG002 (MOA)
- Bekreftet data for opprinnelig indikasjon for å muliggjøre gyldig MOA-til-ny-indikasjon-sammenligning
- Ny kjøring av TxGNN-filtrering for å ekskludere ikke-menneskelige sykdomsnoder og gjentagelser av legemidlets kjente indikasjon før rangeringen anses som handlingsbar
- Hvis en genuint ny indikasjon ønskes, evaluer lavere rangerte kandidater med uavhengig mekanistisk plausibilitet utover proteasehomologi-artefakter

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

