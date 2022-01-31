import datetime as dt
import smtplib
import requests
from flask import Flask, render_template, request
from hidden_secrets import EMAIL, PASSWORD

COPYRIGHT_YEAR = dt.datetime.now().strftime("%Y")

app = Flask(__name__)


@app.route("/")
def index():
    # get dummy blogs from npoint
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.request(url=url, method='GET')
    posts = response.json()

    return render_template("index.html",
                           copyright_year=COPYRIGHT_YEAR,
                           posts=posts)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return_message = None
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['message']
            email_message = f"Subject: Contact Form Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            # create smtp connection
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=EMAIL,
                                    msg=email_message)
            return_message = ["success",
                              "Thanks for your message! I will be in touch as soon as possible."]
        except:
            return_message = ["danger",
                              "Something went wrong! Your message could not be sent."]
        return render_template("contact.html",
                               copyright_year=COPYRIGHT_YEAR,
                               return_message=return_message)
    # for GET request
    return render_template("contact.html",
                           copyright_year=COPYRIGHT_YEAR,
                           return_message=return_message)


@app.route("/about")
def about():
    return render_template("about.html",
                           copyright_year=COPYRIGHT_YEAR)


@app.route("/blog/<int:post_id>")
def get_blog(post_id):
    # get dummy blogs from npoint
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.request(url=url, method='GET')
    posts = response.json()
    select_post = dict()

    for post in posts:
        if post["id"] == post_id:
            select_post = post
            break

    return render_template("post.html",
                           copyright_year=COPYRIGHT_YEAR,
                           post=select_post)


if __name__ == "__main__":
    app.run(debug=True)
