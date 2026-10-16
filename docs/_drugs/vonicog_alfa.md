---
layout: default
title: Vonicog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vonicog Alfa: predikert ny indikasjon Primær frigjøringsforstyrrelse i blodplater (evidensnivå L5). Opprinnelig indikasjon: von Willebrands sykdom"
---

# Vonicog Alfa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Vonicog alfa: Fra von Willebrands sykdom til primær frigjøringsforstyrrelse i blodplater

## Oppsummering i én setning

Vonicog alfa er et rekombinant von Willebrand-faktor-preparat (rVWF) som opprinnelig brukes til behandling av **von Willebrands sykdom**.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **primær frigjøringsforstyrrelse i blodplater** (primary release disorder of platelets).
Det finnes **ingen kliniske studier** og **ingen publikasjoner** som direkte støtter denne prediksjonen, så den er foreløpig en ren modellprediksjon.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | von Willebrands sykdom |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse i blodplater |
| TxGNN-prediksjonsscore | 99,98 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (opphevet) |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold (avvent) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige fra legemiddeldatabasen. Basert på kjent informasjon er vonicog alfa rekombinant von Willebrand-faktor (VWF). VWF formidler adhesjon og aggregasjon av blodplater og stabiliserer i tillegg endogen faktor VIII. Effekten ved von Willebrands sykdom er godt dokumentert.

Primær frigjøringsforstyrrelse i blodplater er en iboende defekt i blodplatenes lagrings- og sekresjonsfunksjon. Siden feilen sitter i selve blodplaten, forventes det ikke at tilførsel av eksogen VWF kan korrigere den. Koblingen er derfor basert utelukkende på nærhet i kunnskapsgrafen (nettverksprediksjon), uten kliniske data eller litteratur som støtte.

Den høye scoren bør tolkes med forsiktighet. Flere av de øvrige topp-10-prediksjonene (Glanzmanns trombasteni, Scotts syndrom, defekt kollagenreseptor, konstitusjonell trombocytopeni) gjelder også blodplatedefekter der mekanismen er svak. Blant de øvrige prediksjonene er særlig tre verdt å nevne:

- **Hemofili** (score 99,95 %, evidensnivå L4): Det finnes en indirekte kobling via VWFs stabilisering av faktor VIII, men de fire funnede publikasjonene gjelder von Willebrands sykdom og ikke hemofili.
- **Pseudo-von Willebrands sykdom**: Biologisk plausibel, men VWF-tilskudd kan ha begrenset effekt eller forverre klaring av blodplater. Vanlig behandling er blodplatetransfusjon.
- **X-bundet von Willebrands sykdom**: Ligger tett opp mot den godkjente indikasjonen og kan heller sees som en utvidelse av eksisterende indikasjon enn som reell repurposing.

---

## Klinisk studiedokumentasjon

Det er for tiden ingen relaterte kliniske studier registrert for den predikerte indikasjonen.

---

## Litteraturdokumentasjon

Det er for tiden ingen relevant litteratur tilgjengelig for den predikerte indikasjonen.

*Merk:* For hemofili (rang 4) ble det funnet fire publikasjoner. De gjelder von Willebrands sykdom og gir kun indirekte støtte:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [35439298](https://pubmed.ncbi.nlm.nih.gov/35439298/) | 2022 | Fase 3-studie | Blood | Profylakse med rVWF hos voksne med alvorlig von Willebrands sykdom |
| [37332615](https://pubmed.ncbi.nlm.nih.gov/37332615/) | 2023 | PK/PD-sammenligning | Journal of Blood Medicine | Sammenligning av rekombinant og plasmaavledet VWF ved VWD type 3 |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Oversikt | Current Pharmaceutical Design | Nye hemostatika og perioperative hensyn for anestesi |
| [37926687](https://pubmed.ncbi.nlm.nih.gov/37926687/) | 2024 | Laboratoriestudie/undersøkelse | Haemophilia | Hvordan laboratorier analyserer rekombinant og plasmaavledet VWF |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004454 | Veyvondi | Ikke oppgitt | von Willebrands sykdom |

Godkjenningen er avregistrert (opphevet), og det finnes ingen gyldige markedsføringstillatelser.

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold (avvent)**

**Begrunnelse:**
Prediksjonen bygger kun på nettverksnærhet i kunnskapsgrafen (evidensnivå L5), uten kliniske studier eller litteratur. Mekanismen er svak fordi defekten ligger i blodplaten og ikke i mangel på VWF. I tillegg er den norske godkjenningen avregistrert.

**For å gå videre kreves følgende:**
- Informasjon om virkningsmekanisme (MOA) fra legemiddeldatabasen
- Pakningsvedlegg med advarsler og kontraindikasjoner fra godkjenningsmyndigheten (nødvendig før sikkerhetsscreening)
- Prekliniske eller mekanistiske studier som viser at VWF-tilførsel kan gi nytte ved den predikerte blodplatesykdommen
- Vurdering av om prediksjoner nær den opprinnelige indikasjonen (X-bundet VWD) og hemofili bør prioriteres foran blodplatedefektene
- Avklaring av legemidlets markedsstatus og tilgjengelighet i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

