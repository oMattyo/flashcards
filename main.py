import tkinter

WINDOW_LANGS_FONT = ("Courier", 34, "bold")
CARD_LANG_FONT = ("Arial", 22, "italic")
CARD_WORD_FONT = ("Arial", 32, "bold")
SPEECH_COMPONENT_FONT = ("Arial", 18, "normal")
BG_COLOR = "#cccccc"

THUMB_UP_IMG = "./img/thumbup.png"
THUMB_DOWN_IMG = "./img/thumbdown.png"
FLASH_FRONT = "./img/flashcard_front.png"
FLASH_BACK = "./img/flashcard_back.png"

# Tkinter App - window
window = tkinter.Tk()
window.title("Flashcards - Language App")
window.config(padx=20, pady=20, bg=BG_COLOR)

# Flashcard Back - canvas
canvas = tkinter.Canvas(width=700, height=400, bg=BG_COLOR, highlightthickness=0)
fl_back_img = tkinter.PhotoImage(file=FLASH_BACK)
flash_back = canvas.create_image((350, 220), image=fl_back_img)
card_lang = canvas.create_text((180, 110), text="French", font=CARD_LANG_FONT)
card_word = canvas.create_text((350, 226), text="Word", font=CARD_WORD_FONT)
card_speech_component = canvas.create_text((350, 326), 
                                           text="NOUN", font=SPEECH_COMPONENT_FONT)
canvas.grid(row=1, column=0, columnspan=3)

# Tkinter Top - label
top_label = canvas.create_text((350, 30), text="French - English", font=WINDOW_LANGS_FONT)

# ThumbDown - button
thumb_down_img = tkinter.PhotoImage(file=THUMB_DOWN_IMG)
thumb_down_btn = tkinter.Button(image=thumb_down_img, highlightthickness=0, bg=BG_COLOR)
thumb_down_btn.grid(row=2, column=0, pady=(0, 20))

# ThumbUp - button
thumb_up_img = tkinter.PhotoImage(file=THUMB_UP_IMG)
thumb_up_btn = tkinter.Button(image=thumb_up_img, highlightthickness=0, bg=BG_COLOR)
thumb_up_btn.grid(row=2, column=2, pady=(0, 20))




window.mainloop()
