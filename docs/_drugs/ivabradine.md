---
layout: default
title: Ivabradine
parent: Kun modellprediksjon (L5)
nav_order: 192
evidence_level: L5
indication_count: 6
---

# Ivabradine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Ivabradine: Fra kronisk hjertesvikt/angina til hypertrikose

## Sammenfatting på én setning

Ivabradine er en selektiv HCN (If, «funny current») kanalblokker som bremser sinusknuttefrekvensen, brukt klinisk for kronisk hjertesvikt og stabil angina. TxGNN-modellen forutsier at den kan være effektiv for **Hypertrikose (sykdom)**, men denne prognosen er for tiden støttet av **0 kliniske studier** og **0 publikasjoner**, og bevisstoffpakken selv noterer at det ikke er kjent noen mekanistisk sammenheng mellom HCN-kanalblokkering og regulering av hårvekst.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke spesifisert i bevisstoffpakke (DrugBank `original_indications` felt tomt) |
| Forutsagt ny indikasjon | Hypertrikose (sykdom) |
| TxGNN-prognosescore | 99.79% |
| Bevisnivå | L5 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt avgjørelse | Avvent |

---

## Hvorfor er denne prognosen rimelig?

Detaljerte felt for opprinnelig indikasjon og formell virkningsmekanisme er ikke utfylt i denne bevisstoffpakken. Imidlertid beskriver pakkens egen begrunnelse for ombruk ivabradine som en selektiv HCN-kanalblokkerer som virker på sinusknutten for å redusere hjertefrekvensen, brukt for kronisk hjertesvikt og stabil angina.

Det finnes ingen etablert biologisk vei som forbinder HCN-kanalblokkering i sinusknutten med regulering av hårsekkvekst (f.eks. Wnt/β-catenin-signalering eller androgenreseptor-signalveier som er implisert i hypertrikose). Bevisstoffpakken angir eksplisitt at denne kandidaten oppstår rent fra graf-innebyggingslikhet i TxGNN-modellen, uten direkte eller indirekte klinisk eller mekanistisk støtte.

Det samme mønsteret gjelder for alle seks forutsagte indikasjoner i denne pakken — hypertrikose, Ambras-syndrom, periodont-malformasjonssyndrom, Dandy-Walker-malformasjon, abnormitet av hårhaft og nefrogent syndrom for upassende antidiurese. Hver begrunnelsestekst noterer uavhengig mangelen på en plausibel mekanistisk forbindelse til HCN-kanalfarmakologi, og litteraturen om periodontale sykdommer som ble hentet (rangering 3) består av generelle periodontologi-oversikter som aldri nevner ivabradine, noe som indikerer nøkkelordmatchings-støy snarere enn stoffspesifikk bevis.

---

## Bevis fra kliniske studier

Ingen relaterte kliniske studier er for tiden registrert.

---

## Litteraturbevis

Ingen relevant litteratur er for tiden tilgjengelig.

---

## Norsk markedsinformasjon

Ivabradine er ikke markedsført i Norge under denne bevisstoffpakken (`market_status: Not marketed`, 0 totale lisenser). Ingen godkjenningsregistre er tilgjengelige for opplistning.

---

## Sikkerhetshensyn

Vennligst se pakningsinnskriften for sikkerhetsinformasjon.

*(Merk: den underliggende bevisstoffpakken flagger TFDA-advarsler/kontraindikasjondata som en datalukke med Blokkering-alvorlighetsgrad (DG001), noe som betyr at en formell sikkerhetsgjennomgang (S1) ikke kan utføres for denne kandidaten for øyeblikket.)*

---

## Konklusjon og neste steg

**Avgjørelse: Avvent**

**Begrunnelse:**
Alle seks TxGNN-forutsagte indikasjoner for ivabradine er vurdert til L5 (kun modellprognose), med null støttende kliniske studier og ingen stoffspesifikk litteratur. Bevisstoffpakkens egen mekanistiske begrunnelse for den topprankerte prognosen (hypertrikose) angir eksplisitt at det ikke er kjent noen biologisk sammenheng til ivabradines HCN-kanalblokkering. Kombinert med stoffets ikke-markedsførte status i Norge og en datalukke med Blokkering-alvorlighetsgrad i TFDA-sikkerhetsetikettdata, er det intet grunnlag for å fremme denne kandidaten utover oppdagingsfasen.

**For å gå videre er det nødvendig med:**
- TFDA/regulatoriske etikettdata (advarsler, kontraindiksjoner) — for tiden datalukke (DG001)
- Bekreftet virkningsmekanismedata fra DrugBank (DG002)
- Eventuelle prekliniske eller mekanistiske studier som direkte forbinder HCN-kanalsmodulering med hårsekkvekst eller de andre forutsagte fenotypene
- Revurdering dersom fremtidige TxGNN-modelloppdateringer avdekker indikasjoner med høyere tiltro og mekanistisk plausibilitet for dette stoffet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

