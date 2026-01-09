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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    title_text.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        title_text.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        title_text.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        title_text.config(text="Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # minutes = int(count / 60)
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmarks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checkmarks += "✓"
        checkmark_label.config(text=checkmarks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_text.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, bg=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
checkmark_label.grid(column=1, row=3)

window.mainloop()