from tkinter import *
from tkinter import messagebox
import random
import pyperclip

import os
os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 29\password-manager-start")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# from day 5 project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # list comprehension
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter+ password_symbol + password_number
    random.shuffle(password_list)
    
    password = "".join(password_list)
    
    # tkmethod inserts
    password_entry.insert(0, password)
    
    pyperclip.copy(password)
    



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_input = website_entry.get()
    email_input= email_entry.get()
    password_input = password_entry.get()
    
    # warning if empty
    if website_input == "" or password_input == "":
        messagebox.showerror(title="Opps", message="Please dont leave the fields emptry")
        
    else:
        # message box
        is_ok = messagebox.askokcancel(title=website_input, message=f"""These are the details entered: 
                            Email: {email_input} \nPassword: {password_input}\n""")
        if is_ok:
            # saves the data
            with open("save_data.csv", mode='a') as data:
                data.write(f"\n{website_input} | {email_input} | {password_input}")   
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1,row=0)

# Label
website = Label(text="Website:")
website.grid(column=0, row=1)
email = Label(text="Email/Username:")
email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dummyemailjosh@gmail.com") #this is from a tkinter documentation
password_entry = Entry()
password_entry.grid(column=1, row=3, columnspan=2)

# Button
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="Add", width=36, command=save_data)
add.grid(column=1, row=4, columnspan=2)







window.mainloop()