# package imports
import os
from os.path import join

from dotenv import load_dotenv

# load in dotenv file
dotenv_path = join(os.getcwd(), "src", "plotting", "environment", ".env.development")
load_dotenv(dotenv_path=dotenv_path, override=True)

# set variables
APP_HOST = os.environ.get("HOST")
APP_PORT = int(os.environ.get("PORT"))
APP_DEBUG = bool(os.environ.get("DEBUG"))
DEV_TOOLS_PROPS_CHECK = bool(os.environ.get("DEV_TOOLS_PROPS_CHECK"))
