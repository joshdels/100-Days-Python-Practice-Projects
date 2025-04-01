from tkinter import *

def converter():
    n = input.get()
    converted = int(n) * 1.60934
    solved.config(text = converted)

result = 0

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=50, pady=50)

#Label
label1 = Label(text="is equal to", font=("Arial", 10))
label1.grid(column=0, row=1)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

# Result
solved = Label(text=0, font=("Arial", 10))
solved.grid(column=1, row=1)

# Button
button = Button(text="Calculate", font=("Arial", 10), command=converter)
button.grid(column=1, row=2)

# Miles
miles = Label(text="Miles", font=("Arial", 10))
miles.grid(column=2, row=0)

# Kilometer
kilometer = Label(text="km", font=("Arial", 10))
kilometer.grid(column=2, row=1)




window.mainloop()