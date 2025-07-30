from pathlib import Path
from dotenv import dotenv_values

project_root_path = Path(__file__).parent.parent.parent

config = dotenv_values((project_root_path / ".env").resolve())

if len(config) == 0:
    raise Exception(".env file not found.")

VARIABLES = {
    'PG_HOST': config['PG_HOST'],
    'PG_PORT': int(config['PG_PORT']),
    'PG_NAME': config['PG_NAME'],
    'PG_USER': config['PG_USER'],
    'PG_PASSWORD': config['PG_PASSWORD']
}
