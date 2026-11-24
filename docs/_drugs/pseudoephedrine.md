---
layout: default
title: Pseudoephedrine
parent: Kun modellprediksjon (L5)
nav_order: 342
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Pseudoephedrine: predikert ny indikasjon Sykdom i nesehulen (nasal cavity disease) (evidensnivå L5). Opprinnelig indikasjon: Rhinitis, allergic, seasonal (sesongbetinnet allergisk rhinitt)"
monitor_inn: "pseudoephedrine"
predicted_indications: ["nasal cavity disease", "allergic urticaria"]
---

# Pseudoephedrine
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

## Pseudoefedrin: Fra sesongbetinnet allergisk rhinitt til sykdom i nesehulen
{: .text-alpha }

## Sammendrag i én setning

Pseudoefedrin er et sympatomimetikum som opprinnelig ble godkjent for behandling av sesongbetinnet allergisk rhinitt (i kombinasjonsproduktet Aerinaze).
TxGNN-modellen predikerer at det kan være effektivt ved **sykdom i nesehulen** (nasal cavity disease).
Støtten er imidlertid svak: **ingen registrerte kliniske studier** og **7 publikasjoner**, hovedsakelig prekliniske dyremodeller og oversikter.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Rhinitis, allergic, seasonal (sesongbetinnet allergisk rhinitt) |
| Predikert ny indikasjon | Sykdom i nesehulen (nasal cavity disease) |
| TxGNN-prediksjonsscore | 0,9975 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Data om virkningsmekanisme er ikke tilgjengelig i de innsamlede dataene. Basert på kjent farmakologi er pseudoefedrin et sympatomimetikum som virker på alfa-adrenerge reseptorer, delvis direkte og delvis indirekte via frigjøring av noradrenalin. Dette gir vasokonstriksjon i nesens slimhinne og dermed avsvelling.

Sesongbetinnet allergisk rhinitt og sykdommer i nesehulen har felles hovedsymptom: tett nese. Mekanismen er derfor direkte relevant, for eksempel ved ikke-allergisk rhinitt. Den svært høye TxGNN-scoren (0,9975) henger sannsynligvis sammen med at den predikerte indikasjonen ligger tett opptil den eksisterende bruken. Den representerer dermed i hovedsak et nærliggende bruksområde og ikke et reelt nytt repurposing-signal.

To andre prediksjoner er vurdert, men har svakere støtte. **Allergisk urticaria** (score 0,9914) har ingen direkte evidens (L5). Pseudoefedrin er ikke en H1-antihistamin, og litteraturen gjelder antihistaminer som i praksis er funnet via kombinasjonsprodukter ved allergisk rhinitt. Den er anbefalt som «Hold».

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Klinisk farmakologistudie | Am J Rhinol | Sammenligning av oral og topisk dekongestiv effekt av fenylpropanolamin og d-pseudoefedrin målt med akustisk rinometri (beslektet virkestoff) |
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Oversikt | Allergy Asthma Proc | Kapittel om ikke-allergisk rhinitt: inflammatoriske og ikke-inflammatoriske årsaker til tett nese og rennende nese |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Dyremodell | J Pharmacol Exp Ther | Selektive α2c-adrenerge agonister i dyremodeller for nesetetthet |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Dyremodell (katt) | Am J Rhinol Allergy | Loratadin og montelukast i kombinasjon gir avsvelling; d-pseudoefedrin undersøkt med og uten desloratadin |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Dyremodell (hund) | Am J Rhinol | Modell for allergisk nesetetthet hos hunder sensibilisert for ragweed |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Dyremodell (hund) | J Pharmacol Toxicol Methods | Farmakologisk karakterisering av en kronisk, ikke-invasiv hundemodell for nesetetthet |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Dyremodell (metodikk) | Am J Rhinol | Akustisk rinometri hos hund som stordyrmodell for nesetetthet |

---

