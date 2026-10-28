---
layout: default
title: Azathioprine
parent: Kun modellprediksjon (L5)
nav_order: 50
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Azathioprine: predikert ny indikasjon Colobomatous microphthalmia-rhizomelic dysplasia syndrome (rangert nr… (evidensnivå L5). Opprinnelig indikasjon: Avstøtning av transplantat (graft rejection)"
monitor_inn: "AZATHIOPRINE"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
---

# Azathioprine
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

## Azatioprin: Fra transplantasjonsavstøtning til Kolobomatøs mikroftalmi-rhizomelisk dysplasi-syndrom
{: .text-alpha }

## Oppsummering

Azatioprin er et immundempende legemiddel som opprinnelig er godkjent for å forebygge avstøtning av transplantert organ (graft rejection).
TxGNN-modellen rangerer flere nye indikasjoner høyt. Den best underbygde er **inflammatorisk tarmsykdom (IBD)**, med **22 kliniske studier** og **19 publikasjoner** i datagrunnlaget. Dette er i praksis en etablert bruk, ikke ny repurposing. Flere av de øvrige prediksjonene, for eksempel sjeldne misdannelsessyndromer, har ingen støtte i data utover modellscoren.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Avstøtning av transplantat (graft rejection) |
| Predikert ny indikasjon | Colobomatous microphthalmia-rhizomelic dysplasia syndrome (rangert nr. 1 av TxGNN; se merknad nedenfor) |
| TxGNN-prediksjonsscore | 1,0000 |
| Evidensnivå | L5 for rangert nr. 1. For IBD og ulcerøs kolitt: L1 |
| Status på det norske markedet | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall autorisasjoner | 1 (avregistrert) |
| Anbefalt beslutning | Hold for rangert nr. 1. Proceed with Guardrails for IBD / ulcerøs kolitt |

**Merknad:** Den høyest rangerte prediksjonen (score 1,0000) er et sjeldent utviklingssyndrom uten studier, litteratur eller plausibel mekanisme.

### Oversikt over de ti øverste prediksjonene

| Rang | Sykdom | Score | Evidensnivå | Anbefaling |
|------|------|------|------|------|
| 1 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 1,0000 | L5 | Hold |
| 2 | Brachydactyly-syndactyly syndrome | 1,0000 | L5 | Hold |
| 4 | WHIM-syndrom | 0,9968 | L5 | Hold |
| 6 | Kronisk granulomatøs sykdom, autosomal recessiv 5 | 0,9941 | L5 | Hold |
| 7 | Osteoartritt | 0,9940 | L5 | Hold |
| 8 | Granulomatøs sykdom med defekt nøytrofil kjemotaksi | 0,9937 | L5 | Hold |
| 10 | Acromesomelic dysplasia, Hunter-Thompson-type | 0,9927 | L5 | Hold |

---

## Hvorfor er prediksjonen rimelig?

Detaljerte mekanismedata (original MOA) er foreløpig ikke tilgjengelige i datagrunnlaget. Ut fra kjent informasjon omdannes azatioprin til 6-merkaptopurin og tioguaninnukleotider. Disse hemmer purinsyntesen og fremmer apoptose av T-celler (blant annet via Rac1-hemming). Dette er den samme immundempende mekanismen som brukes ved transplantasjon.

**IBD og ulcerøs kolitt:** Ved IBD driver overaktivering av slimhinneimmunsystemet sykdommen. Azatioprin demper denne aktiveringen og brukes til å vedlikeholde remisjon og i kombinasjon med TNF-hemmere som infliximab. Mekanismen er derfor godt forenlig med den opprinnelige immundempende bruken. Bruken er allerede veletablert i klinisk praksis.

**Øvrige prediksjoner:** For de sjeldne misdannelsessyndromene (rang 1, 2, 10) og genetiske tilstander (rang 3) finnes ingen plausibel mekanistisk kobling. Ved WHIM-syndrom, kronisk granulomatøs sykdom og defekter i nøytrofilfunksjon kan azatioprins myelosuppresjon og immundempende effekt tvert imot øke risikoen for cytopeni og infeksjon. Osteoartritt (rang 7) har ingen etablert begrunnelse; den hentede litteraturen ser ut til å være funnet via nøkkelordtreff og ikke via relevant evidens.

---

## Kliniske studier (inflammatorisk tarmsykdom)

Utvalg av de mest relevante studiene, prioritert etter direkte bruk av azatioprin:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Fase 3 | Avsluttet tidlig | 242 | Infliximab alene eller sammen med azatioprin versus azatioprin alene ved moderat til alvorlig ulcerøs kolitt |
| [NCT02177071](https://clinicaltrials.gov/study/NCT02177071) | Fase 4 | Fullført | 211 | Infliximab-antimetabolitt-kombinasjon versus monoterapi ved Crohns sykdom i remisjon |
| [NCT03393247](https://clinicaltrials.gov/study/NCT03393247) | Ikke klassifisert | Ukjent | 160 | Azatioprin fra start eller 14 uker etter infliximab ved Crohns sykdom |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Fase 4 | Rekrutterer | 300 | Mirikizumab (top-down) versus standardbehandling med azatioprin ved nydiagnostisert ulcerøs kolitt |
| [NCT02247258](https://clinicaltrials.gov/study/NCT02247258) | Fase 2 | Avsluttet tidlig | 63 | Systematisk versus endoskopistyrt azatioprin for å forebygge tilbakefall etter kirurgi ved ileal Crohns sykdom |
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Fase 3 | Fullført | 83 | Azatioprin versus mesalazin for å forebygge postoperativt tilbakefall ved Crohns sykdom |
| [NCT01564823](https://clinicaltrials.gov/study/NCT01564823) | Fase 3 | Fullført | 86 | Adalimumab versus azatioprin for å forebygge postoperativt tilbakefall ved Crohns sykdom |
| [NCT02425852](https://clinicaltrials.gov/study/NCT02425852) | Fase 4 | Fullført | 65 | Tidlig azatioprin pluss infliximab versus kortikosteroider pluss azatioprin ved akutt alvorlig kolitt |
| [NCT03101800](https://clinicaltrials.gov/study/NCT03101800) | Fase 3 | Ukjent | 84 | Lavdose azatioprin pluss allopurinol versus azatioprin alene ved ulcerøs kolitt |
| [NCT00521950](https://clinicaltrials.gov/study/NCT00521950) | Ikke klassifisert | Fullført | 853 | TPMT-genotyping før tiopurinbehandling; relevant for sikkerhet og dosering |

Flere av studiene ble avsluttet tidlig med få deltakere, noe som begrenser tolkningen. Ved de øvrige prediksjonene er det registrert ingen kliniske studier.

---

## Litteraturevidens (inflammatorisk tarmsykdom og ulcerøs kolitt)

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE-studien: top-down infliximab pluss azatioprin versus azatioprin alene ved akutt alvorlig ulcerøs kolitt som responderer på intravenøse steroider |
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Systematisk oversikt | Cochrane Database Syst Rev | Oppdatert vurdering av azatioprin og 6-merkaptopurin for vedlikehold av remisjon ved ulcerøs kolitt |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Systematisk oversikt | Cochrane Database Syst Rev | Tidligere Cochrane-oversikt om samme spørsmål; effekten ble beskrevet som omdiskutert |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Metaanalyse | Aliment Pharmacol Ther | Effekt av azatioprin og merkaptopurin ved ulcerøs kolitt |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Oversikt | J Crohns Colitis | Nye funn og perspektiver for tiopuriner ved IBD |
| [16048561](https://pubmed.ncbi.nlm.nih.gov/16048561/) | 2005 | Oversikt | J Gastroenterol Hepatol | Farmakogenetikk og metabolittmonitorering; alvorlig toksisitet fører til seponering hos 9–25 % |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Oversikt | Expert Rev Gastroenterol Hepatol | Molekylære mekanismer og kliniske implikasjoner av azatioprin ved IBD |
| [15177535](https://pubmed.ncbi.nlm.nih.gov/15177535/) | 2004 | Oversikt | Gastroenterol Clin North Am | Kritisk gjennomgang av effekt og toksisitet av azatioprin og 6-merkaptopurin |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Prekliniske/mekanistisk | Cell Rep Med | Tarmbakterier (Blautia wexlerae) kan gi behandlingssvikt ved å redusere biotilgjengeligheten av 6-merkaptopurin |
| [32799195](https://pubmed.ncbi.nlm.nih.gov/32799195/) | 2020 | Oversikt | Digestion | Sammenheng mellom IBD og kreft |

---

## Informasjon om det norske markedet

| Autorisasjonsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005055 | Jayempi | Ikke oppgitt | Graft rejection (godkjent) |

Legemidlet er markedsført; 1 av 1 autorisasjon er gyldig.

---

## Sikkerhetsvurderinger

- **Kontraindikasjoner fra kunnskapsgrafen (ikke preparatomtale):** TxGNN-kunnskapsgrafen kobler azatioprin til følgende tilstander: pankreatitt, trombocytopeni, anemi (inkludert makrocytær anemi), nedsatt nyrefunksjon, infeksjonssykdommer (inkludert soppinfeksjoner og dermatofytose), lymfom (inkludert primært lymfom i sentralnervesystemet, lymfosarkom og hepatosplenisk T-cellelymfom), levervenetrombose og Budd-Chiari syndrom.
- **Legemiddelinteraksjoner:** 100 interaksjoner er registrert. Moderat alvorlighetsgrad gjelder aminosalisylater: mesalazin, balsalazid, olsalazin og sulfasalazin. Minor gjelder sinksalter (sinkacetat, sinkglukonat, sinksulfat). Flere andre (blant annet acetylsalisylsyre, amfotericin B, metformin, omeprazol og pantoprazol) har ukjent alvorlighetsgrad.
- **Forholdsregler som fremgår av litteratur og vurdering:** TPMT/NUDT15-genotyping, kontroll av blodtelling og leverfunksjon, metabolittmonitorering samt oppmerksomhet på risiko for malignitet (lymfom, hudkreft) og infeksjoner. Pankreatitt er en kjent tiopurinbivirkning.

Det mangler data fra preparatomtalen om advarsler og kontraindikasjoner. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Hold for høyest rangerte prediksjon (rang 1–4, 6–8, 10). Proceed with Guardrails for inflammatorisk tarmsykdom og ulcerøs kolitt.**

**Begrunnelse:**
- De høyest scorende prediksjonene er sjeldne genetiske eller utviklingsrelaterte tilstander uten studier, litteratur eller plausibel mekanisme, og for enkelte (WHIM, granulomatøs sykdom) er azatioprin potensielt skadelig. Scoren alene er ikke et tilstrekkelig grunnlag.
- For IBD og ulcerøs kolitt støtter flere randomiserte studier (inkludert fase 3), Cochrane-oversikter og en nylig RCT bruken. Dette er imidlertid allerede etablert klinisk praksis, så rapporten bekrefter validert bruk mer enn ny repurposing.

**For å gå videre trengs følgende:**
- Sikkerhetsdata fra preparatomtalen (advarsler og kontraindikasjoner), som i dag mangler og er registrert som blokkerende datahull
- Data om virkningsmekanisme (MOA) fra DrugBank
- Plan for sikkerhetsmonitorering: TPMT/NUDT15-testing, blodtelling, leverprøver og overvåking av malignitet og infeksjon
- Avklaring av regulatorisk status i Norge, siden eneste autorisasjon er avregistrert
- Vurdering av tilgjengelige legemiddelformer og administrasjonsveier (ikke vurdert i datagrunnlaget)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

