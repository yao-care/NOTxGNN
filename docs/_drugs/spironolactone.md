---
layout: default
title: Spironolactone
parent: Kun modellprediksjon (L5)
nav_order: 332
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **2** stk.
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

# Spironolakton: Fra en udokumentert original indikasjon til Hypotrichosis Simplex of the Scalp

## En setnings sammendrag

> Den opprinnelige godkjente indikasjonen for spironolakton er ikke dokumentert i denne bevissamlingen (datakluft, venter på DrugBank/etikett-oppslag).
> TxGNN-modellen forutsier en mulig sammenheng med **Hypotrichosis Simplex of the Scalp**,
> men denne prediksjonen er for øyeblikket støttet av **0 kliniske studier** og **0 publikasjoner** — modellpoeng alene.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ikke dokumentert i bevissamlingen (datakluft — venter på DrugBank-spørring) |
| Forutsagt ny indikasjon | Hypotrichosis Simplex of the Scalp |
| TxGNN prediksjonspoeng | 99.26% |
| Bevisgrad | L5 (modellpreduksjon kun, ingen kliniske studier eller litteratur) |
| Status på norsk marked | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Avvent |

---

## Hvorfor er denne prediksjonen rimelig?

For øyeblikket er detaljerte virkningsmekanisme-data ikke tilgjengelige for spironolakton i denne bevissamlingen (`original_moa` = datakluft). Basert på begrunnelsesteksten som er gitt sammen med prediksjonen, er spironolakton kjent for å virke som en **mineralokortikoid reseptor antagonist med anti-androgen aktivitet**, og det har faktisk off-label-bruk i den kliniske praksis ved androgenetisk alopeci — så en generell sammenheng mellom spironolakton og hårrelaterte tilstander er ikke urimelig på sitt ansikt.

Imidlertid er bevissamlingens egen mekanistiske vurdering for denne spesifikke prediksjonen skeptisk: **hypotrichosis simplex of the scalp** er en autosomalt dominant, strukturell/utviklings-relatert hårfollikkellidelse som er **ikke androgen-avhengig**. Det finnes ingen etablert biologisk sammenheng mellom spironolaktones kjente virkningsmekanisme og denne sykdommens patofysiologi — koblingen er vurdert som en TxGNN-ekstrapolasjon basert på fenotypisk likhet (hårrelaterte utfall) snarere enn genuin mekanistisk overlapping.

En andre, lavere rangert preduksjon (**congenital hypotrichosis milia**, poeng 99.04%) viser samme mønster: en sjelden ektodermale/follikulær utviklingslidelse uten kjent sammenheng til mineralokortikoid eller anti-androgen veier. Begge prediksjoner i denne bevissamlingen er flagget som manglende mekanistisk støtte utover modellens statistiske assosiasjon.

---

## Bevis fra kliniske studier

For øyeblikket ingen relaterte kliniske studier registrert.

---

## Litteraturbevis

For øyeblikket ingen relatert litteratur tilgjengelig.

---

## Status på norsk marked

Spironolakton er for øyeblikket **ikke markedsført** i Norge under denne bevissamlingen (0 godkjenninger, ingen lisensposter tilgjengelige).

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merk: viktige advarsler, kontraindikasjoner og DDI-data er flagget som blokkerende/høy-alvorlighetsgrad dataklufter — se Konklusjon nedenfor.)*

---

## Konklusjon og neste steg

**Beslutning: Avvent**

**Begrunnelse:**
Begge kandidatindikasjoner er støttet kun av TxGNN modellpoeng (L5, ingen klinisk eller litteraturbevis), og bevissamlingens egen mekanistiske begrunnelse noter eksplisitt mangel på biologisk plausibilitet for topprediksjonen. I tillegg forhindrer en **blokkerende** datakluft (manglende TFDA/etikettadvarsler og kontraindikasjoner) at stoffet til og med går inn i S1 sikkerhet pre-vurderingsstadiet.

**For å fortsette, er følgende nødvendig:**
- TFDA/produktetikett advarsler og kontraindikasjoner (DG001 — blokkerende, påkrevd for S1 sikkerhet screening)
- Virkningsmekanisme data via DrugBank API (DG002 — høy alvorlighetsgrad)
- Dokumentasjon av spironolaktones opprinnelige godkjente indikasjon(er)
- Uavhengig klinisk eller preklinisk bevis som knytter spironolakton til hypotrichosis simplex of the scalp, utover modell-avledet likhet

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

