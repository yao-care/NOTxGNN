---
layout: default
title: Carfilzomib
parent: Kun modellprediksjon (L5)
nav_order: 76
evidence_level: L5
indication_count: 5
---

# Carfilzomib
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **5** stk.
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

# Carfilzomib: Fra multipelt myelom til melanom

## Sammendrag i én setning

Carfilzomib er en irreversibel 26S proteasominhibitor som brukes internasjonalt til behandling av tilbakevendende/refraktært multipelt myelom (ikke for tiden markedsført i Norge iht. denne bevisvurderingen).
TxGNN-modellen predikerer aktivitet mot **melanom**, støttet av **0 kliniske forsøk** og **5 prekliniske/in silico-publikasjoner** — det finnes ingen kliniske bevis ennå.
TxGNN gav også fire smalere melanom-subtypetermer høyere score (CMM7, pediatrisk leptomeningeal melanom, epiteloid uveal melanom, vulvært melanom), men disse har **ingen støttende bevis** og er merket «Avvent» — de noteres for transparens men brukes ikke som hovedindikasjon.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Multipelt myelom (tilbakevendende/refraktært) — basert på internasjonalt kjent legemiddelklasse; ikke dokumentert i norsk reguleringsdata (legemidlet ikke markedsført) |
| Predikert ny indikasjon | Melanom |
| TxGNN-prediksjonspoengsum | 99,03% (rangering 9297) |
| Bevisnivå | L4 (kun prekliniske/mekanistiske studier) |
| Status på norskmarkedet | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

**Andre TxGNN-rangerte melanom-relaterte termer (ingen støttende bevis, alle Avvent/L5):**

| Sykdom | TxGNN-poengsum | Merknad |
|--------|---|---------|
| CMM7 | 99,37% | Sykdomsdefinisjon uklar (mulig melanom molekylær subtype); ingen bevis |
| Pediatrisk leptomeningeal melanom | 99,30% | Ultrasjelden pediatrisk CNS-subtype; blod-hjerne-barriere-penetrasjon ukjent; ingen bevis |
| Epiteloid cella uveal melanom | 99,23% | Distinkt GNAQ/GNA11-drevet biologi fra kutant melanom; ingen bevis |
| Vulvært melanom | 99,19% | Sjelden mukosal subtype med distinkt molekylær profil; ingen bevis |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljert virkningsmekanisme-data er ikke tilgjengelig i denne bevisvurderingen (DG002). Basert på kjent farmakologi er carfilzomib en irreversibel 26S proteasominhibitor: den blokkerer proteasomal nedbrytning av ubiquitinerte proteiner, som forårsaker akkumulering av feilfoldet proteiner intracellulært, hemming av NF-κB-signalveien, ER-stress og etterfølgende apoptose. Det er etablert (internasjonalt) for multipelt myelom, en hematologisk malignom som er høyt avhengig av proteasomfunksjon for overlevelse.

Melanom er biologisk distinkt fra multipelt myelom (solid tumor kontra hematologisk), så den mekanistiske forbindelsen er avhengig av en felles sårbarhet for proteasomstress snarere enn vevsspesifikk overlapping. En enkelt in vitro-studie (B16-F1 musemelanomseller) viste apoptoseinisieringsinduksjon med carfilzomib kombinert med bortezomib, dokumentert ved caspase 3/8/9/12-aktivering. Gjenværende litteratur er enten indirekte (kinase-målvalg docking-skjerming, NF-κB/heparanasemekanismesstudier i myelommodeller, PROTAC-degrader-studier) snarere enn melanomspesifikk effektivitetsdata.

Overordnet er den biologiske begrunnelsen plausibel men tynn: den hviler på én preklinisk cellinje-studie, uten in vivo-, kliniske eller humane translasjonsdata. De fire høyere rangerte subtypeprediksjoner (CMM7, pediatrisk leptomeningeal, uveal, vulvært melanom) har for tiden ingen litteratur- eller forsøksstøtte i det hele tatt og bør behandles som algoritmiske signaler kun.

---

## Bevis fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert (på tvers av alle fem predikerte melanom-relaterte indikasjoner).

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Preklinisk (in vitro) | Biology | Carfilzomib + bortezomib induserte apoptose i B16-F1 melanomseller via caspase 3/8/9/12-aktivering |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | In silico (docking/simulering) | J Biomol Struct Dyn | Molekylær docking/dynamikk-skjerming på tvers av 10 krefttyper (inkl. melanom) mot 18 kinase-mål for legemiddelombruk |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preklinisk (mekanisme) | Matrix Biology | Bortezomib/carfilzomib aktiverer NF-κB og oppregulerer heparanase, assosiert med aggressiv tumorfenottype (myelommodell) |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preklinisk (genregulering) | Mol Cancer Res | AIRAP/ZFAND2A-gen regulerer melanom-celloverlevelse via E3-ligase cIAP2; proteasom-stressveien relevans |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Preklinisk (PROTAC/BET-degrader) | Leukemia | BET-nedbrytende PROTAC-er aktive i myelom prekliniske modeller; proteasom-avhengig mekanisme-kontekst |

Ingen RCT-er, oversiktsartikler eller kasuistikker er tilgjengelige; alt bevis er preklinisk eller in silico.

---

## Informasjon om norskmarkedet

Carfilzomib er ikke markedsført i Norge (0 godkjenninger på fil). Ingen lisensdokumentasjon eller godkjent indiksjonstekst er tilgjengelig i denne bevisvurderingen.

---

## Cytotoksisitet

Carfilzomib er et antineoplastisk middel (proteasominhibitor-klasse), så denne seksjonen gjelder.

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Målrettet terapi (proteasominhibitor) |
| Risiko for benmargsupptrykking | Vennligst se forsikringsinseratet advarsler og forholdsregler |
| Emetogenisitetsklassifisering | Vennligst se forsikringsinseratet advarsler og forholdsregler |
| Overvåkingselementer | Vennligst se forsikringsinseratet advarsler og forholdsregler |
| Håndteringsbeskyttelse | Standard antineoplastisk legemiddelhåndteringsforsiktigheter gjelder iht. institusjonell protokoll; formell TFDA/etikett-veiledning ikke ennå tilgjengelig (se DG001) |

---

## Sikkerhetshensyn

Vennligst se forsikringsinseratet for sikkerhetsinformasjon. Ingen viktige advarsler, kontraindikasjoner eller DDI-data er for tiden tilgjengelige i denne bevisvurderingen (DG001, blokkerende alvorlighetsgrad).

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
Bevis for melanom er begrenset til én in vitro cellinje-studie uten in vivo-, kliniske eller humane data (L4/S1), og de fire høyere rangerte melanom-subtypesignalene har ingen støttende bevis i det hele tatt. Kombinert med fraværet av norsk markedsgodkjenning og en blokkerende datakløft på TFDA-etikett sikkerhetsinformasjon, kan kandidaten ikke gå videre forbi første screening.

**For å komme videre er følgende nødvendig:**
- TFDA-etikett/forsikringsinseratt-data (advarsler, kontraindikasjoner) — nødvendig for å rydde blokkeringskløften før noen S1 sikkerhetsvurdering (DG001)
- Bekreftet original virkningsmekanisme og indikasjonsdokumentasjon fra DrugBank eller tilsvarende kilde (DG002)
- In vivo prekliniske eller tidlige kliniske bevis som spesielt støtter melanom før avansering utover S1
- Klargjøring av sykdomstermdefinisjoner for CMM7 og de andre subtypeprediksjoner, da disse ser ut til å være datakvalitetsartefakter snarere enn handlingskraftige signaler

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

