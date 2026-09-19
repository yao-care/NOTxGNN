---
layout: default
title: Everolimus
parent: Kun modellprediksjon (L5)
nav_order: 144
evidence_level: L5
indication_count: 10
---

# Everolimus
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

## Everolimus: Fra avansert nyrecellekarsinom til liposarkom

## Oppsummering på én setning

> Everolimus er en mTOR-hemmer (rapalog) med etablert bruk ved avansert nyrecellekarsinom, basert på beskrivelser funnet i den støttende litteraturen.
> TxGNN-modellen forutsier at det også kan være effektivt for **Liposarkom**,
> med **1 klinisk prøvelse** og **5 publikasjoner** som for tiden støtter denne retningen.
> Ingen offisiell Taiwan/Norge markedsføringsgodkjenning eller merkeetikettdata er tilgjengelige for denne kandidaten, noe som begrenser styrken av denne konklusjonen.

---

## Rask oversikt

| Element | Innhold |
|------|--------|
| Originalindikasjon | Avansert nyrecellekarsinom (etter antiangiogen terapi) — utledet fra litteraturkontekst (PMID 33867192); ingen offisiell lisens/merkeetikettdata tilgjengelige |
| Forutsagt ny indikasjon | Liposarkom |
| TxGNN prediksjonspoengsum | 99.88% |
| Bevisnivå | L2 (1 publisert fase 2-prøvelse, offisiell status fortsatt aktiv/ikke rekrutterer) |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Fortsett med sikkerhetstiltak |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert virkningsmekanismedata ble ikke gitt direkte i DrugBank-feltet for denne kandidaten (datagap). Imidlertid beskriver den støttende litteraturen i denne bevisutstillingen konsekvent og gjentatt everolimus som **"en mTOR-hemmer"** (f.eks. PMID 33867192, PMID 27601542), i samsvar med dens kjente klassifisering som en rapalog. Everolimus ble opprinnelig brukt til avansert nyrecellekarsinom, en setting der PI3K/Akt/mTOR-signaleringsbanen er en godt etablert driver for tumorvekst.

Liposarkom – spesielt den dedifferensierte undertypen (DDL) – deler denne samme veibanbiologien. PMID 26518767 demonstrerer direkte **aktivering av Akt-mTOR-signaleringsbanen i dedifferensierte liposarkomprøver**, noe som gir en molekylær begrunnelse for mTOR-rettet intervensjon. Fordi DDL ofte også inneholder CDK4-amplifisering, kan kombinasjonen av everolimus med en CDK4/6-hemmer (ribociclib) – som testet i NCT03114527 og rapportert i PMID 37967116 – tilby en mekanistisk synergistisk tilnærming: CDK4/6-hemming adresserer cellsyklusdriveren mens mTOR-hemming adresserer den nedstrøms overlevingsbanen. Dette gir et plausibelt, biologi-drevet grunnlag for TxGNN-prediksjonen i stedet for en rent statistisk assosiasjon.

---

## Klinisk prøvelsesbevis

| Prøvelsenummer | Fase | Status | Rekruttering | Viktige funn |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Fase 2 | Aktiv, ikke rekrutterer | 48 | To-arms studie av ribociclib + everolimus ved avansert dedifferensiert liposarkom (Arm A) og leiomyosarkom (Arm B) etter ≥1 tidligere systemisk terapi; evaluerer anti-tumoraktiviteten ved kombinert CDK4/6 og mTOR-hemming. |

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Fase 2 klinisk prøvelelsesrapport | Clinical Cancer Research | Rapporterer ribociclib + everolimus (SAR-096) prøvelsen; CDK4/mTOR-kombinasjonen viser synergistisk veksthemming i DDL/LMS-tumormodeller, og støtter klinisk begrunnelse. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Oversikt | Frontiers in Oncology | PDOX-musemodeller identifiserer effektive kombinasjonsregimer med CDK-hemmere (f.eks. palbociclib) i sarkomaer, og støtter cellsyklus/mTOR-veibanmålstrategi. |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mekanistisk/immunhistokjemisk studie | Tumour Biology | Demonstrerer aktivering av Akt-mTOR og MAPK-signaleringsbanen i dedifferensierte liposarkomprøver; in vitro-data viser antitumor-effekt av en mTOR-hemmer. |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preklinisk | Anticancer Research | Evaluerer eribulin i kombinasjon med mekanistisk ulike kreftmidler i liposarkommodeller; bredt spekter kombinert antitumor-aktivitet kontekst. |
| [41991999](https://pubmed.ncbi.nlm.nih.gov/41991999/) | 2026 | Mekanistisk studie | Oncogene | Identifiserer XPO1-hemmer (selinexor) forstyrring av kjerne-transkripsjonell krets som driver DDLPS; støtter konseptet med å målrette dysregulert overlevelse/transkripsjonelle veier i denne tumortypen. |

---

## Norges markedsinformasjon

For tiden ikke markedsført i Norge; ingen lisens-/godkjenningsregistreringer er tilgjengelige i bevisutstillingen.

---

## Cytotoksisitet

Everolimus er et onkologi-bruk mTOR-rettet middel og er derfor inkludert her.

| Element | Innhold |
|------|--------|
| Cytotoksisitetsklassifisering | Målrettet terapi (mTOR-hemmer / rapalog) – ikke et konvensjonelt cytotoksisk middel |
| Myelosuppresjonrisiko | Ikke tilgjengelig i bevisutstillingen; vennligst se pakningsvedlegget |
| Emetogenisitetsklassifisering | Ikke tilgjengelig i bevisutstillingen; vennligst se pakningsvedlegget |
| Overvåkingspunkter | Ikke tilgjengelig i bevisutstillingen; vennligst se pakningsvedlegget |
| Håndteringsbeskyttelse | Ikke tilgjengelig i bevisutstillingen; vennligst se pakningsvedlegget |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Ingen viktige advarsler, kontraindikasjoner eller legemiddel-legemiddelinteraksjonsdata var tilgjengelige i denne bevisutstillingen.

---

## Konklusjon og neste steg

**Beslutning: Fortsett med sikkerhetstiltak**

**Begrunnelse:**
Det er en biologisk plausibel mekanistisk forbindelse (Akt-mTOR-signalering aktivering i DDL) og en aktivt rapportert fase 2-kombinasjonsprøvelse (ribociclib + everolimus), som sammen støtter forsiktig videre evaluering. Imidlertid er prøvelsen selv ikke ennå formelt avsluttet, og denne kandidaten har en **blokkerende** datagap (TFDA/lokal merkeetikettadvarsler og kontraindikasjoner) som må løses før noen sikkerhetsmessig relevant beslutning kan sluttføres.

**For å fortsette, følgende er nødvendig:**
- Løse DG001 (Blokkering): få offisiell merkeetikettadvarsler og kontraindikasjoner
- Løse DG002 (Høy): bekrefte virkningsmekanisme via DrugBank API-spørring
- Bekrefte formell avslutning og topline-resultater av NCT03114527
- Avklare den opprinnelige godkjente indikasjon(er) via en autoritativ regulatorisk kilde, siden `taiwan_regulatory.licenses` for tiden er tom og den "opprinnelige indikasjon" i denne rapporten ble utledet fra litteraturkontekst alene

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

