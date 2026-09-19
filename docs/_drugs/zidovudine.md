---
layout: default
title: Zidovudine
parent: Kun modellprediksjon (L5)
nav_order: 392
evidence_level: L5
indication_count: 6
---

# Zidovudine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Zidovudin: Fra HIV/AIDS antiretroviral terapi til felid ervervet immunsviktsyndrom

## Sammenfattelse på en setning

> Zidovudin (AZT/ZDV) er den opprinnelige nukleosidrevers transkriptasehemmeren (NRTI), globalt etablert som antiretroviral for HIV/AIDS hos mennesker — selv om denne spesifikke bevisspakken inneholder ingen formell registrering av den opprinnelige indikasjonen.
> TxGNN-modellens topprangerte prediksjon er **felid ervervet immunsviktsyndrom (FIV/FAIDS)**, en veterinærsjukdom (ikke-menneskelig), støttet bare av **20 prekliniske dyremodellpublikasjoner** og **null kliniske forsøk**.
> Fordi den toppscorende kandidaten ikke er en menneskelig indikasjon, er dette signalet ikke handlingsbar for menneskelig medikament omgjøring i sin nåværende form.

---

## Raskt oversikt

| Emne | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke registrert i kildedata (medikament ikke markedsført lokalt); zidovudin er internasjonalt dokumentert som den første NRTI antiretroviral for HIV/AIDS |
| Forutsagt ny indikasjon | Felid ervervet immunsviktsyndrom (veterinærindikasjon — ikke aktuelt for menneskelige pasienter) |
| TxGNN prediksjonspoeng | 99.96% |
| Bevistnivå | L4 (kun preklinisk/dyremodellitteratur; ikke overførbar til menneskelig indikasjon) |
| Norsk markedsstatus | Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Avvente |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert data om virkningsmekanisme er ikke tilgjengelig i denne bevisspakken (`original_moa`: Datagap). Basert på den omfattende litteraturen returnert over alle rangerte indikasjoner, beskrives zidovudin konsekvent som en tymidin-analog nukleosidrevers transkriptasehemmer (NRTI) — den er fosforylert intracellulært og inkorporert av retroviral revers transkriptase, som avbryter proviral DNA-syntese. Denne mekanismen er artsuavhengig på enzymnivå, noe som forklarer hvorfor medikamentet viser antiretroviral aktivitet ikke bare mot HIV-1 hos mennesker, men også mot relaterte lentiviruser hos andre arter.

Denne mekanistiske ikke-spesifisiteten er nøyaktig hvorfor de to topprangerte TxGNN-prediksjonen — **felid ervervet immunsviktsyndrom** (rang 1, poeng 0.9996) og **simianimmunsviktvirusinfeksjon** (rang 2, nesten identisk poeng 0.9996) — scorer så høyt: kunnskapsgrafen forbinder zidovudin til disse enhetene gjennom tiår med komparativ virologi-litteratur der katter og makaker ble brukt som *eksperimentelle dyremodeller* for HIV/AIDS-medikamentutvikling, ikke fordi zidovudin er en klinisk indisert terapi for kjæledyr eller primatsjukdom. Med andre ord, modellen plukker opp litteratur co-forekomst fra prekliniske modellsystemer, ikke en genuine ny menneskelig terapeutisk mulighet.

Derimot, ranger 5 og 6 i denne samme bevisspakken — **AIDS-relatert kompleks** og **kongenital menneskelig immunsviktvirus** — er sterkt støttet av dusinvis av fullførte fase 1–3 menneskelige forsøk (inkludert landemerkeforsøket ACTG 076 for prevensjon av perinatal overføring) og er faktisk *allerede etablert* menneskelig bruk av zidovudin snarere enn nye omgjøringskandidater. Ranger 3 og 4 (et sjeldent nevroevolutivt syndrom og "foreldet familiesamset hyperlipidemi") er allerede internt flagget uten mekanistisk forbindelse, og for rang 4 går det mulige forholdet i *motsatt retning* — NRTI-terapi er assosiert med lipodystrofi/dyslipidemi som bivirkningseffekt, ikke terapeutisk fordel. Samlet sett illustrerer denne kandidatbundelen et tilfelle der råt TxGNN-rangering, uten art- og klinisk kontekstfiltrering, presenterer modellartefakter snarere enn levedyktige omgjøringssignaler.

---

## Kliniske forsøksbevis

For tiden ingen relaterte kliniske forsøk registrert for felid ervervet immunsviktsyndrom (som forventet — dette er en veterinærindikasjon og ville ikke dukke opp i ClinicalTrials.gov/ICTRP for menneskelige forsøkspersoner).

---

## Litteraturbevis

All tilgjengelig litteratur for denne indikasjonen består av prekliniske dyremodellstudier hos hjemmekatter; ingen er menneskelige kliniske forsøk, randomiserte kontrollerte forsøk eller oversikter.

