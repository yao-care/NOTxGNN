---
layout: default
title: Catridecacog
parent: Kun modellprediksjon (L5)
nav_order: 78
evidence_level: L5
indication_count: 3
---

# Catridecacog
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

# Catridecacog: Fra koagulasjonsfaktor XIII-substitusjonsterapi til primær platelettsekresjonsforstyrrelse

## Oppsummering i én setning

Catridecacog er rekombinant menneskelig koagulasjonsfaktor XIII A-underenhet, som virker ved å fremme fibrinkorsbinding og stabilisere dannet blodpropp. Opprinnelige indikasjonsdata er foreløpig ikke tilgjengelig; kun kan det utledes fra legemiddelmekanisme at tradisjonelle bruksområder er forbundet med koagulasjonsfaktor XIII-relaterte blødningslidelser. TxGNN-modellen predikerer at den kan være forbundet med **primær platelettsekresjonsforstyrrelse**, med en prediksjonspoengsum på **99.29%**, men **det finnes foreløpig ingen kliniske forsøk eller litteraturbevis** som støtter denne forbindelsen.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelige indikasjoner | Datakluft (`original_indications` ikke gitt; utledet fra mekanisme forbundet med koagulasjonsfaktor XIII-mangel/blødningstendens) |
| Predikert ny indikasjon | Primary release disorder of platelets |
| TxGNN-prediksjonspoengsum | 99.29% (rangering 7143) |
| Bevistnivå | L5 (kun modellprediksjon, ingen kliniske forsøk eller litteraturbevis) |
| Norsk markedsstatus | Not marketed |
| Totalt antall lisensiering | 0 |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prognosen rimelig?

De aktuelle virkningsmekanisme-dataene er i seg selv en datakluft, men basert på analysen av mekanismeassosiasjoner i Evidence Pack kan det utledes: Catridecacog er rekombinant koagulasjonsfaktor XIII A-underenhet som virker på **sluttringet** av koagulasjonskaskaden – fremmer fibrinkorsbinding for å stabilisere dannet blodpropp. Dette er en «strukturstabilisering»-type virkningsmekanisme, ikke en bane som deltar i platelettaktivering, -aggregering eller -granulafrislippelse.

Primær platelettsekresjonsforstyrrelse (Primary release disorder of platelets) har en patofysiologisk mekanisme der **granulafrislippelse etter platelettaktivering er abnorm**, som tilhører nivået av platelettfunksjon, og det er ingen kjent direkte fysiologisk baneoverlapp med fibrinkorsbindingsnivået der koagulasjonsfaktor XIII befinner seg. De to ligner kun på nivået for fenotypeindeling som «blødningslidelse». TxGNN-poengsummen som oppnås reflekterer sannsynligvis **fenotypisk nærhet til blødningsrelaterte sykdomsknuter i kunnskapsgrafen**, i stedet for en reell mekanistisk årsakssammenheng. Inntil originaldata for MOA og indikasjon blir fullstendig supplert, forblir denne assosiasjonen på spekulasjonsnivå, kan hverken utelukkes eller bekreftes.

> Tillegg: Den samme batch (`TW-DB09310-multi`) inneholder to andre relaterte prediksjoner for referanse:

| Rangering | Predikert indikasjon | TxGNN-poengsum | Sammendrag av mekanistisk rimelighet |
|---|---|---|---|
| 2 | Pseudo-von Willebrand disease | 99.29% | Patologien er funksjonell anomali i platelettreseptor GPIbα, uten direkte forbundet mekanisme til faktor XIII, drevet av fenotypisk likhet |
| 3 | Glanzmann thrombasthenia | 99.15% | GPIIb/IIIa-integrin-mangel; teoretisk kunne faktor XIII fungere som hjelpemiddel for blodpropstabilisering, men uten empirisk støtte |

## Bevis fra kliniske forsøk

Det finnes foreløpig ingen relevante registreringer av kliniske forsøk.

## Litteraturbevis

Det finnes foreløpig ingen relevant litteratur som kan brukes som referanse.

## Informasjon om norsk marked

Dette legemidlet har foreløpig **ikke oppnådd noen markedsgodkjenning** på det norske markedet (`market_status: Not marketed`, `total_licenses: 0`); det finnes ingen autorisasjonsregistreringsdata som kan opplistes.

## Sikkerhetshensyn

Vennligst se sikkerhetsinformasjon angitt i legemiddelsamlingen.

> Påminnelse: I henhold til datakluftlisten er «DMP package insert warnings/contraindications» en **Blocking**-nivå datakluft (DG001); før fullstendige legemiddelsamlings-data er innhentet, kan denne kandidaten **ikke gå videre til S1-sikkerhetsgjennomsyn-fasen**.

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
- Begge kandidatprediksjoner ligger ved **L5** (kun modellprediksjon), uten noen kliniske forsøks- eller litteraturbevis som støtter mekanistisk forbindelse;
- Sikkerhetsdata inneholder en Blocking-nivå datakluft (DG001: DMP package insert warnings/contraindications ukjent), som ikke oppfyller regelverket for å kunne gå inn i neste fase av sikkerhetsgjennomsyn.

**Hvis du vil fortsette, må følgende fylles ut:**
- TFDA/originalfabrikantens fullstendige advarsels- og motindikasjonsinformasjon fra legemiddelsamlingen (DG001, Blocking, kilde: DMP-nettsted, metode: Last ned og analyser legemiddelsamlings-PDF)
- DrugBank virkningsmodus (MOA) fullstendige data (DG002, High, kilde: DrugBank API)
- Bekreftet opprinnelig indikasjon (`original_indications`), for å lette mekanistisk assosiasjonssammenligning av predikerte indikasjoner
- Kontinuerlig overvåking for nye registreringer av kliniske forsøk eller litteratur, som grunnlag for oppgradering av bevisnivå

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

