---
layout: default
title: Pertuzumab
parent: Kun modellprediksjon (L5)
nav_order: 276
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: Fra HER2-positiv brystkreft til progesteronreseptor-positiv brystkreft

## Sammendrag i én setning

> Pertuzumab er et HER2-rettet monoklonal antistoff allerede etablert (ifølge kilde-kliniske forsøk) som en FDA-godkjent behandling for HER2-positiv brystkreft, vanligvis kombinert med trastuzumab og en taksan.
> TxGNN-modellen forutsier at det også kan være effektivt for **progesteronreseptor (PR) positiv brystkreft**,
> med **10 kliniske forsøk** og **20 publikasjoner** som for tiden er knyttet til det — selv om det er merkbart at flere av de beste forsøkene faktisk rekrutterte **PR/ER-negative** populasjoner, som er den motsatte molekylære profilen av den forutsagte indikasjonen.
> Gitt denne bevismessige uoverensstemmelsen pluss flere uløste datamangler (virkningsmekanisme, sikkerhetsetikett, status på norskemarkedet), krever denne kandidaten manuell kurering før videre tiltak.

---

## Rask oversikt

| Emne | Innhold |
|------|------|
| Opprinnelig indikasjon | HER2-positiv brystkreft (etablert bruk, referert på tvers av forsøksbevisgrunnlaget; ikke separat dokumentert i Bevisspakkens regulatoriske felt) |
| Forutsagt ny indikasjon | Progesteronreseptor-positiv brystkreft |
| TxGNN-prediksjonspoengsum | 99.93% |
| Bevisnivå | L3 (bevis eksisterer, men er i stor grad indirekte/uoverensstemmende — se begrunnelse nedenfor) |
| Status på norskemarkedet | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | **I bero** |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte virkningsmekanisme-data for pertuzumab er ikke tilgjengelige i denne Bevisspakken (flagget som en datamangler av høy alvorlighetsgrad). Basert på informasjon innebygd i de støttende kliniske forsøkspostene, er pertuzumab et monoklonal antistoff som "blokkerer medlemmer av en familie av proteiner som inkluderer Human Epidermal Growth Factor Receptor 2 (HER2)" og brukes sammen med trastuzumab (og vanligvis en taksan som docetaxel) som standard-of-care-terapi for HER2-positiv brystkreft, både i neoadjuvant/adjuvant og metastatisk sammenheng.

Den forutsagte nye indikasjonen — PR-positiv brystkreft — er ikke en distinkt sykdom, men en hormonreseptor-subklassifisering som kan forekomme sammen med HER2-positivitet (det vil si "trippel-positiv" eller HR+/HER2+ brystkreft). Flere forsøk i bevissettet studerer direkte denne overlappingspopulasjonen (for eksempel NCT02689921 som evaluerer aromatase-hemmer + pertuzumab/trastuzumab i HR+/HER2+ sykdom; NCT00999804 sammenligner lapatinib+trastuzumab ± endokrin terapi i HER2-overeksprimering, hormonreseptor-relevant sykdom), som støtter en plausibel mekanistisk rasjonale: dual HER2-blokkering kombinert med endokrin terapi i HR+/HER2+ tumorer.

Imidlertid er en vesentlig del av de "beste" siterte forsøkene for denne spesifikke prediksjonen (for eksempel NCT04629846, NCT03726879) faktisk rekrutterte **ER/PR-negative** eller hormonreseptor-uselekterte HER2-positive populasjoner — den motsatte eller en ikke-samsvarende biomarkør-profil i forhold til den forutsagte indikasjonen. Dette antyder at bevisinnhentingen fanget opp generell "pertuzumab + HER2-positiv brystkreft"-litteratur i stedet for PR-positiv-spesifikk data, og prediksjonen selv kan ganske enkelt re-identifisere en allerede dekket biomarkør-undergruppe av legemidlets eksisterende godkjent bruk i stedet for en genuint ny terapeutisk retning.

