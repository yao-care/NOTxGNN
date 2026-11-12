---
layout: default
title: Bupivacaine
parent: Kun modellprediksjon (L5)
nav_order: 70
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-12
description: "Bupivacaine: predikert ny indikasjon Akrodermatitis chronica atrophicans (evidensnivå L5). Opprinnelig indikasjon: Akutt smerte"
monitor_inn: "BUPIVACAINE"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
---

# Bupivacaine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Bupivakain: Fra akutt smerte til akrodermatitis chronica atrophicans
{: .text-alpha }

## Oppsummering i én setning

Bupivakain er et lokalbedøvende middel av amid-typen, opprinnelig godkjent for behandling av akutt smerte (liposomal formulering, Exparel).
TxGNN-modellen forutsier at det kan ha effekt ved **akrodermatitis chronica atrophicans**, men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen.
Prediksjonen er derfor kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Akutt smerte |
| Predikert ny indikasjon | Akrodermatitis chronica atrophicans |
| TxGNN-prediksjonsscore | 0.9923 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (trukket tilbake) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme var ikke tilgjengelige i datagrunnlaget for denne rapporten. Bupivakain er allment kjent som et lokalbedøvende middel som blokkerer spenningsstyrte natriumkanaler og dermed hemmer nerveledning. Denne opplysningen kommer fra generell kunnskap og ikke fra de innsamlede dataene.

Akrodermatitis chronica atrophicans er en sen hudmanifestasjon av Borrelia-infeksjon, og behandlingen er antibiotika. Det er ikke påvist noen plausibel mekanistisk kobling mellom natriumkanalblokade og sykdommens forløp. Den høye scoren (0.9923) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. En eventuell nytte ville begrenset seg til symptomlindring av nevropatisk smerte, og dette er ikke underbygget av data.

For de øvrige predikerte indikasjonene (neonatal dermatomyositt, sekundær interstitiell lungesykdom hos barn assosiert med bindevevssykdom og amyopatisk dermatomyositt) er bildet tilsvarende: alle har evidensnivå L5, ingen studier eller publikasjoner, og ingen støttet mekanistisk kobling. Bupivakains kjente myotoksisitet er en teoretisk bekymring ved myositt-sykdommer, og kardiotoksisitet er en bekymring hos nyfødte.

---

## Klinisk studieevidens

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes ingen relatert litteratur.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004586 | Exparel liposomal | Ikke oppgitt | Akutt smerte |

Produsenten er Pacira Ireland Limited.

<!-- review:begin no-lic-20261106-bupivacaine-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Tillatelsen er trukket tilbake (status: cancelled), og produsenten er Pacira Ireland Limited.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-bupivacaine-1 -->

---

## Sikkerhetsmessige hensyn

**Kontraindikasjoner fra kunnskapsgrafen** (basert på kunnskapsgrafen PrimeKG, ikke på preparatomtale), registrert for blant annet:
- Hjerte- og karsykdommer: hypertensjon, hypotensjon, atrieflimmer, koronarsykdom, hjerteinfarkt, koronar trombose, plutselig hjertestans, hjerteledningssykdom
- Lever- og nyresykdommer: leversvikt, leversykdom, nyresykdom, sykdom i galleblæren
- Lunge- og luftveissykdommer: kols, respirasjonssvikt
- Endokrine og metabolske sykdommer: diabetes mellitus, diabetisk ketoacidose, hypotyreose (inkl. myxødem og medfødt hypotyreose), kaliummangel
- Øvrige: epilepsi, inflammatorisk tarmsykdom, godartet prostatahyperplasi, vinkellukket glaukom, hemoglobinopati, rusmiddelmisbruk/avhengighet, pyoureter

Disse kobler er grafbaserte og må verifiseres mot preparatomtale før de brukes klinisk.

**Legemiddelinteraksjoner:** Totalt 56 interaksjoner er registrert. De viktigste med nivå «moderat» er:
- Aprepitant
- Morfin (liposomal)

Øvrige registrerte interaksjoner har ukjent alvorlighetsgrad, blant annet pantoprazol, omeprazol, lansoprazol, vankomycin, atropin, triamcinolon, prednison, simvastatin, hydrokortison, kaliumklorid, prednisolon, ranitidin, ondansetron, metronidazol, famotidin, naloksom, metoklopramid og deksametason.

Opplysninger om advarsler og kontraindikasjoner fra preparatomtalen mangler. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5), uten kliniske studier eller publikasjoner, og uten en plausibel mekanistisk kobling mellom natriumkanalblokade og akrodermatitis chronica atrophicans, som behandles med antibiotika. Sikkerhetsdata fra preparatomtalen mangler.

<!-- review:begin no-lic-20261106-bupivacaine-2 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Den eneste norske tillatelsen er trukket tilbake, og sikkerhetsdata fra preparatomtalen mangler.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Antall godkjenninger i dataene: 1, hvorav gyldige: 1; oppdaterte tall står i hurtigoversikten og i markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-bupivacaine-2 -->

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel)
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Systematisk litteratursøk og søk etter pågående studier for den predikerte indikasjonen
- Vurdering av administrasjonsvei og formulering som er forenlig med den nye indikasjonen
- Sikkerhetsvurdering for sårbare grupper (barn og nyfødte, hjerte-, lever- og nyresykdom), spesielt med tanke på kardiotoksisitet og myotoksisitet

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «Tillatelsen er trukket tilbake (status: cancelled), og p» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-06 | Fjernet: «Den eneste norske tillatelsen er trukket tilbake, og s» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

