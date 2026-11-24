---
layout: default
title: Clopidogrel
parent: Kun modellprediksjon (L5)
nav_order: 102
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Clopidogrel: predikert ny indikasjon Migrene med hjernestammeaura (evidensnivå L5). Opprinnelig indikasjon: Perifer karsykdom, hjerneslag, hjerteinfarkt…"
monitor_inn: "CLOPIDOGREL"
predicted_indications: ["migraine with brainstem aura", "migraine disorder", "osteoarthritis", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "rheumatoid arthritis"]
---

# Clopidogrel
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

## Clopidogrel: Fra hjerte- og karsykdommer til migrene med hjernestammeaura
{: .text-alpha }

## Oppsummering

Clopidogrel er en blodplatehemmer (P2Y12-hemmer) som opprinnelig brukes til å forebygge aterotrombotiske hendelser ved hjerteinfarkt, akutt koronarsyndrom, hjerneslag og perifer karsykdom.
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **migrene** (høyest rangerte forslag: migrene med hjernestammeaura, deretter generell migrene). Det er best støtte for **migrene med høyre-til-venstre-shunt/patent foramen ovale (PFO)**, med **6 kliniske studier** og **20 publikasjoner** for migrene som helhet.
Det er ingen Fase 3-studie som tester clopidogrel direkte som migreneprofylakse.

> **Merk:** Rapporten omfatter de åtte høyest rangerte forslagene fra modellen. Hovedvekten ligger på **migrene** (forslag nr. 2), som har klart sterkest evidens. Forslag nr. 1 (migrene med hjernestammeaura) har ingen egne registrerte studier.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Perifer karsykdom, hjerneslag, hjerteinfarkt, akutt koronarsyndrom (enkelte preparater også atrieflimmer) |
| Predikert ny indikasjon | Migrene (migrene med aura / PFO-assosiert migrene); modellens topprangerte forslag er migrene med hjernestammeaura |
| TxGNN-prediksjonsscore | 0,9944 (migrene med hjernestammeaura); 0,9944 (migrene) |
| Evidensnivå | L5 for migrene; L3 for migrene med hjernestammeaura |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 16 av 16) |
| Antall godkjenninger | 16 (gyldige: 16) |
| Antall tillatelser | 16 (alle avregistrert) |
| Anbefalt beslutning | Proceed with Guardrails (for migrene med PFO, som forskningsspørsmål); Hold for øvrige forslag |

---

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Clopidogrel (uoffisiell oversettelse): «Klopidogrel er en hemmer av blodplateaktivering og -aggregering gjennom irreversibel binding av sin aktive metabolitt til P2Y 12 -klassen av ADP-reseptorer på blodplater.» Engelsk originaltekst: "Clopidogrel is an inhibitor of platelet activation and aggregation through the irreversible binding of its active metabolite to the P2Y 12 class of ADP receptors on platelets." ([DailyMed: Plavix (clopidogrel) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de8b0b67-eb25-4684-83b5-7ad785314227), versjon av 2025-05-30; hentet 2026-11-19). Clopidogrel er en blodplatehemmer som blokkerer P2Y12-reseptoren og dermed ADP-avhengig blodplateaktivering. Effekten er godt dokumentert ved hjerte- og karsykdommer.

Den mulige koblingen til migrene går via blodplateaktivering og paradoksale mikroemboli, særlig hos pasienter med patent foramen ovale (PFO) eller andre høyre-til-venstre-shunter. Slike mikroemboli, og frigjøring av vasoaktive stoffer som serotonin fra blodplater, kan utløse kortikal spredende depresjon, som antas å ligge bak migreneaura. Flere kasuistikker og kohortstudier viser at migrene som oppstår eller forverres etter lukking av atrieseptumdefekt, bedres med clopidogrel.

For de øvrige forslagene (artrose, tendinitt, myositt, revmatoid artritt) finnes det ingen overbevisende mekanistisk begrunnelse. For revmatoid artritt peker litteraturen snarere mot en mulig skadesignal (clopidogrel-assosiert inflammatorisk artritt).

---

## Klinisk studieevidens

