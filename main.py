import logging, os
from flask import Flask
from route.userRoute import blueprint

app = Flask(__name__)

# registering the routes
app.register_blueprint(blueprint)


# index route
@app.route("/")
def index():
    return "Welcome!"


# running server
def runApp():
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


if __name__ == "__main__":
    runApp()
