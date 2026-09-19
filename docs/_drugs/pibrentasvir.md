---
layout: default
title: Pibrentasvir
parent: Kun modellprediksjon (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Pibrentasvir
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

# Pibrentasvir: Fra hepatitt C-virusinfeksjon til hepatitt B-virusinfeksjon

## Oppsummering i en setning

> Pibrentasvir er en NS5A-hemmer som markedsføres kun som del av fastdosiskombinasjon glecaprevir/pibrentasvir, brukt til å behandle kronisk hepatitt C-virusinfeksjon (HCV).
> TxGNN-modellen forutsier at det også kan være effektivt for **hepatitt B-virusinfeksjon**, med et svært høyt likhetsresultat (**99,84%**),
> men ved nærmere gjennomgang **tester ingen av de 14 støttende kliniske forsøkene eller 20 litteraturreferansene faktisk pibrentasvir mot HBV** – alle er HCV-studier. Denne prediksjonen bør behandles som et sannsynlig kunnskapsgrafartefakt i stedet for et genuint omformål-signal.

---

## Rask oversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Kronisk hepatitt C-virusinfeksjon, genotype 1–6 (som komponent av glecaprevir/pibrentasvir-kombinasjon) |
| Forutsagt ny indikasjon | Hepatitt B-virusinfeksjon |
| TxGNN prediksjonsresultat | 99,84% |
| Bevisnivå | L5 (modellpreduksjon kun – ingen studie evaluerer direkte pibrentasvir ved HBV) |
| Markedsstatus Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte mekanisme-for-virkning-data for pibrentasvir ikke tilgjengelige fra den strukturerte DrugBank-posten (Datakløft). Basert på kjent informasjon er pibrentasvir NS5A-hemmerkomponenten av fastdosiskombinasjon glecaprevir/pibrentasvir (Maviret/Mavyret), og effektiviteten er etablert spesifikt for kronisk HCV-infeksjon gjennom de store ENDURANCE-, EXPEDITION-, SURVEYOR- og CERTAIN-programmene i fase 2/3.

Mekanistisk er pibrentasvir svært selektivt for HCV NS5A-proteinet, som er essensielt for samling av HCV-replikasjonskompleks og viruspartikkelpakning. HBV er et hepadnavirus som replikeres via omvendt transkripsjonen av pregenomisk RNA ved hjelp av sitt eget polymerase og koder ikke for en NS5A-homolog – det er ingen kjent molekylært mål delt mellom de to virusene. I samsvar med dette er hver klinisk forsøk og nesten hver publikasjon hentet under denne «forutsagte indikasjonen» faktisk en HCV-forsøk (i noen tilfeller hos pasienter med eller screenet for HBV/HIV-koinfeksjon som sikkerhetshensyn), ikke en forsøk som evaluerer antivirale aktivitet mot HBV selv.

Dette mønsteret er ikke isolert til HBV: samme bevispaket viser like høye TxGNN-resultater for HIV, hepatitt A, hepatitt E, dyreviralt hepatitt, Omsk hemorhagisk feber, Kyasanur-skogssykdom, simian/felin immunsviktsvirusinfeksjon, og til og med en ikke-relatert sjelden nevronevolutiv lidelse – ingen støttet av mekanistisk plausible eller sykdomsspesifikke bevis. Dette tyder på at modellen grupperer pibrentasvir med en bred «viralt hepatitt/koinfeksjon»-nodeomegn i kunnskapsgrafen i stedet for å identifisere et genuint farmakologisk forhold til HBV.

---

## Bevis fra kliniske forsøk

Alle forsøkene nedenfor ble hentet som «toppebevis» for HBV-prediksjonen, men iht. bevispapkets egen relevansvurdering (grad C), er hvert enkelt faktisk en HCV-forsøk for glecaprevir/pibrentasvir – ingen rekrutterte eller evaluerte HBV-infiserte pasienter for antivirale effekt.

| Forsøksnummer | Fase | Status | Rekruttering | Hovedresultater |
|---------|------|------|------|---------|
| [NCT01995071](https://clinicaltrials.gov/study/NCT01995071) | Fase 2 | Avsluttet | 89 | Dosisprogresjon sikkerhet/antivirale aktivitet av ABT-493+ABT-530 (glecaprevir/pibrentasvir) ved **HCV** genotype 1 – ikke en HBV-forsøk |
| [NCT02640157](https://clinicaltrials.gov/study/NCT02640157) | Fase 3 | Avsluttet | 506 | ENDURANCE-3: G/P vs sofosbuvir+daklatasvir ved **HCV** genotype 3 – ikke en HBV-forsøk |
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Fase 4 | Avsluttet | 87 | Kardiovaskulære utfall etter **HCV**-helbredelse hos HIV-koinfiserte pasienter – ikke en HBV-forsøk |
| [NCT02707952](https://clinicaltrials.gov/study/NCT02707952) | Fase 3 | Avsluttet | 295 | CERTAIN-1: G/P-effektivitet/sikkerhet hos japanske **HCV**-pasienter – ikke en HBV-forsøk |
| [NCT03092375](https://clinicaltrials.gov/study/NCT03092375) | Fase 3 | Avsluttet | 177 | G/P ± ribavirin ved NS5A-inhibitor-erfarne **HCV** GT1-pasienter – ikke en HBV-forsøk |
| [NCT03219216](https://clinicaltrials.gov/study/NCT03219216) | Fase 3 | Avsluttet | 100 | G/P hos behandlingsnyttige brasilianske **HCV** GT1–6-pasienter – ikke en HBV-forsøk |
| [NCT02441283](https://clinicaltrials.gov/study/NCT02441283) | Fase 2/3 | Avsluttet | 384 | Langsiktig holdbarhet/resistensoppfølging av glecaprevir/pibrentasvir ved **HCV** – ikke en HBV-forsøk |
| [NCT02446717](https://clinicaltrials.gov/study/NCT02446717) | Fase 2/3 | Avsluttet | 141 | G/P ± ribavirin hos **HCV**-pasienter som mislyktes tidligere DAA-terapi – ikke en HBV-forsøk |
| [NCT02243280](https://clinicaltrials.gov/study/NCT02243280) | Fase 2 | Avsluttet | 174 | SURVEYOR-I: G/P PK/effektivitet ved **HCV** GT1,4,5,6 – ikke en HBV-forsøk |
| [NCT02640482](https://clinicaltrials.gov/study/NCT02640482) | Fase 3 | Avsluttet | 304 | ENDURANCE-2: placebokontrollert G/P-forsøk ved **HCV** GT2 – ikke en HBV-forsøk |

**Ingen forsøk i dette bevisettet rekrutterte pasienter med det formål å behandle eller evaluere HBV-infeksjon.**

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [29485084](https://pubmed.ncbi.nlm.nih.gov/29485084/) | 2018 | Oversikt | Lancet Infect Dis | Diskuterer behov for HBV-vaksinasjon *etter* vellykket HCV-behandling – et koinfeksjons-/prevensjonsmotiv, ikke bevis på pibrentasvir-aktivitet mot HBV |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Oversikt | World J Gastroenterol | Oversikt over pediatrisk HBV/HCV-behandling; bemerker at nåværende HBV-terapi ikke er kurativ – kun bakgrunnsinformasjon |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | Retrospektiv | Klin Mikrobiol Infekc Lek | Retrospektiv gjennomgang av antiviralbehandlingsfrekvens/effektivitet for kronisk HBV og HCV hos barn – tester ikke pibrentasvir ved HBV |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | Tverrseksjonell | Annals of Hepatology | Sammenlikner HBV vs HCV-medikament**prising** på tvers av land – økonomisk analyse, ingen effektivitetsdata |
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Kohorte | J Viral Hepatitis | Virkelig GLE/PIB-effektivitet/sikkerhet ved **HCV** hos pasienter med alvorlig nyresvikt (Taiwan) – kun HCV |
| [35431505](https://pubmed.ncbi.nlm.nih.gov/35431505/) | 2022 | Kohorte | World J Gastroenterol | Virkelig DAA-effektivitet ved HIV/**HCV** genotype 6-koinfeksjon – kun HCV |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Oversikt | Lancet Gastroenterol Hepatol | HCV-behandling hos barn/ungdom innenfor global strategi for viralhepatittelimineringer – HCV-fokusert |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Oversikt | Eur J Gen Pract | Generell oversikt over kronisk HCV-diagnose og -behandling – kun HCV |
| [34298832](https://pubmed.ncbi.nlm.nih.gov/34298832/) | 2021 | Oversikt | Cancers | Risiko for hepatocellulært karsinom ved kronisk nyresykdom – ikke spesifikt for pibrentasvir eller HBV |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Oversikt | Clin Pharmacokinetics | PK/PD-oversikt over HCV DAA-regimer inkludert glecaprevir/pibrentasvir – kun HCV |

**Ingen publikasjon i denne samlingen rapporterer direkte antivirale effektivitets- eller kliniske utfallsdata for pibrentasvir mot HBV.**

---

## Markedsinformasjon for Norge

Pibrentasvir har for tiden **ingen markedsføringstillatelse i Norge** (0 lisenser på fil; markedsstatus: Ikke markedsført). Ingen produkt-/autorisasjonsopplysninger er tilgjengelige for oppsummering.

---

## Sikkerhetshensyn

Vær vennlig se pakningsvedlegget for sikkerhetsinformasjon. (Viktige advarsler, kontraindikasjoner og interaksjondata for legemidler er ikke ennå tilgjengelige i dette bevisettet – henting av TFDA/produsentens etikett er flagget som en **Blokkering** datakløft.)

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Til tross for et høyt TxGNN-likhetsresultat, er hver klinisk forsøk og nesten hver publikasjon som støtter denne «HBV»-prediksjonen faktisk bevis for pibrentasvirens etablerte HCV-indikasjon – ingen tester HBV-spesifikk antiviralaktivitet. Pibrentasvirmekanismen (selektiv HCV NS5A-hemming) har ingen kjent motpart-mål i HBV, og det samme urimelige mønsteret (HIV, hepatitt A/E, veterinær lentivirusinfeksjoner, til og med en ikke-relatert nevronevolutiv lidelse) vises på tvers av hele topp-10-prediksjonstabellen for dette stoffet, noe som indikerer et sannsynlig kunnskapsgrafartefakt i stedet for et genuint omformål-signal. Kombinert med at stoffet er umarkedsført i Norge og en Blokkering-mangel på kjerneinformasjon fra sikkerhetsetikett, er det ikke grunnlag for å fremme denne kandidaten på dette tidspunktet.

**For å gå videre er følgende nødvendig:**
- Genuint in vitro/in vivo-bevis for pibrentasvir antiviralaktivitet mot HBV (eksisterer for tiden ikke)
- TFDA/produsentens pakningsvedlegg for advarsler og kontraindikasjoner (Blokkering datakløft)
- Verifisert mekanisme-for-virkning-dokumentasjon fra DrugBank (Høyalvorlighets datakløft)
- En sanitetskontroll på TxGNN-sykdomsinnstilling-omegnen for dette stoffet, gitt mønsteret av urimelig høy-scorende prediksjoner på tvers av hele kandidatlisten

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

