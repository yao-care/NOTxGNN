---
layout: default
title: Inclisiran
parent: Kun modellprediksjon (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: Fra hyperkholesterolemi til kaliummangelsykdom

## Oppsummering i én setning

> Inclisiran (DB14901) er en PCSK9-rettet siRNA; dens opprinnelig godkjente indikasjon er ikke fanget i denne bevissamlingen (norske lisensieringsdata er tomme — legemidlet er for tiden **ikke markedsført**).
> TxGNNs topp-rangerte prediksjon i denne serien er **kaliummangelsykdom** (score 99.93%), men dette signalet støttes av **0 kliniske forsøk** og **0 publikasjoner** — det er en ren modellartefakt uten biologisk begrunnelse, og den interne scoringmotoren selv flaggerer det som **Hold**.

---

## Rask oversikt

| Punkt | Innhold |
|------|---------|
| Opprinnelig indikasjon | Ikke tilgjengelig — `taiwan_regulatory.licenses` er tom i denne bevissamlingen. (Generell farmakologisk bakgrunn, ikke fra dette datasettet: inclisiran er en PCSK9-rettet siRNA brukt for LDL-C-senkelse/ASCVD-risikoreduksjon.) |
| Forutsagt ny indikasjon | Kaliummangelsykdom |
| TxGNN-prediksjons-poengsum | 99.93% |
| Bevisnivå | L5 (modellprediksjon kun, ingen støttestudier) |
| Norsk markedsstatus | ✗ Ikke markedsført (Ikke markedsført) |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte virkningsmekanisme-data ikke tilgjengelige for inclisiran i denne bevissamlingen (`original_moa: [Data Gap]`). Basert på generell farmakologisk kunnskap, er inclisiran en liten interfererende RNA (siRNA) som hemmer hepatisk PCSK9 mRNA-translasjon, og dermed øker LDL-reseptor-resirkulering og senker sirkulerende LDL-kolesterol.

For den topp-rangerte prediksjonen i denne serien — **kaliummangelsykdom** — erklærer bevissamlingens egen mekanistiske vurdering eksplisitt at det er **ingen kjent biologisk sammenheng** mellom PCSK9/LDL-reseptor-banen og kaliumhomøostase, og **ingen forsøks- eller litteraturbevis** eksisterer for å støtte forbindelsen. Dette er konsistent med en høy TxGNN embedding-likhets-poengsum som ikke tilsvarer plausibel farmakologi — en kjent sviktmodus for ren graf-embedding-prediksjoner når de ikke er begrenset av mekanistiske filtre.

Gitt dette, skal prediksjonen **ikke** tolkes som et genuint ombruksignal. Det er beholdt i denne rapporten for transparens- og revisjonsformål.

---

## Klinisk forsøksbevis

For tiden er ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er ingen relatert litteratur tilgjengelig.

---

## Norsk markedsinformasjon

Inclisiran er for tiden **ikke markedsført** i Norge — `taiwan_regulatory.market_status = "Not marketed"`, med **0 godkjennelser** på fil. Ingen lisenseopplysninger er tilgjengelige for oppsummering.

---

## Andre kandidater i denne serien (kontekst)

Denne bevissamlingen ("TW-DB14901-multi") inneholder 10 TxGNN-rangerte prediksjoner for inclisiran, de fleste av dem deler det samme problemet som tophiten — høy poengsum, null bevis, "Hold." En kandidat skiller seg ut som vesentlig annerledes og garanterer separat oppfølging:

| Rangering | Sykdom | TxGNN-poengsum | Bevisnivå | Beslutningsstadium | Anbefaling | Notat |
|------|---------|-------------|-----------------|------------------|-----------------|------|
| 1 | Kaliummangelsykdom | 99.93% | L5 | S0 | Hold | Ingen mekanistisk forbindelse, ingen bevis |
| 2 | Spiserørsykdom | 99.87% | L5 | S0 | Hold | Ingen bevis |
| 4 | Migrene | 99.83% | L5 | S0 | Hold | Ingen bevis |
| 7 | Migrene med eller uten aura, disponering | 99.78% | L5 | S0 | Hold | 20 artikler hentet, men alle om epilepsi/migrene-genetikk — ingen adresserer PCSK9/lipidveier |
| **8** | **Aortamalformasjon** | **99.76%** | **L4** | **S1** | **Forskningsspørsmål** | **2 aktive fase 3 pediatriske FH-forsøk (NCT06597006, NCT06597019); plausibel mekanistisk forbindelse via LDL-C-drevet vaskulær/valvulær lipiddeposisjon, men forsøksinklusjonskriterier (HoFH/HeFH) trenger manuell verifisering mot "aortamalformasjon" som et MeSH-nivåterm** |
| 9 | Spiserørsår | 99.73% | L5 | S0 | Hold | Ingen bevis |
| 10 | Raynaud-sykdom | 99.73% | L5 | S0 | Hold | Ingen bevis |

Rangering 8 ("aortamalformasjon") er den eneste kandidaten i denne serien som nådde beslutningsstadium S1 med virkelig klinisk forsøksstøtte, og er det mer passende målet for en dedikert oppfølgingsevaluering — ikke den topp-rangerte "kaliummangelsykdom"-oppføringen.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. `safety.key_warnings`, `safety.contraindications`, og `safety.ddi` er alle markert som datahull i denne bevissamlingen (se DG001, "Blocking"-alvorlighetsgrad — TFDA/etikett-advarsler ikke ennå hentet).

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Den topp-rangerte prediksjonen (kaliummangelsykdom) har en meget høy TxGNN-poengsum, men null bekrefteende klinisk eller litteraturbevis, og pakningens egen begrunnelse bekrefter ingen biologisk plausibilitet. Dette er et modellartefaktsignal, ikke en genuint ombrukskandidat.

**For å gå videre, er følgende nødvendig:**
- Løs DG001 (Blocking): hent TFDA/Norge-etikett-advarsler og kontraindikasjoner før noen S1-sikkerhetsscreening kan begynne for dette legemidlet
- Løs DG002 (High): hent strukturerte MOA-data fra DrugBank for å korrekt evaluere mekanistisk plausibilitet på tvers av alle kandidater
- Hvis du fortsetter ombruksutforsking for inclisiran, omdirigér fokus til **rangering 8 (aortamalformasjon)** — bekreft faktiske inklusjonskriterier for NCT06597006/NCT06597019 mot det forutsagte indikasjonstermet før du går videre til S2
- Fyll `taiwan_regulatory.licenses` / `original_indications` — for tiden tomme, blokkerer en fullstendig original-versus-ny indikasjonsammenligning
- Ikke gå videre med "kaliummangelsykdom," "spiserørsykdom/sår/malformasjon," "migrene," eller "Raynaud-sykdom" uten nye støttebevis — alle for tiden L5/Hold

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

