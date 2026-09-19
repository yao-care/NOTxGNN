---
layout: default
title: Oritavancin
parent: Kun modellprediksjon (L5)
nav_order: 255
evidence_level: L5
indication_count: 3
---

# Oritavancin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Oritavancin: Fra gram-positive bakterieinfeksjoner til Bacteroidaceae-infeksjonssykdom

## Sammenfatting på en setning

> Oritavancin er et lipoglycopeptidantibiotikum hvis kjente aktivitetsspektrum er begrenset til gram-positive bakterier.
> TxGNN-modellen forutser at det kan være effektivt mot **Bacteroidaceae-infeksjonssykdom**,
> men denne forutsigelsen har **ingen støttende kliniske studier eller litteratur**, og evidensens egen mekanistiske analyse indikerer at forutsigelsen er **biologisk usannsynlig**.

## Rask oversikt

| Emne | Innhold |
|------|------|
| Original indikasjon | Ikke formelt dokumentert i denne evidenspakken (legemiddel ikke markedsført på Taiwan; ingen godkjent indikationstekst tilgjengelig). Kjent legemiddelklasse: lipoglycopeptidantibiotikum aktivt mot gram-positive organismer. |
| Forutsagt ny indikasjon | Bacteroidaceae-infeksjonssykdom |
| TxGNN-prediksjonspoeng | 99.48% |
| Bevisnivå | L5 |
| Status på Taiwan-marked | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne forutsigelsen rimelig?

Detaljerte data om virkningsmekanisme er flagget som et datahull i denne evidenspakken (`original_moa: [Data Gap]`). Imidlertid beskriver gjenutnyttelsesgrunnlaget knyttet til toppforutsigelsen oritavancin som et lipoglycopeptidantibiotikum som binder D-Ala-D-Ala-terminalen til celleveggens forløpere, og hemmer peptidoglykansyntese — en mekanisme som er effektiv **bare mot gram-positive bakterier**.

Bacteroidaceae er gram-negative anaeober hvis ytre membran strukturelt blokkerer penetrasjon av store glykopeptidmolekyler. Ifølge evidenspakken selv er den mekanistiske lenken mellom oritavancin og den forutsagte indikasjon **i strid med legemidlets kjente antibakteriespektrum**, snarere enn støttende.

Det samme mønsteret gjelder for de to andre topp-rangerte forutsigelsene i denne evidenspakken:
- **Oftalmisk herpes zoster** er en virusinfeksjon; oritavancin har ingen kjent antivirusaktivitet.
- **Mycoplasma pneumoniae-pneumoni** involverer en celleveggsdefisient organisme, som er iboende motstandsdyktig mot celleveggsyntesehemmere som oritavancin.

Alle tre topp TxGNN-rangerte forutsigelser for dette legemiddelet har høye likhetsskårer, men er flagget av evidensens egen mekanistiske annoteringer som farmakologisk inkonsistent med oritavancins etablerte virkningsmekanisme. Dette tyder sterkt på at disse er modellstøy-forutsigelser snarere enn ekte gjenutnyttelsesskandidater.

## Bevis fra kliniske studier

For øyeblikket er det ikke registrert relaterte kliniske studier

## Litteraturbevis

For øyeblikket er ingen relevant litteratur tilgjengelig

## Markedsinformasjon for Taiwan

Ingen markedsføringsautorisasjoner eksisterer for øyeblikket på Taiwan — oritavancin er ikke markedsført i denne jurisdiksjonen (`market_status: Not marketed`, `total_licenses: 0`).

## Sikkerhetshensyn

Vennligst henvise til pakningsvedlegget for sikkerhetsinformasjon.

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
TxGNN-skåren er numerisk høy (99.48%), men bevisnivå er L5 — ingen kliniske studier, ingen litteratur, og ingen data fra virkeligheten støtter denne forutsigelsen. Enda viktigere er det at evidensens egen mekanistiske begrunnelse eksplisitt motsier forutsigelsen: oritavancins gram-positiv-selektive, celleveggsavhengige mekanisme er uforenlig med et gram-negativt anaerobisk mål (Bacteroidaceae), og den samme diskvalifiserende logikken gjelder for de to andre rangerte kandidatene (en virusinfeksjon og en celleveggsdefisient organisme). Dette er et tilfelle der modellskåren ikke bør ha forrang over mekanistisk rimelighet.

**For å fortsette er følgende nødvendig:**
- Bekreftet MOA og godkjent indikasjondata fra DrugBank/produsentmerking (for øyeblikket merket som datahull: DG001, DG002)
- TFDA/regulatorisk pakningsvedlegg med advarsler og kontraindikasjoner
- Uavhengig gjennomgang av hvorfor TxGNN tildelte høye skårer til mekanistisk motsagte indikasjoner (mulig modellkalibrasjonsproblem for denne legemiddelnoden)
- Hvis forfølges videre, in vitro-følsomhetsdata mot Bacteroidaceae-arter før noen preklinisk eller klinisk investering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

