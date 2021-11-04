# package imports
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# local imports
from plotting.app import app
from plotting.layout.layout import store_id
from plotting.pages.table import table
from plotting.utils.functions import fetch_columns_options


@app.callback(
    Output(table.table_id, "data"),
    Output(table.table_id, "columns"),
    Input(store_id, "data"),
)
def initialize_table_data(data):
    """Handle setting table data

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        data: dict
            Data from stored dcc.Store component
    """
    if data is None:
        raise PreventUpdate

    cols = fetch_columns_options(data["df"], table=True)
    return data["df"], cols
