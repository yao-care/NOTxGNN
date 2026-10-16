---
layout: default
title: Lusutrombopag
parent: Kun modellprediksjon (L5)
nav_order: 256
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Lusutrombopag: predikert ny indikasjon Arvelig trombocytopeni med normale blodplater (evidensnivå L5). Opprinnelig indikasjon: Trombocytopeni"
monitor_inn: "LUSUTROMBOPAG"
predicted_indications: ["hereditary thrombocytopenia with normal platelets", "marcothrombocytopenia with mitral valve insufficiency", "transient neonatal thrombocytopenia", "dense granule disease", "platelet storage pool deficiency", "amyotrophic lateral sclerosis", "lower motor neuron syndrome with late-adult onset", "amyotrophic lateral sclerosis, susceptibility to", "bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia"]
---

# Lusutrombopag
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

# Lusutrombopag: Fra trombocytopeni til arvelig trombocytopeni med normale blodplater

## Oppsummering

Lusutrombopag er en trombopoietinreseptoragonist (TPO-R-agonist) som opprinnelig er godkjent for behandling av **trombocytopeni**. Modellen TxGNN predikerer at legemidlet kan ha effekt ved **arvelig trombocytopeni med normale blodplater**, men dette er kun en modellprediksjon. Det foreligger **ingen kliniske studier** og **ingen publikasjoner** i dataene som er samlet inn for denne rapporten.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Trombocytopeni |
| Predikert ny indikasjon | Arvelig trombocytopeni med normale blodplater |
| TxGNN-prediksjonsskår | 99,995 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (ingen gyldig markedsføringstillatelse) |
| Antall godkjenninger | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Basert på kjent informasjon er lusutrombopag en TPO-R-agonist. Effekten ved trombocytopeni hos pasienter med kronisk leversykdom som skal gjennomgå et inngrep er dokumentert, og mekanistisk kan den tenkes å være relevant for tilstander med redusert blodplateproduksjon.

Koblingen til den predikerte indikasjonen er imidlertid svak. Tilstanden er definert ved normalt blodplatetall eller normal blodplatefunksjon, slik at det er lite å vinne på å øke blodplateproduksjonen. Den høye TxGNN-skåren (0,99995) er en ren modellprediksjon uten støtte fra studier eller litteratur.

### Andre predikerte indikasjoner (alle evidensnivå L5, anbefaling Hold)

| Rang | Sykdom | TxGNN-skår | Vurdering |
|------|------|------|------|
| 2 | Makrotrombocytopeni med mitralklaffinsuffisiens | 99,995 % | TPO-R-agonisme kan i prinsippet øke blodplatetallet, men den strukturelle hjertefeilen påvirkes ikke |
| 3 | Forbigående neonatal trombocytopeni | 99,995 % | Tilstanden er selvbegrensende; mangel på sikkerhets- og doseringsdata hos nyfødte, og risiko for trombose |
| 4 | Tett granula-sykdom (dense granule disease) | 99,995 % | Primært en funksjonsdefekt, ikke et antallsproblem; begrenset nytte forventet |
| 5 | Mangel på blodplatelagringspool | 99,958 % | Kvalitativ blodplatelidelse; funksjonen forventes ikke gjenopprettet |
| 6 | Amyotrofisk lateralsklerose | 99,948 % | Ingen tydelig mekanistisk kobling; sannsynligvis artefakt i kunnskapsgrafen |
| 7 | Nedre motornevronsyndrom med sen voksendebut | 99,948 % | Ingen kjent kobling til trombopoietinsignalering |
| 8 | ALS, mottakelighet for | 99,946 % | Genetisk variant, dupliserer ALS-signalet |
| 9 | Bilateral parasagittal parieto-oksipital polymikrogyri | 99,945 % | Medfødt misdannelse som ikke kan reverseres med legemiddel |
| 10 | Aksial spondylometafysær dysplasi | 99,943 % | Ingen mekanisme som kobler TPO-R-agonisme til sykdommen |

---

## Kliniske studier

Foreløpig finnes ingen relevante kliniske studier registrert.

---

## Litteraturevidens

Foreløpig finnes ingen relevant litteratur.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004720 | Mulpleo (tidligere Lusutrombopag Shionogi) | Ikke oppgitt | Trombocytopeni (status: avregistrert) |

---

## Sikkerhetsvurderinger

### Legemiddelinteraksjoner

Interaksjonssøket er fullført og fant totalt 100 interaksjoner. Eksemplene nedenfor er alle klassifisert som **moderate** (kilde: DDInter):

- Hydrokortison
- Klaritromycin
- Eliglustat
- Fidaksomicin
- Rolapitant
- Simvastatin
- Tolbutamid
- Kobicistat
- Abirateron
- Lidokain
- Nifedipin
- Afatinib
- Alpelisib
- Amiodaron
- Testosteron
- Apremilast
- Atazanavir
- Azitromycin
- Ingefær
- Kabozantinib

Øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner) finnes i preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle predikerte indikasjoner har kun modellstøtte (evidensnivå L5), uten kliniske studier eller publikasjoner. Den mekanistiske koblingen er svak for den fremste prediksjonen, og flere av de øvrige kandidatene (for eksempel ALS og medfødte misdannelser) mangler biologisk begrunnelse. I tillegg har legemidlet ingen gyldig markedsføringstillatelse i Norge.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen, som nå mangler og blokkerer sikkerhetsscreening
- Prekliniske data eller litteratur som støtter bruk ved arvelige trombocytopenier med redusert blodplateproduksjon
- Sikkerhets- og doseringsdata for spesielle populasjoner, spesielt nyfødte, og vurdering av trombose­risiko
- Avklaring av regulatorisk status og eventuell ny markedsføringstillatelse i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

