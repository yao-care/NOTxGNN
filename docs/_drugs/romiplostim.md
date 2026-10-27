---
layout: default
title: Romiplostim
parent: Kun modellprediksjon (L5)
nav_order: 367
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Romiplostim: predikert ny indikasjon Primær frigjøringsforstyrrelse av blodplater (evidensnivå L5). Opprinnelig indikasjon: Idiopatisk trombocytopenisk purpura (ITP)"
monitor_inn: "ROMIPLOSTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "platelet-type bleeding disorder", "autosomal dominant macrothrombocytopenia", "Ehlers-Danlos syndrome, fibronectinemic type"]
---

# Romiplostim
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

## Romiplostim: Fra idiopatisk trombocytopenisk purpura til primær frigjøringsforstyrrelse av blodplater
{: .text-alpha }

## Kort oppsummering

Romiplostim er en trombopoietinreseptor-agonist (TPO-reseptor-agonist) som opprinnelig brukes til behandling av idiopatisk trombocytopenisk purpura (ITP).
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **primær frigjøringsforstyrrelse av blodplater**, men det finnes **0 kliniske studier** og bare **1 publikasjon** (en mekanistisk studie om ITP, ikke direkte om den predikerte sykdommen). Prediksjonen er dermed kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Idiopatisk trombocytopenisk purpura (ITP) |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse av blodplater |
| TxGNN-prediksjonsscore | 99,99 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun opphevede (kansellerte) godkjenninger |
| Antall godkjenninger | 1 (opphevet) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Romiplostim binder seg til TPO-reseptoren (MPL) og øker produksjonen av blodplater. Data om detaljert virkningsmekanisme er foreløpig ikke tilgjengelig i de innsamlede dataene, men målet (MPL) er bekreftet i farmakologidata.

Den predikerte sykdommen er en funksjonsforstyrrelse av blodplatene, ikke en mangel på antall. Å øke antallet blodplater korrigerer vanligvis ikke funksjonsdefekter, og nydannede blodplater vil bære den samme defekten. Den eneste funnede publikasjonen (PMID 25682608) gjelder autoantistoffers hemming av blodplatedannelse ved ITP, som er den allerede godkjente indikasjonen. Den mekanistiske begrunnelsen er derfor svak, og den svært høye TxGNN-scoren må tolkes som en ren prediksjon.

---

## Klinisk studiedokumentasjon

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Grunnforskning/mekanistisk | Haematologica | Antiblodplate-autoantistoffer ved ITP hemmer proplatelet-dannelse i megakaryocytter og svekker blodplateproduksjon in vitro. Gjelder ITP, ikke frigjøringsforstyrrelser. |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000942 | Nplate (Amgen Europe B.V.) | Ikke oppgitt | Idiopatisk trombocytopenisk purpura (status: opphevet) |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Carfilzomib er registrert med interaksjonsnivå **alvorlig (Major)** (kilde: DDInter).

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen.

---

## Andre predikerte indikasjoner (kort oversikt)

| Rang | Sykdom | TxGNN-score | Evidensnivå | Vurdering |
|---|---|---|---|---|
| 2 | Pseudo-von Willebrands sykdom | 99,99 % | L5 | Hold: nydannede blodplater har samme GPIbα-defekt |
| 3 | Glanzmanns trombasteni | 99,99 % | L5 | Hold: funksjonsdefekt, normalt antall blodplater |
| 4 | Føtal og neonatal alloimmun trombocytopeni | 99,99 % | L4 | Forskningsspørsmål: kun indirekte evidens (ITP hos barn, graviditet, kasuistikker) |
| 5 | Scott syndrom | 99,97 % | L5 | Hold: scramblase-defekt |
| 6 | Blødningsforstyrrelse ved konstitusjonell trombocytopeni | 99,95 % | L5 | Hold: heterogen gruppe, ingen evidens |
| 7 | Blødningsdiatese ved kollagenreseptordefekt | 99,95 % | L5 | Hold |
| 8 | Blodplatetype blødningsforstyrrelse | 99,93 % | L5 | Hold |
| 9 | Autosomal dominant makrotrombocytopeni | 99,88 % | L5 | Hold: usikker nytte ved defekter nedstrøms for TPO-signalering |
| 10 | Ehlers-Danlos syndrom, fibronektinemisk type | 99,85 % | L5 | Hold: ingen klar trombopoietisk mekanisme |

Den mest interessante kandidaten blant disse er føtal og neonatal alloimmun trombocytopeni (rang 4), hvor en trombopoietisk mekanisme er plausibel. Evidensen er likevel kun indirekte, og sikkerhet for foster og nyfødt (blant annet placentaovergang) er uavklart.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den predikerte indikasjonen mangler kliniske studier og direkte litteratur, og mekanismen er svak siden sykdommen gjelder blodplatefunksjon og ikke antall. I tillegg er den eneste norske godkjenningen opphevet.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA)
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner)
- Avklaring av hvorfor den norske godkjenningen er opphevet, og av dagens reguleringsstatus
- Systematisk litteraturgjennomgang for den predikerte sykdommen og eventuelt for føtal og neonatal alloimmun trombocytopeni
- Vurdering av klinisk betydning av den alvorlige interaksjonen med carfilzomib
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

