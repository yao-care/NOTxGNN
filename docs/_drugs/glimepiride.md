---
layout: default
title: Glimepiride
parent: Kun modellprediksjon (L5)
nav_order: 163
evidence_level: L5
indication_count: 9
---

# Glimepiride
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

# Glimepirid: Fra type 2-diabetes til Focal Stiff Limb Syndrome (virkningsmåte-assosiasjon usikker)

## Oppsummering i en setning

Glimepirid er et sulfonylureum-basert oralt antidiabetikum som virker på KATP-kanalen i bukspyttkjertelceller (β-celler) for å fremme insulinutskillelse.
TxGNN-modellen forutsier at det muligens kan være effektivt for **Focal Stiff Limb Syndrome**,
men det finnes for tiden **ingen kliniske forsøk eller litteraturstøtte**, og modellens egen mekanismegenerering indikerer allerede at dette sannsynligvis er en falsk positiv lenke i kunnskapsgrafen.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Type 2-diabetes (konkludert fra farmakologisk kunnskap; Evidence Pack gir ingen formell godkjenningsindikasjon, `original_indications` er tom) |
| Forutsagt ny indikasjon | Focal Stiff Limb Syndrome |
| TxGNN-prediksjonspoengsum | 99.75% (rangering 3254 / total database) |
| Bevisnivå | L5 (kun modellprediksjon, ingen faktisk forskning) |
| Markedsstatus lokalt | ✗ Ikke markedsført |
| Antall godkjenningssertifikater | 0 |
| Anbefalt beslutning | **Hold** |

---

## Hvorfor er denne prediksjonen mekanistisk tvilsom?

Glimepirids virkningsmåte er å blokkere KATP-kanalen i bukspyttkjertelceller (SUR1/Kir6.2-underenheter), som forårsaker cellular depolarisering og kalsiuminnstrømming, noe som stimulerer insulinutskillelse – en typisk sulfonylureum-virkningsmåte begrenset til øyer-β-celler og glukosekontrollveier.

Focal Stiff Limb Syndrome er en del av Stiff Person Syndrome-spekteret, hvis kjernepathologi er anti-GAD65-antistoff som forårsaker GABA-syntesestyrke i sentralnervesystemet, noe som forårsaker muskelstivhet og kramper – en autoimmunsykdom i nervesystemet uten kjent kryssing med sulfonylureums insulinsekresjonsmekanisme.

I henhold til `repurposing_rationale` som er gitt i Evidence Pack, er denne høye-scoren-prediksjonen **svært sannsynlig å være en kunnskapsgrafs falsk-positiv**: GAD65-proteinet uttrykkes både i sentralnervesystemets GABAerg-neuroner og i bukspyttkjertelceller (β-celler); TxGNN genererte sannsynligvis denne feilaktige høye-score-assosiasjonen via "GAD65/diabetes"-felveien snarere enn å gjenspeile ekte farmakologisk sannsynlighet. Det er ingen støtte for å bygge en biologisk hypotese for denne prediksjonen, og det finnes ingen formell mekanisme-nivå (MOA) data til verifisering – `original_moa` er klassifisert som datakløft, en høy-prioritets informasjonshull for dette tilfellet.

> Tilleggsmerknad: Blant disse ni kandidatindikasjonene er det niende kandidatet «Pancreatic agenesis» (bukspyttkjertel-agenesie) med relativt mer rimelig mekanismeformodling (sulfonylureum er kjent for å kunne brukes i nyfødt diabetes forårsaket av KATP-kanal-gen KCNJ11/ABCC8 mutasjoner), men fordi pasienter med bukspytktkjerttel-utviklingsmangler kan mangle tilstrekkelig funksjonelle β-celler, er rimelighetens sikkerhet fortsatt betydelig usikker, og den eneste tilgjengelige litteraturen (PMID 12720536) har ingen direkte tilknytning til denne indikasjonen. Denne kandidaten er verdt oppmerksomhet men utilstrekkelig til å støtte fremgang til neste fase.

---

## Klinisk forsøksbevis

Det er for tiden ingen relaterte kliniske forsøksregistreringer.

---

## Litteraturbevis

For tiden ingen relatert litteratur funnet.

---

## Informasjon om lokalt marked

Legemidlet er for tiden **ikke godkjent for markedsføring på lokalt marked**, uten effektive godkjenningssertifikater (`total_licenses` = 0).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

> Merk: I `data_gaps` er "DMP package insert warnings/contraindications" merket som **Blocking**-niveau kløft, noe som direkte påvirker sikkerhetsinitialvurderingen (S1) og må fylles med høy prioritet.

---

## Konklusjon og videre trinn

**Beslutning: Hold**

**Begrunnelse:**
- Bevisnivå er L5, kun modellprediksjonspoengsum, uten noen klinisk forsøks- eller litteraturstøtte.
- Modellens egen mekanismegenerering har allerede gjort klart at dette er en kunnskapsgrafs falsk positiv (indirekte lenke generert via GAD65-noden), mangler biologisk rimelighetsjustifikasjon.
- Legemidlet er ikke godkjent på lokalt marked, og både virkningsmåte (MOA) og sikkerhetspakningsvedleggsdata er informasjonshull som må fylles, noe som gjør sikkerhetsinitialvurderingen (S1) umulig.

**Hvis man fortsetter, er følgende nødvendig:**
- Glimepirids formelle MOA-data (DrugBank API-spørring)
- TFDA/lokal tilsynsmyndighets pakningsvedleggets advarsler og kontraindikasjonsdata (løse Blocking-kløften DG001)
- Søk etter all mulig in vitro/dyreforsøks- eller kasuistisk bevis for mekanisme mellom Stiff Person Syndrome-spektret og sulfonylureum-medikamenter
- Hvis prioritering endres, anbefales det å separat evaluere den niende kandidaten «Pancreatic agenesis» fordi den har relativt klar KATP-kanal-mekanismegrunnlag og er verdt uavhengig inspeksjon for å se om det finnes KCNJ11/ABCC8-relaterte kasusforsøks- eller rapportbevis som kan støtte det

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

