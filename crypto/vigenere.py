#! /usr/bin/env python
""" An even cooler encryption algorithm. """
import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    """ return the result of rotating each letter in the text by rot places to the right based on key """
    encrypted = ""
    key_pos = 0
    for char in text:
        key_pos = key_pos % len(key)
        if not char.isalpha():
            rot = 0
            new_char = rotate_character(char, rot)
        else:
            rot = alphabet_position(key[key_pos])
            new_char = rotate_character(char, rot)
            key_pos += 1
        encrypted += new_char
    return encrypted

def main():
    """ main """
    message = input("Type a message: \n")
    key = input("Encryption key: \n")
    print(encrypt(message, key))

if __name__ == "__main__":
    main()
