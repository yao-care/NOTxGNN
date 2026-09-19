---
layout: default
title: Turoctocog Alfa Pegol
parent: Kun modellprediksjon (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa Pegol
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

# Turoctocog alfa pegol: Fra Hemofili A til Ervervet Mangel på Koagulasjonsfaktor

## Oppsummering i én setning

Turoctocog alfa pegol er en PEGylert rekombinant faktor VIII (FVIII) erstatningsterapi, opprinnelig utviklet for FVIII-mangel ved Hemofili A (utledet fra stoffets mekanistiske beskrivelse; formelle data om originalindikasjon er ikke ennå dokumentert i denne bevisepakken). TxGNN-modellens topprangerte prediksjon (trombocyttfrigjøringsforstyrrelse) holder ikke mekanistisk, så rapporten fremhever i stedet **Ervervet Mangel på Koagulasjonsfaktor** som den farmakologisk mest plausible kandidaten blant de 10 prediksjonene. **Ingen kliniske forsøk eller litteratur støtter for øyeblikket noen av de 10 predikterte indikasjonene** — dette er et rent modellprediktert tilfelle (L5) med et uløst MOA-datahull.

---

## Rask Oversikt

| Element | Innhold |
|------|------|
| Originalindikasjon | Ikke dokumentert i regulatoriske data (legemiddelet er ikke ennå markedsført i Norge); antatt å være Hemofili A / FVIII-mangel basert på stoffklasse |
| Prediktert Ny Indikasjon | Ervervet Mangel på Koagulasjonsfaktor (valgt som det mekanistisk sterkeste blant 10 kandidater; TxGNN sin #1-rangerte prediksjon, trombocyttfrigjøringsforstyrrelse, ble vurdert som ikke farmakologisk plausibel — se begrunnelse nedenfor) |
| TxGNN Prediktert Poengsum | 99.97% (rangert 525 av alle sykdomspredikasjoner) |
| Bevisnivå | L5 (modellprediksjon kun — ingen kliniske forsøk eller litteratur for noen av de 10 kandidatene) |
| Norsk Markedsstatus | ✗ Ikke markedsført |
| Antall Autorisasjoner | 0 |
| Anbefalt Avgjørelse | Opphold |

---

## Hvorfor Er Denne Prediktionen Rimelig?

Detaljerte formelle data om virkningsmekanisme er for øyeblikket et dokumentert hull (DG002, høy alvorlighetsgrad — DrugBank API-oppslag venter). Basert på kontekstinformasjon tilgjengelig i denne bevisepakken, er turoctocog alfa pegol en **PEGylert rekombinant faktor VIII-erstatningsterapi**, brukt til å korrigere FVIII-mangel ved Hemofili A.

Blant de 10 TxGNN-predikterte indikasjonene, involverer de fleste (trombocyttfrigjøringsforstyrrelse, pseudo-von Willebrand-sykdom, Glanzmanns thrombasteni, Scott-syndrom, kollagenreseptordefekter, konstitusjonell trombocytopeni, FNAIT, og to tvetydige/sannsynlig feilmerkede oppføringer) **trombocyttnivå-dysfunksjon eller urelaterte genetiske syndromer**, ikke koagulasjonsfaktormangel. FVIII-erstatning kan ikke korrigere defekter i trombocyttgranulesekresjonen, reseptoravvik, eller fosfatidylserinscrambling på membranen — disse prediksjonene gjenspeiler trolig TxGNN's kunnskapsgrafs klynging av sykdommer gjennom en delt «blødningstendens»-node heller enn genuine farmakologisk relevans.

**Ervervet Mangel på Koagulasjonsfaktor** skiller seg ut som unntak: denne kategorien inkluderer ervervet Hemofili A (f.eks. anti-FVIII autoantistoff-mediert FVIII-mangel), for hvilken standard/langtidsvirkende FVIII-erstatningsprodukter allerede brukes som støtteterapi i gjeldende praksis. Dette er den eneste av de 10 prediksjonene hvor sykdomsmekanismen (FVIII-utilstrekkelighet) direkte samsvarer med stoffets mekanisme (FVIII-erstatning) — og det er hvorfor bevisepakken fremhever det til beslutningstrinn S1 («Forskningsspørsmål») mens de øvrige 9 forblir på S0 (Opphold).

---

## Bevis fra Kliniske Forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert.

---

## Bevis fra Litteratur

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Informasjon om Norges Marked

Turoctocog alfa pegol er **ikke markedsført i Norge** — ingen produktautorisasjoner er for øyeblikket registrert (0 lisenser på fil), så ingen tabell over doseringsform eller godkjent-indikasjon kan produseres på dette tidspunktet.

---

## Sikkerhetshensyn

Vennligst se pakningslisten for sikkerhetsinformasjon. (Merk: TFDA/etikett-advarsler og kontraindikasjoner er flagget som et **Blokkerende datahull** (DG001) i denne bevisepakken — de må løses før noen sikkerhet-forhåndsvurdering (S1) kan fortsette.)

---

## Konklusjon og Neste Trinn

**Avgjørelse: Opphold**

**Begrunnelse:**
Alle 10 TxGNN-predikterte indikasjonene for turoctocog alfa pegol har for øyeblikket null støttende kliniske forsøk eller litteratur (L5, prediksjon kun), legemiddelet er ikke markedsført i Norge, og både de formelle MOA-data og TFDA/etikett-sikkerhetsdataene er dokumenterte hull. Selv den mekanistisk mest plausible kandidaten (ervervet koagulasjonsfaktormangel) har ingen direkte bevis ennå — den kvalifiserer bare for videre undersøkelse (S1), ikke videre fremdrift.

**For å gå videre er følgende nødvendig:**
- Løs DG001 (Blokkerende): innhent TFDA/Norge-etikettvarsler og kontraindikasjoner før noen S1-sikkerhetsvurdering
- Løs DG002 (Høy): bekreft formell MOA via DrugBank API for å validere den mekanistiske begrunnelsen for FVIII-erstatning
- Søk spesifikt etter litteratur/kasusserier på FVIII-produktbruk i ervervet Hemofili A / ervervet koagulasjonsfaktormangel
- Revurder de gjenværende 9 prediksjonenes plausibilitet før du allokerer videre ressurser til disse

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

