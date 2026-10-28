---
layout: default
title: Vonicog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 454
evidence_level: L5
indication_count: 8
monitor_inn: "VONICOG ALFA"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "hemophilia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
last_modified_at: 2026-10-28
description: "Vonicog Alfa: predikert ny indikasjon Primær frigjøringsforstyrrelse i blodplater (evidensnivå L5). Opprinnelig indikasjon: von Willebrands sykdom"
---

# Vonicog Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **8** stk.
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

## Vonicog alfa: Fra von Willebrands sykdom til primær frigjøringsforstyrrelse i blodplater
{: .text-alpha }

## Oppsummering

Vonicog alfa er rekombinant von Willebrand-faktor (rVWF), opprinnelig godkjent for behandling av von Willebrands sykdom.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **primær frigjøringsforstyrrelse i blodplater**,
men det finnes **ingen kliniske studier** og **ingen publikasjoner** som direkte omhandler denne sykdommen. Prediksjonen bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | von Willebrands sykdom |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse i blodplater |
| TxGNN-prediksjonsscore | 0,9998 |
| Evidensnivå | L5 |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor kan denne prediksjonen være rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelige i de innsamlede dataene. Vonicog alfa er rekombinant von Willebrand-faktor, som medierer blodplatenes adhesjon og aggregasjon ved karskade og bærer faktor VIII. Effekten er dokumentert ved von Willebrands sykdom.

Primær frigjøringsforstyrrelse i blodplater er en iboende funksjonsfeil i blodplatene (defekt granulefrigjøring). Tilførsel av ekstern VWF forventes derfor ikke å korrigere denne defekten. Den høye modellscoren er en nettverksbasert prediksjon uten støtte i studier eller litteratur, og den mekanistiske sammenhengen er svak.

### Andre predikerte indikasjoner (alle uten direkte klinisk støtte)

| Rangering | Sykdom | Score | Evidensnivå | Vurdering |
|------|------|------|------|------|
| 2 | Glanzmanns trombasteni | 0,9998 | L5 | Skyldes mangel på/dysfunksjon av integrin αIIbβ3, som VWF ikke erstatter. Blodplatetransfusjon og rekombinant FVIIa er etablert behandling. |
| 3 | Hemofili | 0,9995 | L5* | VWF stabiliserer endogen FVIII, noe som gir en plausibel mekanistisk kobling til hemofili A. Eksisterende litteratur gjelder von Willebrands sykdom, ikke hemofili. |
| 4 | Scotts syndrom | 0,9995 | L5 | Defekt i fosfatidylserin-eksponering (TMEM16F/ANO6). VWF adresserer ikke denne veien. |
| 5 | Ervervet koagulasjonsfaktormangel | 0,9994 | L5 | Kategorien er heterogen. Ervervet von Willebrand-syndrom kan teoretisk respondere, men ingen data støtter det. |
| 6 | Blødningsdiatese ved kollagenreseptordefekt | 0,9992 | L5 | Defekten ligger på blodplatesiden og omgås neppe av VWF. |
| 7 | Hemoragisk lidelse ved konstitusjonell trombocytopeni | 0,9992 | L5 | VWF korrigerer ikke blodplatetallet. Effekten er teoretisk. |
| 8 | «Flood factor deficiency» | 0,9990 | L5 | Uklar term, kan være en merkingsfeil i data. Bør verifiseres i kildeontologien. |

*Pakken angir L4 for hemofili, men ingen av de siterte studiene undersøker hemofili direkte. Etter reglene settes nivået derfor til L5.

---

## Klinisk studieevidens

Foreløpig er det ikke registrert relevante kliniske studier for den predikerte indikasjonen.

---

## Litteraturevidens

Foreløpig er det ingen relevant litteratur for den predikerte indikasjonen (primær frigjøringsforstyrrelse i blodplater).

Litteratur funnet for rangert nr. 3 (hemofili) gjelder i realiteten den allerede godkjente indikasjonen, von Willebrands sykdom:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [35439298](https://pubmed.ncbi.nlm.nih.gov/35439298/) | 2022 | Fase 3-studie | Blood | Profylakse med rVWF hos voksne med alvorlig von Willebrands sykdom |
| [37332615](https://pubmed.ncbi.nlm.nih.gov/37332615/) | 2023 | Farmakokinetisk/farmakodynamisk sammenligning | Journal of Blood Medicine | Sammenligning av rekombinant og plasmaavledet VWF ved type 3 von Willebrands sykdom |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Oversikt | Current Pharmaceutical Design | Nye hemostatiske midler og perioperative hensyn |
| [37926687](https://pubmed.ncbi.nlm.nih.gov/37926687/) | 2024 | Laboratoriestudie og spørreundersøkelse | Haemophilia | Hvordan laboratorier analyserer rekombinante og plasmaavledne VWF-produkter |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004454 | Veyvondi | – | von Willebrands sykdom |

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Den predikerte indikasjonen støttes kun av modellscore (evidensnivå L5), uten kliniske studier eller litteratur. Den mekanistiske sammenhengen er svak, siden defekten ligger i blodplatene og ikke i mangel på VWF.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA)
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner)
- Prekliniske eller kliniske data som direkte undersøker blodplatefrigjøringsforstyrrelser
- Eventuelt en mer relevant kandidatindikasjon (for eksempel ervervet von Willebrand-syndrom) som bør vurderes separat
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

