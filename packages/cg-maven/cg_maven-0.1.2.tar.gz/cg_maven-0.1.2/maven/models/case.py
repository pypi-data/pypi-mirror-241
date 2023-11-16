from pydantic import BaseModel, ConfigDict

from maven.models.pipeline import Pipeline
from maven.models.sample import Sample


class Case(BaseModel):
    id: str
    pipeline: Pipeline
    samples: list[Sample]

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "subsonichedgehog",
                "pipeline": {"name": "MIP", "version": "0.0.0"},
                "samples": [{"id": "ACC2341", "pipeline_qc_metrics": "{}"}],
            }
        },
    )
