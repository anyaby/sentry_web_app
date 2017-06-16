from flask import Flask
from raven import Client
from creds import SENTRY_URL

client = Client(SENTRY_URL)
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/anya")
def hello_sentry():
    try:
        1 / 0
    except ZeroDivisionError:
        client.captureException()
        return "exception sent"
