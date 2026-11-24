---
layout: default
title: Tivozanib
parent: Kun modellprediksjon (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Tivozanib: predikert ny indikasjon Endocervikalt karsinom (evidensnivå L5). Opprinnelig indikasjon: Nyrecellekarsinom (Carcinoma, Renal Cell)"
monitor_inn: "TIVOZANIB"
predicted_indications: ["endocervical carcinoma", "uterine ligament adenocarcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma", "cervical mucinous adenocarcinoma, minimal deviation variant"]
---

# Tivozanib
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

## Tivozanib: Fra nyrecellekarsinom til endocervikalt karsinom
{: .text-alpha }

## Oppsummering i én setning

Tivozanib er en VEGF-reseptor-tyrosinkinasehemmer som opprinnelig brukes til behandling av avansert nyrecellekarsinom.
TxGNN-modellen forutsier at legemidlet kan ha effekt mot **endocervikalt karsinom**,
men det finnes foreløpig **0 kliniske studier** og **0 publikasjoner** i de innsamlede dataene som støtter denne retningen. Prediksjonen er kun beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Nyrecellekarsinom (Carcinoma, Renal Cell) |
| Predikert ny indikasjon | Endocervikalt karsinom |
| TxGNN-prediksjonsscore | 0,9981 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Tivozanib (uoffisiell oversettelse): «Tivozanib er en tyrosinkinasehemmer. Cellulære kinaseanalyser in vitro viste at tivozanib hemmer fosforylering av vaskulær endotelial vekstfaktorreseptor (VEGFR)-1, VEGFR-2 og VEGFR-3, og hemmer andre kinaser, inkludert c-kit og PDGFR β, ved klinisk relevante konsentrasjoner.» Engelsk originaltekst: "Tivozanib is a tyrosine kinase inhibitor. In vitro cellular kinase assays demonstrated that tivozanib inhibits phosphorylation of vascular endothelial growth factor receptor (VEGFR)-1, VEGFR-2 and VEGFR-3 and inhibits other kinases including c-kit and PDGFR β at clinically relevant concentrations." ([DailyMed: Fotivda (tivozanib) prescribing information, AVEO Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de77155c-ecf2-4f15-9758-21d271449d83), versjon av 2026-11-11; hentet 2026-11-19). Ut fra generell kunnskap er tivozanib en hemmer av alle tre VEGF-reseptorene (VEGFR-1, -2 og -3, kodet av genene FLT1, KDR og FLT4). Farmakologidataene bekrefter at legemidlet hemmer disse tre reseptorene med lik potens.

VEGF-drevet angiogenese er viktig i biologien til livmorhalskreft, og antiangiogen behandling (bevacizumab) har dokumentert nytte ved livmorhalskreft. Dette gir et plausibelt, men ubekreftet grunnlag for at en VEGFR-hemmer kan ha effekt også ved endocervikalt karsinom.

Den høye TxGNN-scoren (0,998) er imidlertid utelukkende en beregningsbasert prediksjon. Ingen studier eller publikasjoner i dataene støtter den, og likheten med den opprinnelige indikasjonen er ikke vurdert.

De øvrige topp-10-prediksjonene gjelder sjeldne gynekologiske karsinomer (blant annet adenokarsinomer i livmorligamentet og sjeldne varianter av livmorhalskreft), alle med scorer rundt 0,998 og kun generell antiangiogen begrunnelse uten evidens.

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004131 | Fotivda | tivozanib | Carcinoma, Renal Cell | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (VEGFR-tyrosinkinasehemmer) |
| Myelosuppresjonsrisiko | Se pakningsvedlegg for advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegg for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegg for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se pakningsvedlegg for advarsler og forholdsregler |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (7 registrerte oppføringer i dataene; 4 med angitt alvorlighetsgrad):

- **Alvorlig (Major):** fenobarbital, johannesurt
- **Moderat:** riociguat, medroksyprogesteronacetat

Øvrige oppføringer gjelder legemidlets målproteiner (FLT1, KDR, FLT4) og er ikke interaksjoner i klinisk forstand.

Det foreligger ingen data om advarsler eller kontraindikasjoner fra pakningsvedlegg. Se pakningsvedlegget for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en beregningsmodell (L5) uten kliniske studier eller publikasjoner. I tillegg mangler sikkerhetsdata fra pakningsvedlegg.

<!-- review:begin no-lic-20261124b-tivozanib-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «I tillegg er den eneste norske godkjenningen kansellert, og sikkerhetsdata fra pakningsvedlegg mangler.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-tivozanib-1 -->

**For å gå videre kreves følgende:**
- Hente og analysere sikkerhetsinformasjon (advarsler og kontraindikasjoner) fra pakningsvedlegget
- Fullstendige mekanismedata (MOA) fra DrugBank
- Litteratur- og studiesøk spesifikt for tivozanib ved livmorhalskreft og andre gynekologiske karsinomer
- Vurdering av likhet med den opprinnelige indikasjonen og av administrasjonsvei
- Avklaring av markedsstatus i Norge

<!-- review:begin no-lic-20261124b-tivozanib-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av markedsstatus i Norge, siden godkjenningen er kansellert» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-tivozanib-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Fotivda (tivozanib) prescribing information, AVEO Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de77155c-ecf2-4f15-9758-21d271449d83) |
| 2026-11-24 | Rettet: «I tillegg er den eneste norske godkjenningen kansellert, og sikkerhetsdata fra pakningsvedlegg mangler.» → «I tillegg mangler sikkerhetsdata fra pakningsvedlegg.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av markedsstatus i Norge, siden godkjenningen er kansellert» → «Avklaring av markedsstatus i Norge» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

