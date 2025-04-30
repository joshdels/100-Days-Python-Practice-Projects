from flask import Flask
import random

app = Flask(__name__)

def result(func):
    def wrapper(*args):
        num = random.randint(1,9)
        if args[0] == num:
            func
            return f'<h1 style="color:green">You found me!</>'\
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
        elif args[0] > num:
            func 
            return f'<h1 style="color:violet">Too high, try again!</>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        elif args[0] < num:
            return f'<h1 style="color:red">Too low, try again!</>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    return wrapper

@app.route('/')
def countdown():
    return '<h1> Guess the number between 1 - 9 </h1>' \
        '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDRsZ3djaG0weWZvMGJ5aWdtYzduZ2dvM3NxZ3Z2MWFxNWpmdTdqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:number>")
@result()
def number(number):
    return f'this is the number {number}'
    

if __name__  == "__main__":
    app.run(debug=True)