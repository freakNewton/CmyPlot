# package imports
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# local imports
from plotting.app import app
from plotting.utils.functions import fetch_columns_options
from plotting.pages.table import table
from plotting.layout.layout import store_id



@app.callback(
    Output(table.table_id, 'data'),
    Output(table.table_id, 'columns'),
    Input(table.table_id, "page_current"),
    Input(table.table_id, "page_size"),
    Input(store_id, 'data')
)
def initialize_table_data(page_current,page_size,data):
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
    # print(type(data['df']))

    cols = fetch_columns_options(data['df'], table=True)
    # data = data.iloc[
    #     page_current*page_size:(page_current+ 1)*page_size
    # ].to_dict('records')
    temp = data['df'][page_current*page_size:(page_current+ 1)*page_size]
    print(len(temp), len(data['df']))

    return temp,cols


@app.callback(
    Output(table.table_id_x, 'data'),
    Output(table.table_id_x, 'columns'),
    Input(store_id, 'data')
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
    # print(type(data['df']))

    cols = fetch_columns_options(data['df'], table=True)
    # data = data.iloc[
    #     page_current*page_size:(page_current+ 1)*page_size
    # ].to_dict('records')

    return data['df'],cols

# @app.callback(
#     Output('page_count','children'),
#     Input(store_id, 'data')
# )
# def createComponent(data):
#     if data is None:
#         raise PreventUpdate

#     return dbc.Input(
#             id='datatable-page-count',
#             type='number',
#             min=1,
#             max=len(data['df']),
#             value=1
#         )

# @app.callback(
#     Output('get_max','children'),
#     Input(store_id, 'data'))
# def get_maximum_cols(data):
#     if data is None:
#         raise PreventUpdate

#     return len(data['df'])


@app.callback(
    Output(table.table_id, 'page_count'),
    Input(table.use_page_count, 'value'),
    Input(table.page_count, 'value'))
def update_table(use_page_count, page_count_value):
    if len(use_page_count) == 0 or page_count_value is None:
        return None
    return page_count_value
