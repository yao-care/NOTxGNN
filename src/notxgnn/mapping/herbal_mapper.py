#!/usr/bin/env python3
"""中草藥映射模組

由於 TCMSP 沒有公開 API，此模組提供：
1. 常見中草藥的靜態映射表
2. 中草藥主要活性成分對照
3. 可映射到 DrugBank 的已知成分

資料來源：
- TCMSP (https://tcmsp-e.com/tcmsp.php)
- 中藥大辭典
- 相關學術文獻
"""

import logging
from typing import Dict, Optional, Set

logger = logging.getLogger(__name__)

# 中草藥到主要活性成分的映射
# 格式：{FDA 成分名稱: (DrugBank 可映射名稱, 中文名)}
HERBAL_ACTIVE_COMPOUNDS: Dict[str, tuple] = {
    # ===== 甘草 (Glycyrrhiza) =====
    "GLYCYRRHIZA EXTRACT": ("GLYCYRRHIZIC ACID", "甘草萃取物"),
    "GLYCYRRHIZA POWDER": ("GLYCYRRHIZIC ACID", "甘草粉"),
    "GLYCYRRHIZA": ("GLYCYRRHIZIC ACID", "甘草"),
    "GLYCYRRHIZA RADIX": ("GLYCYRRHIZIC ACID", "甘草根"),
    "GLYCYRRHIZA RADIX POWDER": ("GLYCYRRHIZIC ACID", "甘草根粉"),
    "GLYCYRRHIZA FLUIDEXTRACT": ("GLYCYRRHIZIC ACID", "甘草流浸膏"),
    "GLYCYRRHIZAE EXTRACT": ("GLYCYRRHIZIC ACID", "甘草萃取物"),
    "POWDERED GLYCYRRHIZA": ("GLYCYRRHIZIC ACID", "甘草粉"),
    "GLYCYRRHIZINE EXTRACT": ("GLYCYRRHIZIC ACID", "甘草素萃取物"),
    "GLYCYRRHIZATE AMMONIUM SALT": ("GLYCYRRHIZIC ACID", "甘草酸銨"),

    # ===== 銀杏 (Ginkgo biloba) =====
    # 注意：銀杏萃取物主要成分（Ginkgolide、Bilobalide）在 DrugBank 不存在
    "GINKGO BILOBA EXTRACT": (None, "銀杏葉萃取物"),

    # ===== 水飛薊 (Silybum marianum / Milk Thistle) =====
    # 注意：SILYBIN/SILYMARIN 不在 DrugBank 中，無法映射
    "EXSICCATED FRUCTUS CARDUI MARIAE EXTRACT": (None, "水飛薊果萃取物"),
    "SILYMARIN": (None, "水飛薊素"),
    "MILK THISTLE EXTRACT": (None, "水飛薊萃取物"),

    # ===== 莨菪 (Scopolia) =====
    # 主要成分：Scopolamine（東莨菪鹼）、Hyoscyamine
    "SCOPOLIA EXTRACT": ("SCOPOLAMINE", "莨菪萃取物"),
    "SCOPOLIA EXTRACT POWDER": ("SCOPOLAMINE", "莨菪萃取物粉"),

    # ===== 顛茄 (Belladonna) =====
    # 主要成分：Atropine、Scopolamine、Hyoscyamine
    "BELLADONNA EXTRACT": ("ATROPINE", "顛茄萃取物"),
    "BELLADONNA ALKALOID": ("ATROPINE", "顛茄生物鹼"),
    "BELLADONNA TINCTURE": ("ATROPINE", "顛茄酊"),
    "BELLADONNA LEAF POWDER": ("ATROPINE", "顛茄葉粉"),

    # ===== 桔梗 (Platycodon) =====
    # 主要成分：Platycodin D（桔梗皂苷）- DrugBank 不存在
    "PLATYCODON EXTRACT": (None, "桔梗萃取物"),
    "PLATYCODON FLUID EXTRACT": (None, "桔梗流浸膏"),
    "PLATYCODON POWDER": (None, "桔梗粉"),
    "POWDERED PLATYCODON ROOT": (None, "桔梗根粉"),

    # ===== 人參 (Ginseng) =====
    # 主要成分：Ginsenoside（人參皂苷）- DrugBank 不存在
    "GINSENG EXTRACT": (None, "人參萃取物"),
    "GINSENG RADIX EXTRACT": (None, "人參根萃取物"),
    "PANAX GINSENG EXTRACT": (None, "高麗參萃取物"),

    # ===== 當歸 (Angelica) =====
    # 主要成分：Ligustilide、Ferulic acid
    "ANGELICA RADIX EXTRACT": ("FERULIC ACID", "當歸萃取物"),
    "ANGELICA SINENSIS EXTRACT": ("FERULIC ACID", "中國當歸萃取物"),

    # ===== 雷公藤 (Polygala) =====
    "POLYGALA EXTRACT": (None, "遠志萃取物"),

    # ===== 辣椒 (Capsicum) =====
    "CAPSICUM EXTRACT": ("CAPSAICIN", "辣椒萃取物"),
    "CAPSICUM TINCTURE": ("CAPSAICIN", "辣椒酊"),
    "CAPSICUM OLEORESIN": ("CAPSAICIN", "辣椒油樹脂"),

    # ===== 積雪草 (Centella asiatica) =====
    # 主要成分：Asiaticoside、Madecassoside
    "CENTELLA ASIATICA TITRATED EXTRACT": (None, "積雪草萃取物"),
    "CENTELLA ASIATICA EXTRACT": (None, "積雪草萃取物"),

    # ===== 黃柏 (Phellodendron) =====
    # 主要成分：Berberine
    "PHELLODENDRON EXTRACT": ("BERBERINE", "黃柏萃取物"),
    "PHELLODENDRI CORTEX EXTRACT": ("BERBERINE", "黃柏皮萃取物"),

    # ===== 葛根 (Pueraria) =====
    # 主要成分：Puerarin - DrugBank 不存在
    "PUERARIAE RADIX EXTRACT": (None, "葛根萃取物"),
    "PUERARIA EXTRACT": (None, "葛根萃取物"),

    # ===== 川芎 (Cnidium) =====
    # 主要成分：Ligustilide
    "CNIDIUM RHIZOMA EXTRACT": (None, "川芎萃取物"),

    # ===== 其他常見草藥 =====
    "ECHINACEA EXTRACT": (None, "紫錐花萃取物"),
    # VALERIC ACID 不在 DrugBank 中（只有衍生物）
    "VALERIAN EXTRACT": (None, "纈草萃取物"),
    "ST JOHN'S WORT EXTRACT": ("HYPERFORIN", "聖約翰草萃取物"),
    "TURMERIC EXTRACT": ("CURCUMIN", "薑黃萃取物"),
    "CURCUMA EXTRACT": ("CURCUMIN", "薑黃萃取物"),
}

