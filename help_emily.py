import string

def alphabet_position(letter):
    return string.ascii_letters.find(letter) % 26

def rotate_character(char, rot):
    i = (alphabet_position(char) + rot) % 26
    if not char.isalpha():
        return char
    else:
        if char.isupper():
            return string.ascii_uppercase[i]
        elif char.islower():
            return string.ascii_lowercase[i]

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted = encrypted + rotate_character(char, rot)
    return encrypted

def main():
    print(alphabet_position('L'))
    print(rotate_character('Z', 2))
    print(encrypt('abcde', 3))
    print(encrypt('nopqr', 8))


if __name__ == "__main__":
    main()
