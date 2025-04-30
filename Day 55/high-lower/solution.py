from flask import Flask
import random

app = Flask(__name__)

num = random.randint(1,9)
print(num)
 

@app.route('/')
def countdown():
    # homepage 
    return '<h1> Guess the number between 1 - 9 </h1>' \
        '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDRsZ3djaG0weWZvMGJ5aWdtYzduZ2dvM3NxZ3Z2MWFxNWpmdTdqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def number(guess):
    # returns the result as gif
    if guess == num:
        return f'<h1 style="color:green">You found me!</>'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    elif guess > num:
        return f'<h1 style="color:violet">Too high, try again!</>'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    elif guess < num:
        return f'<h1 style="color:red">Too low, try again!</>'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'
    

if __name__  == "__main__":
    app.run(debug=True)
    
    
#NOTE
# hmm i got overthink thinking it was the solution to wrap them all hehehe
# nice try dofos