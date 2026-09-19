---
layout: default
title: Eflornithine
parent: Kun modellprediksjon (L5)
nav_order: 121
evidence_level: L5
indication_count: 2
---

# Eflornithine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Eflornithine: Fra afrikanisk trypanosomiasis/hirsutisme til esotropi (prediksjon med lav selvtillit)

## Oppsummering i én setning

Eflornithine er en irreversibel ornithin dekarboxylase (ODC)-hemmer kjent klinisk for behandling av afrikanisk trypanosomiasis og, topisk, ansiktshirsutisme. TxGNN forutsier en mulig ny indikasjon for **esotropi**, men dette støttes av **0 kliniske forsøk** og **0 publikasjoner**, og modellens egen begrunnelse flagger ingen plausibel farmakologisk sammenheng — dette er et modellbasert signal, ikke evidensbasert.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | Ikke registrert i dette datasettet (ingen taiwansk lisens/formell indikasjonstekst tilgjengelig); kjente kliniske bruksområder per tilgjengelig bevis: afrikanisk trypanosomiasis, topisk behandling av ansiktshirsutisme |
| Forutsagt ny indikasjon | Esotropi |
| TxGNN prediksjonspoeng | 99.85% |
| Bevisnivå | L5 |
| Taiwansk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) er ikke tilgjengelig i det formelle `original_moa`-feltet for denne kandidaten (flagget som **blokkering** datakløft, DG001/DG002). Basert på det tilleggsbevis som er vedlagt denne prediksjonen, forstås eflornithine å irreversibelt hemme ornithin dekarboxylase (ODC) og blokkere polyaminsyntese — en mekanisme som ligger til grunn for dens etablerte bruk mot afrikanisk trypanosomiasis (antiparasittisk) og topisk undertrykkelse av økt ansiktshårvekst (antiproliferativ effekt på hårfollikler).

Esotropi er en lidelse av ekstrakular muskeltonus/neuromuskulær kontroll, ikke en proliferativ, parasittisk eller polyaminavhengig tilstand. Modellens egen begrunnelse for omdisponering sier eksplisitt at det **ikke finnes noen kjent fysiologisk eller farmakologisk mekanisme** som forbinder ODC-hemmelse/polyaminblokkade til esotropi, og vurderer denne prediksjonen som mest sannsynlig et artefakt («støy») av TxGNN embedding-rom snarere enn et biologisk begrunnet signal.

En sekundær kandidat, neurotrof keratopati (rangering 2, poengsum 99.38%), ble også evaluert men viser en lignende ustøttet — og potensielt mekanistisk **ugunstig** — sammenheng: ODC-hemmelse ville forventes å *redusere* polyamin-drevet korneal epitelial regenerasjon i stedet for å forbedre den. Ingen av kandidatene har noe bekreftende forsøks- eller litteraturbevis.

## Bevis fra kliniske forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert.

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig.

## Taiwansk markedsinformasjon

Eflornithine er ikke for tiden markedsført i Taiwan; ingen lisensposter er tilgjengelig (`total_licenses = 0`).

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjon er ikke tilgjengelig i dette bevismateriell — løsing av dette er et **blokkering** gap, DG001, nødvendig før noen S1 sikkerhetsevaluering kan fortsette.)

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Prediksjonen hviler utelukkende på en TxGNN-modellpoengsum (L5) uten kliniske forsøk, uten litteratur, og uten plausibel mekanistisk vei identifisert av modellens egen begrunnelse — faktisk peker mekanismen plausibelt i motsatt retning for den sekundære kandidaten. Kombinert med et **blokkering** gap på TFDA/etikett sikkerhetsdataene (DG001) og en manglende formell MOA (DG002), kan denne kandidaten ikke avansere forbi S0.

**For å fortsette, er følgende nødvendig:**
- Bekreftet originalmekanisme (MOA) og godkjent indikasjon(er) fra DrugBank/regulatorisk kilde (løs DG002)
- TFDA (eller tilsvarende) etikett advarsler/kontraindikasjoner (løs DG001, **blokkering** — nødvendig før noen S1 sikkerhetsevaluering)
- Uavhengig farmakologisk plausibilitetsevaluering for esotropi gitt fravær av en mekanistisk begrunnelse
- Løpende litteratur-/forsøksovervåking i tilfelle nye bevis dukker opp, gitt nåværende mangel på noen støttestudie

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

