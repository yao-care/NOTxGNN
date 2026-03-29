#!/usr/bin/env python3
"""PubChem 橋接模組

使用 PubChem API 補充 DrugBank 不存在的藥物映射。
PubChem 涵蓋範圍更廣，包含營養補充品、草藥成分等。

API 文件：https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest
"""

import json
import logging
import time
from pathlib import Path
from typing import Dict, List, Optional, Set

import pubchempy as pcp

logger = logging.getLogger(__name__)

# 快取檔案路徑
CACHE_FILE = Path(__file__).parent.parent.parent.parent / "data" / "external" / "pubchem_cache.json"


class PubChemBridge:
    """PubChem API 橋接器

    使用 PubChem 查詢藥物資訊，並快取結果。
    """

    def __init__(self, cache_file: Optional[Path] = None):
        """初始化橋接器

        Args:
            cache_file: 快取檔案路徑
        """
        self.cache_file = cache_file or CACHE_FILE
        self.cache: Dict[str, dict] = {}
        self._load_cache()
        self.request_count = 0
        self.last_request_time = 0.0

    def _load_cache(self):
        """載入快取"""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    self.cache = json.load(f)
                logger.info(f"Loaded {len(self.cache)} cached PubChem entries")
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load cache: {e}")
                self.cache = {}

    def _save_cache(self):
        """儲存快取"""
        self.cache_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.cache_file, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, ensure_ascii=False, indent=2)

    def _rate_limit(self):
        """速率限制（PubChem 建議每秒不超過 5 請求）"""
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        if elapsed < 0.2:  # 200ms 間隔
            time.sleep(0.2 - elapsed)
        self.last_request_time = time.time()

    def get_compound_by_name(self, name: str) -> Optional[dict]:
        """根據名稱查詢化合物

        Args:
            name: 藥物/化合物名稱

        Returns:
            化合物資訊字典，若找不到則回傳 None
        """
        name_upper = name.upper().strip()
        cache_key = f"name:{name_upper}"

        # 檢查快取
        if cache_key in self.cache:
            return self.cache[cache_key]

        self._rate_limit()

        try:
            compounds = pcp.get_compounds(name, 'name')
            self.request_count += 1

            if compounds:
                compound = compounds[0]
                result = {
                    "cid": compound.cid,
                    "iupac_name": compound.iupac_name,
                    "synonyms": compound.synonyms[:20] if compound.synonyms else [],
                    "molecular_formula": compound.molecular_formula,
                }
                self.cache[cache_key] = result
                return result
            else:
                self.cache[cache_key] = None
                return None

        except Exception as e:
            logger.warning(f"PubChem query error for '{name}': {e}")
            return None

    def get_synonyms(self, name: str) -> List[str]:
        """取得藥物的所有同義詞

        Args:
            name: 藥物名稱

        Returns:
            同義詞列表
        """
        compound = self.get_compound_by_name(name)
        if compound and compound.get("synonyms"):
            return [s.upper() for s in compound["synonyms"]]
        return []

    def find_drugbank_candidates(
        self,
        name: str,
        drugbank_names: Set[str]
    ) -> Optional[str]:
        """透過 PubChem 尋找可能的 DrugBank 映射

        Args:
            name: 原始成分名稱
            drugbank_names: DrugBank 中所有藥物名稱（大寫）

        Returns:
            匹配的 DrugBank 名稱，若無則回傳 None
        """
        synonyms = self.get_synonyms(name)

        for synonym in synonyms:
            if synonym in drugbank_names:
                return synonym

        return None

    def save(self):
        """儲存快取到檔案"""
        self._save_cache()
        logger.info(f"Saved {len(self.cache)} PubChem cache entries")


def build_pubchem_mapping(
    unmapped_ingredients: List[str],
    drugbank_names: Set[str],
    max_queries: int = 500,
) -> Dict[str, str]:
    """為未映射成分建立 PubChem 補充映射

    Args:
        unmapped_ingredients: 未映射的成分名稱列表
        drugbank_names: DrugBank 中所有藥物名稱（大寫）
        max_queries: 最大查詢次數

    Returns:
        映射字典 {原始成分: DrugBank 名稱}
    """
    bridge = PubChemBridge()
    mapping = {}
    queries = 0

    logger.info(f"Building PubChem mapping for {len(unmapped_ingredients)} ingredients")

    # 跳過明確無法映射的類型
    skip_patterns = [
        "EXTRACT", "POWDER", "OIL", "TINCTURE", "DRIED",
        "TOXOID", "VACCINE", "ANTIGEN", "RADIX", "HERBA",
        "FLOS", "FRUCTUS", "SEMEN", "CORTEX", "RHIZOMA", "FOLIUM",
        "WATER", "SOLUTION", "EMULSION", "FLUID"
    ]

    for ingredient in unmapped_ingredients:
        if queries >= max_queries:
            logger.info(f"Reached max queries limit ({max_queries})")
            break

        ingredient_upper = ingredient.upper().strip()

        # 跳過無法映射的類型
        if any(pattern in ingredient_upper for pattern in skip_patterns):
            continue

        # 查詢 PubChem
        match = bridge.find_drugbank_candidates(ingredient_upper, drugbank_names)
        queries += 1

        if match:
            mapping[ingredient_upper] = match
            logger.debug(f"Found PubChem mapping: {ingredient_upper} -> {match}")

        # 每 50 次查詢儲存一次快取
        if queries % 50 == 0:
            bridge.save()
            logger.info(f"Processed {queries} queries, found {len(mapping)} mappings")

    # 最終儲存
    bridge.save()
    logger.info(f"Completed: {queries} queries, {len(mapping)} new mappings")

    return mapping


if __name__ == "__main__":
    # 測試範例
    logging.basicConfig(level=logging.INFO)

    bridge = PubChemBridge()

    # 測試幾個 DrugBank 不存在但 PubChem 有的藥物
    test_names = [
        "SILYMARIN",
        "LYSOZYME",
        "ISOCONAZOLE",
        "CHLOROPHYLLIN",
        "BERBERINE",
    ]

    for name in test_names:
        print(f"\n=== {name} ===")
        compound = bridge.get_compound_by_name(name)
        if compound:
            print(f"CID: {compound['cid']}")
            print(f"IUPAC: {compound['iupac_name']}")
            print(f"Synonyms (top 5): {compound['synonyms'][:5]}")
        else:
            print("Not found")

    bridge.save()
