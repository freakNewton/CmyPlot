# package imports
from src.plotting.app import app
import argparse

# local imports
from src.plotting.environment.settings import APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK

# initializes all callbacks
import src.plotting.utils.routes
import src.plotting.pages.upload.upload_callbacks
import src.plotting.pages.table.table_callbacks
import src.plotting.pages.graph.graph_callbacks

# initialize services
server = app.server

# site endpoint
if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='CmyPlot')
    my_parser.add_argument(
        '--host',
        action='store',
        default='127.0.0.1',
        type=str,
        metavar='host address',
        help='Host address where the website has to be deployed'
    )
    args = my_parser.parse_args()
    app.run_server(
        host=args.host,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
    )
