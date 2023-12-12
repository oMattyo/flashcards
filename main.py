import tkinter
from tkinter import ttk
import pandas
import random
import constants as c

lang_list = [c.ARABIC, c.CHINESE, c.FRENCH, c.GERMAN, c.JAPANESE, c.SPANISH]
to_learn = {}
current_card = {}
timer_start = False

def next_card():
    """Pressing thumbs_down.btn or thumbs_up.btn will call this. thumbs_down (directly), thumbs_up through the is_known() fnc"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_lang, text=f"{selected_language.get().title()}")
    canvas.itemconfig(card_word, text=current_card[f"{selected_language.get()}"])
    canvas.itemconfig(fl_card, image=fl_back_img)
    flip_timer = window.after(c.FOUR_SECONDS, func=flip_card)

def flip_card():
    canvas.itemconfig(card_lang, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    canvas.itemconfig(fl_card, image=fl_front_img)

def is_known():
    """Handle removing card from to_learn csv file as thumb_up_btn is clicked for the card"""
    global timer_start
    to_learn.remove(current_card)

    if len(to_learn) > 0:
        # Keep track of remaining words. Remove word as Checkmark btn is clicked
        data = pandas.DataFrame(to_learn)
        data.to_csv(f"data/{selected_language.get().lower()}_words_remaining.csv", index=False) # Do this on_save or on exit
        next_card()
    else:
        window.after_cancel(flip_timer)
        timer_start = False
        canvas.itemconfig(card_lang, text="")
        canvas.itemconfig(card_word, text="List Completed!")
        thumb_up_btn["state"] = tkinter.DISABLED  
        thumb_down_btn["state"] = tkinter.DISABLED

def choose_language(event):
    """Handle the language selection in combobox. Starts flip timer on selection"""
    global to_learn, timer_start, flip_timer
    
    timer_start = True
    lower_language = selected_language.get().lower()

    canvas.itemconfig(card_lang, text=f"{selected_language.get().title()}")
    canvas.itemconfig(top_label, text=f"{selected_language.get().title()} - English")
    lang_cb["state"] = tkinter.DISABLED
    thumb_up_btn["state"] = tkinter.NORMAL
    thumb_down_btn["state"] = tkinter.NORMAL

    try:
        lang_df = pandas.read_csv(filepath_or_buffer=f"./data/{lower_language}_words_remaining.csv")
    except FileNotFoundError:
        lang_df = pandas.read_csv(filepath_or_buffer=f"./data/{lower_language}_nouns.csv")

    to_learn = lang_df.to_dict(orient="records")
    
    flip_timer = window.after(c.FOUR_SECONDS, func=flip_card)

    next_card()
    print(f"Language selected {selected_language.get()}")


# Tkinter App - window
window = tkinter.Tk()
window.title("Flashcards - Language App")
window.config(padx=20, pady=20, bg=c.BG_COLOR)

# Initial flip timer
while timer_start:
    flip_timer = window.after(c.FOUR_SECONDS, func=flip_card)

# Flashcard Back - canvas
canvas = tkinter.Canvas(width=700, height=400, bg=c.BG_COLOR, highlightthickness=0)
fl_back_img = tkinter.PhotoImage(file=c.FLASH_BACK)
fl_front_img = tkinter.PhotoImage(file=c.FLASH_FRONT)
fl_card = canvas.create_image((350, 220), image=fl_back_img)
card_lang = canvas.create_text((188, 110), text="Language", font=c.CARD_LANG_FONT)
card_word = canvas.create_text((350, 226), text="Word", font=c.CARD_WORD_FONT)
canvas.grid(row=1, column=0, columnspan=3)

# Tkinter Language Selection - combobox
selected_language = tkinter.StringVar()
lang_cb = ttk.Combobox(window, textvariable=selected_language)
lang_cb["values"] = [lang.title() for lang in lang_list]
lang_cb["state"] = "readonly"
lang_cb.current(0)
lang_cb.grid(row=2, column=1, pady=(0,20))

lang_cb.bind("<<ComboboxSelected>>", choose_language)

# Tkinter Combobox - label
cb_label = canvas.create_text((350, 388), text="Choose Your Language", font=c.LANGUAGE_CB_FONT)

# Tkinter Top - label
top_label = canvas.create_text((350, 30), text="Language - English", font=c.WINDOW_LANGS_FONT)

# ThumbDown - button
thumb_down_img = tkinter.PhotoImage(file=c.THUMB_DOWN_IMG)
thumb_down_btn = tkinter.Button(image=thumb_down_img, highlightthickness=0, bg=c.BG_COLOR, command=next_card)
thumb_down_btn.grid(row=2, column=0, pady=(0, 20))
thumb_down_btn["state"] = tkinter.DISABLED

# ThumbUp - button
thumb_up_img = tkinter.PhotoImage(file=c.THUMB_UP_IMG)
thumb_up_btn = tkinter.Button(image=thumb_up_img, highlightthickness=0, bg=c.BG_COLOR, command=is_known)
thumb_up_btn.grid(row=2, column=2, pady=(0, 20))
thumb_up_btn["state"] = tkinter.DISABLED

# Main tkinter window loop
window.mainloop()
