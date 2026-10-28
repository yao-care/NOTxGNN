---
layout: default
title: Pertuzumab
parent: Kun modellprediksjon (L5)
nav_order: 323
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
monitor_inn: "PERTUZUMAB"
predicted_indications: ["ectomesenchymoma", "malignant cutaneous granular cell skin tumor", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma"]
description: "Pertuzumab: predikert ny indikasjon Ectomesenchymoma (evidensnivå L5). Opprinnelig indikasjon: Breast Neoplasms"
---

# Pertuzumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

## Pertuzumab: Ectomesenchymoma
{: .text-alpha }

## Oppsummering i én setning

Pertuzumab er et HER2-rettet monoklonalt antistoff som opprinnelig brukes til behandling av brystkreft.
TxGNN-modellen predikerer at det kan være effektivt for **progesteronreseptor-positiv brystkreft**,
og denne retningen støttes for øyeblikket av **1 fase 3-studie** og **rundt 20 publikasjoner**.
Dette er i realiteten en undergruppe av den opprinnelige indikasjonen, ikke en reell ny sykdom.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Breast Neoplasms |
| Predikert ny indikasjon | Ectomesenchymoma |
| TxGNN-prediksjonsscore | 0.9971 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 2 av 2) |
| Antall godkjenninger | 2 (gyldige: 2) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med forbehold) |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i datagrunnlaget. Ut fra kjent informasjon er pertuzumab en HER2-dimeriseringshemmer. Den binder HER2 (ERBB2) og hindrer dimerisering med andre HER-reseptorer. Effekten i HER2-positiv brystkreft er dokumentert, ofte i kombinasjon med trastuzumab og docetaksel.

Brystkreft med positiv progesteronreseptor (PR+) er en undergruppe av brystkreft. Rundt halvparten av HER2-positive svulster har samtidig uttrykk for østrogen- og/eller progesteronreseptor (HR+/HER2+). Pertuzumabs HER2-blokade er derfor mekanistisk relevant også her. Prediksjonen bør dermed forstås som en presisering av subtype, ikke som reell repurposing.

Studiene WSG-ADAPT og WSG TP-II støtter bruk av pertuzumab + trastuzumab, med eller uten endokrin behandling, ved HR+/HER2+ sykdom. Merk at PR-status alene ikke avgjør effekten. HER2-status er avgjørende.

---

## Dokumentasjon fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Fase 3 | Fullført | 517 | Randomisert, dobbeltblind ekvivalensstudie: pertuzumab-biosimilar (QL1209) mot referansepertuzumab, begge med trastuzumab + docetaksel, ved neoadjuvant behandling av HER2-positiv, ER/PR-negativ brystkreft. Bekrefter effekten av referanselegemidlet i stedet for å teste en ny indikasjon. |

---

