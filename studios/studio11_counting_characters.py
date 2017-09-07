def counting(text):
    letters = {}
    for char in text:
        number = text.count(char)
        letters[char] = number
    return letters

def main():
    text = "Lorem ipsum"


if __name__ == "__main__":
    main()