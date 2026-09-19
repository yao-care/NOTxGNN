---
layout: default
title: Eculizumab
parent: Kun modellprediksjon (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: Fra ikke oppgitt originalindikasjon til syklisk hematopoese

## Oppsummering i én setning

> Evidenspakken for eculizumab inneholder ikke originalindikasjon eller virkningsmekanisme (MOA)-data (flagget som et **blokkert datamangel**).
> TxGNN-modellen forutsier at eculizumab kan være effektivt for **syklisk hematopoese**, men denne forutsielsen støttes av **0 kliniske forsøk** og **0 publikasjoner**, og den medfølgende mekanistiske begrunnelsen sier eksplisitt at det **ikke er noen kjent biologisk forbindelse** mellom eculizumabs komplementinhiberende mekanisme og denne sykdommen.

---

## Rask oversikt

| Emne | Innhold |
|------|---------|
| Originalindikasjon | Ikke oppgitt i evidenspakke (datamangel) |
| Forutsatt ny indikasjon | Syklisk hematopoese |
| TxGNN-forutsigelsesscore | 99.97% |
| Bevisnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne forutsielsen rimelig?

Detaljerte virkningsmekanisme-data for eculizumab er ikke tilgjengelige i denne evidenspakken (merket som et alvorlig datamangel). Basert på legemidlets kjente målklasse er eculizumab et anti-C5 monoklonalt antistoff som blokkerer terminal komplementaktivering (MAC/C5a-dannelse).

Ombruksforklaringen som følger med denne forutsielsen er imidlertid eksplisitt **negativ**: syklisk hematopoese er forårsaket av *ELANE*-genmutatsjoner som påvirker nøytrofilelastase og granulosyttprodukasjonsregulering — en bane som er urelatert til komplementaktivering. Forklaringen sier at det ikke er noen kjent forbindelse mellom eculizumabs mekanisme og denne sykdommens patofysiologi, og karakteriserer forutsielsen som oppstått rent fra likhetsmønstre i nettverket snarere enn fra noen mekanistisk hypotese.

Dette er et viktig forbehold: en høy TxGNN-score alene indikerer ikke biologisk plausibilitet. I dette tilfelle er modellscoren (rangering 597, score 0.9997) ikke bekreftet av mekanisme, kliniske forsøk eller litteratur, som er konsistent med klassifiseringen som **L5 – kun modellforutsigelse**.

---

## Bevis fra kliniske forsøk

Ingen relaterte kliniske forsøk er for øyeblikket registrert.

---

## Bevis fra litteratur

Ingen relatert litteratur er for øyeblikket tilgjengelig.

*Merk: Blant de øvrige 9 lavere-rangerte kandidatindikasjonene i denne evidenspakken returnerte to (rangering 4 – medfødt nøytropeni-myelofibrose-nefromegali-syndrom; rangering 10 – primær frigjøringsforstyrrelse av blodplater) litteraturtreff, men disse ble gjennomgått og bedømt som søkestøy — de hentede artiklene diskuterer eculizumabs allerede etablert bruk ved PNH, aHUS og myasteniske syndromer, ikke de forutsatte indikasjonene selv. Ingen utgjør direkte eller indirekte bevis for den topprangerte forutsielsen (syklisk hematopoese).*

---

## Norsk markedsinformasjon

Eculizumab er ikke for øyeblikket markedsført og har ingen registrerte autorisasjoner (0 lisenser registrert).

---

## Sikkerhetshensyn

Se pakningslisten for sikkerhetsinformasjon.

*Merk: TFDA/etikettadvarsler, kontraindikasjoner og DDI-data kunne ikke hentes og er flagget i kildeevidenspakken som et **blokkert** datamangel — dette hindrer spesifikt kandidaten fra å gå videre til S1-stadiet for foreløpig sikkerhetsvurdering.*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den topprangerte forutsatte indikasjonen (syklisk hematopoese) har ingen støttende kliniske forsøk eller litteratur, og den gitte mekanistiske forklaringen sier eksplisitt at det ikke er noen biologisk forbindelse mellom eculizumabs komplementinhiberende mekanisme og denne sykdommen — TxGNN-scoren reflekterer kun nettverkslikhet. Kombinert med et blokkert datamangel i TFDA sikkerhet/etikett-data, kan denne kandidaten ikke for øyeblikket gå videre fra S0.

**For å gå videre, er følgende nødvendig:**
- TFDA pakningsliste (advarsler, kontraindikasjoner) — blokkert datamangel, påkrevd for å gå inn i S1-sikkerhetsvurderingen
- Virkningsmekanisme (MOA)-data via DrugBank API — påkrevd for mekanistisk plausibilitetsvurdering
- Originalindikasjon/regulatorisk historie for eculizumab, som for øyeblikket mangler fra denne evidenspakken
- Uavhengig mekanistisk eller preklinisk bevis som spesifikt knytter komplementinhibisjon (C5) til syklisk hematopoese, dersom denne kandidaten skal vurderes på nytt
- Ny screening av de gjenstående 9 lavere-rangerte kandidatene i denne pakken, som alle også har L5/Avvent-status uten direkte støttende bevis

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

