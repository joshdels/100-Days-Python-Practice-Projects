from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    all_post = response.json()
    return render_template("index.html", posts = all_post)

@app.route("/post/<int:post_id>")
def get_post(post_id):
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=url)
    all_post = response.json()
    return render_template("post.html", posts = all_post, id=post_id)

if __name__ == "__main__":
    app.run(debug=True)
    
#NOTE 
# im still confuse of the logic order
