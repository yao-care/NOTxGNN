---
layout: default
title: Vismodegib
parent: Kun modellprediksjon (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vismodegib: predikert ny indikasjon Medulloblastom med utbredt nodularitet (evidensnivå L5). Opprinnelig indikasjon: Basalcellekarsinom"
---

# Vismodegib
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

# Vismodegib: Fra basalcellekarsinom til medulloblastom med utbredt nodularitet

## Oppsummering i en setning

Vismodegib er en Hedgehog-hemmer som opprinnelig brukes mot basalcellekarsinom. TxGNN-modellen forutsier at legemidlet kan ha effekt ved **medulloblastom med utbredt nodularitet**. Per i dag finnes det **ingen kliniske studier og ingen publikasjoner** for denne spesifikke diagnosen, så prediksjonen bygger kun på modellen.

---

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Basalcellekarsinom |
| Predikert ny indikasjon | Medulloblastom med utbredt nodularitet |
| TxGNN-prediksjonsscore | 99,93 % |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Kun avregistrerte/tilbakekalte godkjenninger |
| Antall godkjenninger | 1 (0 gyldige, 1 avregistrert) |
| Anbefalt beslutning | Hold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte mekanismedata er foreløpig ikke tilgjengelige i datagrunnlaget for denne rapporten. Vismodegib er imidlertid kjent som en hemmer av Smoothened (SMO), en sentral komponent i Hedgehog-signalveien. Effekten ved basalcellekarsinom er påvist, og denne kreftformen drives av aktivering av Hedgehog-signalveien (PTCH1/SMO-mutasjoner).

Medulloblastom med utbredt nodularitet er en undertype av den SHH-aktiverte gruppen, der Hedgehog-signalering (endringer i PTCH1/SUFU) driver tumorutviklingen. Mekanistisk er det derfor plausibelt at en SMO-hemmer kan ha effekt.

Det er likevel viktige forbehold:
- Responsen ved SHH-medulloblastom avhenger av hvor i signalveien mutasjonen sitter. Mutasjoner i SMO eller PTCH1 gir sannsynlig respons, mens tap av SUFU nedstrøms for SMO trolig gjør en SMO-hemmer virkningsløs.
- Det finnes ingen studier eller litteratur for akkurat denne diagnosen i datagrunnlaget.
- Bruk hos barn gir bekymring for vekstsonene (for tidlig lukking av epifysene).

---

## Klinisk evidens

Foreløpig ingen relaterte kliniske studier registrert.

---

## Litteraturevidens

Foreløpig ingen relatert litteratur tilgjengelig.

---

## Markedsinformasjon for Norge

| Godkjenningsnummer | Produktnavn | Legemiddelform | Godkjent indikasjon |
|---------|------|------|-----------|
| EMEA/H/C/002602 (avregistrert) | Erivedge | Ikke oppgitt | Basalcellekarsinom |

---

## Cytotoksisitet

| Punkt | Innhold |
|------|------|
| Klassifisering | Målrettet terapi (Hedgehog-/Smoothened-hemmer), ikke konvensjonelt cytostatikum |
| Risiko for myelosuppresjon | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Emetogenisitet | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Overvåkingsparametere | Se pakningsvedlegget for advarsler og forsiktighetsregler |
| Håndtering og vern | Se pakningsvedlegget. Legemidlet er teratogent, og dette må hensyntas ved håndtering og bruk |

---

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner**: Datagrunnlaget viser 56 registrerte interaksjoner.
  - Den eneste med moderat alvorlighetsgrad blant de listede er **klaritromycin**.
  - De øvrige listede interaksjonene er **milde** og gjelder hovedsakelig syrehemmende legemidler: protonpumpehemmere (omeprazol, esomeprazol, pantoprazol, lansoprazol, rabeprazol, deksansoprazol), H2-blokkere (famotidin, ranitidin, cimetidin, nizatidin) og antacida (aluminiumhydroksid, kalsiumkarbonat, magnesiumoksid/-hydroksid/-karbonat, magaldrat, natriumbikarbonat, natriumsitrat).
- **Bruk hos barn**: Risiko for for tidlig lukking av epifysene (vekstsonene) må vurderes nøye, særlig siden medulloblastom ofte rammer barn.
- **Andre kjente bivirkninger som bør overvåkes** (fra datagrunnlaget): teratogenisitet, muskelkramper, hårtap og smaksforstyrrelser.

---

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen har høy modellscore og en plausibel mekanisme via Hedgehog-signalveien, men evidensnivået er L5 uten kliniske studier eller litteratur for denne diagnosen. I tillegg avhenger responsen av mutasjonsnivå i signalveien, bruk hos barn gir sikkerhetsbekymringer, og legemidlet har kun avregistrerte godkjenninger i Norge.

Til sammenligning har andre prediksjoner for vismodegib bedre støtte i datagrunnlaget:
- **Hudkreft** (evidensnivå L2): flere fase 2-studier og retningslinjer, men indikasjonen overlapper i stor grad med den opprinnelige.
- **Xeroderma pigmentosum** (evidensnivå L4): to kasuistikker om behandling av multiple basalcellekarsinomer hos pasienter med sykdommen.

**For å gå videre trengs følgende:**
- Systematisk gjennomgang av litteratur og pågående studier om SHH-medulloblastom, inkludert undertypen med utbredt nodularitet
- Molekylær karakterisering av tumorene (SMO-, PTCH1- og SUFU-status) for å identifisere hvilke pasienter som kan respondere
- Plan for sikkerhetsovervåking hos barn, særlig vekstsoner og vekst
- Avklaring av tilgjengelighet i Norge, siden alle godkjenninger er avregistrert
- Fullstendig gjennomgang av pakningsvedlegget (advarsler, kontraindikasjoner) og detaljerte mekanismedata
## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

