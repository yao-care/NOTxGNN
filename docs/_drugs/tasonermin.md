---
layout: default
title: Tasonermin
parent: Kun modellprediksjon (L5)
nav_order: 400
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Tasonermin: predikert ny indikasjon Prostatisk uretral urotelkarsinom (evidensnivå L5). Opprinnelig indikasjon: Sarkom"
monitor_inn: "TASONERMIN"
predicted_indications: ["prostatic urethra urothelial carcinoma", "kidney pelvis sarcomatoid transitional cell carcinoma", "infiltrating bladder urothelial carcinoma sarcomatoid variant", "renal pelvis papillary urothelial carcinoma", "HER2 positive breast carcinoma", "uterine ligament adenocarcinoma", "endocervical carcinoma", "uterine ligament serous adenocarcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament clear cell adenocarcinoma"]
---

# Tasonermin
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

## Tasonermin: Fra sarkom til prostatisk uretral urotelkarsinom
{: .text-alpha }

## Oppsummering i én setning

Tasonermin er rekombinant humant TNF-alfa, opprinnelig godkjent for behandling av **sarkom** (bløtdelssarkom i ekstremiteter, gitt ved isolert lemperfusjon).
TxGNN-modellen forutsier at legemidlet kan ha effekt ved **prostatisk uretral urotelkarsinom**, men
det finnes for øyeblikket **ingen kliniske studier** og **ingen publikasjoner** som støtter denne retningen. Prediksjonen er rent beregningsbasert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Sarkom |
| Predikert ny indikasjon | Prostatisk uretral urotelkarsinom |
| TxGNN-prediksjonsscore | 0,9981 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen (ikke) rimelig?

Detaljerte data om virkningsmekanisme er foreløpig ikke tilgjengelige. Tasonermin er kjent som rekombinant humant TNF-alfa, brukt sammen med isolert lemperfusjon ved bløtdelssarkom. Virkningen i denne bruken antas å skyldes vaskulær skade i svulsten, men dette er ikke dokumentert i dataene som er samlet for denne rapporten.

Det er ikke mulig å etablere en mekanistisk kobling mellom sarkom og urotelkarsinom i prostatisk uretra ut fra de foreliggende dataene. Den høye scoren (0,998) er en prediksjon fra TxGNN-modellen (dyp læring) alene. Systemisk TNF-alfa-toksisitet begrenser dessuten bruk utenfor regional administrering, og isolert lemperfusjon lar seg ikke overføre til svulster i urinveiene.

Flere av de øvrige topp-10-prediksjonene har et visst, men løst, slektskap med den opprinnelige indikasjonen:
- **Sarkomatoid nyrebekken-overgangscellekarsinom** og **infiltrerende blæreurotelkarsinom, sarkomatoid variant**: den sarkomatoide histologien har mesenkymale trekk som ligner sarkom, noe som kan forklare modellens prediksjon. Direkte evidens mangler.
- **HER2-positivt brystkarsinom**: TNF-alfa-signalering er kontekstavhengig og kan fremme svulstvekst, så rasjonalet er usikkert. Eksisterende HER2-målrettet behandling er svært effektiv.
- **Gynekologiske karsinomer** (livmorligament, livmorhals): scorene kommer fra TxGNN-modellen (dyp læring) og kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens.

---

## Klinisk studieevidens

Det er for øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Det er for øyeblikket ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/000206 | Beromun | – | Sarkom |

Godkjenningen er avregistrert (innehaver: Belpharma s.a.).

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Cytotoksisitetsklassifisering | Biologisk kreftlegemiddel (rekombinant TNF-alfa, immunmodulerende/vaskulært virkende). Detaljert klassifisering er ikke tilgjengelig i dataene |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisk klassifisering | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingspunkter | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Håndteringsbeskyttelse | Følg lokale retningslinjer for håndtering av cytostatika/kreftlegemidler inntil annet er avklart |

---

## Sikkerhetsvurderinger

Se pakningsvedlegget for sikkerhetsinformasjon. Det er ikke funnet registrerte legemiddelinteraksjoner i dataene som er samlet for denne rapporten. Det bør likevel bemerkes at systemisk TNF-alfa-toksisitet er en kjent begrensning ved bruk utover regional administrering.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen bygger kun på en score fra TxGNN-modellen (dyp læring) (evidensnivå L5), uten kliniske studier, litteratur eller en identifiserbar mekanistisk kobling. Scoren kan gjenspeile likheter modellen har lært mellom beslektede sykdommer, ikke biologisk evidens. Legemidlet er markedsført i Norge (1 av 1 lisens er gyldig), men systemisk toksisitet begrenser anvendelsen. Det samme gjelder alle de ti predikerte indikasjonene.

**For å gå videre kreves følgende:**
- Innhenting og analyse av pakningsvedlegget med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Prekliniske data eller litteratur som viser en rimelig mekanisme i urotelkarsinom
- Vurdering av administrasjonsvei (regional/lokal levering) og dens gjennomførbarhet for den predikerte indikasjonen
- Avklaring av tilgjengelighet i Norge, siden eneste godkjenning er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

