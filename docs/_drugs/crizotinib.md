---
layout: default
title: Crizotinib
parent: Kun modellprediksjon (L5)
nav_order: 106
evidence_level: L5
indication_count: 10
---

# Crizotinib
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

# Crizotinib: Fra ikke-småcellet lungekreft til fibromatose i gingiva

## Oppsummering i én setning

Crizotinib er en hemmer av tyrosinkinasene ALK, ROS1 og MET, og er opprinnelig brukt mot ikke-småcellet lungekreft.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **fibromatose i gingiva** (score 99,81 %), men for denne indikasjonen finnes det **ingen kliniske studier og ingen publikasjoner**. Forutsigelsen er kun grafbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke-småcellet lungekreft (Carcinoma, Non-Small-Cell Lung) |
| Predikert ny indikasjon | Fibromatose i gingiva |
| TxGNN-prediksjonsscore | 99,81 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun kansellert |
| Antall godkjenninger | 1 (kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme var ikke tilgjengelige i datagrunnlaget. Ut fra kjent informasjon er crizotinib en ATP-konkurrerende liten molekylhemmer av reseptortyrosinkinasene ALK, ROS1 og MET. Effekten er godt dokumentert ved ALK- og ROS1-positiv ikke-småcellet lungekreft.

Det er ikke påvist noen mekanistisk kobling mellom crizotinib og fibromatose i gingiva. Den høye TxGNN-scoren er en ren grafbasert prediksjon, og verken kliniske studier eller litteratur knytter legemidlet til tilstanden. Prediksjonen bør derfor betraktes som en hypotese og ikke som et signal med støtte i data.

**Andre predikerte indikasjoner (kort oversikt)**

Det er også vurdert ni andre predikerte indikasjoner. De fleste har svak eller ingen evidens:
- **Lungehilus-karsinom** (L4): kasuistikker om ALK- og ROS1-positivt lungeadenokarsinom. Dette ligger i praksis innenfor den eksisterende indikasjonen og gir lite nytt for repurposing.
- **Lungegerminalcelletumor** (L3, forskningsspørsmål): to basket-studier og litteratur om ALK-drevne svulster, men evidensen er indirekte og avhenger av en målbar genetisk endring.
- **Godartet lungesvulst**: litteraturen gjelder i hovedsak malign ALK-positiv lungekreft, ikke godartede svulster.
- **Fibrom i lunge, lungehamartom, pulmonalsulcus-svulst, inklusjonslegememyopati med Pagets sykdom, junksjonell epidermolysis bullosa og et sjeldent syndrom med leukomelanoderma**: ingen eller irrelevant støtte i data.

---

## Dokumentasjon fra kliniske studier

For fibromatose i gingiva er det for øyeblikket ingen relaterte kliniske studier registrert.

---

## Dokumentasjon fra litteratur

Det finnes for øyeblikket ingen relatert litteratur for fibromatose i gingiva.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002489 | Xalkori (Pfizer Europe MA EEIG) | Ikke oppgitt | Ikke-småcellet lungekreft (status: kansellert) |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet terapi (tyrosinkinasehemmer mot ALK/ROS1/MET) |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Leverfunksjon, hjerterytme/QT og blodstatus bør følges. Se pakningsvedlegget for detaljer. |
| Håndteringsbeskyttelse | Følg gjeldende regler for håndtering av cytostatika/antineoplastiske legemidler |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Det er funnet 100 registrerte interaksjoner. Blant dem som er oppgitt, er følgende vurdert som **alvorlige (Major)**: klaritromycin, cisaprid, dolasetron, eliglustat og granisetron. Mange andre er vurdert som moderate, blant annet famotidin, metformin, loperamid, bupropion, aprepitant, deksametason, budesonid og flere laksantia.
- **Sikkerhetssignaler fra litteraturen**: Publikasjonene som er innhentet beskriver tilfeller av dødelig fulminant leversvikt, kardiotoksisitet (bradykardi, QT-forlengelse, sinusknutesyndrom), erytema multiforme og erosiv øsofagitt hos et barn. Dette er kasuistikker, men de understreker behovet for overvåking.

Se pakningsvedlegget for fullstendig informasjon om advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for fibromatose i gingiva bygger kun på en grafbasert modellscore, uten kliniske studier, litteratur eller en kjent mekanistisk sammenheng. I tillegg er den eneste norske godkjenningen kansellert, og viktige sikkerhetsdata fra preparatomtalen mangler.

**For å gå videre trengs følgende:**
- Innhenting og gjennomgang av pakningsvedlegg/preparatomtale (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Prekliniske data eller en mekanistisk hypotese som kobler ALK/ROS1/MET-signalering til fibromatose i gingiva
- Avklaring av hvorfor godkjenningen i Norge er kansellert, og av hvilke administrasjonsveier som er relevante
- Hvis man vil prioritere en annen kandidat: en egen vurdering av lungegerminalcelletumor eller ALK-drevne svulster, med molekylær seleksjon av pasienter
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

