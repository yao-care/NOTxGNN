---
layout: default
title: Laronidase
parent: Kun modellprediksjon (L5)
nav_order: 233
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Laronidase: predikert ny indikasjon Lysosomal lagringssykdom med skjelettaffeksjon (evidensnivå L4). Opprinnelig indikasjon: Mukopolysakkaridose I"
monitor_inn: "LARONIDASE"
predicted_indications: ["lysosomal storage disease with skeletal involvement", "Sanfilippo syndrome"]
---

# Laronidase
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Laronidase: Fra mukopolysakkaridose I til lysosomal lagringssykdom med skjelettaffeksjon
{: .text-alpha }

## Oppsummering i én setning

Laronidase er en rekombinant alfa-L-iduronidase (enzymerstatningsterapi) som opprinnelig brukes til behandling av **mukopolysakkaridose I (MPS I)**. TxGNN-modellen predikerer at legemidlet kan være virksomt ved **lysosomal lagringssykdom med skjelettaffeksjon** (score 0,9931). Det foreligger **ingen registrerte kliniske studier** og **4 publikasjoner** for denne indikasjonen, og indikasjonen overlapper i stor grad med den allerede godkjente. En andre prediksjon, **Sanfilippo syndrom**, er omtalt til slutt og har svakt mekanistisk grunnlag.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Mukopolysakkaridose I |
| Predikert ny indikasjon | Lysosomal lagringssykdom med skjelettaffeksjon |
| TxGNN-prediksjonsscore | 0,9931 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme fra legemiddeldatabasen er for øyeblikket ikke tilgjengelige. Basert på kjent informasjon er laronidase rekombinant alfa-L-iduronidase, som bryter ned glykosaminoglykanene dermatansulfat og heparansulfat. Effekten ved MPS I er dokumentert, og mekanistisk kan den være relevant for beslektede lysosomale lagringssykdommer.

Den predikerte indikasjonen er i hovedsak identisk med den godkjente MPS I-indikasjonen. MPS I (Hurler/Scheie) er en lysosomal lagringssykdom med betydelig skjelettinvolvering (dysostosis multiplex), så dette er ikke en reell ny bruk. En in vitro-studie (PMID 18758061) viser at laronidase tas opp av dyrkede fibroblaster og osteoblaster, noe som støtter en plausibel cellulær vei til benvev.

Intravenøs enzymerstatning har imidlertid kjent begrenset penetrasjon i avaskulær brusk og ben, så skjelettnytten forventes å være beskjeden. Evidensen for andre lysosomale sykdommer med skjelettaffeksjon er indirekte.

---

## Evidens fra kliniske studier

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Oversikt | Pediatric Endocrinology Reviews | MPS I skyldes mangel på alfa-L-iduronidase og gir opphopning av dermatan- og heparansulfat; spekteret går fra Hurler til Scheie. |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Oversikt | BioDrugs | Beskriver utviklingen av laronidase som enzymerstatning ved MPS I, med orphan drug-status. |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | In vitro-studie | Biological & Pharmaceutical Bulletin | Laronidase tas opp i fibroblaster og osteoblaster via mannose-6-fosfatreseptorer og transporteres til lysosomer. |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Kasuistikk | Pediatric Neurology | 6,5 års oppfølging av en gutt med Scheie syndrom på enzymerstatning; sykdommen progredierte likevel over tid. |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000477 | Aldurazyme | Ikke oppgitt | Mukopolysakkaridose I (status: kansellert) |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** To interaksjoner er registrert, begge av grad «mindre» (Minor): klorokin og prokain.

For øvrig sikkerhetsinformasjon, se pakningsvedlegget/preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den predikerte indikasjonen overlapper i stor grad med den allerede godkjente MPS I-indikasjonen og representerer ikke en reell ny bruk. Evidensen er på nivå L4 uten registrerte kliniske studier, og skjelettnytten av intravenøs behandling forventes å være begrenset. Den eneste norske godkjenningen er kansellert.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra legemiddeldatabasen
- Advarsler og kontraindikasjoner fra preparatomtalen
- Avklaring av hvorfor godkjenningen i Norge er kansellert
- Data på skjelettutfall (f.eks. leddbevegelighet, røntgen) ved ERT for å vurdere reell tilleggsverdi

---

## Tilleggsvurdering: Sanfilippo syndrom (rang 2)

TxGNN-score 0,9922, evidensnivå L4, anbefaling **Hold**. Ingen kliniske studier er registrert.

Sanfilippo syndrom (MPS III) skyldes mangel på andre enzymer i nedbrytningen av heparansulfat (SGSH, NAGLU, HGSNAT, GNS), ikke alfa-L-iduronidase. Laronidase kan derfor ikke erstatte det manglende enzymet. Kjernepatologien er nevrologisk, og intravenøs laronidase passerer ikke blod-hjerne-barrieren i meningsfull grad. Den høye scoren gjenspeiler trolig nærhet i nettverket innen MPS-familien snarere enn en reell terapeutisk sammenheng.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [15126990](https://pubmed.ncbi.nlm.nih.gov/15126990/) | 2004 | RCT (MPS I, placebokontrollert; indirekte) | J Pediatr | Pivotal fase 3-studie som bekrefter effekt og sikkerhet av laronidase ved MPS I. |
| [40830667](https://pubmed.ncbi.nlm.nih.gov/40830667/) | 2025 | RCT, fase III (MPS I; indirekte) | Sci Rep | Biosimilær laronidase sammenlignet med referanseproduktet for å opprettholde uGAG-nivåer ved MPS I. |
| [31020996](https://pubmed.ncbi.nlm.nih.gov/31020996/) | 2019 | Systematisk oversikt | J Inherit Metab Dis | Begrenset data for å vurdere reell effekt av ERT ved MPS I. |
| [32340185](https://pubmed.ncbi.nlm.nih.gov/32340185/) | 2020 | Oversikt | Int J Mol Sci | Effekt og begrensninger ved intravenøs ERT ved MPS; motstridende data etter markedsføring. |
| [15794739](https://pubmed.ncbi.nlm.nih.gov/15794739/) | 2005 | Oversikt | Expert Opin Pharmacother | De første fem årene med klinisk erfaring med laronidase ved MPS I. |
| [33139350](https://pubmed.ncbi.nlm.nih.gov/33139350/) | 2021 | Kohort | Arch Dis Child | Tid til behandling er forbedret over 15 år, men ikke tid til diagnose (MPS I). |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Oversikt | BioDrugs | Utvikling av laronidase ved MPS I. |
| [23251908](https://pubmed.ncbi.nlm.nih.gov/23251908/) | 2012 | Prekliniske (in vitro) | Acta Biochim Pol | Sammenligning av siRNA-basert substratreduksjon og ERT i cellekultur; laronidase var ikke cytotoksisk. |

All litteratur gjelder MPS I og er indirekte evidens for Sanfilippo syndrom.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

