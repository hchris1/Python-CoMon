# Comon Python Package

The comon package is a Python library that provides a convenient interface for interacting with the Comon API. This package allows you to create and send status updates, including messages, key performance indicators (KPIs), and various types of charts.

## Installation

To install the comon package, use the following command:

```bash
pip install comon
```

## Usage

You can find an example including all chart types in the [example.py](example.py) file.

To get started, import the necessary modules and create a Client instance. Replace the URL in Client with the actual Comon API URL.

```python
import comon.api as comon_api

client = comon_api.Client("https://localhost:44311")
```

Create your status:

```python
import datetime as dt
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

messages = ["Something was detected."]
kpis = [
    Kpi(name="Sample KPI 1", value=35, unit="ms"),
    Kpi(name="Sample KPI 2", value=22, unit="Watt"),
]

time_based_line_chart = Chart(
    title="Time Based Line Chart",
    sub_title="Some Subtitle",
    type=ChartType.LINE,
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
```

Send the status to Comon:

```python
client.create_status("YOUR_PACKAGE_GUID", status)
```

You can get the package guid in the edit mode of the asset by clicking on the "Copy Package Guid" button. This requires you to create an external package first.
