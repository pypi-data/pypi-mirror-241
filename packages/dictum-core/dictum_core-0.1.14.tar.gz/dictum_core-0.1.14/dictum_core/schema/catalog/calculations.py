from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class CatalogType(BaseModel):
    name: str
    grain: Optional[str] = None

    class Config:
        orm_mode = True


class CatalogFormat(BaseModel):
    type: CatalogType
    d3_format: Optional[str] = None

    class Config:
        orm_mode = True


class CatalogCalculation(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    expr: Optional[str] = Field(None, alias="str_expr")
    format: CatalogFormat
    type: CatalogType

    class Config:
        orm_mode = True


class CatalogDimension(CatalogCalculation):
    pass


class MetricLineageItem(BaseModel):
    id: str
    name: str
    type: Literal["Metric", "Measure", "Dimension", "Column"]
    parent: Optional[str] = None


class MetricLineage(BaseModel):
    __root__: List[MetricLineageItem]


class CatalogMetric(CatalogCalculation):
    lineage: MetricLineage
    dimensions: List[CatalogDimension]
    time: List[CatalogDimension] = Field(alias="generic_time_dimensions")
