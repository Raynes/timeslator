"""Start the server and whatnot."""
from os import environ
from flask import Flask
from timeslator.views import timeslate


app = Flask(__name__)

app.register_blueprint(timeslate.bp)

if __name__ == '__main__':
    app.run(debug=not environ.get("PROD", False))
