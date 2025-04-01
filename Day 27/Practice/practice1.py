from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print("I got clicked")

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button1
button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=1,row=1)

# Button2
button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2,row=0)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=3)













window.mainloop()