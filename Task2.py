from PIL import Image
import numpy as np
import getpass
import os

def encrypt(image_path, key):
    img = Image.open(image_path)
    arr = np.array(img)
    k = sum(bytearray(key.encode())) % 256
    encrypted = (arr + k) ^ k
    Image.fromarray(encrypted.astype(np.uint8)).save("encrypted_" + image_path)
    print("Encrypted image saved as encrypted_" + image_path)

def decrypt(image_path, key):
    img = Image.open(image_path)
    arr = np.array(img)
    k = sum(bytearray(key.encode())) % 256
    decrypted = (arr ^ k) - k
    Image.fromarray(decrypted.astype(np.uint8)).save("decrypted_" + image_path)
    print("Decrypted image saved as decrypted_" + image_path)

choice = input("Enter E for Encrypt or D for Decrypt: ").upper()
image_name = input("Enter image file name (with extension): ")

if not os.path.exists(image_name):
    print("Image file not found")
    exit()

key = getpass.getpass("Enter secret key: ")

if choice == "E":
    encrypt(image_name, key)
elif choice == "D":
    decrypt(image_name, key)
else:
    print("Invalid choice")
