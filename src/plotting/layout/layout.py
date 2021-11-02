# package imports
from dash import html, dcc

# local imports
# from plotting.layout.navbar 
import navbar
import footer

# constants
store_id = 'id-data-store'
layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        dcc.Store(id=store_id),
        navbar,
        html.Div(id='page-content'),
        footer
    ]
)
