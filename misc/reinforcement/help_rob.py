alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    letter = letter.lower()
    alpha_index = alphabet.find(letter)
    return alpha_index


def rotate_character(char, rot):
    if char.isalpha():
        rot_index = (alphabet_position(char) + rot) % 26
        new_char = alphabet[rot_index]
        if char.isupper():
            return new_char.upper()
        elif char.islower():
            return new_char
    else:
        return char


def encrypt(message, cipher):
    encrypted_str = ''
    key_index = 0
    for char in message:
        if char.isalpha():
            key_index = key_index % len(cipher)
            rot = alphabet_position(cipher[key_index])
            encrypted_str += rotate_character(char, rot)
            key_index += 1
        else:
            encrypted_str += char
    return encrypted_str


def main():
    message = "abcd xyz!"
    cipher = "boom"
    print(encrypt(message, cipher))


if __name__ == "__main__":
    main()
