import numpy as np
import random
import string

# Define the characters and their two-digit mappings
characters = string.ascii_letters + string.digits + string.punctuation + " "
char_to_code = {char: f"{i:02d}" for i, char in enumerate(characters)}
code_to_char = {v: k for k, v in char_to_code.items()}

# Generate a random 2x2 invertible matrix
def generate_key_matrix():
    while True:
        key_matrix = np.random.randint(0, 10, (2, 2))
        if np.linalg.det(key_matrix) != 0:  # Ensure the matrix is invertible
            return key_matrix

# Convert a message to its numeric matrix representation
def message_to_matrix(message):
    numeric_message = ''.join(char_to_code[char] for char in message)
    matrix = np.array([int(numeric_message[i:i+2]) for i in range(0, len(numeric_message), 2)])
    return matrix.reshape(2, -1)

# Convert a numeric matrix back to a message
def matrix_to_message(matrix):
    numeric_message = ''.join(f"{num:02d}" for num in matrix.flatten())
    return ''.join(code_to_char[numeric_message[i:i+2]] for i in range(0, len(numeric_message), 2))

# Encode a message
def encode_message(message):
    message_matrix = message_to_matrix(message)
    key_matrix = generate_key_matrix()
    encoded_matrix = np.dot(key_matrix, message_matrix) % 100
    encoded_message = matrix_to_message(encoded_matrix)
    key_str = ''.join(f"{num:02d}" for num in key_matrix.flatten())
    return key_str[:2] + encoded_message + key_str[2:]

# Decode a message
def decode_message(encoded_message):
    key_str = encoded_message[:2] + encoded_message[-2:]
    key_matrix = np.array([int(key_str[i:i+2]) for i in range(0, len(key_str), 2)]).reshape(2, 2)
    inverse_key_matrix = np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)
    inverse_key_matrix = np.round(inverse_key_matrix).astype(int) % 100
    
    encoded_message_body = encoded_message[2:-2]
    encoded_matrix = message_to_matrix(encoded_message_body)
    
    decoded_matrix = np.dot(inverse_key_matrix, encoded_matrix) % 100
    return matrix_to_message(decoded_matrix)

# Example usage
message = "i love you"
print("Original message:", message)

encoded = encode_message(message)
print("Encoded message:", encoded)

decoded = decode_message(encoded)
print("Decoded message:", decoded)
