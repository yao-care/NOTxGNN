#!/usr/bin/env python3
"""
Integrate KG and DL prediction results.

This script combines predictions from:
1. Knowledge Graph (KG) method - fast, lower precision
2. Deep Learning (DL) method - slow, higher precision

Output:
- Unified prediction results with confidence levels
- Predictions supported by both methods are marked as high confidence
"""

import argparse
from pathlib import Path

import pandas as pd

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"

# Input files
KG_PREDICTIONS = DATA_DIR / "processed" / "repurposing_candidates.csv.gz"
DL_PREDICTIONS = DATA_DIR / "processed" / "txgnn_dl_predictions.csv.gz"
DRUG_MAPPING = DATA_DIR / "processed" / "drug_mapping.csv"

# Output files
OUTPUT_FILE = DATA_DIR / "processed" / "integrated_predictions.csv.gz"
STATS_FILE = DATA_DIR / "processed" / "integration_stats.json"


def load_kg_predictions() -> pd.DataFrame:
    """Load KG prediction results."""
    print("Loading KG predictions...")
    kg = pd.read_csv(KG_PREDICTIONS)
    print(f"  KG predictions: {len(kg):,}")
    print(f"  KG drugs: {kg['drugbank_id'].nunique():,}")
    print(f"  KG indications: {kg['潛在新適應症'].nunique():,}")
    return kg


def load_dl_predictions(score_threshold: float = 0.5, max_rows: int | None = None) -> pd.DataFrame:
    """Load DL prediction results with optional filtering."""
    print(f"\nLoading DL predictions (score >= {score_threshold})...")

    # Read in chunks to handle large file
    chunks = []
    total_rows = 0

    for chunk in pd.read_csv(DL_PREDICTIONS, chunksize=1_000_000):
        # Filter by score threshold
        filtered = chunk[chunk["txgnn_score"] >= score_threshold]
        chunks.append(filtered)
        total_rows += len(chunk)

        if max_rows and total_rows >= max_rows:
            break

    dl = pd.concat(chunks, ignore_index=True)
    print(f"  Total DL predictions: {total_rows:,}")
    print(f"  Filtered DL predictions (score >= {score_threshold}): {len(dl):,}")
    print(f"  DL drugs: {dl['drugbank_id'].nunique():,}")
    print(f"  DL indications: {dl['潛在新適應症'].nunique():,}")

    return dl


def load_drug_mapping() -> pd.DataFrame:
    """Load drug mapping to Taiwan FDA products."""
    print("\nLoading drug mapping...")
    mapping = pd.read_csv(DRUG_MAPPING)
    # Keep only successful mappings
    mapping = mapping[mapping["映射成功"] == True]
    print(f"  Mapped drugs: {len(mapping):,}")
    print(f"  Unique DrugBank IDs: {mapping['drugbank_id'].nunique():,}")
    return mapping


