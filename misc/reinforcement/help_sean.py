def alphabet_position(letter):
    temp = letter.lower()
    value = ord(temp)
    pos_num = value - 97
    return pos_num


def rotate_character(char, rot):
    new_pos = (alphabet_position(char) + rot) % 26
    if char.isupper():
        temp = chr(new_pos + 65)
        return temp.upper()
    elif char.isalpha():
        return chr(new_pos + 97)
    else:
        return char


def encrypt(text, rot):
    words = ''
    for letters in text:
        count = 1
        while count <= len(text):
            words += str(rotate_character(text[count - 1], rot))
            count += 1
    return words


def main():
    text = input("What would you like encrypted?")
    key = input("How many character rotations would you like?")
    text = str(text)
    key = int(key)
    rot_text = encrypt(text, key)
    print(rot_text)


if __name__ == "__main__":
    main()
