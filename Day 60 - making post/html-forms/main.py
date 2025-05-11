from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# refer to the docs flask request and post
@app.route("/login", methods=['POST'])
def received_data():
    name = request.form['name']
    password = request.form['password']
    return f"<h1>Name: {name}, Password: {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)