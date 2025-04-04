from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

import os
os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 30\password-manager-start")

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
    new_data = {
        website_input: {
        "email": email_input,
        "password": password_input,
        }
    }    
    
    # warning if empty
    if website_input == "" or password_input == "":
        messagebox.showerror(title="Opps", message="Please dont leave the fields empty")
        
    else:

        try:
            with open("save_data.json", mode='r') as data_file:
                # Read old data
                data = json.load(data_file) # load method
        except FileNotFoundError:
            with open("save_data.json", mode='w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4) #dump method
        except json.JSONDecodeError:
            with open("save_data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data
            data.update(new_data) # update method
            
            with open("save_data.json", mode='w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4) #dump method
                
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website_input = website_entry.get()
    
    ## my attempt
    # try:
    #     with open("save_data.json", "r") as data_file:
    #         print("loading data")
    #         my_data = json.load(data_file)
            
    #         if website_input in my_data:

    #             retrieved_email = my_data[website_input]["email"]
    #             retrieved_password = my_data[website_input]["password"]
    # except KeyError:
    #     messagebox.showwarning(title="Storage Warning", message=(f"there is no website {website_input} in the database"))
        
    # except FileNotFoundError:
    #     messagebox.showwarning(title="File Error", message=(f"there is data file"))
    # else:
    #     messagebox.showinfo(title="Information", message = f"""Email: {retrieved_email} \nPassword: {retrieved_password}\n""")
        
        
    # finally:

    #     website_entry.delete(0, END)
        
        
    # the solution
    try:
        with open("save_data.json", "r") as data_file:
            print("loading data")
            my_data = json.load(data_file)
            
            if website_input in my_data:
                retrieved_email = my_data[website_input]["email"]
                retrieved_password = my_data[website_input]["password"]
                messagebox.showinfo(title="Information", message = f"""Email: {retrieved_email} \nPassword: {retrieved_password}\n""")
                
    except KeyError:
        messagebox.showwarning(title="Storage Warning", message=(f"there is no website {website_input} in the database"))
        
    except FileNotFoundError:
        messagebox.showwarning(title="File Error", message=(f"there is data file"))
        
        
    finally:

        website_entry.delete(0, END)
        
    


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
generate = Button(text="Generate Password", width=15, command=generate_password)
generate.grid(column=2, row=3)
add = Button(text="Add", width=30, command=save_data)
add.grid(column=1, row=4, columnspan=2)
search = Button(text="Search", command=find_password)
search.grid(column=2, row=1)







window.mainloop()