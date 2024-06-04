import streamlit as st
import numpy as np
from PIL import Image
from image_encryption_web import encrypt_image, decrypt_image
from pathlib import Path
from io import BytesIO

# Define character to number mapping
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

# Define number to character mapping
num_to_char = {v: k for k, v in char_to_num.items()}

def string_to_matrices(input_string):
    numbers = list(map(int, input_string.split()))
    matrix1 = np.array([[numbers[0], numbers[-2]], [numbers[1], numbers[-1]]])
    remaining_numbers = numbers[2:-2]
    num_columns = len(remaining_numbers) // 2
    matrix2 = np.array(remaining_numbers).reshape(2, num_columns, order='F')
    return matrix1, matrix2

def message_to_matrix(message):
    numbers = [char_to_num.get(char, 95) for char in message]
    if len(numbers) % 2 != 0:
        numbers.append(char_to_num[' '])
    matrix = np.array(numbers).reshape(-1, 2).T
    return matrix

def generate_invertible_key_matrix():
    n = 2
    while True:
        matrix = np.random.randint(1, 11, size=(n, n))
        det = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
        if det != 0:
            return matrix

def insert_columns(product, key):
    col1 = key[:, 0]
    col2 = key[:, 1]
    result_matrix = np.insert(product, 0, col1, axis=1)
    insert_idx = product.shape[1] + 1
    result_matrix = np.insert(result_matrix, insert_idx, col2, axis=1)
    return result_matrix

def matrix_to_string(matrix):
    flattened = [str(matrix[row][col]) for col in range(len(matrix[0])) for row in range(len(matrix))]
    flattened_str = " ".join(flattened)
    return flattened_str

def encrypt_text(message):
    if len(message) % 2 != 0:
        message += ' '
    key = generate_invertible_key_matrix()
    matrix = message_to_matrix(message)
    product = np.dot(key, matrix)
    result = insert_columns(product, key)
    encoded = matrix_to_string(result)
    return encoded, key

def decrypt_text(encoded):
    matrix1, matrix2 = string_to_matrices(encoded)
    inv_matrix1 = np.linalg.inv(matrix1)
    final = np.dot(inv_matrix1, matrix2)
    rounded_matrix = np.round(final).astype(int)
    result = ''.join(num_to_char[rounded_matrix[row][col]] for col in range(len(rounded_matrix[0])) for row in range(len(rounded_matrix)))
    return result

def read_image(image_path):
    return Image.open(image_path)

def image_to_bytes(image):
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

def main():
    st.title("Encode Decode App")
    mode = st.sidebar.selectbox("Choose Mode", ["Home", "Text", "Image"])

    if mode == "Home":
        st.image("back.png")
        st.write("Choose an option from the sidebar to start encoding or decoding.")
    elif mode == "Text":
        st.image("back2.png")
        normal = st.text_area("Normal Text")
        encoded = st.text_area("Encoded Text")
        
        if st.button("Encrypt"):
            encoded, key = encrypt_text(normal)
            st.write("Encoded Text:")
            st.write(encoded)
            st.write("Key:")
            st.write(key)
        
        if st.button("Decrypt"):
            result = decrypt_text(encoded)
            st.write("Decoded Text:")
            st.write(result)
        
        if st.button("Clear"):
            st.experimental_rerun()
    elif mode == "Image":
        st.image("back3.png")
        action = st.selectbox("Choose Action", ["Encrypt Image", "Decrypt Image"])
        
        if action == "Encrypt Image":
            uploaded_file = st.file_uploader("Choose an image to encrypt...", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
                image_path = Path(uploaded_file.name)
                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                if st.button("Encrypt Image"):
                    encrypted_path = Path(encrypt_image(image_path))
                    encrypted_image = read_image(encrypted_path)
                    st.image(encrypted_image, caption='Encrypted Image.', use_column_width=True)
                    img_byte_arr = image_to_bytes(encrypted_image)
                    st.download_button(
                        label="Download Encrypted Image",
                        data=img_byte_arr,
                        file_name=encrypted_path.name,
                        mime="image/png"
                    )
        
        if action == "Decrypt Image":
            uploaded_file = st.file_uploader("Choose an encrypted image to decrypt...", type=["png"])
            if uploaded_file is not None:
                st.image(uploaded_file, caption='Uploaded Encrypted Image.', use_column_width=True)
                image_path = Path(uploaded_file.name)
                with open(image_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                if st.button("Decrypt Image"):
                    decrypted_path = Path(decrypt_image(image_path))
                    decrypted_image = read_image(decrypted_path)
                    st.image(decrypted_image, caption='Decrypted Image.', use_column_width=True)
                    img_byte_arr = image_to_bytes(decrypted_image)
                    st.download_button(
                        label="Download Decrypted Image",
                        data=img_byte_arr,
                        file_name=decrypted_path.name,
                        mime="image/png"
                    )
        
        if st.button("Clear"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
