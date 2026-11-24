---
layout: default
title: Tolcapone
parent: Kun modellprediksjon (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Tolcapone: predikert ny indikasjon Rasmussens subakutte encefalitt (evidensnivå L5). Opprinnelig indikasjon: Parkinsons sykdom"
monitor_inn: "TOLCAPONE"
predicted_indications: ["Rasmussen subacute encephalitis", "myelitis", "PLA2G6-associated neurodegeneration", "transaldolase deficiency", "fructose-1,6-bisphosphatase deficiency", "Lewy body dementia", "X-linked intellectual disability-ataxia-apraxia syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "X-linked intellectual disability-cerebellar hypoplasia syndrome", "paralysis agitans, juvenile, of Hunt"]
---

# Tolcapone
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

## Tolkapon: Fra Parkinsons sykdom til Rasmussens subakutte encefalitt
{: .text-alpha }

## Oppsummering i én setning

Tolkapon er en COMT-hemmer som opprinnelig brukes til behandling av Parkinsons sykdom.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **Rasmussens subakutte encefalitt**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Parkinsons sykdom |
| Predikert ny indikasjon | Rasmussens subakutte encefalitt |
| TxGNN-prediksjonsscore | 0,9993 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Tolcapone (uoffisiell oversettelse): «Tolkapon er en selektiv og reversibel hemmer av katekol-O-metyltransferase (COMT). Hos pattedyr er COMT fordelt i ulike organer. Den høyeste aktiviteten finnes i lever og nyrer. COMT forekommer også i hjerte, lunger, glatt muskulatur og skjelettmuskulatur, tarmkanalen, reproduksjonsorganer, ulike kjertler, fettvev, hud, blodceller og nevronalt vev, særlig i gliaceller.» Engelsk originaltekst: "Tolcapone is a selective and reversible inhibitor of catechol- O -methyltransferase (COMT). In mammals, COMT is distributed throughout various organs. The highest activities are in the liver and kidney. COMT also occurs in the heart, lung, smooth and skeletal muscles, intestinal tract, reproductive organs, various glands, adipose tissue, skin, blood cells and neuronal tissues, especially in glial cells." ([DailyMed: Tasmar (tolcapone) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0e47a9d-78e7-4523-983a-aa259f221736), versjon av 2020-10-02; hentet 2026-11-19). Tolkapon er kjent som en hemmer av enzymet katekol-O-metyltransferase (COMT), som bryter ned blant annet levodopa og katekolaminer. Ved Parkinsons sykdom forlenger dette effekten av levodopa.

Rasmussens encefalitt er en immunmediert, kronisk betennelsessykdom i hjernen, vanligvis i én hjernehalvdel. Det er ikke påvist noen mekanistisk sammenheng mellom COMT-hemming og denne tilstanden. Den høye scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

For oversiktens skyld vurderte modellen også andre kandidater. Disse er heller ikke støttet av kliniske data:

| Rangering | Predikert indikasjon | Score | Kommentar |
|------|------|------|------|
| 2 | Myelitt | 0,9990 | Ingen plausibel mekanisme |
| 3 | PLA2G6-assosiert nevrodegenerasjon | 0,9988 | Parkinsonlignende trekk kan forklare nærheten, men gir ikke effekt på den underliggende lipidmetabolismefeilen |
| 4 | Transaldolasemangel | 0,9985 | Sannsynligvis drevet av grafstruktur |
| 5 | Fruktose-1,6-bisfosfatasemangel | 0,9978 | Ingen kobling til COMT |
| 6 | Lewy body-demens | 0,9964 | Biologisk plausibel (dopaminerg dysfunksjon og alfa-synuklein), men uten klinisk evidens |
| 10 | Juvenil paralysis agitans (Hunt) | 0,9952 | I praksis den eksisterende indikasjonen under et annet navn |

---

## Evidens fra kliniske studier

Foreløpig er det ingen registrerte kliniske studier knyttet til denne prediksjonen.

---

## Litteraturevidens

Foreløpig finnes det ingen relevant litteratur for Rasmussens subakutte encefalitt.

For den sjette kandidaten, Lewy body-demens, er én publikasjon funnet:

<!-- review:begin no-lic-20261106-tolcapone-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Godkjenningen har status avregistrert.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-tolcapone-1 -->

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preklinisk (iPSC-organoidmodell) | Science Advances | Modellering av Lewy body-sykdom med kortikale organoider fra pasienter med SNCA-triplikasjon, og identifisering av mulige legemidler. Studien viser ikke klinisk evidens for tolkapon. |

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000132 | Tasmar | tolcapone | Parkinson Disease | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

Opplysninger fra pakningsvedlegg om advarsler og kontraindikasjoner er ikke tilgjengelige i datagrunnlaget. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Kontraindikasjoner fra kunnskapsgrafen** (kunnskapsgrafen PrimeKG, ikke fra preparatomtale):
- Leversykdom
- Galleblæresykdom
- Melanom
- Hypotensive tilstander
- Rabdomyolyse
- Nodulær fasciitt
- Tardiv dyskinesi
- Lingual-facial-bukkal dyskinesi

Tolkapon er i tillegg kjent for leverskade (hepatotoksisitet), som er grunnen til at bruken er begrenset. Dette er en vesentlig sikkerhetsbekymring ved enhver ny bruk.

**Legemiddelinteraksjoner:** Totalt 65 interaksjoner er registrert. Blant de viste er:
- **Alvorlig (Major):** Metylenblått
- **Moderat:** Epinefrin (inkl. oftalmisk og topisk), morfin (inkl. liposomal), opium, kodein, dronabinol, nabilon, naltrekson, metoklopramid, etanol, prometazin, klorfeniramin, cetirizin, dekstrometorfan
- **Mindre (Minor):** Warfarin, dikumarol
- **Ukjent nivå:** Omeprazol

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for Rasmussens subakutte encefalitt støttes verken av kliniske studier eller litteratur, og det finnes ingen kjent mekanistisk sammenheng. Evidensnivået er L5 (kun modellprediksjon). Leverskaderisikoen er en betydelig barriere.

<!-- review:begin no-lic-20261106-tolcapone-2 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «I tillegg er tolkapons godkjenning i Norge avregistrert, og leverskaderisikoen er en betydelig barriere.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-tolcapone-2 -->

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen (kritisk datahull som blokkerer sikkerhetsscreening)
- Prekliniske studier som tester en mulig sammenheng mellom COMT-hemming og Rasmussens encefalitt
- Vurdering av leversikkerhet og overvåkingsplan før noen klinisk utprøving
- Eventuelt vurdere Lewy body-demens som en mer biologisk plausibel kandidat for videre litteraturgjennomgang

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «Godkjenningen har status avregistrert» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-06 | Fjernet: «I tillegg er tolkapons godkjenning i Norge avregistrert, og l» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Tasmar (tolcapone) prescribing information, Bausch Health US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a0e47a9d-78e7-4523-983a-aa259f221736) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

