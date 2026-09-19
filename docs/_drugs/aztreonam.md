---
layout: default
title: Aztreonam
parent: Høy evidens (L1-L2)
nav_order: 45
evidence_level: L2
indication_count: 10
---

# Aztreonam
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **10** stk.
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

# Aztreonam: Fra gram-negative infeksjoner til gonokkokk-urethritt

## Ensetnings-sammendrag

> Aztreonam er et monobaktam-antibiotikum brukt mot aerobe gram-negative bakterielle infeksjoner.
> Blant 10 TxGNN-predikerte indikasjoner, **Gonokkokk-urethritt** er den eneste kandidaten med meningsfull evidens,
> støttet av **1 fullført klinisk studie** og **8 publikasjoner** (inkludert 1 RCT).
> De gjenværende 9 kandidatene — inkludert modellens høyest-scorede prediksjon, hyperamylasemi — mangler enhver mekanistisk eller empirisk støtte og er flagget **Hold**.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Ikke bekreftet via lokale lisensieringsdata; etter generell farmakologi, aztreonam er indisert for infeksjoner forårsaket av aerobe gram-negative bakterier |
| Prediktert ny indikasjon | Gonokkokk-urethritt |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Status i Norges marked | Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Gjennomfør med forbehold |

**Merknad om rangering:** Bevisakkens høyest-rangerte prediksjon (hyperamylasemi, score 99.73%) og rangeringene 2–3, 5–7, 9–10 er alle annotert av repurposinggrunnlaget som å ha **ingen mekanistisk kobling** og **ingen klinisk/litteraturstøtte** (Hold, L5). Denne rapporten fokuserer på **Gonokkokk-urethritt (rangering 4)**, den eneste kandidaten med virkelige-verden-evidens, og noterer kort **Epiglottitt (rangering 8, L4, Forskningsspørsmål)** som et sekundært signal verdt oppfølging.

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er ingen formell MOA-registrering tilgjengelig i bevisakkelen (DrugBank MOA-felt: Manglende data). Basert på kjent farmakologi, aztreonam er et **monobaktam-antibiotikum** som selektivt binder til Penicillin-bindende protein 3 (PBP3) hos gram-negative bakterier, og hemmer bakteriell celleveggsyntes. Dets aktivitetsspektrum er begrenset til aerobe gram-negative organismer, med ubetydelig aktivitet mot gram-positive bakterier eller anaerobier.

*Neisseria gonorrhoeae* er en gram-negativ diplococcus, som plasserer gonokkokk-urethritt rett innenfor aztreonams kjente antibakteriell spektrum. Dette er derfor **ikke en ny mekanistisk slutning av TxGNN, men en direkte forlengelse av et etablert antibakteriell spektrum** — modellen har i hovedsak gjenoppdaget et farmakologisk forventet forhold. Dette forsterkes ytterligere av klinisk kontekst: CDC har identifisert antimikrobiell-resistente *N. gonorrhoeae* som et alvorlig folkehelseproblem, siden ceftriaxone (en tredje-generasjons cephalosporin) nå er nesten den eneste pålitelig effektive førstlinjeagenten. Gjenbruk av eldre, underutnyttede antibiotika som aztreonam har blitt eksplisitt foreslått i litteraturen som en strategi for å utvide behandlingsalternativene mot resistent gonorè, inkludert for faryngeal infeksjonslokalisering som er vanskeligere å utrydde.

Derimot er flere andre TxGNN-flaggede kandidater mekanistisk usannsynlige — for eksempel, Ureaplasma urethritt er forårsaket av cellevegglløse organismer (Mycoplasmataceae), mot hvilke en cellvegg-syntesehemmer som aztreonam teoretisk burde ha ingen effekt. Dette illustrerer viktigheten av evidens-nivå-triage i stedet for å handle på TxGNN-score alene.

---

## Klinisk bevis fra forsøk

| Forsøksnummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Fase 2/3 | Fullført | 32 | Enarmsstudie, åpen merking, demonstrasjonsstudie av aztreonam for faryngeal gonorè, utført som svar på CDCs identifikasjon av antimikrobiell-resistente *N. gonorrhoeae* som en alvorlig trussel; evaluerte et eldre, underutnyttet antibiotikum som et potensielt nytt alternativ gitt økende resistens mot førstlinjes cephalosporiner |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | RCT (enkeltdose) | Genitourinary Medicine | Enkelt 1g IM dose av aztreonam ryddet opp infeksjon hos 61 menn og 26 kvinner på nesten alle steder; godt tolerert, effektiv mot både penicillin-sensitive og penicillinase-produserende stammer |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Oversikt/Overvåking | J Infect Chemother | Gjennomgår fremvekst av cephem/aztreonam-resistente *N. gonorrhoeae* ikke formidlet av beta-lactamase; noterer at ingen kliniske behandlingsfeil med tredje-generasjons cephems og aztreonam hadde blitt rapportert til dags dato |
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Kohortstudie (enarm, åpen merking) | Antimicrob Agents Chemother | Enkeltdose IM aztreonam (2g) forsøk hos menn, utført for å identifisere nye gonorèbehandlingsalternativ midt i ceftriaxone-resistensbekymringer; understreker behovet for regimer effektive ved pharynx |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Kohortstudie | Hinyokika Kiyo | Japansk epidemiologisk og enkelt-dose terapi-studie av aztreonam for gonorèinfeksjoner; rapporterer resistansgrader blant kliniske isolater |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Kohortstudie | J Infect Dis | Demonstrerer aztreonam-effektivitet mot penicillinase-produserende, penicillin-resistente gonokokker midt i stigende globalt PPNG-utbredelse |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Kohortstudie | Jpn J Antibiot | Bakteriologisk og klinisk evaluering av aztreonam hos 30 menn med gonokkokk-urethritt, inkludert PPNG og ikke-PPNG-stammer |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Kohortstudie | Antimicrob Agents Chemother | 1g IM aztreonam sammenlignet med spektinomycin for ukomplisert gonorè; ingen behandlingsfeil med noen av medisinene på tvers av uretral, rektal og endocervical lokalisering |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Kohortstudie | G Ital Dermatol Venereol | Italiensk studie av aztreonam hos pasienter med akutt gonokkokk-urethritt (sammendrag ikke tilgjengelig) |

---

## Informasjon om Norges marked

Aztreonam er for tiden **ikke markedsført** i Norge, og ingen autorisasjonsregistreringer er tilgjengelige i denne bevisakkelen.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Ingen strukturerte advarsler, kontraindikasjoner eller data om vekselvirkninger mellom stoffer er for tiden tilgjengelige i bevisakkelen (DDI-søkstatus: ikke funnet).

---

## Konklusjon og neste trinn

**Beslutning: Gjennomfør med forbehold**

**Begrunnelse:**
Gonokkokk-urethritt er den eneste TxGNN-predikerte indikasjonen i denne bevisakkelen støttet av direkte mekanistisk rasjonale (gram-negative spektrumstilpasning), en fullført fase 2/3 klinisk studie, og en RCT ved siden av flere tiår gamle kohortstudier. Dette er en plausibel, evidens-støttet gjenbrukingskandidat — men den støttende studien (n=32) er liten og enarm, og mye av den støttende litteraturen forut for moderne resistensmønstre, så forbehold er berettiget før videre fremgang.

**For å fortsette, følgende er nødvendig:**
- Løs **DG001 (Blocking)**: få TFDA/lokale regulatoriske merkevaringsadvarsler og kontraindikasjoner — nødvendig før noen S1 sikkerhetspre-vurdering kan fortsette
- Løs **DG002 (High)**: få formell DrugBank MOA-registrering for å bekrefte mekanistisk analyse
- Siden stoffet ikke er for tiden markedsført i Norge, vurder gjennomførbarhet av import-/registreringsvei
- Gitt den små, enarmede naturen av den primære studien, vurder om ytterligere bekreftelsesdata (f.eks. større RCTs, nåværende resistansoversyn) finnes før klinisk bruk vurderes
- **Sekundært signal for oppfølging**: Epiglottitt (rangering 8, L4, Forskningsspørsmål) — mekanistisk plausibel (H. influenzae, gram-negative) men kun støttet av ikke-spesifikk gram-negative infeksjonskohorter; ennå ikke handlingsbar
- **Nedprioritiser**: Rangeringene 1–3, 5–7, 9–10 (inkludert det høyeste TxGNN-score, hyperamylasemi) — eksplisitt flagget som manglende mekanistisk eller empirisk støtte; ingen videre handling anbefalt på dette tidspunktet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

