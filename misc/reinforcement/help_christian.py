from sys import argv
import string


def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in letter:
        if char.isalpha():
            lower_char = char.lower()
            alphabet_index = alphabet.index(lower_char)
    return alphabet_index


def rotate_character(char, rot):
    # encrypted = ' '
    # for letter in char:
    if not char.isalpha():
        # encrypted += char
        return char  # encrypted
    else:
        rot_index = (alphabet_position(char) + rot) % 26
        return string.ascii_lowercase[rot_index]


print(rotate_character(argv[1], int(argv[2])))
