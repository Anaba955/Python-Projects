from tkinter import *
import pandas
import random

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_card():
    global card, flip_timer
    window.after_cancel(flip_timer)
    card = random.choice(to_learn)
    rand_word = card["French"]
    canvas.itemconfig(word, text=rand_word, fill="black")
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(background, image=old_photo)
    flip_timer = window.after(3000, reveal)


def reveal():
    global card, flip_timer
    card = random.choice(to_learn)
    rand_word = card["English"]
    canvas.itemconfig(word, text=rand_word, fill="white")
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(background, image=new_photo)


def is_known():
    to_learn.remove(card)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, reveal)

canvas = Canvas(height=526, width=800)
old_photo = PhotoImage(file="images/card_front.png")
new_photo = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=old_photo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=cross_image, highlightthickness=0, command=new_card)
wrong.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
wrong.grid(column=0, row=1)

tick_image = PhotoImage(file="images/right.png")
right = Button(image=tick_image, highlightthickness=0, command=is_known)
wrong.config(padx=10, pady=10, bg=BACKGROUND_COLOR)
right.grid(column=1, row=1)

new_card()

window.mainloop()
