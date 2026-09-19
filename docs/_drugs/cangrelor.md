---
layout: default
title: Cangrelor
parent: Kun modellprediksjon (L5)
nav_order: 72
evidence_level: L5
indication_count: 0
---

# Cangrelor
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

# Cangrelor: Ingen eksisterende prognose for ny bruk

## Sammendrag i én setning

Cangrelor er en intravenøs, direkte virkende P2Y12 plateletaggregasjonshemmer brukt i akutte kardiovaskulære situasjoner som perkutan koronar intervensjon (PCI). Gjeldende bevissamling inneholder **ingen TxGNN-baserte prognoser for ny bruk** av dette legemidlet, og kritiske datagap i virkningsmekanisme og sikkerhetsinformasjon hindrer en fullstendig evaluering. Denne rapporten fungerer som foreløpig dokumentasjon i påventing av ytterligere datainnsamling.

---

## Rask oversikt

| Punkt | Innhold |
|-------|---------|
| Opprinnelig indikasjon | Antitrombotisk terapi under perkutan koronar intervensjon (PCI) |
| Forutsatt ny indikasjon | Ingen prognose tilgjengelig |
| TxGNN-prediksjonspoeng | N/A |
| Evidensnivå | L5 — kun modellprediksjon; ingen støttende prognoser generert |
| Status på det norske marked | Ikke markedsført |
| Antall markedsføringstillatelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor vurdering er begrenset

Cangrelor (merkenavn: Kengreal / Kengrexal) er en korttidsvirkende, reversibel P2Y12 ADP-reseptorantagonist gitt intravenøst. I motsetning til orale antitrombotika som klopidogrel eller tikagrelor, har cangrelor en ekstremt kort plasmahalveringstid (~3–5 minutter), noe som gjør det særlig egnet for prosedyrebaserte situasjoner hvor rask oppstart og avslutning av plateletaggregasjonshemning er påkrevet.

Detaljerte data for virkningsmekanisme fra DrugBank ble ikke hentet i gjeldende bevissamling (Data Gap DG002). Uten denne informasjonen er det ikke mulig å resonnere om mekanismisk likhet til potensielle nye indikasjoner.

Enda mer kritisk: TxGNN-modellen genererte ingen prognoser for ny bruk av cangrelor i denne pipeline-kjøringen. Matrisen `predicted_indications` er tom, noe som betyr at kjernanalytisk utdata fra arbeidsflyt for ny bruk mangler. Dette kan reflektere utilstrekkelig graftilkobling i den underliggende kunnskapsgrafen, eller legemidlet har muligens ikke blitt scoret mot noen nye sykdomsnoder i denne kjøringen.

---

## Informasjon om det norske marked

Cangrelor er **ikke for tiden godkjent eller markedsført i Norge**. Ingen produktgodkjennelser er registrert i den regulatoriske databasen.

---

## Sikkerhetshensyn

Se pakningsvedlegg for sikkerhetsinformasjon.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Bevissamlingen inneholder ingen TxGNN-genererte prognoser for ny bruk, og to blokkerende/alvorlige datagap (DG001: sikkerhetsadvarsler; DG002: virkningsmekanisme) hindrer enhver meningsfull klinisk eller mekanismisk vurdering.

**For å gå videre er følgende nødvendig:**
- Kjør TxGNN-scoringsprosessen på nytt for å generere `predicted_indications` for cangrelor
- Hent virkningsmekanisme (MOA) fra DrugBank API (Data Gap DG002)
- Analyser PDF-pakningsvedlegg for å trekke ut viktige advarsler og kontraindikasjoner (Data Gap DG001 — er for tiden merket med blokkerings alvorlighetsgrad)
- Gjennomgå EMA/norsk regulatorisk status for cangrelor (Kengrexal), ettersom legemidlet er EU-godkjent og kan kvalifisere for vurdering av norsk markedsføringstillatelse

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

