import json
from flask import make_response


def error(message):
    """Create an error response."""
    return make_response(json.dumps({'error': message}))
