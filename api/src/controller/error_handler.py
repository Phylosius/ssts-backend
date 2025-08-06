from flask import make_response

def notfound_error_handler(error):
    return make_response("oups, not found ¯\_(ツ)_/¯", 404)
