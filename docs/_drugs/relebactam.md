---
layout: default
title: Relebactam
parent: Kun modellprediksjon (L5)
nav_order: 353
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
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

Ifølge ChEMBL (EMBL-EBI) er den registrerte virkningsmekanismen for Relebactam (uoffisiell oversettelse): «Betalaktamase SHV-1-hemmer; bakteriell betalaktamase TEM-hemmer; betalaktamasehemmer; karbapenemhydrolyserende betalaktamase KPC-hemmer». Engelsk originaltekst: "Beta-lactamase SHV-1 inhibitor; Bacterial beta-lactamase TEM inhibitor; Beta-lactamase inhibitor; Carbapenem-hydrolyzing beta-lactamase KPC inhibitor" ([ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605), CC BY-SA 3.0; hentet 2026-11-19). Basert på kjent informasjon er relebactam en betalaktamasehemmer (diazabicyclooktan) som gis sammen med imipenem/cilastatin for å gjenopprette karbapenemets effekt mot resistente gramnegative bakterier.

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

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004808 | Recarbrio | imipenem monohydrate; cilastatin sodium; relebactam monohydrate | Gram-Negative Bacterial Infections | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

Se preparatomtalen for sikkerhetsinformasjon. Det er ikke funnet registrerte interaksjoner, og ingen kontraindikasjoner fra kunnskapsgrafen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Alle tre prediksjonene er på evidensnivå L5 uten kliniske studier, litteratur eller mekanistisk begrunnelse.

<!-- review:begin no-lic-20261124b-relebactam-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den eneste godkjenningen i Norge kansellert.» Fjernet: opplysningen om at godkjenningen(e) er kansellert, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-relebactam-1 -->

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (mangler, og blokkerer sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Vurdering av om hyperamylasemi er en bivirkning/assosiasjon snarere enn et terapeutisk mål
- Prekliniske eller mekanistiske data som kan underbygge en eventuell sammenheng
- Avklaring av administrasjonsvei og markedsstatus

<!-- review:begin no-lic-20261124b-relebactam-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av administrasjonsvei og markedsstatus (godkjenningen er kansellert)» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-relebactam-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde (revidert 2026-11-20; tidligere versjon er lagret i posten) | [ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605) |
| 2026-11-24 | Fjernet: «I tillegg er den eneste godkjenningen i Norge kansellert.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av administrasjonsvei og markedsstatus (godkjenningen er kansellert)» → «Avklaring av administrasjonsvei og markedsstatus» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

