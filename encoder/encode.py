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

char_to_num = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18,
    't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,
    'A': 26, 'B': 27, 'C': 28, 'D': 29, 'E': 30, 'F': 31, 'G': 32, 'H': 33, 'I': 34,
    'J': 35, 'K': 36, 'L': 37, 'M': 38, 'N': 39, 'O': 40, 'P': 41, 'Q': 42, 'R': 43,
    'S': 44, 'T': 45, 'U': 46, 'V': 47, 'W': 48, 'X': 49, 'Y': 50, 'Z': 51,
    '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60,
    '9': 61,
    ' ': 62, '!': 63, '"': 64, '#': 65, '$': 66, '%': 67, '&': 68, "'": 69, '(': 70,
    ')': 71, '*': 72, '+': 73, ',': 74, '-': 75, '.': 76, '/': 77, ':': 78, ';': 79,
    '<': 80, '=': 81, '>': 82, '?': 83, '@': 84, '[': 85, '\\': 86, ']': 87, '^': 88,
    '_': 89, '`': 90, '{': 91, '|': 92, '}': 93, '~': 94
}


root = tk.Tk()

root.geometry("650x386")
root.title("Encode_Decode")


script_dir = Path(__file__).resolve().parent
image_path1 = script_dir / "back.png"
filename = PhotoImage(file=image_path1)

image_path2 = script_dir / "back2.png"
filename2 = PhotoImage(file=image_path2)
background_label = Label(root, image=filename)
background_label.place(x=0,    y=0,     relwidth=1,     relheight=1)

image_path3 = script_dir / "back3.png"
filename3 = PhotoImage(file=image_path3)

entry_n = Entry()
entry_e = Entry()
entry_path = Entry()
button_text = Button()
button_picture = Button()
button_encode = Button()
button_back = Button()
button_back2 = Button()
button_choose = Button()
button_clear = Button()
button_clear2 = Button()
button_go = Button()
button_norm = Button()
normal  = ''
encoded = ''
image_path = ''

def home():
    global button_encode
    global button_back
    global button_back2
    global button_clear
    global button_go
    global button_norm
    global entry_e
    global entry_n
    global button_choose

    global filename
    global entry_path
    global script_dir
    global button_text
    global button_picture
    global background_label
    global filename

    entry_path.place(x=900.0, y=197.0, width=250.0, height=21.0)
    button_go.place(x=900,   y=287.0,   width=86.0,     height=38)
    button_norm.place(x=900.0,   y=287.0,    width=86.0,     height=38)
    button_encode.place(x=900.0,    y=287.0,    width=86.0,     height=38)
    button_clear.place(x=900,    y=287.0,    width=86.0,     height=38)
    button_clear2.place(x=900,    y=287.0,    width=86.0,     height=38)
    button_back.place(x=900,    y=340.0,    width=59.0,     height=25)
    button_back2.place(x=900,    y=340.0,    width=59.0,     height=25)
    button_choose.place(x=900,    y=340.0,    width=59.0,     height=25)
    entry_n.place(x=900, y=197.0, width=250.0, height=21.0)
    entry_e.place(x=900, y=235.0, width=245.0, height=21.0) 

    background_label.configure(image=filename)

    
    button_text.place(x=47.0,   y=238.0,   width=112.0,     height=43)
    button_picture.place(x=227.0,   y=238.0,    width=112.0,     height=43.0)
    
    # Hide encryption and decryption buttons initially
    button_encrypt.place_forget()
    button_decrypt.place_forget()

def text():
    global button_text
    global button_picture


    global button_encode
    global button_back
    global button_clear
    global button_go
    global button_norm

    global background_label
    global filename2

    global entry_n
    global entry_e

    button_text.place(x=900.0,   y=238.0,   width=112.0,     height=43)
    button_picture.place(x=900.0,   y=238.0,    width=112.0,     height=43.0)

    background_label.configure(image=filename2)
    button_go.place(x=16.0,   y=287.0,   width=86.0,     height=38)
    button_norm.place(x=126.0,   y=287.0,    width=86.0,     height=38)
    button_encode.place(x=232.0,    y=287.0,    width=86.0,     height=38)
    button_clear.place(x=339.0,    y=287.0,    width=86.0,     height=38)
    button_back.place(x=565.0,    y=340.0,    width=59.0,     height=25)
    entry_n.place(x=118.0, y=197.0, width=250.0, height=21.0)
    entry_e.place(x=118.0, y=235.0, width=245.0, height=21.0) 

