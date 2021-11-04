# package imports
import argparse

import dash
import dash_auth
import pages.graph.graph_callbacks
import pages.table.table_callbacks
import pages.upload.upload_callbacks
import plotly
# initializes all callbacks
import utils.routes
# local imports
from environment.settings import APP_DEBUG, APP_PORT, DEV_TOOLS_PROPS_CHECK

from plotting.app import app

# initialize services
server = app.server


VALID_USERNAME_PASSWORD_PAIRS = {
    "hello": "world",
    "thosaniparth": "pthosan",
    "shahnisarg": "nsshah05",
}
auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSWORD_PAIRS)

# site endpoint
if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description="CmyPlot")
    my_parser.add_argument(
        "--host",
        action="store",
        default="127.0.0.1",
        type=str,
        metavar="host address",
        help="Host address where the website has to be deployed",
    )
    args = my_parser.parse_args()
    app.run_server(
        host=args.host,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK,
    )
