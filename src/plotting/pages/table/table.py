# package imports
import dash_bootstrap_components as dbc
from dash import dash_table, html

# local imports
from plotting.utils import color

# set constants
path = "/table"
title = "Table"
table_id = "id-table"

layout = dbc.Container(
    [
        html.H1("Table"),
        dash_table.DataTable(
            id=table_id,
            page_size=20,
            sort_action="native",
            filter_action="native",
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": color.light_grey}
            ],
            style_header={"backgroundColor": color.dark_grey},
            style_table={"overflowX": "auto"},
            style_cell={
                "maxWidth": "180px",
                "overflow": "hidden",
                "textOverflow": "ellipsis",
            },
        ),
    ]
)
