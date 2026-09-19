---
layout: default
title: Trabectedin
parent: Høy evidens (L1-L2)
nav_order: 366
evidence_level: L2
indication_count: 1
---

# Trabectedin
{: .fs-9 }

Evidensnivå: **L2** | Predikerte indikasjoner: **1** stk.
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

# Trabectedin: Fra myktvevsarkom/eggstokkreft til brystkreft hos kvinner

## Sammendrag i én setning

> Trabectedin er et marinestammet cytotoksisk middel som for tiden brukes internasjonalt til avansert myktvevsarkom og, i kombinasjon med pegylert liposomalt doksirubicin (PLD), til platinasensitiv tilbakevendende eggstokkreft.
> TxGNN-modellen forutsier at det også kan være effektivt for **brystkreft hos kvinner**, særlig ved BRCA1/2-mutasjoner eller homolog-rekombinasjondefekte tumorer,
> med **2 registrerte kliniske studier** og **20 publikasjoner** som for tiden er identifisert, inkludert to tidligfase-brystkreftstudier.
> Legemidlet er **ikke for tiden markedsført i Norge**, og flere sikkerhetsdatafelter gjenstår uløst.

---

## Rask oversikt

| Element | Innhold |
|---------|---------|
| Opprinnelig indikasjon | Ingen norsk godkjenning på arkiv (legemidlet er ikke markedsført). I henhold til internasjonal litteratur er trabectedin godkjent i EU for annen linjers myktvevsarkom og, kombinert med PLD, for platinasensitiv tilbakevendende eggstokkreft. |
| Forutsagt ny indikasjon | Brystkreft hos kvinner |
| TxGNN-prediksjonspoengsum | 99.73% (rang 3480) |
| Bevisnivå | L2 |
| Norsk markedsstatus | ✗ Ikke markedsført |
| Antall godkjenninger | 0 |
| Anbefalt beslutning | Opphold |

---

## Hvorfor er denne prediksjonen rimelig?

Detaljerte data om virkningsmekanisme er ikke tilgjengelig i denne bevisorienterte pakken (flagget som et datakløft med høy alvorlighetsgrad). Basert på publisert farmakologlitteratur er trabectedin en marinestammet DNA-alkylator som binder seg til mindre groover og foretrekker GC-rike sekvenser, og som forstyrrer transkripsjonsutløst nukleotidekskisjonsreparasjon (TC-NER). Dette gir selektiv cytotoksisitet i tumorer med nukleotidekskisjonreparasjon (NER) eller homolog-rekombinasjon (HR)-mangler — særlig *BRCA1/2*-muterte celler — og modulerer separat tumorumgivelsen ved å danne tumortilknyttede makrofager.

Denne mekanismen strekker seg rimeligvis fra sarkom og eggstokkreft til brystkreft fordi en betydelig andel av brysttumorer, spesielt trippel-negative og arvelige *BRCA1/2*-muterte tilfeller, deler samme HR-defekte (syntetisk-letale) biologi som ligger til grunn for trabectedins virksomhet ved eggstokkreft. Flere identifiserte studier og publikasjoner tester direkte denne hypotesen, inkludert en fase II-studie begrenset til germlinale *BRCA1/2*-muterte metastatisk brystkreft og en olaribmaintenance-studie etter trabectedin+PLD-respons, som styrker den mekanistiske begrunnelsen for TxGNN-prediksjonen snarere enn å etablere den som et nytt, uforklarlig signal.

Det bør bemerkes at den rapporterte *BRCA*/HR-bane-begrunnelsen ovenfor er hentet fra ekstern litteratur, ikke fra det strukturerte `original_moa`-feltet, som forblir et datakløft i denne bevisorienterte pakken.

---

## Klinisk prøvebevis

| Studienummer | Fase | Status | Registrering | Hovedfunn |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Fase 2 | Gjennomført | 76 | Enkeltblind, multicenter, placebokontrollert, sekvensielt designet studie som evaluerer trabectedins effekt på QT/QTc-intervall hos pasienter med avanserte solide tumormaligniteter (hjertesikkerhetsstudie, ikke brystkrefteffikasitet). |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Fase 2 | Gjennomført | 9 | Olaribmaintenance-terapi etter respons på trabectedin + pegylert liposomalt doksirubicin ved tilbakevendende eggstokkarsinomer; tester BRCA/HR-deficiency-begrunnelsen relevant for brystkreft, men ekstremt lite utvalg (n=9). |

---

## Litteraturbevis

