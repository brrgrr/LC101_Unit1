#1
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

    for i in range(5):
        draw_square(alex,20)
        alex.up()
        alex.forward(40)
        alex.down()

    wn.exitonclick()

if __name__ == "__main__":
    main()

#2
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


#3
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

#4
import turtle
import sys

sys.setExecutionLimit(35000)

def draw_spiral(t, angle):
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2
    t.stamp()                      #show final position

def main(): 
    #create and configure screen 
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    #create and configure turtle
    axl = turtle.Turtle()
    axl.color('blue')
    axl.pensize(2)
    axl.speed(0)
    axl.ht()

    #adjust for first spiral
    axl.penup()
    axl.backward(105)
    axl.pendown()

    
    # squared spiral
    draw_spiral(axl, 90) 
      
    #adjust for second spiral 
    axl.penup()
    axl.home()
    axl.forward(95)
    axl.pendown()

     # twisted spiral
    draw_spiral(axl, 88.75)    

if __name__ == "__main__":
    main()

#5
import turtle

def draw_poly(t, sides, side_length):
    ''' Draw polygon '''

    for i in range(sides):
        t.forward(side_length)
        t.left(360/sides)
        
def draw_equi_triangle(turtle, size):
    draw_poly(turtle, 3, size)
        
def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("salmon")
    tess.pensize(3)

    draw_equi_triangle(tess, 100)
    
    wn.exitonclick()

if __name__ == "__main__":
    main()


#6
def sum_to(n):
    # your code here
     return int((n * (n + 1)) / 2)

print(sum_to(10))

#7
import turtle

def draw_star(t):
    ''' Draw star '''

    for i in range(5):
        t.forward(100)
        t.right(144)
        
def main():
    wn = turtle.Screen()
    wn.bgcolor('white')

    axl = turtle.Turtle()
    axl.color('black')
    axl.pensize(3)
    axl.speed(0)
    axl.ht()
    axl.up()
    axl.backward(50)
    axl.down()
    draw_star(axl)
    
    wn.exitonclick()

if __name__ == "__main__":
    main()


#8
import turtle

def draw_star(t):
    ''' Draw star '''
    for i in range(5):
        t.forward(100)
        t.right(144)
   
def draw_stars(t):
    
    for i in range(5):
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()
        draw_star(t)
        
def main():
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')

    axl = turtle.Turtle()
    axl.color('salmon')
    axl.pensize(3)
    axl.speed(0)
    
    axl.penup()
    axl.right(15)
    axl.backward(175)
    axl.left(15)
    axl.pendown()

    draw_stars(axl)   

    wn.exitonclick()

if __name__ == "__main__":
    main()


#9
import turtle

def draw_star(t):
    ''' Draw star '''
    for i in range(5):
        t.forward(100)
        t.right(144)
   
def draw_stars(t):
    
    for i in range(5):
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()
        draw_star(t)
        
def main():
    wn = turtle.Screen()
    wn.bgcolor('lightgreen')

    axl = turtle.Turtle()
    axl.color('salmon')
    axl.pensize(3)
    axl.speed(0)
    
    axl.penup()
    axl.right(15)
    axl.backward(175)
    axl.left(15)
    axl.pendown()

    draw_stars(axl)   

    wn.exitonclick()

if __name__ == "__main__":
    main()


#10
import turtle

def draw_sprite(t, legs, leg_length):
    ''' Draw sprite '''
    angle = 360/legs

    for i in range(legs):
        t.forward(leg_length)
        t.dot()
        t.backward(leg_length)
        t.left(angle)

def main():
    wn = turtle.Screen()
    wn.bgcolor('white')

    axl = turtle.Turtle()
    axl.color('black')
    axl.pensize(3)
    axl.speed(0)
    axl.ht()

    draw_sprite(axl, 15, 120)

    wn.exitonclick()

if __name__ == "__main__":
    main()


#11
def sum_to(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def main():
    test_value = int(input("What is the test value for n?"))
    result=sum_to(test_value)
    print("The sum of all integer numbers up to (and including)", test_value, "is", result)
    
if __name__ == "__main__":
    main()


#12
import turtle
import math

def draw_sprite(t, legs, leg_length):
    ''' Draw sprite '''
    angle = 360 / legs
    for i in range(legs):
        t.forward(leg_length)
        #t.dot()
        t.backward(leg_length)
        t.left(angle)

def fancy_square(t, legs, size):
    '''Draw square with a sprite at each corner'''
	
	# center the square
    t.penup()
    t.left(45)
    t.backward(math.hypot( size/2, size/2 ))
    t.right(45)
    t.pendown()
    
    # draw the square
    for i in range(4):
        t.forward(size)
        t.left(90)
        draw_sprite(t, legs, size//4)
        
def main():
    wn = turtle.Screen()
    wn.bgcolor('white')

    axl = turtle.Turtle()
    axl.color('black')
    axl.pensize(3)
    axl.speed(0)
    axl.ht()

    fancy_square(axl, 15, 120)

    wn.exitonclick()

if __name__ == "__main__":
    main()

#Weekly Graded Assignment
import math
def area_of_circle(r):
    return math.pi * (r * r)

# Below are some tests which can give you an indication that your code seems to be correct.

# IMPORTANT: You should NOT include this part when you submit in Vocareum.
# When you submit, only include the function above.
from test import testEqual

t = area_of_circle(0)
testEqual(t, 0)
t = area_of_circle(1)
testEqual(t,math.pi)
t = area_of_circle(100)
testEqual(t, 31415.926535897932)
t = area_of_circle(-1)
testEqual(t, math.pi)
t = area_of_circle(-5)
testEqual(t, 25 * math.pi)
t = area_of_circle(2.3)
testEqual(t, 16.61902513749)
