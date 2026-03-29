#!/usr/bin/env python3
"""知識圖譜方法 - 老藥新用預測

使用 TxGNN 知識圖譜進行藥物-疾病關係預測。
此方法速度快，不需要深度學習環境。

使用方法:
    uv run python scripts/run_kg_prediction.py
"""

import sys
from pathlib import Path

# 將 src 加入 Python 路徑
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from notxgnn.data import load_fda_drugs, filter_active_drugs
from notxgnn.mapping import (
    map_fda_drugs_to_drugbank,
    map_fda_indications_to_diseases,
    get_mapping_stats,
    get_indication_mapping_stats,
)
from notxgnn.predict import find_repurposing_candidates, generate_repurposing_report


def main():
    print("=" * 60)
    print("知識圖譜方法 - Norway藥品老藥新用預測")
    print("Prediksjon av legemiddelreposisjonering i Norge")
    print("=" * 60)
    print()

    # 載入欄位設定
    import yaml
    config_path = Path(__file__).parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as _f:
        config = yaml.safe_load(_f)

    base_dir = Path(__file__).parent.parent
    processed_dir = base_dir / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    # 1. 載入藥品資料
    print("步驟 1/5: 載入藥品資料...")
    df = load_fda_drugs()
    print(f"  總藥品數: {len(df)}")

    # 2. 過濾有效藥品
    print("步驟 2/5: 過濾有效藥品...")
    active = filter_active_drugs(df)
    print(f"  有效藥品數: {len(active)}")

    # 3. 藥品成分映射
    print("步驟 3/5: 映射藥品成分到 DrugBank...")
    fm = config["field_mapping"]
    field_map = {
        "license_id": fm.get("license_id", ""),
        "brand_name": fm.get("brand_name_local", ""),
        "ingredients": fm.get("ingredients", ""),
    }
    drug_mapping = map_fda_drugs_to_drugbank(active, field_mapping=field_map)
    drug_mapping.to_csv(processed_dir / "drug_mapping.csv", index=False)
    stats = get_mapping_stats(drug_mapping)
    print(f"  成分映射率: {stats['mapping_rate']:.2%}")
    print(f"  對應到 DrugBank 藥品數: {stats['unique_drugbank_ids']}")

    # 4. 適應症映射
    print("步驟 4/5: 映射適應症到疾病...")
    indication_field = config["field_mapping"].get("indication", "")
    indication_mapping = map_fda_indications_to_diseases(active, indication_field=indication_field)
    indication_mapping.to_csv(processed_dir / "indication_mapping.csv", index=False)
    if len(indication_mapping) > 0 and 'disease_id' in indication_mapping.columns:
        ind_stats = get_indication_mapping_stats(indication_mapping)
        print(f"  適應症映射率: {ind_stats['mapping_rate']:.2%}")
        print(f"  對應到疾病數: {ind_stats['unique_diseases']}")
    else:
        print("  適應症映射: 無適應症資料或映射結果為空（正常，將僅使用藥品映射）")
        ind_stats = {'mapping_rate': 0, 'unique_diseases': 0}

    # 5. 老藥新用預測
    print("步驟 5/5: 執行老藥新用預測...")
    candidates = find_repurposing_candidates(drug_mapping, indication_mapping)
    output_path = processed_dir / "repurposing_candidates.csv.gz"
    candidates.to_csv(output_path, index=False)

    # 產生報告
    report = generate_repurposing_report(candidates)

    print()
    print("=" * 60)
    print("預測完成！")
    print("=" * 60)
    print()
    print(f"結果檔案: {output_path}")
    print()
    print("統計摘要:")
    print(f"  老藥新用候選數: {report['total_candidates']}")
    print(f"  涉及藥物數: {report['unique_drugs']}")
    print(f"  潛在新適應症數: {report['unique_diseases']}")


if __name__ == "__main__":
    main()