## Litteraturdokumentasjon

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (fase 2) | Lancet Oncol | NeoSphere, 5-årsanalyse: neoadjuvant pertuzumab + trastuzumab + docetaksel ved HER2-positiv brystkreft; progresjonsfri og sykdomsfri overlevelse samt sikkerhet |
| [42150145](https://pubmed.ncbi.nlm.nih.gov/42150145/) | 2026 | RCT | J Clin Oncol | WSG TP-II, overlevelsesanalyse: neoadjuvant trastuzumab + pertuzumab + endokrin behandling mot kjemoterapi ved HR+/HER2+ tidlig brystkreft |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II: endokrin behandling + dobbel HER2-blokade sammenlignet med de-eskalert kjemoterapi ved HR+/HER2+ tidlig brystkreft |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (fase 2) | Ann Oncol | WSG-ADAPT HER2+/HR-: 12 ukers neoadjuvant dobbel blokade med trastuzumab og pertuzumab ± ukentlig paklitaksel |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (fase 3) | Br J Cancer | Pertuzumab-biosimilaren QL1209 mot referansepertuzumab ved HER2-positiv, ER/PR-negativ brystkreft |
| [41401771](https://pubmed.ncbi.nlm.nih.gov/41401771/) | 2026 | RCT (fase 3) | ESMO Open | Biosimilaren TQB2440 mot referansepertuzumab ved HER2-positiv, ER/PgR-negativ brystkreft |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Retningslinje | J Clin Oncol | Oppdatert ASCO-retningslinje for systemisk behandling av avansert HER2-positiv brystkreft |
| [28259011](https://pubmed.ncbi.nlm.nih.gov/28259011/) | 2017 | Retningslinje | Eur J Cancer | EGTM-retningslinje om biomarkører: ER og PR bør måles ved all ny invasiv brystkreft, og HER2 må bestemmes for anti-HER2-behandling |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Oversikt | Cancer Treat Rev | HR/HER2-positiv brystkreft: status og fremtid, med omtale av samspill mellom signalveiene |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Oversikt | Breast Cancer | Signalveier og klinisk oversettelse ved HR+/HER2+ brystkreft |

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002547 | Perjeta (godkjent) | Ikke oppgitt | Brystkreft (Breast Neoplasms) |
| EMEA/H/C/005386 | Phesgo (godkjent) | Ikke oppgitt | Brystkreft (Breast Neoplasms) |

Begge godkjenningene er registrert som avregistrert. Dette bør kontrolleres mot gjeldende regional merking for referanseproduktet og biosimilarer.

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Målrettet behandling (monoklonalt antistoff mot HER2); ikke et konvensjonelt cytotoksisk middel |
| Myelosuppresjonsrisiko | Lav som enkeltstoff. Risikoen styres i hovedsak av kjemoterapi gitt samtidig (f.eks. docetaksel) |
| Emetogenisitet | Lav |
| Overvåkingspunkter | Hjertefunksjon (LVEF), blodstatus (særlig ved kombinasjon med kjemoterapi), lever- og nyrefunksjon |
| Håndteringsvern | Se preparatomtalen for gjeldende krav til håndtering |

Kardiale sikkerhetsstudier (TRYPHAENA og BERENICE) er omtalt i litteraturen og viser at hjerteovervåking er viktig.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**:
  - Idelalisib: moderat interaksjonsnivå (kilde: DDInter).
  - Farmakologisk mål: pertuzumab binder HER2 (ERBB2), og er brukt ved HER2-overuttrykkende brystkreft i kombinasjon med trastuzumab og docetaksel.

Se preparatomtalen for informasjon om advarsler og kontraindikasjoner.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med forbehold)**

**Begrunnelse:**
Pertuzumab har etablert effekt ved HER2-positiv brystkreft, og PR+-sykdom er en undergruppe av dette. Evidensen omfatter en fullført fase 3-studie og flere randomiserte studier (NeoSphere, WSG-ADAPT, WSG TP-II). Fase 3-studien er imidlertid en biosimilarstudie som bekrefter referanselegemidlet, og den ble gjennomført i ER/PR-negativ populasjon. Direkte evidens for PR+-gruppen kommer derfor fra fase 2-studier.

**For å gå videre trengs følgende:**
- Detaljerte data om virkningsmekanisme (MOA)
- Advarsler og kontraindikasjoner fra preparatomtalen, som er en blokkerende datamangel for sikkerhetsvurderingen
- Avklaring av markedsstatus i Norge, siden begge godkjenningene står som avregistrert
- Bekreftelse av HER2-status hos pasientene og et program for hjerteovervåking (LVEF)
- Oppfølging av at fase 2-studien DECRESCENDO ble avsluttet tidlig, noe som begrenser konklusjoner om kjemoterapi-de-eskalering

---

## Andre predikerte indikasjoner (kort)

| Rangering | Predikert indikasjon | Evidensnivå | Anbefaling |
|------|------|------|------|
| 3 | Progesteronreseptor-negativ brystkreft | L1 | Proceed with Guardrails |
| 4 | Luminal A- eller B-brysttumor | L2 | Forskningsspørsmål (gjelder kun HER2+ luminal B) |
| 2, 5–10 | Normal-like brystkreftsubtype, ektomesenkymom, malign kutan granulær celletumor, HHV-8-relatert svulst, nevroendokrin svulst i mellomøret, urotelkarsinom i prostatisk uretra, sarkomatoid overgangscellekarsinom i nyrebekken | L5 | Hold (kun modellprediksjon, ingen studier eller litteratur) |
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

