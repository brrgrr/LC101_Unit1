'''
Write a non-fruitful function draw_poly(t, sides, side_length) which makes a turtle draw a regular polygon. When called with draw_poly(tess, 8, 50), it will draw a shape like this:
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
