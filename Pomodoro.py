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
resp = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global resp
    window.after_cancel(timer)
    label.config(text="Timer")
    resp = 0
    canvas.itemconfig(timer_text, text="00:00")
    tick_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global resp, label
    resp += 1

    if resp > 8:
        resp = 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if resp % 2 != 0:
        label.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN)
        count_down(work_sec)
    elif resp % 2 == 0:
        label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(resp / 2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 50, "bold"))
label.config(fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # widget
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

tick_mark = Label(font=(FONT_NAME, 10, "normal"))
tick_mark.config(fg=GREEN, bg=YELLOW)
tick_mark.grid(column=1, row=3)

start_button = Button(text="Start", bd=0, padx=5, pady=5, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                      command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", bd=0, padx=5, pady=5, font=(FONT_NAME, 10, "bold"), highlightthickness=0,
                      command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()
