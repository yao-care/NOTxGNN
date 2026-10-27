---
layout: default
title: Miglustat
parent: Kun modellprediksjon (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Miglustat: predikert ny indikasjon Tay-Sachs sykdom (evidensnivå L5). Opprinnelig indikasjon: Gauchers sykdom"
monitor_inn: "MIGLUSTAT"
predicted_indications: ["autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease", "Krabbe disease", "metachromatic leukodystrophy", "Wolman disease with hypolipoproteinemia and acanthocytosis", "encephalopathy due to prosaposin deficiency", "Tay-Sachs disease", "benign neoplasm of adrenal gland", "recessive X-linked ichthyosis", "fatty acid hydroxylase-associated neurodegeneration"]
---

# Miglustat
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

## Miglustat: Fra Gauchers sykdom til Tay-Sachs sykdom
{: .text-alpha }

## Oppsummering

Miglustat brukes opprinnelig til behandling av Gauchers sykdom, og i tillegg til Pompes sykdom (glykogenlagringssykdom type II, i kombinasjon med enzymerstatning) og Niemann-Picks sykdom.
TxGNN-modellen forutsier at legemidlet kan ha effekt på **Tay-Sachs sykdom** (rangert som nr. 7 av de ti øverste prediksjonene, men den eneste med faktisk klinisk dokumentasjon),
og for øyeblikket finnes det **4 kliniske studier** og **11 publikasjoner** i datagrunnlaget. Effekten på nevrologiske endepunkter er foreløpig uavklart.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Gauchers sykdom |
| Predikert ny indikasjon | Tay-Sachs sykdom (valgt fordi den er den eneste av de ti toppprediksjonene med kliniske data; rang 1 i modellen er «autosomal ichthyosis syndrome with fatal disease course», kun modellprediksjon) |
| TxGNN-prediksjonsscore | 99,75 % (for Tay-Sachs; 99,83 % for rang 1) |
| Evidensnivå | L1 (formelt, basert på høyeste studiedesign; se merknad under) |
| Status på det norske markedet | ✗ Kun kansellerte godkjenninger |
| Antall godkjenninger | 5 (alle kansellerte) |
| Anbefalt beslutning | Hold |

**Merknad om evidensnivå:** L1 gjenspeiler her det høyeste studiedesignnivået som finnes, ikke bekreftet effekt. Fase 3-studiene er små PK-/sikkerhets- eller kartleggingsstudier, og to av dem ble avsluttet tidlig.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelige i datagrunnlaget. Ut fra kjent informasjon hemmer miglustat glukosylceramid-syntase (UGCG), enzymet som starter syntesen av de fleste glykosfingolipider. Dette er prinsippet bak substratreduksjonsterapi.

Tay-Sachs sykdom (GM2-gangliosidose) skyldes mangel på enzymet HEXA, som fører til opphopning av GM2-gangliosid i nerveceller. Ved Gauchers sykdom er problemet opphopning av glukosylceramid. Begge er lysosomale lagringssykdommer innen samme glykosfingolipid-vei. Ved å redusere syntesen oppstrøms kan mengden substrat som må brytes ned, bli mindre. Miglustat passerer dessuten blod-hjerne-barrieren, noe som er viktig siden Tay-Sachs først og fremst rammer sentralnervesystemet.

Begrunnelsen er altså biologisk sammenhengende. Klinisk nytte er likevel ikke påvist: en case-studie av infantil Tay-Sachs viste at behandlingen ikke stoppet nevrologisk forverring, selv om legemiddelkonsentrasjonen i spinalvæske var betydelig.

Øvrige toppprediksjoner (f.eks. Krabbe, metakromatisk leukodystrofi, prosaposin-mangel) har en mulig, men indirekte mekanistisk begrunnelse og ingen kliniske data. Prediksjoner som kolesterylester-lagringssykdom, Wolmans sykdom, godartet binyresvulst og X-bundet ichthyose har svak eller ingen mekanistisk kobling og er sannsynligvis artefakter fra kunnskapsgrafen.

---

## Klinisk studiedokumentasjon

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00672022](https://clinicaltrials.gov/study/NCT00672022) | Fase 3 | Fullført | 10 | Farmakokinetikk, sikkerhet og toleranse av miglustat ved infantil GM2-gangliosidose; liten studie som sier mer om sikkerhet og dosering enn effekt |
| [NCT02030015](https://clinicaltrials.gov/study/NCT02030015) | Fase 4 | Avsluttet | 16 | Syner-G: miglustat kombinert med ketogen diett ved gangliosidoser; kombinasjonsregime, tidlig avslutning begrenser tolkningen |
| [NCT00418847](https://clinicaltrials.gov/study/NCT00418847) | Fase 2 | Fullført | 5 | Farmakokinetikk og toleranse ved juvenil GM2-gangliosidose; svært liten studie |
| [NCT03822013](https://clinicaltrials.gov/study/NCT03822013) | Fase 3 | Avsluttet | 30 | Kartlegging av terapeutiske effekter på nevrologiske og systemiske symptomer ved infantil Sandhoff/Tay-Sachs; avslutning og observasjonsdesign gir lavere evidensvekt |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [19346952](https://pubmed.ncbi.nlm.nih.gov/19346952/) | 2009 | RCT | Genetics in Medicine | 12 måneders randomisert kontrollert studie med 24 måneders forlenget behandling av miglustat ved senutviklet Tay-Sachs; vurderer sikkerhet og effekt |
| [37209042](https://pubmed.ncbi.nlm.nih.gov/37209042/) | 2023 | Systematisk oversikt | European Journal of Neurology | Vurderer effekt og sikkerhet av miglustat ved GM2-gangliosidose etter tidligere inkonsistente resultater |
| [42794762](https://pubmed.ncbi.nlm.nih.gov/42794762/) | 2026 | Oversikt | Int J Mol Sci | Biologisk begrunnelse, klinisk evidens og grenser for reposisjonering av miglustat ved nevronopatiske lysosomale lagringssykdommer |
| [16434676](https://pubmed.ncbi.nlm.nih.gov/16434676/) | 2006 | Kasuistikk | Neurology | Substratreduksjon hos to pasienter med infantil Tay-Sachs stoppet ikke nevrologisk forverring, men ga betydelig konsentrasjon i spinalvæske og forhindret makrocefali |
| [30743792](https://pubmed.ncbi.nlm.nih.gov/30743792/) | 2009 | Oversikt | Expert Rev Endocrinol Metab | Substratreduksjonsterapi med miglustat ved glykosfingolipid-lagringssykdommer som rammer hjernen |
| [16763917](https://pubmed.ncbi.nlm.nih.gov/16763917/) | 2006 | Oversikt | J Inherit Metab Dis | Substratreduksjonsterapi ved glykosfingolipid-lagringssykdommer |
| [30524313](https://pubmed.ncbi.nlm.nih.gov/30524313/) | 2018 | Oversikt | Frontiers in Physiology | Nye tilnærminger til behandling av Tay-Sachs sykdom |
| [28476546](https://pubmed.ncbi.nlm.nih.gov/28476546/) | 2017 | Naturhistorie/kohort | Mol Genet Metab | Tidslinje for kliniske endringer ved infantile gangliosidoser; ingen godkjente behandlinger, miglustat begrenset av gastrointestinale bivirkninger |
| [18618288](https://pubmed.ncbi.nlm.nih.gov/18618288/) | 2008 | Pilotstudie | J Inherit Metab Dis | Nevrokognitiv testing ved senutviklet Tay-Sachs som mulig effektmål |
| [12808890](https://pubmed.ncbi.nlm.nih.gov/12808890/) | 2003 | Legemiddelprofil | Curr Opin Investig Drugs | Profil av miglustat, utviklet for Gauchers sykdom og under utvikling for Tay-Sachs, Fabry og Niemann-Pick type C |

---

## Informasjon om det norske markedet

Alle fem godkjenninger er kansellerte, og det finnes ingen gyldige godkjenninger i dag.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000435 | Zavesca | – | Gauchers sykdom; Niemann-Picks sykdom |
| EMEA/H/C/004016 | Yargesa | – | Gauchers sykdom |
| EMEA/H/C/004904 | Miglustat Dipharma | – | Gauchers sykdom |
| EMEA/H/C/004366 | Miglustat Gen.Orph | – | Gauchers sykdom |
| EMEA/H/C/005695 | Opfolda | – | Glykogenlagringssykdom type II |

---

## Sikkerhetshensyn

- **Kontraindikasjoner fra kunnskapsgrafen** (ikke fra preparatomtale): perifer nervesystemsykdom, perifer nevropati og nedsatt nyrefunksjon.
- **Legemiddelinteraksjoner:** Imiglucerase (moderat interaksjon, ifølge DDInter). I tillegg er UGCG (glukosylceramid-syntase) identifisert som farmakologisk mål, noe som er selve virkningsmekanismen og ikke en klinisk interaksjon.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Miglustat har en biologisk sammenhengende begrunnelse for Tay-Sachs og noe klinisk dokumentasjon, men studiene er små, to ble avsluttet tidlig, og nevrologisk effekt er uavklart. I tillegg har legemidlet ingen gyldig godkjenning i Norge, og sikkerhetsdata fra preparatomtalen mangler. Øvrige toppprediksjoner er kun modellbaserte (L5).

**For å gå videre kreves følgende:**
- Innhente og analysere preparatomtale (advarsler og kontraindikasjoner), noe som er en blokkerende datamangel for sikkerhetsvurderingen
- Detaljerte data om virkningsmekanisme (f.eks. fra DrugBank)
- Kritisk gjennomgang av resultatene fra RCT-en (PMID 19346952) og den systematiske oversikten (PMID 37209042) for å avklare effekt på nevrologiske endepunkter
- Vurdere regulatorisk vei, siden alle norske/EU-godkjenninger er kansellert
- Sikkerhetsplan for pasienter med perifer nevropati eller nedsatt nyrefunksjon
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

