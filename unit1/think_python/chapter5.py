'''
1. Use the draw_square function we wrote in this chapter to draw the image shown below. Assume each side is 20 units.

(Hint: notice that the turtle has already moved away from the ending point of the last square when the program ends.)
'''
import turtle

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("pink")

    draw_square(alex,20)

    wn.exitonclick()

if __name__ == "__main__":
    main()

'''
2. Write a program to draw this. Assume the innermost square is 20 units per side and each successive square is 20 units bigger, per side, than the one inside it.
'''
import turtle

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("salmon")
    alex.pensize(3)
    magic_number = 20
    number_of_squares = 5

    for i in range(number_of_squares):
        size = magic_number * (i+1)
        draw_square(alex,size)
        alex.up()
        alex.backward(magic_number/2)
        alex.right(90)
        alex.forward(magic_number/2)
        alex.left(90)
        alex.down()


    wn.exitonclick()

if __name__ == "__main__":
    main()


'''
3. Write a non-fruitful function draw_poly(t, sides, side_length) which makes a turtle draw a regular polygon. When called with draw_poly(tess, 8, 50), it will draw a shape like this:
'''
import turtle

def draw_poly(t, sides, side_length):
    """Get turtle t to draw a square with sz side"""

    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("salmon")
    tess.pensize(3)

    draw_poly(tess, 8, 50)


    wn.exitonclick()

if __name__ == "__main__":
    main()

