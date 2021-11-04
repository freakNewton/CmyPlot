# package imports
import statistics
from dash.dependencies import ALL, Input, Output, State
from dash.exceptions import PreventUpdate
from dash import callback_context
import plotly.io as pio
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import plotly.express as px
import smtplib
import numpy as np
# from pandas.api.types import is_integer_dtype
# local imports
from src.plotting.app import app
from src.plotting.layout.layout import store_id
from src.plotting.utils import functions as func
from src.plotting.pages.graph.components import graph_options as go
from src.plotting.pages.graph import graph
import joblib

sender_email = 'cmyplot@gmail.com'
sender_pwd = 'Cmyplot@123'
receiver_email = 'cmyplot@gmail.com'

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
    # print(data, type(()))
    # dcc.Store(id="uploaddata", data=json.dumps(data), storage_type='session')
    options = func.fetch_columns_options(data['df'])

    return [options for i in range(len(go.attributes))]


@app.callback(
    Output({'type': go.hover_input, 'index': ALL}, 'options'),
    Input(store_id, 'data')
)
def fetch_hover_columns_from_data(data):
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

    return [options for i in range(len(go.columns))]


@app.callback(
    Output(graph.graph_id, 'figure'),
    Output(graph.x_mean_id, component_property='children'),
    Output(graph.x_median_id, component_property='children'),
    Output(graph.x_mode_id, component_property='children'),
    Output(graph.y_mean_id, component_property='children'),
    Output(graph.y_median_id, component_property='children'),
    Output(graph.y_mode_id, component_property='children'),
    Output(graph.x_std_id, component_property='children'),
    Output(graph.y_std_id, component_property='children'),
    Input(store_id, 'data'),
    Input({'type': go.att_drop, 'index': ALL}, 'value'),
    Input({'type': go.label_input, 'index': ALL}, 'value'),
    Input({'type': go.hover_input, 'index': ALL}, 'value'),
    Input(go.graph_height, 'value'),
    Input(go.graph_type, 'value')
)
def create_figure(data, att_values, label_values, hover_values, height, 
                  graph_type):
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
    if not func.validate_store_data(data) or all(i is None for i in att_values) or all(i is None for i in hover_values):
        raise PreventUpdate
    # zip keys with values for easy dictionary access
    attributes = dict(zip(go.attributes, att_values))
    labels = dict(zip(go.labels, label_values))
    hover = dict(zip(go.columns, hover_values))

    # prep data
    df = pd.DataFrame(data['df'])

    # Set the x and y axis labels
    graph_labels = {}

    x_att = attributes[go.x_att]
    x_lab = labels[go.x_lab]
    graph_labels[x_att] = x_lab if (x_att and x_lab) else x_att

    x_mean = "X label is Not a Number"
    x_median = "X label is Not a Number"
    x_mode = "X label is Not a Number"
    if(df[x_att].dtype == np.float64 or df[x_att].dtype == np.int64):
        x_mean = round(statistics.mean(df[x_att]), 2)
        x_median = round(statistics.median(df[x_att]), 2)
        x_mode = round(statistics.mode(df[x_att]), 2)
    y_mean = "Y label is Not a Number"
    y_median = "Y label is Not a Number"
    y_mode = "Y label is Not a Number"

    y_att = attributes[go.y_att]
    y_lab = labels[go.y_lab]
    graph_labels[y_att] = y_lab if (y_att and y_lab) else y_att
    # print(statistics.mean(df[y_att]))
    # print(statistics.median(df[y_att]))
    # print(statistics.mode(df[y_att]))

    if(df[y_att].dtype == np.float64 or df[y_att].dtype == np.int64):
        y_mean = round(statistics.mean(df[y_att]), 2)
        y_median = round(statistics.median(df[y_att]), 2)
        y_mode = round(statistics.mode(df[y_att]), 2)
    x_std = "X label is Not a Number"
    if(df[x_att].dtype == np.float64 or df[x_att].dtype == np.int64):
        x_std = round(statistics.stdev(df[x_att]))
    y_std = "Y label is Not a Number"
    if(df[y_att].dtype == np.float64 or df[y_att].dtype == np.int64):
        y_std = round(statistics.stdev(df[y_att]))

    hover_column = hover[go.column_attr]
    if(graph_type == 'scatter'):
        figure = px.scatter(
            df,
            x=x_att,
            y=y_att,
            size=attributes[go.size],
            color=attributes[go.color],
            title=labels[go.title],
            labels=graph_labels,
            height=height,
            hover_data=[hover_column]
        )
    elif(graph_type == 'bar'):
        figure = px.bar(
            df,
            x=x_att,
            y=y_att,
            # size=attributes[go.size],
            color=attributes[go.color],
            title=labels[go.title],
            labels=graph_labels,
            height=height,
            hover_data=[hover_column]
        )
    elif(graph_type == 'line'):
        figure = px.line(
            df,
            x=x_att,
            y=y_att,
            # size=attributes[go.size],
            color=attributes[go.color],
            title=labels[go.title],
            labels=graph_labels,
            height=height,
            hover_data=[hover_column]
        )
    joblib.dump(figure, "src/plotting/assets/images/fig.pkl")

    return figure, x_mean, x_median, x_mode, y_mean, y_median, y_mode, x_std, y_std


@app.callback(
    Output('share-modal', 'is_open'),
    [Input('share-button', 'n_clicks'), Input('send-button', 'n_clicks')],
    [State("share-modal", "is_open"), State('email-id', 'value'), State('email-message', 'value')]
)
def share_graph(n1, n2, is_open, emailid, msg):
    if(is_open is True):
        print(emailid, msg)
        receiver_email = emailid
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            # restoring graph object pkl
            temp = joblib.load("src/plotting/assets/images/fig.pkl")
            pio.write_image(temp, "src/plotting/assets/images/graph.png")
            # saving graph image locally
            with open("src/plotting/assets/images/graph.png", 'rb') as f:
                img_data = f.read()
            # initlializing message object for email
            message = MIMEMultipart()
            message['SUBJECT'] = 'CmyPlot'
            image = MIMEImage(img_data, name="graph.png")
            message.attach(image)   # attaching graph image
            message.attach(MIMEText(msg))  # attaching text message
            # Identify ourselves with the mail server we are using.
            smtp.ehlo()
            # Encrypt our connection
            smtp.starttls()
            # Reidentify our connection as encrypted with the mail server
            smtp.ehlo()
            smtp.login(sender_email, sender_pwd)
            smtp.sendmail(sender_email, receiver_email, message.as_string())
            smtp.quit()
    if(n1 or n2):
        return not is_open
    return is_open
