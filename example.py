import comon.api as comon_api
from comon.models import (
    Criticality,
    Status,
    Kpi,
    Chart,
    Series,
    DataPoint,
    ChartType,
    VizType,
)
import datetime as dt

client = comon_api.Client("https://localhost:44311", False)

messages = ["Something was detected."]
kpis = [
    Kpi(name="Sample KPI 1", value=35, unit="ms"),
    Kpi(name="Sample KPI 2", value=22, unit="Watt"),
]

time_based_line_chart = Chart(
    title="Time Based Line Chart",
    sub_title="Some Subtitle",
    type=ChartType.LINE,
    labels=[],
    series=[
        Series(
            name="First Series",
            viz_type=VizType.PRIMARY,
            y_unit="ms",
            data_points=[
                DataPoint(
                    time=dt.datetime.now() - dt.timedelta(seconds=5),
                    y=[3],
                ),
                DataPoint(
                    time=dt.datetime.now() - dt.timedelta(seconds=3),
                    y=[5],
                ),
                DataPoint(
                    time=dt.datetime.now() - dt.timedelta(seconds=1),
                    y=[4],
                ),
            ],
        )
    ],
)

value_based_line_chart = Chart(
    title="Value Based Line Chart",
    sub_title="Some Subtitle",
    type=ChartType.LINE,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.DANGER,
            y_unit="ms",
            data_points=[
                DataPoint(
                    x=1,
                    y=[3],
                ),
                DataPoint(
                    x=2,
                    y=[5],
                ),
                DataPoint(
                    x=3,
                    y=[4],
                ),
            ],
        )
    ],
)

pie_chart = Chart(
    title="Pie Chart",
    sub_title="Some Subtitle",
    labels=["label1", "label2", "label3"],
    type=ChartType.PIE,
    series=[
        Series(
            name="First Series",
            data_points=[
                DataPoint(
                    x=1,
                    y=[30, 70, 20],
                )
            ],
        )
    ],
)

donut_chart = Chart(
    title="Donut Chart",
    sub_title="Some Subtitle",
    labels=["label1", "label2", "label3"],
    type=ChartType.DONUT,
    series=[
        Series(
            name="First Series",
            data_points=[
                DataPoint(
                    x=1,
                    y=[30, 70, 20],
                )
            ],
        )
    ],
)

area_chart = Chart(
    title="Area Chart",
    sub_title="Some Subtitle",
    type=ChartType.AREA,
    series=[
        Series(
            name="First Series",
            y_unit="ms",
            data_points=[
                DataPoint(
                    x=1,
                    y=[3],
                ),
                DataPoint(
                    x=2,
                    y=[5],
                ),
                DataPoint(
                    x=3,
                    y=[4],
                ),
            ],
        )
    ],
)

bar_chart = Chart(
    title="Bar Chart",
    sub_title="Some Subtitle",
    type=ChartType.BAR,
    series=[
        Series(
            name="First Series",
            y_unit="ms",
            data_points=[
                DataPoint(
                    x=1,
                    y=[30],
                ),
                DataPoint(
                    x=2,
                    y=[70],
                ),
                DataPoint(
                    x=3,
                    y=[20],
                ),
            ],
        )
    ],
)

heatmap_chart = Chart(
    title="Heatmap Chart",
    sub_title="Some Subtitle",
    labels=["label1", "label2", "label3"],
    type=ChartType.HEAT_MAP,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.DANGER,
            data_points=[
                DataPoint(
                    x=1,
                    y=[30, 70, 20],
                ),
            ],
        )
    ],
)

polar_area_chart = Chart(
    title="Polar Area Chart",
    sub_title="Some Subtitle",
    labels=["label1", "label2", "label3"],
    type=ChartType.POLAR_AREA,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.DANGER,
            data_points=[
                DataPoint(
                    x=1,
                    y=[30, 70, 20],
                ),
            ],
        )
    ],
)

radar_chart = Chart(
    title="Radar Chart",
    sub_title="Some Subtitle",
    labels=["label1", "label2", "label3"],
    type=ChartType.RADAR,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.DANGER,
            data_points=[
                DataPoint(
                    x=1,
                    y=[30, 70, 20],
                ),
            ],
        )
    ],
)

radial_bar_chart = Chart(
    title="Radial Bar Chart",
    sub_title="Some Subtitle",
    labels=["label1", "label2", "label3"],
    type=ChartType.RADIAL_BAR,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.DANGER,
            data_points=[
                DataPoint(
                    x=1,
                    y=[30, 70, 20],
                ),
            ],
        )
    ],
)

range_area_chart = Chart(
    title="Range Area Chart",
    sub_title="Some Subtitle",
    type=ChartType.RANGE_AREA,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.SUCCESS,
            y_unit="ms",
            data_points=[
                DataPoint(
                    x=1,
                    y=[3, 4],
                ),
                DataPoint(
                    x=2,
                    y=[5, 6],
                ),
                DataPoint(
                    x=3,
                    y=[4, 5],
                ),
            ],
        )
    ],
)

scatter_chart = Chart(
    title="Scatter Chart",
    sub_title="Some Subtitle",
    type=ChartType.SCATTER,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.PRIMARY,
            y_unit="ms",
            data_points=[
                DataPoint(
                    x=1,
                    y=[3],
                ),
                DataPoint(
                    x=2,
                    y=[5],
                ),
                DataPoint(
                    x=3,
                    y=[4],
                ),
            ],
        )
    ],
)

tree_map_chart = Chart(
    title="Tree Map",
    sub_title="Some Subtitle",
    type=ChartType.TREE_MAP,
    series=[
        Series(
            name="First Series",
            viz_type=VizType.PRIMARY,
            data_points=[
                DataPoint(
                    tag="tag1",
                    y=[3],
                ),
                DataPoint(
                    tag="tag2",
                    y=[5],
                ),
                DataPoint(
                    tag="tag3",
                    y=[4],
                ),
            ],
        )
    ],
)

status = Status(
    criticality=Criticality.WARNING,
    messages=messages,
    kpis=kpis,
    charts=[
        value_based_line_chart,
        time_based_line_chart,
        pie_chart,
        donut_chart,
        area_chart,
        bar_chart,
        heatmap_chart,
        polar_area_chart,
        radar_chart,
        radial_bar_chart,
        range_area_chart,
        scatter_chart,
        tree_map_chart,
    ],
)


client.create_status("810d8d56-9fe4-452e-8248-c0cbf8208866", status)
