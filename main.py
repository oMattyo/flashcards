import tkinter
from tkinter import ttk
import constants as c

# TODO - Add functions to handle click events on buttons
# TODO - Add function to handle card flipping
# TODO - Add reading from and writing to csv files for words
# TODO - Allow for text to dynamically change depending on language selected

def language_selected(event):
    """Handle the language selection in combobox"""
    canvas.itemconfig(card_lang, text=f"{selected_language.get().title()}")
    canvas.itemconfig(top_label, text=f"{selected_language.get().title()} - English")
    lang_cb["state"] = "disabled"
    # print(f"Language selected {selected_language.get()}")


# Tkinter App - window
window = tkinter.Tk()
window.title("Flashcards - Language App")
window.config(padx=20, pady=20, bg=c.BG_COLOR)

# Flashcard Back - canvas
canvas = tkinter.Canvas(width=700, height=400, bg=c.BG_COLOR, highlightthickness=0)
fl_back_img = tkinter.PhotoImage(file=c.FLASH_BACK)
fl_front_img = tkinter.PhotoImage(file=c.FLASH_FRONT)
fl_card = canvas.create_image((350, 220), image=fl_back_img)
card_lang = canvas.create_text((188, 110), text="Language", font=c.CARD_LANG_FONT)
card_word = canvas.create_text((350, 226), text="Word", font=c.CARD_WORD_FONT)
# TODO - Add combobox dropdown to select languages
canvas.grid(row=1, column=0, columnspan=3)

# Tkinter Language Selection - combobox
dummy_lang_list = ["arabic", "chinese", "french", "german", "japanese", "spanish"]
selected_language = tkinter.StringVar()
lang_cb = ttk.Combobox(window, textvariable=selected_language)
lang_cb["values"] = [lang for lang in dummy_lang_list]
lang_cb["state"] = "readonly"
lang_cb.current(0)
lang_cb.grid(row=2, column=1, pady=(0,20))

lang_cb.bind("<<ComboboxSelected>>", language_selected)

# Tkinter Combobox - label
cb_label = canvas.create_text((350, 388), text="Choose Your Language", font=c.LANGUAGE_CB_FONT)

# Tkinter Top - label
top_label = canvas.create_text((350, 30), text="Language - English", font=c.WINDOW_LANGS_FONT)

# ThumbDown - button
thumb_down_img = tkinter.PhotoImage(file=c.THUMB_DOWN_IMG)
thumb_down_btn = tkinter.Button(image=thumb_down_img, highlightthickness=0, bg=c.BG_COLOR)
thumb_down_btn.grid(row=2, column=0, pady=(0, 20))

# ThumbUp - button
thumb_up_img = tkinter.PhotoImage(file=c.THUMB_UP_IMG)
thumb_up_btn = tkinter.Button(image=thumb_up_img, highlightthickness=0, bg=c.BG_COLOR)
thumb_up_btn.grid(row=2, column=2, pady=(0, 20))




window.mainloop()
