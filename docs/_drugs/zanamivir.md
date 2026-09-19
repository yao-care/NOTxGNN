---
layout: default
title: Zanamivir
parent: Kun modellprediksjon (L5)
nav_order: 389
evidence_level: L5
indication_count: 2
---

# Zanamivir
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

# Zanamivir: Fra influensa til pyelonefritt

## Ensetningssammendrag

> Zanamivir er et nevraminidase-hemmer antiviralt middel, opprinnelig utviklet for behandling og profylakse av influensa.
> TxGNN-modellen forutsier at det kan være effektivt for **pyelonefritt**, men **0 kliniske forsøk** og **0 publikasjoner**
> støtter denne retningen for tiden — prediksjonen hviler for tiden bare på modellassosiasjon, uten identifisert biologisk begrunnelse.

---

## Raskt overblikk

| Punkt | Innhold |
|------|---------|
| Originalindikasjon | Influensa (basert på kjent antiviralmekanisme; ikke bekreftet av norsk lisensdokumentasjon — stoffet er ikke markedsført, ingen lisensdata tilgjengelig) |
| Predikert ny indikasjon | Pyelonefritt |
| TxGNN-prediksjonspoeng | 99.84% |
| Bevisnivå | L5 |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt vedtak | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte virkningsmekanisme-data for zanamivir er ikke tilgjengelig i denne evidenspakken (`original_moa: [Data Gap]`). Basert på stoffets kjente farmakologiske klasse, er zanamivir en nevraminidase-hemmer som blokkerer influensa-virusnevraminidase-enzymet, og forhindrer frigjøring av nye viruspartikler fra infiserte celler — en mekanisme spesifikk for influensa A/B-virusreplikasjon.

Pyelonefritt er overveiende en bakteriell infeksjon av nyreparenkym (oftest forårsaket av *E. coli* og andre Enterobacteriaceae). Det finnes ingen kjent antibakteriell aktivitet, nyremålrettet farmakokinetisk egenskap, eller immunmodulatorisk mekanisme for zanamivir som plausibelt ville forklare effektivitet i denne tilstanden. Bevispaekkets egen omformål-rasjonale sier eksplisitt at denne høye TxGNN-poengsum gjenspeiler en grafneuralnettverk-assosiasjon bare, **uten støttende biologisk plausibilitet, mekanistisk litteratur, eller klinisk bevis**.

En annen kandidatindikasjon i denne evidenspakken — «tyrosinmetabolisme-lidelse» (en genetisk metabolsk sykdom) — viser samme mønster: de tre litteratursitatene som ble hentet, gjelder faktisk oseltamivir-resistensmutsasjoner og nevraminidase-hemmer assayer (hvor «tyrosin» vises som et resttypnavn på H275Y mutasjonsstedet), ikke tyrosinmetabolsk sykdom. Dette er en sterk indikator på en nøkelords-samsvar-artefakt snarere enn et genuint biologisk signal, og styrker at ingen av prediksjonene i denne pakken bør fremmes uten uavhengig mekanistisk eller klinisk validering.

---

## Kliniske forsøksbevis

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden ingen relatert litteratur tilgjengelig.

*(Merk: litteratur ble hentet for den andre, lavere prioritets kandidatindikasjon — «tyrosinmetabolisme-lidelse» — men ved gjennomgang gjelder den oseltamivir/nevraminidase-resistensforskning og er ikke tematisk relevant for tyrosinmetabolisme-lidelser. Det presenteres ikke her som støttende bevis.)*

---

## Norges markedsinformasjon

Zanamivir er for tiden ikke markedsført i Norge; ingen lisensiopplysninger er tilgjengelige i denne evidenspakken.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjoner er ikke for tiden tilgjengelige for dette stoffet.)

---

## Konklusjon og neste trinn

**Vedtak: Avvent**

**Begrunnelse:**
Den predikerte indikasjon (pyelonefritt) har et L5-bevisnivå — bare modellprediksjon, med null kliniske forsøk, null støttende litteratur, og ingen identifiserbar mekanistisk vei som forbinder en viral nevraminidase-hemmer til en overveiende bakteriell nyreinfeksjon. En annen kandidatindikasjon i samme pakke viser bevis på et litteraturhentings-misforhold, som ytterligere understreker behovet for forsiktighet før noe ytterligere evaluering.

**For å fortsette er følgende nødvendig:**
- Bekreftet virkningsmekanisme (MOA)-data fra DrugBank eller primær litteratur
- TFDA/regulatoriske merknadsadvarsler og kontraindikasjoner (blokkerer for tiden S1-sikkerhetsscreening per DG001)
- Uavhengig mekanistisk eller preklinisk bevis som knytter nevraminidase-hemming til noen nyre-/urinveispatologi
- Omvalidering av litteraturhentings-rørledningen for å utelukke nøkelords-samsvar-artefakter (som observert med tyrosinmetabolisme-kandidaten)
- Hvis slike bevis ikke dukker opp, bør denne kandidaten nedprioriteres i stedet for å fremmes til videre scoringsstadier

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

