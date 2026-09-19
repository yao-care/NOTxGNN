---
layout: default
title: Caspofungin
parent: Kun modellprediksjon (L5)
nav_order: 77
evidence_level: L5
indication_count: 1
---

# Caspofungin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

# Caspofungin: Fra antifungal terapi til abnormalitet i gastrinsekresjon

## Sammenfattelse i én setning

Caspofungin er et antifungalt middel i echinocandin-klassen; bevissamlingen spesifiserer ikke dets godkjent indikasjon i Norge (midlet er for tiden ikke markedsført der). TxGNN-modellen forutsier en mulig sammenheng med **abnormalitet i gastrinsekresjon**, men denne prognosen støttes av **null kliniske studier** og **null publikasjoner**, og den tilhørende mekanistiske analysen finner eksplisitt ingen plausibel biologisk vei som knytter de to sammen.

---

## Rask oversikt

| Punkt | Innhold |
|------|------|
| Original indikasjon | Ikke spesifisert i bevissamlingen (kjent stoffklasse: echinocandin-antifungal; ingen godkjent indikasjon oppgitt) |
| Forutsagt ny indikasjon | Abnormalitet i gastrinsekresjon |
| TxGNN-prediksjonsresultat | 99.44% |
| Bevisnivå | L5 (modellprognose bare, ingen støttende studier/litteratur) |
| Markedsstatus i Norge | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Vent |

---

## Hvorfor er denne prognosen rimelig?

For tiden er `original_moa`-feltet for stoffet merket som et datagap. Imidlertid identifiserer bevissamlingens egen mekanistiske begrunnelse caspofungin som et echinocandin-antifungal som hemmer fungal cellevegg β-1,3-D-glukan syntase — et fungus-spesifikt enzym uten human homolog.

Ingen kjent farmakologisk vei knytter denne mekanismen til regulering av gastrinsekresjon (f.eks. G-celle funksjon, H+/K+-ATPase, somatostatinsignalering eller CCK2-reseptoraktivitet). Den opprinnelige indikasjonen (systemisk antifungal terapi) og den forutsagte nye indikasjonen (en gastroenterologisk/endokrin lidelse) deler ingen åpenbar patofysiologisk overlapp.

Gitt den fullstendige mangelen på kliniske studier eller litteratur, og mangelen på noen tolkbar biologisk mekanisme, er denne prognosen mest sannsynlig en modellartefakt eller en falskt-positiv associasjon i kunnskapsgrafen snarere enn et genuint gjenbrukssignal.

---

## Bevis fra kliniske studier

For tiden ingen relaterte kliniske studier registrert

---

## Bevis fra litteraturen

For tiden ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon for Norge

Ingen godkjennelser i arkivene — caspofungin er for tiden ikke markedsført i Norge (0 lisenser).

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Vent**

**Begrunnelse:**
Denne kandidaten ligger på bevisnivå L5 (modellprognose bare) uten kliniske studier, ingen litteratur og ingen plausibel mekanistisk sammenheng — bevissamlingens egen begrunnelse argumenterer mot biologisk plausibilitet. Det oppfyller ikke minimumskravet for å gå videre forbi S0.

**For å gå videre er følgende nødvendig:**
- Bekreftet MOA og TFDA/regulatoriske merkedata (for tiden blokkerer sikkerhetsvurdering per DG001/DG002)
- Uavhengig litteratur eller preklinisk bevis som etablerer en mekanistisk sammenheng mellom echinocandin-aktivitet og gastrins regulering
- Hvis ingen slik bevis dukker opp, bør denne kandidaten nedprioriteres som en sannsynlig falskt-positiv prediksjon

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

