---
layout: default
title: Rotigotine
parent: Kun modellprediksjon (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Rotigotine: predikert ny indikasjon Attention deficit-hyperactivity disorder (ADHD) (evidensnivå L5). Opprinnelig indikasjon: Rastløse bein-syndrom"
monitor_inn: "ROTIGOTINE"
predicted_indications: ["attention deficit-hyperactivity disorder", "schizophrenia", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "faciodigitogenital syndrome", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "myopia X-linked", "atypical glycine encephalopathy", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "myopia 26, X-linked, female-limited"]
---

# Rotigotine
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

## Rotigotin: Fra Parkinsons sykdom og rastløse bein-syndrom til attention deficit-hyperactivity disorder (ADHD)
{: .text-alpha }

## Oppsummering i én setning

Rotigotin er en dopaminagonist som opprinnelig brukes til behandling av Parkinsons sykdom og rastløse bein-syndrom (RLS).
TxGNN-modellen predikerer at legemidlet kan være virksomt mot **ADHD**, men det finnes foreløpig **ingen registrerte kliniske studier** og bare **3 indirekte publikasjoner** som støtter retningen. Prediksjonen er derfor på et tidlig, modellbasert stadium.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Rastløse bein-syndrom; Parkinsons sykdom |
| Predikert ny indikasjon | Attention deficit-hyperactivity disorder (ADHD) |
| TxGNN prediksjonsscore | 1,0000 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Rotigotine (uoffisiell oversettelse): «Rotigotin er en non-ergolin dopaminagonist. Den nøyaktige virkningsmekanismen til rotigotin som behandling av Parkinsons sykdom er ukjent, men den antas å være relatert til evnen til å stimulere dopaminreseptorer i caudatus-putamen i hjernen.» Engelsk originaltekst: "Rotigotine is a non-ergoline dopamine agonist. The precise mechanism of action of rotigotine as a treatment for Parkinson's disease is unknown, although it is thought to be related to its ability to stimulate dopamine receptors within the caudate-putamen in the brain." ([DailyMed: Neupro (rotigotine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=939e28c5-f3a9-42c0-9a2d-8d471d82a6e0), versjon av 2026-11-11; hentet 2026-11-19). Ut fra generell kunnskap er rotigotin en dopaminagonist som virker på reseptorene D1–D5 (høyest affinitet for D3), og i tillegg på 5-HT1A- og alfa-2B-reseptorer. Effekten er dokumentert ved Parkinsons sykdom og RLS.

ADHD er knyttet til dysregulering av dopamin- og noradrenalinsystemene, så en biologisk sammenheng er plausibel. De tre publikasjonene er imidlertid indirekte: to omhandler RLS (blant annet hos barn, hvor tilstanden ofte opptrer sammen med ADHD), og én gjelder samspillet mellom alfa-2A-adrenoreseptorer og dopamin D4-reseptorvarianter, som er relevant for ADHD-biologi. Det finnes ingen ADHD-spesifikke kliniske data for rotigotin. Den svært høye scoren er utelukkende en beregnet prediksjon.

---

## Klinisk studieevidens

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Oversiktsartikkel | Revue neurologique | Oversikt over RLS: en sensorimotorisk lidelse med uimotståelig bevegelsestrang i bena, som rammer 2–3 % av befolkningen i vestlige land |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Oversiktsartikkel | Current pharmaceutical design | Oversikt over RLS hos barn og farmakologiske alternativer |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Prekliniske/mekanistiske data | Pharmacological research | Heteromerisering mellom α2A-adrenoreseptorer og polymorfe varianter av dopamin D4-reseptoren; relevant for impulskontrollforstyrrelser og ADHD |

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000626 | Neupro | rotigotine | Restless Legs Syndrome; Parkinson Disease | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter rotigotin til følgende tilstander: hypertensiv lidelse, hypertensjon, multippel systematrofi, posturalt ortostatisk takykardisyndrom, ortostatisk hypotensjon og legemiddelindusert dyskinesi. Dette er modellbaserte koblinger og ikke offisiell merketekst.
- **Legemiddelinteraksjoner:** Det er funnet 51 interaksjoner. De 20 som er listet i dataene er alle av moderat alvorlighetsgrad, blant annet: morfin, kodein, difenoksin, difenoksylat, dronabinol, nabilon, metoklopramid, opium, sibutramin, etanol, prometazin, ioflupan I-123, klorfeniramin, cetirizin, azelastin (nasal), dekstrometorfan, bromfeniramin, karbinoksamin og clemastin. Mange av disse gir additiv sedasjon eller CNS-depresjon.
- **Teoretisk risiko ved schizofreni (sekundær prediksjon):** Full dopaminagonisme kan i teorien forverre psykotiske symptomer.

Se preparatomtalen for fullstendig informasjon om advarsler og kontraindikasjoner.

---

## Andre predikerte indikasjoner (kort oversikt)

| Rangering | Sykdom | Score | Evidensnivå | Kommentar |
|------|------|------|------|------|
| 2 | Schizofreni | 1,0000 | L5 | Indirekte støtte fra metaanalyse av prodopaminerge legemidler mot negative symptomer (PMID 31688399); rotigotin er ikke spesifikt evaluert, og det er teoretisk risiko for forverring av positive symptomer |
| 3–10 | Sjeldne genetiske/utviklingsmessige tilstander (bl.a. polymikrogyri, faciodigitogenitalt syndrom, medfødt glykosyleringsforstyrrelse, retinal dystrofi, X-bundet myopi, atypisk glycinencefalopati, CMT type 1G) | 99,992–1,0000 | L5 | Ingen identifiserbar mekanistisk kobling eller støttende evidens; kun modellprediksjon |

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for ADHD bygger på en biologisk plausibel dopamin- og noradrenalinkobling, men evidensen er kun indirekte (L4), uten kliniske studier. Rotigotin er markedsført i Norge med 1 gyldig markedsføringstillatelse av 1, men viktige sikkerhets- og mekanismedata mangler.

**For å gå videre kreves følgende:**
- Gjennomgang av preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel for sikkerhetsvurderingen
- Detaljerte data om virkningsmekanisme (f.eks. fra DrugBank)
- Prekliniske eller tidlige kliniske data for rotigotin ved ADHD
- Vurdering av kardiovaskulære risikoer (hypertensjon, ortostatisk hypotensjon) hos en ADHD-populasjon, inkludert barn
- Avklaring av regulatorisk status og tilgjengelige administrasjonsveier (plaster) i Norge

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Neupro (rotigotine) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=939e28c5-f3a9-42c0-9a2d-8d471d82a6e0) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

