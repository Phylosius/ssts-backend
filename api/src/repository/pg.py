from psycopg2 import connect
from ..config import VARIABLES

connection = connect(
    host=VARIABLES['PG_HOST'],
    port=VARIABLES['PG_PORT'],
    database=VARIABLES['PG_NAME'],
    user=VARIABLES['PG_USER'],
    password=VARIABLES['PG_PASSWORD']
)

def transactional(fn):
    def wrapper(*args, **kwargs):
        with connection.cursor() as cur:
            try:
                result = fn(cur, *args, **kwargs)
                connection.commit()
                return result
            except Exception as e:
                connection.rollback()
                raise e
    return wrapper

