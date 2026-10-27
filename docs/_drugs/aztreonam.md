---
layout: default
title: Aztreonam
parent: Kun modellprediksjon (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Aztreonam: predikert ny indikasjon Hyperamylasemi (TxGNN-rangering 1) (evidensnivå L5). Opprinnelig indikasjon: Gramnegative bakterieinfeksjoner"
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "gonococcal urethritis", "Ureaplasma urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
---

# Aztreonam
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Aztreonam: Fra gramnegative infeksjoner til gonokokkuretritt
{: .text-alpha }

## Oppsummering i en setning

Aztreonam er et monobaktam-antibiotikum som opprinnelig brukes mot gramnegative bakterieinfeksjoner, urinveisinfeksjoner, helsetjenesteassosiert lungebetennelse og bløtdelsinfeksjoner.
TxGNN-modellen forutsier at det kan være effektivt mot **gonokokkuretritt** (den høyest rangerte indikasjonen med litteraturstøtte), med **0 kliniske studier** og **6 publikasjoner** i de samlede dataene.
Merk at modellens høyest rangerte prediksjon (hyperamylasemi) mangler både mekanistisk grunnlag og evidens, og at flere av de 10 øverste prediksjonene sannsynligvis er artefakter fra kunnskapsgrafen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Gramnegative bakterieinfeksjoner; urinveisinfeksjoner; helsetjenesteassosiert lungebetennelse; bløtdelsinfeksjoner |
| Predikert ny indikasjon (høyest rangert) | Hyperamylasemi (TxGNN-rangering 1) |
| Klinisk mest relevante prediksjon | Gonokokkuretritt (rangering 4) |
| TxGNN-prediksjonsscore | 99,73 % (hyperamylasemi); 99,59 % (gonokokkuretritt) |
| Evidensnivå | L5 (hyperamylasemi); L3 (gonokokkuretritt) |
| Markedsstatus i Norge | Kun avregistrert |
| Antall markedsføringstillatelser | 1 (avregistrert) |
| Anbefalt beslutning | Hold (samlet); gonokokkuretritt kan vurderes som forskningsspørsmål |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige i de samlede dataene. Basert på kjent informasjon er aztreonam et monobaktam-antibiotikum som hemmer bakteriell celleveggsyntese via penicillinbindende protein 3 (PBP3) hos gramnegative aerobe bakterier, og effekten er etablert ved gramnegative infeksjoner.

**Høyest rangerte prediksjoner:** Hyperamylasemi, polyklonalt hyperviskositetssyndrom, medfødt analbuminemi, blodgruppeinkompatibilitet og premaligne hematologiske sykdommer har ingen plausibel mekanistisk kobling til et antibakterielt middel. Dette er laboratoriefunn eller ikke-infeksiøse tilstander, og de høye scorene ser ut til å være grafbaserte artefakter. For blodgruppeinkompatibilitet gjelder den eneste funnede artikkelen resistensgener hos *Klebsiella pneumoniae* og er et rent nøkkelordtreff.

**Ureaplasma-uretritt:** Prediksjonen er mekanistisk motsagt. Ureaplasma mangler cellevegg, og betalaktamer som aztreonam er derfor iboende uvirksomme.

**Plausible prediksjoner:**
- **Gonokokkuretritt:** Aztreonam har aktivitet mot *Neisseria gonorrhoeae*, og flere kliniske studier fra 1983–1986 samt en åpen enarmet studie fra 2020 (2 g) rapporterer effekt av enkeltdose, også mot penicillinresistente stammer. Evidensen er imidlertid ikke-randomisert og i hovedsak historisk, resistensutvikling er beskrevet, og gjeldende retningslinjer bygger på andre midler. Dette er mer en utvidelse av den eksisterende gramnegative indikasjonen enn ekte repurposing.
- **Epiglottitt:** Ofte forårsaket av *Haemophilus influenzae* type b (gramnegativ). Støtten er indirekte, og tredjegenerasjons cefalosporiner er foretrukket.
- **Xantogranulomatøs pyelonefritt:** Teoretisk antibakteriell aktivitet, men definitiv behandling er vanligvis kirurgisk, og direkte evidens mangler.
- **Monoklonal gammopati:** Aztreonam behandler ikke selve sykdommen. Litteraturen gjelder infeksjoner hos pasienter med hematologiske sykdommer.

---

## Klinisk studieevidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Tabellen gjelder gonokokkuretritt (rangering 4), som har mest relevant litteratur.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Åpen enarmet klinisk studie | Antimicrob Agents Chemother | Enkeltdose aztreonam 2 g intramuskulært hos menn med gonoré, undersøkt som mulig nytt regime på grunn av trusselen fra ceftriaxonresistent *N. gonorrhoeae* |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Klinisk studie | Genitourin Med | Enkeltdose 1 g i.m. kurerte infeksjonen hos 61 menn og 26 kvinner på alle steder unntatt svelget hos én pasient; godt tolerert |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Klinisk effektstudie | Antimicrob Agents Chemother | Aztreonam 1 g i.m. sammenlignet med spektinomycin 2 g ved ukomplisert gonoré; ingen behandlingssvikt i noen av armene |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiologisk og terapeutisk studie | Hinyokika Kiyo | Enkeltdosebehandling av gonoréinfeksjoner med aztreonam, kombinert med epidemiologisk kartlegging |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | In vitro/klinisk effektstudie | J Infect Dis | Aztreonam mot penicillinresistente gonokokker (PPNG) |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Resistens/mikrobiologi | J Infect Chemother | Beskriver fremvekst av cefem- og aztreonam-høyresistent *N. gonorrhoeae* uten betalaktamaseproduksjon |
| [3766490](https://pubmed.ncbi.nlm.nih.gov/3766490/) | 1986 | Åpen studie/serie (epiglottitt) | Am J Dis Child | 59 barn med alvorlige gramnegative infeksjoner, inkludert én med epiglottitt; indirekte støtte |
| [4079014](https://pubmed.ncbi.nlm.nih.gov/4079014/) | 1985 | Klinisk studie (monoklonal gammopati) | Jpn J Antibiot | Behandling av alvorlige infeksjoner ved hematologiske sykdommer; samlet effektrate 51,1 % (indirekte) |

---

## Markedsinformasjon for Norge

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/006113 | Emblaveo | Ikke oppgitt | Gramnegative bakterieinfeksjoner; urinveisinfeksjoner; helsetjenesteassosiert lungebetennelse; bløtdelsinfeksjoner (status: avregistrert) |

---

## Sikkerhetsvurderinger

**Kontraindikasjoner fra kunnskapsgrafen** (kunnskapsgrafen PrimeKG, ikke preparatomtale): nyresykdom, pyoureter, leversykdom, gallblæresykdom, *Clostridium difficile*-kolitt, perinatal nekrotiserende enterokolitt og bronkial sykdom.

**Legemiddelinteraksjoner:** 27 interaksjoner er identifisert totalt. Av de 20 som er oppført i dataene, er følgende klassifisert som **moderate**:
- Pikosulfat
- Dikumarol
- Warfarin

De øvrige er klassifisert som «ukjent» og omfatter blant annet pantoprazol, omeprazol, lansoprazol, morfin, vankomycin, hydrokortison, ondansetron, metronidazol, deksametason, amfotericin B, acetylsalisylsyre, heparin, salbutamol, flukonazol, takrolimus, amikacin og aciklovir.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
De høyest rangerte prediksjonene (hyperamylasemi, hyperviskositetssyndrom, analbuminemi) er rene modellprediksjoner uten mekanistisk eller klinisk støtte, og Ureaplasma-uretritt er mekanistisk motsagt. Gonokokkuretritt (L3) er biologisk plausibel og kan følges opp som et forskningsspørsmål, men evidensen er ikke-randomisert og historisk, resistens er beskrevet, og eneste norske tillatelse er avregistrert.

**For å gå videre kreves følgende:**
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner mangler og er en blokkerende datamangel)
- Detaljerte data om virkningsmekanisme
- For gonokokkuretritt: vurdering mot gjeldende behandlingsretningslinjer og lokale resistensdata, samt randomiserte sammenlignende studier
- Avklaring av regulatorisk status og tilgjengelige administrasjonsveier, siden tillatelsen er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

