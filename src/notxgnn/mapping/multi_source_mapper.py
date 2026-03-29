#!/usr/bin/env python3
"""多來源藥物映射整合模組

整合 DrugBank、RxNorm、PubChem、ChEMBL 和 TCMSP 的映射能力，
提供統一的映射介面。

映射優先順序：
1. DrugBank 直接映射（最可靠）
2. DrugBank 同義詞映射
3. 中草藥映射表（TCMSP 靜態資料）
4. RxNorm API 橋接
5. PubChem API 橋接
6. ChEMBL API 橋接
"""

import logging
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd

from .drugbank_mapper import build_name_index, map_ingredient_to_drugbank
from .herbal_mapper import is_herbal_ingredient, map_herbal_ingredient

logger = logging.getLogger(__name__)


class MultiSourceMapper:
    """多來源藥物映射器

    整合多個資料來源，依優先順序嘗試映射。
    """

    def __init__(
        self,
        drugbank_df: Optional[pd.DataFrame] = None,
        use_rxnorm: bool = False,
        use_pubchem: bool = False,
        use_chembl: bool = False,
    ):
        """初始化映射器

        Args:
            drugbank_df: DrugBank 詞彙表
            use_rxnorm: 是否啟用 RxNorm 橋接
            use_pubchem: 是否啟用 PubChem 橋接
            use_chembl: 是否啟用 ChEMBL 橋接
        """
        # 載入 DrugBank
        if drugbank_df is None:
            drugbank_path = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drugbank_vocab.csv"
            drugbank_df = pd.read_csv(drugbank_path)

        self.drugbank_df = drugbank_df
        self.name_index = build_name_index(drugbank_df)
        self.drugbank_names = set(drugbank_df["drug_name_upper"].str.upper())

        # 初始化外部橋接
        self.rxnorm_bridge = None
        self.pubchem_bridge = None
        self.chembl_bridge = None

        if use_rxnorm:
            try:
                from .rxnorm_bridge import RxNormBridge
                self.rxnorm_bridge = RxNormBridge()
                logger.info("RxNorm bridge enabled")
            except ImportError as e:
                logger.warning(f"Failed to import RxNorm bridge: {e}")

        if use_pubchem:
            try:
                from .pubchem_bridge import PubChemBridge
                self.pubchem_bridge = PubChemBridge()
                logger.info("PubChem bridge enabled")
            except ImportError as e:
                logger.warning(f"Failed to import PubChem bridge: {e}")

        if use_chembl:
            try:
                from .chembl_bridge import ChEMBLBridge
                self.chembl_bridge = ChEMBLBridge()
                logger.info("ChEMBL bridge enabled")
            except ImportError as e:
                logger.warning(f"Failed to import ChEMBL bridge: {e}")

        # 統計
        self.stats = {
            "total": 0,
            "drugbank_direct": 0,
            "drugbank_synonym": 0,
            "herbal": 0,
            "rxnorm": 0,
            "pubchem": 0,
            "chembl": 0,
            "failed": 0,
        }

    def map_ingredient(self, ingredient: str) -> Tuple[Optional[str], str]:
        """映射單一成分

        Args:
            ingredient: 成分名稱

        Returns:
            (DrugBank ID, 來源) 元組
        """
        self.stats["total"] += 1
        ingredient_upper = ingredient.upper().strip()

        # 1. DrugBank 直接/同義詞映射
        drugbank_id = map_ingredient_to_drugbank(ingredient_upper, self.name_index)
        if drugbank_id:
            if ingredient_upper in self.drugbank_names:
                self.stats["drugbank_direct"] += 1
                return drugbank_id, "drugbank_direct"
            else:
                self.stats["drugbank_synonym"] += 1
                return drugbank_id, "drugbank_synonym"

        # 2. 中草藥映射
        if is_herbal_ingredient(ingredient_upper):
            herbal_target = map_herbal_ingredient(ingredient_upper)
            if herbal_target:
                drugbank_id = map_ingredient_to_drugbank(herbal_target, self.name_index)
                if drugbank_id:
                    self.stats["herbal"] += 1
                    return drugbank_id, "herbal"

        # 3. RxNorm 橋接
        if self.rxnorm_bridge:
            candidates = self.rxnorm_bridge.find_drugbank_candidates(ingredient_upper)
            for candidate in candidates:
                if candidate in self.drugbank_names:
                    drugbank_id = self.name_index.get(candidate)
                    if drugbank_id:
                        self.stats["rxnorm"] += 1
                        return drugbank_id, "rxnorm"

        # 4. PubChem 橋接
        if self.pubchem_bridge:
            match = self.pubchem_bridge.find_drugbank_candidates(
                ingredient_upper, self.drugbank_names
            )
            if match:
                drugbank_id = self.name_index.get(match)
                if drugbank_id:
                    self.stats["pubchem"] += 1
                    return drugbank_id, "pubchem"

        # 5. ChEMBL 橋接
        if self.chembl_bridge:
            match = self.chembl_bridge.find_drugbank_candidates(
                ingredient_upper, self.drugbank_names
            )
            if match:
                drugbank_id = self.name_index.get(match)
                if drugbank_id:
                    self.stats["chembl"] += 1
                    return drugbank_id, "chembl"

        self.stats["failed"] += 1
        return None, "failed"

    def map_ingredients(
        self,
        ingredients: List[str],
        verbose: bool = False
    ) -> Dict[str, Tuple[Optional[str], str]]:
        """批次映射多個成分

        Args:
            ingredients: 成分名稱列表
            verbose: 是否顯示進度

        Returns:
            {成分: (DrugBank ID, 來源)} 字典
        """
        results = {}

        for i, ingredient in enumerate(ingredients):
            if verbose and (i + 1) % 100 == 0:
                logger.info(f"Progress: {i + 1}/{len(ingredients)}")

            drugbank_id, source = self.map_ingredient(ingredient)
            results[ingredient] = (drugbank_id, source)

        return results

    def get_stats(self) -> Dict[str, int]:
        """取得映射統計"""
        return self.stats.copy()

    def print_stats(self):
        """印出映射統計"""
        print("\n=== 映射統計 ===")
        total = self.stats["total"]
        if total == 0:
            print("尚無統計資料")
            return

        success = total - self.stats["failed"]
        print(f"總成分數: {total}")
        print(f"映射成功: {success} ({100*success/total:.1f}%)")
        print()
        print("來源分布:")
        for source in ["drugbank_direct", "drugbank_synonym", "herbal", "rxnorm", "pubchem", "chembl"]:
            count = self.stats[source]
            if count > 0:
                print(f"  {source}: {count} ({100*count/total:.1f}%)")
        print(f"  failed: {self.stats['failed']} ({100*self.stats['failed']/total:.1f}%)")

    def save_caches(self):
        """儲存所有橋接的快取"""
        if self.rxnorm_bridge:
            self.rxnorm_bridge.save()
        if self.pubchem_bridge:
            self.pubchem_bridge.save()
        if self.chembl_bridge:
            self.chembl_bridge.save()

    def close(self):
        """關閉所有連線"""
        self.save_caches()
        if self.chembl_bridge:
            self.chembl_bridge.close()


