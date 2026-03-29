#!/usr/bin/env python3
"""
產生新聞監測用的關鍵字清單

從現有資料提取：
- 191 個藥物名稱（英文 + 中文商品名）
- 原始適應症（中文）
- 預測適應症（英文）

輸出：data/news/keywords.json
"""

import json
import re
from datetime import datetime
from pathlib import Path

# 專案根目錄
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DATA_DIR = PROJECT_ROOT / "docs" / "data"


def load_json(path: Path) -> dict | list:
    """載入 JSON 檔案"""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_chinese_terms(text: str) -> list[str]:
    """從中文文字中提取獨立的詞彙（以頓號、逗號、句號分隔）"""
    if not text:
        return []
    # 分隔符：頓號、逗號、句號、分號
    terms = re.split(r"[、，。；,;]", text)
    # 清理空白並過濾空字串
    return [t.strip() for t in terms if t.strip() and len(t.strip()) >= 2]


def get_brand_names_from_fda(fda_data: list, drug_name: str) -> list[str]:
    """從 FDA 資料中找出藥物的中文商品名"""
    brand_names = set()
    drug_name_lower = drug_name.lower()

    for item in fda_data:
        # 檢查主成分是否匹配
        ingredient = item.get("主成分略述") or ""
        if drug_name_lower in ingredient.lower():
            chinese_name = item.get("中文品名", "")
            if chinese_name and item.get("註銷狀態") != "已註銷":
                # 只取品牌名部分（通常在括號前或第一個空白前）
                # 例如：「安美達錠 1 毫克」取「安美達」
                match = re.match(r"^([^\s\d（(]+)", chinese_name)
                if match:
                    brand = match.group(1).strip()
                    if len(brand) >= 2:
                        brand_names.add(brand)

    return list(brand_names)[:5]  # 最多取 5 個商品名