Studier for **migrene** (forslag nr. 2):

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Fase 4 | Fullført | 220 | CANOA: clopidogrel i tillegg til aspirin for å forebygge nyoppstått migrene etter transkateter-lukking av atrieseptumdefekt |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Fase 2 | Fullført | 1000 | COMPETE: antikoagulasjon vs. blodplatehemmer vs. migrenemedisin ved migrene med PFO |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Fase 4 | Ukjent | 50 | Clopidogrel som profylakse ved migrene med høyre-til-venstre-shunt; liten studie med begrenset pålitelighet |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Fase 3 | Aktiv, ikke rekrutterende | 440 | SPRING: PFO-lukking vs. medikamenter ved migrene (kun indirekte relevans for clopidogrel) |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Fase 3 | Fullført | 664 | CLOSE: PFO-lukking eller antikoagulasjon vs. blodplatehemmer for å forebygge slagresidiv; migrene er ikke primært endepunkt |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Ikke relevant | Avsluttet | 7 | Septumokkluder ved migrene; avsluttet tidlig og uten clopidogrel |

For migrene med hjernestammeaura, artrose, tendinitt, myositt og revmatoid artritt er det ingen registrerte kliniske studier.

---

## Litteraturevidens

Utvalg for **migrene**:

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [42526943](https://pubmed.ncbi.nlm.nih.gov/42526943/) | 2026 | RCT | BMJ | Multisenter, åpen, aktivt kontrollert studie av antitrombotisk behandling ved migrene med PFO |
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | JAMA | CANOA: clopidogrel + aspirin vs. aspirin alene etter lukking av atrieseptumdefekt |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT | JAMA Cardiology | CANOA ettårsresultater etter seponering av clopidogrel ved 3 måneder |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | RCT (pilot) | Cephalalgia | Pilotstudie av clopidogrel som migreneprofylakse |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematisk oversikt | Headache | Vurdering av antitrombotika i migreneforebygging; forsiktig om samlet evidensstyrke |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Systematisk oversikt | Indian J Thorac Cardiovasc Surg | Nyoppstått hodepine etter lukking av atrieseptumdefekt |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Kohort | J Investig Med | Clopidogrel som tilleggsprofylakse ved legemiddelresistent migrene med PFO |
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | Retrospektiv kohort | Neurology | Tienopyridinbehandling hos migrenepasienter med PFO |
| [24770421](https://pubmed.ncbi.nlm.nih.gov/24770421/) | 2014 | Retrospektiv gjennomgang | Cephalalgia | Clopidogrel som primærbehandling ved migrene med høyre-til-venstre-shunt |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Kohort | Heart | Clopidogrel reduserer migrene med aura etter lukking av PFO/atrieseptumdefekt |

For de øvrige forslagene er litteraturen i hovedsak ikke klinisk evidens for nytte. Eksempler: en kohortstudie tyder på lavere artroserisiko med tikagrelor enn med clopidogrel (PMID 32564514), og for revmatoid artritt er det rapportert clopidogrel-assosiert inflammatorisk artritt (PMID 38107217).

---

## Markedsinformasjon for Norge

Markedsført: 16 av 16 tillatelser er gyldige.

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000174 | Plavix | clopidogrel hydrogen sulfate | Stroke; Peripheral Vascular Diseases; Atrial Fibrillation; Myocardial Infarction; Acute Coronary Syndrome | Gyldig |
| EMEA/H/C/000175 | Iscover | clopidogrel | Stroke; Peripheral Vascular Diseases; Atrial Fibrillation; Myocardial Infarction; Acute Coronary Syndrome | Gyldig |
| EMEA/H/C/000975 | Clopidogrel Zentiva (previously Clopidogrel Winthrop) | clopidogrel | Stroke; Peripheral Vascular Diseases; Myocardial Infarction; Acute Coronary Syndrome | Gyldig |
| EMEA/H/C/001053 | Clopidogrel Teva (hydrogen sulphate) | clopidogrel (as hydrogen sulfate) | Acute Coronary Syndrome; Peripheral Vascular Diseases; Myocardial Infarction; Stroke | Gyldig |
| EMEA/H/C/001056 | Clopidogrel Krka | clopidogrel (as hydrochloride) | Peripheral Vascular Diseases; Stroke; Myocardial Infarction | Gyldig |
| EMEA/H/C/001058 | Zyllt | clopidogrel (as hydrogen sulfate) | Peripheral Vascular Diseases; Stroke; Acute Coronary Syndrome; Myocardial Infarction | Gyldig |
| EMEA/H/C/001059 | Grepid | clopidogrel (as besilate) | Peripheral Vascular Diseases; Stroke; Myocardial Infarction | Gyldig |
| EMEA/H/C/001134 | Clopidogrel Taw Pharma (previously Clopidogrel Mylan) | clopidogrel hydrochloride | Peripheral Vascular Diseases; Stroke; Myocardial Infarction; Acute Coronary Syndrome | Gyldig |
| EMEA/H/C/001136 | Clopidogrel TAD | clopidogrel (as hydrochloride) | Peripheral Vascular Diseases; Stroke; Myocardial Infarction | Gyldig |
| EMEA/H/C/001137 | Clopidogrel Krka d.d. (previously Zopya) | clopidogrel (as hydrochloride) | Peripheral Vascular Diseases; Stroke; Myocardial Infarction | Gyldig |
| EMEA/H/C/001138 | Clopidogrel BGR (previously Zylagren) | clopidogrel (as hydrogen sulfate) | Peripheral Vascular Diseases; Stroke; Myocardial Infarction | Gyldig |
| EMEA/H/C/001143 | DuoPlavin | clopidogrel; acetylsalicylic acid | Acute Coronary Syndrome; Myocardial Infarction | Gyldig |
| EMEA/H/C/001144 | Clopidogrel/Acetylsalicylic acid Zentiva (previously DuoCov… | clopidogrel; acetylsalicylic acid | Acute Coronary Syndrome; Myocardial Infarction | Gyldig |
| EMEA/H/C/002255 | Clopidogrel HCS | clopidogrel (as hydrochloride) | Peripheral Vascular Diseases; Acute Coronary Syndrome; Myocardial Infarction; Stroke | Gyldig |
| EMEA/H/C/004006 | Clopidogrel ratiopharm | clopidogrel (as hydrogen sulfate) | Myocardial Infarction; Acute Coronary Syndrome; Peripheral Vascular Diseases; Stroke | Gyldig |
| EMEA/H/C/004996 | Clopidogrel / Acetylsalicylic acid Viatris (previously Clop… | acetylsalicylic acid; clopidogrel hydrogen sulfate | Acute Coronary Syndrome; Myocardial Infarction | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

**Mulige kontraindikasjoner (fra kunnskapsgrafen, ikke fra preparatomtale):** akutt leversvikt, hepatitt, blodkoagulasjonssykdom, skade/traume, trombocytopenisk purpura, aktivt magesår og intrakraniell blødning.

**Legemiddelinteraksjoner** (100 registrert; utvalg):
- **Alvorlig (Major):** rabeprazol, omeprazol, esomeprazol (protonpumpehemmere, via CYP2C19), pioglitazon, loperamid, repaglinid
- **Moderat:** acetylsalisylsyre, bupropion, morfin, cimetidin, klaritromycin, lansoprazol, pantoprazol, opium, fenfluramin, deksfenfluramin, eluxadolin, sibutramin
- **Mindre:** deksansoprazol, glimepirid

Blødningsrisiko er en sentral bekymring, spesielt ved kombinasjon med acetylsalisylsyre eller NSAID. Se preparatomtalen for fullstendig sikkerhetsinformasjon, da data fra preparatomtalen ikke var tilgjengelige for denne rapporten.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails** (kun for migrene, særlig migrene med PFO/høyre-til-venstre-shunt, som forskningsspørsmål). **Hold** for migrene med hjernestammeaura, artrose, tendinitt, myositt, revmatoid artritt og artroserisiko.

**Begrunnelse:**
- For migrene finnes det randomiserte studier (CANOA, pilot-RCT, COMPETE/BMJ 2026), men resultatene er heterogene, mye av evidensen gjelder etter lukking av septumdefekt, og ingen Fase 3-studie tester clopidogrel direkte som migreneprofylakse.
- De øvrige forslagene mangler mekanistisk begrunnelse og klinisk evidens, og for revmatoid artritt finnes det et mulig skadesignal.

**For å gå videre trengs følgende:**
- Gjennomgang av resultatene fra COMPETE/BMJ-studien (2026) for clopidogrel-armen spesielt
- En dedikert randomisert Fase 3-studie av clopidogrel som migreneprofylakse i en tydelig definert populasjon (PFO/høyre-til-venstre-shunt)
- Data om virkningsmekanisme og fullstendig sikkerhetsinformasjon fra preparatomtale (advarsler og kontraindikasjoner)
- Blødningsrisikovurdering og plan for håndtering av interaksjoner (særlig protonpumpehemmere og acetylsalisylsyre)
- Avklaring av regulatorisk vei i Norge for clopidogrel, som er markedsført med 16 gyldige tillatelser

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Plavix (clopidogrel) prescribing information, Sanofi-Aventis U.S. LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de8b0b67-eb25-4684-83b5-7ad785314227) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

