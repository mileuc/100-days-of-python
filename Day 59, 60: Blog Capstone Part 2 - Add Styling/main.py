from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv("./.env")
MY_EMAIL = os.getenv("MY_GMAIL")
PASSWORD = os.getenv("MY_PASSWORD")
POSTS_URL = "https://api.npoint.io/e42b353ee387383898c7"
response = requests.get(POSTS_URL)
response.raise_for_status()
post_objects = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(name, email, phone, message)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # specify location of the email providers smtp
            connection.starttls()  # a way to secure connection to our email server by encrypting message
            connection.login(user=MY_EMAIL, password=PASSWORD)  # log in by providing a username and password
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:A blog reader is trying to get in touch! \n\nHey,\n{name} with the email {email} is"
                                    f" trying to get in touch with the following message: \n{message}")
        return render_template("contact.html", message_sent=True)
    else:
        return render_template("contact.html", message_sent=False)


@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for post_object in post_objects:
        if post_id == post_object["id"]:
            requested_post = post_object

    if requested_post is not None:
        return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)