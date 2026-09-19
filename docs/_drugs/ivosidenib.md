---
layout: default
title: Ivosidenib
parent: Kun modellprediksjon (L5)
nav_order: 193
evidence_level: L5
indication_count: 3
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

# Ivosidenib: Fra IDH1-mutert akutt myeloid leukemi til bulbær polio

## Sammendrag i en setning

Ivosidenib er en IDH1-mutant enzymhemmer, antatt ut fra tilgjengelige data å være godkjent for IDH1-mutert akutt myeloid leukemi (AML) — formell dokumentasjon av original indikasjon er for øyeblikket en datakløft.
TxGNN-modellens topprangerte prediksjon for dette legemidlet er **bulbær polio**, men **0 kliniske studier** og **0 publikasjoner** støtter for øyeblikket denne spesifikke forbindelsen, og modellens egen begrunnelse merker ingen kjent mekanistisk forbindelse.

## Hurtig oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | IDH1-mutert AML (antatt ut fra gjenbruksbegrunnelse; ikke bekreftet av formelle lisensdata – se datakløft DG001/DG002) |
| Forutsagt ny indikasjon | Bulbær polio |
| TxGNN prediksjonspoeng | 99.31% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er det ikke tilgjengelig detaljerte data om virkningsmekanisme (datakløft DG002). Basert på gjenbruksbegrunnelsen som følger med denne bevissamlingen, forstås ivosidenib å hemme det muterte IDH1-enzymet, og blokkerer akkumulering av onkometabolitten 2-hydroksyglutarat (2-HG) i IDH1-muterte kreftformer som AML.

Bulbær polio er en poliovirus-indusert motorneuron-sykdom. Det eksisterer ingen kjent biologisk forbindelse mellom IDH1/2-HG-metabolisme og poliovirus-mediert nevroneskade. Modellens egen genererte begrunnelse slår eksplisitt fast at denne høye poengsum sannsynligvis reflekterer en **sparsom eller støyende kant i den underliggende kunnskapsgrafen**, snarere enn en genuin mekanistisk forbindelse, og at ingen mekanistisk hypotese for øyeblikket støtter denne koblingen.

Ingen kliniske studier, litteratur eller biologisk sannsynlighet eksisterer for øyeblikket for å støtte ivosidenib som en kandidatbehandling for bulbær polio. Denne prediksjonen bør behandles som en modellartefakt som ikke krever umiddelbar handling, snarere enn som et genuint gjenbrukssignal.

## Klinisk studiebevis

For øyeblikket ingen relaterte kliniske studier registrert

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig

## Markedsinformasjon for Norge

Ivosidenib er for øyeblikket ikke markedsført i Norge. Ingen autorisasjonsregistre er tilgjengelige i denne bevissamlingen (0 lisenser på fil).

## Cytotoksisitet

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (IDH1-mutant enzymhemmer) |
| Risiko for myelosuppresjon | Se pakningsvedleggets advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Se pakningsvedleggets advarsler og forholdsregler |
| Overvåkingselementer | Se pakningsvedleggets advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se pakningsvedleggets advarsler og forholdsregler |

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-poengsum er høy, men det eksisterer ingen klinisk studiebevis, ingen publisert litteratur og ingen plausibel mekanistisk begrunnelse som knytter ivosidenib til bulbær polio. Denne koblingen reflekterer mest sannsynlig støy i kunnskapsgrafen snarere enn en ekte gjenbruksmulighet.

**For å fortsette, er følgende nødvendig:**
- Formell MOA- og original-indikasjonsdokumentasjon (løs DG001, DG002) før ytterligere poengsum
- TFDA/EMA pakningsvedleggets advarsler og kontraindikasjoner for grunnlinjesikkerhetsvurdering
- Hvis denne kandidaten blir gjenbesøkt, kreves en uavhengig mekanistisk hypotese utover det nåværende grafsignalet før man går videre enn S0

---

### Ytterligere forutsagte indikassjoner i denne bevissamlingen

Denne bevissamlingen inneholder to andre kandidatindikassjoner for ivosidenib som er mekanistisk mer plausible og som rettferdiger separat sporing snarere enn avvisning:

| Rangering | Sykdom | TxGNN-poengsum | Bevisnivå | Anbefaling | Sammendrag av begrunnelse |
|-----------|--------|----------------|-----------|------------|---------------------------|
| 2 | AML/MDS relatert til alkylerende midler | 99.26% | L4 | Forskningsspørsmål | Ivosidenib brukes bredt i IDH1-mutert AML (inkludert noen terapirelaterte subtyper ifølge AGILE-forsøket); ekstrapolering til alkylerende-middel-relatert AML/MDS er mekanistisk rimelig hvis IDH1-mutasjon er til stede, men subtypespesifikk mutasjonsprevales og tilleggtoksisitet fra tidligere kjemoterapieksponering er ubekreftet. |
| 3 | AML/MDS relatert til stråling | 99.26% | L4 | Forskningsspørsmål | Samme ekstrapoleringslogikk som ovenfor for strålingsindusert terapirelatert myeloid neoplasmer; ingen subtypespesifikk forsøk eller litteraturbevis eksisterer for øyeblikket i denne samlingen. |

Disse to kandidatene bør prioriteres fremfor Bulbær polio-prediksjonen for enhver framtidig oppfølging av forskningsspørsmål, da de bygger på en etablert (om enn ikke formelt dokumentert i denne samlingen) godkjent bruk av ivosidenib i IDH1-mutert AML.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

