#1
'''
Farmer takes the chicken across the river, and returns alone.
Next, the farmer takes the fox across the river, and returns with the chicken.
Then, the farmer take the corn, and returns alone.
Finally, farmer takes the chicken across the river.
'''

#2
'''
Ask for an item from the box labeled for containing both. That will show you the correct label for that box. From there it's process of elimination.
'''

#3
'''
Number the boxes 1-10 and take the corresponding number of balls for each box.
Weight the new set of balls.
Subtract the total weight of those from 550 (weight if all were normal)
Difference will correspond to the number of the defective box.
'''

#4
def some_function():
    # Imagine code that could raise value or unicode errors
    pass

def main():
    # Put your exception handling code below
    try:
        some_function()
    except UnicodeError:
        print("unicode error happening now")
    except ValueError:
        print("value error happening now")

if __name__ == "__main__":
    main()


#5
def line(n):
    line_str = ''
    for i in range(n):
        line_str += "#"

    return line_str

def main():
    print(line(5))

if __name__ == "__main__":
    main()


#6
def line(n):
    line_str = ''
    for i in range(n):
        line_str += '#'

    return line_str

def square(n):
    square_str = ''
    for i in range(n):
        square_str += (line(n) + '\n')

    return square_str

def main():
    print(square(5))

if __name__ == "__main__":
    main()

#7
def line(n):
    line_str = ''
    for i in range(n):
        line_str += '#'

    return line_str

def rectangle(width, height):
    rectangle_str = ''
    for i in range(height):
        rectangle_str += (line(width) + '\n')

    return rectangle_str

def main():
    print(rectangle(5, 3))

if __name__ == "__main__":
    main()

#8
def line(n):
    line_str = ''
    for i in range(n):
        line_str += '#'

    return line_str

def stairs(n):
    stairs_str = ''
    for i in range(n):
        stairs_str += (line(i+1) + '\n')

    return stairs_str

def main():
    print(stairs(5))

if __name__ == "__main__":
    main()

#9
def space_line(spaces, hashes):
    return (spaces * ' '+ hashes * '#')

def main():
    print(space_line(3,5))

if __name__ == "__main__":
    main()

#10
def space_line(spaces, hashes):
    return (spaces * ' '+ hashes * '#')

def triangle(n):
    triangle_str = ''
    for i in range(n):
        triangle_str +=  (space_line(n-i-1, 2*i+1) + '\n')
    return triangle_str

def main():
    print(triangle(5))

if __name__ == "__main__":
    main()

#11
def space_line(spaces, hashes):
    return (spaces * ' '+ hashes * '#')

def triangle(n):
    triangle_str = ''
    for i in range(n):
        triangle_str +=  (space_line(n-i-1, 2*i+1) + '\n')
    return triangle_str

def diamond(n):
    diamond_str = triangle(5)
    for i in range(n-2,-1,-1):
        diamond_str +=  (space_line(n-i-1, 2*i+1) + '\n')
    return diamond_str

def main():
    print(diamond(5))

if __name__ == "__main__":
    main()

