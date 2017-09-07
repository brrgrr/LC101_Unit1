'''
from helpers import alphabet_position, rotate_character
'''
import string


def alphabet_position(letter):
    return ord(letter)


def rotate_character(char, rot):
    encoded = ""
    # loop over characters for ord
    char_ord = alphabet_position(char)
    # non-alphabet characters
    if (char_ord > 90 and char_ord < 97) or char_ord < 65 or char_ord > 122:
        encoded = encoded + char
        return encoded
    else:
        # set each according to whether upper or lower case
        # ord of "Z" is 90, so 91 for upper range and ord of "A" is 65 so uppercase boundary
        if char.isupper():
            asciirange = 91
            asciibound = 65
        else:
            # ord of "z" is 122 so 123 for upper range and ord of "a" is 97 so lowercase boundary
            asciirange = 123
            asciibound = 97

    enc_char = ((char_ord + rot) % asciirange)
    print(enc_char)
    if enc_char < asciibound:
        enc_char = (enc_char + asciibound)
        encoded = encoded + (chr(enc_char))
    else:
        encoded = encoded + (chr(enc_char))
    return encoded


def encrypt(text, keyword):
    encoded_text = ""
    key_start = 0
    # find rot
    alpha = string.ascii_letters
    for char in text:
        # check if character is a letter
        if char.isalpha():
            key_num = (alphabet_position(keyword[key_start]))
            # convert key_num to a letter to find index
            rot = alpha.find(chr(key_num))
            encoded_text += (rotate_character(char, rot))
            if key_start == (len(keyword) - 1):
                key_start = 0
            else:
                key_start += 1
        else:
            encoded_text += char
    return encoded_text


def main():
    text = input("Type a message:")
    keyword = input("Encryption keyword:")
    print(alphabet_position("z"))
    print(alphabet_position("Z"))

    print(encrypt(text, keyword))


if __name__ == "__main__":
    main()
