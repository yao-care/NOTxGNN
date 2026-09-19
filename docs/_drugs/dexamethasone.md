---
layout: default
title: Dexamethasone
parent: Høy evidens (L1-L2)
nav_order: 107
evidence_level: L2
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: Fra systemisk kortikosteroidterapi til alopecia areata

## Sammendrag på én setning

> Dexametason er en potent, langvirkende syntetisk kortikosteroid med bredt etablerte anti-inflammatoriske og immunosuppressive bruksområder.
> TxGNN-modellen forutsier at det kan være effektivt for **Alopecia Areata**,
> og i motsetning til de fleste co-occurrence-drevne prediksjoner, er denne støttet av **ekte litteraturbevis** — inkludert randomiserte kontrollerte studier og systematiske oversikter over dexametason oral mini-pulse (OMP) terapi — selv om ingen klinisk studie i evidenspakken ble designet spesifikt for denne indikasjonen.

---

## Rask oversikt

| Element | Innhold |
|---|---|
| Opprinnelig indikasjon | Ikke spesifisert i evidenspakken (dexametason er en syntetisk kortikosteroid med bredt, godt etablerte anti-inflammatoriske/immunosuppressive bruksområder; `original_moa` og `original_indications` er dataluker i denne pakken) |
| Predikert ny indikasjon | Alopecia Areata |
| TxGNN prediksjonspoengsum | 99.99% (rank 168) |
| Bevisnivå | L2 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Fortsett med sikkerhetstiltak |

---

## Hvorfor er denne prediksjonen fornuftig?

Foreløpig er detaljerte data om virkningsmekanisme ikke tilgjengelige i det formelle MOA-feltet (datakluft). Imidlertid gir evidenspakkens begrunnelse for ombruk en klar mekanistisk forklaring: dexametason er en potent, langvirkende glukokortikoid som fremkaller systemisk immunsuppresjon, og blokkerer T-celle-mediert perikulær inflammatorisk infiltrasjon som driver det autoimmune angrepet på hårfollikler i alopecia areata (AA).

Viktig er det at dette **ikke er en ny mekanistisk hypotese** — dexametason mini-pulse (oral eller IV) terapi er allerede et etablert off-label behandlingsalternativ i dermatologisk praksis for moderat til alvorlig AA, særlig hos pasienter som ikke er kvalifisert for eller ikke kan få tilgang til JAK-hemmere. TxGNN-prediksjonen gjenoppretter derfor en reell, klinisk praktisert bruk i stedet for å foreslå et utestet mekanistisk sprang.

Det er verdt å merke seg at ingen av de kliniske studiene som automatisk er knyttet til denne prediksjonen i evidenspakken, faktisk er AA-studier — de er onkologistudier (multippelt myelom, mesoteliom, NSCLC osv.) der dexametason ble brukt som støtte-/kombinasjonsterapi, og databaselinken er en falskt positiv drug co-occurrence. Det egentlige støttende beviset for denne indikasjonen kommer helt fra **litteraturen** (PubMed), ikke fra registrerte kliniske studier.

---

## Bevis fra kliniske studier

