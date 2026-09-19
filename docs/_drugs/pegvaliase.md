---
layout: default
title: Pegvaliase
parent: Kun modellprediksjon (L5)
nav_order: 271
evidence_level: L5
indication_count: 3
---

# Pegvaliase
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

# Pegvaliase: Fra fenylketonuri til diabetisk retinopati

## Oppsummering på en setning

Pegvaliase er en PEGylert fenylalanin ammoniakk-lyase (PAL) enzymerstattingsterapi opprinnelig brukt til å kontrollere blodets fenylalaninnivåer ved **fenylketonuri (PKU)**.
TxGNN-modellen forutsier at det kan være effektivt for **diabetisk retinopati**, men for tiden **ingen kliniske forsøk og ingen litteratur** støtter denne retningen — prediksjonen er kun modellutgang.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Original indikasjon | Fenylketonuri (PKU) — kontroll av blodets fenylalaninnivåer |
| Forutsagt ny indikasjon | Diabetisk retinopati |
| TxGNN prediksjonspoengsum | 99.17% |
| Bevisgrad | L5 |
| Markedsstatus Norge | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

**Notat:** To nært beslektede indikasjoner ble også merket med nesten identiske poengsum og samme L5/Avvent-status: *alvorlig nonproliferativ diabetisk retinopati* (99.16%) og *diabetisk katarakt* (99.11%). Ingen har noen støttende forsøk eller litteratur.

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelige (MOA: Datahull). Basert på kjent informasjon er pegvaliase en enzymerstattingsterapi som metaboliserer fenylalanin til trans-kanellesyre og ammoniakk, og dens effektivitet ved fenylketonuri er godt etablert.

Imidlertid har denne mekanismen **ingen kjent biologisk overlapping** med patofysiologien ved diabetisk retinopati, som primært er drevet av VEGF-mediert neovaskularisering, kronisk hyperglykemi, oksidativ stress, polyolstieaktivering og AGE-akkumulering. Det er ingen plausibel farmakologisk vei som forbinder fenylalanin-metabolisme til retinale mikrovaskulære sykdommer.

Gitt at denne legemiddelnoden også mangler registrert MOA og null DDI-oppføringer i kunnskapsgrafen, produserte den sparsomme tilkoblingen rundt pegvaliase sannsynligvis en spuriøs høy-konfidens prediksjon snarere enn et genuint biologisk signal. Denne vurderingen er konsistent med bevispakkens egen omformålsrasjonale, som eksplisitt merker poengsumet som en sannsynlig falsk positiv drevet av grafsparsitet.

---

## Klinisk forsøksevidens

For tiden ingen beslektede kliniske forsøk registrert.

---

## Litteraturevidens

For tiden ingen beslektet litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Pegvaliase er **for tiden ikke markedsført i Norge** og har ingen markedsgodkjenninger registrert (0 lisenser).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Notat: TFDA-advarsler/kontraindikasjoner er merket i bevispakningen som et blokkerende datahull — DG001 — noe som betyr at denne kandidaten ikke kan gå videre til S1-sikkerhetsgjennomgang inntil etikett-data er innhentet.)*

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Rasjonale:**
Det er ingen klinisk eller litteraturbevis som støtter denne indikasjonen, den mekanistiske koblingen mellom PAL-enzymerstattning og diabetisk retinopati er biologisk implausibel, og de underliggende MOA/DDI-datahullene antyder at det høye TxGNN-poengsumet kan være et artefakt av grafsparsitet snarere enn et genuint signal. Et blokkerende datahull (manglende TFDA-advarsler/kontraindikasjoner) forhindrer også sikkerhetsgjennomgang på dette stadiet.

**For å gå videre, kreves følgende:**
- TFDA-etikett-data (advarsler, kontraindikasjoner) — løser det blokkerende datahullet DG001
- Bekreftet virkningsmekanisme fra DrugBank eller primærlitteratur — løser høyprioritet-datahullet DG002
- Preklinisk eller mekanistisk bevis som etablerer en biologisk rasjonale som forbinder PAL/fenylalanin-metabolisme til diabetisk retinalsykdom
- Minst ett observasjonelt studie eller tilfellerapport før framgang forbi S0

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

