---
layout: default
title: Sacubitril
parent: Moderat evidens (L3-L4)
nav_order: 374
evidence_level: L3
indication_count: 5
---

# Sacubitril
{: .fs-9 }

Evidensnivå: **L3** | Predikerte indikasjoner: **5** stk.
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

# Sacubitril: Fra hjertesvikt til diabetisk nefropati

## Oppsummering i én setning

Sacubitril er en nøkkelkomponent i kombinasjonen sacubitril/valsartan, som opprinnelig brukes til behandling av hjertesvikt.
TxGNN-modellen forutsier at den kan ha effekt ved **diabetisk nefropati**, og for dette området foreligger det **1 klinisk studie** (fase 4, resultater ikke tilgjengelige) og **15 publikasjoner**, hovedsakelig prekliniske studier og oversiktsartikler.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hjertesvikt |
| Foreslått ny indikasjon | Diabetisk nefropati (diabetic nephropathy) |
| TxGNN-prediksjonsscore | 99,50 % |
| Evidensnivå | L3 |
| Markedsstatus i Norge | Kun opphevede (avregistrerte) tillatelser |
| Antall tillatelser | 2 (begge opphevet) |
| Anbefalt beslutning | Proceed with Guardrails |

*Merknad: Den høyest rangerte prediksjonen i TxGNN (rangert som nr. 1) er «brain small vessel disease 1 with or without ocular anomalies» (score 99,58 %). Den har imidlertid ingen støttende evidens (L5). Diabetisk nefropati (nr. 3) er derfor valgt som hovedfokus, siden det er den eneste prediksjonen med klinisk og preklinisk grunnlag.*

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanismen (MOA) er for øyeblikket ikke tilgjengelige i dataene som er sammenstilt for denne rapporten. Basert på kjent informasjon er sacubitril en del av kombinasjonen sacubitril/valsartan (en angiotensinreseptor-neprilysinhemmer, ARNI). Effekten ved hjertesvikt er dokumentert, og mekanistisk kan den være aktuell også ved diabetisk nefropati.

Valsartan blokkerer renin-angiotensin-systemet (RAAS), som er en etablert hjørnestein i nyrebeskyttende behandling ved diabetisk nyresykdom. Sacubitril hemmer neprilysin og øker dermed nivået av natriuretiske peptider, som kan gi tilleggsgevinst gjennom antifibrotiske, antiinflammatoriske og hemodynamiske effekter.

Prekliniske studier på gnagere (PMID 35992034, 36589853, 32596035, 33870733) rapporterer redusert oksidativt stress, NF-κB-mediert inflammasjon og fibrose, samt bedre nyreutfall. Direkte humane effektdata ved diabetisk nefropati mangler imidlertid i de tilgjengelige dataene, og evidensnivået er derfor L3 og ikke høyere.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Fase 4 | Ukjent | 297 | Randomisert, kontrollert multisenterstudie som sammenligner sacubitril/valsartan med valsartan hos pasienter med essensiell hypertensjon og type 2-diabetisk nefropati over 12 uker. Ingen resultater tilgjengelige. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | Sekundæranalyse av RCT (PARADIGM-HF) | The Lancet Diabetes & Endocrinology | Undersøker effekten av neprilysinhemming på nyrefunksjon hos pasienter med type 2-diabetes og kronisk hjertesvikt |
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | Klinisk studie (randomisert) | International Immunopharmacology | 112 pasienter med diabetisk nefropati og hypertensjon; nifedipin kombinert med sacubitril/valsartan sammenlignet med nifedipin kombinert med valsartan |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Klinisk studie | Diabetes, Metabolic Syndrome and Obesity | BOLD-MR-vurdering av nyrebeskyttende effekt av sacubitril/valsartan ved diabetisk nefropati |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Oversikt | Diabetes Care | Oppdatering om hjørnesteinene i behandling som bremser progresjon av diabetisk nefropati |
| [35165832](https://pubmed.ncbi.nlm.nih.gov/35165832/) | 2022 | Oversikt | Current Hypertension Reports | Nyere blodtrykkssenkende legemidler og beskyttelse mot hypertensiv organskade |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Preklinisk (rotte) | Diabetes Metab Syndr Obes | Sacubitril/valsartan bremser progresjon av tidlig diabetisk nefropati via hemming av NLRP3-inflammasomet |
| [36589853](https://pubmed.ncbi.nlm.nih.gov/36589853/) | 2022 | Preklinisk (mus) | Frontiers in Endocrinology | Bedring av diabetisk nyresykdom og påvirkning av tarmmikrobiota |
| [32596035](https://pubmed.ncbi.nlm.nih.gov/32596035/) | 2020 | Preklinisk (rotte) | PeerJ | LCZ696 reduserer oksidativt stress, NF-κB-mediert inflammasjon og glomerulosklerose |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | Preklinisk (mus) | Am J Physiol Renal Physiol | Ulik effekt i db/db- og KKAy-mus sammenlignet med valsartan |
| [37202215](https://pubmed.ncbi.nlm.nih.gov/37202215/) | 2023 | Preklinisk (mus) | Nephrol Dial Transplant | Reduserer tubulointerstitiell nyreskade ved økt renal plasmastrøm ved aldosteronoverskudd |

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004343 | Neparvis | – | Hjertesvikt (opphevet) |
| EMEA/H/C/004062 | Entresto | – | Hjertesvikt (opphevet) |

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (6 registrert, alle med alvorlighetsgrad moderat):
- Nitisinon
- Rosuvastatin
- Simvastatin
- Kobicistat
- Revefenacin
- Alpelisib

For øvrig sikkerhetsinformasjon, se preparatomtalen (SPC). Ved bruk ved diabetisk nefropati bør risiko for hyperkalemi og hypotensjon vurderes spesielt.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails**

**Begrunnelse:**
Diabetisk nefropati har plausibel mekanistisk støtte (RAAS-blokade pluss neprilysinhemming), konsistente prekliniske funn og én randomisert fase 4-studie (n = 297). Studien har imidlertid ukjent status og ingen publiserte resultater, så det finnes ennå ikke solide humane effektdata. De øvrige fire prediksjonene (rangert 1, 2, 4 og 5) mangler støttende evidens og bør settes på vent (Hold).

**For å gå videre kreves følgende:**
- Resultater fra NCT06501651 og bekreftelse av studiens status
- Humane data på nyreutfall (f.eks. albuminuri, eGFR-forløp) i en tilstrekkelig stor populasjon
- Data om virkningsmekanisme (MOA) fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (for øyeblikket ikke tilgjengelig i dataene)
- Vurdering av regulatorisk status i Norge, ettersom begge tillatelsene er opphevet
- Plan for sikkerhetsovervåking av hyperkalemi, hypotensjon og nyrefunksjon
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

