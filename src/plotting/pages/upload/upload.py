# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports
from plotting.pages.table import table
from plotting.pages.graph import graph

# set constants
path = "/upload"
title = "Upload"
upload_id = "id-upload-data"
info_id = "id-upload-info"
buttons_id = "id-upload-redirect-buttons"

layout = dbc.Container(
    [
        html.Div(
            dbc.Container(
                [
                    html.H1(
                        [html.I(className="fas fa-file-upload pr-1"), "Upload file"],
                        className="display-3",
                    ),
                    dcc.Upload(
                        [
                            "Drag and Drop or Click to upload",
                        ],
                        style={
                            "width": "100%",
                            "height": "60px",
                            "lineHeight": "60px",
                            "borderWidth": "1px",
                            "borderStyle": "dashed",
                            "borderRadius": "5px",
                            "textAlign": "center",
                        },
                        id=upload_id,
                        className="lead",
                    ),
                    html.Hr(className="my-2"),
                    html.Div(id=info_id),
                    html.P(
                        [
                            dbc.Button(
                                html.Big("Table"),
                                color="success",
                                disabled=True,
                                className="mr-2",
                                id={"type": buttons_id, "index": 0},
                                href=table.path,
                            ),
                            dbc.Button(
                                html.Big("Graph"),
                                color="info",
                                disabled=True,
                                id={"type": buttons_id, "index": 1},
                                href=graph.path,
                            ),
                        ],
                        className="lead",
                    ),
                ],
                fluid=True,
                className="py-3",
            ),
            className="my-2 bg-light rounded-3",
        )
    ]
)
