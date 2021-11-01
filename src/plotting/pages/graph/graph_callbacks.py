# package imports
from dash.dependencies import ALL, Input, Output, State
from dash.exceptions import PreventUpdate
from dash import callback_context
from dash import dcc
import email as email
from plotly.io import to_image
from email.mime.image import MIMEImage
import pandas as pd
import plotly.express as px
import smtplib
# local imports
from plotting.app import app
from plotting.layout.layout import store_id
from plotting.utils import functions as func
from plotting.pages.graph.components import graph_options as go
from plotting.pages.graph import graph

sender_email = 'cmyplot@gmail.com'
sender_pwd = 'Cmyplot@123'
receiver_email = 'simranbosmiya3571@gmail.com'


@app.callback(
    Output(go.collapse, 'is_open'),
    Input(go.toggler, 'n_clicks'),
    State(go.collapse, 'is_open')
)
def handle_accordian_collapse(go_clicks, go_open):
    """Handle toggling the various accordian collapses

    Parameters
    ----------
        temp_clicks: int
            How many times the temp link has been clicked
        temp_open: bool
            Whether the temp card is currenlty open or not

    Returns
    ----------
        temp_open: bool
            The reverse of what temp_open passed in
    """

    # Extract button id from triggered context
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Open specific accordian item
    if button_id == go.toggler and go_clicks:
        return not go_open
    else:
        raise PreventUpdate


@app.callback(
    Output({'type': go.att_drop, 'index': ALL}, 'options'),
    Input(store_id, 'data')
)
def fetch_columns_from_data(data):
    """Handle options for graph option dropdowns

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        options: list of dict
            Options for each of the dropdowns in the form of
            {'label': 'Example', 'value': 'example'}
    """

    if not func.validate_store_data(data):
        raise PreventUpdate

    options = func.fetch_columns_options(data['df'])

    return [options for i in range(len(go.attributes))]


@app.callback(
    Output(graph.graph_id, 'figure'),
    Input(store_id, 'data'),
    Input({'type': go.att_drop, 'index': ALL}, 'value'),
    Input({'type': go.label_input, 'index': ALL}, 'value'),
    Input(go.graph_height, 'value')
)
def create_figure(data, att_values, label_values, height):
    """Handle options for graph option dropdowns

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component
        att_values: list
            List of values returned from the attribute dropdowns
        label_values: list
            List of values for various labels
        height: int
            Height of graph in pixels

    Returns
    ----------
        figure: plotly.graph_objects.Figure
            Created graph object
    """

    if not func.validate_store_data(data) or all(i is None for i in att_values):
        raise PreventUpdate

    # zip keys with values for easy dictionary access
    attributes = dict(zip(go.attributes, att_values))
    labels = dict(zip(go.labels, label_values))

    # prep data
    df = pd.DataFrame(data['df'])

    # Set the x and y axis labels
    graph_labels = {}

    x_att = attributes[go.x_att]
    x_lab = labels[go.x_lab]
    graph_labels[x_att] = x_lab if (x_att and x_lab) else x_att

    y_att = attributes[go.y_att]
    y_lab = labels[go.y_lab]
    graph_labels[y_att] = y_lab if (y_att and y_lab) else y_att

    # create the scatter plot
    figure = px.scatter(
        df,
        x=x_att,
        y=y_att,
        size=attributes[go.size],
        color=attributes[go.color],
        title=labels[go.title],
        labels=graph_labels,
        height=height
    )
    # print(type(figure), figure.to_json())
    # dcc.Store(id="graphstore", data=figure.to_json(), storage_type='session')
    return figure


@app.callback(
    Output('share-modal', 'is_open'),
    [Input('share-button', 'n_clicks'), Input('send-button', 'n_clicks')],
    #  Input(graph.graph_id.format('graphstore'), 'graph_id')
    State("share-modal", "is_open")
)
def share_graph(n1, n2, is_open):
    print(is_open)
    if(is_open is True):
        message = "Hello"
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            # Identify ourselves with the mail server we are using.
            smtp.ehlo()
            # Encrypt our connection
            smtp.starttls()
            # Reidentify our connection as encrypted with the mail server
            smtp.ehlo()
            smtp.login(sender_email, sender_pwd)
            # print(type(figure), figure)

            # -----------------------
            # plot_img = to_image(figure)
            # -----------------------

            # print(type(plot_img), plot_img)
            # message = MIMEImage()
            # message.attach(plot_img, subtype='.png',
            #                _encoder=email.encoders.encode_base64)
            smtp.sendmail(sender_email, receiver_email, message)
    if(n1 or n2):
        return not is_open
    return is_open
