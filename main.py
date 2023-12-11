import tkinter

LANG_FONT = ("Arial", 22, "italic")
WORD_FONT = ("Arial", 36, "bold")
SPEECH_COMPONENT_FONT = ("Arial", 18, "normal")
BG_COLOR = "#d9d9d9"

THUMB_UP_IMG = "./img/thumbup.png"
THUMB_DOWN_IMG = "./img/thumbdown.png"
FLASH_FRONT = "./img/flashcard_front.png"
FLASH_BACK = "./img/flashcard_back.png"

window = tkinter.Tk()
window.title("Flashcards - Language App")
window.config(padx=50, pady=50, bg=BG_COLOR)

# Flashcard Back Canvas
canvas = tkinter.Canvas(width=800, height=600)
flash_back = tkinter.PhotoImage(file=FLASH_BACK)
canvas.create_image((400, 310), image=flash_back)
canvas.grid(row=1, column=0, columnspan=3)








window.mainloop()
