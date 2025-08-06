from flask import Flask

from api.src.config.variables import VARIABLES
from api.src.controller.index_controller import index_bp

app = Flask(__name__)
app.register_blueprint(index_bp)

app_host = '0.0.0.0' if VARIABLES.WSGI_IS_EXPOSED else '127.0.0.1'
app_port = VARIABLES.WSGI_PORT if VARIABLES.WSGI_PORT else 5721

app.run(host=app_host, port=app_port)