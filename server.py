from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)


@app.route("/")
def hello():
    return "Test flask on github pages"


if __name__ == "__main__":
    freezer.freeze()
    app.run(port=8000)
