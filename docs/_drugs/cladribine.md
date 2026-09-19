---
layout: default
title: Cladribine
parent: Kun modellprediksjon (L5)
nav_order: 88
evidence_level: L5
indication_count: 7
---

# Cladribine
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

# Cladribin: Fra hårcelleleukemi til parameningeal embryonal rabdomyosarkom

## Oppsummering i en setning

Cladribin er en purinkinukleosidanalolog (deoksyadenosin) opprinnelig etablert for **hårcelleleukemi** og **multippel sklerose**. TxGNN-modellen forutsier at det kan være effektivt for **parameningeal embryonal rabdomyosarkom**, men dette er for tiden støttet av **null kliniske forsøk** og **null publikasjoner** — prediksjonen hviler helt og holdent på modellens grafbaserte poengsum.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Hårcelleleukemi; Multippel sklerose (basert på kjent legemiddelklasseprofil — ikke avledet fra Taiwan-lisensdata, da legemidlet ikke er markedsført der) |
| Forutsagt ny indikasjon | Parameningeal embryonal rabdomyosarkom |
| TxGNN-prediksjonspoengsum | 99.77% |
| Bevisnivå | L5 (bare modellprediksjon, ingen støttestudier) |
| Taiwan markedsstatus | Ikke markedsført (Ikke markedsført) |
| Antall autorisasjoner | 0 |
| Anbefalt beslutning | Vent |

---

## Hvorfor er denne prediksjonen rimelig?

For tiden er en offisiell virkningsmekanisme-registrering fra DrugBank ikke tilgjengelig (datakløft DG002). Basert på legemiddelprofi len innebygd i bevisspakken er cladribin en deoksyadenosinanalolog som, etter intracellulær fosforyling, motstår adenosindeaminase-nedbrytning, inkorporeres i DNA og forårsaker strengbrudd som hemmer DNA-syntese og -reparasjon. Denne brede cytotoksiske mekanismen ligger til grunn for dens godkjente bruk ved hårcelleleukemi og dens immunomodulerende bruk ved multippel sklerose.

Hårcelleleukemi og rabdomyosarkom er begge maligne tumorer av raskt delende celler, så et generisk «cytotoksiske legemidler kan undertrykke prolifererande tumorsoller»-argument er mekanistisk plausibelt. Imidlertid er det **ingen rabdomyosarkom-spesifikk mekanistisk kobling** — ingen forbindelse til veiene som faktisk driver denne pediatriske solide tumoren (f.eks. PAX3/PAX7–FOXO1-fusjon i alveoløre subtyper, RAS-veiendringer i embryonale subtyper). Begrunnelsen er en klassenivåekstrapolering, ikke en målbasert hypotese.

Det er bemerkelsesverdig at denne kandidatens forutsagte-indikasjonsliste (ranger 1–6) består nesten utelukkende av rabdomyosarkom-anatomi/histologi-subtyper med nesten identiske poengsum (99.69%–99.77%), noe som foreslår at TxGNN har identifisert en bred «rabdomyosarkom»-kluster i kunnskapsgrafen snarere enn et subtypespesifikt signal. Den ene litteraturreferansen som ble hentet for rang 7 (leveresarkom) er en kasuistikk om cladribin for smoldrende systemisk mastocytose — ikke relatert til leveresarkom — og er best behandlet som en **falskt-positiv gjenfinning**, ikke støttebevis.

---

## Klinisk forsøksbevis

For tiden er ingen relaterte kliniske forsøk registrert.

---

## Litteraturbevis

For tiden er ingen relatert litteratur tilgjengelig.

*(Merk: en litteraturregistrering ble hentet annet sted i denne kandidatens bevisspakke — PMID [15241520](https://pubmed.ncbi.nlm.nih.gov/15241520/), en kasuistikk fra 2004 om cladribin for systemisk mastocytose, vedlagt *leveresarkom*-prediksjon, rang 7. Den adresserer ikke rabdomyosarkom og telles ikke som støttebevis for den høyeste rangerte indikasjon.)*

---

## Taiwan markedsinformasjon

Cladribin er for tiden ikke markedsført i Taiwan (0 autorisasjoner); ingen produktlisensregistreringer er tilgjengelige for visning.

---

## Cytotoksisitet

| Element | Innhold |
|---------|---------|
| Cytotoksisitetsklassifisering | Konvensjonell cytotoksisk (purinkinukleosid-/antimetabolitanalolog) |
| Myelosuppresjonrisiko | Høy — purinanalogene, og cladribin særlig, er forbundet med betydelig og ofte langvarig myelosuppresjon (særlig alvorlig lymfopeni); dette gjenspeiler den etablerte klasseprofi len, ettersom kvantitativ TFDA/DrugBank-toksisitetsdata ikke er tilgjengelig i denne bevisspakken (se DG001) |
| Emetogenisitetsklassifisering | Lav til moderat (i samsvar med purinanalogklassen; spesifikk TFDA-emetogenisitetsdata ikke tilgjengelig — se DG001) |
| Overvåkingselementer | CBC med differensial (særlig lymfocyttkellinger), infeksjonsovervåking, nyre- og leverfunksjon |
| Håndteringsbeskyttelse | Ja — forholdsregler for håndtering av cytotoksiske legemidler gjelder |

---

## Sikkerhetshensyn

Vennligst se pakningsvedlegget for sikkerhetsinformasjon. Viktige advarsler, kontraindikasjoner og legemiddelinteraksjondata er for tiden ikke tilgjengelige i denne bevisspakken (datakløft DG001, sperret alvorlighetsgrad).

---

## Konklusjon og neste steg

**Beslutning: Vent**

**Begrunnelse:**
Toppprediksjonen har null støtte fra kliniske forsøk eller litteratur og ligger på bevisnivå L5 (bare modellpoengsum), uten rabdomyosarkom-spesifikk mekanistisk begrunnelse. TFDA-sikkerhetdata som kreves selv for en foreløpig S1-sikkerhetsgransking, mangler (DG001, sperret), og legemidlet er for tiden ikke markedsført i Taiwan.

**For å gå videre, er det følgende nødvendig:**
- TFDA-pakningsvedlegg (advarsler/kontraindikasjoner) — nødvendig for å rydde det sperrede gapet DG001 før noen sikkerhetsgransking
- Bekreftet DrugBank virkningsmekanisme-registrering (DG002)
- Preklinisk (cellinje-/dyremodell) eller klinisk bevis spesifikk for rabdomyosarkom, som ideelt sett adresserer embryonal-subtypbiologi
- Ny verifisering av rang 7-litteraturtreffet (PMID 15241520), som ser ut til å være en irrelevant gjenfinning og bør utelukkes eller korrigeres
- Vurdering av administrasjonsvei- og formuleringskompabilitet (for tiden merket «ventende» for alle rangerte indikasjoner)

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

