import tkinter

LANG_FONT = ("Arial", 22, "italic")
WORD_FONT = ("Arial", 36, "bold")
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
flash_back = tkinter.PhotoImage(file=FLASH_BACK)
canvas.create_image((350, 220), image=flash_back)
canvas.grid(row=1, column=0, columnspan=3)

# Tkinter Top - label
canvas.create_text((350, 30), text="English - French", font=LANG_FONT)

# top_label = tkinter.Label(text="English - French", font=WORD_FONT, bg=BG_COLOR)
# top_label.grid(row=0, column=1, pady=(0, 10))

# ThumbUp - button
thumb_up_img = tkinter.PhotoImage(file=THUMB_UP_IMG)
thumb_up_btn = tkinter.Button(image=thumb_up_img, highlightthickness=0, bg=BG_COLOR)
thumb_up_btn.grid(row=2, column=0, pady=(0, 20))

# ThumbDown - button
thumb_down_img = tkinter.PhotoImage(file=THUMB_DOWN_IMG)
thumb_down_btn = tkinter.Button(image=thumb_down_img, highlightthickness=0, bg=BG_COLOR)
thumb_down_btn.grid(row=2, column=2, pady=(0, 20))





window.mainloop()