def start():
    global entry_n
    global entry_e
    global normal
    global encoded
    global char_to_num

    normal = entry_n.get()
    encoded = entry_e.get()
    
    if normal == "" and encoded  == '':
        return 0

    if normal == '' and encoded != '':
        def string_to_matrices(input_string):
            # Split the input string into a list of integers
            numbers = list(map(int, input_string.split()))

            # Extract the elements for the first 2x2 matrix
            matrix1 = np.array([[numbers[0], numbers[-2]], [numbers[1], numbers[-1]]])

            # Extract the remaining elements for the second 2xN matrix
            remaining_numbers = numbers[2:-2]
            # Determine the number of columns in the second matrix
            num_columns = len(remaining_numbers) // 2
            # Reshape the remaining numbers into a 2xN matrix
            matrix2 = np.array(remaining_numbers).reshape(2, num_columns, order='F')

            return matrix1, matrix2

        # Test the function
        
        matrix1, matrix2 = string_to_matrices(encoded)

        inv_matrix1 = np.linalg.inv(matrix1) 

        final = np.dot(inv_matrix1, matrix2)

        rounded_matrix = np.round(final).astype(int)


        num_to_char = {v: k for k, v in char_to_num.items()}


        # Translating the numbers in the matrix to characters
        result = ''
        for column in range(len(rounded_matrix[0])):
            for row in range(len(rounded_matrix)):
                result += num_to_char[rounded_matrix[row][column]]



        print("Matrix 1:")
        print(matrix1)
        print("Matrix 2:")
        print(matrix2)
        print("Final string:")
        print(rounded_matrix)
        print(result)
        entry_n.delete(0, tk.END)
        entry_n.insert(tk.END, result)

    else:
        def message_to_matrix(message):
            global num_to_char
            # Convert message characters to their assigned numbers
            numbers = [char_to_num.get(char, 95) for char in message]  # Return 95 for unknown characters
            
            # Pad the message with space if necessary to make its length even
            if len(numbers) % 2 != 0:
                numbers.append(char_to_num[' '])
            
            # Reshape the numbers into a 2xN matrix
            matrix = np.array(numbers).reshape(-1, 2).T
            return matrix


    def multiply(matrix, key):
        result = np.dot(matrix,key)
        
        return result

    def generate_invertible_key_matrix():
        n = 2  # Size of invertible matrix
        while True:
            # Generate a random integer matrix with positive values between 1 and 10
            matrix = np.random.randint(1, 11, size=(n, n))
            # Ensure the determinant is non-zero (invertibility condition for 2x2 matrices)
            det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
            if det != 0:
                return matrix

    def insert_columns(product, key):
        # Get the first and second columns of the 2x2 matrix
        col1 = key[:, 0]
        col2 = key[:, 1]
        
        # Insert the first column of the 2x2 matrix at the beginning of each row
        result_matrix = np.insert(product, 0, col1, axis=1)
        
        # Calculate the index to insert the second column based on the new shape
        insert_idx = product.shape[1] + 1
        
        # Insert the second column of the 2x2 matrix at the end of each row
        result_matrix = np.insert(result_matrix, insert_idx, col2, axis=1)
        
        return result_matrix




    def matrix_to_string(matrix):
        flattened = []
        for col in range(len(matrix[0])):
            for row in range(len(matrix)):
                flattened.append(matrix[row][col])
        flattened_str = "".join(map(lambda x: str(x) + " ", flattened))
        return flattened_str




    message = normal
    if len(message) % 2 != 0:
        message += ' '

    key = generate_invertible_key_matrix()
    matrix = message_to_matrix(message)
    product = multiply(key, matrix)
    result = insert_columns(product, key)
    encoded = matrix_to_string(result)
    print(key)
    print(matrix)
    print(product)
    print(result)
    print(encoded)


    entry_e.delete(0, tk.END)
    entry_e.insert(tk.END, encoded)
    
def clear():
    global entry_e
    global entry_n
    global normal
    global encoded
    entry_n.delete(0, tk.END)
    entry_e.delete(0, tk.END)
    normal = ''
    encoded = ''

def clear2():
    global entry_path
    global image_path
    entry_path.delete(0, tk.END)
    image_path = ''
    
def copy_n():
    global normal
    root.clipboard_clear()
    root.clipboard_append(normal)

def copy_e():
    global encoded
    root.clipboard_clear()
    root.clipboard_append(encoded)

