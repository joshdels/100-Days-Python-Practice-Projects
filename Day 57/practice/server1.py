from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, current_year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io/?name={name}") 
    data = gender_response.json()
    gender = data['gender']
    
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    data = age_response.json()
    age = data['age']
    
    return render_template("index1.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
        
if __name__ == "__main__":
    # runs debug mode
    app.run(debug=True)