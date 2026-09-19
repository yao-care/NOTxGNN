---
layout: default
title: Abatacept
parent: Kun modellprediksjon (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
---

# Abatacept
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

# ABATACEPT: Innledende vurdering av resirkulering av legemiddel

## Sammendrag i en setning

Abatacept (DrugBank: DB01281) er en selektiv T-celle ko-stimulasjonsmodulator (CTLA4-Ig fusjonprotein), bredt brukt internasjonalt for revmatoid artritt og andre autoimmune tilstander. For tiden er **ingen TxGNN-predikerte indikasjoner** tilgjengelige for evaluering, og legemiddelet er **ikke markedsført i Taiwan**. Denne rapporten tjener som en innledende datainventar; ytterligere datainnsamling er nødvendig før vurdering av resirkulering av legemiddel kan fortsette.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig i evidenspakken (ingen Taiwan-lisenser) |
| Forutsagt ny indikasjon | Ingen — TxGNN-prediksjon ikke ennå tilgjengelig |
| TxGNN prediktiv poengsum | N/A |
| Bevisgrad | L5 (Utilstrekkelige data) |
| Taiwans markedsstatus | ✗ Ikke markedsført (Ikke markedsført) |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | **Avvent** |

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanisme-data ikke tilgjengelig i evidenspakken. Basert på offentlig tilgjengelig informasjon er abatacept et løselig fusjonprotein som består av det ekstracellulære domenet til menneskelig CTLA-4 koblet til den modifiserte Fc-delen av menneskelig IgG1. Det fungerer som en selektiv T-celle ko-stimulasjonsmodulator ved å binde seg til CD80/CD86 på antigen-presenterende celler, og dermed blokkerer CD28 ko-stimulatory signalet som kreves for full T-celle-aktivering.

Internasjonalt er abatacept (merkenavn: Orencia®) godkjent for revmatoid artritt, juvenil idiopatisk artritt og psoriasisartritt. Disse indikasjonene reflekteres imidlertid **ikke i gjeldende evidenspakken** ettersom legemiddelet ikke har noen Taiwan FDA (TFDA) markedsføringsautoritet.

Siden ingen TxGNN-predikerte indikasjoner har blitt generert, er det ikke mulig å evaluere mekanistisk plausibilitet for noen spesifikk resirkuleringskandidat på nåværende tidspunkt. TxGNN-modellens prediktive pipeline bør kjøres med abatasepts kunnskapsgrafidata for å identifisere potensielle nye indikasjoner.

## Kliniske forsøksbevis

Ingen forutsagt indikasjon er tilgjengelig; derfor ble det ikke utført noe indikasjonsspesifikt klinisk forsøkssøk.

## Litteraturbevis

Ingen forutsagt indikasjon er tilgjengelig; derfor ble det ikke utført noe indikasjonsspesifikt litteratursøk.

## Taiwans markedsinformasjon

Abatacept har for tiden **ingen markedsføringsautoritet** fra Taiwan FDA (TFDA). Det er ingen lisensierte produkter i Taiwan.

## Sikkerhetsvurderinger

> Vennligst se pakningsbilaget for sikkerhetsinformasjon.
>
> Merknad: Advarsler fra TFDA-pakningsmerkingen, kontraindikasjoner og legemiddel-legemiddel-interaksjonsdata var ikke tilgjengelig for dette legemiddelet (ingen Taiwan-markedsføringsautoritet eksisterer). Sikkerhetsevaluering skal referere til internasjonal merking (f.eks. US FDA, EMA) hvis en resirkuleringskandidat identifiseres.

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Evidenspakken er kritisk ufullstendig — det finnes ingen TxGNN-predikerte indikasjoner å evaluere, ingen Taiwan-markedsautoriseringsdata, og ingen lokalt tilgjengelig sikkerhetsinformasjon. Uten en målindikasjon kan en vurdering av resirkulering av legemiddel ikke fortsette.

**For å fortsette, er følgende nødvendig:**
- **Kjør TxGNN-prediktiv pipeline** for abatacept (DB01281) for å generere kandidat-resirkulering-indikasjoner
- **Hent virkningsmekanisme (MOA) data** fra DrugBank API (Data Gap DG002, alvorlighetsgrad: Høy)
- **Hent sikkerhetsmerkingsdata** — enten fra TFDA (hvis fremtidig godkjenning oppstår) eller fra internasjonale regulatoriske kilder som US FDA eller EMA (Data Gap DG001, alvorlighetsgrad: Blokkering)
- **Vurder Taiwan regulatorisk vei** — siden abatacept for tiden ikke er markedsført i Taiwan, bestemme om importasjon eller spesielle tilgangsprogrammer ville være gjennomførbar for noen identifisert resirkulering-indikasjon
- **Omvurder** når predikerte indikasjoner og sikkerhetdata er tilgjengelige

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

