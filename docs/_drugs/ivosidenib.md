---
layout: default
title: Ivosidenib
parent: Kun modellprediksjon (L5)
nav_order: 226
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Ivosidenib: predikert ny indikasjon Bulbær polio (evidensnivå L5). Opprinnelig indikasjon: Akutt myeloid leukemi"
monitor_inn: "IVOSIDENIB"
predicted_indications: ["bulbar polio"]
---

# Ivosidenib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Ivosidenib: Fra akutt myeloid leukemi og kolangiokarsinom til bulbær polio
{: .text-alpha }

## Oppsummering i én setning

Ivosidenib er en hemmer av mutert IDH1, opprinnelig godkjent for behandling av akutt myeloid leukemi og kolangiokarsinom.
TxGNN-modellen forutsier at legemidlet kan ha effekt mot **bulbær polio**, men dette er en ren modellprediksjon uten støtte i kliniske studier (**0 kliniske studier**) eller litteratur (**0 publikasjoner**).
To av de tre toppforutsigelsene (AML/MDS relatert til alkyleringsmidler og stråling) er i realiteten undergrupper av den allerede godkjente AML-indikasjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Akutt myeloid leukemi; kolangiokarsinom |
| Predikert ny indikasjon | Bulbær polio |
| TxGNN-prediksjonsscore | 0,9931 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ivosidenib hemmer mutert IDH1-enzym og senker nivået av onkometabolitten 2-hydroksyglutarat i IDH1-muterte svulster. Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Ivosidenib (uoffisiell oversettelse): «Ivosidenib er en småmolekylær hemmer rettet mot det muterte enzymet isocitratdehydrogenase 1 (IDH1). Hos pasienter med AML defineres mottakelige IDH1-mutasjoner som mutasjoner som fører til økte nivåer av 2-hydroksyglutarat (2-HG) i leukemicellene, og der effekt predikeres av 1) klinisk betydningsfulle remisjoner med anbefalt dose ivosidenib og/eller 2) hemming av mutert IDH1-enzymaktivitet ved konsentrasjoner av ivosidenib som kan opprettholdes ved anbefalt dosering, i henhold til validerte metoder.» Engelsk originaltekst: "Ivosidenib is a small molecule inhibitor that targets the mutant isocitrate dehydrogenase 1 (IDH1) enzyme. In patients with AML, susceptible IDH1 mutations are defined as those leading to increased levels of 2-hydroxyglutarate (2-HG) in the leukemia cells and where efficacy is predicted by 1) clinically meaningful remissions with the recommended dose of ivosidenib and/or 2) inhibition of mutant IDH1 enzymatic activity at concentrations of ivosidenib sustainable at the recommended dosage according to validated methods." ([DailyMed: Tibsovo (ivosidenib) prescribing information, Servier Pharmaceutical LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65d254c0-67ad-42c4-b972-ad463b755b2d), versjon av 2025-12-22; hentet 2026-11-19).

For den toppredikerte indikasjonen, **bulbær polio**, er det ikke identifisert noen plausibel mekanistisk kobling. Bulbær polio er en virusinfeksjon i motoriske nevroner forårsaket av poliovirus, og ingen IDH1-avhengig mekanisme er kjent. Den svært høye scoren (0,9931) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens, og den har ingen støtte fra studier eller litteratur.

De to neste prediksjonene, **AML/MDS relatert til alkyleringsmidler** og **AML/MDS relatert til stråling**, er biologisk plausible, men indirekte. Behandlingsrelatert AML/MDS kan ha IDH1-mutasjoner, og en eventuell effekt vil avhenge av mutasjonsstatus, ikke av årsaken til sykdommen. Begge har identisk score (0,9931), noe som tyder på at de er søskennoder i sykdomsontologien og scores samlet. De utgjør en undergruppe av en allerede godkjent bruk, og er derfor ikke ekte repurposing-kandidater.

---

## Kliniske studier

Foreløpig er det ingen relaterte kliniske studier registrert for noen av de predikerte indikasjonene.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005936 | Tibsovo | Ikke oppgitt | Akutt myeloid leukemi; kolangiokarsinom |

Legemidlet er markedsført i Norge, og 1 av 1 tillatelser er gyldig. Innehaver: Les Laboratoires Servier.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet terapi (IDH1-hemmer), ikke konvensjonelt cytotoksisk |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Blodstatus (CBC), lever- og nyrefunksjon, elektrolytter og EKG (QT-intervall) bør vurderes; bekreft mot pakningsvedlegget |
| Håndteringsvern | Følg gjeldende regler for håndtering av kreftlegemidler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Interaksjonssøket er gjennomført og fant totalt 100 interaksjoner. Blant de første 20 som er vist, er de viktigste:

- **Alvorlig (Major):** aprepitant, klaritromycin, dolasetron, palonosetron, cisaprid, granisetron og levofloksacin. Flere av disse er knyttet til QT-forlengelse eller CYP3A4-påvirkning og krever nøye vurdering.
- **Moderat:** famotidin, loperamid, bisakodyl, pikosulfat, polyetylenglykol, saksagliptin, eliglustat, linagliptin, natriumsulfat, lakserolje, glyserin, laktitol og laktulose.

Advarsler og kontraindikasjoner fra pakningsvedlegget er ikke tilgjengelige. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Toppprediksjonen (bulbær polio) mangler både mekanistisk støtte og enhver klinisk evidens. Scoren kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Legemidlet er markedsført i Norge, og den ene tillatelsen (1 av 1) er gyldig.

**For å gå videre trengs følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Subgruppeanalyser fra pivotale AML-studier (sekundær eller behandlingsrelatert AML/MDS) med IDH1-mutasjonsstatus
- Avklaring av hvorfor den norske tillatelsen er kansellert, og om en ny søknad er aktuell
- Vurdering av QT-relaterte og CYP3A4-relaterte interaksjoner før eventuell klinisk bruk

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Tibsovo (ivosidenib) prescribing information, Servier Pharmaceutical LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=65d254c0-67ad-42c4-b972-ad463b755b2d) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

