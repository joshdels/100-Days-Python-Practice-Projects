from flask import Flask, render_template, url_for, request
import requests
import smtplib
import os

app = Flask(__name__)

url = "https://api.npoint.io/674f5423f73deab1e9a7"
response = requests.get(url=url)
all_post = response.json()
name = "Joshua De Leon"

# Email and password
my_email = os.environ.get('MY_TEST_EMAIL')
my_pass = os.environ.get('TEST_PASSWORD')

@app.route("/")
def home():
    return render_template('index.html', data=all_post, name=name)

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == "POST":
        # Getting the Post Section
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        
        #Sending an Email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(
                user=my_email, 
                password=my_pass
            )
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:New Message\n\n Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )
        return render_template("contact.html", msg_sent=True)
    return render_template('contact.html', msg_sent=False)



@app.route("/post.html/<int:post_id>")
def get_post(post_id):
    requested_post = None
    for post in all_post:
        if post['id'] == post_id:
             requested_post = post
    return render_template('post.html', data=requested_post)

if __name__ == "__main__":
    app.run(debug=True)