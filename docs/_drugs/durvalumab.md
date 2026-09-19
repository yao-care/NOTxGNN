---
layout: default
title: Durvalumab
parent: Kun modellprediksjon (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Durvalumab
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

# Durvalumab: Fra anti-PD-L1 immun-onkologi til urotelkarsinom i prostataurethra

## Oppsummering i en setning

Durvalumab er en anti-PD-L1 immun-checkpoint-inhibitor monoklonal antistoff; ingen godkjent indikasjon er for tiden registrert for dette markedet og produktet er **ikke markedsført** her. TxGNN-modellens topprangerte prediksjon er **Urotelkarsinom i prostataurethra** (poengsum 99.98%), men denne spesifikke indikasjonen har for tiden **0 kliniske forsøk** og **0 publikasjoner** som direkte støtter den — begrunnelsen hviler helt på legemiddelklasse-analogi til PD-L1-responsive uroteliale kreftformer. På tvers av hele 10-indikasjon-porteføljen som ble generert for durvalumab, gir **4 unike forsøk** og **1 publikasjon** indirekte støtte, med det sterkeste beviset (L2) faktisk funnet for en lavere rangert kandidat, endoservikal karsinom.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Original indikasjon | Ikke registrert — legemidlet er ikke markedsført i denne jurisdiksjonen og DrugBank `original_indications` er tomt |
| Predikert ny indikasjon | Urotelkarsinom i prostataurethra |
| TxGNN prediksjon poengsum | 99.98% |
| Bevisnivå | L4 (kun mekanistisk/klasse-analogi; ingen direkte forsøk eller litteratur) |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Vente |

---

## Portefølje av predikerte indikasjoner (topp 10)

Modellen returnerte 9 ytterligere kandidater i samme kjøring. To — de sarkomatoride urotelialvariantene — har allerede early-phase forsøksstøtte, og en (endoservikal karsinom) har det sterkeste bevisnivået i hele settet til tross for at den rangeres 6. på råpoengsum.

| Rangering | Predikert indikasjon | TxGNN poengsum | Bevisnivå | Beslutningsstadium | Anbefaling |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Urotelkarsinom i prostataurethra | 99.98% | L4 | S0 | Vente |
| 2 | Sarkomatordt overgangscellekarsinom i nyrebasseng | 99.98% | L3 | S1 | Forskningsspørsmål |
| 3 | Infiltrerende blæreurotelkarsinom, sarkomatorid variant | 99.98% | L3 | S1 | Forskningsspørsmål |
| 4 | Papillært urotelkarsinom i nyrebasseng | 99.98% | L4 | S0 | Vente |
| 5 | Adenokarsinom i uterinligament | 99.92% | L5 | S0 | Vente |
| 6 | **Endoservikal karsinom** | 99.91% | **L2** | **S2** | Forskningsspørsmål |
| 7 | Adenoid cystisk karsinom i cervix uteri | 99.91% | L5 | S0 | Vente |
| 8 | Serøs adenokarsinom i uterinligament | 99.91% | L5 | S0 | Vente |
| 9 | Signet ring celle variant av servikal mucint adenokarsinom | 99.90% | L5 | S0 | Vente |
| 10 | Intestinal variant av servikal mucint adenokarsinom | 99.90% | L5 | S0 | Vente |

---

## Hvorfor er denne prediksjonen fornuftig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelige i DrugBank-posten (DB11714) for denne bevisposten — dette er flagget som datagap **DG002 (høy alvorlighetsgrad)**. Basert på bevisene for omformål som er samlet inn på tvers av alle 10 prediksjoner, beskrives durvalumab konsekvent som en **anti-PD-L1 (programmed death-ligand 1) immun-checkpoint-inhibitor**, en legemiddelklasse med etablert aktivitet i PD-L1-uttrykkende, immunologisk aktive tumorer.

De 10 predikerte indikasjonene grupperes i to biologiske grupper. **Urotelialgruppen** (rangeringer 1–4: prostataurethra, nyrebasseng, blæresarkomatorid variant, papillært nyrebasseng) deler vevopprinnelse med blæreurotelkarsinom — en tumortype hvor anti-PD-L1-midler allerede har bred farmakologisk-klassepresedens — og deler PD-L1-uttrykk og tumor mutasjonsbyrde (TMB) karakteristika med denne etablerte indikasjonen. Dette er en sammenhengende mekanistisk utvidelse selv der direkte forsøksdata er fraværende (rangeringer 1 og 4). **Den gynekologiske gruppen** (rangeringer 5–10) er mer heterogen: endoservikal karsinom (rangering 6) har plausibel mekanistisk støtte via HPV-relatert tumor immunogenitet og et aktivt forsøk som kombinerer durvalumab med ATR/PARP-inhibisjon for å forsterke immunogen celledød. I kontrast, noterer begrunnelsenteksten for flere ultra-sjeldne varianter (adenoid cystisk karsinom i cervix uteri, signet ring celle og intestinal-variant mucint adenokarsinom) eksplisitt at disse histologiene typisk er assosiert med **lav PD-L1-uttrykk og lav TMB** basert på analoge tumorer andre steder i kroppen — noe som betyr at den mekanistiske saken for disse spesifikke kandidatene er svak selv om modellpoengene er høye. Disse bør behandles med mer skepsis enn poengene alene foreslår.

For hovedindikasjonen (urotelkarsinom i prostataurethra), eksisterer det ingen direkte klinisk eller litteraturbevis i denne posten; saken hviler utelukkende på vevopprinnelses-analogi til blæreurotelkarsinom, som er grunnen til at den er scoret L4/Vente til tross for den høyeste råpoeng TxGNN-scoren i settet.

---

## Bevis fra kliniske forsøk

**Urotelkarsinom i prostataurethra (hovedindikasjon):** For tiden ingen relaterte kliniske forsøk registrert.

Følgende forsøk ble identifisert for andre kandidater i samme portefølje og er inkludert for kontekst, da de informerer den mekanistiske saken for urotelial- og gynekologisk-klyngene ovenfor:

| Forsøksnummer | Fase | Status | Antall deltakere | Relevant indikasjon | Hovedfunn |
|---------|------|------|------|------|---------|
| [NCT02812420](https://clinicaltrials.gov/study/NCT02812420) | Early Phase 1 | Aktivt, ikke rekrutterer | 54 | Sarkomatordt overgangscellekarsinom i nyrebasseng (rangering 2) / Blæresarkomatorid variant (rangering 3) | Pilot pre-kirurgisk studie av durvalumab + tremelimumab hos cisplatin-uegnede pasienter med høyrisiko muskelinvasiv urotelkarsinom; ingen resultater rapportert ennå |
| [NCT03912818](https://clinicaltrials.gov/study/NCT03912818) | Phase 2 | Avsluttet | 7 | Infiltrerende blæreurotelkarsinom, sarkomatorid variant (rangering 3) | Neoadjuvant durvalumab + kjemoterapibehandling ved blærekreftvarianter med variant histologi; avsluttet med kun 7 pasienter inkludert, grunn ikke angitt — behandle som uavgjort resultat, ikke negativt |
| [NCT04065269](https://clinicaltrials.gov/study/NCT04065269) | Phase 2 | Aktivt, ikke rekrutterer | 174 | Endoservikal karsinom (rangering 6) | ATARI-forsøk: ATR-inhibitor ceralasertib ± olaparib eller durvalumab ved tilbakevendende gynekologiske krefttyper stratifisert etter ARID1A-status; pågående, ingen resultater ennå |
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Avsluttet | 20 | Endoservikal karsinom (rangering 6) | Hypofraksjonert stereotaktisk strålebehandling + durvalumab/tremelimumab ved tilbakevendende/metastatisk servikal-, vaginal- eller vulvakreft; liten early-phase sikkerhets- og gjennomførlighetsstudie |

---

## Litteraturbevis

**Urotelkarsinom i prostataurethra (hovedindikasjon):** Ingen relatert litteratur tilgjengelig for tiden.

| PMID | År | Type | Tidsskrift | Relevant indikasjon | Hovedfunn |
|------|-----|------|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Oversikt | Biomedical Journal | Endoservikal karsinom (rangering 6) | Gjennomgang av småcellet neuroendokrint karsinom i cervix — en sjelden, aggressiv HPV-relatert cervikalkreft uten etablerte evidensbaserte behandlingsretningslinjer; behandling er for tiden ekstrapolert fra småcellet lungekreftprotokoller |

---

## Markedsinformasjon for Norge

Durvalumab er **ikke markedsført** i denne jurisdiksjonen for tiden. Det finnes ingen markedsføringstillatelser, produktnavn, legemiddelformer eller godkjent indiksjonstekst på fil (`total_licenses: 0`).

---

## Cytotoksisitet

Durvalumab er et onkologisk legemiddel (anti-PD-L1 immun-checkpoint-inhibitor, per bevisene for omformål ovenfor), så denne seksjonen gjelder.

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Immunterapi (anti-PD-L1 checkpoint-inhibitor) |
| Risiko for beinmargssuppresjon | Se produktinformasjon for advarsler og forholdsregler |
| Emetogenitetsklassifisering | Se produktinformasjon for advarsler og forholdsregler |
| Overvåkingspunkter | Se produktinformasjon for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se produktinformasjon for advarsler og forholdsregler |

Ingen DrugBank-toksisitetsdata eller TFDA produktinformasjonsinnhold var tilgjengelig i denne bevisposten for å underbygge spesifikke beinmargssuppresjon-, emetogenisitets- eller overvåkingsdetaljer — checkpoint-inhibitorer som klasse er typisk assosiert med immunrelaterte bivirkninger (f.eks. colitt, pneumonitt, hepatitt, endokrinopati) snarere enn klassisk beinmargssuppresjon, men dette bør bekreftes mot den faktiske produktinformasjonen i stedet for å antas.

---

## Sikkerhetshensyn

Produktinformasjonsadvarsler, kontraindikasjoner og legemiddel-legemiddel interaksjonsdata er ikke tilgjengelig for durvalumab i denne bevisposten for tiden. Dette gapet er flagget som **DG001 (blokkering-alvorlighetsgrad)** — dens angitte virkning er at kandidaten **ikke kan passere S1-sikkerhetsprøvingsporten** inntil TFDA produktinformasjonsinnhold er innhentet og analysert. Vennligst se produktinformasjon for sikkerhetsinformasjon når det blir tilgjengelig.

---

## Konklusjon og neste trinn

**Beslutning: Vente** (hovedindikasjon — urotelkarsinom i prostataurethra)

**Begrunnelse:**
Til tross for å ha den høyeste TxGNN-poengsummen i porteføljen (99.98%), har hovedindikasjonen null direkt klinisk forsøks- eller litteraturstøtte og hviler på klasse-nivå mekanistisk analogi alene (L4). Separat, en **blokkering-alvorlighetsgrad** datagap (DG001 — manglende TFDA produktinformasjon) forhindrer denne kandidaten fra å passere S1-sikkerhetsprøvingsporten uavhengig av indikasjonsnivå-bevis, og legemidlet er ikke markedsført i denne jurisdiksjonen for tiden (0 autorisasjoner).

**For å gå videre kreves følgende:**
- TFDA produktinformasjon (advarsler, kontraindikasjoner) — nødvendig for å passere S1-sikkerhetsporten (DG001, blokkering-alvorlighetsgrad)
- Detaljerte data om virkningsmekanisme via DrugBank API (DG002, høy alvorlighetsgrad)
- Fortsatt overvåking av NCT02812420 (est. avslutning 2027-12) og NCT04065269 (est. avslutning 2026-08) for interim eller endelige resultater
- Gitt bevisubalansen innen denne porteføljen, prioriter **endoservikal karsinom** (rangering 6, L2, S2 — Forskningsspørsmål) og de **sarkomatoride urotelialvariantene** (rangeringer 2–3, L3, S1 — Forskningsspørsmål) for aktiv oppfølging, da de for tiden har mer modne bevis enn den topprangerte hovedindikasjonen
- Periodisk gjentatte søk i ClinicalTrials.gov/PubMed spesielt for "prostatic urethra urothelial carcinoma" + durvalumab, da det for tiden ikke finnes direkte bevis for denne eksakte indikasjonen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

