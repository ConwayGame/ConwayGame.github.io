from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "Test flask on github pages"


if __name__ == "__main__":
    app.run(port=8000)
