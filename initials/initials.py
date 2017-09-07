def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    name_list = fullname.split()
    initials = ""
    for name in name_list:
        initials += name[0]
    return initials.upper()

def main():
    fullname = input("What is your full name?")
    print(get_initials(fullname))

if __name__ == '__main__':
    main()
