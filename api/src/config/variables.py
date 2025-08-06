from pathlib import Path
from dotenv import dotenv_values

project_root_path = Path(__file__).parent.parent.parent.parent

config = dotenv_values((project_root_path / ".env").resolve())

if len(config) == 0:
    raise Exception(".env file not found.")

class Variables:
    WSGI_PORT = int(config['WSGI__PORT'])
    WSGI_IS_EXPOSED = bool(config['WSGI__IS_EXPOSED'])

    DB_HOST = config['DB_HOST']
    DB_PORT = int(config['DB_PORT'])
    DB_NAME = config['DB_NAME']
    DB_USER = config['DB_USER']
    DB_PASSWORD = config['DB_PASSWORD']

VARIABLES = Variables()
