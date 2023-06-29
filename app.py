import logging
from flask import Flask
from route.userRoute import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)


@app.route("/")
def index():
    return "Welcome!"
