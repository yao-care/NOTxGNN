---
layout: default
title: Bupropion
parent: Kun modellprediksjon (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bupropion: predikert ny indikasjon Oppmerksomhetssvikt-hyperaktivitetsforstyrrelse (ADHD) (evidensnivå L5). Opprinnelig indikasjon: Fedme og overvekt"
monitor_inn: "Bupropion"
predicted_indications: ["attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "chondromyxoid fibroma", "proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "benign paroxysmal torticollis of infancy", "trigeminal nerve neoplasm", "obsolete hypertelorism (disease)"]
---

# Bupropion
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Bupropion: Fra fedme til oppmerksomhetssvikt-hyperaktivitetsforstyrrelse (ADHD)
{: .text-alpha }

## Én-setnings sammendrag

Bupropion er i Norge (via EU-godkjenningen for Mysimba) registrert for behandling av fedme og overvekt.
TxGNN-modellen forutsier at legemidlet kan være effektivt ved **oppmerksomhetssvikt-hyperaktivitetsforstyrrelse (ADHD)**,
og retningen støttes for øyeblikket av **6 kliniske studier** og **20 publikasjoner**, blant dem en Cochrane-oversikt om bupropion ved ADHD hos voksne.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Fedme og overvekt |
| Predikert ny indikasjon | Oppmerksomhetssvikt-hyperaktivitetsforstyrrelse (ADHD) |
| TxGNN-prediksjonsscore | 99,99 % |
| Evidensnivå | L1 (basert på de sammenstilte dataene; se merknad under kliniske studier) |
| Markedsstatus i Norge | Kun avregistrert |
| Antall godkjenninger | 1 (avregistrert) |
| Anbefalt beslutning | Proceed with Guardrails (gå videre med sikkerhetsrammer) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanismen mangler i de sammenstilte dataene. Basert på kjent informasjon hemmer bupropion gjenopptaket av noradrenalin (NET) og dopamin (DAT). Det er de samme katekolaminerge banene som etablerte ADHD-legemidler, som sentralstimulerende midler og atomoksetin, virker på.

Den opprinnelige indikasjonen (fedme/overvekt) bygger på bupropions effekt på sentrale appetitt- og belønningsbaner, og disse overlapper med de dopaminerge og noradrenerge systemene som er involvert i ADHD. Bupropion er dessuten kjent for bruk ved depresjon og røykeslutt, og litteraturen omtaler også bruk ved ADHD som ikke-stimulerende alternativ.

Prediksjonen er dermed mekanistisk plausibel. Samtidig er bupropion ikke førstevalg ved ADHD, og oversiktsartiklene beskriver det som et alternativ når sentralstimulerende midler ikke fungerer eller ikke tåles.

---

## Klinisk studieevidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Fase 3 | Fullført | 162 | Randomisert, dobbeltblindet, placebokontrollert 8-ukers studie av bupropion XL 300–450 mg/dag ved ADHD hos voksne |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Fase 4 | Fullført | 105 | Bupropion ved ADHD hos ungdom med samtidig rusmiddelbruk |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Fase 2/3 | Fullført | 115 | Behandling av ADHD hos voksne i metadonbehandling (bupropion-arm bør verifiseres) |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | Ikke angitt | Fullført | 32 | Åpen studie av bupropion SR ved ADHD hos voksne med rusmiddelbruk |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | Ikke angitt | Fullført | 32 | Kokainmisbruk og oppmerksomhetssvikt; legemiddelarm er ikke spesifisert |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Tidlig fase 1 | Trukket tilbake | 0 | Residivforebygging ved stimulansmisbruk; ingen data, fokus ikke på ADHD |

**Merknad om evidensnivå:** Kun én fullført fase 3-studie (NCT00048360) er identifisert, supplert med en fase 2/3-studie og en fase 4-studie. Nivået L1 er hentet fra de sammenstilte dataene, men strengt tatt er kriteriet om minst to fullførte fase 3-studier ikke klart oppfylt. Et mer forsiktig anslag ville vært L2.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [28965364](https://pubmed.ncbi.nlm.nih.gov/28965364/) | 2017 | Cochrane-oversikt | Cochrane Database Syst Rev | Vurderer bupropion ved ADHD hos voksne som alternativ til sentralstimulerende midler |
| [30097390](https://pubmed.ncbi.nlm.nih.gov/30097390/) | 2018 | Systematisk oversikt/nettverksmetaanalyse | Lancet Psychiatry | Sammenligner effekt og tolerabilitet av ADHD-legemidler hos barn, ungdom og voksne |
| [33085721](https://pubmed.ncbi.nlm.nih.gov/33085721/) | 2020 | Systematisk oversikt/nettverksmetaanalyse | PLoS One | Sammenligner farmakologiske behandlinger av ADHD hos voksne |
| [37405312](https://pubmed.ncbi.nlm.nih.gov/37405312/) | 2023 | Oversikt | Health Psychol Res | Bupropions effekter ved depresjon, ADHD og røykeslutt, inkludert mekanismer og interaksjoner |
| [38915262](https://pubmed.ncbi.nlm.nih.gov/38915262/) | 2024 | Oversikt | Expert Rev Neurother | Ikke-stimulerende legemidler ved ADHD hos voksne |
| [39172673](https://pubmed.ncbi.nlm.nih.gov/39172673/) | 2024 | Oversikt | Am Fam Physician | Diagnostikk og behandling av ADHD hos voksne |
| [26601963](https://pubmed.ncbi.nlm.nih.gov/26601963/) | 2016 | Oversikt | Curr Pharm Des | Effekter og bivirkninger av ADHD-legemidler, bupropion nevnt blant alternativene |
| [24259638](https://pubmed.ncbi.nlm.nih.gov/24259638/) | 2014 | Oversikt | Ann Pharmacother | Patofysiologi, årsaker og behandling av ADHD |
| [27738872](https://pubmed.ncbi.nlm.nih.gov/27738872/) | 2017 | Sammenligning av flere behandlinger | Mol Neurobiol | Effekt og sikkerhet av ADHD-behandling hos barn og ungdom |
| [19023824](https://pubmed.ncbi.nlm.nih.gov/19023824/) | 2008 | Post hoc-analyse | Nicotine Tob Res | Røykeslutt med bupropion og nikotinplaster i relasjon til uoppmerksomhet/hyperaktivitet |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/003687 | Mysimba | Ikke angitt | Fedme og overvekt (status: avregistrert) |

---

## Sikkerhetsvurderinger

Pakningsvedlegget er ikke tilgjengelig i de sammenstilte dataene, og sikkerhetsinformasjon fra preparatomtalen må derfor innhentes før videre arbeid.

**Kontraindikasjoner fra kunnskapsgrafen (ikke preparattekst):** Kunnskapsgrafen (PrimeKG) knytter bupropion til følgende tilstander, som bør vurderes nøye:
- **Nevrologiske/psykiatriske:** epilepsi, manisk bipolar lidelse, psykotiske lidelser, schizofreniform og schizoaffektiv lidelse, angstlidelse, annen psykisk lidelse, rusmiddelavhengighet, opioid-/morfinavhengighet
- **Spiseforstyrrelser:** anoreksi og bulimi
- **Kardiovaskulære:** hypertensjon, hjerteinfarkt, koronar trombose
- **Lever og nyre:** leversvikt, leversykdom, skrumplever, nyresykdom, galleblæresykdom
- **Andre:** hemoglobinopati, svulster i sentralnervesystemet, pyoureter

**Legemiddelinteraksjoner:** Interaksjonsdataene beskriver kun farmakologiske målproteiner (noradrenalintransportør NET og dopamintransportør DAT), ikke kliniske interaksjoner mellom legemidler. Vurderingen i dataene nevner at CYP2D6-interaksjoner bør gjennomgås.

**Sentrale forholdsregler:** DosEavhengig krampefare, forsiktighet ved rusmiddelbruk eller spiseforstyrrelser og blodtrykkskontroll.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (gå videre med sikkerhetsrammer)**

**Begrunnelse:**
Flere fullførte kliniske studier (blant dem en placebokontrollert fase 3-studie), en Cochrane-oversikt og flere nettverksmetaanalyser støtter bupropion ved ADHD, og mekanismen (NET/DAT-hemming) er plausibel. Likevel er markedsstatus «kun avregistrert», og sikkerhetsprofilen (krampefare, hypertensjon, rusmiddelbruk, spiseforstyrrelser) krever tydelige rammer.

**For å gå videre kreves følgende:**
- Innhente og analysere preparatomtale/pakningsvedlegg (advarsler og kontraindikasjoner) for å kunne gjennomføre sikkerhetsscreeningen
- Fullstendige mekanismedata fra DrugBank
- Avklare regulatorisk status og tilgjengelige formuleringer i Norge, siden Mysimba-godkjenningen er avregistrert og bupropion-produkter for andre indikasjoner må vurderes
- Verifisere legemiddelarm i NCT00061087 og NCT00000268 samt bekrefte evidensnivået (L1 mot L2) mot registerdata
- Utarbeide en plan for sikkerhetsovervåking: krampeterskel, blodtrykk, CYP2D6-interaksjoner og screening for rusmiddelbruk og spiseforstyrrelser

---

## Øvrige prediksjoner (kort)

De øvrige prediksjonene har svakere støtte:
- **ADHD, uoppmerksom type** (score 99,99 %): Evidensnivå L3, kun overordnede ADHD-data og én post hoc-analyse. Vurderes som et forskningsspørsmål.
- **Faciodigitogenitalt syndrom, spesifikk utviklingsforstyrrelse, kondromyksoid fibrom, 16p11.2-mikrodelesjon, hypervitaminose, godartet paroksysmal torticollis hos spedbarn, trigeminusnevrom og «obsolete hypertelorism»:** Kun modellprediksjoner uten kliniske studier og med lite eller ingen relevant litteratur, uten påvisbar mekanistisk kobling. Anbefaling: **Hold**.
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

