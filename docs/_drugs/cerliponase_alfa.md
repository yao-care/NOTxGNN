---
layout: default
title: Cerliponase Alfa
parent: Kun modellprediksjon (L5)
nav_order: 92
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Cerliponase Alfa: predikert ny indikasjon Scheie syndrom (evidensnivå L5). Opprinnelig indikasjon: Nevronale ceroid-lipofuscinoser"
monitor_inn: "CERLIPONASE ALFA"
predicted_indications: ["Scheie syndrome", "Hurler syndrome", "lysosomal storage disease with skeletal involvement", "cholesteryl ester storage disease", "Gaucher disease", "familial encephalopathy with neuroserpin inclusion bodies", "Wolman disease with hypolipoproteinemia and acanthocytosis", "proximal myopathy with extrapyramidal signs", "autosomal ichthyosis syndrome with fatal disease course"]
---

# Cerliponase Alfa
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

## Cerliponase alfa: Fra nevronal ceroid-lipofuscinose til Scheie syndrom
{: .text-alpha }

## Oppsummering i én setning

Cerliponase alfa er et rekombinant enzym (tripeptidylpeptidase 1, TPP1) som opprinnelig brukes til å behandle nevronale ceroid-lipofuscinoser (CLN2-sykdom).
TxGNN-modellen forutsier at det kan være effektivt mot **Scheie syndrom**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen.
Prediksjonen bygger kun på modellen (evidensnivå L5), og mekanismen taler snarere mot en effekt.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Nevronale ceroid-lipofuscinoser |
| Predikert ny indikasjon | Scheie syndrom |
| TxGNN-prediksjonsscore | 0,9998 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall markedsføringstillatelser | 1 (0 gyldige, 1 kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Cerliponase Alfa (uoffisiell oversettelse): «CLN2-sykdom er en nevrodegenerativ sykdom forårsaket av mangel på det lysosomale enzymet tripeptidylpeptidase-1 (TPP1), som kataboliserer polypeptider i CNS. TPP1 har ingen kjent substratspesifisitet. […] Cerliponase alfa (rhTTP1), et proenzym, tas opp av målceller i CNS og translokeres til lysosomene via den kationuavhengige mannose-6-fosfatreseptoren (CI-MPR, også kjent som M6P/IGF2-reseptor).» Engelsk originaltekst: "CLN2 disease is a neurodegenerative disease caused by deficiency of the lysosomal enzyme tripeptidyl peptidase-1 (TPP1), which catabolizes polypeptides in the CNS. TPP1 has no known substrate specificity. […] Cerliponase alfa (rhTTP1), a proenzyme, is taken up by target cells in the CNS and is translocated to the lysosomes through the Cation Independent Mannose-6-Phosphate Receptor (CI-MPR, also known as M6P/IGF2 receptor)." ([DailyMed: Brineura (cerliponase alfa) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=485ab3c5-0359-4878-872f-2fe1e7df4047), versjon av 2024-08-05; hentet 2026-11-19). Basert på kjent informasjon er cerliponase alfa rekombinant humant TPP1, et lysosomalt enzym som gis som enzymerstatning direkte i hjerneventriklene (intracerebroventrikulært) ved CLN2-sykdom.

Scheie syndrom (mild form av MPS I) skyldes mangel på et annet lysosomalt enzym, alfa-L-iduronidase (IDUA). Det er ingen åpenbar overlapp i substrat: TPP1 bryter ikke ned glykosaminoglykaner, og enzymerstatning med TPP1 ventes ikke å korrigere IDUA-mangel. Den høye TxGNN-scoren gjenspeiler trolig at sykdommene ligger nær hverandre i nettverket av lysosomale lagringssykdommer, ikke et reelt mekanistisk grunnlag.

De øvrige predikerte indikasjonene i datagrunnlaget (blant annet Hurler syndrom, Gaucher sykdom, kolesterolesterlagringssykdom og Wolmans sykdom) har samme svakhet: de involverer andre enzymdefekter eller ikke-lysosomale mekanismer, og alle er vurdert til L5 med anbefaling Hold.

---

## Klinisk studieevidens

Foreløpig er det ingen registrerte kliniske studier knyttet til denne indikasjonen.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur for Scheie syndrom.

For sammenhengen kan nevnes at for den femte predikerte indikasjonen (Gaucher sykdom) ble én publikasjon funnet:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [41527340](https://pubmed.ncbi.nlm.nih.gov/41527340/) | 2026 | Oversiktsartikkel | Journal of Inherited Metabolic Disease | Kartlegging av naturlig sykdomsforløp ved lysosomale lagringssykdommer med Gaucher som modell. Omhandler ikke cerliponase alfa og gir kun indirekte bakgrunn. |

---

## Informasjon om markedet i Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004065 | Brineura | Ikke oppgitt | Nevronale ceroid-lipofuscinoser (status: kansellert) |

---

## Sikkerhetsvurderinger

Se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon. Det er ikke funnet noen registrerte legemiddelinteraksjoner i datagrunnlaget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes kun av modellen (L5), uten kliniske studier eller litteratur. Mekanismen er dessuten uforenlig: TPP1 kan ikke erstatte manglende IDUA, og høy score skyldes mest sannsynlig nærhet i sykdomsnettverket. I tillegg er den eneste norske tillatelsen kansellert.

**For å gå videre kreves følgende:**
- Detaljerte mekanismedata (MOA) og en konkret biologisk begrunnelse for hvorfor TPP1 kunne påvirke IDUA-mangel
- Preparatomtale med advarsler og kontraindikasjoner fra DMP, som er nødvendig for sikkerhetsscreening
- Prekliniske data som viser effekt i modeller for MPS I
- Avklaring av administrasjonsvei og markedstilgang i Norge, siden tillatelsen er kansellert

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Brineura (cerliponase alfa) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=485ab3c5-0359-4878-872f-2fe1e7df4047) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

