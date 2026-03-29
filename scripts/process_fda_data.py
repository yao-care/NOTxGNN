#!/usr/bin/env python3
"""處理挪威 DMP / EMA 藥品資料

由於 FEST (Forskrivnings- og ekspedisjonsstøtte) 僅提供 SOAP/WCF web service，
無穩定的批量靜態檔案下載，改用 EMA Medicines Report 作為資料來源。
挪威為 EEA 成員國，EMA 集中授權藥品在挪威有效。

使用方法:
    uv run python scripts/process_fda_data.py

資料來源:
    主要: EMA Medicines Report (集中授權藥品，含挪威)
          https://www.ema.europa.eu/en/documents/report/medicines-output-medicines-report_en.xlsx
    備用: EMA Article 57 Database (全 EEA 已授權藥品)
          https://www.ema.europa.eu/en/documents/other/article-57-product-data_en.xlsx
    參考: FEST SOAP Service (複雜，需 WCF 客戶端)
          https://fest.legemiddelverket.no/Fest/FestService251.svc
    參考: DMP Legemiddelsøk (僅網頁查詢)
          https://www.legemiddelsok.no/

產生檔案:
    data/raw/no_fda_drugs.json
"""

import json
from pathlib import Path

import pandas as pd
import requests
import yaml


def load_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def download_ema_data(output_path: Path) -> Path:
    """從 EMA 下載藥品資料 Excel

    嘗試兩個 EMA 資料來源：
      1. Medicines Report: 集中授權程序的藥品清單 (~880 KB)
      2. Article 57 Database: 全 EEA 已授權藥品 (~7.7 MB)

    Args:
        output_path: Excel 輸出路徑

    Returns:
        下載的檔案路徑
    """
    config = load_config()
    ds = config["data_source"]
    download_urls = ds.get("download_urls", [])

    if not download_urls:
        download_urls = [ds.get("url", "")]

    for url_entry in download_urls:
        if isinstance(url_entry, dict):
            url = url_entry["url"]
            name = url_entry.get("name", url)
        else:
            url = url_entry
            name = url

        if not url:
            continue

        print(f"正在下載: {name}")
        print(f"URL: {url}")

        try:
            response = requests.get(url, timeout=180, headers={
                "User-Agent": "Mozilla/5.0 (compatible; TxGNN/1.0; research)",
            })
            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            if "html" in content_type.lower():
                print(f"  返回 HTML 頁面而非 Excel，跳過")
                continue

            # 根據 URL 決定檔名
            if "article-57" in url:
                actual_path = output_path.parent / "ema_article57_product_data.xlsx"
            elif "medicines-report" in url:
                actual_path = output_path.parent / "ema_medicines_report.xlsx"
            else:
                actual_path = output_path

            actual_path.parent.mkdir(parents=True, exist_ok=True)
            with open(actual_path, "wb") as f:
                f.write(response.content)

            size_mb = actual_path.stat().st_size / 1024 / 1024
            print(f"  下載完成: {actual_path}")
            print(f"  檔案大小: {size_mb:.1f} MB")

            if size_mb < 0.01:
                print(f"  檔案過小，跳過")
                actual_path.unlink(missing_ok=True)
                continue

            return actual_path

        except requests.RequestException as e:
            print(f"  下載失敗: {e}")
            continue

    raise FileNotFoundError(
        f"無法自動下載 EMA 藥品資料\n\n"
        f"請手動取得資料：\n\n"
        f"方法 A: EMA Medicines Report (推薦，集中授權程序藥品)\n"
        f"  1. 前往 https://www.ema.europa.eu/en/medicines/download-medicine-data\n"
        f"  2. 下載 'Medicines' 資料表 (.xlsx)\n"
        f"  3. 將檔案放置於: {output_path.parent}/ema_medicines_report.xlsx\n\n"
        f"方法 B: EMA Article 57 Database (全 EEA 已授權藥品)\n"
        f"  1. 前往上述頁面\n"
        f"  2. 下載 Article 57 Product Data Excel\n"
        f"  3. 將檔案放置於: {output_path.parent}/ema_article57_product_data.xlsx\n\n"
        f"方法 C: FEST SOAP Service (進階，需 WCF 客戶端)\n"
        f"  1. 前往 https://www.dmp.no/om-oss/distribusjon-av-legemiddeldata/fest\n"
        f"  2. 使用 GetM30 SOAP 方法取得 FEST XML\n"
        f"  3. 將 XML 檔案放至 {output_path.parent}/\n\n"
        f"支援格式: .xlsx, .xls, .csv, .json"
    )


