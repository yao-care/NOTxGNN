---
layout: default
title: Reteplase
parent: Kun modellprediksjon (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Reteplase
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

# Reteplase: Fra myokardinfarkt til posteroinferiørt myokardinfarkt

## Oppsummering i én setning

Reteplase er et rekombinant vevsplasminogenaktivator-preparat (trombolytikum) som opprinnelig brukes til behandling av akutt myokardinfarkt.
TxGNN-modellen predikerer at det kan være effektivt ved **posteroinferiørt myokardinfarkt**, men dette er en undertype av den allerede godkjente indikasjonen, og det finnes **ingen kliniske studier** og **ingen publikasjoner** som spesifikt støtter denne prediksjonen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Myokardinfarkt |
| Predikert ny indikasjon | Posteroinferiørt myokardinfarkt |
| TxGNN-prediksjonsscore | 99,90 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun trukket tilbake (kansellert) |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Basert på kjent informasjon er reteplase en rekombinant vevsplasminogenaktivator som omdanner plasminogen til plasmin og dermed løser opp blodpropper i kransarteriene. Effekten ved akutt myokardinfarkt er etablert, og mekanismen kan i prinsippet også gjelde for anatomiske undertyper av infarkt.

Posteroinferiørt myokardinfarkt er en anatomisk undertype av den godkjente indikasjonen. Dette er derfor ikke en reell ompakking av legemidlet (repurposing), men faller inn under den opprinnelige indikasjonen. Den høye TxGNN-scoren (0,999) gjenspeiler mest sannsynlig nærheten til myokardinfarkt i kunnskapsgrafen, snarere enn ny evidens.

For andre høyt rangerte prediksjoner er bildet svakere:
- **Posterolateralt og septalt myokardinfarkt:** Også undertyper av myokardinfarkt. Kun enkeltstående kasuistikker er koblet til disse, og de viser ikke effekt av reteplase for den aktuelle undertypen.
- **Koronarstenose (rang 5):** Eneste prediksjon med noe relevant litteratur (evidensnivå L4), men studiene er sekundæranalyser eller studier av «facilitert PCI» hos infarktpasienter, og evidensen er indirekte.
- **Prediksjoner uten mekanistisk kobling (rang 6–10 og kongenitale tilstander):** Arvelig trombofili, kromosomdelesjon, beta-talassemi og enzymmangel i røde blodceller mangler plausibel kobling til reteplase og er trolig artefakter fra kunnskapsgrafen.

## Klinisk studieevidens

Foreløpig er det ingen registrerte kliniske studier knyttet til denne prediksjonen.

## Litteraturevidens

For posteroinferiørt myokardinfarkt finnes foreløpig ingen relatert litteratur. Under er litteratur knyttet til nærliggende prediksjoner som illustrerer evidensbildet:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [15800019](https://pubmed.ncbi.nlm.nih.gov/15800019/) | 2005 | Kohort | European Heart Journal | Prognostisk betydning av aPTT etter reteplase eller halv dose reteplase pluss abciksimab (GUSTO-V) |
| [11079647](https://pubmed.ncbi.nlm.nih.gov/11079647/) | 2000 | Klinisk studie | J Am Coll Cardiol | Tidlig PCI etter reteplase med eller uten abciksimab ved akutt myokardinfarkt (SPEED/GUSTO-4 pilot) |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Kasuistikk | Catheter Cardiovasc Interv | Primær PCI av ubeskyttet venstre hovedstamme, tilrettelagt med intrakoronar reteplase, ved posterolateralt infarkt |
| [16786798](https://pubmed.ncbi.nlm.nih.gov/16786798/) | 2005 | Kasuistikk | Przeglad Lekarski | Akutt inferiørt og høyre ventrikkelinfarkt hos pasient med atrieseptumdefekt; reteplase og abciksimab ga elektrokardiografisk reperfusjon |
| [34512848](https://pubmed.ncbi.nlm.nih.gov/34512848/) | 2021 | Oversikt/kasuistikk | Pan African Medical Journal | De Winter-mønster i EKG ved spontan koronardisseksjon; vurderer ikke reteplase |

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000105 | Rapilysin | Ikke oppgitt | Myokardinfarkt |

Godkjenningen er kansellert, og det finnes ingen gyldige godkjenninger i Norge.

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Totalt 100 interaksjoner er registrert. Eksempler på de viktigste (alvorlighetsgrad «Major», økt blødningsrisiko er forventet for antitrombotiske midler):
  - Abciksimab
  - Apiksaban
  - Betriksaban
  - Acalabrutinib
  - Avapritinib
  - Deferasirox
  - Ibritumomab tiuxetan og tositumomab (inkl. I-131)
- **Moderate interaksjoner** omfatter blant annet acetylsalisylsyre, ketorolak, ibuprofen, celekoksib, diklofenak (topikal), aminokapronsyre, omega-3-fettsyrer, fenfluramin, deksfenfluramin og sibutramin.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den predikerte indikasjonen er en undertype av den allerede godkjente indikasjonen, og det finnes verken kliniske studier eller direkte litteratur. Den høye scoren er trolig et resultat av ontologinærhet. Produktet er dessuten ikke lenger markedsført i Norge.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Direkte kliniske data for den aktuelle undertypen, eller en avklaring av at den allerede dekkes av den opprinnelige indikasjonen
- Avklaring av kommersiell tilgjengelighet, siden den eneste godkjenningen er kansellert
- Eventuelt fokus på koronarstenose (L4) som et mulig forskningsspørsmål, med forbehold om at facilitert PCI generelt ikke har vist klar nytte
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

