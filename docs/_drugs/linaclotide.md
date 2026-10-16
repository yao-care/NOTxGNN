---
layout: default
title: Linaclotide
parent: Kun modellprediksjon (L5)
nav_order: 246
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Linaclotide: predikert ny indikasjon Cauda equina-syndrom (evidensnivå L5). Opprinnelig indikasjon: Irritabelt tarmsyndrom"
monitor_inn: "LINACLOTIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)"]
---

# Linaclotide
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **3** stk.
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

# Linaclotide: Fra irritabelt tarmsyndrom til cauda equina-syndrom

## Oppsummering

Linaclotide er et legemiddel som opprinnelig ble godkjent for behandling av **irritabelt tarmsyndrom (IBS)**.
TxGNN-modellen predikerer at det kan ha effekt ved **cauda equina-syndrom**, men prediksjonen støttes foreløpig kun av modellscore: **ingen kliniske studier** og **ingen publikasjoner** er registrert.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Irritabelt tarmsyndrom |
| Predikert ny indikasjon | Cauda equina-syndrom |
| TxGNN-prediksjonsscore | 99,96 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrert (trukket tilbake) |
| Antall godkjenninger | 1 |
| Anbefalt beslutning | Hold |

---

## Hvorfor kan denne prediksjonen være rimelig?

Det foreligger for øyeblikket ingen detaljerte data om virkningsmekanisme i de innsamlede dataene. Linaclotide er kjent som en guanylatsyklase-C-agonist som virker lokalt i tarmen og har minimal systemisk absorpsjon. Effekten ved IBS med forstoppelse er godt kjent.

Koblingen til cauda equina-syndrom er svak. Det eneste støttepunktet er den høye modellscoren (0,9996). En mulig, men spekulativ forklaring er indirekte lindring av nevrogen tarmdysfunksjon (forstoppelse) som kan forekomme ved syndromet. Dette ville ikke behandle den underliggende nervekompresjonen, og er en slutning, ikke dokumentert evidens.

For fullstendighet predikerer modellen også andre indikasjoner, alle med evidensnivå L5 og beslutning Hold:

| Rang | Predikert indikasjon | TxGNN-score | Merknad |
|------|------|------|------|
| 2 | Nevrogen blære (term merket som foreldet i ontologien) | 99,89 % | Begrepet bør kartlegges på nytt før videre vurdering. Tarmrestriktiv virkning gjør effekt på blærefunksjon lite sannsynlig. |
| 3 | Søvnløshet | 99,51 % | Systemisk eksponering er minimal, så en direkte effekt på sentralnervesystemet er lite plausibel. En eventuell bedring ville være indirekte via lindring av tarmsymptomer. |

---

## Klinisk studiedokumentasjon

Foreløpig er ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig er ingen relatert litteratur tilgjengelig.

---

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002490 | Constella | – | Irritabelt tarmsyndrom |

Denne godkjenningen (innehaver: AbbVie Deutschland GmbH & Co. KG) er avregistrert. Det finnes ingen gyldige godkjenninger.

---

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner:** Det er registrert 56 interaksjoner. Blant de 20 som er vist i de innsamlede dataene er de fleste av mindre alvorlighetsgrad (Minor). Interaksjoner med moderat alvorlighetsgrad:

- Levonorgestrel
- Etinyløstradiol
- Noretisteron
- Levotyroksin
- Tyreoideaekstrakt (svin)

Blant de mindre alvorlige finnes blant annet protonpumpehemmere (rabeprazol, esomeprazol, deksansoprazol), NSAIDs (ibuprofen, ketorolak, diklofenak, oksaprozin, bromfenak) og andre avføringsmidler (bisakodyl, dokusat, natriumpikosulfat, ricinusolje, polyetylenglykol).

For øvrig sikkerhetsinformasjon (advarsler og kontraindikasjoner), se preparatomtalen.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen støttes kun av en høy modellscore. Det finnes ingen kliniske studier eller litteratur, ingen dokumentert mekanisme, og linaclotides tarmrestriktive virkning gjør en direkte effekt på cauda equina-syndrom lite plausibel. Den eneste godkjenningen i Norge er avregistrert.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Preparatomtale med advarsler og kontraindikasjoner (blokkerende datamangel for sikkerhetsscreening)
- Systematisk litteratur- og studiesøk for cauda equina-syndrom, inkludert nevrogen tarmdysfunksjon
- Ny kartlegging av den foreldede sykdomstermen «nevrogen blære» før eventuell videre vurdering
- Avklaring av administrasjonsvei og formuleringskompatibilitet
- Avklaring av dagens regulatoriske status i Norge, siden preparatet er avregistrert
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

