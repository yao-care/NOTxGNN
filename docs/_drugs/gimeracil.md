---
layout: default
title: Gimeracil
parent: Kun modellprediksjon (L5)
nav_order: 188
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Gimeracil: predikert ny indikasjon Kolonneoplasme (colonic neoplasm) (evidensnivå L5). Opprinnelig indikasjon: Magekreft (Stomach Neoplasms)"
monitor_inn: "GIMERACIL"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "lipoma of colon", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "colonic lymphangioma", "colon leiomyoma"]
---

# Gimeracil
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

## Gimeracil: Fra magekreft til kolonneoplasme
{: .text-alpha }

## Sammendrag i én setning

Gimeracil er DPD-hemmeren i kombinasjonspreparatet S-1 (tegafur/gimeracil/oteracil), opprinnelig brukt til behandling av magekreft.
TxGNN-modellen predikerer at det kan være effektivt ved **kolonneoplasme (tykktarmskreft)**,
og denne retningen støttes foreløpig av **6 kliniske studier** og **12 publikasjoner** i de samlede dataene. Evidensen gjelder S-1 som fast kombinasjon, ikke gimeracil som enkeltstoff.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Magekreft (Stomach Neoplasms) |
| Predikert ny indikasjon | Kolonneoplasme (colonic neoplasm) |
| TxGNN prediksjonsscore | 99,88 % |
| Evidensnivå | L1 (basert på de innsamlede dataene; se merknad under) |
| Markedsstatus i Norge | Kun opphevede godkjenninger |
| Antall godkjenninger | 1 (opphevet) |
| Anbefalt beslutning | Proceed with Guardrails (fortsett med sikkerhetstiltak) |

*Merknad om evidensnivå:* L1 forutsetter minst to fullførte fase 3-RCT-er. Dataene inneholder kun én fullført fase 3-studie (NCT00660894), mens den andre fase 3-studien (NCT03448549) har ukjent status. Nivået L1 er derfor optimistisk, og L2 er et mer forsiktig anslag.

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte mekanismedata (MOA) er for tiden ikke tilgjengelige i datagrunnlaget. Ut fra kjent informasjon er gimeracil en hemmer av enzymet dihydropyrimidindehydrogenase (DPD). Ved å hemme DPD bremser det nedbrytningen av 5-FU og opprettholder dermed systemisk 5-FU-eksponering fra tegafur i S-1.

Magekreft og tykktarmskreft er begge gastrointestinale svulster som er følsomme for fluoropyrimidiner. Den mekanistiske koblingen er derfor sammenhengende: forlenget 5-FU-eksponering som gir effekt ved magekreft, kan også gi effekt ved kolorektal kreft. Dette understøttes av kliniske studier der S-1 er brukt i kolorektal kreft.

Det er viktig å merke seg at gimeracil ikke har egen antitumoreffekt. Alle kliniske data gjelder S-1-kombinasjonen, så prediksjonen må tolkes som en støtte for S-1 og ikke for gimeracil alene.

---

