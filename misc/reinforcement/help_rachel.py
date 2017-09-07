def alphabet_position(letter):
    letter_pos = ""
    for char in letter:
        if char.islower():
            pos = ord(char)
            letter_pos += str(pos - 97)
        elif char.isupper():
            pos = ord(char)
            letter_pos += str(pos - 65)
        else:
            letter_pos += char
    return letter_pos

def rotate_character(message, rot):
    if message.isalpha():
        shift = (int(alphabet_position(message)) + rot) % 26
        return shift
    else:
        return message

def encrypt_c(text, rot):
    encrypt = ""
    for char in text:
        new_char = rotate_character(char, rot)
        if char.islower():
            new_char = chr(new_char + 97)
            encrypt += new_char
        elif char.isupper():
            new_char = chr(new_char + 65)
            encrypt += new_char
        else:
            encrypt += new_char
    return encrypt

def encrypt_v(text, key):
    encrypt = ""
    key_length = len(key)
    key_pos = []
    for char in key:
        key_pos += alphabet_position(char)
    print(key_pos)
    return encrypt


print(encrypt("abc", 1))
