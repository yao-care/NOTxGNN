---
layout: default
title: Irbesartan
parent: Kun modellprediksjon (L5)
nav_order: 191
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **4** stk.
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

# Irbesartan: Fra hypertensjon til malign renovaskular hypertensjon

## Sammenfatning i én setning

Irbesartan er en angiotensin II-reseptorblokkerer (ARB); detaljert godkjent indikasjonsbeskrivelse er ikke tilgjengelig i dette datasettet. TxGNN-modellen forutsier potensiell effektivitet for **malign renovaskular hypertensjon**, men denne prognosen støttes for øyeblikket av **ingen kliniske studier og ingen litteratur** — den baseres utelukkende på mekanistisk plausibilitet (RAAS-veiblokade).

## Rask oversikt

| Emne | Innhold |
|------|------|
| Opprinnelig indikasjon | Ikke spesifisert i datasettet (ingen medikamentlisens eller indikasjonsbeskrivelse tilgjengelig; Irbesartan er en kjent ARB som vanligvis brukes mot hypertensjon) |
| Forutsagt ny indikasjon | Malign renovaskular hypertensjon |
| TxGNN prediktiv score | 99.31% |
| Bevisnivå | L4 (mekanisme-basert, ingen klinisk/litteraturstøtte) |
| Markedsstatus for Norge | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt vedtak | Hold |

## Hvorfor er denne prognosen rimelig?

For øyeblikket er detaljerte data om virkningsmåte for denne kandidaten ikke tilgjengelig i datasettet (merket som høy-alvorlighetsgrad datakløft, DG002). Basert på generell farmakologisk kunnskap tilhører Irbesartan angiotensin II-reseptorblokkerer-klassen (ARB), som blokkerer AT1-reseptoren for å dempe RAAS-drevet vasokonstriksjon — en vei som er sentral for patofysiologien ved renovaskular hypertensjon (nyrearteriestenose → økt renin-frigjøring → systemisk hypertensjon).

Mekanistisk sett forklarer dette hvorfor TxGNN tildeler en høy prediktiv score: ARB-farmakologi er konseptuelt i tråd med patofysiologien ved malign renovaskular hypertensjon. Imidlertid er dette en viktig advarsel snarere enn ren støtte — ARB-er og ACE-hemmere har en veletablert risiko for å forårsake akutt nyreskade hos pasienter med bilateral nyrearteriestenose eller stenose i en enkelt fungerende nyre, som er nettopp populasjonen denne indikasjonen retter seg mot. Prognosen bør derfor behandles som en mekanistisk hypotese som krever nøye sikkerhetsvurdering, ikke som validert effektivitet.

## Bevis fra kliniske studier

Ingen relaterte kliniske studier er for øyeblikket registrert.

## Litteraturbevis

Ingen relatert litteratur er for øyeblikket tilgjengelig.

*(Merknad: bevissamlingen inneholder imidlertid 20 litteraturreferanser under en lavere rangert, lavere konfidensindikasjon — "pulmonal hypertensjon på grunn av lungesykdom og/eller hypoksi" — men ingen av disse artiklene nevner Irbesartan eller ARB-er; de er generelle hypoksi-/onkologibiologiartikler og utgjør heller ikke støttende bevis for den indikasjonen heller.)*

## Markedsinformasjon for Norge

Irbesartan er for øyeblikket **ikke markedsført** i Norge i henhold til dette datasettet — ingen medikamentlisenser ble funnet (`total_licenses: 0`).

## Sikkerhetshensyn

Detaljerte sikkerhetdata (sentrale advarsler, kontraindikasjon, legemiddelinteraksjoner) er ikke tilgjengelig i dette datasettet. Dette er merket som en **Blocking**-alvorlighetsgrad datakløft (DG001 — TFDA/regulatorisk pakningssedhette advarsler og kontraindikasjon), som betyr at denne kandidaten ikke kan gå videre til formell sikkerhetsvurdering (S1) inntil den offisielle produktinformasjonen hentes.

Vennligst se den offisielle pakningssedhetten for fullstendig sikkerhetsinformasjon når den er tilgjengelig. Gitt den kjente klasse-effekt-risikoen for ARB-er ved nyrearteriestenose (potensiell akutt nyreskade), bør nyrefunksjon og sikkerhetdata prioriteres før videre evaluering av denne spesifikke indikasjonen.

## Konklusjon og neste skritt

**Vedtak: Hold**

**Begrunnelse:**
Bevisnivå er L4 — prognosen støttes kun av mekanistisk resonnering på klassenivå, uten noen kliniske studier eller litteratur som direkte omhandler Irbesartan ved malign renovaskular hypertensjon. Legemidlet er for øyeblikket ikke markedsført i Norge, og en Blocking sikkerhetsdatakløft (manglende pakningssedhette advarsler/kontraindikasjon) hindrer framskriden til formell sikkerhetsvurdering. Det finnes også en kjent klassespesifikk risiko (AKI ved nyrearteriestenose) som direkte strider mot målpopulasjonen, som rettferdiggjør forsiktighet snarere enn framgang.

**For å gå videre kreves følgende:**
- Offisiell produktinformasjon (TFDA eller tilsvarende) for advarsler og kontraindikasjon (løser blocking-kløft DG001)
- Detaljert virkningsmåtedata fra DrugBank (løser DG002)
- Målrettet litteratur-/forsøkssøk spesifikt for ARB-bruk ved renovaskular eller malign hypertensjon (gjeldende litteratursamling er ikke relevant)
- Nyrefunksjonsovervåkningsprotokoll gitt den kjente AKI-risikoen for ARB-er ved bilateral/enkelt-nyre nyrearteriestenose
- Revurdering av markedsstatussen i Norge før man vurderer omsidesbruksforløp

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

