---
layout: default
title: Maraviroc
parent: Kun modellprediksjon (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Maraviroc
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

# Maraviroc: fra HIV-1-infeksjon (kjent indikasjon, ikke i bevissamlingen) til multipel endokrin neoplasi

## Oppsummering på én setning

> Maraviroc er en CCR5-antagonist som brukes i antiretroviral terapi for HIV-1-infeksjon; imidlertid er den opprinnelige indikasjonen og virkningsmekanismen ikke dokumentert i denne bevissamlingen (datakluft).
> TxGNN-modellen predikerer at det kan være effektivt for **multipel endokrin neoplasi**,
> men denne prediksjonen er for øyeblikket støttet av **0 kliniske forsøk** og **0 publikasjoner**, og modellens egen begrunnelse sier eksplisitt at det ikke er noen kjent biologisk sammenheng mellom CCR5–CCL5-aksen og MEN-patologi.

---

## Kort oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke registrert i bevissamlingen (`original_indications` tomt) — offentlig kjent som HIV-1-infeksjon, ikke bekreftet innenfor dette datasettet |
| Predikert ny indikasjon | Multipel endokrin neoplasi |
| TxGNN-prediksjonspoeng | 99.82% |
| Bevisnivå | L5 (kun modellprediksjon, ingen støttende forsøk eller litteratur) |
| Norges markedsstatus | ✗ Ikke markedsført |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte data om virkningsmekanisme ikke tilgjengelige (datakluft DG002). Basert på generell kunnskap om stoffklassen er maraviroc en CCR5- (C-C-chemokinreseptor type 5) antagonist som blokkerer virusinngang i antiretroviral terapi. Dets etablerte kliniske bruk er ikke registrert i denne bevissamlingen, så denne sammenhengen bør behandles kun som bakgrunnskunnskap, ikke som bekreftet data som støtter denne repurposingkandidaten.

Forholdet mellom stoffets kjente mekanisme og den predikerte indikasjonen er svakt. Multipel endokrin neoplasi (MEN) er et arvelig endokrint tumorsyndom drevet av *RET*- eller *MEN1*-genmuteringer, og — ifølge modellens egen repurposingbegrunnelse — har **ingen kjent biologisk sammenheng** til CCR5–CCL5-signaliseringsaksen. Begrunnelsesteksten sier eksplisitt at dette er en prediksjon basert kun på TxGNN-poeng, uten mekanistisk støtte eller litteraturstøtte.

Gitt dette bør den høyest rangerte prediksjonen tolkes som en kandidat flagget rent av modellens lærte embedding-likhet, ikke av noen farmakologisk eller klinisk begrunnelse. Dette gjør nødvendigvis ikke modellutgangen ugyldig, men det betyr at prediksjonen for øyeblikket sitter på det laveste tillitsnivået (L5) og krever betydelig uavhengig validering før ytterligere tiltak.

---

## Bevis fra kliniske forsøk

For øyeblikket ingen relaterte kliniske forsøk registrert

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig

---

## Markedsinformasjon for Norge

Maraviroc har for øyeblikket **ingen markedsføringstillatelse i Norge** (`market_status`: Not marketed / Not Marketed; `total_licenses`: 0). Ingen lisensposter er tilgjengelige for sammenfatning.

---

## Sikkerhetshensyn

Se pakningsvedlegget for sikkerhetsinformasjon.

(Notat: Viktige advarsler, kontraindikasjoner og data om legemiddelinteraksjoner er alle flagget som dataklufter (DG001, blokkeringsseveritet) i denne bevissamlingen — dette er en forutsetningskluft som må løses før noen sikkerhetsvurdering, ifølge bevissamlingens eget S1-trinns gatingprinsipp.)

---

## Konklusjon og neste trinn

**Beslutning: Hold**

**Begrunnelse:**
Den høyest rangerte predikerte indikasjonen (multipel endokrin neoplasi) har ingen støttende kliniske forsøk, ingen støttende litteratur, og modellens egen mekanistiske begrunnelse sier eksplisitt at det ikke er noen kjent biologisk sammenheng mellom CCR5-signalisering og MEN-patologi. Kombinert med den blokkerende datakluften på sikkerhetsetikett (DG001) og de manglende MOA-dataene (DG002), finnes det for øyeblikket intet grunnlag for å fremme denne kandidaten utover modellutgang.

**For å gå videre, er det følgende nødvendig:**
- Løs DG001 (TFDA/regulatoriske etikettadvarsler og kontraindikasjoner) — blokkerer for øyeblikket enhver sikkerhetsvurdering
- Løs DG002 (bekreftet virkningsmekanisme fra DrugBank eller primær litteratur)
- Uavhengig in vitro eller bioinformatisk validering av en CCR5–MEN-signalveisammenheng før ytterligere bevisinnsamling prioriteres
- Vurder å omdirigere bevisinnsamlingsinnsatsen mot bevissamlingens kandidater med sterkere bevis i stedet for kandidaten med høyeste TxGNN-score: **HER2-positivt brystkreft** (rang 10, L4, beslutningsstadium S1 "Research Question" — støttet av en konkret preklinisk mekanismeartikel om CCL5–CCR5-formidlet trastuzumabresistens) og **cytomegalovirus-infeksjon** (rang 9, L4, S1 — støttet av to immunologi-kohort-/oversiktsartikler), som begge for øyeblikket har sterkere mekanistisk og bevisgrunnlag enn den høyest rangerte MEN-prediksjonen

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

