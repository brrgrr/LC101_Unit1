def alphabet_position(letter):
    if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter)-97
    elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter)-65
    else:
        pass

def rotate_character(char,rot):
    if (ord(char) >= 97) and (ord(char) <= 122):
        return chr(97+(alphabet_position(char)+rot)%26)
    elif (ord(char) >= 65) and (ord(char) <=90):
        return chr(65+(alphabet_position(char)+rot)%26)
    else:
        return char

def encrypt(text, key):
    encrypted = []
    key_int = 0
    rot_char = ord(key[key_int])
    for char in text:
        if char.isalpha():
            encrypted.append(rotate_character(char, rot_char))
            key_int += 1

        else:
            encrypted.append(char)
    return ''.join(encrypted)

def main():
    text = "aBCd" #input("Enter some text: ")
    key = "a" #input("Enter a keyword: ")
    print(encrypt(text, key))

if __name__ == "__main__":
    main()