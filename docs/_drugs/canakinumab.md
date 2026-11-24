---
layout: default
title: Canakinumab
parent: Kun modellprediksjon (L5)
nav_order: 80
evidence_level: L5
indication_count: 9
monitor_inn: "CANAKINUMAB"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
last_modified_at: 2026-11-24
description: "Canakinumab: predikert ny indikasjon Leverinfarkt (hepatic infarction) (evidensnivå L5). Opprinnelig indikasjon: Cryopyrin-Associated Periodic Syndromes"
---

# Canakinumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **9** stk.
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

## Kanakinumab: IL-1β-hemmer → Leverinfarkt (hepatic infarction)
{: .text-alpha }

## Kort oppsummering

Kanakinumab er et monoklonalt antistoff som blokkerer interleukin-1β. Modellen TxGNN predikerer at legemidlet kan ha effekt ved **leverinfarkt (hepatic infarction)**. Det finnes imidlertid **ingen kliniske studier og ingen publikasjoner** som støtter denne prediksjonen, som dermed bygger kun på modellen.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Cryopyrin-Associated Periodic Syndromes;Arthritis, Juvenile Rheumatoid;Arthritis, Gouty |
| Predikert ny indikasjon | Leverinfarkt (hepatic infarction) |
| TxGNN-prediksjonsscore | 0,9986 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Canakinumab (uoffisiell oversettelse): «Kanakinumab er et humant monoklonalt anti-humant IL-1β-antistoff av isotypen IgG1/κ. Kanakinumab bindes til humant IL-1β og nøytraliserer dets aktivitet ved å blokkere interaksjonen med IL-1-reseptorer, men det bindes ikke til IL-1α eller IL-1-reseptorantagonist (IL-1ra).» Engelsk originaltekst: "Canakinumab is a human monoclonal anti-human IL-1β antibody of the IgG1/κ isotype. Canakinumab binds to human IL-1β and neutralizes its activity by blocking its interaction with IL-1 receptors, but it does not bind IL-1α or IL-1 receptor antagonist (IL-1ra)." ([DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e), versjon av 2026-06-08; hentet 2026-11-19). Kanakinumab nøytraliserer interleukin-1β, en sentral mediator i steril betennelse.

Teoretisk kan IL-1β-blokade dempe den sterile betennelsesreaksjonen som følger etter iskemisk skade i leveren. Dette er en spekulativ hypotese. Det er ikke framlagt mekanistiske eller kliniske data for denne indikasjonen, og likheten med de opprinnelige bruksområdene er ikke vurdert.

## Klinisk studiedokumentasjon

For tiden er ingen relaterte kliniske studier registrert.

## Litteraturdokumentasjon

For tiden er ingen relatert litteratur tilgjengelig.

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/001109 | Ilaris | Canakinumab | Cryopyrin-Associated Periodic Syndromes; Arthritis, Juvenile Rheumatoid; Arthritis, Gouty | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Dataene viser én lisens (EMEA/H/C/001109, Novartis Europharm Limited) for enkeltstoffet. Markedsstatus for legemidlet er «Markedsført».

## Sikkerhetsvurderinger

**Legemiddelinteraksjoner** (100 registrerte interaksjoner; de viktigste er listet):

- **Moderat alvorlighetsgrad:** kortikosteroider (hydrokortison, triamcinolon, deksametason, betametason, budesonid, prednisolon, prednison), simvastatin, antikoagulantia (apiksaban, dikumarol, rivaroksaban, warfarin) og radiofarmaka (ibritumomab tiuxetan, jobenguan (I-131), tositumomab, tositumomab (I-131)).
- **Mindre alvorlighetsgrad:** sinkpreparater (sinkacetat, sinkglukonat, sinksulfat).

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for leverinfarkt støttes ikke av noen kliniske studier eller publikasjoner, og den mekanistiske koblingen er kun teoretisk. Evidensnivået er L5.

**For å gå videre kreves følgende:**
- Data om virkningsmekanisme (MOA) og en mekanistisk begrunnelse for leverinfarkt
- Prekliniske data eller en systematisk litteraturgjennomgang som direkte omhandler leverinfarkt
- Sikkerhetsinformasjon fra preparatomtalen (advarsler og kontraindikasjoner)
- Vurdering av administrasjonsvei og aktuell pasientpopulasjon

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

