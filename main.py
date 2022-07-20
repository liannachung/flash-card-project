from tkinter import *
from pandas import *
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("./data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}

def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_word = current_card["French"]
    card.itemconfig(card_title, text="French", fill="black")
    card.itemconfig(card_word, text=current_word, fill="black")
    card.itemconfig(card_image, image=card_front)

    flip_timer = window.after(ms=3000, func=flip_card)


def flip_card():
    card.itemconfig(card_image, image=card_back)
    card.itemconfig(card_title, text="English", fill="white")
    card.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    global data
    to_learn.remove(current_card)

    words_to_learn = DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", infex=False)
    new_card()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(ms=3000, func=flip_card)

card = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = card.create_image(400, 263, image=card_front)
card_title = card.create_text(400, 150, text="title", font=("Arial", "40", "italic"))
card_word = card.create_text(400, 263, text="word", font = ("Arial", "60", "bold"))
card.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="./images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)

window.mainloop()