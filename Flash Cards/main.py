from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    data_records = data.to_dict(orient="records")



def delete_entry():
    data_records.remove(new_word)
    new_card()

def new_card():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(data_records)
    french_word = new_word["French"]
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(lang_name, text="French", fill="black")
    canvas.itemconfig(3, text=french_word, fill="black")
    flip_timer = window.after(3000, card_flip)


def card_flip():
    # window.after_cancel(after_id)
    english_word = new_word["English"]
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(lang_name, text="English", fill="white")
    canvas.itemconfig(3, text=english_word, fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, card_flip)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
lang_name = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
lang_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


card_back_img = PhotoImage(
    file="images/card_back.png")
# back_image = canvas.create_image(400, 263, image=card_back_img)
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(
    file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=delete_entry)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(
    file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)


new_card()

window.mainloop()

df = pandas.DataFrame(data_records)
df.to_csv('data/words_to_learn.csv', index=False)
