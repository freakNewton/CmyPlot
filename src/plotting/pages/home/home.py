# package imports
from dash import html
import dash_bootstrap_components as dbc

# local imports
from plotting.pages.upload import upload

# set contansts
path = "/home"
title = "Home"
layout = dbc.Container(
    [
        html.Div(
            dbc.Container(
                [
                    html.H1(
                        [html.I(className="far fa-chart-bar pr-1"), "CmyPlot"],
                        className="display-3",
                    ),
                    html.P(
                        "Open source online graphing tool.",
                        className="lead",
                    ),
                    html.Hr(className="my-2"),
                    html.P("More text here."),
                    html.P(
                        dbc.Button("Upload data", color="primary", href=upload.path),
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