# 可直接映射到 DrugBank 的中草藥活性成分
HERBAL_DRUGBANK_MAPPINGS: Dict[str, str] = {
    # 從 HERBAL_ACTIVE_COMPOUNDS 提取有效映射
    k: v[0] for k, v in HERBAL_ACTIVE_COMPOUNDS.items() if v[0] is not None
}


def map_herbal_ingredient(ingredient: str) -> Optional[str]:
    """將中草藥成分映射到 DrugBank 可用的名稱

    Args:
        ingredient: 成分名稱

    Returns:
        DrugBank 可映射的名稱，若無法映射則回傳 None
    """
    ingredient_upper = ingredient.upper().strip()

    # 直接查表
    if ingredient_upper in HERBAL_DRUGBANK_MAPPINGS:
        return HERBAL_DRUGBANK_MAPPINGS[ingredient_upper]

    # 嘗試模糊匹配
    for pattern, target in HERBAL_DRUGBANK_MAPPINGS.items():
        if pattern in ingredient_upper or ingredient_upper in pattern:
            return target

    return None


def get_herbal_info(ingredient: str) -> Optional[dict]:
    """取得中草藥成分的詳細資訊

    Args:
        ingredient: 成分名稱

    Returns:
        包含中文名和活性成分的字典
    """
    ingredient_upper = ingredient.upper().strip()

    if ingredient_upper in HERBAL_ACTIVE_COMPOUNDS:
        active, chinese_name = HERBAL_ACTIVE_COMPOUNDS[ingredient_upper]
        return {
            "chinese_name": chinese_name,
            "active_compound": active,
            "mappable": active is not None,
        }

    return None


def is_herbal_ingredient(ingredient: str) -> bool:
    """判斷是否為中草藥成分

    Args:
        ingredient: 成分名稱

    Returns:
        是否為中草藥成分
    """
    ingredient_upper = ingredient.upper().strip()

    # 中草藥關鍵字
    herbal_keywords = [
        "EXTRACT", "RADIX", "HERBA", "FLOS", "FRUCTUS", "SEMEN",
        "CORTEX", "RHIZOMA", "FOLIUM", "TINCTURE", "POWDER",
        "GLYCYRRHIZA", "GINKGO", "GINSENG", "ANGELICA", "ASTRAGALUS",
        "SCUTELLARIA", "PLATYCODON", "POLYGALA", "SCOPOLIA", "BELLADONNA",
        "PUERARIA", "CNIDIUM", "CENTELLA", "ECHINACEA", "VALERIAN",
    ]

    return any(kw in ingredient_upper for kw in herbal_keywords)


def get_unmappable_herbal_ingredients() -> Dict[str, str]:
    """取得無法映射到 DrugBank 的中草藥成分清單

    Returns:
        {成分名稱: 中文名} 字典
    """
    return {
        k: v[1] for k, v in HERBAL_ACTIVE_COMPOUNDS.items() if v[0] is None
    }


if __name__ == "__main__":
    # 測試範例
    test_ingredients = [
        "GLYCYRRHIZA EXTRACT",
        "GINKGO BILOBA EXTRACT",
        "SILYMARIN",
        "BELLADONNA EXTRACT",
        "CAPSICUM EXTRACT",
        "GINSENG EXTRACT",
    ]

    print("=== 中草藥映射測試 ===\n")

    for ing in test_ingredients:
        info = get_herbal_info(ing)
        mapping = map_herbal_ingredient(ing)

        print(f"{ing}")
        if info:
            print(f"  中文名: {info['chinese_name']}")
            print(f"  活性成分: {info['active_compound'] or '(無法映射)'}")
            print(f"  DrugBank 映射: {mapping or '無'}")
        else:
            print(f"  無資料")
        print()

    print("\n=== 無法映射的中草藥成分 ===")
    unmappable = get_unmappable_herbal_ingredients()
    for name, chinese in list(unmappable.items())[:10]:
        print(f"  {name}: {chinese}")
