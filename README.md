# NOTxGNN - Norge: Legemiddelreposisjonering

> 本專案由 **藥提醒科技有限公司**（[yao.care](https://www.yao.care)）開發與維運。
> NOTxGNN 站台：<https://notxgnn.yao.care/>｜產品總覽：<https://www.yao.care/medical/txgnn/>

[![Website](https://img.shields.io/badge/Website-notxgnn.yao.care-blue)](https://notxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Prediksjoner for legemiddelreposisjonering av DMP-godkjente legemidler (Norway) ved bruk av TxGNN-modellen.

## Ansvarsfraskrivelse

- Resultatene av dette prosjektet er kun for forskningsformaal og utgjor ikke medisinsk raadgivning.
- Kandidater for legemiddelreposisjonering krever klinisk validering for bruk.

## Prosjektoversikt

### Rapportstatistikk

| Element | Antall |
|------|------|
| **Legemiddelrapporter** | 444 |
| **Totale prediksjoner** | 2,539,217 |
| **Unike legemidler** | 641 |
| **Unike indikasjoner** | 17,041 |
| **DDI-data** | 302,516 |
| **DFI-data** | 857 |
| **DHI-data** | 35 |
| **DDSI-data** | 8,359 |
| **FHIR-ressurser** | 466 MK / 2,395 CUD |

### Fordeling av evidensnivaaer

| Evidensnivaa | Antall rapporter | Beskrivelse |
|---------|-------|------|
| **L1** | 0 | Flere Fase 3 RCT-er |
| **L2** | 0 | Enkelt RCT eller flere Fase 2 |
| **L3** | 0 | Observasjonelle studier |
| **L4** | 0 | Prekliniske / mekanistiske studier |
| **L5** | 466 | Kun beregningsbasert prediksjon |

### Etter kilde

| Kilde | Prediksjoner |
|------|------|
| DL | 2,536,822 |
| KG + DL | 2,149 |
| KG | 246 |

### Etter tillit

| Tillit | Prediksjoner |
|------|------|
| very_high | 1,688 |
| high | 117,105 |
| medium | 231,216 |
| low | 2,189,208 |

---

## Prediksjonsmetoder

| Metode | Hastighet | Noyaktighet | Krav |
|------|------|--------|----------|
| Kunnskapsgraf | Rask (sekunder) | Lavere | Ingen spesielle krav |
| Dyp laering | Langsom (timer) | Hoyere | Conda + PyTorch + DGL |

### Kunnskapsgraf-metode

```bash
uv run python scripts/run_kg_prediction.py
```

| Metrikk | Verdi |
|------|------|
| DMP Totalt antall legemidler | 1,850 |
| Kartlagt til DrugBank | 1,334 (72.1%) |
| Repositioneringskandidater | 2,395 |

### Dyp laering-metode

```bash
conda activate txgnn
PYTHONPATH=src python -m notxgnn.predict.txgnn_model
```

| Metrikk | Verdi |
|------|------|
| Totale DL-prediksjoner | 1,472,850 |
| Unike legemidler | 641 |
| Unike indikasjoner | 17,041 |

### Scoretolkning

TxGNN-scoren representerer modellens tillit til et legemiddel-sykdomspar, med et intervall fra 0 til 1.

| Terskelverdi | Betydning |
|-----|------|
| >= 0.9 | Svart hoy tillit |
| >= 0.7 | Hoy tillit |
| >= 0.5 | Moderat tillit |

#### Poengfordeling

| Terskelverdi | Betydning |
|-----|------|
| ≥ 0.9999 | Ekstremt hoey tillit, modellens mest sikre prediksjoner |
| ≥ 0.99 | Svart hoey tillit, verdt aa prioritere for validering |
| ≥ 0.9 | Hoey tillit |
| ≥ 0.5 | Moderat tillit (sigmoid-beslutningsgrense) |

#### Definisjoner av evidensnivaaer

| Nivaa | Definisjon | Klinisk betydning |
|-----|------|---------|
| L1 | Fase 3 RCT eller systematisk gjennomgang | Kan stoette klinisk bruk |
| L2 | Fase 2 RCT | Kan vurderes for bruk |
| L3 | Fase 1 eller observasjonsstudie | Krever videre evaluering |
| L4 | Kasusrapport eller preklinisk forskning | Ennaa ikke anbefalt |
| L5 | Kun beregningsbasert prediksjon, ingen klinisk evidens | Krever videre forskning |

#### Viktige paaminnelser

1. **Hoeye poeng garanterer ikke klinisk effektivitet: TxGNN-poeng er kunnskapsgrafbaserte prediksjoner som krever klinisk validering.**
2. **Lave poeng betyr ikke ineffektivt: modellen har kanskje ikke laert visse assosiasjoner.**
3. **Anbefales aa bruke med valideringspipeline: bruk dette prosjektets verktoey for aa gjennomgaa kliniske studier, litteratur og annen evidens.**

### Valideringspipeline

```mermaid
flowchart TD
    A["TxGNN-prediksjonsresultater"] --> B
    subgraph B["Step 1: DrugBundle Collector"]
        B1["Legemiddelnivaa: DMP, DDI, DrugBank"]
        B2["Indikasjonsnivaa: ClinicalTrials, PubMed, ICTRP"]
    end
    B --> |"drug_bundle.json"| C
    subgraph C["Step 2: Evidence Pack Generator"]
        C1["Programmatisk dataoverforing (100%)"]
        C2["+ LLM Analyse (L1-L5)"]
    end
    C --> |"drug_evidence_pack.json/md"| D
    subgraph D["Step 3: Notes Writer"]
        D1["drug_pharmacist_notes.md"]
        D2["drug_sponsor_notes.md"]
    end
```

---

## Hurtigstart

### Trinn 1: Last ned data

| Fil | Nedlasting |
|------|------|
| DMP Data | [EMA Medicines Data (proxy for Norwegian-authorized medicines)](https://www.ema.europa.eu/en/medicines/download-medicine-data) |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) |
| model_ckpt.zip | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) |

### Trinn 2: Installer avhengigheter

```bash
uv sync
```

### Trinn 3: Behandle legemiddeldata

```bash
uv run python scripts/process_fda_data.py
```

### Trinn 4: Forbered vokabulardata

```bash
uv run python scripts/prepare_external_data.py
```

### Trinn 5: Kjoer kunnskapsgraf-prediksjon

```bash
uv run python scripts/run_kg_prediction.py
```

### Trinn 6: Sett opp dyp laering-miljoe

```bash
conda create -n txgnn python=3.11 -y
conda activate txgnn
pip install torch==2.2.2 torchvision==0.17.2
pip install dgl==1.1.3
pip install git+https://github.com/mims-harvard/TxGNN.git
pip install pandas tqdm pyyaml pydantic ogb
```

### Trinn 7: Kjoer dyp laering-prediksjon

```bash
conda activate txgnn
PYTHONPATH=src python -m notxgnn.predict.txgnn_model
```

---

## Ressurser

### TxGNN Kjerne

- [TxGNN Paper](https://www.nature.com/articles/s41591-024-03233-x) - Nature Medicine, 2024
- [TxGNN GitHub](https://github.com/mims-harvard/TxGNN)
- [TxGNN Explorer](http://txgnn.org)

### Datakilder

| Kategori | Data | Kilde | Merknad |
|------|------|------|------|
| **Legemiddeldata** | DMP | [EMA Medicines Data (proxy for Norwegian-authorized medicines)](https://www.ema.europa.eu/en/medicines/download-medicine-data) | Norway |
| **Kunnskapsgraf** | TxGNN KG | [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM) | 17,080 diseases, 7,957 drugs |
| **Legemiddeldatabase** | DrugBank | [DrugBank](https://go.drugbank.com/) | Kartlegging av legemiddelingredienser |
| **Legemiddelinteraksjoner** | DDInter 2.0 | [DDInter](https://ddinter2.scbdd.com/) | DDI-par |
| **Legemiddelinteraksjoner** | Guide to PHARMACOLOGY | [IUPHAR/BPS](https://www.guidetopharmacology.org/) | Godkjente legemiddelinteraksjoner |
| **Kliniske studier** | ClinicalTrials.gov | [CT.gov API v2](https://clinicaltrials.gov/data-api/api) | Register for kliniske studier |
| **Kliniske studier** | WHO ICTRP | [ICTRP API](https://apps.who.int/trialsearch/api/v1/search) | Internasjonal plattform for kliniske studier |
| **Litteratur** | PubMed | [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/) | Medisinsk litteratursok |
| **Navnekartlegging** | RxNorm | [RxNav API](https://rxnav.nlm.nih.gov/REST) | Standardisering av legemiddelnavn |
| **Navnekartlegging** | PubChem | [PUG-REST API](https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest) | Kjemiske stoff-synonymer |
| **Navnekartlegging** | ChEMBL | [ChEMBL API](https://www.ebi.ac.uk/chembl/api/data) | Bioaktivitetsdatabase |
| **Standarder** | FHIR R4 | [HL7 FHIR](http://hl7.org/fhir/) | MedicationKnowledge, ClinicalUseDefinition |
| **Standarder** | SMART on FHIR | [SMART Health IT](https://smarthealthit.org/) | EHR-integrasjon, OAuth 2.0 + PKCE |

### Modellnedlastinger

| Fil | Nedlasting | Merknad |
|------|------|------|
| Fortrent modell | [Google Drive](https://drive.google.com/uc?id=1fxTFkjo2jvmz9k6vesDbCeucQjGRojLj) | model_ckpt.zip |
| node.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144482) | Nodedata |
| kg.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144484) | Kunnskapsgrafdata |
| edges.csv | [Harvard Dataverse](https://dataverse.harvard.edu/api/access/datafile/7144483) | Kantdata (DL) |

## Prosjektintroduksjon

### Katalogstruktur

```
NOTxGNN/
├── README.md
├── CLAUDE.md
├── pyproject.toml
│
├── config/
│   └── fields.yaml
│
├── data/
│   ├── kg.csv
│   ├── node.csv
│   ├── edges.csv
│   ├── raw/
│   ├── external/
│   ├── processed/
│   │   ├── drug_mapping.csv
│   │   ├── repurposing_candidates.csv
│   │   ├── txgnn_dl_predictions.csv.gz
│   │   └── integration_stats.json
│   ├── bundles/
│   └── collected/
│
├── src/notxgnn/
│   ├── data/
│   │   └── loader.py
│   ├── mapping/
│   │   ├── normalizer.py
│   │   ├── drugbank_mapper.py
│   │   └── disease_mapper.py
│   ├── predict/
│   │   ├── repurposing.py
│   │   └── txgnn_model.py
│   ├── collectors/
│   └── paths.py
│
├── scripts/
│   ├── process_fda_data.py
│   ├── prepare_external_data.py
│   ├── run_kg_prediction.py
│   └── integrate_predictions.py
│
├── docs/
│   ├── _drugs/
│   ├── fhir/
│   │   ├── MedicationKnowledge/
│   │   └── ClinicalUseDefinition/
│   └── smart/
│
├── model_ckpt/
└── tests/
```

**Forklaring**: 🔵 Prosjektutvikling | 🟢 Lokale data | 🟡 TxGNN-data | 🟠 Valideringspipeline

### Dataflyt

```mermaid
flowchart TD
    FDA["DMP Data"] --> proc["process_fda_data.py"]
    TxGNN["TxGNN Data"] --> prep["prepare_external_data.py"]

    proc --> json["no_fda_drugs.json"]
    prep --> ext["data/external/"]

    json --> norm["normalizer.py"]
    ext --> norm

    norm --> drug_map["drug_mapping.csv"]
    drug_map --> ind_map["indication_mapping.csv"]

    ind_map --> KG["Kunnskapsgraf"]
    ind_map --> DL["Dyp laering"]

    KG --> kg_out["repurposing_candidates.csv"]
    DL --> dl_out["txgnn_dl_predictions.csv"]
```

---

## Sitering

Hvis du bruker dette datasettet eller programvaren, vennligst siter:

```bibtex
@software{notxgnn2026,
  author       = {Yao.Care},
  title        = {NOTxGNN: Drug Repurposing Validation Reports for Norway DMP Drugs},
  year         = 2026,
  publisher    = {GitHub},
  url          = {https://github.com/yao-care/NOTxGNN}
}
```

Siter ogsaa den originale TxGNN-artikkelen:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and Chandak, Payal and Wang, Qianwen and Haber, Shreyas and Zitnik, Marinka},
  journal={Nature Medicine},
  year={2024},
  doi={10.1038/s41591-024-03233-x}
}
```

<!-- txgnn-ops:start -->
## 維運：資料還原與許可證更新

### 完整還原

git 只放程式碼與網站頁面；許可證原始資料、證據包、藥師報告原稿、預測結果放在本 repo 的 Release。

```bash
git clone https://github.com/yao-care/notxgnn.git && cd notxgnn
uv sync                                  # Python 相依套件
bash scripts/restore_data.sh             # 取最新的 data-* Release，還原 data/（含校驗）
bash scripts/restore_data.sh --with-kg   # 另加共用知識圖譜與預測模型（只有重跑預測才需要）
```

需要 [GitHub CLI](https://cli.github.com/)（`gh auth login`）與 [uv](https://docs.astral.sh/uv/)。

### 改頁工具鏈

事實層、checker、許可證狀態計算等放在 `tools/txgnn/.claude/`，是母 repo `yao-care/txgnn` 的 `.claude/` 複本（版本見 `tools/txgnn/VERSION`）。
規則要改請改母 repo，再用 `python3 .claude/sync_site_tools.py NOTxGNN` 同步過來，不要直接改這裡的複本。
在本 repo 單獨使用時，先組工作目錄：

```bash
WS=$(bash scripts/txgnn_ws.sh)
cd "$WS"
python3 .claude/dump_license_facts_20261021.py NOTxGNN       # 依證據包算市場狀態（checker 要用）
python3 .claude/checker_trend.py --no-append NOTxGNN           # 全部藥物頁 checker，必須「非 0 0」
```

### 許可證排程更新（GitHub Actions）

`.github/workflows/license-refresh.yml` 每週一 UTC 03:17 自動執行，也可以在 Actions 頁手動觸發（可選只試跑）：

1. 從 Release 還原 `data/`（`scripts/restore_data.sh`）
2. 從主管機關下載最新許可證資料（`scripts/license_adapter.py`），檢查筆數與格式
3. 更新證據包的許可證狀態 → 重算市場狀態 → 同步許可證表 → 事實層改頁 → checker 全量必須 0 → 衍生檔 → gate
4. 全部通過才推上 `main` 並觸發部署；更新後的 `data/` 另存成新的 `data-YYYYMMDD` Release

以下情況一律不推、自動開 issue（label `license-refresh`）：下載失敗或格式改變、狀態變動超過兩成、
改到的藥物頁超過 min(200, 5%)、checker／gate／h1 沒過、有人工查核紀錄的頁會被改到。全程不使用 AI。
<!-- txgnn-ops:end -->
