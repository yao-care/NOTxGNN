---
layout: default
title: Lomitapide
parent: Kun modellprediksjon (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Lomitapide
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

# Lomitapid: Fra homozygot familiekolesterolemi til makrotrombocytopeni med mitralinsuffisiens

## Sammenfattelse på én setning

> Lomitapid er en mikrosomal trigliseridtransferprotein-hemmer (MTP-hemmer) som allerede er godkjent i utlandet for **homozygot familiekolesterolemi (HoFH)** — selv om denne opprinnelige indikasjonen mangler fra den strukturerte legemiddeloppføringen og bare dukker opp indirekte i litteraturen i bevissamlingen.
> TxGNN-modellens høyest rangerte nye prediksjonsresultat er **makrotrombocytopeni med mitralinsuffisiens**, en sjelden nedarvet blodplattlidelse.
> Denne prediksjonen støttes av **null kliniske forsøk og null publikasjoner** — det er en ren modellscore uten mekanistisk begrunnelse.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke tilstede i strukturerte data (`original_indications` er tom). Homozygot familiekolesterolemi (HoFH) kan utledes fra litteraturen/forsøksbeviser knyttet til en *annen* rangert oppføring (se merknad nedenfor), men er ikke bekreftet i legemiddeloppføringen. |
| Forutsagt ny indikasjon | Makrotrombocytopeni med mitralinsuffisiens |
| TxGNN-prediksjonscore | 99.92% |
| Bevisnivå | L5 (modellprediksjon kun, ingen støttende studier) |
| Taiwans markedsstatus | Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | **Hold** |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er offisielt flagget som datakløft (DG002) i denne bevissamlingen. Basert på informasjon som dukker opp andre steder i bevissamlingen, er lomitapid kjent for å virke som en **MTP-hemmer** som blokkerer hepatisk og intestinal apoB-lipoproteinsyntese for å senke LDL-C/VLDL — grunnlaget for dets etablerte bruk ved alvorlig hyperkolesterolemi.

For den høyest rangerte forutsagte indikasjonen, makrotrombocytopeni med mitralinsuffisiens, er bevissamlingens eget begrunnelse eksplisitt: *"en ekstremt sjelden nedarvet lidelse uten kjent patologisk forbindelse til MTP-hemming. Dette er rent en graf nevralt nettverk-prediksjonscore, uten støtte fra mekanisme, forsøk eller litteratur."* Det finnes ingen plausibel farmakologisk forbindelse mellom apoB/lipoproteinsyntesehemming og nedarvet blodplatt-/klappepatologi. Den høye TxGNN-scoren gjenspeiler sannsynligvis en indirekte grafassosasjon (f.eks. delte lipidstoffskifte-noder) snarere enn et genuint biologisk signal.

---

## Bevis fra kliniske forsøk

For tiden er ingen relaterte kliniske forsøk registrert.

---

## Bevis fra litteratur

For tiden er ingen relatert litteratur tilgjengelig.

---

## Taiwans markedsinformasjon

Lomitapid er **for tiden ikke markedsført i Taiwan** (0 godkjennelser, 0 lisenser på register). Ingen produkt-/doserings-/indikasjonsdata er tilgjengelig for tabulering.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsopplysninger. (TFDA-merking advarsler/kontraindikasjoner er flagget som en **blokkering** datakløft — DG001 — og må innhentes før S1 sikkerhetsverifisering kan iverksettes.)

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Den høyest rangerte forutsagte indikasjonen (makrotrombocytopeni med mitralinsuffisiens) har ingen kliniske forsøk, ingen litteratur og ingen plausibel mekanistisk forbindelse — bevisnivå L5, beslutningsstadium S0. Det er intet grunnlag for å fremme denne kandidaten.

**For å gå videre er følgende nødvendig:**
- TFDA-merking (advarsler/kontraindikasjoner) — for tiden en blokkering datakløft (DG001)
- Bekreftet virkningsmekanisme og opprinnelige godkjente indikasjoner for lomitapid — for tiden mangler fra legemiddeloppføringen (DG002)
- Ny vurdering av rangering 2–8 og 10 i det samme prediksjonssettet, som alle på samme måte er L5/Hold uten støttende bevis

**⚠️ Datakvalitetsmerknad (viktig for oppstrøms korreksjon):** Rangering 9 i dette samme prediksjonspartiet, *hyperlipoproteinemi*, bærer sterkt bevis (12 kliniske forsøk inkludert flere fullførte fase-3-studier, 19 publikasjoner) og er den eneste L1/S3-oppføring i settet. Imidlertid flagger dens egen begrunnelse at dette meget sannsynlig **ikke er et nytt omdisponerings-signal** — det tilsvarer lomitapids allerede godkjente indikasjon (HoFH, markedsført som Juxtapid/Lojuxta, FDA-godkjent 2012), feilkategorisert som "ny" kun fordi `original_indications`-feltet er tomt. Dette bør korrigeres på datakilde før kandidaten blir evaluert på nytt, for å unngå å blande "bekreftet opprinnelig indikasjon" med "omdisponerings-oppdagelse" i fremtidige rapporter.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