###
def image():
    global button_text
    global button_picture
    global button_encrypt
    global button_decrypt
    global button_choose
    global button_encode
    global button_back2
    
    global button_clear
    global button_go
    global button_norm
    global entry_path
    global background_label
    global filename3


    # Hide the text and picture buttons when the image mode is active
    button_text.place(x=900.0, y=238.0, width=112.0, height=43)
    button_picture.place(x=900.0, y=238.0, width=112.0, height=43.0)  # Hide the button
    entry_path.place(x=30.0, y=215.0, width=302.0, height=21.0)
    # Set the background image for image mode
    background_label.configure(image=filename3)

    # Place the buttons and entries for image mode
    button_encrypt.place(x=34.0, y=284.0, width=77.0, height=33)
    button_decrypt.place(x=139.0, y=284.0, width=77.0, height=33)
    button_choose.place(x=125.0, y=140.0, width=102.0, height=43)
    button_clear2.place(x=249.0, y=284.0, width=77.0, height=33)
    button_back2.place(x=566.0, y=340.0, width=59.0, height=25)

# def select_image_file():
#     file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
#     return file_path

def save_encrypted_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])
    return file_path

def save_decrypted_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])
    return file_path

def encrypt_action():
    global image_path
    global entry_path
    
    if image_path:
        encrypt_image(image_path)
        entry_path.delete(0, tk.END)
        entry_path.insert(tk.END, f"Encrypted image was saved")

def decrypt_action():
    global image_path
    global entry_path
    
    if image_path:
        encrypt_image(image_path)
        entry_path.delete(0, tk.END)
        entry_path.insert(tk.END, f"Decrypted image was saved")

def choose():
    global image_path
    global entry_path

    # filename = filedialog.askopenfilename()
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    image_path = filename
    entry_path.delete(0, tk.END)
    entry_path.insert(tk.END, filename)

	
	




# Configure encryption and decryption buttons
button_encrypt_img = PhotoImage(file=script_dir / "assets/encrypt.png")
button_decrypt_img = PhotoImage(file=script_dir / "assets/decrypt.png")
button_choose_img = PhotoImage(file=script_dir / "assets/choosee.png")
button_clear2_img = PhotoImage(file=script_dir / "assets/clear2.png")
button_back2_img= PhotoImage(file=script_dir / "assets/back2.png")

button_encrypt = Button(image=button_encrypt_img, borderwidth=0, highlightthickness=0, command=lambda: encrypt_action(), relief="flat")
button_decrypt = Button(image=button_decrypt_img, borderwidth=0, highlightthickness=0, command=lambda: decrypt_action(), relief="flat")
button_choose = Button(image=button_choose_img, borderwidth=0, highlightthickness=0, command=lambda: choose(), relief="flat")
button_clear2 = Button(image=button_clear2_img,borderwidth=0,highlightthickness=0,command=lambda: clear2(),relief="flat")
button_back2 = Button(image=button_back2_img,borderwidth=0,highlightthickness=0,command=lambda: home(),relief="flat")


###

button_text_img= PhotoImage(file=script_dir / "assets/text1.png")
button_picture_img = PhotoImage(file=script_dir / "assets/image.png")

button_picture = Button(image=button_picture_img,borderwidth=0,highlightthickness=0,command=lambda: image(),relief="flat")
button_text = Button(image=button_text_img,borderwidth=0,highlightthickness=0,command=lambda: text(),relief="flat")

button_go_img= PhotoImage(file=script_dir / "assets/start.png")
button_norm_img = PhotoImage(file=script_dir / "assets/norm.png")
button_encode_img= PhotoImage(file=script_dir / "assets/encode.png")
button_clear_img = PhotoImage(file=script_dir / "assets/clear.png")
button_back_img= PhotoImage(file=script_dir / "assets/back.png")

button_go = Button(image=button_go_img,borderwidth=0,highlightthickness=0,command=lambda: start(),relief="flat")
button_norm = Button(image=button_norm_img,borderwidth=0,highlightthickness=0,command=lambda: copy_n(),relief="flat")
button_encode = Button(image=button_encode_img,borderwidth=0,highlightthickness=0,command=lambda: copy_e(),relief="flat")
button_clear = Button(image=button_clear_img,borderwidth=0,highlightthickness=0,command=lambda: clear(),relief="flat")
button_back = Button(image=button_back_img,borderwidth=0,highlightthickness=0,command=lambda: home(),relief="flat")
###
button_picture = Button(image=button_picture_img, borderwidth=0, highlightthickness=0, command=lambda: image(), relief="flat")
###

entry_n = Entry(font = "Calibri 15 bold", fg="#013c3c", bd=0, bg="#ffffff", highlightthickness=0)
entry_e = Entry(font = "Calibri 15 bold", fg="#013c3c", bd=0, bg="#ffffff", highlightthickness=0)
entry_path = Entry(font = "Calibri 15 bold", fg="#013c3c", bd=0, bg="#ffffff", highlightthickness=0)

home()
root.resizable(False, False)
root.mainloop()
