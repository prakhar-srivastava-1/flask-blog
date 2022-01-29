import datetime as dt

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    # get dummy blogs from npoint
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.request(url=url, method='GET')
    posts = response.json()
    copyright_year = dt.datetime.now().strftime("%Y")
    return render_template("index.html",
                           copyright_year=copyright_year,
                           posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
