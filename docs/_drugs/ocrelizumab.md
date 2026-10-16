---
layout: default
title: Ocrelizumab
parent: Kun modellprediksjon (L5)
nav_order: 292
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Ocrelizumab: predikert ny indikasjon HER2-positiv brystkreft (evidensnivå L5). Opprinnelig indikasjon: Multippel sklerose"
monitor_inn: "OCRELIZUMAB"
predicted_indications: ["HER2 positive breast carcinoma", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer"]
---

# Ocrelizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Okrelizumab: Fra multippel sklerose til HER2-positiv brystkreft

## Oppsummering

Okrelizumab er et anti-CD20-monoklonalt antistoff som opprinnelig brukes til behandling av multippel sklerose (MS). TxGNN-modellen forutsier at det kan ha effekt ved **HER2-positiv brystkreft**, men prediksjonen er rent beregningsbasert: det finnes **0 kliniske studier** og **0 publikasjoner** som støtter akkurat denne indikasjonen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Multippel sklerose |
| Predikert ny indikasjon | HER2-positiv brystkreft |
| TxGNN-prediksjonsscore | 99,89 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert/trukket tilbake |
| Antall godkjenninger | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Okrelizumab er et humanisert anti-CD20-antistoff som selektivt tømmer CD20-uttrykkende B-celler. Detaljerte data om virkningsmekanisme (MOA) er ikke tilgjengelige i datagrunnlaget som er samlet for denne rapporten. Basert på kjent informasjon er legemidlet godkjent for MS, der B-celledepletering har vist klar effekt.

Det er ikke påvist noen direkte mekanistisk sammenheng mellom CD20-rettet B-celledepletering og HER2-drevet brystkreft. Tumorinfiltrerende B-celler diskuteres i brystkreftimmunologi, men depletering av CD20-positive celler kan være nøytralt eller til og med skadelig. Dette er spekulativt. Den svært høye TxGNN-scoren (0,999) er en ren modellprediksjon og bør ikke tolkes som klinisk evidens.

Merk at de øvrige toppredikasjonene (normal brystlignende subtype, progesteronreseptor-positiv, luminal A/B og progesteronreseptor-negativ brystkreft) alle er brystkrefttyper med tilsvarende score og tilsvarende mangel på evidens. Det tyder på at modellen peker på brystkreft generelt, ikke på en spesifikk subtype.

---

## Klinisk studieevidens

Foreløpig er det ikke registrert noen relaterte kliniske studier.

---

## Litteraturevidens

Det finnes ingen litteratur som evaluerer okrelizumab ved HER2-positiv brystkreft. For predikasjonen «luminal A/B brystsvulst» ble det hentet 18 publikasjoner via nøkkelordassosiasjon med legemidlet, men ingen av dem omhandler brystkreft. De mest relevante som bakgrunn om legemidlet:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [28002688](https://pubmed.ncbi.nlm.nih.gov/28002688/) | 2017 | RCT | N Engl J Med | Okrelizumab mot placebo ved primær progressiv MS (ORATORIO) |
| [28002679](https://pubmed.ncbi.nlm.nih.gov/28002679/) | 2017 | RCT | N Engl J Med | Okrelizumab mot interferon beta-1a ved relapserende MS (OPERA) |
| [40245351](https://pubmed.ncbi.nlm.nih.gov/40245351/) | 2025 | Fase 3 | Neurology | Subkutan mot intravenøs okrelizumab ved MS (OCARINA II) |
| [35176351](https://pubmed.ncbi.nlm.nih.gov/35176351/) | 2022 | Veiledning | J Allergy Clin Immunol | Sekundær hypogammaglobulinemi, relevant for sikkerhet ved anti-CD20-behandling |
| [35192158](https://pubmed.ncbi.nlm.nih.gov/35192158/) | 2022 | Oversikt | Drugs | Oversikt over okrelizumab ved MS |

Disse publikasjonene gir ingen evidens for brystkreft. De er kun bakgrunn om legemidlets sikkerhetsprofil og bruk ved MS.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004043 | Ocrevus | Ikke oppgitt | Multippel sklerose |

Godkjenningen har status avregistrert/trukket tilbake. Det finnes ingen gyldige godkjenninger i dataene.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det ble funnet 100 registrerte interaksjoner. De fleste av de viste er av moderat alvorlighetsgrad:
  - Kortikosteroider (hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednisolon, prednison): moderat
  - Radiofarmaka og radioimmunoterapi (jobenguan I-131, ibritumomab tiuxetan, tositumomab, samarium-153-leksidronam): moderat
  - Albendazol, pentamidin, levamisol: moderat
  - Sinksalter (sulfat, acetat, glukonat, klorid): mindre alvorlig
- **Bakgrunn om sikkerhet**: Litteraturen peker på risiko for sekundær hypogammaglobulinemi ved anti-CD20-behandling.

Se preparatomtalen for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en modellscore uten støtte fra kliniske studier eller litteratur (evidensnivå L5), og det finnes ingen påvist mekanistisk sammenheng mellom CD20-depletering og brystkreft. Legemidlet har dessuten ingen gyldig markedsføringstillatelse i Norge i dataene.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA)
- Prekliniske studier som undersøker B-celler og CD20 i brystkrefts tumormikromiljø
- Preparatomtale med advarsler og kontraindikasjoner for sikkerhetsscreening
- Avklaring av regulatorisk status i Norge og tilgjengelig administrasjonsvei
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

