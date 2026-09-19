---
layout: default
title: Enzalutamide
parent: Kun modellprediksjon (L5)
nav_order: 134
evidence_level: L5
indication_count: 7
---

# Enzalutamide
{: .fs-9 }

Evidensnivå: **L5** | Predikerte indikasjoner: **7** stk.
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

# Enzalutamid: Fra kastrasjonsresistent prostatakreft til prostatakreft/hjernekreft-mottakelighet

## Sammendrag i en setning

Enzalutamid er en androgen-reseptor (AR) antagonist fra andre generasjon hvis etablerte indikasjon er kastrasjonsresistent prostatakreft (CRPC); denne spesifikke rollen er beskrevet i evidenspakkens mekanistiske begrunnelse selv om offisielle felter for lisens/MOA er merket som datakløfter.
TxGNN-modellens høyest rangerte prediksjon for dette legemidlet er **prostatakreft/hjernekreft-mottakelighet**, en genetisk-mottakelighetsetikett snarere enn en definert sykdomsenhet.
For øyeblikket **0 kliniske forsøk** og **0 publikasjoner** støtter denne spesifikke prediksjonen, og modellen selv flagger poengsummen som sannsynligvis et artefakt fra kunnskapsgrafs samforekomst snarere enn et genuint mekanistisk signal.

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Original indikasjon | Kastrasjonsresistent prostatakreft (CRPC) — ingen norsk lisenstekst tilgjengelig; legemidlet er globalt godkjent AR-antagonist for denne indikasjonen (iht. mekanistisk begrunnelse i evidenspakke) |
| Predikert ny indikasjon | Prostatakreft/hjernekreft-mottakelighet |
| TxGNN-prediksjonsscore | 99.71% |
| Bevisnivå | L5 |
| Markedsstatus i Norge | ✗ Ikke markedsført |
| Antall godkjennelser | 0 |
| Anbefalt beslutning | Avvent |

## Hvorfor er denne prediksjonen rimelig?

Evidenspakkens `original_moa` felt er merket som en datakløft, men den mekanistiske begrunnelsen knyttet til andre kandidater i samme pakke bekrefter enzalutamids kjente farmakologi: det er en androgen-reseptor antagonist fra andre generasjon som blokkerer testosteron/DHT binding til androgen-reseptoren og hemmer AR nukleær translokalisering og DNA binding — mekanismen som ligger til grunn for dens etablerte bruk i CRPC.

Den høyest rangerte nye etiketten, «prostatakreft/hjernekreft-mottakelighet,» er ikke en distinkt sykdom med en plausibel AR-drevet patofysiologi. Det ser ut til å være en genetisk-predisposisjon-etikett som kombinerer to løst relaterte tilstander. Evidenspakkens egen begrunnelse sier dette eksplisitt: den høye TxGNN-poengsummen stammer sannsynligvis fra at kunnskapsgrafen har «prostatakreft»-noden som forekommer sammen med «hjernekreft»-noden, snarere enn at den reflekterer noen reell biologisk forbindelse til enzalutamids AR-blokkerende mekanisme.

Fordi det ikke finnes uavhengig AR-bane-bevis for hjernekreft-mottakelighet, og ingen klinisk eller litteraturdata støtter denne pairingen, er den mekanistiske saken for ombruk mot denne etiketten svak. Den bør behandles som modellstøy som venter på ytterligere validering, ikke som en genuint ombruk-hypotese.

## Klinisk forsøks-bevis

For øyeblikket ingen relaterte kliniske forsøk registrert.

## Litteratur-bevis

For øyeblikket ingen relatert litteratur tilgjengelig.

## Markedsinformasjon for Norge

Enzalutamid er for øyeblikket **ikke markedsført** i Norge (0 godkjennelser); ingen lisens, doseringsform eller godkjent indikasjon data er tilgjengelig for dette markedet.

## Cytotoksisitet

| Element | Innhold |
|---------|---------|
| Cytotoksisitet klassifisering | Målrettet terapi (hemmer av androgen-reseptor-signalering) — ikke et konvensjonelt cytotoksisk kjemoterapi-middel |
| Myelosuppresjon risiko | Vennligst se pakningsvedleggets advarsler og forholdsregler |
| Emetogenisitet klassifisering | Vennligst se pakningsvedleggets advarsler og forholdsregler |
| Overvåkings elementer | Vennligst se pakningsvedleggets advarsler og forholdsregler |
| Håndteringsbeskyttelse | Vennligst se pakningsvedleggets advarsler og forholdsregler |

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. (Merk: TFDA/produsent advarsel og kontraindikasjon data mangler for øyeblikket — flagget som en blokkerende datakløft som må løses før noen sikkerhetspre-vurdering kan fortsette.)

## Konklusjon og neste skritt

**Beslutning: Avvent**

**Begrunnelse:**
Den høyest rangerte prediksjonen («prostatakreft/hjernekreft-mottakelighet») har ingen støttende kliniske forsøk eller litteratur (Bevisnivå L5), og dens egen mekanistiske begrunnelse identifiserer poengsummen som et sannsynlig kunnskapsgrafs-artefakt snarere enn et reelt AR-bane-drevet signal.

**For å fortsette, kreves følgende:**
- TFDA pakningsvedlegg (advarsler/kontraindikasjoner) — for øyeblikket en blokkerende datakløft
- Formell MOA dokumentasjon fra DrugBank — for øyeblikket en høy-alvorlighets datakløft
- Uavhengig preklinisk eller klinisk bevis som knytter AR antagonisme til hjernekreft-mottakelighet, dersom denne kandidaten skal forfølges videre
- Vurder omfangsendring av evalueringen mot bedre-evidensierte kandidater allerede til stede i dette datasettet, f.eks. «godartet neoplasi i reproduktivt system» (L4, Forskningsspørsmål) eller legemidlets egen kjerne CRPC-indikasjon (L1, selv om ikke en ny ombruk-sak)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

