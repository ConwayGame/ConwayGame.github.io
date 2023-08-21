from flask import Flask
from flask_frozen import Freezer
from os import getcwd


app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DESTINATION'] = getcwd()
app.config['FREEZER_DESTINATION_IGNORE'] = '*'


@app.route("/")
def hello():
    return "Re:Test flask on github pages"


if __name__ == "__main__":
    freezer.freeze()
    # app.run(port=8000)