## Informasjon om det norske markedet

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/000772 | Aerinaze | desloratadine; pseudophedrine sulfate | Rhinitis, Allergic, Seasonal | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: 150 interaksjoner er registrert. Blant de første 20 er de fleste av moderat alvorlighetsgrad, og de gjelder særlig antidiabetika, blant annet:
  - sulfonylurea-preparater (acetoheksamid, klorpropamid, glimepirid, glipizid, glyburid)
  - SGLT2-hemmere (kanagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - GLP-1-agonister og relaterte (albiglutid, dulaglutid, eksenatid)
  - DPP-4-hemmeren alogliptin og akarbose
  - ulike insuliner
  - dietylpropion (moderat)
  - askorbinsyre (mindre alvorlig)
- **Sykdommer med kontraindikasjon i kunnskapsgrafen** (fra TxGNN-kunnskapsgrafen, ikke fra preparatomtale): blant annet hypertensjon, hjertesvikt, koronarsykdom, hjerneslag og cerebrovaskulær sykdom, diabetes og diabetisk ketoacidose, hypotyreose, godartet prostataforstørrelse, epilepsi, KOLS, lever-, nyre- og galleblæresykdom, magesår, pankreatitt, inflammatorisk tarmsykdom, blodkoagulasjonssykdom, rabdomyolyse og rusmiddelmisbruk/avhengighet.

For øvrig sikkerhetsinformasjon, inkludert varsler og kontraindikasjoner, vises det til preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den høye TxGNN-scoren gjenspeiler i hovedsak nærhet til den eksisterende indikasjonen. Evidensen for sykdom i nesehulen er preklinisk (L4), uten kliniske studier. Signalet kan derfor ikke regnes som en reell ny repurposing-mulighet foreløpig, og det egner seg best som et forskningsspørsmål.

<!-- review:begin no-lic-20261124b-pseudoephedrine-1 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Evidensen for sykdom i nesehulen er preklinisk (L4), uten kliniske studier, og den eneste godkjenningen i Norge er kansellert.» Rettet: opplysningen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); resten av setningen er uendret. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-pseudoephedrine-1 -->

**For å gå videre trengs følgende:**
- Detaljerte data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner fra DMP (nødvendig for sikkerhetsscreening)
- Avklaring av den regulatoriske statusen
- Kontrollerte kliniske studier av pseudoefedrin ved konkrete tilstander i nesehulen, f.eks. ikke-allergisk rhinitt
- Sikkerhetsplan for pasienter med hypertensjon, hjerte- og karsykdom og diabetes, samt vurdering av interaksjoner (bl.a. MAO-hemmere)

<!-- review:begin no-lic-20261124b-pseudoephedrine-2 -->

> **Kontrollrettelse (2026-11-24)**: Opprinnelig sto det: «Avklaring av den regulatoriske statusen og årsaken til kanselleringen» Rettet: begrunnelsen om at godkjenningen(e) er kansellert, er tatt ut fordi den ikke stemte med EMAs data om sentrale EU-godkjenninger (2026-11-12), der godkjenningene står som gyldige (Authorised); selve oppfølgingspunktet er beholdt. Oppdaterte antall og statuser for godkjenningene står i hurtigoversikten og i lisenstabellen under markedsinformasjonen. Kilde: [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/).

<!-- review:end no-lic-20261124b-pseudoephedrine-2 -->

<!-- review:begin log -->

## Kontrollogg

Nedenfor er kontrolloggen for denne siden: opplysninger kontrollert mot EMAs data om sentrale EU-godkjenninger. Rettelser gjelder bare grunnleggende faktaopplysninger; modellens prediksjoner, evidensnivåer og konklusjoner er ikke skrevet om.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-24 | Rettet: «Evidensen for sykdom i nesehulen er preklinisk (L4), uten kliniske studier, og den eneste godkjenningen i Norge er kansellert.» → «Evidensen for sykdom i nesehulen er preklinisk (L4), uten kliniske studier.» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |
| 2026-11-24 | Rettet: «Avklaring av den regulatoriske statusen og årsaken til kanselleringen» → «Avklaring av den regulatoriske statusen» | Rettet | [EMA – Medicines output: medicines report](https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx); [European Medicines Agency](https://www.ema.europa.eu/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

