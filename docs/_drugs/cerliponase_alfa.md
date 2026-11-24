---
layout: default
title: Cerliponase Alfa
parent: Kun modellprediksjon (L5)
nav_order: 92
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
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
| Anbefalt beslutning | Hold |

<!-- review:begin no-lic-20261124b-cerliponase_alfa-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Antall markedsføringstillatelser / 1 (0 gyldige, 1 kansellert)» Fjernet: raden gjentok antallet godkjenninger med status «kansellert», noe som ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); antall og status står i raden «Antall godkjenninger» og i lisenstabellen. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-cerliponase_alfa-1 -->

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

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004065 | Brineura | cerliponase alfa | Neuronal Ceroid-Lipofuscinoses | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

Se preparatomtalen (pakningsvedlegget) for sikkerhetsinformasjon. Det er ikke funnet noen registrerte legemiddelinteraksjoner i datagrunnlaget.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes kun av modellen (L5), uten kliniske studier eller litteratur. Mekanismen er dessuten uforenlig: TPP1 kan ikke erstatte manglende IDUA, og høy score skyldes mest sannsynlig nærhet i sykdomsnettverket.

<!-- review:begin no-lic-20261124b-cerliponase_alfa-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den eneste norske tillatelsen kansellert.» Fjernet: opplysningen om at godkjenningen(e) er kansellert, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-cerliponase_alfa-2 -->

**For å gå videre kreves følgende:**
- Detaljerte mekanismedata (MOA) og en konkret biologisk begrunnelse for hvorfor TPP1 kunne påvirke IDUA-mangel
- Preparatomtale med advarsler og kontraindikasjoner fra DMP, som er nødvendig for sikkerhetsscreening
- Prekliniske data som viser effekt i modeller for MPS I
- Avklaring av administrasjonsvei og markedstilgang i Norge

<!-- review:begin no-lic-20261124b-cerliponase_alfa-3 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av administrasjonsvei og markedstilgang i Norge, siden tillatelsen er kansellert» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-cerliponase_alfa-3 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Brineura (cerliponase alfa) prescribing information, BioMarin Pharmaceutical Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=485ab3c5-0359-4878-872f-2fe1e7df4047) |
| 2026-11-24 | Fjernet: «&#124; Antall markedsføringstillatelser &#124; 1 (0 gyldige, 1 kansellert) &#124;» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Fjernet: «I tillegg er den eneste norske tillatelsen kansellert.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av administrasjonsvei og markedstilgang i Norge, siden tillatelsen er kansellert» → «Avklaring av administrasjonsvei og markedstilgang i Norge» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

