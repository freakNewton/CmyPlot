# package imports
import base64
import io
from dash.dependencies import ALL, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# local imports
from plotting.app import app
from plotting.pages.upload import upload
from plotting.layout.layout import store_id
from plotting.utils import functions as func


@app.callback(
    Output(upload.info_id, "children"),
    Output(store_id, "data"),
    Input(upload.upload_id, "contents"),
    State(upload.upload_id, "filename"),
)
def update_upload(contents, filename):
    """Handle uploading data

    Parameters
    ----------
        contents: str
            base64 string that contains contents of uploaded file
        filename: str
            Name of file being uploaded

    Returns
    ----------
        text: list or str
            list of components or str of output text
        data: dict
            Dictionary that contains data from uploaded file
    """

    if filename is None:
        raise PreventUpdate

    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)

    try:
        if filename.endswith(".csv"):
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8", "replace")))
        else:
            raise Exception
    except Exception as e:
        print(e)
        error_text = "Error uploading, something is wrong with the file."
        return error_text, None

    succ_text = "File uploaded successfully: " + filename
    return succ_text, {"df": df.to_dict("records")}


@app.callback(
    Output({"type": upload.buttons_id, "index": ALL}, "disabled"),
    Input(store_id, "data"),
)
def set_button_status(data):
    """Set buttons to disabled or not

    Parameters
    ----------
        data: dict
            data from stored dcc.Store component

    Returns
    ----------
        disabled: bool
            Determine if the buttons should be disabled or not
    """

    if func.validate_store_data(data):
        return [False, False]
    return [True, True]
