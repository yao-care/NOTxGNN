---
layout: default
title: Ketoconazole
parent: Moderat evidens (L3-L4)
nav_order: 227
evidence_level: L4
indication_count: 1
last_modified_at: 2026-11-24
description: "Ketoconazole: predikert ny indikasjon Akne (evidensnivå L4). Opprinnelig indikasjon: Cushings syndrom"
monitor_inn: "KETOCONAZOLE"
predicted_indications: ["acne (disease)"]
---

# Ketoconazole
{: .fs-9 }

Evidensnivå: **L4** | Predikerte indikasjoner: **1** stk.
{: .fs-6 .fw-300 }

---

## Innholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmasøytens vurderingsrapport

</div>

## Ketokonazol: Fra Cushings syndrom til akne
{: .text-alpha }

## Oppsummering i én setning

Ketokonazol er et imidazol-soppmiddel som i Europa er godkjent for behandling av Cushings syndrom.
TxGNN-modellen forutsier at det kan ha effekt mot **akne**,
men støtten er foreløpig svak: **1 klinisk studie** (aktiv, ikke rekrutterende, lokalbehandling) og noen få **publikasjoner**, hvorav de fleste er oversikts- og kasuistikker eller laboratoriestudier.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cushings syndrom |
| Foreslått ny indikasjon | Akne |
| TxGNN-prediksjonsscore | 0,9980 |
| Evidensnivå | L4 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Ketoconazole (uoffisiell oversettelse): «Ketokonazol blokkerer syntesen av ergosterol, en sentral komponent i soppcellemembranen, gjennom hemming av det cytokrom P-450-avhengige enzymet lanosterol-14α-demetylase, som er ansvarlig for omdannelsen av lanosterol til ergosterol i soppcellemembranen. Dette fører til en akkumulering av metylerte sterolforløpere og en uttømming av ergosterol i cellemembranen, noe som svekker strukturen og funksjonen til soppcellemembranen.» Engelsk originaltekst: "Ketoconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: ketoconazole prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4baebcab-a237-42c0-9183-6f447a44e371), versjon av 2025-11-18; hentet 2026-11-19). Ut fra kjent farmakologi hemmer ketokonazol soppenzymet CYP51 (ergosterolsyntese), og i høyere doser også humane steroidogene enzymer (CYP17A1, CYP11A1, CYP11B1). Dette senker produksjonen av androgener og kortisol, og forklarer bruken ved Cushings syndrom.

Redusert androgensignalering kan i teorien redusere talgproduksjonen ved androgendrevet akne, for eksempel ved hyperandrogene tilstander som PCOS. Ved lokal bruk kan den antisoppvirkningen mot *Malassezia* (*Pityrosporum*) og en mild antiinflammatorisk effekt være nyttig ved akneliknende eller follikulære utbrudd der gjær spiller en rolle. Laboratoriestudier viser også at ketokonazol hemmer vekst og lipaseaktivitet hos *Propionibacterium acnes*.

Koblingene er plausible, men indirekte. Den svært høye TxGNN-scoren er en beregnet prediksjon og ikke klinisk evidens. Det bør også bemerkes at den opprinnelige indikasjonen (systemisk, ved hormonoverskudd) og den foreslåtte (trolig topisk ved akne) skiller seg i administrasjonsvei og doseringsprofil.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | Ikke relevant (NA) | Aktiv, ikke rekrutterende | 52 | Randomisert studie som sammenligner topisk ketokonazol 2 % krem med adapalen 2 % krem ved mild komedonal og papulopustuløs akne i 12 uker. Ingen publiserte resultater ennå. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | Oversikt | Dermatology | Oppdatering om systemisk aknebehandling; antibiotika er førstevalg ved papulopustuløs akne. |
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | Laboratoriestudie | Microbiology and Immunology | Ketokonazol hemmer lipaseaktivitet og vekst hos *P. acnes*; kan være et alternativ ved antibiotikaresistens. |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | Laboratoriestudie | Biological & Pharmaceutical Bulletin | In vitro-aktivitet av azol-soppmidler mot *P. acnes* isolert fra aknepasienter. |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Klinisk studie | Clinical and Experimental Dermatology | Pityrosporum-follikulitt forveksles ofte med akne; diagnose og behandlingsforsøk hos 62 pasienter. |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | Kasuistikk | Archives of Dermatology | Sammenheng mellom neonatal papulopustuløst utbrudd og *Malassezia furfur*-infeksjon. |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | Oversikt | Keio Journal of Medicine | *Pityrosporum ovale* og hudsykdommer, blant annet follikulitt og seboreisk dermatitt. |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | Oversikt | BMJ Clinical Evidence | PCOS er assosiert med hirsutisme, akne og andre metabolske komplikasjoner (indirekte relevans). |

