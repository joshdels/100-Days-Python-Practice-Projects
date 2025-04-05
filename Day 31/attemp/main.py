import os
os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 31\attemp")
from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

#data source
data = pandas.read_csv(r".\data\french_words.csv")
to_learn = data.to_dict(orient="records")
    
current_card = {}
words_to_learn = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)  
    canvas.itemconfig(canvas_image, image=front_picture)
    canvas.itemconfig(top_word, text="french", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(top_word, text="English", fill="white")
    canvas.itemconfig(canvas_image, image =back_picture)
    canvas.itemconfig(top_word, fill="white")
    canvas.itemconfig(card_word, text = current_card["English"], fill="white")
    canvas.itemconfig(card_word, fill="white")

# ganna review this part, dot
def find_save_file():
    #1 find to learn database
    try:
        data = pandas.read_csv(r".\data\words_to_learn.csv")
    except FileNotFoundError:
        print("No database find")
    else:
    #2 if only 3 records remain, back to original
        words_to_learn = data.to_dict(orient="records")
        current_card = random.choice(words_to_learn)
        if len(words_to_learn) == 0:
            print("zero")
        else:
            pass
            
            
    #3 if there is record, show then remove if check button for update
    #4 if words to learn does not exist, use french_words.csv

def draw_cards():
    pass
        
    
def known_card():
    pass
     
def review_card():
    pass
    

window = Tk()
window.title("Flashy cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_picture = PhotoImage(file=".\images\card_front.png")
back_picture = PhotoImage(file=".\images\card_back.png")
canvas_image = canvas.create_image(400,263, image = front_picture)
top_word = canvas.create_text(400,150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0,row=0,columnspan=2)


# buttons
right_image = PhotoImage(file=r".\images\tama.png")
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=0, row=1)
wrong_image = PhotoImage(file=r".\images\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=2, row=1)


next_card()

    
    








window.mainloop()



# notes, time stoping im a bit weak hehehe
# changing itemconfig
# making a placeholder of current data
