"""This module holds the sample model."""
from pydantic import BaseModel

from maven.models.pipeline_qc_metrics import (
    BalsamicQCMetric,
    FluffyQCMetrics,
    MicroSALTQCMetrics,
    MIPDNAQCMetrics,
    MIPRNAQCMetrics,
    MutantQCMetrics,
    RNAFusionQCMetrics,
    TaxprofilerQCMetrics,
)


class Sample(BaseModel):
    id: str
    pipeline_qc_metrics: BalsamicQCMetric | MIPDNAQCMetrics | MIPRNAQCMetrics | FluffyQCMetrics | MutantQCMetrics | RNAFusionQCMetrics | MicroSALTQCMetrics | TaxprofilerQCMetrics
