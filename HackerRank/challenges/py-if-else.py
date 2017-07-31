if __name__ == '__main__':
    n = int(input())

    if n % 2 == 1: #odd
        print("Weird")
    else: #even
        if 2 <= n <= 5:
			#even and in the inclusive range of 2 to 5
            print("Not Weird")
        elif 6 <= n <= 20:
			#even and in the inclusive range of 6 to 20
            print("Weird")
        if n > 20:
			#even and greater than 20
            print("Not Weird")
            