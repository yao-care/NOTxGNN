"""DMP 藥品資料載入與過濾

載入挪威 DMP/FEST 藥品註冊資料。
"""

import json
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_config() -> dict:
    """載入欄位映射設定

    Returns:
        設定字典
    """
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入挪威 DMP 藥品資料

    Args:
        filepath: JSON 檔案路徑，預設為 data/raw/no_fda_drugs.json

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到 DMP 資料檔案時，提供下載指引
    """
    if filepath is None:
        # loader.py -> data -> notxgnn -> src -> NOTxGNN
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "no_fda_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到 DMP 藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 執行: uv run python scripts/process_fda_data.py\n"
            f"   (腳本會從 FEST 下載 XML 資料)"
        )

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品（排除已註銷）

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有效藥品的 DataFrame
    """
    config = load_config()
    status_field = config["field_mapping"]["status"]
    ingredients_field = config["field_mapping"]["ingredients"]
    withdrawn_statuses = config.get("withdrawn_statuses", [])

    # 過濾未註銷的藥品
    if status_field and status_field in df.columns:
        active = df[~df[status_field].isin(withdrawn_statuses)].copy()
    else:
        active = df.copy()

    # 過濾有主成分的藥品（TxGNN 需要）
    if ingredients_field and ingredients_field in df.columns:
        active = active[active[ingredients_field].notna() & (active[ingredients_field] != "")]

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    config = load_config()
    fm = config["field_mapping"]

    ingredients_field = fm["ingredients"]
    indication_field = fm["indication"]
    dosage_form_field = fm["dosage_form"]

    result = {
        "total_count": len(df),
        "with_ingredient": df[ingredients_field].notna().sum() if ingredients_field in df.columns else 0,
        "with_indication": df[indication_field].notna().sum() if indication_field and indication_field in df.columns else 0,
        "unique_ingredients": df[ingredients_field].nunique() if ingredients_field in df.columns else 0,
    }

    # 劑型統計
    if dosage_form_field and dosage_form_field in df.columns:
        result["dosage_forms"] = df[dosage_form_field].value_counts().to_dict()

    return result
