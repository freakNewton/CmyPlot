# package imports
import dash_bootstrap_components as dbc
from dash import dcc, html

# local imports
from plotting.pages.graph.components import graph_options
from plotting.utils.constants import graph_config

# set constants
path = "/graph"
title = "Graph"
graph_id = "id-graph"

layout = dbc.Container(
    [
        html.H1("Graph"),
        dbc.Row(
            [
                dbc.Col(
                    # The next update of dash_bootstrap_components includes
                    # an accordian component. The collapse items should be
                    # changed to an accordian.
                    [
                        graph_options.card,
                    ],
                    className="col-lg-3",
                ),
                dbc.Col(
                    dcc.Graph(id=graph_id, config=graph_config), className="col-lg-9"
                ),
            ]
        ),
    ]
)
