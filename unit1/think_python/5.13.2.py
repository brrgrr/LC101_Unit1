'''
Write a program to draw this. Assume the innermost square is 20 units per side and each successive square is 20 units bigger, per side, than the one inside it.
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

