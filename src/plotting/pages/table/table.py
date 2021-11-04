# package imports
from dash import dash_table, html
import dash_bootstrap_components as dbc

# local imports
from src.plotting.utils import color,functions

# set constants
path = '/table'
title = 'Table'
table_id = 'id-table'
table_id_x='id-table-x'
use_page_count = 'datatable-use-page-count'
page_count = 'datatable-page-count'
page_size = 'id-page-size'

layout = dbc.Container([
    html.H1('Table'),
    dash_table.DataTable(
        id=table_id,
        # page_size=20,
        page_current=0,
        page_size=10,
        page_action='custom',
        # sort_action='native',
        #filter_action='native',
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': color.light_grey
            }
        ],
        style_header={
            'backgroundColor': color.dark_grey
        },
        style_table={'overflowX': 'auto'},
        style_cell={
            'maxWidth': '180px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis'
        }
    ),
    html.Br(),
    dbc.Checklist(
        id=use_page_count,
        options=[
            {'label': 'Use page_count', 'value': 'True'}
        ],
        value=['True']
    ),
    # 'Page count: ',
    # html.Div(id='page_count'),
    #     'Page count: ',
    dbc.Input(
        id=page_count,
        type='number',
        min=1,
        max=50,
        value=20
    ),
    dbc.Input(
        id=page_size,
        type='number'
    ),
    html.H1('Table'),
    dash_table.DataTable(
        id=table_id_x,
        page_size=20,
        sort_action='native',
        filter_action='native',
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': color.light_grey
            }
        ],
        style_header={
            'backgroundColor': color.dark_grey
        },
        style_table={'overflowX': 'auto'},
        style_cell={
            'maxWidth': '180px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis'
        }
    )
])
