## Safecrypt
Safecrypt is a tool for encoding and decoding text and images using various encryption methods. This project includes functionalities for encrypting and decrypting text messages with a matrix-based cipher and image files with a bitwise XOR operation using a generated key.

### Features
- **Text Encryption and Decryption**: Uses a matrix-based cipher for encoding and decoding text messages.
- **Image Encryption and Decryption**: Uses a bitwise XOR operation for encoding and decoding images, ensuring secure and reversible transformations.

### Text Encryption and Decryption

![image](https://github.com/shahzodjabbarov/Safecrypt/assets/145886003/f8f5876a-841d-4524-b1f6-d9a49801801d)

#### Functions
1. **generate_key_matrix()**
   - Generates a random 2x2 invertible key matrix.

2. **message_to_matrix(message)**
   - Converts a message into a numeric matrix representation.

3. **matrix_to_message(matrix)**
   - Converts a numeric matrix back into a message.

4. **encode_message(message)**
   - Encodes a message using the generated key matrix and returns the encoded message.

5. **decode_message(encoded_message)**
   - Decodes an encoded message using the same key matrix used for encoding.

#### Usage
```python
message = "We are Group G!"
print("Original message:", message)

encoded = encode_message(message)
print("Encoded message:", encoded)
```

### Image Encryption and Decryption

#### Functions
1. **generate_key(shape, seed=0)**
   - Generates a key for each channel of the image with a specified seed for reproducibility.

2. **encrypt_image(image_path, output_path, key_seed=42)**
   - Encrypts an image file using a generated key and saves the encrypted image to the specified output path.

3. **decrypt_image(encrypted_path, output_path, key_seed=42)**
   - Decrypts an encrypted image file using the same key seed used for encryption and saves the decrypted image to the specified output path.

#### Usage
```python
image_path = 'back.png'  # Replace with the path to your image 
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'

encrypt_image(image_path, encrypted_image_path)
decrypt_image(encrypted_image_path, decrypted_image_path)
```

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/shahzodjabbarov/Safecrypt.git
   cd safecrypt
   ```

2. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Code
To run the text encryption and decryption example:
```sh
python text_encryption.py
```

To run the image encryption and decryption example:
```sh
python image_encryption.py
```

### Notes
- Ensure that the image file paths provided in the code are correct.
- For text encryption, messages are padded to ensure compatibility with the matrix operations.


### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### Contact
For any questions or issues, please open an issue in the repository or contact the project maintainers.

---

Enjoy using Safecrypt for secure and reliable encryption of your text and image data!