def integrate_predictions(
    kg: pd.DataFrame,
    dl: pd.DataFrame,
    mapping: pd.DataFrame
) -> pd.DataFrame:
    """Integrate KG and DL predictions using vectorized operations."""
    print("\nIntegrating predictions...")

    # Create composite key for efficient joining
    kg["_key"] = kg["drugbank_id"] + "|" + kg["潛在新適應症"]
    dl["_key"] = dl["drugbank_id"] + "|" + dl["潛在新適應症"]

    # Get max DL score per (drug, indication) pair using groupby (vectorized)
    print("  Computing DL scores...")
    dl_scores = dl.groupby("_key")["txgnn_score"].max().reset_index()
    dl_scores = dl_scores.rename(columns={"txgnn_score": "dl_score"})
    print(f"  DL unique pairs: {len(dl_scores):,}")

    # Create sets for comparison
    kg_keys = set(kg["_key"])
    dl_keys = set(dl_scores["_key"])

    common = kg_keys & dl_keys
    kg_only = kg_keys - dl_keys
    dl_only = dl_keys - kg_keys

    print(f"\n  Common predictions (KG + DL): {len(common):,}")
    print(f"  KG only predictions: {len(kg_only):,}")
    print(f"  DL only predictions: {len(dl_only):,}")

    # Process KG predictions (merge with DL scores)
    print("\n  Processing KG predictions...")
    kg_unified = kg.merge(dl_scores, on="_key", how="left")
    kg_unified["kg_prediction"] = True
    kg_unified["dl_prediction"] = kg_unified["dl_score"].notna()

    # Process DL-only predictions (need to map to Taiwan products)
    print("  Processing DL-only predictions...")
    dl_only_keys = dl_scores[dl_scores["_key"].isin(dl_only)].copy()

    if len(dl_only_keys) > 0:
        # Extract drugbank_id and indication from key
        dl_only_keys[["drugbank_id", "潛在新適應症"]] = dl_only_keys["_key"].str.split("|", expand=True)

        # Map to Taiwan products
        dl_mapped = dl_only_keys.merge(
            mapping[["許可證字號", "中文品名", "標準化成分", "drugbank_id"]],
            on="drugbank_id",
            how="inner"
        )
        dl_mapped = dl_mapped.rename(columns={"標準化成分": "藥物成分"})
        dl_mapped["kg_prediction"] = False
        dl_mapped["dl_prediction"] = True
        dl_mapped["來源"] = "TxGNN Deep Learning Model"

        print(f"    DL-only mapped to Taiwan products: {len(dl_mapped):,}")

        # Combine
        unified = pd.concat([
            kg_unified[["許可證字號", "中文品名", "藥物成分", "drugbank_id",
                       "潛在新適應症", "kg_prediction", "dl_prediction", "dl_score", "來源"]],
            dl_mapped[["許可證字號", "中文品名", "藥物成分", "drugbank_id",
                      "潛在新適應症", "kg_prediction", "dl_prediction", "dl_score", "來源"]]
        ], ignore_index=True)
    else:
        unified = kg_unified[["許可證字號", "中文品名", "藥物成分", "drugbank_id",
                              "潛在新適應症", "kg_prediction", "dl_prediction", "dl_score", "來源"]]

    # Add confidence level using numpy select (proper vectorized approach)
    print("  Computing confidence levels...")
    import numpy as np

    # Fill NaN in dl_score for comparison
    dl_score_filled = unified["dl_score"].fillna(0)

    conditions = [
        (unified["kg_prediction"] & unified["dl_prediction"] & (dl_score_filled >= 0.9)),
        (unified["kg_prediction"] & unified["dl_prediction"]),
        (~unified["kg_prediction"] & unified["dl_prediction"] & (dl_score_filled >= 0.9)),
        (~unified["kg_prediction"] & unified["dl_prediction"] & (dl_score_filled >= 0.7)),
        (~unified["kg_prediction"] & unified["dl_prediction"]),
        (unified["kg_prediction"] & ~unified["dl_prediction"]),
    ]
    choices = ["very_high", "high", "high", "medium", "low", "medium"]
    unified["confidence"] = np.select(conditions, choices, default="low")

    # Update source column using vectorized conditions
    unified.loc[unified["kg_prediction"] & unified["dl_prediction"], "來源"] = "KG + DL"
    unified.loc[unified["kg_prediction"] & ~unified["dl_prediction"], "來源"] = "KG"
    unified.loc[~unified["kg_prediction"] & unified["dl_prediction"], "來源"] = "DL"

    # Sort by confidence and dl_score
    confidence_order = {"very_high": 0, "high": 1, "medium": 2, "low": 3}
    unified["_conf_order"] = unified["confidence"].map(confidence_order)
    unified["_dl_score"] = unified["dl_score"].fillna(0)
    unified = unified.sort_values(
        ["_conf_order", "_dl_score"],
        ascending=[True, False]
    ).drop(columns=["_conf_order", "_dl_score"])

    return unified


def print_statistics(unified: pd.DataFrame):
    """Print integration statistics."""
    print("\n" + "=" * 60)
    print("Integration Statistics")
    print("=" * 60)

    print(f"\nTotal predictions: {len(unified):,}")
    print(f"Unique drugs: {unified['drugbank_id'].nunique():,}")
    print(f"Unique indications: {unified['潛在新適應症'].nunique():,}")
    print(f"Unique Taiwan products: {unified['許可證字號'].nunique():,}")

    print("\nBy source:")
    for source, count in unified["來源"].value_counts().items():
        print(f"  {source}: {count:,}")

    print("\nBy confidence level:")
    for conf, count in unified["confidence"].value_counts().sort_index().items():
        print(f"  {conf}: {count:,}")

    # High confidence predictions
    high_conf = unified[unified["confidence"].isin(["very_high", "high"])]
    print(f"\nHigh/Very High confidence predictions: {len(high_conf):,}")
    print(f"  Drugs: {high_conf['drugbank_id'].nunique():,}")
    print(f"  Indications: {high_conf['潛在新適應症'].nunique():,}")


def save_results(unified: pd.DataFrame):
    """Save integration results."""
    print(f"\nSaving results to {OUTPUT_FILE}...")
    unified.to_csv(OUTPUT_FILE, index=False)
    print(f"  Saved {len(unified):,} predictions")

    # Save statistics as JSON
    import json
    stats = {
        "total_predictions": len(unified),
        "unique_drugs": int(unified["drugbank_id"].nunique()),
        "unique_indications": int(unified["潛在新適應症"].nunique()),
        "unique_taiwan_products": int(unified["許可證字號"].nunique()),
        "by_source": unified["來源"].value_counts().to_dict(),
        "by_confidence": unified["confidence"].value_counts().to_dict(),
    }

    with open(STATS_FILE, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    print(f"  Saved statistics to {STATS_FILE}")


def main():
    parser = argparse.ArgumentParser(description="Integrate KG and DL predictions")
    parser.add_argument(
        "--dl-threshold",
        type=float,
        default=0.5,
        help="DL score threshold (default: 0.5)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without saving results"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("TwTxGNN Prediction Integration")
    print("=" * 60)

    # Load data
    kg = load_kg_predictions()
    dl = load_dl_predictions(score_threshold=args.dl_threshold)
    mapping = load_drug_mapping()

    # Integrate
    unified = integrate_predictions(kg, dl, mapping)

    # Statistics
    print_statistics(unified)

    # Save
    if not args.dry_run:
        save_results(unified)
    else:
        print("\n[Dry run - results not saved]")

    print("\nDone!")


if __name__ == "__main__":
    main()
