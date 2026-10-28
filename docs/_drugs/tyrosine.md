---
layout: default
title: Tyrosine
parent: Kun modellprediksjon (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tyrosine: predikert ny indikasjon Cauda equina-syndrom (evidensnivå L5). Opprinnelig indikasjon: Lønnesirupsykdom (Maple Syrup Urine Disease)"
monitor_inn: "tyrosine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "angle-closure glaucoma", "hyperthyroidism", "postural orthostatic tachycardia syndrome", "hyperthyroxinemia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "traumatic glaucoma", "aqueous misdirection", "neovascular glaucoma"]
---

# Tyrosine
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

## Tyrosin: Fra lønnesirupsykdom til cauda equina-syndrom
{: .text-alpha }

## Oppsummering i én setning

Tyrosin (handelsnavn Maapliv) er registrert for behandling av lønnesirupsykdom (Maple Syrup Urine Disease).
TxGNN-modellen predikerer at det kan være virksomt ved **cauda equina-syndrom**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Lønnesirupsykdom (Maple Syrup Urine Disease) |
| Predikert ny indikasjon | Cauda equina-syndrom |
| TxGNN-prediksjonsscore | 0,9977 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Antall tillatelser | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Data om virkningsmekanisme (MOA) er ikke tilgjengelig i dataene som er samlet inn for denne rapporten. Tyrosin er en aminosyre og forløper for katekolaminer (dopamin, noradrenalin, adrenalin) og skjoldbruskkjertelhormoner.

Det er ikke funnet noen plausibel mekanistisk kobling mellom tyrosin og cauda equina-syndrom, som skyldes kompresjon eller strukturell skade på nerverøttene. Den høye scoren (0,9977) er en ren beregningsmessig prediksjon, og likhet med den opprinnelige indikasjonen (lønnesirupsykdom) er ikke vurdert.

Også de øvrige topp-10-prediksjonene mangler overbevisende støtte:

- **Hypertyreose og hyperthyroksinemi:** Tyrosin er et substrat for syntese av skjoldbruskkjertelhormon, så tilskudd kan teoretisk sett forverre i stedet for behandle tilstanden. Dette er et sikkerhetsmoment, ikke en terapeutisk begrunnelse.
- **Postural ortostatisk takykardi-syndrom (POTS):** Én kasuistikk beskriver effekt av alfa-metyl-p-tyrosin, en hemmer av tyrosinhydroksylase med motsatt virkning av tyrosin. Dette er i beste fall indirekte evidens.
- **Glaukomvarianter (trangvinklet, traumatisk, neovaskulært, vandig misdirection):** Litteraturen er generell og viser ingen terapeutisk relevans for tyrosin.
- **Resistens mot skjoldbruskkjertelhormon (reseptor beta-mutasjon):** Tilstanden skyldes reseptordefekt, ikke substratmangel.
- **Foreldet nevrogen blære:** Dette er en utdatert ontologioppføring og ikke en klinisk anvendbar indikasjon.

---

## Klinisk evidens

For den primære prediksjonen (cauda equina-syndrom) er det for tiden ingen relaterte kliniske studier registrert.

Blant de øvrige prediksjonene finnes kun én studie, for hypertyreose:

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Ikke relevant (NA) | Ikke ennå rekrutterende | 150 | Randomisert, dobbeltblindet, placebokontrollert studie av et tilskudd med sink, selen og L-tyrosin for å forebygge tyreotoksikose hos personer med SEPP1-polymorfisme. Sammensatt tilskudd, så tyrosins egen effekt kan ikke isoleres. Ingen resultater tilgjengelig. |

---

## Litteraturevidens

For cauda equina-syndrom finnes for tiden ingen relatert litteratur.

Utvalgte funn for andre prediksjoner (alle med lav relevans for tyrosinbehandling):

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Kohort | Frontiers in Medicine | Endringer i plasmaaminosyrer ved tidlig primær trangvinklet glaukom. Observasjonell sammenheng, ikke bevis for nytte av tyrosin. |
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Kasuistikk | Int J Mol Sci | Kronisk utmattelsessyndrom med respons på alfa-metyl-p-tyrosin (en tyrosinhydroksylasehemmer, motsatt virkning av tyrosin). |
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Oversikt | Lancet Diabetes Endocrinol | Generell oversikt over hypertyreose: årsaker, diagnostikk og behandling. |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Oversikt | Rom J Ophthalmol | Oversikt over neovaskulært glaukom. Ingen tyrosinrelevans. |
| [10579356](https://pubmed.ncbi.nlm.nih.gov/10579356/) | 1999 | Grunnforskning/genetikk | Endocrinology | Mutasjoner i skjoldbruskkjertelhormonreseptor beta ved resistens mot skjoldbruskkjertelhormon. |

---

## Informasjon om det norske markedet

| Tillatelsesnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/005557 | Maapliv | Ikke oppgitt | Lønnesirupsykdom (Maple Syrup Urine Disease) |

Tillatelsen er avregistrert. Innehaver: Recordati Rare Diseases.

---

## Sikkerhetsvurderinger

- **Skjoldbruskkjertelhormon:** Tyrosin er en forløper for skjoldbruskkjertelhormon. Bruk ved hypertyreose eller hyperthyroksinemi kan i teorien forverre tilstanden og bør vurderes nøye.
- **Legemiddelinteraksjoner:** Ingen interaksjoner funnet i dataene.

For øvrig sikkerhetsinformasjon, se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for cauda equina-syndrom bygger kun på en beregningsmodell (evidensnivå L5), uten kliniske studier, uten litteratur og uten plausibel mekanistisk kobling. Produktet er markedsført i Norge med 1 gyldig tillatelse av 1. De øvrige prediksjonene har enten ingen støtte eller gir sikkerhetsbekymringer (tyrosin som skjoldbruskkjertelhormon-forløper).

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra preparatomtalen
- Prekliniske data eller en mekanistisk hypotese som kobler tyrosin til cauda equina-syndrom
- Vurdering av om en annen prediksjon (f.eks. POTS) kan gi en mer realistisk kandidat, med oppdatert evidensgjennomgang
- Avklaring av regulatorisk status og administrasjonsvei (ikke vurdert ennå)
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

