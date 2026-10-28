---
layout: default
title: Levodopa
parent: Kun modellprediksjon (L5)
nav_order: 243
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Levodopa: predikert ny indikasjon Rasmussens subakutte encefalitt (evidensnivå L5). Opprinnelig indikasjon: Parkinsons sykdom"
monitor_inn: "LEVODOPA"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **1** stk.
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

## Levodopa: Fra Parkinsons sykdom til Rasmussens subakutte encefalitt
{: .text-alpha }

## Oppsummering i én setning

Levodopa er en forløper for dopamin og brukes opprinnelig til behandling av Parkinsons sykdom. TxGNN-modellen forutsier at legemidlet kan ha effekt ved **Rasmussens subakutte encefalitt**, men det finnes foreløpig **ingen kliniske studier** og **ingen publikasjoner** i de samlede dataene som støtter denne retningen. Prediksjonen er kun modellbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Parkinsons sykdom |
| Predikert ny indikasjon | Rasmussens subakutte encefalitt |
| TxGNN-prediksjonsscore | 0,9906 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 4 av 4) |
| Antall godkjenninger | 4 (gyldige: 4) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme (MOA) er for tiden ikke tilgjengelige. Levodopa er kjent som en dopaminforløper, og effekten ved Parkinsons sykdom er godt dokumentert. Hvorvidt den kan overføres til Rasmussens encefalitt, er imidlertid uklart.

Rasmussens encefalitt er en sjelden, kronisk og vanligvis ensidig nevroinflammatorisk sykdom. Den er drevet av T-celle-mediert cytotoksisitet og er forbundet med vanskelig behandlbar fokal epilepsi og progressiv atrofi i en hjernehalvdel. En mulig kobling kan ligge i dopaminerg modulering av nevroinflammasjon eller motoriske symptomer, men dette er spekulativt og ikke støttet av noen studie eller publikasjon i dataene.

Levodopa er ikke kjent for å påvirke den underliggende immunpatologien eller anfallene. Dopaminerge midler kan dessuten i teorien senke anfallsterskelen hos enkelte pasienter. Dette må vurderes før en eventuell videre vurdering. Den høye modellscoren (0,9906) kommer fra TxGNN-modellen (deep learning) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens, og er ikke dokumentert klinisk nytte.

---

## Klinisk evidens

Foreløpig er det ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er det ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

Alle fire godkjenninger er registrert som opphevet. Dosageform er ikke oppgitt i dataene.

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004786 | Inbrija | Ikke oppgitt | Parkinsons sykdom |
| EMEA/H/C/002441 | Levodopa/Carbidopa/Entacapone Orion | Ikke oppgitt | Parkinsons sykdom |
| EMEA/H/C/000511 | Stalevo | Ikke oppgitt | Parkinsons sykdom |
| EMEA/H/C/002785 | Corbilta (tidligere Levodopa/Carbidopa/Entacapone Sandoz) | Ikke oppgitt | Parkinsons sykdom |

---

## Sikkerhetsvurderinger

Data om advarsler og kontraindikasjoner fra preparatomtalen er ikke tilgjengelige. Se preparatomtalen for fullstendig sikkerhetsinformasjon.

**Kontraindikasjoner fra kunnskapsgrafen (PrimeKG, ikke fra preparattekst):** Følgende sykdommer er knyttet til levodopa som kontraindikasjoner i kunnskapsgrafen:
- **Nevrologiske/psykiske:** multisystematrofi, legemiddelindusert dyskinesi, epilepsi, angstlidelse, nevrotisk lidelse, dystymi, psykotisk lidelse, schizofreniform lidelse, schizoaffektiv lidelse, psykisk lidelse
- **Kardiovaskulære:** ortostatisk hypotensjon, posturalt ortostatisk takykardisyndrom (POTS), hjerteinfarkt, koronar trombose, plutselig hjertestans, hjerteledningssykdom
- **Mage-tarm/lever/galle:** magesår, ulcussykdom, lever- og galleblæresykdom, diaré
- **Øye:** åpenvinklet og trangvinklet glaukom
- **Metabolske/andre:** nyresykdom, pyoureter, diabetes mellitus, diabetisk ketoacidose, melanom, hemoglobinopati

Spesielt relevant for den predikerte indikasjonen er **epilepsi**, siden Rasmussens encefalitt kjennetegnes av vanskelig behandlbar fokal epilepsi.

**Legemiddelinteraksjoner:** Totalt 100 interaksjoner er funnet (DDInter). Et utvalg:
- **Moderat:** epinefrin, efedrin, bupropion, metronidazol, pyridoksin, metoklopramid, jern, samt antikolinergika (atropin, hyoscyamin, metskopolamin, glykopyrronium, klidinium, dicyklomin, mepenzolat)
- **Mindre:** antacida (aluminiumhydroksid, kalsiumkarbonat, magaldrat, magnesiumkarbonat, -hydroksid og -oksid)

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen er kun modellbasert (L5) uten støtte fra kliniske studier eller litteratur. Mekanismen er spekulativ, og levodopa har potensielt uheldige egenskaper ved epilepsi, som er en sentral del av sykdomsbildet ved Rasmussens encefalitt. I tillegg er alle godkjenninger i Norge opphevet.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), for eksempel fra DrugBank
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner), som i dag er en blokkerende datamangel
- Litteratursøk og prekliniske data som kan belyse en mulig kobling mellom dopaminerg modulering og nevroinflammasjon ved Rasmussens encefalitt
- Vurdering av risiko for senket anfallsterskel hos pasienter med epilepsi
- Avklaring av tilgjengelige produkter og administrasjonsveier, siden ingen godkjenninger er aktive i Norge
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

