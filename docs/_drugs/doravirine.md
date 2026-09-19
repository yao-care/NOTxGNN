---
layout: default
title: Doravirine
parent: Kun modellprediksjon (L5)
nav_order: 113
evidence_level: L5
indication_count: 3
---

# Doravirine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Doravirine: Fra HIV-1-infeksjon til felint ervervet immunsviktsyndrom

## Sammendrag i en setning

Doravirine er en non-nukleosid reversert transkriptasehemmer (NNRTI) utviklet for HIV-1-infeksjon. TxGNN-modellens høyest rangerte prediksjon antyder mulig relevans til **felint ervervet immunsviktsyndrom (FIV)** — en veterinær lentivirus-infeksjon, ikke en menneskesykdom — og denne retningen støttes for øyeblikket av **ingen kliniske forsøk og ingen litteratur**, som tilsvarer det laveste evidensnivået (L5, kun modellprediksjon).

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originalindikasjon | HIV-1-infeksjon (basert på kontekst for legemiddelklasse i evidenspakken; ikke bekreftet via norske reguleringsdata, da legemidlet ikke er markedsført der) |
| Forutsagt ny indikasjon | Felint ervervet immunsviktsyndrom (FIV) |
| TxGNN-prediksjonspoeng | 99.93% |
| Evidensnivå | L5 |
| Status på det norske marked | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Pausert |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme (MOA) for doravirine er ikke tilgjengelige i denne evidenspakken (flagget som en alvorlig datakløft). Basert på konteksten for legemiddelklasse som refereres i hele evidenspakkens begrunnelse for legemiddelomobruk, tilhører doravirine klassen non-nukleosid reversert transkriptasehemmere (NNRTI) — antiretrovirale midler hvis aktivitet avhenger av binding til en høyt spesifikk lomme innen HIV-1 reversert transkriptase (RT) enzym.

Den høyest rangerte prediksjonen, FIV, ser ut til å oppstå fra semantisk likhet i kunnskapsgrafen mellom «antiretrovirale midler» og «lentivirus-infeksjoner» generelt, snarere enn fra direkte farmakologiske eller kliniske bevis. FIV er forårsaket av et lentivirus som, selv om det er fjernt relatert til HIV-1, har en reversert transkriptase-struktur som skiller seg vesentlig fra den. NNRTI er godt kjent for å være høyt sekvens-spesifikk til HIV-1 non-nukleosid bindingslommen — den samme legemiddelklassen (f.eks. efavirenz, nevirapin) viser liten til ingen kryssreaktivitet selv mot det nært relaterte HIV-2, langt mindre mot FIV. FIV er også en veterinær (felint) sykdom, ikke en menneskelig indikasjon, noe som plasserer den utenfor det konvensjonelle omfanget av legemiddelomobruk hos mennesker.

Evidenspakkens egen mekanistiske vurdering av denne kandidaten karakteriserer eksplisitt den som sannsynlig støy i embedding-rommet snarere enn et biologisk plausibelt ombrukssignal. To lavere-konfidenskandidater ble også vurdert for kontekst: simian immunsviktvirus (SIV) infeksjon (rang 2 — mekanistisk plausibel i prinsippet som et annet lentivirus, men mangler direkte bevis for kryssreaktivitet og er, som FIV, ikke en menneskelig indikasjon) og en sjelden nevro-utviklingsforstyrrelse (rang 3 — ingen biologisk begrunnelse forbinder den til reversert transkriptasehemming, og den er flagget som en sannsynlig falsk positiv). Ingen av dem styrker tilfellet for den høyest rangerte prediksjonen.

---

## Klinisk forsøksevidens

For øyeblikket ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig.

*Merknad: En litteraturoppføring ble hentet under rang-2-kandidaten (SIV-infeksjon) — [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/), en 2020-oversikt over islatravir. Dette gjelder et annet legemiddel (islatravir, ikke doravirine) og utgjør derfor ikke direkte støttende bevis for doravirine.*

---

## Informasjon om det norske marked

Doravirine har for øyeblikket ingen markedsføringstillatelse i Norge (markedsstatus: Ikke markedsført; 0 lisenser på fil). Ingen produkt-, doseringsform-, eller godkjent-indikasjondata er tilgjengelig for dette markedet.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. TFDA-pakningsvedlegg advarsler/kontraindikasjoner og DDI-data er for øyeblikket ikke tilgjengelige (DDI-spørringsstatus: ikke funnet) — dette registreres som en **blokkerende** datakløft (DG001) som hindrer videre framgang til sikkerhetsvurdering (S1).

---

## Konklusjon og neste skritt

**Beslutning: Pausert**

**Begrunnelse:**
Evidensnivået er L5 (kun modellprediksjon, ingen kliniske forsøk eller litteratur), og den underliggende mekanistiske begrunnelsen for den høyest rangerte indikasjonen (FIV) er svak — FIV er en ikke-menneskelig veterinærsykdom uten etablerte data om NNRTI-kryssreaktivitet. Kombinert med fraværet av norsk markedstilstedeværelse og en blokkerende sikkerhetsdatakløft, oppfyller denne kandidaten for øyeblikket ikke terskelen for videre vurdering.

**For å fortsette er følgende nødvendig:**
- TFDA/norsk pakningsvedlegg (advarsler, kontraindikasjoner) — Blokkerende datakløft (DG001), påkrevd før enhver S1-sikkerhetsvurdering
- Bekreftet virkningsmekanisme (MOA)-dokumentasjon — Kløft med høy prioritet (DG002)
- Direkte farmakologisk eller in vitro-bevis for doravirin-aktivitet mot FIV eller andre non-HIV-1 lentivirus
- Direkte (legemiddelspesifikk) litteratur- eller forsøksbevis for SIV-infeksjonskandidaten, siden det nåværende litteraturtreffet gjelder et annet legemiddel (islatravir)
- Klargjøring av klinisk relevans, siden den høyest rangerte prediksjonen er en veterinær indikasjon snarere enn et menneskelig sykdomsmål

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

