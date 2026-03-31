# NOTxGNN - Norge: Repositionering av Legemidler

[![Website](https://img.shields.io/badge/Website-notxgnn.yao.care-blue)](https://notxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Prediksjoner for repositionering av legemidler (drug repurposing) for Norge ved hjelp av TxGNN-modellen.

## Ansvarsfraskrivelse

- Resultatene fra dette prosjektet er kun til forskningsformaal og utgjor ikke medisinsk raadgivning.
- Kandidater for repositionering av legemidler krever klinisk validering for bruk.

## Prosjektoversikt

| Element | Antall |
|---------|--------|
| **Legemiddelrapporter** | 466 |
| **Totale Prediksjoner** | 2,539,217 |

## Prediksjonsmetoder

### Kunnskapsgrafmetode (Knowledge Graph)
Direkte soek etter legemiddel-sykdomsrelasjoner i TxGNN-kunnskapsgrafen, identifisering av potensielle repositioneringskandidater basert paa eksisterende forbindelser i det biomedisinske nettverket.

### Dyp laeringsmetode (Deep Learning)
Bruker den forhaandstrente TxGNN nevrale nettverksmodellen til aa beregne prediksjonsscore, og vurderer sannsynligheten for nye terapeutiske indikasjoner for godkjente legemidler.

## Lenker

- Nettsted: https://notxgnn.yao.care
- TxGNN-artikkel: https://doi.org/10.1038/s41591-023-02233-x
