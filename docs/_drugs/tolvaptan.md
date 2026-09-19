---
layout: default
title: Tolvaptan
parent: Kun modellprediksjon (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Tolvaptan
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

# Tolvaptan: Fra hyponatremi (SIADH) til autosomal dominant polycystisk nyresykdom (ADPKD)

## Sammendrag i én setning

> Tolvaptan er en vasopressin V2-reseptorantagonist som historisk brukes til behandling av hyponatremi relatert til SIADH, hjertesvikt og sirrhose.
> TxGNN-modellens toppprediksjon peker mot **polycystisk nyresykdom 3, med eller uten polycystisk leversykdom** — en sjelden monogen variant innenfor det bredere spekteret autosomal dominant polycystisk nyresykdom (ADPKD) —
> og denne retningen støttes av **to landemerke-gjennomførte fase 3 RCT-er** (TEMPO 3:4, REPRISE) pluss **20 støttepublikasjoner**, inkludert konsensusveiledninger og en Cochrane systematisk oversikt. Bemerkelsesverdig er at tolvaptan allerede har godkjent ADPKD-indikasjon i utlandet (f.eks. Jinarc/Jynarque i EU/USA/Japan), så dette forstås best som at modellen korrekt gjenkjenner en etablert, høy-tillits-indikasjon snarere enn et rent nytt signal.

---

## Hurtigoversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Hyponatremi på grunn av SIADH (Samsca) — etablert global etikett; **ikke bekreftet i det norske regulatoriske datapakken**, som for tiden viser 0 autorisasjoner |
| Forutsagt ny indikasjon | Polycystisk nyresykdom 3, med/uten polycystisk leversykdom (ADPKD/PLD-spektrum) |
| TxGNN-prediksjonspoengsum | 99.99% (rang 319 totalt) |
| Bevisnivå | L1 (≥2 gjennomførte fase 3 RCT-er: TEMPO 3:4, REPRISE) |
| Norgesmarkeds status | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Fortsett med sikkerhetstiltak |

---

## Hvorfor er denne prediksjonen rimelig?

DrugBank-baserte virkningsmekanismedata er for tiden utilgjengelige (datagap DG002). Imidlertid identifiserer litteraturbevisene som er samlet i denne pakken konsistent og uavhengig tolvaptan som en **selektiv vasopressin V2-reseptorantagonist**. Ved å blokkere V2-reseptor-signalering i nyrenes samlerørsceller, reduserer tolvaptan intracellulær cAMP, som er den viktigste driveren for epitelproliferasjon og væskesekresjon i cystelinjene ved polycystisk nyresykdom. Denne mekanistiske forbindelsen — cAMP-hemming som stopper cystogenese — er den farmakologiske begrunnelsen gjentatte ganger sitert på tvers av ADPKD-litteraturen i denne pakken (f.eks. PMID 35328738, 40126492).

Forholdet mellom tolvaptans opprinnelige bruk (akvadurse ved hyponatremi/væskeovertilstand) og den forutsagte indikasjon er mekanistisk sammenhengende: begge applikasjoner utnytter V2-reseptorblokade, bare i forskjellige målvev (systemisk vannhåndtering vs. nyrecystepitel). Viktig å merke er at dette ikke er spekulativ ekstrapolasjon — tolvaptan **bærer allerede godkjent ADPKD-indikasjon i USA, EU og Japan** (merkenavn Jynarque/Jinarc), bygget på de samme TEMPO 3:4- og REPRISE-forsøkene som denne bevisspakken identifiserer. TxGNN-modellen reproduserer derfor en godt validert, virkelige-verden-indikasjon snarere enn å foreslå noe uprøvd.

Én forbehold: den spesifikke forutsagte sykdomstermen er "Polycystisk nyresykdom **3**" (en sjeldnere PKD3 monogen undertype, ulik den langt mer vanlige PKD1/PKD2-drevne ADPKD). Alle kliniske bevis i denne pakken (TEMPO 3:4, REPRISE, pediatriske forsøk) ble gjennomført i den bredere ADPKD-populasjonen, ikke PKD3 spesifikt. Ontologikartleggingen fanger sannsynligvis den generelle ADPKD/PLD-sykedomsfamilien, men denne distinksjonen bør verifiseres før noen indikasjonsspesifikk regulatorisk påstand blir fremsatt.

---

## Klinisk forsøksbevis

For tiden ingen relaterte kliniske forsøk registrert i det strukturerte `clinical_trials`-feltet for denne indikasjon. (Merknad: de sentrale forsøkene som etablerte denne indikasjon — TEMPO 3:4 og REPRISE — er fanget som publisert litteratur nedenfor snarere enn som registreringsposter i dette datauttrekket.)

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|-----------|----------|
| [23121377](https://pubmed.ncbi.nlm.nih.gov/23121377/) | 2012 | RCT (fase 3, TEMPO 3:4) | NEJM | Tolvaptan bremset veksten i totalt nyrevolum og nedgangen i eGFR i tidlig-stadium ADPKD |
| [29105594](https://pubmed.ncbi.nlm.nih.gov/29105594/) | 2017 | RCT (fase 3, REPRISE) | NEJM | Bevart nyrefunksjon i senere-stadium ADPKD; oftere elevasjoner i aminotransferase/bilirubin observert |
| [38091246](https://pubmed.ncbi.nlm.nih.gov/38091246/) | 2024 | RCT (pediatrisk, NCT02964273) | Pediatr Nephrol | Evaluerte tolvaptan sikkerhet/farmakodinamikk hos barn (5–17 år) med ADPKD |
| [37150675](https://pubmed.ncbi.nlm.nih.gov/37150675/) | 2023 | Systematisk oversikt/Metaanalyse | Nefrologia | Bekreftet samlet effektivitet og sikkerhetsprofil for tolvaptan i ADPKD |
| [39356039](https://pubmed.ncbi.nlm.nih.gov/39356039/) | 2024 | Systematisk oversikt (Cochrane) | Cochrane Database Syst Rev | Gjennomgikk sykdomsmodifiserende midler, inkludert tolvaptan, for forebygging av ADPKD-progresjon |
| [35134221](https://pubmed.ncbi.nlm.nih.gov/35134221/) | 2022 | Konsensuserklæring | Nephrol Dial Transplant | ERA Working Group/PKD International konsensus om evidensbasert tolvaptan-initiering i ADPKD |
| [40126492](https://pubmed.ncbi.nlm.nih.gov/40126492/) | 2025 | Oversikt | JAMA | Omfattende ADPKD-oversikt som dekker patofysiologi og behandling, inkludert tolvaptan |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Oversikt | Clin Liver Dis | Bekrefter at tolvaptan bremser nedgang i nyrefunksjon og cystevekst i ADPKD/PCLD-overlap |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Retningslinje (EASL) | J Hepatol | Klinisk retningslinje for cystisk leversykdom, inkludert polycystisk lever-sykdom-komponenten |
| [35328738](https://pubmed.ncbi.nlm.nih.gov/35328738/) | 2022 | Oversikt | Int J Mol Sci | Gjennomgår ADPKD-cystogenese-patofysiologi og behandlings-framskritt |

---

## Markedsinformasjon for Norge

Tolvaptan har for tiden **ingen markedsføringsautorisasjoner på fil i Norge** (0 lisenser; markedsstatus "Ikke markedsført"). Ingen produkt-/doseformsdata er tilgjengelige for oppsummering.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon — ingen strukturerte advarsler, kontraindikasjoner eller DDI-data er for tiden tilgjengelige i denne bevisspakken (flagget som **blokkering** datagap DG001).

Som sagt rapporterer den sentrale REPRISE-forsøket (PMID 29105594) eksplisitt **hyppigere elevasjoner i lever-aminotransferaser og bilirubin** med tolvaptan kontra placebo — dette hepatotoksisitetssignalet er godt dokumentert i tolvaptans godkjente etiketter andre steder (boksadvarsel i USA) og bør behandles som en kjent klasserelevant risiko i påvente av bekreftelse av den lokale etiketten.

---

## Konklusjon og neste trinn

**Beslutning: Fortsett med sikkerhetstiltak**

**Begrunnelse:**
Effektivitetsbevis for tolvaptan i ADPKD er ekskepsjonelt sterkt (L1 — to gjennomførte, publiserte fase 3 RCT-er pluss konsensusveiledninger), og indikasjon er allerede godkjent i større markeder. Imidlertid har Norge null eksisterende autorisasjoner og en blokkering datagap på lokale advarsler/kontraindikasjoner, så markedsinngang kan ikke fortsette uten å fullføre sikkerhetsdossieret.

**For å fortsette, er følgende nødvendig:**
- Løse DG001 (blokkering): få den godkjente EU/Norge-ekvivalente SmPC (f.eks. Jinarc) for TFDA-ekvivalente advarsler og kontraindikasjoner
- Løse DG002 (høy): bekrefte DrugBank MOA-rekord for å formelt støtte den mekanistiske begrunnelsen
- Verifisere om målontologibegrepet (PKD3-spesifikt) bør forenes med den bredere ADPKD (PKD1/PKD2)-populasjonen som ble studert i TEMPO 3:4/REPRISE
- Etablere en hepatisk overvåkingsprotokoll (LFT) gitt det dokumenterte hepatotoksisitetssignalet, før norsk MAA-innsending

**Merknad om lavere-rangerte prediksjoner:** Ranger 2–10 (renal-hepatic-pancreatic dysplasia, karyomegalic interstitial nephritis, thoracic malformation, Joubert syndrome, hypertrichosis, periodontal-component syndromes, Dandy-Walker malformation syndrome, osv.) bærer L4–L5-bevis best, med de fleste litteraturtreff vurdert som irrelevante eller utenfor mål (f.eks. periodontitis-litteraturen hentet for rang 9 har ingen mekanistisk forbindelse til tolvaptan). Disse er på vent (Hold) og forfølges ikke videre i denne rapporten.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

