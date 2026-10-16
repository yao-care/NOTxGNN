---
layout: default
title: Efmoroctocog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Efmoroctocog Alfa: predikert ny indikasjon Pseudo-von Willebrands sykdom (evidensnivå L5). Opprinnelig indikasjon: Hemofili A"
monitor_inn: "EFMOROCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "hemophilia A with vascular abnormality", "thrombotic thrombocytopenic purpura"]
---

# Efmoroctocog Alfa
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

# Efmoroctocog alfa: Fra hemofili A til pseudo-von Willebrands sykdom

## Oppsummering i én setning

Efmoroctocog alfa er et rekombinant FVIII-Fc-fusjonsprotein (Elocta) som opprinnelig ble brukt til behandling av **hemofili A**. TxGNN-modellen forutsier at det kan ha effekt ved **pseudo-von Willebrands sykdom**, men det finnes **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen bygger kun på modellen (evidensnivå L5).

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hemofili A |
| Predikert ny indikasjon | Pseudo-von Willebrands sykdom |
| TxGNN-prediksjonsscore | 99,997 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun tilbakekalte/avsluttede autorisasjoner (Cancelled only) |
| Antall autorisasjoner | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Detaljerte data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelige. Basert på kjent informasjon er efmoroctocog alfa et rekombinant FVIII som er koblet til en Fc-del for lengre halveringstid. Effekten ved hemofili A er godt dokumentert, fordi legemidlet erstatter manglende faktor VIII.

Pseudo-von Willebrands sykdom er en blodplatesykdom som skyldes en gain-of-function-mutasjon i GP1BA, noe som øker blodplatenes affinitet for VWF. FVIII-erstatning korrigerer ikke denne blodplatedefekten. Koblingen hviler derfor kun på TxGNN-grafprediksjonen og har ingen klar mekanistisk begrunnelse.

Heller ikke de øvrige topp-10-prediksjonene har klinisk støtte. De fleste gjelder blodplate- eller VWF-relaterte forstyrrelser der FVIII-erstatning ikke gir noen åpenbar farmakologisk effekt:

| Rang | Predikert sykdom | TxGNN-score | Vurdering |
|---|---|---|---|
| 1 | Pseudo-von Willebrands sykdom | 99,997 % | Ingen klar mekanistisk kobling |
| 2 | Primær frisettingsforstyrrelse i blodplater | 99,997 % | Sannsynligvis felles «blødningsforstyrrelse»-naboer i grafen |
| 3 | Glanzmanns trombasteni | 99,995 % | Aggregasjonsdefekt, FVIII løser den ikke |
| 4 | Scotts syndrom | 99,969 % | Kun indirekte og spekulativ kobling |
| 5 | Ervervet koagulasjonsfaktormangel | 99,952 % | Biologisk mest plausibel, men hemmende autoantistoffer kan nøytralisere FVIII |
| 6 | Blødningsdiatese ved kollagenreseptordefekt | 99,921 % | Ingen mekanistisk basis |
| 7 | Hemorragisk forstyrrelse ved konstitusjonell trombocytopeni | 99,917 % | Ingen klar farmakologisk begrunnelse |
| 8 | Føtal og neonatal alloimmun trombocytopeni | 99,845 % | Immunmediert, FVIII virker ikke |
| 9 | Hemofili A med vaskulær abnormitet | 99,779 % | Undergruppe av godkjent bruk, ikke reell repurposing |
| 10 | Trombotisk trombocytopenisk purpura | 99,724 % | Kan være protrombotisk, sikkerhetsbekymring |

---

## Klinisk studiedokumentasjon

Det er for tiden ingen relaterte kliniske studier registrert.

---

## Litteraturdokumentasjon

Det er for tiden ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Autorisasjonsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003964 | Elocta | – | Hemofili A |

Autorisasjonen har status som avsluttet/tilbakekalt, og det finnes ingen gyldige autorisasjoner for øyeblikket.

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

Det finnes ingen registrerte legemiddelinteraksjoner i de innsamlede dataene. Det er likevel verdt å merke seg at for trombotisk trombocytopenisk purpura (TTP) kan FVIII-tilførsel teoretisk være protrombotisk.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene støttes kun av TxGNN-modellen (L5), uten kliniske studier eller litteratur, og de fleste mangler en plausibel mekanistisk kobling til FVIII-erstatning. I tillegg har produktet kun avsluttede autorisasjoner i Norge.

**For å gå videre kreves følgende:**
- Detaljerte data om virkningsmekanisme (MOA)
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Systematisk litteratur- og studiesøk for «ervervet koagulasjonsfaktormangel», som er den biologisk mest plausible kandidaten
- Avklaring av tilgjengelighet, siden markedsstatus er «Cancelled only»
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

