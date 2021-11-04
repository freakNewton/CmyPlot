# package imports
import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container(
    [
        html.Div(
            dbc.Container(
                [
                    html.H1(
                        [
                            html.I(className="fas fa-skull-crossbones"),
                            "404 Error",
                            html.I(className="fas fa-skull-crossbones"),
                        ],
                        className="display-3",
                    ),
                    html.P(
                        "Page not found.",
                        className="lead",
                    ),
                    html.Hr(className="my-2"),
                    html.P(
                        dbc.Button("Home", color="primary", href="/"), className="lead"
                    ),
                ],
                fluid=True,
                className="py-3",
            ),
            className="my-2 bg-light rounded-3",
        )
    ]
)
