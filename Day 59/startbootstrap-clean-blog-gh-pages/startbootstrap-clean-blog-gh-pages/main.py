from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

url = "https://api.npoint.io/674f5423f73deab1e9a7"
response = requests.get(url=url)
all_post = response.json()

name = "Joshua De Leon"

@app.route("/index.html")
def home():
    return render_template('index.html', data=all_post, name=name)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post.html/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post in all_post:
        if post['id'] == post_id:
             requested_post = post
    return render_template('post.html', data=requested_post)

if __name__ == "__main__":
    app.run(debug=True)