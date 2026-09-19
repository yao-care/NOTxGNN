---
layout: default
title: Silodosin
parent: Kun modellprediksjon (L5)
nav_order: 323
evidence_level: L5
indication_count: 6
---

# Silodosin
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **6** stk.
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

# Silodosin: Fra Benign Prostatahyperplasi (BPH) til Ambras Type Hypertrichosis Universalis Congenita

## Sammenfatting i én setning

Silodosin er en høyselektiv α1A-adrenergisk reseptorantagonist, klinisk kjent for å behandle symptomer på nedre urinveier relatert til benign prostatahyperplasi (BPH), ved å virke på glatt muskulatur i prostata og blærehals. TxGNN-modellen forutsier en mulig sammenheng med **Ambras Type Hypertrichosis Universalis Congenita**, en sjelden medfødt hårvekstforstyrrelse, men dette er for øyeblikket støttet av **0 kliniske forsøk** og **0 publikasjoner**, og selve evidenspakken flagget ingen identifiserbar mekanistisk forbindelse.

## Rask oversikt

| Element | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke formelt angitt (`original_indications` er tom; `original_moa` er flagget som et datakløft). Forutsigelsesgrunnlagsteksten refererer til silodosins kjente virkning på glatt muskulatur i prostata og blærehals, i samsvar med dets etablerte BPH-bruk. |
| Forutsagt ny indikasjon | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN-forutsigelsespoengsum | 99.99% (global rangering 153) |
| Bevisnivå | L5 (kun modellforutsigelse — ingen forsøk, ingen litteratur) |
| Norges markedsstatus | Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne forutsigelsen rimelig?

Detaljerte virkningsmekanisme-data er ikke tilgjengelige i denne evidenspakken — det er eksplisitt oppført som et datakløft (DrugBank MOA-spørring, alvorlighetsgrad Høy; TFDA-etikett, alvorlighetsgrad Blokkering). Basert på de mekanistiske merknadene knyttet til hver forutsigelse, forstås silodosin som en høyselektiv α1A-adrenergisk reseptorantagonist som virker primært på glatt muskulatur i prostata og blærehals — det farmakologiske grunnlaget for dets etablerte BPH-bruk.

Ambras type hypertrichosis universalis congenita er en sjelden medfødt tilstand knyttet til kromosomale omarrangeringer nær hårsekk-utviklingsgener (f.eks. nær *TRPS1*) — en biologisk vei uten kjent skjæringspunkt med α1A-adrenergisk signalisering. Evidenspakkens eget grunnlagsfeld uttaler direkte at det er **ingen identifiserbar mekanistisk forbindelse** her.

Dette bør derfor leses som et rent embedding-likhets-funn fra TxGNN-modellen, ikke en mekanistisk begrunnet hypotese. Det samme mønsteret gjelder alle seks kandidatene i denne pakken: ingen har en sannsynlig mekanistisk begrunnelse, ingen har kliniske forsøk, og den ene kandidaten med tilknyttet litteratur (rangering 3, «malformasjonsyndrom med odontalt/periodontalt komponent,» 20 artikler) ble funnet ved inspeksjon å være et irrelevant søkeordsmatch — ingen av disse artiklene nevner silodosin eller α1-adrenergisk farmakologi i det hele tatt.

## Klinisk forsøksevidens

Ingen relaterte kliniske forsøk er for øyeblikket registrert

## Litteraturbevis

Ingen relatert litteratur er for øyeblikket tilgjengelig

## Norges markedsinformasjon

Ingen markedsautoriseringsregistreringer er for øyeblikket tilgjengelige for silodosin (markedsstatus: Ikke markedsført; 0 autorisasjoner på fil).

## Sikkerhetshensyn

Se pakningvedlegg for sikkerhetsinformasjon.

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
- Alle seks kandidatene i denne evidenspakken er utelukkende TxGNN-modellfunn (Bevisnivå L5), uten kliniske forsøk og uten mekanistisk sannsynlig begrunnelse; den ene kandidaten med tilknyttet litteratur viste seg å være et irrelevant søkeordsmatch. Det finnes for øyeblikket intet grunnlag for å ta fatt på noen kandidat for silodosin.

**For å komme videre, er følgende nødvendig:**
- TFDA-ekvivalent etikett (advarsler/kontraindikasjoner) — for øyeblikket er det en Blokkering datakløft (DG001)
- Bekreftet virkningsmekanisme fra DrugBank — for øyeblikket er det et Høy-alvorlighetsgrad datakløft (DG002)
- Formale data om opprinnelig indikasjon/godkjent merking (for øyeblikket tom i denne pakken)
- Dersom en eventuell fremtidig TxGNN-kandidat for silodosin viser en biologisk plausibel α1A-adrenergisk mekanisme, dedikert innsamling av bevis fra kliniske forsøk og litteratur for denne spesifikke kandidaten før omvurdering

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

