---
layout: default
title: Delamanid
parent: Kun modellprediksjon (L5)
nav_order: 104
evidence_level: L5
indication_count: 7
---

# Delamanid
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

# Delamanid: Fra legemiddelresistent tuberkulose til bovint tuberkulose

## Sammendrag i én setning

> Delamanid er en nitro-dihydro-imidazooxazol-antimykobakteriell substans som er etablert for behandling av legemiddelresistent pulmonær tuberkulose (MDR-TB) hos mennesker.
> TxGNN-modellens toppprediksjon peker på **Bovint tuberkulose** (forårsaket av *Mycobacterium bovis*, en nær slektning av *M. tuberculosis*),
> men denne spesifikke prediksjonen er for tiden støttet bare av **0 kliniske forsøk** og **1 indirekte publikasjon** (patogenomikk, ikke en legemiddeleffektivitetsstudie).
> En relatert, mer klinisk handlingsorientert prediksjon i samme evidenssett — **Inaktiv tuberkulose** — er støttet av **2 aktive fase 2/3 kliniske forsøk med delamanid selv** og **20 publikasjoner**, og er flagget nedenfor for vurdering.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Legemiddelresistent pulmonær tuberkulose (MDR-TB) — kjent farmakologisk bruk; ikke tilstede i gjeldende reguleringsblokk (se Datamangler) |
| Forutsagt ny indikasjon | Bovint tuberkulose |
| TxGNN-prediksjonspoengsum | 99.91% |
| Bevisgrad | L5 (modellprediksjon kun; ingen delamanid-spesifikk klinisk eller preklinisk studie for denne indikasjonen) |
| Taiwans markedsstatus | ✗ Ikke markedsført (Not marketed) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljert informasjon om virkningsmekanisme ikke tilgjengelig i denne evidenspakken (flagget som DG002, høy alvorlighetsgrad). Basert på etablert farmakologisk kunnskap er delamanid en nitro-dihydro-imidazooxazol-derivat som hemmer mybølsyre-biosyntese i den mybakterielle celleveggen, og det brukes klinisk (utenfor denne jurisdiksjonen) som del av kombinasjonsterapi for MDR pulmonær tuberkulose forårsaket av *Mycobacterium tuberculosis*.

*Mycobacterium bovis*, agensen for bovint (og zoonotisk) tuberkulose, er medlem av samme *Mycobacterium tuberculosis*-kompleks og deler en nesten identisk celleveggarkitektur, inkludert mybølsyre-biosyntesebaner. Mekanistisk gjør dette tverkartsaktivitet sannsynlig — det samme målet som delamanid hemmer i *M. tuberculosis* er stort sett konservert i *M. bovis*.

Imidlertid er den eneste støttepublikasjonen (PMID 39487429) en helgenomsekvenseringsstudie av legemiddelresistansmønstre i *M. bovis*-isolater — den karakteriserer patogenet, men **tester ikke** delamanids effektivitet mot det. Denne prediksjonen bør derfor leses som en mål-/patogenliknings-hypotese snarere enn en bevis-støttet ombruksmulighet.

**Merknad:** Innenfor samme evidenssett, rangering 2 ("Inaktiv tuberkulose") deler samme underliggende biologi men har direkte klinisk forsøksstøtte for delamanid, inkludert et aktivt fase 2/3-forsøk (CRUSH-TB) og et fase 3-forebyggingsforsøk (PHOENIx MDR-TB) — se nedenfor.

---

## Klinisk forsøksbevis

**For topprangerte prediksjonen (Bovint tuberkulose): For tiden ingen relaterte kliniske forsøk registrert.**

*For referanse har den nært relaterte rangeringsprediksjon 2 ("Inaktiv tuberkulose") direkte delamanid-forsøksstøtte:*

| Forsøksnummer | Fase | Status | Inkludering | Hovedfunn |
|---------|------|------|------|---------|
| [NCT05766267](https://clinicaltrials.gov/study/NCT05766267) | Fase 2/3 | Aktiv, ikke rekrutterer | 288 | 17-ukers kortkursregimer (BMZ + Rifabutin eller Delamanid) vs. standard 6-måneders regime for pulmonær TB |
| [NCT03568383](https://clinicaltrials.gov/study/NCT03568383) | Fase 3 | Aktiv, ikke rekrutterer | 5,832 | 26 ukers delamanid vs. 26 ukers isoniazid for TB-forebygging hos høyrisikohustandskontakter av MDR-TB-indekskasser |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [39487429](https://pubmed.ncbi.nlm.nih.gov/39487429/) | 2024 | Molekylær epidemiologi (WGS) | BMC Genomics | Helgenomsekvensering av zoonotiske *M. bovis*-isolater som karakteriserer genetisk mangfold og legemiddelresistansmarkører; evaluerer ikke delamanid direkte |

---

## Taiwans markedsinformasjon

Delamanid har for tiden **ingen godkjennelse for markedsføring** i denne jurisdiksjonen (`total_licenses: 0`, `market_status: Not marketed`). Ingen lisensposter er tilgjengelige for sammendrag.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

*(Viktige advarsler, kontraindikasjoner og legemiddel–legemiddel-interaksjondata er alle for tiden utilgjengelige — flagget som DG001, blokkerende alvorlighetsgrad, siden det forhindrer S1 sikkerhetsprevurdering.)*

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Topprangerte prediksjonen (Bovint tuberkulose) er støttet bare av TxGNN-poengsummen og ett indirekte patogenomikk-papir — ingen kliniske forsøk eller delamanid-spesifikke studier eksisterer for denne indikasjonen (Bevisgrad L5). Kombinert med et blokkerende datamangler på TFDA-advarsler/kontraindikasjoner (DG001) og stoffets umarkedsførte status lokalt, er det utilstrekkelig bevis for å fremme denne spesifikke prediksjonen.

**For å fortsette, trengs følgende:**
- TFDA/produsent-pakningsvedlegg (advarsler, kontraindikasjoner) for å lukke DG001 før noen sikkerhetsprevurdering
- DrugBank MOA-bekreftelse for å lukke DG002 og støtte mekanistisk begrunnelse
- Preklinisk eller *in vitro*-effektivitetsdata for delamanid spesifikt mot *M. bovis*
- **Vurder å omomfatte ombruksmålet til "Inaktiv tuberkulose" (rangering 2)**, som har aktive fase 2/3 delamanid-spesifikke forsøk og betydelig mer litteraturstøtte, og ville representere en sterkere kandidat for Guardrails-basert evaluering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

