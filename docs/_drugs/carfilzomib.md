---
layout: default
title: Carfilzomib
parent: Kun modellprediksjon (L5)
nav_order: 85
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
description: "Carfilzomib: predikert ny indikasjon CMM7 (evidensnivå L5). Opprinnelig indikasjon: Multippelt myelom"
monitor_inn: "CARFILZOMIB"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
---

# Carfilzomib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

## Karfilzomib: Fra multippelt myelom til CMM7 (familiært kutant malignt melanom)
{: .text-alpha }

## Sammendrag

Karfilzomib er en proteasomhemmer som opprinnelig brukes til behandling av **multippelt myelom**.
TxGNN-modellen (deep learning) forutsier at legemidlet kan ha effekt ved **CMM7** (antatt en subtype av familiært kutant malignt melanom), men dette er kun en prediksjon fra modellen og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.
Det finnes **ingen registrerte kliniske studier** og **ingen publikasjoner** for denne spesifikke indikasjonen. For den bredere diagnosen melanom finnes det kun **4 prekliniske eller beregningsbaserte publikasjoner**.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Multippelt myelom |
| Predikert ny indikasjon | CMM7 |
| TxGNN-prediksjonsscore | 0.9937 |
| Evidensnivå | L5 (kun modellprediksjon). For «melanom» generelt: L4 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold (vent) |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelig i de innsamlede dataene. Basert på kjent informasjon er karfilzomib en proteasomhemmer. Effekten ved multippelt myelom er godt dokumentert, og mekanistisk kan den tenkes å være relevant for melanom.

Et mulig resonnement er at proteasomhemming gir proteotoksisk stress og apoptose i kreftceller. Dette er likevel ikke testet for CMM7. Subtypen antas å være en familiær form for kutant malignt melanom, og det finnes ingen direkte evidens.

Prediksjonene med nest høyest score gjelder pediatrisk leptomeningealt melanom, epiteloid uveal melanom og vulvamelanom. De er også kun modellprediksjoner uten studier eller litteratur. Uvealt og mukosalt melanom er biologisk forskjellige fra kutant melanom, så funn fra kutane melanomcellelinjer kan ikke overføres direkte. For leptomeningealt melanom er det også uavklart om karfilzomib når sentralnervesystemet.

For den bredere diagnosen **melanom** (score 0,9903) finnes det prekliniske data. Her er evidensen indirekte og består av cellestudier og beregningsstudier.

---

## Klinisk studieevidens

Det finnes for tiden ingen relaterte kliniske studier registrert, verken for CMM7 eller for melanom generelt.

---

## Litteraturevidens

Det finnes ingen litteratur for CMM7. Tabellen nedenfor viser litteratur for den bredere diagnosen melanom.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro, preklinisk | Biology | Karfilzomib kombinert med bortezomib økte apoptose (aktivering av kaspase 3, 8, 9 og 12) i B16-F1 museceller fra melanom |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Beregningsbasert (docking/dynamikk) | J Biomol Struct Dyn | Virtuell screening for gjenbruk av legemidler mot kinasemål ved ti krefttyper, inkludert melanom |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preklinisk grunnforskning (indirekte) | Mol Cancer Res | ZFAND2A (AIRAP) som regulator av celleoverlevelse i humant melanom, via E3-ligasen cIAP2 |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preklinisk grunnforskning (indirekte) | Matrix Biol | Bortezomib og karfilzomib aktiverer NF-κB og øker uttrykk av heparanase, noe som er assosiert med en mer aggressiv tumorfenotype |

Bare den første studien er direkte relevant for karfilzomib ved melanom, og den bruker en museuellelinje. Den siste studien peker på en mulig bekymring: proteasomhemmere kan indusere heparanase.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003790 | Kyprolis | Ikke oppgitt | Multippelt myelom |

Legemidlet er markedsført i Norge, og 1 av 1 markedsføringstillatelse er gyldig.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet terapi (proteasomhemmer), antineoplastisk |
| Myelosuppresjonsrisiko | Se pakningsvedlegget for advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Følg gjeldende regelverk for håndtering av cytotoksiske legemidler |

---

## Sikkerhetsvurderinger

Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner) er ikke tilgjengelig i de innsamlede dataene. Se pakningsvedlegget for sikkerhetsinformasjon.

**Legemiddelinteraksjoner:** Interaksjonssøket ble gjennomført og ga 100 registrerte interaksjoner. Blant de 20 som er gjennomgått, er følgende klassifisert som **alvorlige (Major)**:

- Anabole steroider: oksandrolon, oksymetolon, stanozolol
- Deferipron
- Samarium (153Sm) lexidronam
- Blodkoagulasjonsrelaterte midler: rekombinant antihemofilifaktor, aminokapronsyre, humant von Willebrand-faktor, avatrombopag, humant C1-esterasehemmer, rekombinant koagulasjonsfaktor VIIa, koagulasjonsfaktor X, konestat alfa

Interaksjoner klassifisert som **moderate** omfatter metronidazol, naltrekson, rosuvastatin, simvastatin, tinidazol, palifermin og strontiumklorid Sr-89.

---

## Konklusjon og neste steg

**Beslutning: Hold (vent)**

**Begrunnelse:**
CMM7-prediksjonen bygger kun på TxGNN-modellen (deep learning) (L5), uten kliniske studier eller litteratur, og scoren kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. For melanom generelt finnes det bare indirekte prekliniske data. Legemidlet er markedsført i Norge med 1 gyldig markedsføringstillatelse, men sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre trengs følgende:**
- Sikkerhetsdata fra preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (MOA) fra DrugBank
- Bekreftelse av hva CMM7 er, og av biologisk likhet med multippelt myelom
- Prekliniske data i relevante melanommodeller (humane cellelinjer, in vivo) med klinisk oppnåelige doser
- Vurdering av administrasjonsvei og eventuell penetrasjon til sentralnervesystemet, særlig for leptomeningealt melanom
- Avklaring av regulatorisk status i Norge, siden eneste godkjenning er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

