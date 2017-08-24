#! /usr/bin/env python
""" An encryption algorithm. """
import string
from helpers import alphabet_position, rotate_character
from sys import argv, exit


def encrypt(text, rot):
    """ return the result of rotating each letter in the text by rot places to the right """
    return ''.join([rotate_character(char, rot) for char in text])


def main():
    """ main """
    if len(argv) <= 1 or not argv[1].isdigit():
        print("\n\tusage: python caesar.py n")
        exit()
    else:
        rot = argv[1]
    message = input("Type a message: \n")
    # rot = input("Rotate by: \n")

    print(encrypt(message, rot))


if __name__ == "__main__":
    main()
