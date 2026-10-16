---
layout: default
title: Pentosan Polysulfate
parent: Kun modellprediksjon (L5)
nav_order: 321
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Pentosan Polysulfate: predikert ny indikasjon Primær frigjøringsforstyrrelse i blodplater (evidensnivå L5). Opprinnelig indikasjon: Interstitiell cystitt"
---

# Pentosan Polysulfate
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

# Pentosanpolysulfat: Fra interstitiell cystitt til primær frigjøringsforstyrrelse i blodplater

## Oppsummering

Pentosanpolysulfat er et sulfatert polysakkarid som opprinnelig ble godkjent for behandling av **interstitiell cystitt**. TxGNN-modellen predikerer at legemidlet kan være effektivt ved **primær frigjøringsforstyrrelse i blodplater** (primary release disorder of platelets), men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er ren modellbasert, og mekanistiske vurderinger tyder på at effekten kan være motsatt av ønsket.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Interstitiell cystitt |
| Predikert ny indikasjon | Primær frigjøringsforstyrrelse i blodplater |
| TxGNN-prediksjonsscore | 99,71 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalte/avregistrerte godkjenninger (ingen gyldig godkjenning) |
| Antall godkjenninger | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige. Basert på kjent informasjon er pentosanpolysulfat et sulfatert polysakkarid med svak heparinlignende antikoagulerende og antitrombotisk aktivitet. Effekten ved interstitiell cystitt er knyttet til en annen virkning (beskyttelse av blæreslimhinnen), og denne har ingen åpenbar sammenheng med blodplatefunksjon.

En frigjøringsforstyrrelse i blodplater er en blødningsforstyrrelse. Et middel med antikoagulerende egenskaper ville teoretisk forventes å forverre blødningstendensen, ikke behandle den. Den høye TxGNN-scoren (0,997) er en beregnet prediksjon uten klinisk støtte, og effektretningen er trolig motsatt av terapeutisk nytte.

To andre prediksjoner med lignende mønster er også identifisert:

| Rang | Predikert sykdom | TxGNN-score | Vurdering |
|------|------|------|------|
| 2 | Glanzmanns trombasteni | 99,65 % | Skyldes mangel på eller dysfunksjon av integrin αIIbβ3 (GPIIb/IIIa). Pentosanpolysulfat har ingen kjent mekanisme som gjenoppretter reseptoren, og den antikoagulerende effekten kan forverre blødning. Sikkerhetsbekymring snarere enn terapeutisk rasjonale. |
| 3 | Pseudo-von Willebrands sykdom | 99,62 % | Skyldes økt GPIbα-binding til von Willebrand-faktor. Teoretisk kan et polyanionisk stoff interagere med von Willebrand-faktor eller blodplateproteiner, men det finnes ingen evidens for korrigerende effekt, og blødningsrisikoen er økt. |

Alle tre har evidensnivå L5 og anbefalingen Hold.

---

## Klinisk studieevidens

Foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004246 | Elmiron | – | Interstitiell cystitt |

Godkjenningen har status avregistrert/tilbakekalt, og det finnes ingen gyldige godkjenninger i Norge.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgraf (ikke fra preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter legemidlet til kontraindikasjon ved leversykdom, gallblæresykdom, trombocytopeni, blodkoagulasjonssykdom, hemofili og heparinindusert trombocytopeni. Flere av disse overlapper direkte med de predikerte blødnings- og blodplateforstyrrelsene.
- **Legemiddelinteraksjoner:** Totalt 58 interaksjoner er registrert. De viktigste, alle av moderat alvorlighetsgrad, er med acetylsalisylsyre, warfarin, apixaban, edoksaban, betriksaban, klopidogrel, cilostazol, dipyridamol, abciksimab, alteplase, bivalirudin, kangrelor, dalteparin, defibrotid, kaplacizumab, antitrombin III, anistreplase, ibritumomab tiuxetan og tositumomab. Mønsteret er additiv blødningsrisiko sammen med antikoagulantia, platehemmere og trombolytika.

Informasjon fra preparatomtale (advarsler og kontraindikasjoner) mangler i de innsamlede dataene og må innhentes.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene bygger kun på en grafmodell uten kliniske studier eller litteratur. Legemidlets antikoagulerende egenskaper og kontraindikasjoner ved blødnings- og blodplatesykdommer taler mot terapeutisk nytte, og godkjenningen i Norge er avregistrert.

**For å gå videre kreves følgende:**
- Sikkerhetsinformasjon fra preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Prekliniske eller mekanistiske data som viser en eventuell gunstig effekt på blodplatefunksjon
- Vurdering av om retningen på effekten er forenlig med behandling, gitt økt blødningsrisiko
- Avklaring av doseform og administrasjonsvei for den nye indikasjonen
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

