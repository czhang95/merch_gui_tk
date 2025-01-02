from tkinter import *
from PIL import Image, ImageTk

class banner():
    def __init__(self, root, img, padding, screenres, ORI):
        original = Image.open(img)
        if screenres:
            resized = original.resize((1280, 150))
        else:
            resized = original.resize((1050, 150))
        display = ImageTk.PhotoImage(resized)
        banner = Label(root, image = display)
        banner.image = display
        banner.pack(padx = (0, padding), pady = (10, 0), side = ORI)
