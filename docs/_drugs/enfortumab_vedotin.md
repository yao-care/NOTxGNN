---
layout: default
title: Enfortumab Vedotin
parent: Kun modellprediksjon (L5)
nav_order: 150
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Enfortumab Vedotin: predikert ny indikasjon Lepra (evidensnivå L5). Opprinnelig indikasjon: Urotelialt karsinom (overgangscellekarsinom)"
monitor_inn: "ENFORTUMAB VEDOTIN"
predicted_indications: ["leprosy", "multiple endocrine neoplasia", "cytomegalovirus infection", "candidiasis", "cerebral infarction", "HIV infectious disease", "homozygous familial hypercholesterolemia", "infectious bovine rhinotracheitis", "malignant catarrh"]
---

# Enfortumab Vedotin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

## Enfortumab vedotin: Fra urotelialt karsinom til lepra
{: .text-alpha }

## Oppsummering i én setning

Enfortumab vedotin er et antistoff-legemiddelkonjugat (ADC) som er rettet mot Nectin-4 og bærer nyttelasten MMAE. Det brukes opprinnelig mot urotelialt (overgangscelle-) karsinom og urologiske svulster.
TxGNN-modellen predikerer at legemidlet kan ha effekt mot **lepra**, men det finnes **0 kliniske studier** og **0 publikasjoner** som støtter denne retningen.
Prediksjonen er derfor kun modellbasert og har ingen støtte i faktiske studier.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Urotelialt karsinom (overgangscellekarsinom); urologiske svulster |
| Predikert ny indikasjon | Lepra |
| TxGNN-prediksjonsscore | 0,9953 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Enfortumab Vedotin (uoffisiell oversettelse): «Enfortumab vedotin-ejfv er et ADC. Antistoffet er et humant IgG1 kappa rettet mot Nectin-4, et adhesjonsprotein som finnes på celleoverflaten. Småmolekylet, MMAE, er et mikrotubuliforstyrrende middel som er bundet til antistoffet via en proteasespaltbar linker.» Engelsk originaltekst: "Enfortumab vedotin-ejfv is an ADC. The antibody is a human IgG1 kappa directed against Nectin-4, an adhesion protein located on the surface of cells. The small molecule, MMAE, is a microtubule-disrupting agent, attached to the antibody via a protease-cleavable linker." ([DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed), versjon av 2026-08-04; hentet 2026-11-19). Basert på kjent informasjon er enfortumab vedotin et Nectin-4-rettet ADC med MMAE som cytotoksisk nyttelast, godkjent for urotelialt karsinom.

Det er ikke etablert noen mekanistisk kobling mellom dette legemidlet og lepra, som er en mykobakteriell infeksjon. Et cytotoksisk ADC har ingen plausibel rolle i behandling av en slik infeksjon. Den høye TxGNN-scoren er en ren grafbasert prediksjon uten støtte fra studier eller litteratur. Likhet med den opprinnelige indikasjonen er ikke vurdert.

Øvrige prediksjoner i rangeringen har heller ingen terapeutisk støtte:

| Rang | Sykdom | Score | Vurdering |
|---|---|---|---|
| 2 | Multippel endokrin neoplasi | 0,9943 | Ingen holdepunkter for Nectin-4-uttrykk eller respons på MMAE-ADC |
| 3 | Cytomegalovirusinfeksjon | 0,9936 | Kun en kasuistikk om bivirkning; ingen terapeutisk effekt vist |
| 4 | Candidiasis | 0,9930 | Kun en farmakovigilansanalyse (FAERS); gjelder risikosignal, ikke nytte |
| 5 | Hjerneinfarkt | 0,9923 | Ingen plausibel mekanisme |
| 6 | HIV-infeksjon | 0,9919 | Ingen antiviral aktivitet; dårlig egnet for en cytotoksisk substans |
| 7 | Homozygot familiær hyperkolesterolemi | 0,9918 | Ingen sammenheng med virkningsmekanismen |
| 8 | Smittsom bovin rhinotracheitt | 0,9913 | Veterinær sykdom, trolig grafartefakt |
| 9 | Malign katarr (malignant catarrhal fever) | 0,9913 | Veterinær sykdom, trolig grafartefakt |

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur for den predikerte hovedindikasjonen (lepra).

For andre prediksjoner fant man kun sikkerhetsrelatert litteratur, som ikke støtter reposisjonering:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [42647281](https://pubmed.ncbi.nlm.nih.gov/42647281/) | 2026 | Kasuistikk (bivirkning) | Reports (MDPI) | Alvorlig ulcerativ øsofagitt etter enfortumab vedotin og pembrolizumab ved metastatisk urotelialt karsinom |
| [41341429](https://pubmed.ncbi.nlm.nih.gov/41341429/) | 2025 | Farmakovigilansanalyse (FAERS) | Clinical Epidemiology | Risikosignaler for ADC-er ved blærekreft i reelle data |

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/005392 | Padcev | Enfortumab vedotin | Carcinoma, Transitional Cell; Urologic Neoplasms | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi: ADC (Nectin-4-rettet, MMAE-nyttelast), cytotoksisk nyttelast |
| Myelosuppresjonsrisiko | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Følg gjeldende regelverk for håndtering av cytotoksiske legemidler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Totalt 100 interaksjoner er registrert (kilde: DDInter). Utvalget som er vist i dataene omfatter 20 legemidler, hvorav én er klassifisert som **alvorlig** og resten som **moderate**.
  - **Alvorlig**: klaritromycin
  - **Moderate** (utvalg): antidiabetika som akarbose, albiglutid, alogliptin, metformin, pioglitazon, kanagliflozin, klorpropamid, dapagliflozin, saksagliptin, dulaglutid, empagliflozin, linagliptin, acetoheksamid, ertugliflozin, eksenatid, glimepirid, glipizid og glyburid, samt aprepitant.
- **Sikkerhetssignaler fra litteraturen**: Kasuistikk om alvorlig ulcerativ øsofagitt ved kombinasjon med pembrolizumab, og FAERS-analyse av risikosignaler for ADC-er ved blærekreft.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for lepra er kun modellbasert (L5), uten kliniske studier eller litteratur, og det finnes ingen plausibel mekanisme for et cytotoksisk Nectin-4-rettet ADC ved en mykobakteriell infeksjon. I tillegg er den eneste godkjenningen i Norge kansellert, og de øvrige prediksjonene mangler terapeutisk støtte.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Advarsler og kontraindikasjoner fra pakningsvedlegget (blokkerende datamangel for sikkerhetsscreening)
- Prekliniske eller mekanistiske data som viser et biologisk grunnlag, f.eks. Nectin-4-uttrykk ved den predikerte sykdommen
- Avklaring av kanselleringen av den norske godkjenningen og dagens markedstilgjengelighet

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Padcev Ejfv (enfortumab vedotin) prescribing information, SEAGEN INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b5631d3e-4604-4363-8f20-11dfc5a4a8ed) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

