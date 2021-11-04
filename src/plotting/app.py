# package imports
import dash
import dash_bootstrap_components as dbc
from flask_caching import Cache
import os
from dash import dcc

# local imports
from src.plotting.layout.layout import layout
from src.plotting.layout.layout import layout
from src.plotting.layout.layout import store_id

cwd = os.getcwd()
assets_path = os.path.join(
    cwd, 'src', 'plotting', 'assets'
)

# create app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True,
    title='CmyPlot',
    assets_folder=assets_path
)

# set up cache
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})

# set initial layout
app.layout = layout
dcc.Store(id=store_id, storage_type='session')
