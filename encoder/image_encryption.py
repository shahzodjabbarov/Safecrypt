import numpy as np
from PIL import Image
import tkinter as tk
from tkinter import Tk, Button, Entry, Label, PhotoImage, messagebox, filedialog
import random


def generate_key(shape, seed=0):
    np.random.seed(seed)
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)

def encrypt_image(image_path, key_seed=42):
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Generate a key for each channel
    keys = [generate_key(img_array[:, :, i].shape, seed=key_seed + i) for i in range(3)]

    # Encrypt each channel
    encrypted_array = np.zeros_like(img_array)
    for i in range(3):
        encrypted_array[:, :, i] = np.bitwise_xor(img_array[:, :, i], keys[i])

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_array)
    file = filedialog.asksaveasfile(mode='wb', defaultextension=".png")
    
    encrypted_img.save(file)
    return file

def decrypt_image(encrypted_path, key_seed=42):
    # Open the encrypted image
    img = Image.open(encrypted_path)
    img_array = np.array(img)

    # Generate a key for each channel
    keys = [generate_key(img_array[:, :, i].shape, seed=key_seed + i) for i in range(3)]

    # Decrypt each channel
    decrypted_array = np.zeros_like(img_array)
    for i in range(3):
        decrypted_array[:, :, i] = np.bitwise_xor(img_array[:, :, i], keys[i])

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_array)
    return decrypted_img

# Usage example in python
# encrypt_image('back.png', 'encrypted_image.png')  # The key will be generated within the function
# decrypt_image('encrypted_image.png', 'decrypted_image.png')  # The same key will be regenerated
