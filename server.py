import datetime as dt

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    copyright_year = dt.datetime.now().strftime("%Y")
    return render_template("index.html", copyright_year=copyright_year)


if __name__ == "__main__":
    app.run(debug=True)
