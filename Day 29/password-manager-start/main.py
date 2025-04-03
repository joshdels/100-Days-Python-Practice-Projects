from tkinter import *
import os
os.chdir(r"C:\Users\TUF\Documents\GitHub\100-Days-Python-Practice-Projects\Day 29\password-manager-start")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")

# Image
canvas = Canvas(width=400, height=400)
password_image = PhotoImage(file="logo.png")
canvas.create_image(200,200, image=password_image)
canvas.grid(column=0,row=0)





window.mainloop()