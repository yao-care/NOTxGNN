---
layout: default
title: Imipenem
parent: Kun modellprediksjon (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Imipenem: predikert ny indikasjon Diffus sklerodermi (evidensnivå L5). Opprinnelig indikasjon: Gramnegative bakterieinfeksjoner"
---

# Imipenem
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

# Imipenem: Fra gramnegative bakterieinfeksjoner til diffus sklerodermi

## Oppsummering

Imipenem er et karbapenem-antibiotikum som opprinnelig brukes mot **gramnegative bakterieinfeksjoner**.
TxGNN-modellen forutsier at legemidlet kan være effektivt mot **diffus sklerodermi**, men det finnes **ingen kliniske studier og ingen publikasjoner** som støtter denne prediksjonen.
Blant de ti øverste prediksjonene har kun **Staphylococcus aureus-infeksjon** (2 kliniske fase 4-studier) et visst klinisk grunnlag. Flere bakterielle prediksjoner (tyfoidfeber, paratyfoidfeber, salmonellose, bihulebetennelse) er i praksis utvidelser av den opprinnelige indikasjonen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Gramnegative bakterieinfeksjoner |
| Predikert ny indikasjon (rangert som nr. 1) | Diffus sklerodermi |
| TxGNN-prediksjonsscore | 99,99 % |
| Evidensnivå | L5 (kun modellprediksjon) |
| Markedsstatus i Norge | Kun tilbakekalte/avregistrerte godkjenninger |
| Antall godkjenninger | 1 (0 gyldige, 1 kansellert) |
| Anbefalt beslutning | Hold |

**Oversikt over de ti øverste prediksjonene:**

| Rang | Sykdom | Score | Evidensnivå | Anbefaling |
|---|---|---|---|---|
| 1 | Diffus sklerodermi | 99,99 % | L5 | Hold |
| 2 | Paratyfoidfeber | 99,99 % | L4 | Hold |
| 3 | Salmonellose | 99,99 % | L4 | Hold |
| 4 | Bihulebetennelse | 99,99 % | L4 | Hold |
| 5 | Kronisk rhinosinusitt | 99,98 % | L4 | Hold |
| 6 | Tyfoidfeber | 99,98 % | L4 | Hold |
| 7 | Kronisk etmoidal sinusitt | 99,98 % | L4 | Hold |
| 8 | Svulst i paranasale bihuler | 99,98 % | L5 | Hold |
| 9 | Staphylococcus aureus-infeksjon | 99,95 % | L3 | Forskningsspørsmål |
| 10 | Eosinofili-myalgi-syndrom | 99,85 % | L5 | Hold |

## Hvorfor er denne prediksjonen rimelig?

Det foreligger for øyeblikket ingen detaljerte data om virkningsmekanisme i datagrunnlaget. Imipenem er et karbapenem som, ifølge kjent farmakologi, hemmer bakteriell celleveggsyntese via penicillinbindende proteiner.

For **diffus sklerodermi** er det ingen plausibel mekanistisk kobling. Sykdommen er autoimmun og fibrotisk, mens imipenem virker antibakterielt. Den høye TxGNN-scoren er kun en grafbasert prediksjon uten støtte fra studier eller litteratur. Prediksjonen bør derfor tolkes med stor forsiktighet.

De bakterielle prediksjonene er mer plausible. Imipenem har bredt spektrum mot Enterobacterales, inkludert Salmonella, og karbapenemer brukes som reservemidler ved ekstensivt resistent tyfoid. Dette er imidlertid mer en utvidelse av den opprinnelige gramnegative indikasjonen enn ekte reposisjonering. For bihulebetennelse vil systemisk bruk av karbapenem dessuten komme i konflikt med prinsippene for antibiotikastyring. For Staphylococcus aureus (MRSA) er imipenem studert som synergipartner, for eksempel sammen med fosfomycin eller linezolid.

For svulst i paranasale bihuler og eosinofili-myalgi-syndrom finnes det ingen mekanistisk begrunnelse.

## Klinisk studieevidens

Det finnes ingen registrerte kliniske studier for diffus sklerodermi (rang 1). Den eneste prediksjonen med kliniske studier er Staphylococcus aureus-infeksjon (rang 9):

| Studienummer | Fase | Status | Antall deltakere | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00871104](https://clinicaltrials.gov/study/NCT00871104) | Fase 4 | Fullført | 50 | Fosfomycin pluss imipenem sammenlignet med vankomycin (standardbehandling) ved MRSA-endokarditt |
| [NCT01356472](https://clinicaltrials.gov/study/NCT01356472) | Fase 4 | Ukjent | 60 | Linezolid alene eller kombinert med karbapenem mot MRSA ved ventilatorassosiert pneumoni; karbapenemet er ikke nødvendigvis imipenem |

## Litteraturevidens

For diffus sklerodermi finnes for øyeblikket ingen relevant litteratur. Nedenfor vises et utvalg for de mest relevante bakterielle prediksjonene.

| PMID | År | Type | Tidsskrift | Hovedfunn |
|------|-----|------|------|---------|
| [3460521](https://pubmed.ncbi.nlm.nih.gov/3460521/) | 1986 | Kohort | Antimicrob Agents Chemother | Imipenem-cilastatin hos 23 pasienter med MSSA/MRSA-infeksjoner |
| [33020155](https://pubmed.ncbi.nlm.nih.gov/33020155/) | 2020 | Kasuistikk | Antimicrob Agents Chemother | Imipenem/cilastatin pluss fosfomycin ved refraktær MRSA-infeksjon |
| [10588305](https://pubmed.ncbi.nlm.nih.gov/10588305/) | 1999 | Prekliniske | J Antimicrob Chemother | Synergi mellom vankomycin og imipenem mot MRSA in vitro og i musemodell |
| [6421794](https://pubmed.ncbi.nlm.nih.gov/6421794/) | 1983 | Prekliniske | J Antimicrob Chemother | Imipenem ved eksperimentell endokarditt hos kanin |
| [39991360](https://pubmed.ncbi.nlm.nih.gov/39991360/) | 2025 | Ikke klassifisert | Cureus | Karbapenemer som siste forsvarslinje ved MDR/XDR-tyfoid |
| [19208884](https://pubmed.ncbi.nlm.nih.gov/19208884/) | 2009 | Ikke klassifisert | J Med Microbiol | MIC for karbapenemer mot 210 Salmonella-isolater |
| [22204180](https://pubmed.ncbi.nlm.nih.gov/22204180/) | 2011 | In vitro-studie | J Pak Med Assoc | MIC for imipenem og andre midler mot Salmonella Typhi og Paratyphi |
| [15707075](https://pubmed.ncbi.nlm.nih.gov/15707075/) | 2003 | Kasuistikk | J Med Liban | Rabdomyolyse ved S. typhi-infeksjon behandlet med imipenem/cilastatin og hemodialyse |
| [9044641](https://pubmed.ncbi.nlm.nih.gov/9044641/) | 1996 | Ikke klassifisert | Enferm Infecc Microbiol Clin | Alvorlig orbital cellulitt; imipenem kan være et gyldig behandlingsvalg |
| [42482562](https://pubmed.ncbi.nlm.nih.gov/42482562/) | 2026 | Prekliniske | Small | Polymersomer med tobramycin og doripenem mot P. aeruginosa-biofilm ved kronisk rhinosinusitt |

Merk at mesteparten av litteraturen består av resistensovervåking og følsomhetsundersøkelser, som er indirekte in vitro-evidens og ikke viser klinisk effekt av imipenem. Flere av studiene gjelder også andre antibiotika.

## Informasjon om det norske markedet

| Godkjenningsnummer | Produktnavn | Doseringsform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/004808 | Recarbrio | Ikke oppgitt | Gramnegative bakterieinfeksjoner (status: kansellert) |

## Sikkerhetsvurderinger

**Kontraindikasjoner fra kunnskapsgrafen (ikke fra preparatomtale):** epilepsi, nyresykdom, pyoureter, Clostridium difficile-kolitt og nekrotiserende enterokolitt hos nyfødte.

**Legemiddelinteraksjoner** (15 registrert):
- **Alvorlige (Major):** bupropion, ioheksol, iopamidol
- **Moderate:** polyetylenglykol (3350 med elektrolytter), dikumarol, warfarin, lindan, aminofyllin, dyfyllin, oksitrifyllin, teofyllin, ciklosporin, etinylestradiol, mykofenolsyre, pemetreksed

Se preparatomtalen for fullstendig sikkerhetsinformasjon.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Den høyest rangerte prediksjonen, diffus sklerodermi, mangler både mekanistisk rasjonale, kliniske studier og litteratur. De bakterielle prediksjonene er stort sett utvidelser av den eksisterende gramnegative indikasjonen og understøttes kun av indirekte følsomhetsdata. Den eneste prediksjonen med klinisk grunnlag er Staphylococcus aureus-infeksjon (L3, to små fase 4-studier), som kan behandles som et forskningsspørsmål. Legemidlet har dessuten bare en kansellert godkjenning i Norge.

**For å gå videre trengs følgende:**
- Sikkerhetsdata fra preparatomtalen (advarsler og kontraindikasjoner), som er en blokkerende datamangel
- Data om virkningsmekanisme (MOA)
- For S. aureus: større, kontrollerte studier (fase 3) av imipenem i kombinasjonsregimer ved MRSA
- Avklaring av markedsstatus og tilgjengelige administrasjonsveier i Norge
- Vurdering opp mot antibiotikastyring før eventuell bruk ved nye infeksjonsindikasjoner
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

