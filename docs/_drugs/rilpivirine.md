---
layout: default
title: Rilpivirine
parent: Moderat evidens (L3-L4)
nav_order: 304
evidence_level: L4
indication_count: 5
---

# Rilpivirine
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **5** stk.
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

# Rilpivirine: Fra HIV-1-infeksjon til Felint Ervervet Immunsviktssyndrom

## Sammendrag på én setning

> Rilpivirine er en ikke-nukleosid reversstranskriptasehemmer (NNRTI) som opprinnelig ble utviklet for HIV-1-infeksjon hos mennesker.
> TxGNN-modellens topprangerte prediksjon er **felint ervervet immunsviktssyndrom** — en veterinærsykdom forårsaket av felint immunsviktvirus (FIV), ikke en menneskelig indikasjon —
> og denne støttes for tiden bare av **1 in vitro-strukturell studie** og **ingen kliniske forsøk**.

⚠️ **Merknad om denne kandidaten**: TxGNN-prediksjonen rangert #1 i dette bevisemnet målretter en **veterinærsykdom (katter)**, ikke en menneskelig tilstand. Dette flagges som et sannsynlig lavverdi- eller off-target-modellutput og er scoret `Hold` i selve bevisemnet. Menneskerelevante kandidater med mye sterkere bevis finnes lenger ned på samme prediksjonslist (se Konklusjon).

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | HIV-1-infeksjon (NNRTI; utledet fra litteratur/begrunnelse i bevisemnet — ingen formell norsk pakningsvedlegg tilgjengelig) |
| Predikert ny indikasjon | Felint ervervet immunsviktssyndrom (FIV-infeksjon hos katter) |
| TxGNN-prediksjonspoeng | 99.97% |
| Bevisnivå | L4 |
| Markedsstatus i Norge | ✗ Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelige i dette bevisemnet (`original_moa: [Data Gap]`). Basert på informasjon som finnes i støttende litteratur, er rilpivirine en diarylpyrimidin-klasse NNRTI som binder HIV-1-reversstranskriptasemnet (RT), og blokkerer ikke-kompetitivt viral replikasjon. Dens effektivitet ved HIV-1-infeksjon er veletablert, også i langvarig injiserbar kombinasjonsform med cabotegravir.

Den predikerte nye indikasjonen — felint immunsviktvirus (FIV)-relatert syndrom — er mekanistisk tilstøtende bare i videste forstand: FIV er også et lentivirus med en reversstranskriptaseenzym, så en NNRTI kunne i teorien forstyrre viral replikasjon. Imidlertid er FIV RT og HIV-1 RT strukturelt atskilte, og den eneste tilgjengelige studien er en **biokjemisk/strukturell sammenligning**, ikke en funksjonell antiviral effektivitetsstudie.

Per bevisemnet egen begrunnelse: *"Det finnes kun en enkelt biokjemisk/strukturell sammenligningsstudie som analyserer NNRTI-bindingsegenskaper til felint immunsviktvirus (FIV) RT; FIV RT og HIV-1 RT har betydelige strukturelle ulikheter, og tversarts aktivitet er ikke funksjonelt verifisert — det tilhører veterinærmedisinsk område og er ikke et mål for menneskelig legemiddel-omforbruk."* Kort sagt, tversarts binding ble studert strukturelt men aldri bekreftet funksjonelt, og målarten er ikke menneske — dette er grunnen til at bevisemnet selv tilordner `Evidence Level L4` og `Decision Stage S0 / Hold`.

---

## Bevis fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert.

---

## Bevis fra litteratur

| PMID | År | Type | Tidsskrift | Nøkkelfunn |
|------|-----|------|------------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro-strukturell studie | Journal of Veterinary Science | Sammenlignet biokjemisk/strukturell binding av NNRTI-er (nevirapin, efavirenz, rilpivirine) mot felint kontra menneskelig immunsviktvirus-reversstranskriptase, utforsket teoretisk potensial for NNRTI-er for FIV-behandling hos katter; ingen in vivo- eller kliniske effektivitetsdata rapportert. |

---

## Markedsinformasjon for Norge

Ingen autorisasjonsregistreringer funnet — rilpivirine er for tiden ikke markedsført i Norge (`total_licenses: 0`, `licenses: []`).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjoner er alle markert som datagap i dette bevisemnet; DDI-spørring ga ingen resultater.)

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Topprangerte TxGNN-prediksjon målretter en veterinærtilstand (felint AIDS/FIV) i stedet for en menneskelig sykdom, støttes av bare en preklinisk strukturell sammenligningsartikkel uten funksjonell eller klinisk validering, og er allerede selvscorét `L4 / Hold` i bevisemnet. Denne kandidaten oppfyller ikke terskelen for evaluering av menneskelig legemiddel-omforbruk.

**For å fortsette, følgende er nødvendig:**
- Hvis denne kandidaten forfølges spesifikt: funksjonell antiviral effektivitetsdata for rilpivirine mot levende FIV (in vitro eller in vivo), og bekrefting av relevansen av den veterinære reguleringsvei (sannsynligvis utenfor omfang for et menneskelig omforbruksprogram).
- **Anbefalt alternativ**: omdefiner denne evalueringen til rang 4 (`AIDS-relatert kompleks`, L2, Fortsett med sikringer) eller rang 5 (`medfødt HIV` — gjenspeiler faktisk CAB/RPV LA-bruk hos gravide kvinner med HIV, L2, Forskningsspørsmål), som begge har flere fase 3-forsøk og er innenfor rilpivirines faktiske menneskelige sykdomsområde.
- Løs blokkerende datagap: **DG001** (TFDA/norsk pakningsvedlegg advarsler og kontraindikasjoner — Blokkering, påkrevd før noen S1-sikkerhetsvurdering) og **DG002** (formell MOA fra DrugBank — Høy prioritet).
- Verifiser på nytt manuelt TxGNN-sykdoms-etikettkartlegging for rang 5 ("medfødt menneskelig immunsviktsvirus"), da det underliggende forsøks-/litteraturbevis faktisk gjelder mor-foster farmakokinetikk i stedet for en distinkt medfødt-HIV-indikasjon.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

