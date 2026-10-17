---
layout: default
title: Glycine
parent: Kun modellprediksjon (L5)
nav_order: 195
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Glycine: predikert ny indikasjon Sykdom i nesehulen (nasal cavity disease) (evidensnivå L5). Opprinnelig indikasjon: Lønnesirupsykdom (Maple Syrup Urine Disease)"
monitor_inn: "glycine"
predicted_indications: ["acute laryngopharyngitis"]
---

# Glycine
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

# Glycin: Fra Lønnesirupsykdom (MSUD) til sykdom i nesehulen

## Oppsummering i én setning

Glycin (Maapliv) var opprinnelig godkjent i Europa for behandling av lønnesirupsykdom (Maple Syrup Urine Disease, MSUD). TxGNN-modellen forutsier at glycin kan ha effekt ved **sykdom i nesehulen**, men det finnes foreløpig **ingen relevante kliniske studier** og **ingen relevant litteratur** som støtter denne retningen. Forutsigelsen bygger kun på en modellberegning.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Lønnesirupsykdom (Maple Syrup Urine Disease) |
| Forutsagt ny indikasjon | Sykdom i nesehulen (nasal cavity disease) |
| TxGNN-prediksjonsscore | 99,85 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte (trukkede) tillatelser |
| Antall markedsføringstillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden foreligger det ikke detaljerte data om virkningsmekanismen. Glycin er en enkel aminosyre, og den opprinnelige indikasjonen (MSUD) er en metabolsk sykdom. Ut fra de tilgjengelige dataene kan det ikke påvises noen troverdig mekanistisk kobling mellom glycin og sykdom i nesehulen.

TxGNN-scoren er svært høy (99,85 %), men det er en ren beregningsmessig prediksjon. Den ene studien som er koblet til prediksjonen er en bildediagnostikkstudie (PET) av en radiofarmasøytisk markør, og de to publikasjonene gjelder veterinærhistokjemi og slimhinneadjuvanser. Ingen av dem undersøker glycin som behandling for en nasal tilstand.

Den nest rangerte prediksjonen, **akutt laryngofaryngitt** (score 99,84 %), har heller ingen kliniske studier eller litteratur. Eventuelle antiinflammatoriske eller cytobeskyttende effekter av glycin vil her være spekulative.

---

## Dokumentasjon fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT01806675](https://clinicaltrials.gov/study/NCT01806675) | Fase 1–2 | Fullført | 25 | PET/CT- eller PET/MR-studie av en ny radiofarmasøytisk markør (18F-FPPRGD2) for αvβ3-integrinuttrykk som biomarkør for angiogenese hos kreftpasienter. Ikke en behandlingsstudie med glycin, og gir ingen data om effekt eller sikkerhet. |

Studien vurderes som lite relevant (grad C).

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [7771054](https://pubmed.ncbi.nlm.nih.gov/7771054/) | 1995 | Grunnforskning (veterinær histokjemi) | Veterinary Pathology | Lektinhistokjemi av normal og herpesvirusinfisert nesemukosa hos storfe. Omhandler ikke glycin. |
| [29607903](https://pubmed.ncbi.nlm.nih.gov/29607903/) | 2018 | Preklinisk formuleringsforskning | Chemical & Pharmaceutical Bulletin | Oligoarginin-polymerkonjugater som slimhinneadjuvans for antistoffinduksjon i nesehulen hos mus. Omhandler ikke glycin. |

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005557 | Maapliv | Ikke oppgitt | Maple Syrup Urine Disease (avregistrert) |

Produsent: Recordati Rare Diseases. Det finnes ingen gyldige tillatelser for tiden.

---

## Sikkerhetsvurderinger

Pakningsvedlegget er ikke tilgjengelig i de innsamlede dataene, og interaksjonsdata ble ikke funnet. Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

Kunnskapsgrafen (PrimeKG) viser imidlertid kontraindikasjonsrelasjoner mellom glycin og følgende tilstander. Disse er ikke hentet fra preparatomtalen og må verifiseres:

- **Nyre og urinveier**: nyresykdom, kronisk nyresykdom, kronisk nyresvikt, terminal nyresvikt, nefrolitiasis, nefrokalsinose, akutt uratnefropati, pyoureter
- **Kalsium- og fosfatforstyrrelser**: hyperkalsemi, humoral hyperkalsemi ved malignitet, hyperparatyreoidisme, osteitis fibrosa, hyperfosfatemi, forstyrrelser i fosformetabolismen, hypervitaminose, sarkoidose, lytiske beinmetastaser
- **Hjerte og kar**: hjertesykdom, kardiovaskulær sykdom, arteriosclerosis obliterans, digitalisforgiftning, ventrikkelflimmer
- **Stoffskifte**: fenylketonuri, forstyrrelser i fenylalaninmetabolismen
- **Annet**: forstoppelse

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Forutsigelsen støttes kun av en modellscore (evidensnivå L5). Det finnes ingen relevante kliniske studier eller litteratur, virkningsmekanismen er ukjent i dataene, og den eneste norske/europeiske tillatelsen er avregistrert.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Pakningsvedlegg med advarsler og kontraindikasjoner (blokkerende datamangel)
- Prekliniske eller kliniske studier som faktisk undersøker glycin ved sykdom i nesehulen (eller akutt laryngofaryngitt)
- Vurdering av administrasjonsvei og formulering for en nasal/øvre luftveisindikasjon
- Avklaring av de kontraindikasjonene som er identifisert i kunnskapsgrafen
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

