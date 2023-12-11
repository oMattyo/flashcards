import tkinter
import constants as c

# TODO - Add functions to handle click events on buttons
# TODO - Add function to handle card flipping
# TODO - Add reading from and writing to csv files for words
# TODO - Allow for text to dynamically change depending on language selected

# Tkinter App - window
window = tkinter.Tk()
window.title("Flashcards - Language App")
window.config(padx=20, pady=20, bg=c.BG_COLOR)

# Flashcard Back - canvas
canvas = tkinter.Canvas(width=700, height=400, bg=c.BG_COLOR, highlightthickness=0)
fl_back_img = tkinter.PhotoImage(file=c.FLASH_BACK)
flash_back = canvas.create_image((350, 220), image=fl_back_img)
card_lang = canvas.create_text((180, 110), text="French", font=c.CARD_LANG_FONT)
card_word = canvas.create_text((350, 226), text="Word", font=c.CARD_WORD_FONT)
card_cos = canvas.create_text((350, 326), text="NOUN", font=c.CARD_COS_FONT)
# TODO - Add combobox dropdown to select languages
canvas.grid(row=1, column=0, columnspan=3)

# Tkinter Top - label
top_label = canvas.create_text((350, 30), text="French - English", font=c.WINDOW_LANGS_FONT)

# ThumbDown - button
thumb_down_img = tkinter.PhotoImage(file=c.THUMB_DOWN_IMG)
thumb_down_btn = tkinter.Button(image=thumb_down_img, highlightthickness=0, bg=c.BG_COLOR)
thumb_down_btn.grid(row=2, column=0, pady=(0, 20))

# ThumbUp - button
thumb_up_img = tkinter.PhotoImage(file=c.THUMB_UP_IMG)
thumb_up_btn = tkinter.Button(image=thumb_up_img, highlightthickness=0, bg=c.BG_COLOR)
thumb_up_btn.grid(row=2, column=2, pady=(0, 20))




window.mainloop()