| PMID | År | Type | Journal | Hovedfunn |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Fase 2 RCT | Clinical Breast Cancer | Multicenter, randomisert fase II-studie av monoterapi-trabectedin ved avansert brystkreft etter antrasykklin/taksane-svikt, som sammenligner to administreringssystemer. |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Fase 2 | Ann Oncol | First-in-class fase II-studie av trabectedin ved germlinale *BRCA1/2*-muterte metastatisk brystkreft; direkte klinisk støtte for HR-deficiency-mekanistisk sammenheng. |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Fase 2 | Clinical Breast Cancer | Fase 2-studie av trabectedin ved HR-positiv, HER2-negativ avansert brystkreft stratifisert etter XPG-genekspresjon som prediktivt biomarkør. |
| [25722380](https://pubmed.ncbi.nlm.nih.gov/25722380/) | 2015 | Fase 3 (utforskende) | Ann Oncol | Utforskende analyse av fase 3 OVA-301-studien som viser at *BRCA1*/XPG-mutasjonsstatus forutsier respons på trabectedin + PLD, og støtter den biomarkør-drevne begrunnelsen. |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preklinisk | Cancer Immunol Res | Trabectedin reduserer immunosuppressive myeloidceller og forsterker IL-12-drevet NK-cellecytotoksisitet i trippel-negative brystkreftsmodeller. |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Oversikt | Expert Opin Investig Drugs | Gjennomgår trabectedins undersøkelsesbruk ved brystkreft, inkludert dets tosidede cytotoksiske og tumorumgivelsesmodul mekanismer. |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Oversikt | Cancer Treat Rev | Diskuterer trabectedin som et kjemoterapialternativ spesielt for pasienter med BRCA-mangel på tvers av tumortyper. |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preklinisk | Toxicology Letters | Trabectedin induserer apoptose via distinkte baner i HER2-/ER+ (MCF-7) og HER2+/ER- (MDA-MB-453) brystkrefscellelines. |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preklinisk | Eur Cytokine Netw | Demonstrerer anti-angiogene effekter av trabectedin i humane brystkrefscellelines og endothelceller. |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Fase 1 | Eur J Cancer | Fase I farmakokinetisk studie av trabectedin pluss doksirubicin ved avansert myktvevsarkom og brystkreft (blandet populasjon, mulighetsdata). |

---

## Norsk markedsinformasjon

Trabectedin har for tiden **ingen markedsføringsgodkjenning i Norge** (0 lisenser på arkiv). Ingen doseringsformer eller godkjenningsnumre er tilgjengelige for uttak.

---

## Cytotoksisitet

| Element | Innhold |
|---------|---------|
| Cytotoksisitet-klassifisering | Konvensjonell cytotoksisk — marinestammet DNA-minor-groove-alkylator (tetrahydroisokinolin-alkaloid), forstyrrer transkripsjonsutløst DNA-reparasjon |
| Risiko for benmargssuppresjon | Høy — litteratur (PMID 19496709) rapporterer grad 3–4 nøytropeni hos ~50% og trombocytopeni hos ~20% av pasientene; hepatisk transaminaseelevering er også vanlig |
| Emetogenisitet-klassifisering | Moderat (basert på generell onkologilitteratur for trabectedin; ikke bekreftet mot norsk/lokalt pakningsvedlegg, som for tiden er et datakløft) |
| Overvåkingselementer | CBC med differensial, leverfunksjonstester (AST/ALT/bilirubin), nyrufunksjon, kreatinkinase |
| Håndteringsbeskyttelse | Ja — må følge standardprotokoll for håndtering og avfallshåndtering av cytotoksiske stoffer (IV-infusjon, lukket-systemoverføring der tilgjengelig) |

---

## Sikkerhetshensyn

Formelle sikkerhetsdata (viktige advarsler, kontraindikasjoner, legemiddel-legemiddel-interaksjoner) er ennå ikke tilgjengelig for denne kandidaten — dette er flagget som et **blokkerende** datakløft (DG001: TFDA/lokale etikettvarsler og kontraindikasjoner under behandling). Vennligst se pakningsvedlegget når det er tilgjengelig for definitive sikkerhetsinformasjoner.

---

## Konklusjon og neste skritt

**Beslutning: Opphold**

**Begrunnelse:**
Den mekanistiske begrunnelsen (HR/BRCA-mangel syntetisk lethality) er biologisk forsvarlig og støttet av tidligfase-kliniske data, men beviset for brystkreft spesifikt forblir begrenset til små, enkeltarmede eller biomarkør-stratifiserte fase II-studier (største brystkrefftspesifikk kohort: bevis-for-konsept skala). Kombinert med legemidlets ikke-markedsført status i Norge og et **blokkerende** sikkerhetsdatakløft (ingen TFDA/lokale advarsler eller kontraindikasjoner på arkiv), er denne kandidaten ikke ennå klar for evaluering av indikasjoneutvidelse.

**For å fortsette er følgende nødvendig:**
- Løs DG001 (blokkerende): få TFDA/lokalt pakningsvedlegg med advarsler og kontraindikasjoner
- Løs DG002 (høy): bekreft opprinnelig virkningsmekanisme fra DrugBank API for å validere den mekanistiske begrunnelsen presentert her
- Større, randomiserte brystkrefftspesifikke prøvedata, ideelt utberedt for BRCA1/2-muterte eller HR-defekte populasjoner
- Vurdering av gjennomførbarhet for norsk markedsintroduksjon, siden legemidlet for tiden ikke har noen lokal godkjenning

## Ansvarsfraskrivelse

Dette innholdet er kun til forskningsformål og utgjør ikke medisinsk rådgivning.
Klinisk validering kreves før enhver klinisk anvendelse.

---

