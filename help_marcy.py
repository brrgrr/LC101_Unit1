alpha_lower = "abcdefghijklmnopqrstuvwxyz"
alpha_upper = alpha_lower.upper()
def alphabet_position(letter):
    if letter.islower():
        pos = alpha_lower.index(letter)
    else:
        pos = alpha_upper.index(letter)
    return pos
def rotate_character(char, rot):
    if char.isalpha():
        if char.islower():
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                new_char = alpha_lower[rotated_index]
            else:
                new_char = alpha_lower[rotated_index % 26]
            return new_char
        else:
            rotated_index = alphabet_position(char) + rot
            if rotated_index < 26:
                new_char = alpha_upper[rotated_index]
            else:
                new_char = alpha_upper[rotated_index % 26]
            return new_char
    else:
        return char
def encrypt(text, rot):
    encrypted = ''
    for char in text:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            encrypted = encrypted = encrypted + rotate_character(char, rot)
    return encrypted
def main():
    text = input("Type a message: ")
    rot = int(input("Rotate by: "))
    print(encrypt(text, rot))
if __name__ == "__main__":
    main()