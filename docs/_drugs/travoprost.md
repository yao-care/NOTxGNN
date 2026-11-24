---
layout: default
title: Travoprost
parent: Kun modellprediksjon (L5)
nav_order: 434
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Travoprost: predikert ny indikasjon visceral kalsifylaksi (evidensnivå L5). Opprinnelig indikasjon: Åpenvinklet glaukom og okulær hypertensjon"
monitor_inn: "TRAVOPROST"
predicted_indications: ["visceral calciphylaxis", "venous thoracic outlet syndrome", "arterial thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "vascular disease", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis", "idiopathic spontaneous coronary artery dissection", "hemangioendothelioma"]
---

# Travoprost
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Travoprost: Fra glaukom til visceral kalsifylaksi
{: .text-alpha }

## Oppsummering i én setning

Travoprost er en prostaglandin F2-alfa-analog som opprinnelig brukes som øyedråper mot åpenvinklet glaukom og okulær hypertensjon. TxGNN-modellen (deep learning) forutsier at legemidlet kan ha effekt mot **visceral kalcifylaksi**, men dette er kun en prediksjon fra modellen. Det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Åpenvinklet glaukom og okulær hypertensjon |
| Foreslått ny indikasjon | Visceral kalcifylaksi |
| TxGNN-prediksjonsscore | 1.0000 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 3 av 3) |
| Antall godkjenninger | 3 (gyldige: 3) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Travoprost (uoffisiell oversettelse): «Travoprost fri syre, en prostaglandinanalog, er en selektiv agonist ved FP-prostanoidreseptoren, som antas å redusere IOP ved å øke det uveosklerale utløpet. Den nøyaktige virkningsmekanismen er foreløpig ukjent.» Engelsk originaltekst: "Travoprost free acid, a prostaglandin analog is a selective FP prostanoid receptor agonist, which is believed to reduce IOP by increasing uveoscleral outflow. The exact mechanism of action is unknown at this time." ([DailyMed: Travoprost Ophthalmic Soluton (travoprost) prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=498a376e-a74e-48d8-a022-ad15a1ecadb5), versjon av 2026-09-28; hentet 2026-11-19). Travoprost er kjent som en prostaglandin F2-alfa-analog (FP-reseptoragonist) med lokal karutvidende effekt. Ved glaukom senker den øyetrykket, først og fremst ved å øke uveoskleral avrenning.

Det er vanskelig å finne en rimelig mekanistisk kobling til visceral kalcifylaksi. Sykdommen kjennetegnes av karforkalkning og trombose, og det er ikke påvist noen sammenheng mellom FP-reseptoragonisme og disse prosessene. Dessuten gir lokal dosering i øyet minimal systemisk eksponering, noe som gjør en systemisk effekt på visceral sykdom lite sannsynlig.

Prediksjonen bør derfor betraktes som en hypotese fra TxGNN-modellen (deep learning), og scoren kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Det samme gjelder de øvrige toppredikerte indikasjonene (trange passasjer i thoraxapertur, blåtåsyndrom, spontan koronararteriedisseksjon m.fl.), som heller ikke har studier eller publikasjoner.

---

## Klinisk studieevidens

For den foreslåtte indikasjonen (visceral kalcifylaksi) er det for øyeblikket ingen relaterte kliniske studier registrert.

Til sammenligning ble det for den bredere prediksjonen «karsykdom» funnet 10 studier. Alle gjelder travoprost ved glaukom eller bivirkninger i øyet, ikke behandling av karsykdom. Den eneste mekanistisk relevante er en liten fysiologisk studie:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00308945](https://clinicaltrials.gov/study/NCT00308945) | Fase 4 | Fullført | 20 | Sammenligning av travoprost og latanoprost på retinal kardiameter og blodstrøm i årehinnen hos glaukompasienter. Fysiologisk måling, ikke behandling av karsykdom. |

---

## Litteraturevidens

For visceral kalcifylaksi finnes for øyeblikket ingen relatert litteratur.

---

## Informasjon om markedet i Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000390 | Travatan | travoprost | Glaucoma, Open-Angle; Ocular Hypertension | Gyldig |
| EMEA/H/C/000665 | DuoTrav | travoprost; timolol | Glaucoma, Open-Angle; Ocular Hypertension | Gyldig |
| EMEA/H/C/002738 | Izba | travoprost | Ocular Hypertension; Glaucoma, Open-Angle | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Alle tre godkjenningene (innehaver: Novartis Europharm Limited) er gyldige, og legemidlet er markedsført i Norge (3 gyldige godkjenninger av 3).

---

## Sikkerhetsvurderinger

- **Sykdommer med kontraindikasjonssignal i kunnskapsgrafen** (ikke hentet fra preparatomtale): uveitt, irissykdom, sykdom i ciliærlegemet, panuveitt, iritt, cystoid makulaødem og makulært retinalt ødem.
- **Legemiddelinteraksjoner**: 49 mulige interaksjoner er identifisert, men alle har ukjent alvorlighetsgrad. Eksempler: kalsitriol, pantoprazol, sukralfat, morfin, metformin, omeprazol, prednisolon og acetylsalisylsyre.
- **Sikkerhetssignal ved relaterte tilstander**: En kasuistikk (PMID 19107053) beskriver uvealeffusjon med eksudativ netthinneløsning utløst av topikal travoprost hos en pasient med Sturge-Weber-Krabbe-syndrom, altså en tilstand med vaskulær malformasjon. Dette taler mot bruk ved vaskulære lidelser.

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen kommer kun fra TxGNN-modellen (deep learning) (evidensnivå L5), og scoren kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Det finnes ingen studier eller publikasjoner, ingen plausibel mekanisme, og topikal øyedosering gir minimal systemisk eksponering. Legemidlet er markedsført i Norge med 3 gyldige godkjenninger av 3.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og en vurdering av om FP-reseptoragonisme kan ha relevans for kalcifylaksens patofysiologi
- Prekliniske studier som undersøker effekt på karforkalkning
- Vurdering av administrasjonsvei og systemisk eksponering (øyedråper er neppe egnet)
- Preparatomtale med advarsler og kontraindikasjoner for en fullstendig sikkerhetsvurdering
- Avklaring av det regulatoriske grunnlaget

<!-- review:begin no-lic-20261106-travoprost-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Avklaring av det regulatoriske grunnlaget, siden de norske godkjenningene er avregistrert» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-travoprost-1 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «siden de norske godkjenningene er avregistrert» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Travoprost Ophthalmic Soluton (travoprost) prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=498a376e-a74e-48d8-a022-ad15a1ecadb5) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

