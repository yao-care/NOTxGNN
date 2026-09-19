---
layout: default
title: Abemaciclib
parent: Kun modellprediksjon (L5)
nav_order: 14
evidence_level: L5
indication_count: 0
---

# Abemaciclib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **0** stk.
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

# ABEMACICLIB: Rapport om omvurdering av legemiddelbruk

## Sammendrag i én setning

Abemaciclib er en selektiv CDK4/6-hemmer som er bredt godkjent internasjonalt for behandling av HR-positive, HER2-negative avansert eller metastatisk brystkreft.
TxGNN-modellen **genererte ingen forutsagte nye indikasjoner** for dette legemidlet i gjeldende analysegang.
Som følge av dette fungerer denne rapporten som en **vurdering av grunnleggende datastatus** snarere enn en fullstendig omvurdering av legemiddelbruk.

---

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke registrert i denne evidenspakken (internasjonalt godkjent for HR+/HER2− brystkreft) |
| Forutsagt ny indikasjon | **Ingen** — TxGNN returnerte ingen forutsagte indikasjoner |
| TxGNN-prediksjonspoeng | N/A |
| Evidensnivå | **L5** (Ingen prediksjoner, ingen støttestudier i pakken) |
| Status på Taiwan-marked | ❌ Ikke markedsført (Ikke markedsført) |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | **Avvent** |

---

## Hvorfor er denne prediksjonen rimelig?

Ingen ny indikasjon ble forutsagt av TxGNN i denne analysesyklusen. Derfor kan en vurdering av mekanistisk plausibilitet ikke utføres på dette tidspunktet.

For referanse er abemaciclib en selektiv, oralt biotilgjengelig hemmer av cyclin-avhengige kinaser 4 og 6 (CDK4/6). Ved blokkering av CDK4/6 forhindrer det fosforyleringen av retinoblastoma-proteinet (Rb), stanser cellsyklusen ved G1-til-S-fasovergangen, og hemmer tumorcellproliferasjon. Denne mekanismen er validert i HR+/HER2− brystkreft og utforskes i andre CDK4/6-avhengige maligniteter internasjonalt. Imidlertid var MOA-feltet i evidenspakken ikke fylt ut, og denne beskrivelsen er basert på etablert farmakologisk kunnskap.

Dersom TxGNN genererer kandidatindikasjoner i fremtidende analyser, gir CDK4/6-hemningsmekanismen et rasjonelt grunnlag for utforsking av omvurdering av legemiddelbruk i tumortyper med avhengighet av Rb-veien (f.eks. visse lungekrefttyper, liposarkomer, mantellcellelymfom).

---

## Klinisk forsøksevidens

Ingen forutsagt indikasjon ble returnert av TxGNN-modellen, så ingen indikasjonsspesifikke kliniske forsøk presenteres.

---

## Litteraturvidens

Ingen forutsagt indikasjon ble returnert av TxGNN-modellen, så ingen indikasjonsspesifikk litteratur presenteres.

---

## Taiwan-markedsinformasjon

Abemaciclib har for tiden **ingen TFDA-markedsføringstillatelser** på Taiwan (markedsstatus: Ikke markedsført). Ingen lisensregistreringer er tilgjengelige.

---

## Cytotoxisitet

Abemaciclib er et **antineoplastisk agens** (CDK4/6-hemmer, klassifisert som målrettet terapi). Følgende cytotoxisitetsprofil er gitt basert på etablert farmakologisk kunnskap, da evidenspakken ikke inneholdt detaljerte toxisitetsdata.

| Element | Innhold |
|------|------|
| Cytotoxisitetsklassifisering | **Målrettet terapi** (selektiv CDK4/6-hemmer; ikke et konvensjonelt cytotoksisk agens) |
| Risiko for myelosuppresjon | **Moderat til høy** — Nøytropeni er en vanlig bivirkning av CDK4/6-hemmere; dosejusteringer kan være nødvendige |
| Emetogenicitetsklassifisering | **Lav til moderat** — Diaré er mer klinisk signifikant enn kvalme/oppkasting for dette legemidlet |
| Overvåkingspunkter | CBC med differensial (nøytrofiler spesielt), leverfunksjonstester (ALT/AST/bilirubin), serum kreatinin, tegn på venøs tromboembolisme, tegn på interstitiell lungessykdom |
| Håndteringsbeskyttelse | Standard oral målrettet terapi-håndtering; krever ikke de fulle forsiktighetsreglene for håndtering av cytotoksiske legemidler som gjelder for konvensjonell kjemoterapi |

---

## Sikkerhetsbetraktninger

Evidenspakken inneholdt ikke fylt sikkerhetsdata (advarsler, kontraindikasjoner eller legemiddel-legemiddel interaksjoner var ikke tilgjengelige fra TFDA eller DDI-spørringer).

> Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Internasjonalt inkluderer viktige sikkerhetsbetraktninger for abemaciclib diaré, nøytropeni, hepatotoksisitet, venøs tromboembolisme og interstitiell lungessykdom/pneumonitt.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-modellen returnerte ingen forutsagte nye indikasjoner for Abemaciclib i denne analysekjøringen. Uten en kandidatindikasjon kan ingen omvurdering av legemiddelbruk fortsette. I tillegg er legemidlet ikke for tiden markedsført på Taiwan, og flere datakløfter (MOA, TFDA-merking/advarsler, kontraindikasjoner) er uløst.

**For å fortsette, kreves følgende:**
- **Kjør TxGNN-prediksjon på nytt** med oppdaterte kunnskapsgrafikdata for å avgjøre om nye indikasjoner dukker opp
- **Fyll MOA-data** via DrugBank API (Data Gap DG002, alvorlighetsgrad: Høy)
- **Innhent advarsler og kontraindikasjoner fra TFDA-pakningsvedlegget** hvis/når legemidlet oppnår markedsføringsgodkjenning (Data Gap DG001, alvorlighetsgrad: Blokkering)
- **Overvåk regulatorisk status på Taiwan** — Abemaciclib er markedsført i mange land (USA: Verzenio; EU: Verzenios); Taiwan-godkjenning kan være forestående
- **Hvis en forutsagt indikasjon genereres i fremtiden**, gjenstartar evalueringspipelinen med en komplett evidenspakke

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

