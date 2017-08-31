def run_command(i_list, c_list):
    if c_list[0] == "insert":
        i_list.insert(int(c_list[1]), int(c_list[2]))
    elif c_list[0] == "print":
        print(i_list)
    elif c_list[0] == "remove":
        i_list.remove(int(c_list[1]))
    elif c_list[0] == "append":
        i_list.append(int(c_list[1]))
    elif c_list[0] == "sort":
        i_list.sort()
    elif c_list[0] == "pop":
        i_list.pop()
    elif c_list[0] == "reverse":
        i_list.reverse()
    else:
        print(c_list)
    return i_list


def main():
    a_list = []
    num = int(input())

    for _ in range(num):
        command = input()
        c_list = command.split()
        run_command(a_list, c_list)


if __name__ == '__main__':
    main()
