# package imports
from dash import dcc, html

from plotting.layout.footer import footer
# local imports
from plotting.layout.navbar import navbar

# constants
store_id = "id-data-store"
layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        dcc.Store(id=store_id),
        navbar,
        html.Div(id="page-content"),
        footer,
    ]
)