def find_data_file(raw_dir: Path) -> Path | None:
    """在 raw 目錄中尋找已存在的資料檔案

    Args:
        raw_dir: data/raw/ 目錄路徑

    Returns:
        找到的資料檔案路徑，或 None
    """
    # 嘗試常見檔名 (按優先順序)
    candidates = [
        raw_dir / "ema_medicines_report.xlsx",
        raw_dir / "ema_article57_product_data.xlsx",
        raw_dir / "fest.csv",
        raw_dir / "fest.json",
        raw_dir / "legemiddelsok_export.csv",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    # 搜尋任何資料檔案
    for pattern in ["ema*.xlsx", "*.csv", "*.json", "*.xlsx", "*.xls"]:
        files = list(raw_dir.glob(pattern))
        if files:
            return files[0]

    return None


def process_data_file(input_path: Path, output_path: Path) -> Path:
    """處理資料檔案並轉換為 JSON

    支援 CSV、JSON、XLSX 格式。
    針對 EMA 資料進行特殊處理（篩選挪威適用的記錄）。

    Args:
        input_path: 輸入檔案路徑
        output_path: JSON 輸出路徑

    Returns:
        輸出檔案路徑
    """
    config = load_config()
    encoding = config.get("encoding", "utf-8")

    print(f"讀取資料檔案: {input_path}")
    print(f"檔案大小: {input_path.stat().st_size / 1024 / 1024:.1f} MB")

    suffix = input_path.suffix.lower()
    is_ema = "ema" in input_path.name.lower() or "article" in input_path.name.lower()

    if suffix == ".csv":
        try:
            df = pd.read_csv(input_path, encoding=encoding, sep=";", dtype=str, on_bad_lines="skip")
            if len(df.columns) <= 1:
                raise ValueError("Wrong delimiter")
        except (ValueError, Exception):
            try:
                df = pd.read_csv(input_path, encoding=encoding, sep=",", dtype=str, on_bad_lines="skip")
            except UnicodeDecodeError:
                df = pd.read_csv(input_path, encoding="latin-1", sep=";", dtype=str, on_bad_lines="skip")

    elif suffix == ".json":
        with open(input_path, "r", encoding=encoding) as f:
            data = json.load(f)
        df = pd.DataFrame(data)

    elif suffix in (".xlsx", ".xls"):
        try:
            # EMA XLSX 前幾列為元資料，自動偵測表頭列
            df_probe = pd.read_excel(
                input_path, engine="openpyxl", dtype=str, sheet_name=0, header=None, nrows=15,
            )
            header_row = 0
            for i in range(min(15, len(df_probe))):
                row_vals = df_probe.iloc[i].astype(str).str.cat()
                if "Category" in row_vals and "Name of medicine" in row_vals:
                    header_row = i
                    print(f"  偵測到 EMA 表頭列: row {header_row}")
                    break
                if "Authorisation" in row_vals and "Active substance" in row_vals:
                    header_row = i
                    print(f"  偵測到 EMA 表頭列: row {header_row}")
                    break

            df = pd.read_excel(input_path, engine="openpyxl", dtype=str, sheet_name=0, header=header_row)

            # 清理多行欄位名稱
            df.columns = [c.strip().split("\n")[0].strip() for c in df.columns]

            # 移除全空白列
            df = df.dropna(how="all")
        except Exception:
            df = pd.read_excel(input_path, dtype=str, sheet_name=0)

    else:
        raise ValueError(f"不支援的檔案格式: {suffix}")

    print(f"原始資料筆數: {len(df)}")
    print(f"欄位: {', '.join(df.columns.tolist())}")

    # 若為 EMA 資料，篩選人用已授權藥品
    if is_ema:
        df = _filter_ema_for_norway(df)

    # 清理資料
    df = df.fillna("")

    # 轉換為 JSON
    data = df.to_dict(orient="records")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"儲存至: {output_path}")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"完成！共 {len(data)} 筆藥品資料")

    # 顯示統計
    print_statistics(df, config)

    return output_path


