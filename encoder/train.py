import numpy as np
import random

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

def message_to_matrix(message):
    # Convert message characters to their assigned numbers
    numbers = [char_to_num.get(char, 95) for char in message]  # Return 95 for unknown characters
    
    # Pad the message with space if necessary to make its length even
    if len(numbers) % 2 != 0:
        numbers.append(char_to_num[' '])
    
    # Reshape the numbers into a 2xN matrix
    matrix = np.array(numbers).reshape(2, -1)
    
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



def flatten_matrix(matrix):
    flattened = []
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            flattened.append(matrix[row][col])
    flattened_str = "".join(map(lambda x: str(x) + " ", flattened))
    return flattened_str



message = input("Enter the message to encode: ").lower()
if len(message) % 2 != 0:
    message += ' '

key = generate_invertible_key_matrix()
matrix = message_to_matrix(message)
product = multiply(key, matrix)
result = insert_columns(product, key)
result_string = flatten_matrix(result)

print(key)
print(matrix)
print(product)
print(result)
print(result_string)

'''def encode_message(message, key_matrix):
    message_matrix = message_to_matrix(message)
    encoded_matrix = np.dot(key_matrix, message_matrix) % 27  # Adjusted for space
    return encoded_matrix


def decode_message(encoded_matrix, key_matrix):
    # Calculate the modular inverse of the key matrix
    det = int(np.round(np.linalg.det(key_matrix))) % 27
    det_inv = pow(det, -1, 27)
    adjugate = np.array([[key_matrix[1, 1], -key_matrix[0, 1]], [-key_matrix[1, 0], key_matrix[0, 0]]])
    key_matrix_inv = (det_inv * adjugate) % 27
    
    decoded_matrix = np.dot(key_matrix_inv, encoded_matrix) % 27
    decoded_matrix = np.round(decoded_matrix).astype(int) % 27  # Ensure values are integers within the range
    return decoded_matrix'''
