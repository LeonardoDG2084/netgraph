from flask import Flask

# Location of bluprints (extensions)
from netgraph.ext import site

def create_app():
    app = Flask(__name__)
    site.init_app(app)
    return app