def _filter_ema_for_norway(df: pd.DataFrame) -> pd.DataFrame:
    """從 EMA 資料中篩選挪威適用的記錄

    EMA Medicines Report 為集中授權，在所有 EU/EEA 成員國有效（含挪威）。
    Article 57 資料包含 'Country' 欄位可篩選。

    Args:
        df: EMA 原始 DataFrame

    Returns:
        篩選後的 DataFrame
    """
    # 篩選人用藥品
    if "Category" in df.columns:
        human_mask = df["Category"] == "Human"
        human_count = human_mask.sum()
        print(f"\n篩選人用藥品: {human_count:,} / {len(df):,}")
        df = df[human_mask].copy()

    # 篩選已授權藥品
    if "Medicine status" in df.columns:
        auth_mask = df["Medicine status"] == "Authorised"
        auth_count = auth_mask.sum()
        print(f"篩選已授權藥品: {auth_count:,} / {len(df):,}")
        df = df[auth_mask].copy()

    # 嘗試找到國家欄位（Article 57 有此欄位）
    country_cols = [
        col for col in df.columns
        if "country" in col.lower()
    ]

    if country_cols:
        country_col = country_cols[0]
        print(f"\n找到國家欄位: '{country_col}'")

        no_mask = df[country_col].str.contains(
            r"Norway|Norge|NO\b",
            case=False, na=False, regex=True,
        )
        no_count = no_mask.sum()
        print(f"挪威相關記錄: {no_count:,} / {len(df):,}")

        if no_count > 0:
            df = df[no_mask].copy()
            print(f"已篩選為挪威記錄: {len(df):,} 筆")
        else:
            print("未找到挪威特定記錄，保留所有記錄")
            print("(EMA 集中授權藥品在所有 EU/EEA 成員國有效)")
    else:
        print("\n未找到國家欄位 - EMA 集中授權藥品在所有 EU/EEA 成員國有效")
        print(f"保留全部 {len(df):,} 筆記錄")

    return df


def print_statistics(df: pd.DataFrame, config: dict):
    """印出資料統計"""
    fm = config["field_mapping"]
    status_field = fm["status"]
    ingredients_field = fm["ingredients"]

    print("\n" + "=" * 50)
    print("資料統計")
    print("=" * 50)

    if status_field and status_field in df.columns:
        print(f"\n授權狀態分布:")
        status_counts = df[status_field].value_counts()
        for status, count in status_counts.items():
            print(f"  {status}: {count:,}")
    else:
        status_like = [c for c in df.columns if "status" in c.lower() or "authoris" in c.lower()]
        if status_like:
            col = status_like[0]
            print(f"\n使用 '{col}' 作為狀態欄位:")
            status_counts = df[col].value_counts().head(10)
            for status, count in status_counts.items():
                print(f"  {status}: {count:,}")

    if ingredients_field and ingredients_field in df.columns:
        with_ingredients = (df[ingredients_field] != "").sum()
        if len(df) > 0:
            print(f"\n有活性成分: {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")
    else:
        ing_like = [
            c for c in df.columns
            if "active" in c.lower() or "substance" in c.lower()
            or "ingredient" in c.lower()
        ]
        if ing_like:
            col = ing_like[0]
            with_ingredients = (df[col].fillna("") != "").sum()
            if len(df) > 0:
                print(f"\n有活性成分 ('{col}'): {with_ingredients:,} ({with_ingredients/len(df)*100:.1f}%)")


def main():
    print("=" * 60)
    print("處理挪威 DMP / EMA 藥品資料")
    print("=" * 60)
    print()
    print("注意: FEST 僅提供 SOAP/WCF web service，無穩定批量下載。")
    print("使用 EMA 資料作為替代來源 (集中授權藥品在挪威有效)。")
    print()

    base_dir = Path(__file__).parent.parent
    raw_dir = base_dir / "data" / "raw"
    output_path = raw_dir / "no_fda_drugs.json"

    # 確保 raw 目錄存在
    raw_dir.mkdir(parents=True, exist_ok=True)

    # 尋找已存在的資料檔案
    existing = find_data_file(raw_dir)
    if existing:
        print(f"使用已存在的資料檔案: {existing}")
        data_path = existing
    else:
        # 自動從 EMA 下載
        default_path = raw_dir / "ema_medicines_report.xlsx"
        data_path = download_ema_data(default_path)

    # 處理資料
    process_data_file(data_path, output_path)

    print()
    print("下一步: 準備詞彙表資料")
    print("  uv run python scripts/prepare_external_data.py")


if __name__ == "__main__":
    main()
