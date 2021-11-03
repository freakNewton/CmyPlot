import pandas as pd
import plotly
import random

from plotting.pages.graph import graph_callbacks as gc
from plotting.pages.graph.components import graph_options as go

df = pd.DataFrame({
    'x1': [0, 1, 2],
    'x2': [6, 7, 8],
    'y': [0, 0, 0]
})
data = {'df': df.to_dict('records')}
graph_types = ["line", "bar", "scatter"]


def test_handle_accordian_collapse():
    pass
    # since this method uses callback context, we are unable to test it here
    # this will need to be a UI test


def test_fetch_columns_from_data():

    expected = len(go.attributes)
    output = gc.fetch_columns_from_data.__wrapped__(data)
    assert len(output) == expected


def test_create_figure():

    cols = list(data['df'][0].keys())
    att_values = [random.choice(cols) for i in go.attributes]
    label_values = [random.choice(cols) for i in go.labels]
    hover_values = [random.choice(cols) for i in go.hover_input]
    height = 500
    graph_type = random.choice(graph_types)
    output = gc.create_figure.__wrapped__(data, att_values, label_values, hover_values, height,graph_type)

    assert isinstance(output[0], plotly.graph_objects.Figure)
    # Not sure what exactly to test here.
    # This is the output of the above function
    #
    # Figure({
    #     'data': [{'hovertemplate': 'x2=%{x}<br>x1=%{marker.color}<br>y=%{marker.size}<extra></extra>',
    #             'legendgroup': '',
    #             'marker': {'color': array([0, 1, 2], dtype=int64),
    #                         'coloraxis': 'coloraxis',
    #                         'size': array([0, 0, 0], dtype=int64),
    #                         'sizemode': 'area',
    #                         'sizeref': 0.0,
    #                         'symbol': 'circle'},
    #             'mode': 'markers',
    #             'name': '',
    #             'orientation': 'v',
    #             'showlegend': False,
    #             'type': 'scatter',
    #             'x': array([6, 7, 8], dtype=int64),
    #             'xaxis': 'x',
    #             'y': array([0, 1, 2], dtype=int64),
    #             'yaxis': 'y'}],
    #     'layout': {'coloraxis': {'colorbar': {'title': {'text': 'x1'}},
    #                             'colorscale': [[0.0, '#0d0887'], [0.1111111111111111,
    #                                             '#46039f'], [0.2222222222222222,
    #                                             '#7201a8'], [0.3333333333333333,
    #                                             '#9c179e'], [0.4444444444444444,
    #                                             '#bd3786'], [0.5555555555555556,
    #                                             '#d8576b'], [0.6666666666666666,
    #                                             '#ed7953'], [0.7777777777777778,
    #                                             '#fb9f3a'], [0.8888888888888888,
    #                                             '#fdca26'], [1.0, '#f0f921']]},
    #             'height': 500,
    #             'legend': {'itemsizing': 'constant', 'tracegroupgap': 0},
    #             'template': '...',
    #             'title': {'text': 'x2'},
    #             'xaxis': {'anchor': 'y', 'domain': [0.0, 1.0], 'title': {'text': 'x2'}},
    #             'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'x1'}}}
    # })
