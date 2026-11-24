---
layout: default
title: Emicizumab
parent: Kun modellprediksjon (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
monitor_inn: "EMICIZUMAB"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "thrombotic thrombocytopenic purpura", "fetal and neonatal alloimmune thrombocytopenia", "flood factor deficiency"]
last_modified_at: 2026-11-24
description: "Emicizumab: predikert ny indikasjon pseudo-von Willebrands sykdom (pseudo-von Willebrand disease) (evidensnivå L5). Opprinnelig indikasjon: Hemophilia A"
---

# Emicizumab
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **10** stk.
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

## Emicizumab: bispesifikt antistoff som etterligner faktor VIIIa → pseudo-von Willebrands sykdom (pseudo-von Willebrand disease)
{: .text-alpha }

## Oppsummering i én setning

Emicizumab er et bispesifikt antistoff som etterligner funksjonen til aktivert faktor VIII.
TxGNN-modellen predikerer at legemidlet kan være virksomt ved **pseudo-von Willebrands sykdom (pseudo-von Willebrand disease)**,
men det finnes **ingen kliniske studier og ingen publikasjoner** som direkte støtter denne prediksjonen. Prediksjonen er kun modellbasert.

## Hurtigoversikt

| Punkt | Innhold |
|------|------|
| Opprinnelig indikasjon | Hemophilia A |
| Predikert ny indikasjon | pseudo-von Willebrands sykdom (pseudo-von Willebrand disease) |
| TxGNN-prediksjonsscore | 0,9999 |
| Evidensnivå | L5 |
| Markedsstatus i Norge | Markedsført (gyldige tillatelser: 1 av 1) |
| Antall godkjenninger | 1 (gyldige: 1) |
| Anbefalt beslutning | Hold |

## Hvorfor er denne prediksjonen rimelig (eller ikke)?

Ifølge avsnittet «Mechanism of Action» i preparatomtalen som er godkjent av amerikanske FDA (Prescribing Information), for Emicizumab (uoffisiell oversettelse): «HEMLIBRA danner en bro mellom aktivert faktor IX og faktor X for å gjenopprette funksjonen til manglende aktivert faktor VIII, som er nødvendig for effektiv hemostase.» Engelsk originaltekst: "HEMLIBRA bridges activated factor IX and factor X to restore the function of missing activated factor VIII that is needed for effective hemostasis." ([DailyMed: Hemlibra (emicizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2483adba-fab6-4d1b-96c5-c195577ed071), versjon av 2025-07-11; hentet 2026-11-19). Ut fra kjent informasjon er emicizumab et bispesifikt antistoff som binder aktivert faktor IX og faktor X og dermed erstatter kofaktorfunksjonen til faktor VIIIa. Bindingen skjer til de koagulasjonsfaktorene som er målproteiner for legemidlet (F9 og F10).

Pseudo-von Willebrands sykdom er en blodplateforstyrrelse forårsaket av en «gain-of-function»-endring i GP1BA, som gir økt binding av von Willebrand-faktor. Dette er en defekt i blodplater og VWF, ikke en mangel på faktor VIII-kofaktor. Det finnes derfor ingen tydelig mekanistisk begrunnelse for at emicizumab skal virke her, og den høye scoren må ses som en ren modellprediksjon.

## Klinisk studiedokumentasjon

For tiden er ingen relaterte kliniske studier registrert.

## Litteraturdokumentasjon

For tiden er ingen relatert litteratur tilgjengelig for pseudo-von Willebrands sykdom.

## Markedsinformasjon for Norge

<!-- licenses:begin -->

| Godkjenningsnummer | Preparatnavn (EMA) | Virkestoff(er) (EMA, engelsk) | Terapeutisk område (EMA, engelsk) | Status |
|------|------|------|------|------|
| EMEA/H/C/004406 | Hemlibra | emicizumab | Hemophilia A | Gyldig |

Kilde: EMA – Medicines output (sentralt godkjente legemidler til mennesker); preparatnavn, virkestoffer og terapeutisk område er gjengitt i engelsk original. Nasjonale markedsføringstillatelser (DMP) og veterinærpreparater er ikke med i disse dataene.

<!-- licenses:end -->

Markedsstatus i de lokale dataene er «Markedsført». Lisensposten er registrert som én enkelt-ingrediens-godkjenning.

## Sikkerhetsvurderinger

- **Legemiddelinteraksjoner:**
  - **Anti-inhibitor koagulasjonskompleks (aPCC): alvorlig (Major).** Samtidig bruk er forbundet med risiko for trombotisk mikroangiopati og trombose.
  - Antihemofil faktor (rekombinant, human): moderat.
  - Koagulasjonsfaktor VIIa (rekombinant, human): moderat.
- **Farmakologisk binding:** Emicizumab binder koagulasjonsfaktor IX og koagulasjonsfaktor X (ikke en klassifisert interaksjon).

For øvrig sikkerhetsinformasjon, se preparatomtalen.

## Konklusjon og neste steg

**Beslutning: Hold**

**Begrunnelse:**
Prediksjonen for pseudo-von Willebrands sykdom bygger kun på modellscore, uten kliniske studier eller litteratur. Sykdomsmekanismen (blodplate-/VWF-defekt) har ingen klar kobling til emicizumabs virkning, og koagulasjonsfremmende behandling kan i teorien øke trombose­risiko.

**For å gå videre kreves følgende:**
- Prekliniske eller mekanistiske data som viser at emicizumab kan påvirke hemostasen ved GP1BA-relatert sykdom
- Detaljerte data om virkningsmekanisme
- Gjennomgang av preparatomtalen for advarsler og kontraindikasjoner
- En vurdering av trombose­risiko ved bruk i en populasjon med blodplatedefekt

<!-- review:begin log -->

## Kontrollogg

Nedenfor er gjennomgangsloggen for denne siden. Setningen om at data om virkningsmekanismen ikke var tilgjengelige, er erstattet med et utdrag fra den oppgitte offisielle preparatomtalen (med uoffisiell oversettelse); modellprediksjoner, evidensnivåer og konklusjoner er ikke omskrevet.

| Kontrolldato | Punkt | Tiltak | Kilde |
|------|------|------|------|
| 2026-11-19 | Setningen «data om virkningsmekanismen er ikke tilgjengelige» erstattet med utdrag fra amerikansk preparatomtale | Setning om manglende data om virkningsmekanismen erstattet med et utdrag med kilde | [DailyMed: Hemlibra (emicizumab) prescribing information, Genentech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2483adba-fab6-4d1b-96c5-c195577ed071) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