Merk: Flere av publikasjonene gjelder beslektede tilstander (Pityrosporum-follikulitt, PCOS) eller bare er indirekte relevante. Ingen randomiserte studier av ketokonazol ved akne er publisert i det innsamlede materialet.

---

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/003906 | Ketoconazole Esteve (previously Ketoconazole HRA) | Ketoconazole | Cushing Syndrome | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

**Kontraindikasjoner og sykdommer som er knyttet til legemidlet i kunnskapsgrafen (PrimeKG, ikke preparatomtale):**
langt QT-syndrom (inkl. familiært), torsades de pointes, leversykdom, galleblæresykdom, binyrebarksvikt/Addisons sykdom, hudatrofi, telangiektasi (inkl. hereditær hemoragisk telangiektasi), kapillærsykdom, perifer karsykdom/claudicatio/perifer arteriell sykdom og achlorhydri.

**Legemiddelinteraksjoner (100 registrert; utvalg):**
- **Alvorlige (Major):** loperamid, triamcinolon, budesonid
- **Moderate:** famotidin, ranitidin, rabeprazol, omeprazol (syrehemmere – redusert opptak), hydrokortison, deksametason, betametason, aprepitant, pioglitazon, alosetron, atropin, hyoscyamin, metskopolamin, bisakodyl
- **Mindre (Minor):** amfotericin B (inkl. lipidkompleks)

Interaksjonene gjelder hovedsakelig systemisk bruk. For topisk bruk ved akne vil systemisk eksponering være lav, men dette bør bekreftes.

Det foreligger ikke data fra preparatomtale om advarsler og kontraindikasjoner; se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Evidensen er på nivå L4: én liten, ikke-faset studie uten publiserte resultater, samt laboratoriedata og indirekte litteratur. Sikkerhetsdata fra preparatomtale mangler. Den høye TxGNN-scoren er ikke klinisk evidens.

<!-- review:begin no-lic-20261106-ketoconazole-1 -->

> **Kontrollrettelse (2026-11-06)**: Opprinnelig sto det: «Den eneste norske/europeiske godkjenningen er opphevet, og sikkerhetsdata fra preparatomtale mangler.» Fjernet: opplysningen om at godkjenningene er avregistrert eller at ingen gyldig godkjenning finnes, stemte ikke med EMAs data om sentrale EU-godkjenninger (2026-11-06). Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261106-ketoconazole-1 -->

**For å gå videre kreves følgende:**
- Resultater fra NCT07237763 (topisk ketokonazol 2 % mot adapalen 2 %), og bekreftelse av hvilken tilstand som faktisk studeres
- Nedlasting og gjennomgang av preparatomtale med advarsler og kontraindikasjoner (blokkerende datagap)
- Detaljerte data om virkningsmekanisme (f.eks. fra DrugBank)
- Avklaring av administrasjonsvei (topisk vs. systemisk) og tilgjengelige topiske preparater i Norge
- Vurdering av systemisk sikkerhet (lever, QT-forlengelse, binyrehemming) dersom systemisk bruk ved akne vurderes
- Randomiserte, kontrollerte studier med akneendepunkter (lesjonstelling, global vurdering)

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse).

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-06 | Fjernet: «Den eneste norske/europeiske godkjenningen er opphevet, og s» | Rettet (revidert 2026-11-24; tidligere versjon er lagret i posten) | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: ketoconazole prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4baebcab-a237-42c0-9183-6f447a44e371) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

