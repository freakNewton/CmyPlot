# package imports
from dash.dependencies import ALL, Input, Output, State
from dash.exceptions import PreventUpdate
from dash import callback_context
import pandas as pd
import plotly.express as px

# local imports
from src.plotting.app import app
from src.plotting.layout.layout import store_id
from src.plotting.utils import functions as func
from src.plotting.pages.graph.components import graph_options as go
from src.plotting.pages.graph import graph


@app.callback(
    Output(go.collapse, 'is_open'),
    Input(go.toggler, 'n_clicks'),
    State(go.collapse, 'is_open')
)
def handle_accordian_collapse(go_clicks, go_open):
    """Handle toggling the various accordian collapses

    Parameters
    ----------
        temp_clicks: int
            How many times the temp link has been clicked
        temp_open: bool
            Whether the temp card is currenlty open or not

    Returns
    ----------
        temp_open: bool
            The reverse of what temp_open passed in
    """

    # Extract button id from triggered context
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Open specific accordian item
    if button_id == go.toggler and go_clicks:
        return not go_open
    else:
        raise PreventUpdate


@app.callback(
    Output({'type': go.att_drop, 'index': ALL}, 'options'),
    Input(store_id, 'data')
)
def fetch_columns_from_data(data):
    """Handle options for graph option dropdowns

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        options: list of dict
            Options for each of the dropdowns in the form of
            {'label': 'Example', 'value': 'example'}
    """

    if not func.validate_store_data(data):
        raise PreventUpdate

    options = func.fetch_columns_options(data['df'])

    return [options for i in range(len(go.attributes))]


@app.callback(
    Output(graph.graph_id, 'figure'),
    Input(store_id, 'data'),
    Input({'type': go.att_drop, 'index': ALL}, 'value'),
    Input({'type': go.label_input, 'index': ALL}, 'value'),
    Input(go.graph_height, 'value'),
    Input(go.graph_type, 'value')
)
def create_figure(data, att_values, label_values, height, graph_type):
    """Handle options for graph option dropdowns

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component
        att_values: list
            List of values returned from the attribute dropdowns
        label_values: list
            List of values for various labels
        height: int
            Height of graph in pixels

    Returns
    ----------
        figure: plotly.graph_objects.Figure
            Created graph object
    """
    
    if not func.validate_store_data(data) or all(i is None for i in att_values):
        raise PreventUpdate

    # zip keys with values for easy dictionary access
    attributes = dict(zip(go.attributes, att_values))
    labels = dict(zip(go.labels, label_values))

    # prep data
    df = pd.DataFrame(data['df'])

    # Set the x and y axis labels
    graph_labels = {}

    x_att = attributes[go.x_att]
    x_lab = labels[go.x_lab]
    graph_labels[x_att] = x_lab if (x_att and x_lab) else x_att

    y_att = attributes[go.y_att]
    y_lab = labels[go.y_lab]
    graph_labels[y_att] = y_lab if (y_att and y_lab) else y_att

    # create the scatter plot
    if(graph_type == 'scatter'):
        figure = px.scatter(
            df,
            x=x_att,
            y=y_att,
            size=attributes[go.size],
            color=attributes[go.color],
            title=labels[go.title],
            labels=graph_labels,
            height=height
        )
    elif(graph_type == 'bar'):
        figure = px.bar(
            df,
            x=x_att,
            y=y_att,
            # size=attributes[go.size],
            color=attributes[go.color],
            title=labels[go.title],
            labels=graph_labels,
            height=height
        )
    elif(graph_type == 'line'):
        figure = px.line(
            df,
            x=x_att,
            y=y_att,
            # size=attributes[go.size],
            color=attributes[go.color],
            title=labels[go.title],
            labels=graph_labels,
            height=height
        )

    return figure
