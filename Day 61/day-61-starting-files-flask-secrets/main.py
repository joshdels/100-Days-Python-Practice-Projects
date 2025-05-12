from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4
from flask import Flask


'''
On Windows type:
python -m pip install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

class MyForm(FlaskForm):
    email = StringField('email', validators=[Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Log In")
    
app = Flask(__name__)
app.secret_key = "josh"
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    # this will trigger the confirmation of credentials, once matched it will run
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "123123123":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)
 
if __name__ == '__main__':
    app.run(debug=True)
