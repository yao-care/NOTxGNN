"""老藥新用預測 - 基於 TxGNN 知識圖譜"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd


def load_drug_disease_relations(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 藥物-疾病關係

    Args:
        filepath: CSV 檔案路徑

    Returns:
        藥物-疾病關係 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drug_disease_relations.csv"

    return pd.read_csv(filepath)


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """建立藥物 -> 適應症集合的映射

    Args:
        relations_df: 藥物-疾病關係 DataFrame

    Returns:
        {drug_name: {disease1, disease2, ...}}
    """
    # 只取 indication 和 off-label use
    indications = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"]

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def find_repurposing_candidates(
    drug_mapping_df: pd.DataFrame,
    indication_mapping_df: pd.DataFrame,
    relations_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """找出老藥新用候選

    比較藥品的現有適應症與 TxGNN 知識圖譜中的適應症，
    找出可能的新適應症。

    Args:
        drug_mapping_df: 藥品 DrugBank 映射結果
        indication_mapping_df: 適應症疾病映射結果
        relations_df: TxGNN 藥物-疾病關係

    Returns:
        老藥新用候選 DataFrame
    """
    if relations_df is None:
        relations_df = load_drug_disease_relations()

    # 建立 TxGNN 藥物適應症映射
    kg_drug_map = build_drug_indication_map(relations_df)

    # 自動偵測欄位名稱（支援巴西和台灣格式）
    license_col = "NUMERO_REGISTRO_PRODUTO" if "NUMERO_REGISTRO_PRODUTO" in indication_mapping_df.columns else "許可證字號"
    brand_col = "NOME_PRODUTO" if "NOME_PRODUTO" in indication_mapping_df.columns else "中文品名"

    # drug_mapping 使用新的欄位名稱
    drug_license_col = "license_id" if "license_id" in drug_mapping_df.columns else "許可證字號"
    drug_brand_col = "brand_name" if "brand_name" in drug_mapping_df.columns else "中文品名"
    ingredient_col = "normalized_ingredient" if "normalized_ingredient" in drug_mapping_df.columns else "標準化成分"

    # 建立現有藥品的適應症（向量化操作）
    existing_drug_diseases = {}
    if len(indication_mapping_df) > 0 and "disease_name" in indication_mapping_df.columns:
        existing_diseases_df = indication_mapping_df[
            indication_mapping_df["disease_name"].notna()
        ][[license_col, "disease_name"]].copy()
        existing_diseases_df["disease_lower"] = existing_diseases_df["disease_name"].str.lower()
        existing_drug_diseases = existing_diseases_df.groupby(license_col)["disease_lower"].apply(set).to_dict()

    # 建立藥品資訊索引（向量化）
    valid_drugs = drug_mapping_df[drug_mapping_df["drugbank_id"].notna()].copy()

    # 取得唯一的 (license_id, 藥物成分) 組合
    unique_pairs = valid_drugs[[drug_license_col, ingredient_col, drug_brand_col, "drugbank_id"]].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_no = row[drug_license_col]
        drug_name = row[ingredient_col]

        # 查詢 TxGNN 中該藥物的所有適應症
        kg_diseases = kg_drug_map.get(drug_name, set())
        if not kg_diseases:
            continue

        # 取得現有適應症
        current_diseases = existing_drug_diseases.get(license_no, set())

        # 找出潛在新適應症
        for disease in kg_diseases:
            disease_lower = disease.lower()

            # 快速檢查是否已存在
            is_new = all(
                curr_d not in disease_lower and disease_lower not in curr_d
                for curr_d in current_diseases
            )

            if is_new:
                candidates.append({
                    "license_id": license_no,
                    "brand_name": row[drug_brand_col],
                    "drug_ingredient": drug_name,
                    "drugbank_id": row["drugbank_id"],
                    "potential_indication": disease,
                    "source": "TxGNN Knowledge Graph",
                })

    result_df = pd.DataFrame(candidates)

    # 去重
    if len(result_df) > 0:
        # First: remove exact duplicates per license
        result_df = result_df.drop_duplicates(
            subset=["license_id", "drug_ingredient", "potential_indication"]
        )

        # Second: for DL prediction efficiency, keep only unique (drugbank_id, disease) pairs
        # This prevents redundant DL predictions for the same drug-disease combination
        # We keep the first occurrence (arbitrary license_id as representative)
        result_df = result_df.drop_duplicates(
            subset=["drugbank_id", "potential_indication"],
            keep="first"
        )

    return result_df


def generate_repurposing_report(candidates_df: pd.DataFrame) -> dict:
    """生成老藥新用報告統計

    Args:
        candidates_df: 候選藥物 DataFrame

    Returns:
        統計報告字典
    """
    if len(candidates_df) == 0:
        return {
            "total_candidates": 0,
            "unique_drugs": 0,
            "unique_diseases": 0,
            "top_diseases": [],
            "top_drugs": [],
        }

    # 自動偵測欄位名稱
    drug_col = "drug_ingredient" if "drug_ingredient" in candidates_df.columns else "藥物成分"
    indication_col = "potential_indication" if "potential_indication" in candidates_df.columns else "潛在新適應症"

    unique_drugs = candidates_df[drug_col].nunique()
    unique_diseases = candidates_df[indication_col].nunique()

    # 最常見的潛在新適應症
    top_diseases = candidates_df[indication_col].value_counts().head(10).to_dict()

    # 最多潛在新適應症的藥物
    drug_counts = candidates_df.groupby(drug_col)[indication_col].nunique()
    top_drugs = drug_counts.sort_values(ascending=False).head(10).to_dict()

    return {
        "total_candidates": len(candidates_df),
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
        "top_diseases": top_diseases,
        "top_drugs": top_drugs,
    }
