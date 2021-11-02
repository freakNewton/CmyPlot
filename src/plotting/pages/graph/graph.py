# package imports
from dash import dcc, html
import dash_bootstrap_components as dbc

# local imports
from plotting.pages.graph.components import graph_options
from plotting.utils.constants import graph_config

# set constants
path = '/graph'
title = 'Graph'
graph_id = 'id-graph'
x_mean_id = 'x_mean_id'
x_median_id = 'x_median_id'
x_mode_id = 'x_mode_id'
y_mean_id = 'y_mean_id'
y_median_id = 'y_median_id'
y_mode_id = 'y_mode_id'
x_std_id = 'x_std_id'
y_std_id = 'y_std_id'

layout = dbc.Container(
    [
        html.H1('Graph'),
        dbc.Row(
            [
                dbc.Col(
                    # The next update of dash_bootstrap_components includes
                    # an accordian component. The collapse items should be
                    # changed to an accordian.
                    [
                        graph_options.card,
                    ],
                    className='col-lg-3'
                ),
                dbc.Col(
                    [
                        dbc.Row(
                            dcc.Graph(
                                id=graph_id,
                                config=graph_config
                            ),
                            className='col-lg-9'
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div("X Label Mean :"),
                                        html.Div(id = x_mean_id),
                                        html.Br()
                                    ],
                                    className='col-lg-4'    
                                ),
                                dbc.Col(
                                    [
                                        html.Div("X Label Median :"),
                                        html.Div(id = x_median_id),
                                        html.Br()
                                    ],
                                    className='col-lg-4'    
                                ),
                                dbc.Col(
                                    [
                                        html.Div("X Label Mode :"),
                                        html.Div(id = x_mode_id),
                                        html.Br()
                                    ],
                                    className='col-lg-4'    
                                )     
                            ],                            
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div("Y Label Mean :"),
                                        html.Div(id = y_mean_id),
                                        html.Br()
                                    ],
                                    className='col-lg-4'    
                                ),
                                dbc.Col(
                                    [
                                        html.Div("Y Label Median :"),
                                        html.Div(id = y_median_id),
                                        html.Br()
                                    ],
                                    className='col-lg-4'    
                                ),
                                dbc.Col(
                                    [
                                        html.Div("Y Label Mode :"),
                                        html.Div(id = y_mode_id),
                                        html.Br()
                                    ],
                                    className='col-lg-4'    
                                )     
                            ],                            
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Div("X Label Standard Deviation :"),
                                        html.Div(id = x_std_id)
                                    ],
                                    className='col-lg-6'    
                                ),
                                dbc.Col(
                                    [
                                        html.Div("Y Label Standard Deviation :"),
                                        html.Div(id = y_std_id)
                                    ],
                                    className='col-lg-6'    
                                ),        
                            ],                            
                        ),
                    ],
                )
            ]
        )
    ]
)
