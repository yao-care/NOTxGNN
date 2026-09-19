---
layout: default
title: Travoprost
parent: Kun modellprediksjon (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: Fra åpen vinkelglaukom/okulær hypertensjon til viskeral kalsifilaksi

## Oppsummering i en setning

> Travoprost er en prostaglandin F2α (FP-reseptor) analogon som brukes topikalt ved åpen vinkelglaukom og okulær hypertensjon (utledet fra klinisk forsøkskontekst, da ingen `original_indications` ble registrert).
> TxGNN-modellens toppprediksjon er **viskeral kalsifilaksi**,
> men denne kandidaten har for tiden **0 kliniske forsøk** og **0 publikasjoner** som støtter den — poenget gjenspeiler bare innebygningslikhet i kunnskapsgrafen, uten mekanistisk eller klinisk bekrefting.

---

## Hurtig oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Åpen vinkelglaukom / okulær hypertensjon (utledet fra forsøksbevis; ikke til stede i `taiwan_regulatory.licenses`) |
| Forutsatt ny indikasjon | Viskeral kalsifilaksi |
| TxGNN-prediksjonspoeng | 99.9998% |
| Bevisnivå | L5 (modellprediksjon bare, ingen støttende studier) |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte mekanisme-for-handling-data ikke tilgjengelig (`original_moa`: [Data Gap]). Basert på kjent farmakologi er travoprost en synttetisk prostaglandin F2α-analogon og FP-reseptor-agonist; dens etablerte kliniske bruk er senking av intraokulært trykk via økt uveoskleralt utflytning ved glaukom/okulær hypertensjon.

For den topprangerte kandidaten, **viskeral kalsifilaksi**, sier bevispakningen selv at det ikke finnes direkte eller indirekte kliniske bevis, og ingen kjent mekanistisk forbindelse — kalsifilakspatologi sentrerer seg rundt vaskulær kalsinering og mikrotromboser, som ikke er forbundet med FP-reseptor-signalering. Den høye TxGNN-poenget gjenspeiler innebygningslikhet i kunnskapsgrafen, ikke en validert farmakologisk hypotese.

Det er verdt å merke at blant de ni andre forutsatte indikasjonene i denne pakken, bare rang 5 («vaskulær sykdom») har noe klinisk forsøk/litteratur vedlagt, og selv de er indirekte (okulær vasoaktivitetsfunn, hyperemiaadverseffektstudier) i stedet for behandlingsbevis for en systemisk vaskulær sykdom. Rang 10 («hemangioendoteliom») støttes bare av en kasuistikk om travoprost-indusert uveaeffusjon — et bivirkningssignal, ikke ett terapeutisk. Ingen av de ti prediksjoner i denne pakken møter for tiden en troverdig mekanistisk eller klinisk standard.

---

## Klinisk forsøksbevis

For tiden er det ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon Norge

Travoprost har for tiden ingen markedsføringstillatelse på posten (`market_status`: Ikke markedsført / Ikke markedsført; `total_licenses`: 0). Ingen lisensoppføringer er tilgjengelige å oppsummere.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og legemiddelinteraksjonsdata er alle for tiden utilgjengelige — se datastykker DG001/DG002 nedenfor.)

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Den topprangerte prediksjonen (viskeral kalsifilaksi) har null kliniske forsøk, null litteratur, og en eksplisitt oppgitt mangel på mekanistisk troverdighet i bevispakningen selv — dette er et rent modell-likhetssignal (L5) uten noen form for bekreftet bevis.

**For å fortsette, er følgende nødvendig:**
- TFDA-etikettvarsler/kontraindikasjoner (DG001, Blokkering — blokkerer for tiden S1 sikkerhetskontroll)
- Verifisert mekanisme-for-handling-data fra DrugBank (DG002, Høy prioritet)
- Prekliniske eller mekanistiske studier som knytter FP-reseptor-agonisme til vaskulær kalsinerings-patologi
- Hvis man forfølger rang 5 («vaskulær sykdom») i stedet, systemisk (ikke-okulær) farmakokinetisk/eksponeringsdata, siden gjeldende bevis er begrenset til topikale okulære effekter

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

