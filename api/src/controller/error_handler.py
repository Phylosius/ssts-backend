from flask import request

def notfound_error_handler(error):
    return {"error": f"no handler for {request.method} {request.path}"}, 404