if __name__ == "__main__":
    # 測試範例
    logging.basicConfig(level=logging.INFO)

    # 測試成分
    test_ingredients = [
        "ACETAMINOPHEN",           # DrugBank 直接
        "PARACETAMOL",             # DrugBank 同義詞
        "GLYCYRRHIZA EXTRACT",     # 中草藥
        "SILYMARIN",               # 中草藥
        "KETOROLAC TROMETHAMINE",  # 需要外部橋接
        "SOME_UNKNOWN_DRUG",       # 無法映射
    ]

    # 測試基本映射（不啟用外部橋接）
    print("=== 基本映射測試（僅 DrugBank + 中草藥）===")
    mapper = MultiSourceMapper()

    for ing in test_ingredients:
        drugbank_id, source = mapper.map_ingredient(ing)
        print(f"{ing:<30} -> {drugbank_id or 'None':<12} ({source})")

    mapper.print_stats()

    # 測試完整映射（啟用所有橋接）
    print("\n\n=== 完整映射測試（啟用所有橋接）===")
    full_mapper = MultiSourceMapper(
        use_rxnorm=True,
        use_pubchem=True,
        use_chembl=True
    )

    for ing in test_ingredients:
        drugbank_id, source = full_mapper.map_ingredient(ing)
        print(f"{ing:<30} -> {drugbank_id or 'None':<12} ({source})")

    full_mapper.print_stats()
    full_mapper.close()
