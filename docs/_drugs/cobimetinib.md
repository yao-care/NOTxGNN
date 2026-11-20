---
layout: default
title: Cobimetinib
parent: Kun modellprediksjon (L5)
nav_order: 104
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Cobimetinib: predikert ny indikasjon Amyotrofisk lateral sklerose (evidensnivå L5). Opprinnelig indikasjon: Melanom"
monitor_inn: "cobimetinib"
predicted_indications: ["amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "axial spondylometaphyseal dysplasia", "Mills syndrome", "lower motor neuron syndrome with late-adult onset", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "lethal arthrogryposis-anterior horn cell disease syndrome", "amyotrohpic lateral sclerosis type 22", "monomelic amyotrophy"]
---

# Cobimetinib
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

## Cobimetinib: Fra melanom til amyotrofisk lateral sklerose (ALS)
{: .text-alpha }

## Oppsummering

Cobimetinib (Cotellic) er en MEK-hemmer som opprinnelig brukes til behandling av melanom.
TxGNN-modellen predikerer at legemidlet kan være effektivt mot **amyotrofisk lateral sklerose (ALS)**,
men for øyeblikket finnes **ingen kliniske studier** og **ingen publikasjoner** i de innsamlede dataene som støtter denne retningen. Prediksjonen er kun beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Melanom |
| Predikert ny indikasjon | Amyotrofisk lateral sklerose |
| TxGNN-prediksjonsscore | 0,9973 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall autorisasjoner | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Cobimetinib (uoffisiell oversettelse): «Kobimetinib er en reversibel hemmer av mitogenaktivert proteinkinase (MAPK)/ekstracellulært signalregulert kinase 1 (MEK1) og MEK2. MEK-proteiner er oppstrømsregulatorer av signalveien for ekstracellulær signalrelatert kinase (ERK), som fremmer celleproliferasjon.» Engelsk originaltekst: "Cobimetinib is a reversible inhibitor of mitogen-activated protein kinase (MAPK)/extracellular signal regulated kinase 1 (MEK1) and MEK2. MEK proteins are upstream regulators of the extracellular signal-related kinase (ERK) pathway, which promotes cellular proliferation." ([DailyMed: Cotellic (cobimetinib) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c387579e-cee0-4334-bd1e-73f93ac1bde6), versjon av 2026-07-29; hentet 2026-11-19). Basert på generell kunnskap om legemiddelklassen er cobimetinib en hemmer av MEK1/2 i MAPK/ERK-signalveien. Effekten ved melanom er påvist, og mekanistisk kan hemming av denne signalveien tenkes å være relevant for ALS.

Aktivering av MAPK/ERK-signalveien og nevroinflammasjon har vært koblet til ALS-biologi, så en hypotetisk sammenheng finnes. Datagrunnlaget inneholder imidlertid verken studier eller litteratur som underbygger den. Den høye scoren (0,9973) er en ren modellprediksjon.

Systemisk MEK-hemming har også tolerabilitetsutfordringer, blant annet utslett, retinopati og rabdomyolyse/CK-økning. Dette må vurderes nøye i en pasientgruppe med motornevronsykdom.

### Andre predikerte indikasjoner (alle L5, Hold)

Ingen av de ti predikerte indikasjonene har kliniske studier eller litteratur. De øvrige er:

| Rang | Sykdom | Score | Kommentar |
|---|---|---|---|
| 2 | Bilateral parasagittal parieto-occipital polymikrogyri | 0,9966 | Utviklingsmessig kortikal misdannelse; ingen klar mekanistisk sammenheng |
| 3 | Aksial spondylometafysær dysplasi | 0,9961 | Sjelden skjelettdysplasi; ingen mekanistisk sammenheng |
| 4 | Mills syndrom | 0,9959 | Indirekte sammenheng via motornevrondegenerasjon |
| 5 | ALS, mottakelighet for | 0,9957 | Overlapper med hoved-ALS-prediksjonen; ikke uavhengig evidens |
| 6 | Nedre motornevronsyndrom med sen voksendebut | 0,9957 | Indirekte og hypotetisk |
| 7 | Trikomegali-retinal pigmentdegenerasjon-dvergvekst-syndrom | 0,9956 | Ingen støtte; MEK-hemmere kan gi retinal toksisitet |
| 8 | Letal artrogrypose-fremre hornscelle-syndrom | 0,9955 | Letal medfødt tilstand; svært svakt grunnlag |
| 9 | ALS type 22 | 0,9954 | Genetisk ALS-subtype; overlapper med generell ALS |
| 10 | Monomelisk amyotrofi | 0,9951 | Godartet, selvbegrensende; ugunstig nytte-risiko |

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det foreligger for øyeblikket ingen relatert litteratur.

---

## Markedsinformasjon for Norge

| Autorisasjonsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003960 | Cotellic | – | Melanom |

Legemidlet er markedsført, og 1 av 1 autorisasjon er gyldig.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (MEK-hemmer) |
| Myelosuppresjonsrisiko | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Monitoreringspunkter | Se pakningsvedlegget; for MEK-hemmere vurderes generelt CK, lever- og nyrefunksjon samt øyeundersøkelse |
| Håndteringsbeskyttelse | Se pakningsvedlegget for advarsler og forsiktighetsregler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er identifisert totalt 266 interaksjoner. Blant de som er vist i dataene, er de viktigste av alvorlighetsgrad «Major»:

- Aprepitant
- Deksametason
- Klaritromycin
- Kobicistat
- Samarium (153Sm) lexidronam

I tillegg er flere interaksjoner av moderat alvorlighetsgrad registrert, blant andre cimetidin, klotrimazol, mikonazol, naltrekson, tikagrelor, kinin og ivakaftor.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se pakningsvedlegget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på modellscore (evidensnivå L5) uten kliniske studier eller litteratur. Legemidlet har dessuten kun en kansellert autorisasjon i Norge, og systemisk MEK-hemming har tolerabilitetsutfordringer i en nevrodegenerativ pasientgruppe.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Pakningsvedlegg med advarsler og kontraindikasjoner fra DMP
- Prekliniske data eller litteratursøk som kobler MEK/ERK-hemming til ALS-patofysiologi
- Vurdering av markedstilgjengelighet i Norge gitt at autorisasjonen er kansellert
- Sikkerhetsvurdering for MEK-hemmer i motornevronsykdom (CK-økning, retinopati, utslett)

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Cotellic (cobimetinib) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c387579e-cee0-4334-bd1e-73f93ac1bde6) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

