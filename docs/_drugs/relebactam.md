---
layout: default
title: Relebactam
parent: Kun modellprediksjon (L5)
nav_order: 353
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Relebactam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
description: "Relebactam: predikert ny indikasjon Hyperamylasemi (hyperamylasemia) (evidensnivå L5). Opprinnelig indikasjon: Gram-Negative Bacterial Infections"
---

# Relebactam
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

## Relebactam: Hyperamylasemi (hyperamylasemia)
{: .text-alpha }

## Oppsummering i én setning

Relebactam er en betalaktamasehemmer som brukes sammen med imipenem/cilastatin (Recarbrio) mot infeksjoner forårsaket av gramnegative bakterier.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **hyperamylasemi**, men dette er kun en modellprediksjon: det finnes **0 kliniske studier** og **0 publikasjoner** som støtter den.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Gram-Negative Bacterial Infections |
| Predikert ny indikasjon | Hyperamylasemi (hyperamylasemia) |
| TxGNN-prediksjonsscore | 0.9922 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er (eller er ikke) denne prediksjonen rimelig?

Ifølge ChEMBL (EMBL-EBI) er den registrerte virkningsmekanismen for Relebactam (uoffisiell oversettelse): «Betalaktamase SHV-1-hemmer; bakteriell betalaktamase TEM-hemmer; betalaktamasehemmer; karbapenemhydrolyserende betalaktamase KPC-hemmer» Engelsk originaltekst: "Beta-lactamase SHV-1 inhibitor; Bacterial beta-lactamase TEM inhibitor; Beta-lactamase inhibitor; Carbapenem-hydrolyzing beta-lactamase KPC inhibitor" ([ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605), CC BY-SA 3.0; hentet 2026-11-19). Basert på kjent informasjon er relebactam en betalaktamasehemmer (diazabicyclooktan) som gis sammen med imipenem/cilastatin for å gjenopprette karbapenemets effekt mot resistente gramnegative bakterier.

Det er ikke funnet noen plausibel mekanistisk sammenheng mellom dette og hyperamylasemi. Relebactam har ingen kjent virkning på regulering av amylase eller på håndtering av bukspytt- og spyttkjertelenzymer.

To andre prediksjoner med svært høy score mangler også støtte:
- **Polyklonalt hyperviskositetssyndrom** (score 0,9922, identisk med hyperamylasemi): Sykdommen skyldes økte immunglobuliner, og behandlingen rettes mot den underliggende immunprosessen. Relebactam har ingen kjent immunmodulerende virkning. Den identiske scoren tyder på en grafstrukturartefakt.
- **Medfødt analbuminemi** (score 0,9908): En sjelden genetisk sykdom forårsaket av mutasjoner i albumingenet (ALB). Relebactam påvirker ikke albuminsyntese eller -funksjon og kan ikke forventes å korrigere en monogen mangel.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004808 | Recarbrio | – | Gramnegative bakterieinfeksjoner |

---

## Sikkerhetsvurderinger

Se preparatomtalen for sikkerhetsinformasjon. Det er ikke funnet registrerte interaksjoner, og ingen kontraindikasjoner fra kunnskapsgrafen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle tre prediksjonene er på evidensnivå L5 uten kliniske studier, litteratur eller mekanistisk begrunnelse. I tillegg er den eneste godkjenningen i Norge kansellert.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (mangler, og blokkerer sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Vurdering av om hyperamylasemi er en bivirkning/assosiasjon snarere enn et terapeutisk mål
- Prekliniske eller mekanistiske data som kan underbygge en eventuell sammenheng
- Avklaring av administrasjonsvei og markedsstatus (godkjenningen er kansellert)

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

