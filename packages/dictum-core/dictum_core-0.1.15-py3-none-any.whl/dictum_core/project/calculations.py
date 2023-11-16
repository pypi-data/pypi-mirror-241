from copy import deepcopy
from typing import Dict

import dictum_core.model
import dictum_core.project
from dictum_core.engine.metrics import limit_transforms
from dictum_core.engine.metrics import transforms as table_transforms
from dictum_core.model.scalar import transforms as scalar_transforms
from dictum_core.project.templates import environment, lineage_spec
from dictum_core.schema.query import (
    QueryDimension,
    QueryDimensionRequest,
    QueryMetric,
    QueryMetricRequest,
    QueryScalarTransform,
    QueryTableTransform,
)

scalar_transforms = set(scalar_transforms)
table_transforms = set(table_transforms) | set(limit_transforms)


class ProjectCalculation:
    kind: str

    def __init__(self, calculation, locale: str):
        self.calculation = calculation
        self.locale = locale

    def encoding_fields(self, cls=None) -> dict:
        return {"field": f"{self._type}:{self}"}

    @property
    def _type(self) -> str:
        if isinstance(self.calculation, dictum_core.model.Metric):
            return "metric"
        return "dimension"

    def _repr_html_(self):
        template = environment.get_template("calculation.html.j2")
        calculation = self.calculation
        if isinstance(calculation, dictum_core.model.Metric):
            _lineage_spec = deepcopy(lineage_spec)
            _lineage_spec["data"][0]["values"] = calculation.lineage
            if calculation.is_measure:
                calculation = calculation.measures[0]
        return template.render(calculation=calculation, lineage=None)

    def name(self, name: str):
        self.request.alias = name
        return self

    def __eq__(self, other):
        return self.eq(other)

    def __ne__(self, other):
        return self.ne(other)

    def __gt__(self, other):
        return self.gt(other)

    def __ge__(self, other):
        return self.ge(other)

    def __lt__(self, other):
        return self.lt(other)

    def __le__(self, other):
        return self.le(other)

    def __invert__(self):
        return self.invert()

    def __str__(self):
        return self.request.render()


class ProjectMetricRequest(ProjectCalculation):
    kind = "metric"

    def __init__(self, calculation, locale: str):
        self.request = QueryMetricRequest(metric=QueryMetric(id=calculation.id))
        super().__init__(calculation, locale)

    def __getattr__(self, name: str):
        if name not in table_transforms:
            raise AttributeError(name)
        self.request.metric.transforms.append(QueryTableTransform(id=name))
        return self

    def __dir__(self):
        return table_transforms.keys()

    def __call__(self, *args, of=None, within=None):
        of = [] if of is None else of
        within = [] if within is None else within
        if isinstance(of, ProjectDimensionRequest):
            of = [of]
        if isinstance(within, ProjectDimensionRequest):
            within = [within]
        self.request.metric.transforms[-1].args = list(args)
        self.request.metric.transforms[-1].of = [i.request for i in of]
        self.request.metric.transforms[-1].within = [i.request for i in within]
        return self


class ProjectMetric(ProjectMetricRequest):
    def name(self, name: str):
        return ProjectMetricRequest(
            calculation=self.calculation, locale=self.locale
        ).name(name)

    def __getattr__(self, name: str):
        if name not in table_transforms:
            raise AttributeError(name)
        return getattr(
            ProjectMetricRequest(calculation=self.calculation, locale=self.locale),
            name,
        )


class ProjectMetrics:
    def __init__(self, project: "dictum_core.project.Project"):
        self.__project = project
        self.__mount_attributes()

    def __mount_attributes(self):
        self.__metrics: Dict[str, ProjectMetric] = {
            m.id: ProjectMetric(m, self.__project.model.locale)
            for m in self.__project.model.metrics.values()
        }

    def __getattr__(self, attr: str) -> ProjectMetric:
        return self.__metrics[attr]

    def __getitem__(self, key: str) -> ProjectMetric:
        return self.__metrics[key]

    def __dir__(self):
        return self.__metrics.keys()

    def _repr_html_(self):
        template = environment.get_template("calculations.html.j2")
        return template.render(calculations=self.__project.model.metrics.values())


class ProjectDimensionRequest(ProjectCalculation):
    kind = "dimension"

    def __init__(self, calculation, locale: str):
        self.request = QueryDimensionRequest(
            dimension=QueryDimension(id=calculation.id)
        )
        super().__init__(calculation, locale)

    def __getattr__(self, name: str):
        if name not in scalar_transforms:
            raise AttributeError(name)  # for Jupyter checking for _repr_html_ etc.
        self.request.dimension.transforms.append(QueryScalarTransform(id=name))
        return self

    def __call__(self, *args):
        self.request.dimension.transforms[-1].args = list(args)
        return self


class ProjectDimension(ProjectDimensionRequest):
    def __getattr__(self, name: str):
        if name not in scalar_transforms:
            raise AttributeError(name)  # for Jupyter checking for _repr_html_ etc.
        return getattr(
            ProjectDimensionRequest(self.calculation, locale=self.locale),
            name,
        )

    def name(self, name: str):
        return ProjectDimensionRequest(self.calculation, locale=self.locale).name(name)

    def __str__(self):
        return self.calculation.id


class ProjectDimensions:
    def __init__(self, project: "dictum_core.project.Project"):
        self.__project = project
        self.__mount_attributes()

    def __mount_attributes(self):
        self.__dimensions: Dict[str, ProjectDimension] = {
            d.id: ProjectDimension(d, self.__project.model.locale)
            for d in self.__project.model.dimensions.values()
        }

    def __getattr__(self, attr: str) -> ProjectDimension:
        return self.__dimensions[attr]

    def __getitem__(self, key: str) -> ProjectDimension:
        return self.__dimensions[key]

    def _repr_html_(self):
        template = environment.get_template("calculations.html.j2")
        return template.render(calculations=self.__project.model.dimensions.values())
