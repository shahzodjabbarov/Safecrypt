import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import cv2
import numpy as np

# --- functions ---

def savefile():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    edge.save(filename)

# --- main ---

root = tk.Tk()

img = cv2.imread('face_person1.jpg')
edge = Image.fromarray(img)

tk_edge = ImageTk.PhotoImage(edge)
label = tk.Label(root, image=tk_edge)
label.pack()

button = tk.Button(root, text="save as", command=savefile)
button.pack()

root.mainloop()