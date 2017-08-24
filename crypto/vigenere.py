#! /usr/bin/env python
""" An even cooler encryption algorithm. """
import string
from helpers import alphabet_position, rotate_character
from sys import argv

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
    if len(argv) <= 1 or not argv[1].isalpha():
        print('''
usage: python vigenere.py keyword
Arguments:
-keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.
''')
        exit()
    # elif not argv[1].isalpha():
    #     print("ERROR: arg must be word")
    #     exit()
    else:
        rot = argv[1]
    message = input("Type a message: \n")
    # key = input("Encryption key: \n")
    key = argv[1]
    print(encrypt(message, key))

if __name__ == "__main__":
    main()
