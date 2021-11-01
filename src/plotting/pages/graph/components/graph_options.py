# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports

# set constants
# collapse functionality
toggler = 'id-options-toggler'
collapse = 'id-options-collapse'

# option inputs
# attributes
x_att = 'X-Axis'
y_att = 'Y-Axis'
size = 'Size'
color = 'Color'
attributes = [x_att, y_att, size, color]
att_drop = 'id-att-dropdown'
# labels
x_lab = 'X Label'
y_lab = 'Y Label'
title = 'Title'
labels = [title, x_lab, y_lab]
label_input = 'id-label-input'
# other
graph_type = 'id-options-graph-type'
graph_height = 'id-options-height'
# Hover options
column_attr = 'Columns'
columns = [column_attr]
hover_input = 'id-hover-dropdown'

def create_hover_dropdown(columns, id):
    """Create attribute dropdowns

    Parameters
    ----------
        attributes: list
            list of strings for attributes

    Returns
    ----------
        children: list of components
            Componets to be added with the dropdown
    """

    children = [html.H4('Hover Options')]

    for i, att in enumerate(columns):
        children.append(html.H6(att + ':'))
        children.append(
            dcc.Dropdown(
                id={
                    'type': id,
                    'index': i
                },
                className='dash-bootstrap'
            )
        )

    return children


def create_attribute_dropdown(attributes, id):
    """Create attribute dropdowns

    Parameters
    ----------
        attributes: list
            list of strings for attributes

    Returns
    ----------
        children: list of components
            Componets to be added with the dropdown
    """

    children = [html.H4('Attributes')]

    for i, col in enumerate(attributes):
        children.append(html.H6(col + ':'))
        children.append(
            dcc.Dropdown(
                id={
                    'type': id,
                    'index': i
                },
                className='dash-bootstrap'
            )
        )

    return children


def create_label_dropdown(labels, id):
    """Create attribute dropdowns

    Parameters
    ----------
        labels: list
            list of strings for labels

    Returns
    ----------
        children: list of components
            Componets to be added with the dropdown
    """

    children = [html.H4('Labels')]

    for i, lab in enumerate(labels):
        children.append(html.H6(lab + ':'))
        children.append(
            dcc.Input(
                id={
                    'type': id,
                    'index': i
                },
                type='text',
                className='dash-bootstrap'
            )
        )

    return children


# components
card = dbc.Card(
    [
        dbc.CardHeader(
            html.H3(
                dbc.Button(
                    'Graph Options',
                    color='link',
                    id=toggler
                )
            )
        ),
        dbc.Collapse(
            dbc.CardBody(
                [
                    html.Div(create_hover_dropdown(columns, hover_input)),
                    html.Hr(),
                    html.Div(create_attribute_dropdown(attributes, att_drop)),
                    html.Hr(),
                    html.Div(create_label_dropdown(labels, label_input)),
                    html.Hr(),
                    html.H4('Other'),
                    html.H6('Graph Type:'),
                    dcc.Dropdown(
                        id=graph_type,
                        options=[{'label': 'Scatter Plot', 'value': 'scatter'},
                                 {'label': 'Line Plot', 'value': 'line'},
                                 {'label': 'Bar Plot', 'value': 'bar'}],
                        # disabled=True
                        value='scatter'
                    ),
                    html.H6('Height (px):'),
                    dcc.Input(
                        id=graph_height,
                        type='number',
                        min=100,
                        max=1000,
                        step=50,
                        value=700
                    )
                ]
            ),
            id=collapse
        )
    ]
)
