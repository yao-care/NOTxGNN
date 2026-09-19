---
layout: default
title: Chenodeoxycholic Acid
parent: Kun modellprediksjon (L5)
nav_order: 86
evidence_level: L5
indication_count: 5
---

# Chenodeoxycholic Acid
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

# Chenodeoxycholic Acid: Manglende originale indikasjondata → Predikert ny indikasjon «Homozygøs familial hyperkolesterolemi» (HoFH)

## En-setnings sammenfatning

> Khenodeoksikholsyre (Chenodeoxycholic Acid, DB06777) mangler for tiden både **originale indikasjon- og virkningsmekanismedata** (Data Gap DG002), og er ikke ennå markedsført i Taiwan (tillatelser: 0).
> TxGNN-modellen predikerer at den kan være effektiv mot **homozygøs familial hyperkolesterolemi (HoFH)**,
> men for tiden er det kun **0 kliniske forsøk** og **1 publikasjon** som støtter dette, og publikasjonen omhandler faktisk cerebrotendinøs xantomatose (CTX) i stedet for HoFH, med svært svak bevisgrad.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Originale indikasjon | Manglende data (`original_indications` er tom, `original_moa` er heller ikke oppgitt, se DG002) |
| Predikert ny indikasjon | Homozygøs familial hyperkolesterolemi (Homozygous Familial Hypercholesterolemia, HoFH) |
| TxGNN prediksjonspoengsum | 99.57% (opprinnelig rangering 5013) |
| Bevisgrad | L5 (kun modellpreduksjon, ingen kliniske forsøk, den eneste publikasjonen behandler ikke relevant emne) |
| Taiwan-markedsstatus | Ikke markedsført |
| Antall tillatelser | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor virker denne prediksjonen rimelig?

For tiden finnes det ingen detaljert informasjon om virkningsmekanisme (MOA) tilgjengelig for verifisering (Data Gap DG002). Basert på etablert farmakologisk kunnskap er chenodeoxycholic acid en naturlig gallesyre som kan aktivere FXR (farnesol X-reseptor) og tilbakemeldingshemme CYP7A1, og dermed redusere hastigheten for konvertering av kolesterol til gallesyrer – teoretisk sett har det indirekte forbindelse til lipidmetabolske veier.

Rang 1-prediksjonsindikasjon HoFH er forårsaket av funksjonsverlust i LDL-reseptorgenet, noe som fører til at LDL-kolesterol i serum ikke kan fjernes effektivt. CDCA regulert via FXR/CYP7A1-veien påvirker kolesteols «nedstrøms metabolisme», og det finnes ingen kjente mekanismer som kan kompensere for den iboende LDL-reseptorfunksjonsdefekten, slik at mekanismesammenhengen er svak.

Enda viktigere er det at den eneste medfølgende støttepublikasjonen (PMID 25424010) faktisk omhandler **cerebrotendinøs xantomatose (CTX)**, som er en helt annen sykdom med helt annen etiologi enn HoFH. De ble bare merket med samme sykdomsmerknad fordi begge klinisk kan presentere xantomer, som ikke utgjør faktisk bekreftelse. De øvrige fire kandidatindikasjonene (rang 2–5) har enda svakere mekanismesammenhengen: rang 2 og 3 er COL4A1-relaterte vaskulære/okulære medfødte anomalier uten kjent forbindelse til gallesyremetabolisme, rang 2 medfølgende 19 publikasjoner er for det meste individuelle tilfellerapporter av ulike medfødte øyemalformasjoner og helt irrelevante for CDCA-farmakologi, og representerer støy fra nøkkelordfeiltilpasning; rang 4 og 5 sykdommene selv er merket som «foreldet» (obsolete), noe som indikerer datalvalitetsproblemer i ontologien. Samlet sett mangler denne prediksjonsgruppen klinisk tolkbarhet.

---

## Bevis fra kliniske forsøk

Det finnes for tiden ingen relevante registrerte kliniske forsøk.

---

## Litteraturbevis

| PMID | År | Type | Journal | Viktigste funn |
|------|-----|------|---------|----------------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Oversikt (Tier 3) | Orphanet Journal of Rare Diseases | Denne artikkelen gir en komplett oversikt over etiologi, klinisk presentasjon, diagnose og behandling av cerebrotendinøs xantomatose (CTX), **emnet er ikke HoFH**; det antakes at dette er støy forårsaket av feil sykdomsmerknad-tilpasning, og utgjør ikke direkte bekreftelse for HoFH-indikasjon. |

---

## Taiwan-markedsinformasjon

For tiden finnes det ingen data om markedsføring i Taiwan for dette legemidlet, og det er ikke godkjent for markedsføring i Taiwan ennå.

---

## Sikkerhetshensyn

For tiden finnes det ingen taiwanske pakningseddelsadvarsler, kontraindikasjoner eller data om legemiddelinteraksjoner (Data Gap DG001, alvorlighetsgrad: **Blokkering**, denne spalten vil blokkere S1 sikkerhetsinitialvurdering). Etter å ha hentet den offisielle taiwanske TFDA-pakningseddelen og gjennomført analyse, kan fullstendig sikkerhetsassessment oppfylles.

---

## Konklusjon og neste trinn

**Beslutning: Avvent**

**Begrunnelse:**
- Alle 5 prediksjonsindikasjonene har bevisgrad L5 – kun modellprediksjonsscore, ingen kliniske forsøk som støtter dem, og den eneste medfølgende publikasjonen er ikke om relevant emne (eller helt irrelevant), mekanismesammenhengen er svak eller til og med støy fra feil sykdomsmerknad-tilpasning;
- Legemidlet mangler originale indikasjon- og virkningsmekanismedata (DG002, høy), og taiwanske pakningseddelsadvarsler/kontraindikasjoner mangler (DG001, blokkering), noe som gjør at S1 sikkerhetsinitialvurdering ikke kan gjennomføres.

**Hvis man ønsker å fortsette, må følgende tilføyes:**
- Innhente offisiell virkningsmekanisme (MOA) og originale godkjente indikasjondata fra DrugBank eller originalt farmasøytisk firma
- Innhente offisiell taiwansk TFDA-pakningsetikett PDF og analyser advarsler, kontraindikasjoner og legemiddelinteraksjoner for å løse DG001-blokkeringen
- Supplere med riktig relevant klinisk forsøk eller litteraturbevis for rang 1-kandidaten (HoFH) – den eneste publikasjonen (CTX) er ikke relevant
- Gjennomgå ontologidatakvaliteten, eliminer «foreldet» terminologi i rang 3–5-kandidatene og feil sykdomsmerknad-tilpasning som er helt usammenhengende med legemidlets farmakologimekanisme

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

