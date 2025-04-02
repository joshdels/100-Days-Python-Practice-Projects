import os
os.chdir(r"C:\Users\deleo\OneDrive\Documents\GitHub\100-Days-Python-Practice-Projects\Day 28\pomodoro-start")


from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check= ""
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    text_heading.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global check
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    
    if reps % 8 == 0:
        # if its 8th rep
        count_down(long_break_sec)
        text_heading.config(text="Break", fg=PINK)
        check_mark.config(text=check)
    elif reps % 2 == 0 :
        # 1st/3rd/5th/7th rep
        count_down(short_break_sec)
        text_heading.config(text="Break", fg=PINK)
        check_mark.config(text=check)
    else:
        count_down(work_sec)
        text_heading.config(text="Work", fg=GREEN)
        check += "✔"
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1, count_down, count-1)
    else:
        start_timer()
       
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



# Timer Heading
text_heading = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
text_heading.grid(column=1, row=0)

# start_button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# reset_button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Mark
check_mark = Label(text=check, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
