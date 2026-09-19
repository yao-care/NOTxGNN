---
layout: default
title: Pretomanid
parent: Kun modellprediksjon (L5)
nav_order: 290
evidence_level: L5
indication_count: 5
---

# Pretomanid
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

# Pretomanid: Fra tuberkulose til kandidiasis

## Oppsummering på én setning

Pretomanid er en antimykobakteriell nitroimidazooxazin utviklet for medikamentresistent tuberkulose (brukt som del av BPaL/BPaLM-regime sammen med bedaquiline, linezolid og moxifloxacin). Modellens topprediksjon foreslår mulig aktivitet mot **kandidiasis**, men denne kombinasjonen har **null støtting fra kliniske studier eller litteratur** og mangler, etter mekanistisk gjennomgang, biologisk plausibilitet — *Candida*-arter har ikke Ddn/F420-nitroreduktase-systemet som pretomanid krever for aktivering.

---

## Rask oversikt

| Punkt | Innhold |
|-------|---------|
| Originalindikasjon | Medikamentresistent lungetuberkulose (BPaL/BPaLM-regime) — ikke til stede i norske lisenseringdata; hentet fra litteraturkontekst |
| Predikert ny indikasjon | Kandidiasis |
| TxGNN-prediksjonscore | 99.69% |
| Bevisnivå | L5 (modellprediksjon kun, ingen klinisk eller litteraturbevis) |
| Markedsstatus i Norge | Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Innstilles |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte DrugBank-data om virkningsmekanisme er ikke tilgjengelig for pretomanid i denne bevissamlingen. Imidlertid viser kryssreferansering av den medfølgende litteraturen og mekanistiske annoteringer at pretomanid er en nitroimidazooxazin (PA-824) som krever aktivering av det mykobakteriespesifikke **Ddn/F420 deazaflavin-avhengige nitroreduktase-systemet** for å generere sin bakterisidal effekt. Denne aktiveringsbanen er unik for mykobakteria og er grunnlaget for pretomanids rolle i BPaL-regime for omfattende medikamentresistent og behandlingsintolerant multimedikamentresistent TB.

Kandidiasis er forårsaket av *Candida*-arter, som ikke uttrykker Ddn/F420-nitroreduktase-systemet. Nitroimidazol-klasselegemidler er generelt kjent for å mangle antifungal aktivitet gjennom denne mekanismen. Dette betyr at TxGNN-assosiasjonen mest sannsynlig er drevet av innebygd likhet snarere enn noen virkelig farmakologisk eller klinisk signal — i samsvar med det fullstendige fravær av kliniske studier eller publikasjoner som knytter pretomanid til kandidiasis i dette datasettet.

For kontekst er en biologisk mer plausibel kandidat i dette datasettet **spedalskhet** (rangering 2, *M. leprae*, samme slekt som *M. tuberculosis*), som i teorien deler den samme nitroreduktase-aktiveringsbanen. Imidlertid motsier det sterkeste direkte beviset som er tilgjengelig (PMID 17005816, "*Mycobacterium leprae is naturally resistant to PA-824*") direkte effektiviteten — dyremodelldata viser ingen bakterisidal aktivitet mot *M. leprae* til tross for den delte slekten. Dette understreker at likhet på slektsnivå ikke garanterer funksjonell ekvivalens, og forsterker forsiktighet rundt topprankingen av kandidiasis.

---

## Bevis fra kliniske studier

Ingen relaterte kliniske studier er for tiden registrert.

---

## Litteraturbevis

Ingen relatert litteratur er for tiden tilgjengelig.

---

## Norsk markedsinformasjon

Pretomanid er for tiden ikke markedsført i Norge (0 godkjennelser på registrer). Ingen produktlisens, dosisform eller godkjent indikasjondata er tilgjengelig.

---

## Sikkerhetshensyn

Strukturert sikkerhetsdata (advarsler, kontraindikasjoner, DDI) er for tiden ikke tilgjengelig for pretomanid i denne bevissamlingen (TFDA-merkedata-innsamling er en blokkerende datagap — DG001).

Ett sikkerhetssignal dukket opp indirekte gjennom den mekanistiske gjennomgangen av andre kandidatindikasjoner i dette datasettet: pretomanid har en kjent **QT-intervallforlengelsesrisiko**, en hjertesikkerhetsspørsmål som bør tas med i vurderingen ved enhver fremtidig klinisk utvikling uavhengig av målindikasjon.

Se pakningsvedlegget for fullstendig sikkerhetsinformasjon når den er tilgjengelig.

---

## Konklusjon og neste steg

**Beslutning: Innstilles**

**Begrunnelse:**
Topprankingen (kandidiasis) har ingen klinisk studie- eller litteraturstøtte og mangler mekanistisk plausibilitet, siden *Candida*-arter ikke besitter det mykobakteriespesifikke nitroreduktase-aktiveringssystemet som pretomanid er avhengig av. Neste beste kandidat i dette datasettet (spedalskhet) har en delvis plausibel delt-slektsmekanisme, men er direkte motsagt av eksisterende preklinisk bevis som viser at *M. leprae* er naturlig resistent mot pretomanid (PA-824). Ingen kandidat i denne bevissamlingen oppfyller for tiden en bar for videre utvikling.

**For å fortsette er følgende nødvendig:**
- TFDA-merke/advarsler og kontraindikasjonsdata (DG001, blokkering — påkrevd før S1-sikkerhetsscreening)
- DrugBank-hentet detaljert MOA-data (DG002) for å riktig vurdere mekanistisk overlapping for fremtidige kandidater
- Dersom repurposering fortsatt er av interesse, prioriter kandidatsykdommer med faktisk mykobakteriell eller nitroreduktase-avhengig patogenese i stedet for gjeldende TxGNN-topprankingsresultater
- Uavhengig in vitro-bekreftelse før vurdering av noen kandidat på denne listen for videre evaluering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

