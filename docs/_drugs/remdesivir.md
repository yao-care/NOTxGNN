---
layout: default
title: Remdesivir
parent: Kun modellprediksjon (L5)
nav_order: 354
evidence_level: L5
indication_count: 6
---

# Remdesivir
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

# Remdesivir: Fra COVID-19 til HIV-infeksjon

## Oppsummering i én setning

Remdesivir er et antiviralt middel (nukleotidanalog) som opprinnelig brukes til behandling av COVID-19.
TxGNN-modellen predikerer at det kan ha effekt mot **HIV-infeksjon** (den best dokumenterte av de predikerte indikasjonene), men beviset er svakt: det finnes bare **1 klinisk studie** (en farmakokinetikkstudie, ikke en effektstudie mot HIV) og litteratur som nesten utelukkende handler om COVID-19.
Den høyest rangerte prediksjonen, multippel endokrin neoplasi, har ingen støtte i studier eller litteratur.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | COVID-19-virusinfeksjon |
| Predikert ny indikasjon | HIV-infeksjon (rangert som nr. 2; nr. 1 er multippel endokrin neoplasi uten støtte i data) |
| TxGNN-prediksjonsscore | 99,32 % (HIV-infeksjon); 99,50 % (multippel endokrin neoplasi) |
| Evidensnivå | L4 (HIV-infeksjon); L5 (multippel endokrin neoplasi) |
| Markedsstatus i Norge | Kun kansellert |
| Antall godkjenninger | 1 (kansellert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er ikke tilgjengelig i de innsamlede dataene. Ut fra kjent informasjon er remdesivir en nukleotidanalog-prodrug som hemmer viral RNA-avhengig RNA-polymerase. Effekten mot COVID-19 er dokumentert i flere fase 3-studier.

HIV er også et RNA-virus, noe som gir en løs konseptuell begrunnelse. Likevel er HIV-replikasjon avhengig av revers transkriptase og integrasjon i vertens DNA, og remdesivir har ingen etablert anti-HIV-aktivitet. Den høye TxGNN-scoren er derfor først og fremst en grafbasert likhetsprediksjon, ikke en mekanistisk bekreftet kobling.

For de øvrige predikerte indikasjonene (multippel endokrin neoplasi, neuroutviklingsforstyrrelse, homozygot familiær hyperkolesterolemi) er det ikke identifisert noen plausibel mekanistisk kobling. Disse sykdommene skyldes arvelige genetiske defekter som ikke er relatert til remdesivirs antivirale mekanisme. Prediksjonene for felint og simiant immunsviktvirus (dyresykdommer) gjenspeiler trolig likhet med andre lentivirussykdommer i kunnskapsgrafen, uten direkte evidens.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT04385719](https://clinicaltrials.gov/study/NCT04385719) | Fase 2 | Fullført | 24 | Åpen, randomisert enkeltdose-IV-studie på friske frivillige i Uganda om hvordan faste kombinasjoner (tenofovir/lamivudin eller atazanavir/ritonavir) påvirker remdesivirs farmakokinetikk. Gir ingen effektdata for HIV. |

Merk: Kun studien for HIV-infeksjon er listet. Det finnes ingen registrerte studier for de øvrige predikerte indikasjonene.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [33264556](https://pubmed.ncbi.nlm.nih.gov/33264556/) | 2021 | RCT | N Engl J Med | WHO Solidarity: reetablerte antivirale midler (inkl. remdesivir) ved COVID-19 på innlagte pasienter |
| [35817072](https://pubmed.ncbi.nlm.nih.gov/35817072/) | 2022 | RCT | Lancet Respir Med | Tiksagevimab-cilgavimab versus placebo hos innlagte COVID-19-pasienter som fikk remdesivir |
| [38675889](https://pubmed.ncbi.nlm.nih.gov/38675889/) | 2024 | RCT (post hoc) | Viruses | Ingen remdesivirresistens observert i fase 3 SIMPLE-studiene ved COVID-19 |
| [35229634](https://pubmed.ncbi.nlm.nih.gov/35229634/) | 2022 | In vitro/dyr | mBio | Kobicistat (HIV-booster) virker synergistisk med remdesivir mot SARS-CoV-2 in vitro og hos hamstere |
| [34696838](https://pubmed.ncbi.nlm.nih.gov/34696838/) | 2021 | Oversikt | The Enzymes | Mekanismer for hemming av viral RNA-replikasjon med nukleotidanaloger; sammenligner SARS-CoV-2 RdRp med HIV revers transkriptase |
| [34859557](https://pubmed.ncbi.nlm.nih.gov/34859557/) | 2022 | Kohort | HIV Medicine | Høy frekvens av potensielle legemiddelinteraksjoner hos HIV-positive som behandles for COVID-19 |
| [41136410](https://pubmed.ncbi.nlm.nih.gov/41136410/) | 2025 | Oversikt | Nat Rev Dis Primers | Oversikt over akutt SARS-CoV-2-infeksjon |
| [33002954](https://pubmed.ncbi.nlm.nih.gov/33002954/) | 2020 | Oversikt | Curr Opin HIV AIDS | Reetablerte legemidler mot COVID-19 |
| [36347057](https://pubmed.ncbi.nlm.nih.gov/36347057/) | 2022 | Oversikt | Top Antivir Med | CROI 2022: fremskritt i antiviral behandling for HIV, COVID-19 og viral hepatitt |
| [36097825](https://pubmed.ncbi.nlm.nih.gov/36097825/) | 2023 | Kohort | Clin Infect Dis | Subgenomisk RNA for å følge respons på remdesivir ved COVID-19 |

Litteraturen gir bare indirekte støtte for HIV; ingen publikasjoner viser anti-HIV-effekt av remdesivir.

---

## Informasjon om markedet i Norge

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005622 | Veklury (Gilead Sciences Ireland UC) | Ikke oppgitt | COVID-19-virusinfeksjon (status: kansellert) |

---

## Cytotoksisitet

Ikke relevant: remdesivir er et antiviralt middel, ikke et antineoplastisk legemiddel.

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Interaksjonsoppslaget er fullført og viste 100 registrerte interaksjoner. Blant de oppførte er alle av moderat alvorlighetsgrad, blant annet med akarbose, doksycyklin, pioglitazon, amfotericin B, bupropion, mesalazin, klaritromycin, minocyklin, tetrasyklin, vankomycin, kanamycin, naltrekson, levofloksacin og neomycin.

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonene er kun støttet av modellscore. Den eneste studien er en farmakokinetikkstudie uten effektdata for HIV, og litteraturen dreier seg om COVID-19. Remdesivir har dessuten kun en kansellert godkjenning i Norge.

**For å gå videre kreves følgende:**
- Preparatomtale med advarsler og kontraindikasjoner (kritisk datamangel som blokkerer sikkerhetsscreening)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prekliniske data (in vitro-aktivitet mot HIV) før noen klinisk vurdering
- Avklaring av doseringsform og administrasjonsvei (remdesivir gis intravenøst)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

