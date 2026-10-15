---
layout: default
title: Hydroxocobalamin
parent: Kun modellprediksjon (L5)
nav_order: 202
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Hydroksokobalamin: Fra forgiftning til esofagusvaricer

## Oppsummering i én setning

Hydroksokobalamin ble opprinnelig godkjent for behandling av **forgiftning** (Cyanokit). TxGNN-modellen forutsier at legemidlet kan ha effekt ved **esofagusvaricer uten blødning** og **esofagusvaricer med blødning**. Det finnes foreløpig **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen, så prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Forgiftning |
| Predikert ny indikasjon | Esofagusvaricer uten blødning (rangert nr. 2: esofagusvaricer med blødning) |
| TxGNN-prediksjonsscore | 99,23 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake/avregistrert (cancelled) |
| Antall markedsføringstillatelser | 1 (0 gyldige) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme for hydroksokobalamin er ikke tilgjengelig i de sammenstilte dataene. Det er kjent at hydroksokobalamin er en form for vitamin B12 og binder cyanid, noe som er grunnlaget for bruken ved forgiftning. Legemidlet kan også binde nitrogenoksid (NO).

Teoretisk kan fjerning av NO øke vaskulær tonus og dermed påvirke portal hypertensjon, som er den underliggende årsaken til esofagusvaricer. Dette er imidlertid **spekulativt** og ikke støttet av noen innhentede data. Det er ikke påvist noen troverdig mekanistisk kobling mellom forgiftningsindikasjonen og esofagusvaricer, og likheten med den opprinnelige indikasjonen er ikke vurdert.

Standardbehandling for varicer virker via andre, godt etablerte mekanismer:
- Ved varicer uten blødning: ikke-selektive betablokkere og endoskopisk båndligering.
- Ved akutt varicesblødning: vasoaktive legemidler (terlipressin, oktreotid), antibiotika og endoskopisk behandling.

Prediksjonsscoren på 0,992 er en ren grafbasert modellprediksjon og bør ikke tolkes som klinisk evidens.

---

## Klinisk evidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000806 | Cyanokit | – | Forgiftning |

Tillatelsen har status «cancelled», og det finnes ingen gyldige tillatelser.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** Kunnskapsgrafen (PrimeKG) knytter hydroksokobalamin til hypertensjon og hypertensive lidelser. Dette er relevant, siden legemidlet kan gi blodtrykksøkning.
- **Spesielle hensyn ved blødende varicer:** Hydroksokobalamin kan gi rød misfarging av hud og urin. Dette kan forstyrre klinisk vurdering, for eksempel fargebedømmelse ved endoskopi eller av urin, hos en pasient med blødning. Sikkerhetsprofilen i denne situasjonen er ikke evaluert.
- **Legemiddelinteraksjoner:** Totalt 32 mulige interaksjoner er funnet i interaksjonsdatabasen. Blant de 20 som er listet, er fire klassifisert som **moderate**: arsentrioksid, kloramfenikol, jod-131 (Iodide I-131) og jod-123 (Iodide I-123). De øvrige har ukjent alvorlighetsgrad, blant annet omeprazol, lansoprazol, simvastatin, loperamid, prednisolon, ranitidin, acetylsalisylsyre, budesonid, folsyre, valsartan, ramipril, lorazepam, citalopram, paracetamol, mirtazapin og levotyroksin.

Advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelige. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5), uten kliniske studier, litteratur eller en etablert mekanistisk kobling. Legemidlet har dessuten ingen gyldig markedsføringstillatelse i Norge, og kunnskapsgrafen peker på hypertensjon som en mulig kontraindikasjon, noe som er uheldig ved portal hypertensjon og varicer.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank.
- Preparatomtale med advarsler og kontraindikasjoner fra den relevante registeret (dette blokkerer sikkerhetsscreening).
- Litteratursøk og prekliniske data på NO-binding og effekt på portaltrykk.
- Vurdering av administrasjonsvei og tilgjengelige formuleringer (ikke vurdert foreløpig).
- Sikkerhetsvurdering ved blødning, inkludert effekt på blodtrykk og fargeinterferens.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

