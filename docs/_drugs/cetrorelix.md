---
layout: default
title: Cetrorelix
parent: Kun modellprediksjon (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Cetrorelix: predikert ny indikasjon Hypertrikose (evidensnivå L5). Opprinnelig indikasjon: Ovulasjon"
monitor_inn: "CETRORELIX"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
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

# Cetrorelix: Fra ovulasjonsinduksjon til hypertrikose

## Oppsummering

Cetrorelix er en GnRH-reseptorantagonist som opprinnelig brukes til å hemme for tidlige LH-topper hos kvinner under kontrollert ovariestimulering ved fertilitetsbehandling (ovulasjonsinduksjon).
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **hypertrikose**, men dette er en ren modellprediksjon: det er **ingen kliniske studier** og **ingen publikasjoner** som støtter den.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ovulasjon; ovulasjonsinduksjon |
| Predikert ny indikasjon | Hypertrikose |
| TxGNN-prediksjonsscore | 99,98 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (avregistrert) |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Cetrorelix blokkerer GnRH-reseptoren (GNRHR) i hypofysen og demper dermed utskillelsen av LH og FSH. Det reduserer i sin tur produksjonen av kjønnshormoner, inkludert androgener fra gonadene. Detaljerte data om virkningsmekanisme fra legemiddeldatabasen var ikke tilgjengelige i datamaterialet som er samlet inn til denne rapporten, så beskrivelsen bygger på kjent farmakologi.

Teoretisk kan lavere androgenpådriv hjelpe ved androgenavhengig hirsutisme. Hypertrikose er imidlertid vanligvis androgenuavhengig, så den mekanistiske koblingen er svak. Den høye TxGNN-scoren er et resultat av beregninger i en kunnskapsgraf, ikke av farmakologiske eller kliniske funn.

### Andre predikerte indikasjoner (alle uten kliniske studier eller litteratur)

| Rangering | Sykdom | Score | Biologisk plausibilitet |
|------|------|------|------|
| 2 | Ambras-type hypertrichosis universalis congenita | 99,97 % | Ingen klar mekanisme (genomisk omlegging som påvirker TRPS1) |
| 3 | Misdannelsessyndrom med tann-/periodontal komponent | 99,97 % | Ingen plausibel kobling |
| 4 | Syndrom med Dandy-Walker-malformasjon | 99,96 % | Ingen mekanisme for strukturell hjernemisdannelse |
| 5 | Isolert genetisk hårskaftavvik | 99,96 % | Ingen etablert effekt |
| 6 | Persisterende føtal sirkulasjon | 99,67 % | Ingen relevans; sikkerhetsbekymringer hos nyfødte |
| 7 | Familiær isolert trikomegali | 99,63 % | Spekulativ kobling |
| 8 | Familiær mannsbegrenset tidlig pubertet | 99,55 % | Begrenset; reseptormutasjonen virker nedstrøms for GnRH (forskningsspørsmål) |
| 9 | Aromataseoverskuddssyndrom | 99,53 % | Svak; aromatasehemmere er logisk behandling |
| 10 | Sentral tidlig pubertet | 99,29 % | Mest biologisk plausibel (forskningsspørsmål) |

Av disse er **sentral tidlig pubertet** den mest biologisk sammenhengende kandidaten, siden sykdommen skyldes tidlig aktivering av hypothalamus–hypofyse–gonade-aksen. GnRH-agonister er standardbehandling, og en antagonist som cetrorelix kan i teorien gi rask LH/FSH-suppresjon. Cetrorelix har imidlertid kort virketid, og det finnes ingen pediatriske data i materialet.

---

## Klinisk studiedokumentasjon

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000233 | Cetrotide (Merck Europe B.V.) | – | Ovulasjon; ovulasjonsinduksjon |

Denne godkjenningen har status som trukket tilbake, og det finnes ingen gyldige markedsføringstillatelser.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Det ble funnet én farmakologisk oppføring, som beskriver cetrorelix som en peptidligand som virker på GnRH₁-reseptoren (GNRHR, humant mål). Det er ikke angitt noen interaksjonsnivåer eller konkrete interagerende legemidler.

Se preparatomtalen (pakningsvedlegget) for øvrig sikkerhetsinformasjon, inkludert advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore (evidensnivå L5) uten kliniske studier eller publikasjoner. Den mekanistiske koblingen til hypertrikose er svak, og legemidlets markedsstatus i Norge er «kun trukket tilbake».

**For å gå videre kreves følgende:**
- Informasjon om virkningsmekanisme fra legemiddeldatabasen for å støtte mekanistisk analyse
- Advarsler og kontraindikasjoner fra preparatomtalen (nødvendig før sikkerhetsscreening)
- Litteratur- og studiesøk for hypertrikose, og eventuelt for sentral tidlig pubertet som mer plausibel kandidat
- Vurdering av gjennomførbarhet gitt kort virketid, administrasjonsvei og at markedsføringstillatelsen er trukket tilbake
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