Foreløpig er ingen kliniske studier som spesifikt evaluerer dexametason for alopecia areata registrert. De kliniske studiene som ble funnet under evidenssamlingen (f.eks. NCT02004275, NCT02685826, NCT05408026 — alle multippelt myelom-studier som brukte dexametason som kombinasjonsterapibase) ble flagget i evidenspakken som **falskt positive database co-occurrence**, som ikke er relatert til alopecia areata, og er derfor ekskludert fra denne tabellen.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Viktige funn |
|---|---|---|---|---|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | Randomisert kontrollert studie | Dermatologic Therapy | Randomisert sammenligning av lavdose dexametason oral mini-pulse mot DPCP kontaktsensibilisering i alvorlig pediatrisk AA |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Randomisert kontrollert studie (multisentrum) | Dermatologic Therapy | Multisenter-studie av oral dexametason mini-pulse terapi for moderat-alvorlig AA; posisjonert som et tilgjengelig alternativ til JAK-hemmere |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematisk oversikt / Nettverksmetaanalyse | Archives of Dermatological Research | Sammenligner systemiske steroider, orale JAK-hemmere og kontakt-immunterapi for alvorlig AA; ingen enkelt behandling vises klart overlegen |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Oversikt | Pediatric Dermatology | Gjennomgår pulse-dose kortikosteroid doseringsskjemaer og tilknyttede bivirkninger for AA hos barn |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospektiv kohortstudie | Journal of Clinical Medicine | Empirisk bevis for dexametason mini-pulse terapi effektivitet/sikkerhet og prediktorer for respons i AA |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Prospektiv kohortstudie | Dermatologic Therapy | Sammenligner 1-dags vs 3-dagers IV dexametason pulse-skjemaer pluss topisk klobetasol hos 73 barn med alvorlig AA |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Kohort, langtidsstudie | Dermatologic Therapy | Langtids- (median 96 måneder) oppfølging av kombinert oral dexametason pulse + topisk kortikosteroid hos 65 barn med alvorlig AA |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Sammenligningsstudie | Dermatology (Basel) | Sammenligner effektivitet, tilbakefall og bivirkninger på tvers av tre systemiske kortikosteroid-skjemaer for AA |
| [17656876](https://pubmed.ncbi.nlm.nih.gov/17656876/) | 2002 | Klinisk kommentar/oversikt | Indian J Dermatol Venereol Leprol | Diskuterer risiko-nytte ved dexametason pulse terapi for omfattende AA |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Kasusserier | The Journal of Dermatology | To ganger ukentlig 5 mg dexametason oral pulse hos 30 pasienter med omfattende AA; rapporterer resultater for terminalt hårgjenvekst |

---

## Norsk markedsinformasjon

Ingen markedsføringsautorisasjoner er for tiden registrert i Norge (`total_licenses = 0`, `licenses = []`).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsopplysninger. `key_warnings`, `contraindications` og DDI-data er ikke tilgjengelig i denne evidenspakken (spørringsstatus: ikke funnet).

---

## Konklusjon og neste steg

**Beslutning: Fortsett med sikkerhetstiltak**

**Begrunnelse:**

Litteraturbeviset — inkludert to randomiserte kontrollerte studier, en systematisk oversikt/nettverksmetaanalyse og flere kohortstudier — støtter dexametason oral/IV mini-pulse terapi som et allerede praktisert off-label alternativ for moderat-alvorlig alopecia areata (Bevisnivå L2). Imidlertid har denne evidenspakken en **blokkert** datakluft på formelle Norge/regulatoriske merkedata for sikkerhet (advarsler, kontraindikasjoner), som hindrer kandidaten fra å formelt gå inn i S1 sikkerhetsvurderingsfasen.

**For å fortsette er følgende nødvendig:**

- Hent TFDA/Norge-ekvivalente produktmerkingsadvarsler og kontraindikasjoner (Blokkert gap, DG001)
- Hent formell dokumentasjon av virkningsmekanisme (MOA) fra DrugBank eller tilsvarende kilde (Høy prioritet gap, DG002)
- Formell DDI-gjennomgang, gitt dexametasons velkjente interaksjonsprofil (CYP3A4-induktorer/substrater, levende vaksiner, NSAIDs)
- Dosering/regime-standardiseringsgjennomgang — litteratur bruker varierte mini-pulse-protokoller (f.eks. 5 mg to ganger ukentlig vs. månedlige IV-pulser); ingen konsensusregime har blitt etablert
- Bekreft rute-/formuleringkompatibilitet (oral tablett vs. IV pulse) mot lokalt tilgjengelige doseringsformer, siden ingen norske lisenser for tiden eksisterer

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

