from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


'''
On Windows type:
python -m pip install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField("Log In")
    
app = Flask(__name__)
app.secret_key = "josh"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    login_form = MyForm()
    return render_template('login.html', form=login_form)
 

if __name__ == '__main__':
    app.run(debug=True)