---

## Klinisk forsøksbevis

| Forsøksnummer | Fase | Status | Inklusjon | Viktige funn |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Fase 3 | Fullført | 517 | Pertuzumab-biosimilar (QL1209) vs. referanse pertuzumab + docetaxel i HER2-positiv, **ER/PR-negative** tidlig/lokalt fremskridden brystkreft (uoverensstemmende biomarkør-profil) |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Fase 3 | Aktivt, ikke rekruttering | 398 | Biosimilar (BCD-178) vs. Perjeta som neoadjuvant terapi i ER/PR-negative HER2-positiv brystkreft |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Fase 2 | Aktivt, ikke rekruttering | 164 | T-DM1 + pertuzumab preoperativ terapi; utforsker HER2-heterogenitet, ikke PR-status-spesifikk |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Fase 2 | Fullført | 417 | Neoadjuvant Herceptin/docetaxel/pertuzumab kombinasjoner i HER2-positiv brystkreft (uselektert for PR-status) |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Fullført | 1151 | Retrospektiv ikke-intervensjonstudie av HER2-lav prevalens og behandlingsmønstre; ikke PR-spesifikk |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Fase 2 | Trukket tilbake | 0 | Neoadjuvant paclitaxel i nigerianske kvinner med brystkreft; trukket tilbake, ingen inklusjon |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Fase 2 | Ukjent | 7 | Neoadjuvant aromatase-hemmer + pertuzumab/trastuzumab (kjemoterapi-fri) spesifikt i **HR+ (ER+/PR+) HER2+** lokalisert brystkreft — direkte relevant, men veldig liten (n=7) og ukjent status |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Fase 3 | Fullført | 454 | IMpassion050: atezolizumab vs. placebo med neoadjuvant kjemoterapi + trastuzumab/pertuzumab i tidlig HER2-positiv brystkreft; ikke stratifisert etter PR-status |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Fase 2 | Aktivt, ikke rekruttering | 128 | Neoadjuvant lapatinib + trastuzumab ± endokrin terapi i HER2-overeksprimering brystkreft; relevant til HR-vei-samspill |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Fase 2 | Avsluttet | 139 | DECRESCENDO: deeskalert adjuvant kjemoterapi i HER2+, **ER-negative**, lymfeknutte-negative tidlig brystkreft — igjen en uoverensstemmende (ER-negative) populasjon |

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (5-års oppfølging) | Lancet Oncology | NeoSphere-forsøk: neoadjuvant pertuzumab + trastuzumab forbedret patologisk komplett respons i HER2-positiv brystkreft |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (fase 2) | Annals of Oncology | WSG-ADAPT HER2+/HR- forsøk: 12-ukers neoadjuvant dual HER2-blokkering ± paclitaxel, deeskaleringstrategi |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II: endokrin terapi + trastuzumab/pertuzumab vs. deeskalert kjemoterapi i **HR-positiv/HER2-positiv** tidlig brystkreft — direkte relevant til PR-positiv populasjon |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (fase 3 ekvivalens) | British Journal of Cancer | QL1209 biosimilar vs. referanse pertuzumab i HER2-positiv, **ER/PR-negative** brystkreft (uoverensstemmende populasjon) |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (fase 2, åpen merking) | J Clin Oncol | PERTAIN-forsøk: trastuzumab + aromatase-hemmer ± pertuzumab i **HER2-positiv og hormonreseptor-positiv** metastatisk/LABC — direkte relevant |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Retningslinje | J Clin Oncol | ASCO-retningslinje oppdatering på systemisk terapi for HER2-positiv fremskridden brystkreft |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Oversikt | Cancer Treatment Reviews | Oversikt over HR/HER2-positiv brystkreftsbiologi og samspill mellom ER og HER2-veier |
| [33662161](https://pubmed.ncbi.nlm.nih.gov/33662161/) | 2021 | Oversikt | Eur J Clin Invest | CDK4/6 og PI3K-hemmer som fremvoksende kombinasjonsstrategier i HER2-positiv brystkreft |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Oversikt | Breast Cancer (Tokyo) | Fremskritt innen iboende signalveisinteraksjoner og klinisk translasjon av HR+/HER2+ brystkreft |
| [32905036](https://pubmed.ncbi.nlm.nih.gov/32905036/) | 2020 | Oversikt | Cureus | Terapistrategier for HER2-positiv metastatisk brystkreft, dekking av reseptor-subtyping inkludert PR-status |

---

## Informasjon om norskemarkedet

Pertuzumab er **ikke for tiden markedsført i Norge** — ingen autorisasjonspostinger er på fil (`total_licenses = 0`). Ingen original godkjent-indikasjon tekst er tilgjengelig fra lokale regulatoriske kilder for å verifisere mot den globale (FDA/EMA) godkjent indikasjonen referert i det kliniske forsøksbeviset.

---

## Cytotoksisitet

Pertuzumab er et antineoplastisk biologikum (anti-HER2 humanisert monoklonal antistoff), så dette avsnittet gjelder, selv om det **ikke** er et konvensjonelt cytotoksisk kjemoterapi-middel.

| Emne | Innhold |
|------|------|
| Klassifisering av cytotoksisitet | Målrettet terapi (HER2-dimerisering-inhibitor monoklonal antistoff) |
| Risiko for myelosupresjon | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Klassifisering av emetogenitet | Vennligst se pakningsvedlegget for advarsler og forholdsregler |
| Overvåkingselementer | Hjertefunksjonsoversikt (LVEF) er standardpraksis for anti-HER2-terapi gitt kjent klasserelatert kardiotoksisitetsrisiko, særlig i kombinasjonsregimer |
| Håndteringsbeskyttelse | Vennligst se pakningsvedlegget for advarsler og forholdsregler |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Alle sikkerhetsfelt — nøkkeladvarsler, kontraindikasjoner, og legemiddelinteraksjoner — er for tiden ikke tilgjengelig i denne Bevisspakken; TFDA/etikett-datainnhenting er flagget som en datamangler med **Blokkering**-alvorlighetsgrad.)

---

## Konklusjon og neste skritt

**Beslutning: I bero**

**Begrunnelse:**
En datamangler med Blokkering-alvorlighetsgrad (manglende TFDA-etikett advarsler/kontraindikasjoner) forhindrer denne kandidaten fra å gå inn i foreløpig sikkerhetsevalsering (S1), og virkningsmekanisme-data som er nødvendig for å vurdere biologisk plausibilitet er også manglende. I tillegg viser det kliniske forsøksbeviset som er mest nært forbundet med denne spesifikke prediksjonen en merkbar populasjonsuoverensstemmelse (flere viktige forsøk rekrutterte PR/ER-**negative**, ikke PR-**positive**, pasienter), og den "nye" indikasjonen kan i betydelig grad overlappe med pertuzumabs allerede-etablert bruk i HER2-positiv brystkreft i stedet for å representere en distinkt gjenbruksmulighet.

**For å fortsette, er følgende nødvendig:**
- TFDA-pakningsvedlegg / etikett-data (advarsler, kontraindikasjoner) for å fullføre S1 sikkerhetsevalsering
- Bekreftet virkningsmekanisme fra DrugBank eller produsent-etikett
- Manuell omvurdering av relevansflaggene for klinisk forsøk og litteratur (flertall for tiden markert "avventende") for å skille PR-positiv-spesifikk bevis fra generelt HER2-positiv brystkreft bevis
- Avklaring på hvorvidt denne forutsagte indikasjonen representerer en genuint ny bruk versus en biomarkør-undergruppe allerede dekket av pertuzumabs eksisterende godkjent indikasjon
- Norge/EU regulatorisk status bekreftelse, siden legemidlet for tiden har null lokale autorisasjoner på fil

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