def load_synonyms(path: Path) -> dict:
    """載入中文同義詞對照表"""
    if not path.exists():
        return {"indication_synonyms": {}, "drug_synonyms": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


GENERIC_KEYWORD_PATTERNS = {
    "_generic_cancer": [
        "cancer", "carcinoma", "tumor", "tumour", "neoplasm", "malignant",
        "leukemia", "lymphoma", "melanoma", "sarcoma", "myeloma"
    ],
    "_cardiovascular": [
        "cardiovascular", "atherosclerosis", "arteriosclerosis",
        "coronary", "vascular disease"
    ],
    "_heart_disease": [
        "heart disease", "heart failure", "cardiac", "myocardial",
        "arrhythmia", "angina", "cardiomyopathy"
    ],
    "stroke": ["stroke", "ischemic stroke", "cerebrovascular"],
    "herpes zoster": ["herpes", "zoster", "varicella"],
    "dementia": ["dementia", "alzheimer", "cognitive impairment"],
    "pancreatic cancer": ["pancreatic cancer", "pancreatic carcinoma", "pancreatic neoplasm"],
    "menopause": ["menopause", "postmenopaus", "estrogen-receptor", "hormone-resistant"],
}


def build_indication_index(drugs_data: list, search_index: dict, synonyms: dict) -> dict:
    """建立適應症索引，記錄每個適應症關聯哪些藥物"""
    indication_map = {}
    indication_synonyms = synonyms.get("indication_synonyms", {})

    # 首先加入所有同義詞條目（包括通用關鍵字如 _generic_cancer）
    # 這些可能不對應特定藥物，但對新聞匹配很重要
    for en_name, zh_list in indication_synonyms.items():
        key = en_name.lower()
        if key not in indication_map:
            indication_map[key] = {
                "name": en_name.lstrip("_"),  # 移除前綴下劃線
                "keywords_en": [en_name] if not en_name.startswith("_") else [],
                "keywords_zh": zh_list.copy(),
                "related_drugs": []
            }
            # 為每個中文同義詞也建立索引
            for zh in zh_list:
                zh_key = zh.lower()
                if zh_key not in indication_map:
                    indication_map[zh_key] = {
                        "name": zh,
                        "keywords_en": [en_name] if not en_name.startswith("_") else [],
                        "keywords_zh": [zh],
                        "related_drugs": []
                    }

    for drug in search_index.get("drugs", []):
        drug_slug = drug.get("slug", "")

        # 處理預測適應症
        for ind in drug.get("indications", []):
            ind_name = ind.get("name", "").lower()
            if ind_name:
                if ind_name not in indication_map:
                    # 查找同義詞
                    zh_synonyms = indication_synonyms.get(ind.get("name", ""), [])
                    indication_map[ind_name] = {
                        "name": ind.get("name", ""),
                        "keywords_en": [ind.get("name", "")],
                        "keywords_zh": zh_synonyms.copy(),
                        "related_drugs": []
                    }
                # 將中文同義詞也建立獨立索引（方便匹配）
                for zh in indication_synonyms.get(ind.get("name", ""), []):
                    zh_key = zh.lower()
                    if zh_key not in indication_map:
                        indication_map[zh_key] = {
                            "name": zh,
                            "keywords_en": [ind.get("name", "")],
                            "keywords_zh": [zh],
                            "related_drugs": []
                        }
                    if drug_slug not in indication_map[zh_key]["related_drugs"]:
                        indication_map[zh_key]["related_drugs"].append(drug_slug)

                if drug_slug not in indication_map[ind_name]["related_drugs"]:
                    indication_map[ind_name]["related_drugs"].append(drug_slug)

    # 從 drugs.json 加入原始適應症的中文關鍵字
    for drug_info in drugs_data.get("drugs", []):
        original = drug_info.get("original_indication", "")
        drug_slug = drug_info.get("slug", "")

        # 提取中文詞彙
        zh_terms = extract_chinese_terms(original)

        # 為每個中文適應症詞彙建立映射
        for term in zh_terms:
            # 嘗試找到對應的英文適應症（簡化處理）
            term_key = term.lower()
            if term_key not in indication_map:
                indication_map[term_key] = {
                    "name": term,
                    "keywords_en": [],
                    "keywords_zh": [term],
                    "related_drugs": []
                }
            else:
                if term not in indication_map[term_key]["keywords_zh"]:
                    indication_map[term_key]["keywords_zh"].append(term)

            if drug_slug not in indication_map[term_key]["related_drugs"]:
                indication_map[term_key]["related_drugs"].append(drug_slug)

    # 將通用關鍵字連結到有相關適應症的藥物
    for generic_key, patterns in GENERIC_KEYWORD_PATTERNS.items():
        generic_key_lower = generic_key.lower()
        if generic_key_lower not in indication_map:
            continue

        # 找出所有符合模式的藥物
        for drug in search_index.get("drugs", []):
            drug_slug = drug.get("slug", "")
            for ind in drug.get("indications", []):
                ind_name = ind.get("name", "").lower()
                # 檢查是否匹配任何模式
                for pattern in patterns:
                    if pattern.lower() in ind_name:
                        if drug_slug not in indication_map[generic_key_lower]["related_drugs"]:
                            indication_map[generic_key_lower]["related_drugs"].append(drug_slug)
                        break

        # 同時更新該通用關鍵字的中文同義詞條目
        zh_list = indication_synonyms.get(generic_key, [])
        for zh in zh_list:
            zh_key = zh.lower()
            if zh_key in indication_map:
                for drug_slug in indication_map[generic_key_lower]["related_drugs"]:
                    if drug_slug not in indication_map[zh_key]["related_drugs"]:
                        indication_map[zh_key]["related_drugs"].append(drug_slug)

    return indication_map


def main():
    print("載入資料檔案...")

    # 載入資料
    search_index = load_json(DOCS_DATA_DIR / "search-index.json")
    drugs_data = load_json(DOCS_DATA_DIR / "drugs.json")
    fda_data = load_json(DATA_DIR / "raw" / "tw_fda_drugs.json")
    synonyms = load_synonyms(DATA_DIR / "news" / "synonyms.json")

    print(f"  - search-index.json: {search_index.get('drug_count', 0)} 藥物")
    print(f"  - drugs.json: {drugs_data.get('total_count', 0)} 藥物")
    print(f"  - tw_fda_drugs.json: {len(fda_data)} 筆 FDA 資料")
    print(f"  - synonyms.json: {len(synonyms.get('indication_synonyms', {}))} 適應症同義詞")

    # 建立藥物關鍵字清單
    drugs_keywords = []

    for drug in search_index.get("drugs", []):
        drug_name = drug.get("name", "")
        drug_slug = drug.get("slug", "")

        # 英文關鍵字
        keywords_en = [drug_name.lower()]

        # 加入品牌名（從 search-index）
        for brand in drug.get("brands", []):
            if brand.lower() not in keywords_en:
                keywords_en.append(brand.lower())

        # 中文商品名（從 FDA 資料）
        keywords_zh = get_brand_names_from_fda(fda_data, drug_name)

        drugs_keywords.append({
            "slug": drug_slug,
            "name": drug_name,
            "keywords": {
                "en": keywords_en,
                "zh": keywords_zh
            },
            "url": f"/drugs/{drug_slug}/"
        })

    print(f"\n處理藥物關鍵字: {len(drugs_keywords)} 個藥物")

    # 建立適應症關鍵字清單
    indication_map = build_indication_index(drugs_data, search_index, synonyms)

    # 轉換為列表格式（只保留有相關藥物的關鍵字）
    indications_keywords = []
    for key, data in indication_map.items():
        # 只保留有關聯藥物的適應症
        if data["related_drugs"]:
            indications_keywords.append({
                "name": data["name"],
                "keywords": {
                    "en": data["keywords_en"],
                    "zh": data["keywords_zh"]
                },
                "related_drugs": data["related_drugs"]
            })

    print(f"處理適應症關鍵字: {len(indications_keywords)} 個適應症")

    # 輸出
    output = {
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "drug_count": len(drugs_keywords),
        "indication_count": len(indications_keywords),
        "drugs": drugs_keywords,
        "indications": indications_keywords
    }

    output_path = DATA_DIR / "news" / "keywords.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n輸出: {output_path}")
    print(f"  - 藥物關鍵字: {len(drugs_keywords)} 個")
    print(f"  - 適應症關鍵字: {len(indications_keywords)} 個")


if __name__ == "__main__":
    main()
