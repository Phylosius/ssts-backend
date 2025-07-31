from psycopg2 import connect
from ..config import VARIABLES

connection = connect(
    host=VARIABLES.DB_HOST,
    port=VARIABLES.DB_PORT,
    database=VARIABLES.DB_NAME,
    user=VARIABLES.DB_USER,
    password=VARIABLES.DB_PASSWORD
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