| PMID | År | Type | Tidsskrift | Viktige funn |
|------|-----|------|------|---------|
| [2475068](https://pubmed.ncbi.nlm.nih.gov/2475068/) | 1989 | Preklinisk (felid modell) | Antimicrob Agents Chemother | Etablerte FIV som modell for AZT-basert revers transkriptase-rettet kjemoterapi for menneskelig AIDS |
| [3034403](https://pubmed.ncbi.nlm.nih.gov/3034403/) | 1987 | Preklinisk (felid modell) | Cancer Research | Tidlig evaluering av AZT i FeLV-infiserte katter som terapi-/profylaksemodell for AIDS |
| [2178336](https://pubmed.ncbi.nlm.nih.gov/2178336/) | 1990 | Preklinisk (felid modell) | Antimicrob Agents Chemother | Interferon-alfa pluss AZT evaluert i presymptomatisk felid leukemivirus-indusert AIDS (FAIDS) |
| [2163339](https://pubmed.ncbi.nlm.nih.gov/2163339/) | 1990 | Preklinisk (felid modell, toksikologi) | Fundam Appl Toxicol | Dose-rekkevidde toksisitetsstudie av AZT i FeLV-infiserte katter |
| [8381867](https://pubmed.ncbi.nlm.nih.gov/8381867/) | 1993 | Preklinisk (felid modell) | J Acquir Immune Defic Syndr | Profylaktisk AZT reduserte tidlig viremi og lymfocytreduksjon men forhindret ikke primær FIV-infeksjon |
| [7688949](https://pubmed.ncbi.nlm.nih.gov/7688949/) | 1993 | Preklinisk (felid modell) | Arch Virol | AZT og ciklosporin reduserte plasma (men ikke PBMC) FIV-titere |
| [11943320](https://pubmed.ncbi.nlm.nih.gov/11943320/) | 2002 | Preklinisk (felid modell) | Vet Immunol Immunopathol | AZT/3TC-kombinasjon viste additiv til synergistisk anti-FIV-aktivitet in vitro; satte spørsmål ved effektivitet i kronisk infeksjon |
| [18550661](https://pubmed.ncbi.nlm.nih.gov/18550661/) | 2008 | Preklinisk (felid modell, genetikk) | J Virol | Fylogenetisk analyse av FIV-gener i katter som gjennomgår AZT-behandling kontra behandling-naive katter |
| [22816032](https://pubmed.ncbi.nlm.nih.gov/22816032/) | 2012 | Preklinisk (felid modell) | Viruses | Sammenlignet AZT alene kontra AZT-kombinasjoner (IFN-α, 3TC, valporsyre) i naturlig FIV-infiserte katter over ett år |
| [25855689](https://pubmed.ncbi.nlm.nih.gov/25855689/) | 2016 | Preklinisk (felid modell, langsiktig) | J Feline Med Surg | Langsiktig (5–6 år) oppfølging av AZT-basert antiretroviral terapi i FIV-infiserte katter |

---

## Norsk markedsinformasjon

Dette medikamentet har for tiden ingen autorisasjoner registrert for dette markedet (`market_status`: Ikke markedsført; `total_licenses`: 0). Ingen produktoppføringer er tilgjengelige å oppsummere.

---

## Sikkerhetshensyn

Se pakningsinformasjonen for sikkerhetsinformasjon. Ingen strukturerte advarsler, kontraindikasjoner eller legemiddelinteraksjonsdata er for tiden tilgjengelige i bevisspakken (`key_warnings`, `contraindications` og DDI-spørringer returnerte ingen data). Dette er flagget som et **blokkerende** datagap (DG001) — offisiell merkinginformasjon/monografidata må skaffes før denne kandidaten kan gå videre gjennom innledende sikkerhetskontroll (S1).

---

## Konklusjon og neste trinn

**Beslutning: Avvente**

**Begrunnelse:**
Den høyest rangerte TxGNN-prediksjonen (felid ervervet immunsviktsyndrom) er en veterinærindikasjon for ikke-mennesker uten bevis for kliniske forsøk og bare preklinisk dyremodellitteratur — den er ikke handlingsbar som menneskelig medikament omgjøringskandidat. Kombinert med et blokkerende sikkerhetsdatagap (ingen merkinginformasjon/advarselsdata) og medikamentets fravær fra det lokale markedet, er det utilstrekkelig grunnlag for å gå videre.

**For å gå videre, er følgende nødvendig:**
- Offisiell produktmerkinginformasjon / TFDA-ekvivalent monografidata (advarsler, kontraindikasjoner, DDI-er) for å lukke det blokkerende datagapet (DG001)
- Bekreftet virkningsmekanisme-dokumentasjon (DG002)
- Art-/enhetfiltrering på TxGNN-utganger for å utelukke ikke-mennesketige sjukdomsbetegnelser før rangering presenteres for menneskelig omgjøringsvurdering
- Hvis fortsatt forfølgt, bør revurdering fokuseres på de lavere rangerte men klinisk funderte signalene i denne pakken (AIDS-relatert kompleks, kongenital HIV-infeksjon) — med merknad om at disse gjenspeiler zidovudins *allerede etablert* menneskelig bruk snarere enn ny omgjøringsmulighet, så de ville ikke kvalifisere som nye indikasjoner heller

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

