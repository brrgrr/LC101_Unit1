#! /usr/bin/env python
""" Helper functions for crypto. """
import string

def alphabet_position(letter):
    """ returns the 0-based numerical position of the letter within the alphabet """
    return string.ascii_letters.find(letter) % 26

def rotate_character(char, rot):
    """ return new char rotated by given number """
    if not char.isalpha():
        return char
    else:
        rotated_index = (alphabet_position(char) + int(rot)) % 26
        if char.isupper():
            return string.ascii_uppercase[rotated_index]
        elif char.islower():
            return string.ascii_lowercase[rotated_index]
