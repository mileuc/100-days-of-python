from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

all_posts = []
response = requests.get("https://api.npoint.io/ed99320662742443cc5b")
all_post_objects = response.json()
for post_object in all_post_objects:
    post = Post(post_object["id"], post_object["title"], post_object["subtitle"], post_object["body"])
    all_posts.append(post)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    desired_post = None
    for post in all_posts:
        if post.id == blog_id:
            desired_post = post

    return render_template("post.html", post=desired_post)


if __name__ == "__main__":
    app.run(debug=True)
