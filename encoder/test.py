import tkinter as tk
from tkinter import Tk, Button, Entry, Label, PhotoImage, messagebox, filedialog
import random
from tkinter import PhotoImage, Label
from pathlib import Path  
import numpy as np
###
from PIL import Image

from image_encryption import encrypt_image, decrypt_image
###
root = tk.Tk()

root.geometry("650x386")
root.title("Encode_Decode")

script_dir = Path(__file__).resolve().parent
button_go_img= PhotoImage(file=script_dir / "assets/test.png")
file = filedialog.asksaveasfile(mode='w', defaultextension=".png")
if file:
    tk.save(file) # saves the image to the input file name. 

root.resizable(False, False)
root.mainloop()
