def is_sorted(string):
    """Returns True if string is sorted from least to greatest
       False otherwise.
    """
    base_char = ''
    for char in string:
        if base_char > char:
            return False
        else:
            base_char = char
    return True


def main():
    print("ABC", is_sorted("ABC"))
    print("aBc", is_sorted("aBc"))
    print("dog", is_sorted("dog"))


if __name__ == '__main__':
    main()
