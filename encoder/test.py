import numpy as np
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
input_string = "7 7 1 2 17 20 33 38 104 166 1 2 "
matrix1, matrix2 = string_to_matrices(input_string)

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
