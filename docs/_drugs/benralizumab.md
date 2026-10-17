---
layout: default
title: Benralizumab
parent: Kun modellprediksjon (L5)
nav_order: 56
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-15
description: "Benralizumab: predikert ny indikasjon Dermatitt (rangert som nr. 2 (evidensnivå L5). Opprinnelig indikasjon: Astma"
monitor_inn: "BENRALIZUMAB"
predicted_indications: ["thrombocytopenia due to immune destruction", "dermatitis", "acne keloid", "neonatal dermatomyositis", "amyopathic dermatomyositis"]
---

# Benralizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Benralizumab: Fra astma til dermatitt

## Oppsummering i én setning

Benralizumab er et monoklonalt antistoff mot IL-5-reseptor α, opprinnelig brukt til behandling av astma.
TxGNN-modellen predikerer at legemidlet kan ha effekt ved **dermatitt**.
Det finnes **3 kliniske studier** og **19 publikasjoner** (hovedsakelig oversiktsartikler) i dataene som er sammenstilt for denne rapporten, men ingen bekreftede effektresultater.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Astma |
| Predikert ny indikasjon | Dermatitt (rangert som nr. 2; se merknad nedenfor) |
| TxGNN-prediksjonsscore | 99,16 % |
| Evidensnivå | L2 (formelt nivå i dataene; se merknad om styrken nedenfor) |
| Status i Norge | Kun avregistrert |
| Antall godkjenninger | 1 (avregistrert) |
| Anbefalt beslutning | Hold |

**Merknad om valg av indikasjon:** Den høyest rangerte prediksjonen, immunmediert trombocytopeni (99,34 %), har ingen kliniske studier eller litteratur (L5). Rapporten fokuserer derfor på dermatitt, som er den best underbygde prediksjonen. De øvrige prediksjonene (aknekeloid, neonatal dermatomyositt og amyopatisk dermatomyositt) har heller ingen støtte utover modellscore.

---

## Hvorfor er denne prediksjonen rimelig?

Data om detaljert virkningsmekanisme er foreløpig ikke tilgjengelig fra legemiddeldatabasen. Basert på kjent informasjon binder benralizumab IL-5Rα og fører til uttømming av eosinofile og basofile granulocytter gjennom forsterket antistoffavhengig cellemediert cytotoksisitet (ADCC). Effekten er dokumentert ved eosinofil astma.

Eosinofile, basofile og medfødte lymfoide celler (ILC2) bidrar til type 2-betennelse i huden ved atopisk dermatitt. Det er derfor biologisk plausibelt at uttømming av disse cellene kan dempe hudbetennelsen. Det er imidlertid viktig å understreke at den randomiserte placebokontrollerte fase 2-studien (NCT04605094) ble avsluttet tidlig, og at ingen effektresultater er tilgjengelige i dataene. Et negativt eller virkningsløst signal kan ikke utelukkes. Prediksjonen er dermed ikke bekreftet.

---

## Kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT03563066](https://clinicaltrials.gov/study/NCT03563066) | Fase 2 | Fullført | 20 | Mekanistisk studie av effekter på eosinofile, basofile og ILC2-celler ved atopisk dermatitt; ingen kliniske effektdata i dataene |
| [NCT06734884](https://clinicaltrials.gov/study/NCT06734884) | Fase 2 | Ikke rekruttert ennå | 96 | Effekt og sikkerhet ved legemiddelreaksjon med eosinofili og systemiske symptomer (DRESS); planlagt oppstart 2027 |
| [NCT04605094](https://clinicaltrials.gov/study/NCT04605094) | Fase 2 | Avsluttet tidlig | 194 | Randomisert, dobbeltblindet, placebokontrollert 16-ukers studie (HILLIER) ved moderat til alvorlig atopisk dermatitt; årsak og resultater er ikke oppgitt |

---

## Litteraturevidens

Alle publikasjonene nedenfor er oversiktsartikler. Ingen av dem gir direkte effektdata for benralizumab ved dermatitt. Nedenfor listes de ti mest relevante.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [31690400](https://pubmed.ncbi.nlm.nih.gov/31690400/) | 2019 | Oversikt | Allergy Asthma Proc | Gjennomgang av biologiske legemidler (inkl. anti-IL-5) ved alvorlig astma, atopisk dermatitt og kronisk urtikaria |
| [34642091](https://pubmed.ncbi.nlm.nih.gov/34642091/) | 2021 | Oversikt | Ann Allergy Asthma Immunol | Veiledning for valg av biologiske legemidler ved allergi, astma og atopisk dermatitt |
| [37170653](https://pubmed.ncbi.nlm.nih.gov/37170653/) | 2023 | Oversikt | Clin Transl Sci | Immunterapi ved allergiske tilstander, inkludert atopisk dermatitt |
| [39600395](https://pubmed.ncbi.nlm.nih.gov/39600395/) | 2024 | Oversikt | Allergologie Select | Oppdatering om biologiske legemidler ved atopiske sykdommer, urtikaria og angioødem, med vekt på overfølsomhetsreaksjoner |
| [33236428](https://pubmed.ncbi.nlm.nih.gov/33236428/) | 2020 | Oversikt | Pediatr Allergy Immunol | Anti-IL-5 ved allergiske sykdommer hos barn |
| [31994421](https://pubmed.ncbi.nlm.nih.gov/31994421/) | 2020 | Oversikt | Expert Rev Clin Immunol | Overfølsomhet og bivirkninger ved biologiske legemidler mot astma og allergi |
| [35987486](https://pubmed.ncbi.nlm.nih.gov/35987486/) | 2022 | Oversikt | J Allergy Clin Immunol Pract | Sikkerhet ved biologiske legemidler under graviditet |
| [36411004](https://pubmed.ncbi.nlm.nih.gov/36411004/) | 2023 | Oversikt | Immunol Allergy Clin North Am | Monoklonale antistoffer under graviditet og amming |
| [37259416](https://pubmed.ncbi.nlm.nih.gov/37259416/) | 2023 | Oversikt | Pharmaceuticals (Basel) | Biologisk behandling ved astma og allergisk sykdom: fortid, nåtid og fremtid |
| [42383238](https://pubmed.ncbi.nlm.nih.gov/42383238/) | 2026 | Oversikt | Curr Ther Res | Monoklonale antistoffer ved atopisk dermatitt hos barn |

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004433 | Fasenra | Ikke oppgitt | Astma (avregistrert) |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:** Interaksjonsspørringen ga kun en farmakologisk målrelasjon (benralizumab binder IL-5-reseptor α-underenheten, IL5RA). Ingen interaksjoner med andre legemidler er identifisert.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er biologisk plausibel, men den eneste store placebokontrollerte studien ved atopisk dermatitt ble avsluttet tidlig uten tilgjengelige resultater, og litteraturen består kun av oversiktsartikler. I tillegg er produktet avregistrert i Norge, og preparatomtalen med advarsler og kontraindikasjoner mangler i dataene.

**For å gå videre kreves følgende:**
- Årsaken til avslutningen og resultatene fra NCT04605094 (HILLIER)
- Resultater fra NCT03563066 og senere NCT06734884 (DRESS)
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel)
- Detaljerte data om virkningsmekanisme fra DrugBank
- Avklaring av regulatorisk status i Norge (kun avregistrert godkjenning)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

