'''
Use the draw_square function we wrote in this chapter to draw the image shown below. Assume each side is 20 units.

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
