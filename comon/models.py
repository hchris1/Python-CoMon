import datetime as dt
from dataclasses import dataclass, asdict
from enum import Enum


@dataclass
class Criticality(Enum):
    HEALTHY = 1
    WARNING = 3
    ALERT = 5


@dataclass
class Kpi:
    name: str
    value: float | None
    unit: str

    def __init__(self, name: str, value: float | None, unit: str):
        self.name = name
        self.value = value
        self.unit = unit


@dataclass
class VizType(Enum):
    PRIMARY = 0
    SECONDARY = 1
    SUCCESS = 2
    DANGER = 3
    WARNING = 4
    INFO = 5


@dataclass
class DataPoint:
    time: str | None
    tag: str | None
    x: float | None
    y: list[float]

    def __init__(self, y, time: dt.datetime = None, tag=None, x: float | None = None):
        self.time = time.isoformat() if time else None
        self.tag = tag
        self.x = x
        self.y = y


@dataclass
class Series:
    name: str
    viz_type: int
    x_unit: str
    y_unit: str
    data_points: list[DataPoint]

    def __init__(
        self,
        name: str,
        data_points: list[DataPoint],
        viz_type: VizType = VizType.PRIMARY,
        x_unit: str = None,
        y_unit: str = None,
    ):
        self.name = name
        self.viz_type = viz_type.value
        self.x_unit = x_unit
        self.y_unit = y_unit
        self.data_points = data_points


@dataclass
class ChartType(Enum):
    LINE = 1
    AREA = 2
    BAR = 3
    PIE = 4
    DONUT = 5
    RADIAL_BAR = 6
    SCATTER = 7
    HEAT_MAP = 8
    RADAR = 9
    POLAR_AREA = 10
    RANGE_AREA = 11
    TREE_MAP = 12


@dataclass
class Chart:
    title: str
    sub_title: str
    labels: list[str]
    type: int
    series: list[Series]

    def __init__(
        self,
        title: str,
        type: ChartType,
        series: list[Series],
        sub_title: str = None,
        labels: list[str] = [],
    ):
        self.title = title
        self.sub_title = sub_title
        self.labels = labels
        self.type = type.value
        self.series = series


@dataclass
class Status:
    criticality: int
    messages: list[str]
    kpis: list[Kpi]
    charts: list[Chart]

    def __init__(
        self,
        criticality: Criticality,
        messages: list[str] = [],
        kpis: list[Kpi] = [],
        charts: list[Chart] = [],
    ):
        self.criticality = criticality.value
        self.messages = messages
        self.kpis = kpis
        self.charts = charts

    def json(self):
        return asdict(self)
