from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f'<em>{function}</em>'
    return wrapper

def make_underline(function):
    def wrapper():
        return f'<u>{function}</u>'
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>'\
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWw2MmhnOWNnZWo0Y3E0OHliMmdxam1oeHc4M3YyaTM0aWw1NGllcSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12ELmx0C4EFKcE/giphy.gif" width="500px">'

@app.route("/bye")

@make_bold
# @make_emphasis
# @make_underline
def bye():
    return "Bye!"

# variable paths practice
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! you are {number} yeears old"

if __name__ == "__main__":
    # runs debug mode
    app.run(debug=True)