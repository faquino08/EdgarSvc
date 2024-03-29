from pathlib import Path
from os import environ
import json

POSTGRES_LOCATION = environ['POSTGRES_LOCATION']
POSTGRES_PORT = environ['POSTGRES_PORT']
POSTGRES_DB = environ['POSTGRES_DB']
POSTGRES_USER = environ['POSTGRES_USER']
POSTGRES_PASSWORD = environ['POSTGRES_PASSWORD']
DEBUG = json.loads(environ['DEBUG_BOOL'].lower()) if len(environ['DEBUG_BOOL']) > 0 else False