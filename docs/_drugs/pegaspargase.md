---
layout: default
title: Pegaspargase
parent: Høy evidens (L1-L2)
nav_order: 268
evidence_level: L1
indication_count: 10
---

# Pegaspargase
{: .fs-9 }

Evidensnivå: **L1** | Predikerte indikasjoner: **10** stk.
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

# Pegaspargase: Fra akutt lymfoblastisk leukemi til prekursor lymfoblastisk lymfom/leukemi

## Sammenfatting i én setning

Pegaspargase er en PEGylert form av *E. coli* L-asparaginase som brukes som kjernepreparat i behandlingen av akutt lymfoblastisk leukemi (ALL). TxGNN-modellens toppprediksjon, **prekursor lymfoblastisk lymfom/leukemi**, ligger innenfor det samme sykdomsspekteret som legemidlet allerede behandler – dette er ikke en ny repurposing-hypotese, men en bekrefting av etablert standard-of-care, støttet av **50 kliniske forsøk** og **20 publikasjoner** i bevissamlingen.

> ⚠️ **Viktig forbehald**: I motsetning til en typisk repurposing-kandidat overlapper denne predikerte indikasjonen vesentlig med pegaspargas' kjente/godkjente bruk. Bevissamlingen selv flaggerer dette eksplisitt som "en utvidelse av en allerede etablert behandling, ikke en ny repurposing-hypotese." Rapporten nedenfor presenteres for fullstendighet og regulatorisk statussporing, ikke som et tegn på en ny oppdagelse.

---

## Oversikt

| Punkt | Innhold |
|------|------|
| Originalindikasjon | Akutt lymfoblastisk leukemi (ALL) – pegaspargas' etablerte indikasjon, basert på mekanistiske/begrunnelsesdata i bevissamlingen (ingen norsk lisensregistrering eksisterer, da legemidlet ikke er lokalt markedsført) |
| Predikert ny indikasjon | Prekursor lymfoblastisk lymfom/leukemi |
| TxGNN prediksjonspoeng | 99.96% |
| Bevisnivå | L1 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt avgjørelse | Fortsett med sikringsmekanismer |

---

## Hvorfor er denne prediksjonen rimelig?

Pegaspargase tømmer serumasparagin ved å hydrolysere det til asparaginsyre og ammoniakk. Lymfoblaster mangler karakteristisk (eller har svært lavt nivå av) asparaginsyntetas, noe som betyr at de ikke kan syntetisere sitt eget asparagin og er helt avhengige av ekstracellulær pool – uttømming av pegaspargase er derfor selektivt dødbringende for disse cellene mens normale vev som bevarer syntetas-aktivitet blir skånet. Dette er en veletablert, tiår gammel mekanisme, ikke en nylig konkludert.

"Prekursor lymfoblastisk lymfom/leukemi" og "akutt lymfoblastisk leukemi" beskriver overlappende punkter på det samme sykdomskontinuumet (WHO-klassifisering behandler ALL og lymfoblastisk lymfom som den samme neoplasien som presenterer seg enten i blod/marg eller som nodal/ekstranodal masse). Fordi pegaspargas' antineoplastisk mekanisme retter seg mot den delte metabolske sårbarheten til lymfoblaster uavhengig av presentasjon (leukemisk vs. lymfomatøs), er TxGNN-prediksjonen mekanistisk solid – men den reflekterer i stor grad bekreftelse av eksisterende praksis snarere enn en ny terapeutisk hypotese.

Detaljert formell MOA-dokumentasjon (DrugBank `original_moa`-felt) var ikke tilgjengelig i denne bevissamlingen; den mekanistiske beskrivelsen ovenfor er hentet fra modellens egen repurposing-begrunnelse i stedet for en strukturert DrugBank-registrering, og bør uavhengig verifiseres før bruk i regulatoriske innleveringer.

---

## Bevis fra kliniske forsøk

