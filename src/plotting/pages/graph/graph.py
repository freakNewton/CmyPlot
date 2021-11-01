# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports
from plotting.pages.graph.components import graph_options
from plotting.utils.constants import graph_config

# set constants
path = '/graph'
title = 'Graph'
graph_id = 'id-graph'

layout = dbc.Container(
    [
        html.H1('Graph'),
        dbc.Row(
            [
                dbc.Col(
                    # The next update of dash_bootstrap_components includes
                    # an accordian component. The collapse items should be
                    # changed to an accordian.
                    [
                        graph_options.card,
                    ],
                    className='col-lg-3'
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            html.Div([
                                dbc.Button('Share', id='share-button',
                                           n_clicks=0,
                                           className="btn, btn-primary"),
                                dbc.Modal(
                                    [
                                        dbc.ModalHeader(
                                            dbc.ModalTitle("Share")
                                        ),
                                        dbc.ModalBody("Share"),
                                        dbc.ModalFooter(
                                            dbc.Button(
                                                "Send", id="send-button",
                                                className="ms-auto, btn, btn-primary", n_clicks=0
                                            )
                                        )
                                    ],
                                    id="share-modal",
                                    is_open=False
                                )
                            ]),
                            className='float-right'
                        ),
                        dbc.Row(
                            dcc.Graph(
                                id=graph_id,
                                config=graph_config
                            )
                        ),
                        # dcc.Store(id="graphstore", storage_type="session")
                    ],
                    className='col-lg-9'
                )
            ]
        )
    ]
)
