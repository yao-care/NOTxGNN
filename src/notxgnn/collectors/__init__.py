"""Data collectors for evidence gathering."""

from .base import BaseCollector, CollectorResult
from .bundle import BundleAggregator, CandidateInfo, EvidenceBundle
from .clinicaltrials import ClinicalTrialsCollector
from .ddinter import DDInterCollector
from .drug_bundle import (
    CollectionStatus,
    DrugBundle,
    DrugBundleAggregator,
    DrugCandidate,
    PredictedIndication,
    load_predictions_for_drug,
)
from .drugbank import DrugBankCollector
from .ictrp import ICTRPCollector
from .known_relations import KnownRelationsChecker
from .pharmacology import PharmacologyCollector
from .pubmed import PubMedCollector
from .tfda import TFDACollector
from .tfda_package_insert import TFDAPackageInsertCollector
from .unified_ddi import UnifiedDDICollector

__all__ = [
    "BaseCollector",
    "BundleAggregator",
    "CandidateInfo",
    "ClinicalTrialsCollector",
    "CollectionStatus",
    "CollectorResult",
    "DDInterCollector",
    "DrugBankCollector",
    "DrugBundle",
    "DrugBundleAggregator",
    "DrugCandidate",
    "EvidenceBundle",
    "ICTRPCollector",
    "KnownRelationsChecker",
    "load_predictions_for_drug",
    "PharmacologyCollector",
    "PredictedIndication",
    "PubMedCollector",
    "TFDACollector",
    "TFDAPackageInsertCollector",
    "UnifiedDDICollector",
]