| Forsøksnummer | Fase | Status | Deltakere | Viktige funn |
|---------|------|------|------|---------|
| [NCT02013167](https://clinicaltrials.gov/study/NCT02013167) | Fase 3 | Avsluttet | 405 | Blinatumomab vs. standardbehandling kjemoterapiregime (pegaspargas-basert grunnlag) ved tilbakefall/refraktær B-prekursor ALL (TOWER-studie) |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Fase 3 | Fullført | 5,377 | Stor randomisert sammenligning av kombinert kjemoterapiregimer ved nydiagnostisert standard-risiko B-prekursor ALL |
| [NCT00022737](https://clinicaltrials.gov/study/NCT00022737) | Fase 3 | Fullført | 220 | COG pilotstudie av kombinert kjemoterapiregime ± donor stammcelletransplantasjon ved svært høyrisiko pediatrisk ALL |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Fase 3 | Rekrutterer | 5,000 | AIEOP-BFM ALL 2017 internasjonalt samarbeidsprototkoll for barn/ungdom med ALL |
| [NCT00005945](https://clinicaltrials.gov/study/NCT00005945) | Fase 3 | Fullført | 3,054 | Eskalerende-dose IV metotreksat vs. oral metotreksat og intensiveringsstrategier ved standard-risiko pediatrisk ALL |
| [NCT03959085](https://clinicaltrials.gov/study/NCT03959085) | Fase 3 | Rekrutterer | 5,951 | Inotuzumab ozogamicin lagt til post-induksjon kemoterapiimmunterapi for høyrisiko B-ALL |
| [NCT02881086](https://clinicaltrials.gov/study/NCT02881086) | Fase 3 | Fullført | 1,023 | Pediatrisk-inspirert, MRD-rettet terapi inkl. nelaraban konsolidering ved voksen ALL/lymfoblastisk lymfom |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Fase 3 | Rekrutterer | 440 | Levokarnitin-profylakse mot asparaginase-assosiert hepatotoksisitet hos AYA ALL/LL-pasienter |
| [NCT06195735](https://clinicaltrials.gov/study/NCT06195735) | N/A | Fullført | 649 | Prediksjon av overfølsomhet for PEG-asparaginase for å optimalisere ALL-behandlingsresultater |
| [NCT00671034](https://clinicaltrials.gov/study/NCT00671034) | Fase 3 | Fullført | 166 | Calaspargase pegol vs. pegaspargase pilot-RCT ved nydiagnostisert høyrisiko ALL |

*40 ytterligere forsøk ble identifisert i bevissamlingen, men er utelatt her for korthetens skyld (fullstendig liste tilgjengelig i råbevissamlingen).*

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktige funn |
|------|-----|------|------|---------|
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Kohortstudie | Blood Advances | GIMEMA LAL1913: pegaspargase-modifisert, risiko-orientert program forbedrer resultatene ved voksen Ph-negativ ALL/LL |
| [34228505](https://pubmed.ncbi.nlm.nih.gov/34228505/) | 2021 | Kohortstudie | J Clin Oncol | DFCI 11-001: effektivitets-/toksisitetsammenligning av pegaspargase vs. calaspargase pegol ved pediatrisk ALL |
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | Fase 3 RCT | J Clin Oncol | COG AALL1231: bortezomib lagt til terapi ved nydiagnostisert T-ALL/T-LL |
| [39322712](https://pubmed.ncbi.nlm.nih.gov/39322712/) | 2024 | Fase 2 | Leukemia | Langtidsoppfølging: venetoclax + hyper-CVAD/nelaraban/pegylert asparaginase ved T-ALL/LBL |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Oversikt | Haematologica | Ekspertpanelkonsensus om gjenkjenning/forebygging/behandling av asparaginase-relaterte bivirkninger hos voksne |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | Fase 3 RCT | J Clin Oncol | COG AALL0232: dexametason + høydose metotreksat forbedrer resultatene ved høyrisiko B-ALL |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | Fase 3 RCT | J Clin Oncol | COG AALL0434: nelaraban testet ved nydiagnostisert T-celle-ALL |
| [17696798](https://pubmed.ncbi.nlm.nih.gov/17696798/) | 2007 | Oversikt | Expert Opin Pharmacother | Grunnleggende oversikt over PEG-asparaginase farmakologi og klinisk rolle |
| [40163215](https://pubmed.ncbi.nlm.nih.gov/40163215/) | 2025 | Fase 2 | Int J Hematol | Multisenterstudium av liofilisert pegaspargase effektivitet/sikkerhet/PK hos japanske ALL-pasienter |
| [35987855](https://pubmed.ncbi.nlm.nih.gov/35987855/) | 2022 | Oversikt | Bulletin du Cancer | Anbefalinger fra Fransk samfunn for barn- og ungdomskrefts om håndtering av pegaspargase-assosierte toksisiteter |

*10 ytterligere publikasjoner ble identifisert i bevissamlingen, men er utelatt her for korthetens skyld.*

---

## Markedsinformasjon for Norge

Ingen godkjenninger er for tiden registrert for pegaspargase i Norge (markedsstatus: **Ikke markedsført**, totale lisenser: 0). Hvis klinisk bruk forfølges, ville tilgang kreve en navngitt-pasient/unntaksbasert importrute eller en ny søknad om markedsføringsgodkjenning, snarere enn avhengighet av en eksisterende lokal godkjenning.

---

## Cytotoksisitet

Pegaspargase er et antineoplastisk biologisk enzym (L-asparaginase-klasse) som brukes utelukkende i cytotoksiske kjemoterapiregimer for lymfoide malignancer; dets originalindikasjon (ALL) og mekanisme (selektiv cytotoksisitet via asparagin-depletering) oppfyller begge kriteriene for dette avsnittet.

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonell cytotoksisk – enzymbasert antimetabolsk agen (asparaginase-klasse), distinkt mekanisme fra DNA-skadende cytotoksiske midler |
| Risiko for myelosuppresjon | Ikke direkte karakterisert i tilgjengelig bevis; pegaspargase anses generelt som mindre myelosupprimerende alene enn klassisk cytotoksiske midler, men det administreres alltid innenfor kombinerte regimer der samlet myelosuppresjon forårsaket av samadministrerte legemidler (per forsøk NCT01193933, dosering modifiseres basert på kombinert regimemyelosuppresjonsseveritet) |
| Emetogenisitetsklassifisering | Lav til moderat (konsistent med asparaginase-legemiddelklassen) |
| Overvåkingselementer | Leverfunksjon (hepatotoksisitet – PMID 34528411, 40109190), pankreasenzymer/pankreatitt (PMID 10696127), koagulasjonsparametere (trombose/hemostase – NCT01094392), triglyserider og glukose (PMID 30823860, 34931744), og overfølsomhetsovervåking (PMID 31571395, NCT06195735) |
| Håndteringsbeskyttelse | Skal håndteres under standard forsiktighetsregler for håndtering av cytotoksiske/antineoplastiske legemidler |

---

## Sikkerhetsvurderinger

Vennligst konsulter pakningsvedlegget for sikkerhetsinformasjon. Ingen strukturerte viktige advarsler, kontraindikasjoner eller legemiddel–legemiddel–interaksjondata var tilgjengelig i denne bevissamlingen (DDI-spørring returnerte ingen resultater).

---

## Konklusjon og neste steg

**Avgjørelse: Fortsett med sikringsmekanismer**

**Begrunnelse:**
Den mekanistiske og kliniske forsøksbeviset (L1, 50 forsøk inkludert store fase 3 RCT-er) er sterkt, men dette er fundamentalt bekreftelsesbevis for pegaspargas' allerede etablert rolle i ALL/lymfoblastisk lymfom snarere enn en ny repurposing-oppdagelse. Kombinert med legemidlets nåværende ikke-markedsført status i Norge og en kritisk datasvikt angående lokal produktinformasjon, bør denne kandidaten kun fortsette under sikringsmekanismer – ikke som lansering av en ny indikasjon.

**For å fortsette kreves følgende:**
- TFDA/norsk ekvivalent pakningsvedlegg med advarsler og kontraindikasjoner (for tiden en datasvikt av typen **Blokkering** – DG001)
- Formell DrugBank-basert mekanisme-for-handling-dokumentasjon (for tiden en datasvikt av typen **Høy**-alvorlighetsgrad – DG002)
- Bekrefting av regulatorisk bane for norsk markedstilgang (navngitt-pasient import eller ny MA-søknad), gitt null eksisterende godkjenninger
- Avklaring med kliniske/regulatoriske interessenter at denne kandidaten representerer bekreftelse av etablert bruk, ikke en ny repurposing-mulighet, før den tas med i noen repurposing-fokusert beslutningspakke

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

