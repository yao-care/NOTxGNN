---
layout: default
title: Ivosidenib
parent: Kun modellprediksjon (L5)
nav_order: 226
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Ivosidenib: predikert ny indikasjon Bulbær polio (evidensnivå L5). Opprinnelig indikasjon: Akutt myeloid leukemi"
monitor_inn: "IVOSIDENIB"
predicted_indications: ["bulbar polio"]
---

# Ivosidenib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Ivosidenib: Fra akutt myeloid leukemi og kolangiokarsinom til bulbær polio

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
| TxGNN-prediksjonsscore | 99,31 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellert (ingen gyldig markedsføringstillatelse) |
| Antall tillatelser | 1 (kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ivosidenib hemmer mutert IDH1-enzym og senker nivået av onkometabolitten 2-hydroksyglutarat i IDH1-muterte svulster. Data om legemidlets detaljerte virkningsmekanisme er ikke tilgjengelige i datagrunnlaget som er samlet for denne rapporten, så vurderingen bygger på allment kjent farmakologi.

For den toppredikerte indikasjonen, **bulbær polio**, er det ikke identifisert noen plausibel mekanistisk kobling. Bulbær polio er en virusinfeksjon i motoriske nevroner forårsaket av poliovirus, og ingen IDH1-avhengig mekanisme er kjent. Den svært høye scoren (0,993) ser ut til å være en artefakt fra kunnskapsgrafen, uten støtte fra studier eller litteratur.

De to neste prediksjonene, **AML/MDS relatert til alkyleringsmidler** og **AML/MDS relatert til stråling**, er biologisk plausible, men indirekte. Behandlingsrelatert AML/MDS kan ha IDH1-mutasjoner, og en eventuell effekt vil avhenge av mutasjonsstatus, ikke av årsaken til sykdommen. Begge har identisk score (0,9926), noe som tyder på at de er søskennoder i sykdomsontologien og scores samlet. De utgjør en undergruppe av en allerede godkjent bruk, og er derfor ikke ekte repurposing-kandidater.

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

Tillatelsen er kansellert, og det finnes ingen gyldige tillatelser i Norge. Innehaver: Les Laboratoires Servier.

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
Toppprediksjonen (bulbær polio) mangler både mekanistisk støtte og enhver klinisk evidens, og er mest sannsynlig en artefakt i kunnskapsgrafen. De to AML/MDS-prediksjonene er undergrupper av en allerede godkjent indikasjon, og har ingen egne data. I tillegg er den norske tillatelsen kansellert.

**For å gå videre trengs følgende:**
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Subgruppeanalyser fra pivotale AML-studier (sekundær eller behandlingsrelatert AML/MDS) med IDH1-mutasjonsstatus
- Avklaring av hvorfor den norske tillatelsen er kansellert, og om en ny søknad er aktuell
- Vurdering av QT-relaterte og CYP3A4-relaterte interaksjoner før eventuell klinisk bruk
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

