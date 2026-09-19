---
layout: default
title: Albutrepenonacog Alfa
parent: Kun modellprediksjon (L5)
nav_order: 21
evidence_level: L5
indication_count: 6
---

# Albutrepenonacog Alfa
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

# Albutrepenonacog alfa: Fra hemofili B (bakgrunnskunnskap, ubekreftet) til pseudo-von Willebrand-sykdom

## Sammendrag i én setning

Albutrepenonacog alfa er et rekombinant koagulasjonsfaktor-preparat; dens opprinnelig godkjente indikasjon er ikke dokumentert i gjeldende kildedata, selv om farmakologisk bakgrunnskunnskap (også referert i modellens egen begrunnelse) antyder at det fungerer som en **rekombinant faktor IX-erstatningsterapi** for faktor IX-mangel (hemofili B). TxGNN-modellen forutsier at det kan være relevant for **pseudo-von Willebrand-sykdom**, men denne prediksjonen støttes for tiden av **0 kliniske forsøk** og **0 publikasjoner**, og modellens egen mekanistiske begrunnelse beskriver de to tilstandene som virkende på ulike fysiologiske nivåer med **ingen etablert mekanistisk sammenheng**.

---

## Rask oversikt

| Punkt | Innhold |
|-------|---------|
| Opprinnelig indikasjon | Ikke dokumentert i kildedata (datakløft); bakgrunnskunnskap antyder faktor IX-erstatningsterapi for hemofili B — ubekreftet |
| Forutsagt ny indikasjon | Pseudo-von Willebrand-sykdom |
| TxGNN-prediksjonspoengsum | 99.94% (råranking #878 blant alle kandidatsykdommer) |
| Bevisnivå | L5 (modellprediksjon kun, ingen klinisk eller litteraturbevis) |
| Status på norskmarkedet | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Vent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er detaljerte data om virkningsmekanisme ikke tilgjengelig (flagget som et datakløft med høy alvorlighetsgrad i dette bevismateriell). Basert på begrenset bakgrunnsinformasjon i denne pakken, antas albutrepenonacog alfa å være et rekombinant faktor IX-erstatningsprodukt som virker på **sekundær hemostase (koagulasjonsfaktor)-banen**. Denne forutsetningen er ikke bekreftet av en formell MOA-post og bør behandles som ubekreftet til DrugBank/regulatoriske kildedata kan avstemmes.

Den forutsatte nye indikasjonen, pseudo-von Willebrand-sykdom, er en **primær hemostaseforstyrrelse** forårsaket av en gain-of-function-abnormalitet i trombocyttens GpIb-reseptor, som fører til overdreven affinitet for von Willebrand-faktor. Dette er mekanistisk forskjellig fra en koagulasjonsfaktormangel: den ene er en trombocytt-reseptor/bindingsforstyrrelse, den andre er en koagulasjonsfaktormangel. Bevismateriellset er eksplisitt på dette punktet og angir at de to tilstandene «virker på ulike nivåer» og at det er «ingen kjent mekanistisk sammenheng» mellom dem.

Gitt dette, bør prediksjonen leses som en **statistisk assosiasjon som kom fram fra TxGNN-kunnskapsgrafmodellen**, ikke som en mekanistisk eller klinisk validert hypotese. Det høye råprediksjonspoengsumet (99.94%) gjenspeiler modellens interne rangeringskonfidens, ikke ekstern validering — ingen kliniske forsøk, litteratur eller regulatorisk presedens eksisterer for øyeblikket for å korroborere det.

---

## Bevis fra kliniske forsøk

For tiden ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden ingen relevant litteratur tilgjengelig.

---

## Informasjon om norskmarkedet

Albutrepenonacog alfa har for tiden ingen markedsføringstillatelse i Norge (markedsstatus: **ikke markedsført**, 0 lisenser registrert). Ingen produkt-/legemiddelformsinformasjon er tilgjengelig for denne evalueringen.

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon.

*(Merknad: dette bevismateriell flagger fraværet av TFDA-pakningsvedlegg-advarsler/kontraindikasjoner som et **blokkering**-alvorlighetsgrad datakløft — se konklusjon nedenfor. Ingen legemiddel-legemiddel-interaksjonsregistreringer ble funnet i den spørte kilden.)*

---

## Konklusjon og neste steg

**Beslutning: Vent**

**Begrunnelse:**
- Det er ingen klinisk forsøks- eller litteraturbevis som støtter bruk av albutrepenonacog alfa ved pseudo-von Willebrand-sykdom (eller ved noen av de fem andre lavere rangerte forutsette indikasjoner i denne pakken — primær trombocyttvriværelse, Glanzmanns trombasteni, Scott-syndrom, kollagen-reseptor-blødningsdiates og konstitusjonell trombocytopeni), og modellens egen mekanistiske begrunnelse for hver kandidat beskriver den underliggende patofysiologien som forskjellig fra koagulasjonsfaktor-erstatning.
- Et datakløft med **blokkering**-alvorlighetsgrad for TFDA/pakningsvedlegg-sikkerhetsinformasjon (advarsler, kontraindikasjoner) eksisterer, som etter dette programmets egne kriterier hindrer inntreden til S1-sikkerhetsvurdering. Et **høy**-alvorlighetsgrad datakløft eksisterer også for bekreftet virkningsmekanisme.

**For å kunne gå videre er følgende nødvendig:**
- Løse DG001 (Blokkering): skaffe og tolke det offisielle pakningsvedlegget for å etablere viktige advarsler og kontraindikasjoner før noen sikkerhetsvurdering kan begynne.
- Løse DG002 (Høy): bekrefte virkningsmekanisme via DrugBank eller annen autoritativ kilde, siden den nåværende MOA er antatt heller enn bekreftet.
- Bekrefte legemidlets opprinnelig godkjente indikasjon(er), som for tiden er fraværende fra regulatoriske kildedata.
- Hvis denne kandidaten skal fremmes til tross for den svake mekanistiske begrunnelsen, innhent uavhengige prekliniske eller kasuistikk-bevis som kobler faktor IX-veimodulering til trombocytt-formidlet blødningsforstyrrelser som pseudo-von Willebrand-sykdom.

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