## Klinisk studieevidens

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Fullført | 1535 | Randomisert sammenligning av UFT+leukovorin mot TS-1 (S-1) som adjuvant behandling ved stadium III tykktarmskreft |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Ukjent | 1191 | SOX (oksaliplatin + S-1) mot XELOX som adjuvant behandling ved stadium III kolorektal kreft |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Ukjent | 40 | S-1 + bevacizumab ved inoperabel eller residiverende kolorektal kreft etter tidligere behandlingssvikt |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Fase 2 | Ukjent | 82 | Raltitreksed + S-1 ved metastatisk kolorektal kreft etter svikt på standardbehandling; primært endepunkt er progresjonsfri overlevelse |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Fase 2 | Ikke rekrutterende ennå | 52 | Enarmet studie av fruquintinib + tegafur/gimeracil/oteracil som tredjelinjebehandling ved avansert metastatisk kolorektal kreft |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Fase 2 | Avsluttet (terminated) | 20 | Effekt av S-1 og kapecitabin med oksaliplatin på koronar blodstrøm (sikkerhets-/fysiologiendepunkt, ikke effekt) |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Risikofaktoranalyse (87 pasienter) | Gan to Kagaku Ryoho | Risikofaktorer for alvorlig hematologisk toksisitet (grad 3–4, 16,1 %) ved S-1 + irinotekan ved avansert eller residiverende tykktarmskreft |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Farmakokinetisk studie (mus) | Gan to Kagaku Ryoho | Nytte av S-1 ved peritoneale metastaser fra tykktarmskreft i musemodell |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Prekliniske studier (xenograft) | Oncology Reports | Irinotekan overvinner 5-FU-resistens i tykktarmskreft-xenografter; kombinasjon med S-1 økte antitumoreffekten |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Kasuistikk og oversikt | J Oncol Pharm Pract | S-1 beskrives som et av de mest effektive midlene ved kolorektal kreft; hypertriglyseridemi observert etter S-1 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Kasuistikk | Eur J Dermatol | Erytroderm med utbredt slimhinnepåvirkning og hånd-fot-syndrom ved TS-1 |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Kasuistikk | Anticancer Research | Fullstendig respons med S-1 + CPT-11 ved levermetastaser fra tykktarmskreft |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Kasuistikk | Gan to Kagaku Ryoho | SOX + panitumumab som nedstadiering før totrinns hepatektomi ved irresektable levermetastaser |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Kasuistikk | Gan to Kagaku Ryoho | Tverrkolonkreft med levermetastaser og portatrombe behandlet effektivt med kjemoterapi (CapeOX, deretter regimeskifte) |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Kasuistikk | Gan to Kagaku Ryoho | Urinretensjon ved oksaliplatinindusert akutt perifer nevropati; tegafur/gimeracil/oteracil brukt tidligere i forløpet |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Kasuistikk | Gan to Kagaku Ryoho | Gjentatt reseksjon av peritoneale residiver etter kolorektal kreft |

Litteraturen består i hovedsak av kasuistikker og prekliniske data. Det finnes ingen randomiserte publikasjoner i det innsamlede materialet.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/001242 | Teysuno | Ikke oppgitt | Magekreft (Stomach Neoplasms) – status: opphevet |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Konvensjonelt cytotoksisk (fluoropyrimidinklassen, som del av S-1; gimeracil selv er en DPD-hemmer) |
| Risiko for myelosuppresjon | Middels (hematologisk toksisitet grad 3–4 på 16,1 % ved S-1 + irinotekan i en japansk kohorte) |
| Emetogenisitet | Lav til middels |
| Overvåkingspunkter | Blodstatus med differensialtelling, lever- og nyrefunksjon, elektrolytter |
| Håndteringsbeskyttelse | Følg gjeldende regler for håndtering av cytotoksiske legemidler |

Se pakningsvedlegget for fullstendige advarsler og forholdsregler.

---

## Sikkerhetsvurderinger

- **Bivirkninger rapportert i litteraturen (S-1):** hånd-fot-syndrom og erytroderm, hypertriglyseridemi, hematologisk toksisitet ved kombinasjon med irinotekan.
- **Legemiddelinteraksjoner:** Ingen interaksjoner ble funnet i den gjennomførte søkingen.

Se pakningsvedlegget for øvrig sikkerhetsinformasjon.

---

## Konklusjon og neste steg

**Beslutning: Proceed with Guardrails (fortsett med sikkerhetstiltak)**

**Begrunnelse:**
En stor fullført fase 3-studie (n=1535) og flere fase 2-studier støtter bruk av S-1 ved tykktarmskreft, og mekanismen er sammenhengende. Gimeracil er imidlertid kun en del av en fast kombinasjon, evidensen er hovedsakelig fra kombinasjonsregimer, og flere studier har ukjent status. Preparatets eneste norske godkjenning er opphevet.

**For å gå videre kreves følgende:**
- Detaljerte mekanismedata (MOA) fra DrugBank
- Advarsler og kontraindikasjoner fra pakningsvedlegget (mangler i datagrunnlaget)
- Bekreftelse av resultater og status for NCT03448549 og de øvrige studiene med ukjent status
- Avklaring av regulatorisk vei, siden eneste norske godkjenning er opphevet
- Overvåkingsplan for DPD-mangel og hematologisk toksisitet
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

